""" Cisco_IOS_XR_man_ipsla_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ipsla package configuration.

This module contains definitions
for the following management objects\:
  ipsla\: IPSLA configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpslaHistoryFilter(Enum):
    """
    IpslaHistoryFilter (Enum Class)

    Ipsla history filter

    .. data:: failed = 2

    	Store data for failed operations

    .. data:: all = 255

    	Store data for all operations

    """

    failed = Enum.YLeaf(2, "failed")

    all = Enum.YLeaf(255, "all")


class IpslaLife(Enum):
    """
    IpslaLife (Enum Class)

    Ipsla life

    .. data:: forever = 0

    	Schedule operation to run forever

    """

    forever = Enum.YLeaf(0, "forever")


class IpslaLspMonitorReplyMode(Enum):
    """
    IpslaLspMonitorReplyMode (Enum Class)

    Ipsla lsp monitor reply mode

    .. data:: ipv4_udp_router_alert = 3

    	Send replies via IPv4 UDP packets with Router

    	Alert option

    """

    ipv4_udp_router_alert = Enum.YLeaf(3, "ipv4-udp-router-alert")


class IpslaLspMonitorThresholdTypes(Enum):
    """
    IpslaLspMonitorThresholdTypes (Enum Class)

    Ipsla lsp monitor threshold types

    .. data:: immediate = 2

    	Take action immediately after threshold is

    	violated

    .. data:: consecutive = 3

    	Take action after N consecutive threshold

    	violations

    """

    immediate = Enum.YLeaf(2, "immediate")

    consecutive = Enum.YLeaf(3, "consecutive")


class IpslaLspPingReplyMode(Enum):
    """
    IpslaLspPingReplyMode (Enum Class)

    Ipsla lsp ping reply mode

    .. data:: ipv4_udp_router_alert = 3

    	Send replies via IPv4 UDP packets with Router

    	Alert option

    .. data:: control_channel = 4

    	Send replies via a Control Channel option

    """

    ipv4_udp_router_alert = Enum.YLeaf(3, "ipv4-udp-router-alert")

    control_channel = Enum.YLeaf(4, "control-channel")


class IpslaLspReplyDscp(Enum):
    """
    IpslaLspReplyDscp (Enum Class)

    Ipsla lsp reply dscp

    .. data:: default = 0

    	Match packets with default dscp (000000)

    .. data:: af11 = 10

    	Match packets with AF11 dscp (001010)

    .. data:: af12 = 12

    	Match packets with AF12 dscp (001100)

    .. data:: af13 = 14

    	Match packets with AF13 dscp (001110)

    .. data:: af21 = 18

    	Match packets with AF21 dscp (010010)

    .. data:: af22 = 20

    	Match packets with AF22 dscp (010100)

    .. data:: af23 = 22

    	Match packets with AF23 dscp (010110)

    .. data:: af31 = 26

    	Match packets with AF31 dscp (011010)

    .. data:: af32 = 28

    	Match packets with AF32 dscp (011100)

    .. data:: af33 = 30

    	Match packets with AF33 dscp (011110)

    .. data:: af41 = 34

    	Match packets with AF41 dscp (100010)

    .. data:: af42 = 36

    	Match packets with AF42 dscp (100100)

    .. data:: af43 = 38

    	Match packets with AF43 dscp (100110)

    .. data:: cs1 = 8

    	Match packets with CS1(precedence 1) dscp

    	(001000)

    .. data:: cs2 = 16

    	Match packets with CS2(precedence 2) dscp

    	(010000)

    .. data:: cs3 = 24

    	Match packets with CS3(precedence 3) dscp

    	(011000)

    .. data:: cs4 = 32

    	Match packets with CS4(precedence 4) dscp

    	(100000)

    .. data:: cs5 = 40

    	Match packets with CS5(precedence 5) dscp

    	(101000)

    .. data:: cs6 = 48

    	Match packets with CS6(precedence 6) dscp

    	(110000)

    .. data:: cs7 = 56

    	Match packets with CS7(precedence 7) dscp

    	(111000)

    .. data:: ef = 46

    	Match packets with EF dscp (101110)

    """

    default = Enum.YLeaf(0, "default")

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")

    ef = Enum.YLeaf(46, "ef")


class IpslaLspTraceReplyMode(Enum):
    """
    IpslaLspTraceReplyMode (Enum Class)

    Ipsla lsp trace reply mode

    .. data:: ipv4_udp_router_alert = 3

    	Send replies via IPv4 UDP packets with Router

    	Alert option

    """

    ipv4_udp_router_alert = Enum.YLeaf(3, "ipv4-udp-router-alert")


class IpslaMonth(Enum):
    """
    IpslaMonth (Enum Class)

    Ipsla month

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


class IpslaSched(Enum):
    """
    IpslaSched (Enum Class)

    Ipsla sched

    .. data:: pending = 1

    	Schedule pending for later time

    .. data:: now = 2

    	Schedule operation now

    .. data:: after = 3

    	Schedule operation after specifed duration

    .. data:: at = 4

    	Schedule operation at specified time

    """

    pending = Enum.YLeaf(1, "pending")

    now = Enum.YLeaf(2, "now")

    after = Enum.YLeaf(3, "after")

    at = Enum.YLeaf(4, "at")


class IpslaSecondaryFrequency(Enum):
    """
    IpslaSecondaryFrequency (Enum Class)

    Ipsla secondary frequency

    .. data:: connection_loss = 1

    	Enable secondary frequency for connection loss

    .. data:: timeout = 2

    	Enable secondary frequency for timeout

    .. data:: both = 3

    	Enable secondary frequency for timeout and

    	connection loss

    """

    connection_loss = Enum.YLeaf(1, "connection-loss")

    timeout = Enum.YLeaf(2, "timeout")

    both = Enum.YLeaf(3, "both")


class IpslaThresholdTypes(Enum):
    """
    IpslaThresholdTypes (Enum Class)

    Ipsla threshold types

    .. data:: immediate = 2

    	Take action immediately after threshold is

    	violated

    .. data:: consecutive = 3

    	Take action after N consecutive threshold

    	violations

    .. data:: xof_y = 4

    	Take action after X violations in Y probes

    .. data:: average = 5

    	Take action if average of N probes violates the

    	threshold

    """

    immediate = Enum.YLeaf(2, "immediate")

    consecutive = Enum.YLeaf(3, "consecutive")

    xof_y = Enum.YLeaf(4, "xof-y")

    average = Enum.YLeaf(5, "average")



class Ipsla(Entity):
    """
    IPSLA configuration
    
    .. attribute:: common
    
    	IPSLA application common configuration
    	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Common>`
    
    .. attribute:: mpls_lsp_monitor
    
    	MPLS LSP Monitor(MPLSLM) configuration
    	**type**\:  :py:class:`MplsLspMonitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor>`
    
    .. attribute:: operation_
    
    	IPSLA Operation configuration
    	**type**\:  :py:class:`Operation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation>`
    
    .. attribute:: responder
    
    	Responder configuration
    	**type**\:  :py:class:`Responder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder>`
    
    .. attribute:: mpls_discovery
    
    	Provider Edge(PE) discovery configuration
    	**type**\:  :py:class:`MplsDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsDiscovery>`
    
    .. attribute:: server_twamp
    
    	IPPM Server configuration
    	**type**\:  :py:class:`ServerTwamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.ServerTwamp>`
    
    

    """

    _prefix = 'man-ipsla-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipsla, self).__init__()
        self._top_entity = None

        self.yang_name = "ipsla"
        self.yang_parent_name = "Cisco-IOS-XR-man-ipsla-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("common", ("common", Ipsla.Common)), ("mpls-lsp-monitor", ("mpls_lsp_monitor", Ipsla.MplsLspMonitor)), ("operation", ("operation_", Ipsla.Operation)), ("responder", ("responder", Ipsla.Responder)), ("mpls-discovery", ("mpls_discovery", Ipsla.MplsDiscovery)), ("server-twamp", ("server_twamp", Ipsla.ServerTwamp))])
        self._leafs = OrderedDict()

        self.common = Ipsla.Common()
        self.common.parent = self
        self._children_name_map["common"] = "common"

        self.mpls_lsp_monitor = Ipsla.MplsLspMonitor()
        self.mpls_lsp_monitor.parent = self
        self._children_name_map["mpls_lsp_monitor"] = "mpls-lsp-monitor"

        self.operation_ = Ipsla.Operation()
        self.operation_.parent = self
        self._children_name_map["operation_"] = "operation"

        self.responder = Ipsla.Responder()
        self.responder.parent = self
        self._children_name_map["responder"] = "responder"

        self.mpls_discovery = Ipsla.MplsDiscovery()
        self.mpls_discovery.parent = self
        self._children_name_map["mpls_discovery"] = "mpls-discovery"

        self.server_twamp = Ipsla.ServerTwamp()
        self.server_twamp.parent = self
        self._children_name_map["server_twamp"] = "server-twamp"
        self._segment_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipsla, [], name, value)


    class Common(Entity):
        """
        IPSLA application common configuration
        
        .. attribute:: hardware_timestamp
        
        	Hardware Timestamp configuration
        	**type**\:  :py:class:`HardwareTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Common.HardwareTimestamp>`
        
        .. attribute:: authentication
        
        	Authenticaion configuration
        	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Common.Authentication>`
        
        .. attribute:: low_memory
        
        	Configure low memory water mark (default 20M)
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**default value**\: 20480
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.Common, self).__init__()

            self.yang_name = "common"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hardware-timestamp", ("hardware_timestamp", Ipsla.Common.HardwareTimestamp)), ("authentication", ("authentication", Ipsla.Common.Authentication))])
            self._leafs = OrderedDict([
                ('low_memory', (YLeaf(YType.uint32, 'low-memory'), ['int'])),
            ])
            self.low_memory = None

            self.hardware_timestamp = Ipsla.Common.HardwareTimestamp()
            self.hardware_timestamp.parent = self
            self._children_name_map["hardware_timestamp"] = "hardware-timestamp"

            self.authentication = Ipsla.Common.Authentication()
            self.authentication.parent = self
            self._children_name_map["authentication"] = "authentication"
            self._segment_path = lambda: "common"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.Common, ['low_memory'], name, value)


        class HardwareTimestamp(Entity):
            """
            Hardware Timestamp configuration
            
            .. attribute:: disable
            
            	states true if hw\-timestamp is disabled
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Common.HardwareTimestamp, self).__init__()

                self.yang_name = "hardware-timestamp"
                self.yang_parent_name = "common"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                ])
                self.disable = None
                self._segment_path = lambda: "hardware-timestamp"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/common/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Common.HardwareTimestamp, ['disable'], name, value)


        class Authentication(Entity):
            """
            Authenticaion configuration
            
            .. attribute:: key_chain
            
            	Use MD5 authentication for IPSLA control message
            	**type**\: str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Common.Authentication, self).__init__()

                self.yang_name = "authentication"
                self.yang_parent_name = "common"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                ])
                self.key_chain = None
                self._segment_path = lambda: "authentication"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/common/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Common.Authentication, ['key_chain'], name, value)


    class MplsLspMonitor(Entity):
        """
        MPLS LSP Monitor(MPLSLM) configuration
        
        .. attribute:: reactions
        
        	MPLSLM Reaction configuration
        	**type**\:  :py:class:`Reactions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions>`
        
        .. attribute:: schedules
        
        	MPLSLM schedule configuration
        	**type**\:  :py:class:`Schedules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Schedules>`
        
        .. attribute:: definitions
        
        	MPLS LSP Monitor definition table
        	**type**\:  :py:class:`Definitions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions>`
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.MplsLspMonitor, self).__init__()

            self.yang_name = "mpls-lsp-monitor"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reactions", ("reactions", Ipsla.MplsLspMonitor.Reactions)), ("schedules", ("schedules", Ipsla.MplsLspMonitor.Schedules)), ("definitions", ("definitions", Ipsla.MplsLspMonitor.Definitions))])
            self._leafs = OrderedDict()

            self.reactions = Ipsla.MplsLspMonitor.Reactions()
            self.reactions.parent = self
            self._children_name_map["reactions"] = "reactions"

            self.schedules = Ipsla.MplsLspMonitor.Schedules()
            self.schedules.parent = self
            self._children_name_map["schedules"] = "schedules"

            self.definitions = Ipsla.MplsLspMonitor.Definitions()
            self.definitions.parent = self
            self._children_name_map["definitions"] = "definitions"
            self._segment_path = lambda: "mpls-lsp-monitor"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.MplsLspMonitor, [], name, value)


        class Reactions(Entity):
            """
            MPLSLM Reaction configuration
            
            .. attribute:: reaction
            
            	Reaction configuration for an MPLSLM instance
            	**type**\: list of  		 :py:class:`Reaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsLspMonitor.Reactions, self).__init__()

                self.yang_name = "reactions"
                self.yang_parent_name = "mpls-lsp-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reaction", ("reaction", Ipsla.MplsLspMonitor.Reactions.Reaction))])
                self._leafs = OrderedDict()

                self.reaction = YList(self)
                self._segment_path = lambda: "reactions"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions, [], name, value)


            class Reaction(Entity):
                """
                Reaction configuration for an MPLSLM instance
                
                .. attribute:: monitor_id  (key)
                
                	Monitor identifier
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: condition
                
                	Reaction condition specification
                	**type**\:  :py:class:`Condition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.MplsLspMonitor.Reactions.Reaction, self).__init__()

                    self.yang_name = "reaction"
                    self.yang_parent_name = "reactions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['monitor_id']
                    self._child_classes = OrderedDict([("condition", ("condition", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition))])
                    self._leafs = OrderedDict([
                        ('monitor_id', (YLeaf(YType.uint32, 'monitor-id'), ['int'])),
                    ])
                    self.monitor_id = None

                    self.condition = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition()
                    self.condition.parent = self
                    self._children_name_map["condition"] = "condition"
                    self._segment_path = lambda: "reaction" + "[monitor-id='" + str(self.monitor_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/reactions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction, ['monitor_id'], name, value)


                class Condition(Entity):
                    """
                    Reaction condition specification
                    
                    .. attribute:: lpd_tree_trace
                    
                    	React on LPD Tree Trace violation for a monitored MPLSLM
                    	**type**\:  :py:class:`LpdTreeTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace>`
                    
                    .. attribute:: timeout
                    
                    	React on probe timeout
                    	**type**\:  :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout>`
                    
                    .. attribute:: lpd_group
                    
                    	React on LPD Group violation for a monitored MPLSLM
                    	**type**\:  :py:class:`LpdGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup>`
                    
                    .. attribute:: connection_loss
                    
                    	React on connection loss for a monitored MPLSLM
                    	**type**\:  :py:class:`ConnectionLoss <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss>`
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition, self).__init__()

                        self.yang_name = "condition"
                        self.yang_parent_name = "reaction"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("lpd-tree-trace", ("lpd_tree_trace", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace)), ("timeout", ("timeout", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout)), ("lpd-group", ("lpd_group", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup)), ("connection-loss", ("connection_loss", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss))])
                        self._leafs = OrderedDict()

                        self.lpd_tree_trace = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace()
                        self.lpd_tree_trace.parent = self
                        self._children_name_map["lpd_tree_trace"] = "lpd-tree-trace"

                        self.timeout = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout()
                        self.timeout.parent = self
                        self._children_name_map["timeout"] = "timeout"

                        self.lpd_group = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup()
                        self.lpd_group.parent = self
                        self._children_name_map["lpd_group"] = "lpd-group"

                        self.connection_loss = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss()
                        self.connection_loss.parent = self
                        self._children_name_map["connection_loss"] = "connection-loss"
                        self._segment_path = lambda: "condition"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition, [], name, value)


                    class LpdTreeTrace(Entity):
                        """
                        React on LPD Tree Trace violation for a
                        monitored MPLSLM
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular MPLSLM
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace, self).__init__()

                            self.yang_name = "lpd-tree-trace"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"
                            self._segment_path = lambda: "lpd-tree-trace"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "lpd-tree-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                ])
                                self.logging = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdTreeTrace.ActionType, ['logging'], name, value)


                    class Timeout(Entity):
                        """
                        React on probe timeout
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular MPLSLM
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout, self).__init__()

                            self.yang_name = "timeout"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType)), ("threshold-type", ("threshold_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "timeout"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "timeout"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                ])
                                self.logging = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ActionType, ['logging'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaLspMonitorThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspMonitorThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for consecutive
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "timeout"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.Timeout.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class LpdGroup(Entity):
                        """
                        React on LPD Group violation for a monitored
                        MPLSLM
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular MPLSLM
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup, self).__init__()

                            self.yang_name = "lpd-group"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"
                            self._segment_path = lambda: "lpd-group"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "lpd-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                ])
                                self.logging = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.LpdGroup.ActionType, ['logging'], name, value)


                    class ConnectionLoss(Entity):
                        """
                        React on connection loss for a monitored
                        MPLSLM
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular MPLSLM
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss, self).__init__()

                            self.yang_name = "connection-loss"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType)), ("threshold-type", ("threshold_type", Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "connection-loss"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "connection-loss"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                ])
                                self.logging = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ActionType, ['logging'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaLspMonitorThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspMonitorThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for consecutive
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "connection-loss"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


        class Schedules(Entity):
            """
            MPLSLM schedule configuration
            
            .. attribute:: schedule
            
            	Schedule an MPLSLM instance
            	**type**\: list of  		 :py:class:`Schedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Schedules.Schedule>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsLspMonitor.Schedules, self).__init__()

                self.yang_name = "schedules"
                self.yang_parent_name = "mpls-lsp-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("schedule", ("schedule", Ipsla.MplsLspMonitor.Schedules.Schedule))])
                self._leafs = OrderedDict()

                self.schedule = YList(self)
                self._segment_path = lambda: "schedules"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsLspMonitor.Schedules, [], name, value)


            class Schedule(Entity):
                """
                Schedule an MPLSLM instance
                
                .. attribute:: monitor_id  (key)
                
                	Monitor indentifier
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: start_time
                
                	Start time of MPLSLM instance
                	**type**\:  :py:class:`StartTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime>`
                
                .. attribute:: frequency
                
                	Group schedule frequency of the probing
                	**type**\: int
                
                	**range:** 1..604800
                
                	**units**\: second
                
                .. attribute:: period
                
                	Group schedule period range
                	**type**\: int
                
                	**range:** 1..604800
                
                	**units**\: second
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.MplsLspMonitor.Schedules.Schedule, self).__init__()

                    self.yang_name = "schedule"
                    self.yang_parent_name = "schedules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['monitor_id']
                    self._child_classes = OrderedDict([("start-time", ("start_time", Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime))])
                    self._leafs = OrderedDict([
                        ('monitor_id', (YLeaf(YType.uint32, 'monitor-id'), ['int'])),
                        ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                        ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ])
                    self.monitor_id = None
                    self.frequency = None
                    self.period = None

                    self.start_time = Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime()
                    self.start_time.parent = self
                    self._children_name_map["start_time"] = "start-time"
                    self._segment_path = lambda: "schedule" + "[monitor-id='" + str(self.monitor_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/schedules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.MplsLspMonitor.Schedules.Schedule, ['monitor_id', 'frequency', 'period'], name, value)


                class StartTime(Entity):
                    """
                    Start time of MPLSLM instance
                    
                    .. attribute:: schedule_type
                    
                    	Type of schedule
                    	**type**\:  :py:class:`IpslaSched <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaSched>`
                    
                    .. attribute:: hour
                    
                    	Hour value(hh) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    .. attribute:: minute
                    
                    	Minute value(mm) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    .. attribute:: second
                    
                    	Second value(ss) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    .. attribute:: month
                    
                    	Month of the year (optional. Default current month)
                    	**type**\:  :py:class:`IpslaMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaMonth>`
                    
                    .. attribute:: day
                    
                    	Day of the month(optional. Default today)
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    .. attribute:: year
                    
                    	Year (optional. Default current year)
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime, self).__init__()

                        self.yang_name = "start-time"
                        self.yang_parent_name = "schedule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('schedule_type', (YLeaf(YType.enumeration, 'schedule-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSched', '')])),
                            ('hour', (YLeaf(YType.uint32, 'hour'), ['int'])),
                            ('minute', (YLeaf(YType.uint32, 'minute'), ['int'])),
                            ('second', (YLeaf(YType.uint32, 'second'), ['int'])),
                            ('month', (YLeaf(YType.enumeration, 'month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaMonth', '')])),
                            ('day', (YLeaf(YType.uint32, 'day'), ['int'])),
                            ('year', (YLeaf(YType.uint32, 'year'), ['int'])),
                        ])
                        self.schedule_type = None
                        self.hour = None
                        self.minute = None
                        self.second = None
                        self.month = None
                        self.day = None
                        self.year = None
                        self._segment_path = lambda: "start-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsLspMonitor.Schedules.Schedule.StartTime, ['schedule_type', 'hour', 'minute', 'second', 'month', 'day', 'year'], name, value)


        class Definitions(Entity):
            """
            MPLS LSP Monitor definition table
            
            .. attribute:: definition
            
            	MPLS LSP Monitor definition
            	**type**\: list of  		 :py:class:`Definition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsLspMonitor.Definitions, self).__init__()

                self.yang_name = "definitions"
                self.yang_parent_name = "mpls-lsp-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("definition", ("definition", Ipsla.MplsLspMonitor.Definitions.Definition))])
                self._leafs = OrderedDict()

                self.definition = YList(self)
                self._segment_path = lambda: "definitions"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions, [], name, value)


            class Definition(Entity):
                """
                MPLS LSP Monitor definition
                
                .. attribute:: monitor_id  (key)
                
                	Monitor identifier
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: operation_type
                
                	Operation type specification
                	**type**\:  :py:class:`OperationType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.MplsLspMonitor.Definitions.Definition, self).__init__()

                    self.yang_name = "definition"
                    self.yang_parent_name = "definitions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['monitor_id']
                    self._child_classes = OrderedDict([("operation-type", ("operation_type", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType))])
                    self._leafs = OrderedDict([
                        ('monitor_id', (YLeaf(YType.uint32, 'monitor-id'), ['int'])),
                    ])
                    self.monitor_id = None

                    self.operation_type = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType()
                    self.operation_type.parent = self
                    self._children_name_map["operation_type"] = "operation-type"
                    self._segment_path = lambda: "definition" + "[monitor-id='" + str(self.monitor_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-lsp-monitor/definitions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition, ['monitor_id'], name, value)


                class OperationType(Entity):
                    """
                    Operation type specification
                    
                    .. attribute:: mpls_lsp_trace
                    
                    	Perform MPLS LSP Trace operation
                    	**type**\:  :py:class:`MplsLspTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace>`
                    
                    .. attribute:: mpls_lsp_ping
                    
                    	Perform MPLS LSP Ping operation
                    	**type**\:  :py:class:`MplsLspPing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing>`
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType, self).__init__()

                        self.yang_name = "operation-type"
                        self.yang_parent_name = "definition"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mpls-lsp-trace", ("mpls_lsp_trace", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace)), ("mpls-lsp-ping", ("mpls_lsp_ping", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing))])
                        self._leafs = OrderedDict()

                        self.mpls_lsp_trace = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace()
                        self.mpls_lsp_trace.parent = self
                        self._children_name_map["mpls_lsp_trace"] = "mpls-lsp-trace"

                        self.mpls_lsp_ping = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing()
                        self.mpls_lsp_ping.parent = self
                        self._children_name_map["mpls_lsp_ping"] = "mpls-lsp-ping"
                        self._segment_path = lambda: "operation-type"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType, [], name, value)


                    class MplsLspTrace(Entity):
                        """
                        Perform MPLS LSP Trace operation
                        
                        .. attribute:: ttl
                        
                        	Time to live value
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 30
                        
                        .. attribute:: exp_bits
                        
                        	EXP bits in MPLS LSP echo request header
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 0
                        
                        .. attribute:: reply
                        
                        	Echo reply options for the MPLS LSP operation
                        	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this MPLSLM instance
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        .. attribute:: lsp_selector
                        
                        	Attributes used for path selection during LSP load balancing
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 1.0.0.127
                        
                        .. attribute:: output_interface
                        
                        	Echo request output interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: accesslist
                        
                        	Apply access list to filter PE addresses
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: create
                        
                        	Create MPLSLM instance with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: output_nexthop
                        
                        	Echo request output nexthop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: force_explicit_null
                        
                        	Forced option for the MPLS LSP operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: scan
                        
                        	Scanning parameters configuration
                        	**type**\:  :py:class:`Scan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan>`
                        
                        .. attribute:: vrf
                        
                        	Specify a VRF instance to be monitored
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace, self).__init__()

                            self.yang_name = "mpls-lsp-trace"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("reply", ("reply", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply)), ("statistics", ("statistics", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics)), ("scan", ("scan", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan))])
                            self._leafs = OrderedDict([
                                ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                                ('exp_bits', (YLeaf(YType.uint32, 'exp-bits'), ['int'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                ('accesslist', (YLeaf(YType.str, 'accesslist'), ['str'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('output_nexthop', (YLeaf(YType.str, 'output-nexthop'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('force_explicit_null', (YLeaf(YType.empty, 'force-explicit-null'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ])
                            self.ttl = None
                            self.exp_bits = None
                            self.tag = None
                            self.lsp_selector = None
                            self.output_interface = None
                            self.accesslist = None
                            self.create = None
                            self.output_nexthop = None
                            self.timeout = None
                            self.force_explicit_null = None
                            self.vrf = None

                            self.reply = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply()
                            self.reply.parent = self
                            self._children_name_map["reply"] = "reply"

                            self.statistics = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.scan = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan()
                            self.scan.parent = self
                            self._children_name_map["scan"] = "scan"
                            self._segment_path = lambda: "mpls-lsp-trace"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace, ['ttl', 'exp_bits', 'tag', 'lsp_selector', 'output_interface', 'accesslist', 'create', 'output_nexthop', 'timeout', 'force_explicit_null', 'vrf'], name, value)


                        class Reply(Entity):
                            """
                            Echo reply options for the MPLS LSP operation
                            
                            .. attribute:: dscp_bits
                            
                            	DSCP bits in the reply IP header
                            	**type**\: union of the below types:
                            
                            		**type**\:  :py:class:`IpslaLspReplyDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspReplyDscp>`
                            
                            		**type**\: int
                            
                            			**range:** 0..63
                            
                            .. attribute:: mode
                            
                            	Enables use of router alert in echo reply packets
                            	**type**\:  :py:class:`IpslaLspMonitorReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspMonitorReplyMode>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply, self).__init__()

                                self.yang_name = "reply"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dscp_bits', (YLeaf(YType.str, 'dscp-bits'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp', ''),'int'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorReplyMode', '')])),
                                ])
                                self.dscp_bits = None
                                self.mode = None
                                self._segment_path = lambda: "reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Reply, ['dscp_bits', 'mode'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                ])
                                self.hours = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Statistics, ['hours'], name, value)


                        class Scan(Entity):
                            """
                            Scanning parameters configuration
                            
                            .. attribute:: interval
                            
                            	Time interval for automatic discovery
                            	**type**\: int
                            
                            	**range:** 1..70560
                            
                            	**units**\: minute
                            
                            	**default value**\: 240
                            
                            .. attribute:: delete_factor
                            
                            	Number of times for automatic deletion
                            	**type**\: int
                            
                            	**range:** 0..2147483647
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan, self).__init__()

                                self.yang_name = "scan"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                    ('delete_factor', (YLeaf(YType.uint32, 'delete-factor'), ['int'])),
                                ])
                                self.interval = None
                                self.delete_factor = None
                                self._segment_path = lambda: "scan"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspTrace.Scan, ['interval', 'delete_factor'], name, value)


                    class MplsLspPing(Entity):
                        """
                        Perform MPLS LSP Ping operation
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize>`
                        
                        .. attribute:: path_discover
                        
                        	Path discover configuration
                        	**type**\:  :py:class:`PathDiscover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover>`
                        
                        .. attribute:: ttl
                        
                        	Time to live value
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 255
                        
                        .. attribute:: exp_bits
                        
                        	EXP bits in MPLS LSP echo request header
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 0
                        
                        .. attribute:: reply
                        
                        	Echo reply options for the MPLS LSP operation
                        	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this MPLSLM instance
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        .. attribute:: lsp_selector
                        
                        	Attributes used for path selection during LSP load balancing
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 1.0.0.127
                        
                        .. attribute:: output_interface
                        
                        	Echo request output interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: accesslist
                        
                        	Apply access list to filter PE addresses
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: create
                        
                        	Create MPLSLM instance with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: output_nexthop
                        
                        	Echo request output nexthop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: force_explicit_null
                        
                        	Forced option for the MPLS LSP operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: scan
                        
                        	Scanning parameters configuration
                        	**type**\:  :py:class:`Scan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan>`
                        
                        .. attribute:: vrf
                        
                        	Specify a VRF instance to be monitored
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing, self).__init__()

                            self.yang_name = "mpls-lsp-ping"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize)), ("path-discover", ("path_discover", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover)), ("reply", ("reply", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply)), ("statistics", ("statistics", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics)), ("scan", ("scan", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan))])
                            self._leafs = OrderedDict([
                                ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                                ('exp_bits', (YLeaf(YType.uint32, 'exp-bits'), ['int'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                                ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                ('accesslist', (YLeaf(YType.str, 'accesslist'), ['str'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('output_nexthop', (YLeaf(YType.str, 'output-nexthop'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('force_explicit_null', (YLeaf(YType.empty, 'force-explicit-null'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ])
                            self.ttl = None
                            self.exp_bits = None
                            self.tag = None
                            self.lsp_selector = None
                            self.output_interface = None
                            self.accesslist = None
                            self.create = None
                            self.output_nexthop = None
                            self.timeout = None
                            self.force_explicit_null = None
                            self.vrf = None

                            self.data_size = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.path_discover = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover()
                            self.path_discover.parent = self
                            self._children_name_map["path_discover"] = "path-discover"

                            self.reply = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply()
                            self.reply.parent = self
                            self._children_name_map["reply"] = "reply"

                            self.statistics = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.scan = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan()
                            self.scan.parent = self
                            self._children_name_map["scan"] = "scan"
                            self._segment_path = lambda: "mpls-lsp-ping"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing, ['ttl', 'exp_bits', 'tag', 'lsp_selector', 'output_interface', 'accesslist', 'create', 'output_nexthop', 'timeout', 'force_explicit_null', 'vrf'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 100..17986
                            
                            	**units**\: byte
                            
                            	**default value**\: 100
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.DataSize, ['request'], name, value)


                        class PathDiscover(Entity):
                            """
                            Path discover configuration
                            
                            .. attribute:: session
                            
                            	Session parameters configuration
                            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session>`
                            
                            .. attribute:: path
                            
                            	Path parameters configuration
                            	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path>`
                            
                            .. attribute:: echo
                            
                            	Echo parameters configuration
                            	**type**\:  :py:class:`Echo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo>`
                            
                            .. attribute:: scan_period
                            
                            	Time period for finishing path discovery
                            	**type**\: int
                            
                            	**range:** 0..7200
                            
                            	**units**\: minute
                            
                            	**default value**\: 0
                            
                            .. attribute:: create
                            
                            	Create LPD instance
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover, self).__init__()

                                self.yang_name = "path-discover"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("session", ("session", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session)), ("path", ("path", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path)), ("echo", ("echo", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo))])
                                self._leafs = OrderedDict([
                                    ('scan_period', (YLeaf(YType.uint32, 'scan-period'), ['int'])),
                                    ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ])
                                self.scan_period = None
                                self.create = None

                                self.session = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session()
                                self.session.parent = self
                                self._children_name_map["session"] = "session"

                                self.path = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path()
                                self.path.parent = self
                                self._children_name_map["path"] = "path"

                                self.echo = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo()
                                self.echo.parent = self
                                self._children_name_map["echo"] = "echo"
                                self._segment_path = lambda: "path-discover"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover, ['scan_period', 'create'], name, value)


                            class Session(Entity):
                                """
                                Session parameters configuration
                                
                                .. attribute:: timeout
                                
                                	Timeout value for path discovery request
                                	**type**\: int
                                
                                	**range:** 1..900
                                
                                	**units**\: second
                                
                                	**default value**\: 120
                                
                                .. attribute:: limit
                                
                                	Number of concurrent active path discovery requests at one time
                                	**type**\: int
                                
                                	**range:** 1..15
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session, self).__init__()

                                    self.yang_name = "session"
                                    self.yang_parent_name = "path-discover"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                        ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ])
                                    self.timeout = None
                                    self.limit = None
                                    self._segment_path = lambda: "session"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Session, ['timeout', 'limit'], name, value)


                            class Path(Entity):
                                """
                                Path parameters configuration
                                
                                .. attribute:: secondary_frequency
                                
                                	Frequency to be used if path failure condition is detected
                                	**type**\:  :py:class:`SecondaryFrequency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: retry
                                
                                	Number of attempts before declaring the path as down
                                	**type**\: int
                                
                                	**range:** 1..16
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path, self).__init__()

                                    self.yang_name = "path"
                                    self.yang_parent_name = "path-discover"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("secondary-frequency", ("secondary_frequency", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency))])
                                    self._leafs = OrderedDict([
                                        ('retry', (YLeaf(YType.uint32, 'retry'), ['int'])),
                                    ])
                                    self.retry = None

                                    self.secondary_frequency = None
                                    self._children_name_map["secondary_frequency"] = "secondary-frequency"
                                    self._segment_path = lambda: "path"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path, ['retry'], name, value)


                                class SecondaryFrequency(Entity):
                                    """
                                    Frequency to be used if path failure
                                    condition is detected
                                    
                                    .. attribute:: type
                                    
                                    	Condition type of path failure
                                    	**type**\:  :py:class:`IpslaSecondaryFrequency <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaSecondaryFrequency>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: frequency
                                    
                                    	Frequency value in seconds
                                    	**type**\: int
                                    
                                    	**range:** 1..604800
                                    
                                    	**mandatory**\: True
                                    
                                    	**units**\: second
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'man-ipsla-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency, self).__init__()

                                        self.yang_name = "secondary-frequency"
                                        self.yang_parent_name = "path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSecondaryFrequency', '')])),
                                            ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                        ])
                                        self.type = None
                                        self.frequency = None
                                        self._segment_path = lambda: "secondary-frequency"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Path.SecondaryFrequency, ['type', 'frequency'], name, value)


                            class Echo(Entity):
                                """
                                Echo parameters configuration
                                
                                .. attribute:: multipath
                                
                                	Downstream map multipath settings
                                	**type**\:  :py:class:`Multipath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath>`
                                
                                .. attribute:: interval
                                
                                	Send interval between echo requests during path discovery
                                	**type**\: int
                                
                                	**range:** 0..3600000
                                
                                	**units**\: millisecond
                                
                                	**default value**\: 0
                                
                                .. attribute:: timeout
                                
                                	Timeout value for echo requests during path discovery
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                	**units**\: second
                                
                                	**default value**\: 5
                                
                                .. attribute:: retry
                                
                                	Number of timeout retry attempts during path discovery
                                	**type**\: int
                                
                                	**range:** 0..10
                                
                                	**default value**\: 3
                                
                                .. attribute:: maximum_lsp_selector
                                
                                	Maximum IPv4 address used as destination in echo request
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**default value**\: 127.255.255.255
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo, self).__init__()

                                    self.yang_name = "echo"
                                    self.yang_parent_name = "path-discover"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("multipath", ("multipath", Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath))])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                        ('retry', (YLeaf(YType.uint32, 'retry'), ['int'])),
                                        ('maximum_lsp_selector', (YLeaf(YType.str, 'maximum-lsp-selector'), ['str'])),
                                    ])
                                    self.interval = None
                                    self.timeout = None
                                    self.retry = None
                                    self.maximum_lsp_selector = None

                                    self.multipath = Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath()
                                    self.multipath.parent = self
                                    self._children_name_map["multipath"] = "multipath"
                                    self._segment_path = lambda: "echo"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo, ['interval', 'timeout', 'retry', 'maximum_lsp_selector'], name, value)


                                class Multipath(Entity):
                                    """
                                    Downstream map multipath settings
                                    
                                    .. attribute:: bitmap_size
                                    
                                    	Multipath bit size
                                    	**type**\: int
                                    
                                    	**range:** 1..256
                                    
                                    	**default value**\: 32
                                    
                                    

                                    """

                                    _prefix = 'man-ipsla-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath, self).__init__()

                                        self.yang_name = "multipath"
                                        self.yang_parent_name = "echo"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('bitmap_size', (YLeaf(YType.uint32, 'bitmap-size'), ['int'])),
                                        ])
                                        self.bitmap_size = None
                                        self._segment_path = lambda: "multipath"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.PathDiscover.Echo.Multipath, ['bitmap_size'], name, value)


                        class Reply(Entity):
                            """
                            Echo reply options for the MPLS LSP operation
                            
                            .. attribute:: dscp_bits
                            
                            	DSCP bits in the reply IP header
                            	**type**\: union of the below types:
                            
                            		**type**\:  :py:class:`IpslaLspReplyDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspReplyDscp>`
                            
                            		**type**\: int
                            
                            			**range:** 0..63
                            
                            .. attribute:: mode
                            
                            	Enables use of router alert in echo reply packets
                            	**type**\:  :py:class:`IpslaLspMonitorReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspMonitorReplyMode>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply, self).__init__()

                                self.yang_name = "reply"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dscp_bits', (YLeaf(YType.str, 'dscp-bits'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp', ''),'int'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspMonitorReplyMode', '')])),
                                ])
                                self.dscp_bits = None
                                self.mode = None
                                self._segment_path = lambda: "reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Reply, ['dscp_bits', 'mode'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                ])
                                self.hours = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Statistics, ['hours'], name, value)


                        class Scan(Entity):
                            """
                            Scanning parameters configuration
                            
                            .. attribute:: interval
                            
                            	Time interval for automatic discovery
                            	**type**\: int
                            
                            	**range:** 1..70560
                            
                            	**units**\: minute
                            
                            	**default value**\: 240
                            
                            .. attribute:: delete_factor
                            
                            	Number of times for automatic deletion
                            	**type**\: int
                            
                            	**range:** 0..2147483647
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan, self).__init__()

                                self.yang_name = "scan"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                    ('delete_factor', (YLeaf(YType.uint32, 'delete-factor'), ['int'])),
                                ])
                                self.interval = None
                                self.delete_factor = None
                                self._segment_path = lambda: "scan"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.MplsLspMonitor.Definitions.Definition.OperationType.MplsLspPing.Scan, ['interval', 'delete_factor'], name, value)


    class Operation(Entity):
        """
        IPSLA Operation configuration
        
        .. attribute:: schedules
        
        	Schedule an operation
        	**type**\:  :py:class:`Schedules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Schedules>`
        
        .. attribute:: reactions
        
        	Reaction configuration
        	**type**\:  :py:class:`Reactions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions>`
        
        .. attribute:: reaction_triggers
        
        	Reaction trigger configuration
        	**type**\:  :py:class:`ReactionTriggers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.ReactionTriggers>`
        
        .. attribute:: definitions
        
        	Operation definition table
        	**type**\:  :py:class:`Definitions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions>`
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.Operation, self).__init__()

            self.yang_name = "operation"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("schedules", ("schedules", Ipsla.Operation.Schedules)), ("reactions", ("reactions", Ipsla.Operation.Reactions)), ("reaction-triggers", ("reaction_triggers", Ipsla.Operation.ReactionTriggers)), ("definitions", ("definitions", Ipsla.Operation.Definitions))])
            self._leafs = OrderedDict()

            self.schedules = Ipsla.Operation.Schedules()
            self.schedules.parent = self
            self._children_name_map["schedules"] = "schedules"

            self.reactions = Ipsla.Operation.Reactions()
            self.reactions.parent = self
            self._children_name_map["reactions"] = "reactions"

            self.reaction_triggers = Ipsla.Operation.ReactionTriggers()
            self.reaction_triggers.parent = self
            self._children_name_map["reaction_triggers"] = "reaction-triggers"

            self.definitions = Ipsla.Operation.Definitions()
            self.definitions.parent = self
            self._children_name_map["definitions"] = "definitions"
            self._segment_path = lambda: "operation"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.Operation, [], name, value)


        class Schedules(Entity):
            """
            Schedule an operation
            
            .. attribute:: schedule
            
            	Operation schedule configuration
            	**type**\: list of  		 :py:class:`Schedule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Schedules.Schedule>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Operation.Schedules, self).__init__()

                self.yang_name = "schedules"
                self.yang_parent_name = "operation"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("schedule", ("schedule", Ipsla.Operation.Schedules.Schedule))])
                self._leafs = OrderedDict()

                self.schedule = YList(self)
                self._segment_path = lambda: "schedules"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Operation.Schedules, [], name, value)


            class Schedule(Entity):
                """
                Operation schedule configuration
                
                .. attribute:: operation_id  (key)
                
                	Operation number
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: start_time
                
                	Start time of the operation
                	**type**\:  :py:class:`StartTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Schedules.Schedule.StartTime>`
                
                .. attribute:: life
                
                	Length of the time to execute (default 3600 seconds)
                	**type**\: union of the below types:
                
                		**type**\:  :py:class:`IpslaLife <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLife>`
                
                		**type**\: int
                
                			**range:** 0..2147483647
                
                	**units**\: second
                
                .. attribute:: ageout
                
                	How long to keep this entry after it becomes inactive
                	**type**\: int
                
                	**range:** 0..2073600
                
                	**units**\: second
                
                .. attribute:: recurring
                
                	probe to be scheduled automatically every day
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Operation.Schedules.Schedule, self).__init__()

                    self.yang_name = "schedule"
                    self.yang_parent_name = "schedules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['operation_id']
                    self._child_classes = OrderedDict([("start-time", ("start_time", Ipsla.Operation.Schedules.Schedule.StartTime))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                        ('life', (YLeaf(YType.str, 'life'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLife', ''),'int'])),
                        ('ageout', (YLeaf(YType.uint32, 'ageout'), ['int'])),
                        ('recurring', (YLeaf(YType.empty, 'recurring'), ['Empty'])),
                    ])
                    self.operation_id = None
                    self.life = None
                    self.ageout = None
                    self.recurring = None

                    self.start_time = Ipsla.Operation.Schedules.Schedule.StartTime()
                    self.start_time.parent = self
                    self._children_name_map["start_time"] = "start-time"
                    self._segment_path = lambda: "schedule" + "[operation-id='" + str(self.operation_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/schedules/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Operation.Schedules.Schedule, ['operation_id', 'life', 'ageout', 'recurring'], name, value)


                class StartTime(Entity):
                    """
                    Start time of the operation
                    
                    .. attribute:: schedule_type
                    
                    	Type of schedule
                    	**type**\:  :py:class:`IpslaSched <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaSched>`
                    
                    .. attribute:: hour
                    
                    	Hour value(hh) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    .. attribute:: minute
                    
                    	Minute value(mm) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    .. attribute:: second
                    
                    	Second value(ss) in hh\:mm\:ss specification
                    	**type**\: int
                    
                    	**range:** 0..59
                    
                    .. attribute:: month
                    
                    	Month of the year (optional. Default current month)
                    	**type**\:  :py:class:`IpslaMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaMonth>`
                    
                    .. attribute:: day
                    
                    	Day of the month(optional. Default today)
                    	**type**\: int
                    
                    	**range:** 1..31
                    
                    .. attribute:: year
                    
                    	Year(optional. Default current year)
                    	**type**\: int
                    
                    	**range:** 1993..2035
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.Operation.Schedules.Schedule.StartTime, self).__init__()

                        self.yang_name = "start-time"
                        self.yang_parent_name = "schedule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('schedule_type', (YLeaf(YType.enumeration, 'schedule-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaSched', '')])),
                            ('hour', (YLeaf(YType.uint32, 'hour'), ['int'])),
                            ('minute', (YLeaf(YType.uint32, 'minute'), ['int'])),
                            ('second', (YLeaf(YType.uint32, 'second'), ['int'])),
                            ('month', (YLeaf(YType.enumeration, 'month'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaMonth', '')])),
                            ('day', (YLeaf(YType.uint32, 'day'), ['int'])),
                            ('year', (YLeaf(YType.uint32, 'year'), ['int'])),
                        ])
                        self.schedule_type = None
                        self.hour = None
                        self.minute = None
                        self.second = None
                        self.month = None
                        self.day = None
                        self.year = None
                        self._segment_path = lambda: "start-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.Operation.Schedules.Schedule.StartTime, ['schedule_type', 'hour', 'minute', 'second', 'month', 'day', 'year'], name, value)


        class Reactions(Entity):
            """
            Reaction configuration
            
            .. attribute:: reaction
            
            	Reaction configuration for an operation
            	**type**\: list of  		 :py:class:`Reaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Operation.Reactions, self).__init__()

                self.yang_name = "reactions"
                self.yang_parent_name = "operation"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reaction", ("reaction", Ipsla.Operation.Reactions.Reaction))])
                self._leafs = OrderedDict()

                self.reaction = YList(self)
                self._segment_path = lambda: "reactions"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Operation.Reactions, [], name, value)


            class Reaction(Entity):
                """
                Reaction configuration for an operation
                
                .. attribute:: operation_id  (key)
                
                	Operation number
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: condition
                
                	Reaction condition specification
                	**type**\:  :py:class:`Condition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Operation.Reactions.Reaction, self).__init__()

                    self.yang_name = "reaction"
                    self.yang_parent_name = "reactions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['operation_id']
                    self._child_classes = OrderedDict([("condition", ("condition", Ipsla.Operation.Reactions.Reaction.Condition))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                    ])
                    self.operation_id = None

                    self.condition = Ipsla.Operation.Reactions.Reaction.Condition()
                    self.condition.parent = self
                    self._children_name_map["condition"] = "condition"
                    self._segment_path = lambda: "reaction" + "[operation-id='" + str(self.operation_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/reactions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Operation.Reactions.Reaction, ['operation_id'], name, value)


                class Condition(Entity):
                    """
                    Reaction condition specification
                    
                    .. attribute:: jitter_average_ds
                    
                    	React on destination to source jitter threshold violation
                    	**type**\:  :py:class:`JitterAverageDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs>`
                    
                    .. attribute:: timeout
                    
                    	React on probe timeout
                    	**type**\:  :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Timeout>`
                    
                    .. attribute:: jitter_average
                    
                    	React on average round trip jitter threshold violation
                    	**type**\:  :py:class:`JitterAverage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage>`
                    
                    .. attribute:: verify_error
                    
                    	React on error verfication violation
                    	**type**\:  :py:class:`VerifyError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.VerifyError>`
                    
                    .. attribute:: rtt
                    
                    	React on round trip time threshold violation
                    	**type**\:  :py:class:`Rtt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Rtt>`
                    
                    .. attribute:: packet_loss_sd
                    
                    	React on destination to source packet loss threshold violation
                    	**type**\:  :py:class:`PacketLossSd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd>`
                    
                    .. attribute:: jitter_average_sd
                    
                    	React on average source to destination jitter threshold violation
                    	**type**\:  :py:class:`JitterAverageSd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd>`
                    
                    .. attribute:: connection_loss
                    
                    	React on connection loss for a monitored operation
                    	**type**\:  :py:class:`ConnectionLoss <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss>`
                    
                    .. attribute:: packet_loss_ds
                    
                    	React on source to destination packet loss threshold violation
                    	**type**\:  :py:class:`PacketLossDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs>`
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.Operation.Reactions.Reaction.Condition, self).__init__()

                        self.yang_name = "condition"
                        self.yang_parent_name = "reaction"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("jitter-average-ds", ("jitter_average_ds", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs)), ("timeout", ("timeout", Ipsla.Operation.Reactions.Reaction.Condition.Timeout)), ("jitter-average", ("jitter_average", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage)), ("verify-error", ("verify_error", Ipsla.Operation.Reactions.Reaction.Condition.VerifyError)), ("rtt", ("rtt", Ipsla.Operation.Reactions.Reaction.Condition.Rtt)), ("packet-loss-sd", ("packet_loss_sd", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd)), ("jitter-average-sd", ("jitter_average_sd", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd)), ("connection-loss", ("connection_loss", Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss)), ("packet-loss-ds", ("packet_loss_ds", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs))])
                        self._leafs = OrderedDict()

                        self.jitter_average_ds = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs()
                        self.jitter_average_ds.parent = self
                        self._children_name_map["jitter_average_ds"] = "jitter-average-ds"

                        self.timeout = Ipsla.Operation.Reactions.Reaction.Condition.Timeout()
                        self.timeout.parent = self
                        self._children_name_map["timeout"] = "timeout"

                        self.jitter_average = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage()
                        self.jitter_average.parent = self
                        self._children_name_map["jitter_average"] = "jitter-average"

                        self.verify_error = Ipsla.Operation.Reactions.Reaction.Condition.VerifyError()
                        self.verify_error.parent = self
                        self._children_name_map["verify_error"] = "verify-error"

                        self.rtt = Ipsla.Operation.Reactions.Reaction.Condition.Rtt()
                        self.rtt.parent = self
                        self._children_name_map["rtt"] = "rtt"

                        self.packet_loss_sd = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd()
                        self.packet_loss_sd.parent = self
                        self._children_name_map["packet_loss_sd"] = "packet-loss-sd"

                        self.jitter_average_sd = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd()
                        self.jitter_average_sd.parent = self
                        self._children_name_map["jitter_average_sd"] = "jitter-average-sd"

                        self.connection_loss = Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss()
                        self.connection_loss.parent = self
                        self._children_name_map["connection_loss"] = "connection-loss"

                        self.packet_loss_ds = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs()
                        self.packet_loss_ds.parent = self
                        self._children_name_map["packet_loss_ds"] = "packet-loss-ds"
                        self._segment_path = lambda: "condition"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition, [], name, value)


                    class JitterAverageDs(Entity):
                        """
                        React on destination to source jitter
                        threshold violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs, self).__init__()

                            self.yang_name = "jitter-average-ds"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "jitter-average-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "jitter-average-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "jitter-average-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "jitter-average-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageDs.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class Timeout(Entity):
                        """
                        React on probe timeout
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.Timeout, self).__init__()

                            self.yang_name = "timeout"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "timeout"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Timeout, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "timeout"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "timeout"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Timeout.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class JitterAverage(Entity):
                        """
                        React on average round trip jitter threshold
                        violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage, self).__init__()

                            self.yang_name = "jitter-average"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "jitter-average"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "jitter-average"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "jitter-average"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "jitter-average"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverage.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class VerifyError(Entity):
                        """
                        React on error verfication violation
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError, self).__init__()

                            self.yang_name = "verify-error"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "verify-error"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "verify-error"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "verify-error"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.VerifyError.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class Rtt(Entity):
                        """
                        React on round trip time threshold violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.Rtt, self).__init__()

                            self.yang_name = "rtt"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "rtt"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Rtt, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "rtt"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "rtt"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "rtt"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.Rtt.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class PacketLossSd(Entity):
                        """
                        React on destination to source packet loss
                        threshold violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd, self).__init__()

                            self.yang_name = "packet-loss-sd"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "packet-loss-sd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "packet-loss-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "packet-loss-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "packet-loss-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossSd.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class JitterAverageSd(Entity):
                        """
                        React on average source to destination
                        jitter threshold violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd, self).__init__()

                            self.yang_name = "jitter-average-sd"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "jitter-average-sd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "jitter-average-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "jitter-average-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "jitter-average-sd"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.JitterAverageSd.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class ConnectionLoss(Entity):
                        """
                        React on connection loss for a monitored
                        operation
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss, self).__init__()

                            self.yang_name = "connection-loss"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "connection-loss"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss, ['create'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "connection-loss"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "connection-loss"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.ConnectionLoss.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


                    class PacketLossDs(Entity):
                        """
                        React on source to destination packet loss
                        threshold violation
                        
                        .. attribute:: threshold_limits
                        
                        	Specify threshold limits for the monitored element
                        	**type**\:  :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: action_type
                        
                        	Type of action to be taken on threshold violation(s)
                        	**type**\:  :py:class:`ActionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType>`
                        
                        .. attribute:: create
                        
                        	Create reaction condition for a particular operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: threshold_type
                        
                        	Type of thresholding to perform on the monitored element
                        	**type**\:  :py:class:`ThresholdType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs, self).__init__()

                            self.yang_name = "packet-loss-ds"
                            self.yang_parent_name = "condition"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("threshold-limits", ("threshold_limits", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits)), ("action-type", ("action_type", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType)), ("threshold-type", ("threshold_type", Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType))])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                            ])
                            self.create = None

                            self.threshold_limits = None
                            self._children_name_map["threshold_limits"] = "threshold-limits"

                            self.action_type = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType()
                            self.action_type.parent = self
                            self._children_name_map["action_type"] = "action-type"

                            self.threshold_type = Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType()
                            self.threshold_type.parent = self
                            self._children_name_map["threshold_type"] = "threshold-type"
                            self._segment_path = lambda: "packet-loss-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs, ['create'], name, value)


                        class ThresholdLimits(Entity):
                            """
                            Specify threshold limits for the monitored
                            element
                            
                            .. attribute:: lower_limit
                            
                            	Threshold lower limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: upper_limit
                            
                            	Threshold upper limit value
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits, self).__init__()

                                self.yang_name = "threshold-limits"
                                self.yang_parent_name = "packet-loss-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('lower_limit', (YLeaf(YType.uint32, 'lower-limit'), ['int'])),
                                    ('upper_limit', (YLeaf(YType.uint32, 'upper-limit'), ['int'])),
                                ])
                                self.lower_limit = None
                                self.upper_limit = None
                                self._segment_path = lambda: "threshold-limits"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdLimits, ['lower_limit', 'upper_limit'], name, value)


                        class ActionType(Entity):
                            """
                            Type of action to be taken on threshold
                            violation(s)
                            
                            .. attribute:: logging
                            
                            	Generate a syslog alarm on threshold violation
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: trigger
                            
                            	Generate trigger to active reaction triggered operation(s)
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType, self).__init__()

                                self.yang_name = "action-type"
                                self.yang_parent_name = "packet-loss-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('logging', (YLeaf(YType.empty, 'logging'), ['Empty'])),
                                    ('trigger', (YLeaf(YType.empty, 'trigger'), ['Empty'])),
                                ])
                                self.logging = None
                                self.trigger = None
                                self._segment_path = lambda: "action-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ActionType, ['logging', 'trigger'], name, value)


                        class ThresholdType(Entity):
                            """
                            Type of thresholding to perform on the monitored
                            element
                            
                            .. attribute:: thresh_type
                            
                            	Type of thresholding to perform
                            	**type**\:  :py:class:`IpslaThresholdTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaThresholdTypes>`
                            
                            .. attribute:: count1
                            
                            	Probe count for avarage, consecutive case or X value for XofY case
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: count2
                            
                            	Y value, when threshold type is XofY
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType, self).__init__()

                                self.yang_name = "threshold-type"
                                self.yang_parent_name = "packet-loss-ds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('thresh_type', (YLeaf(YType.enumeration, 'thresh-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaThresholdTypes', '')])),
                                    ('count1', (YLeaf(YType.uint32, 'count1'), ['int'])),
                                    ('count2', (YLeaf(YType.uint32, 'count2'), ['int'])),
                                ])
                                self.thresh_type = None
                                self.count1 = None
                                self.count2 = None
                                self._segment_path = lambda: "threshold-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Reactions.Reaction.Condition.PacketLossDs.ThresholdType, ['thresh_type', 'count1', 'count2'], name, value)


        class ReactionTriggers(Entity):
            """
            Reaction trigger configuration
            
            .. attribute:: reaction_trigger
            
            	Reaction trigger for an operation
            	**type**\: list of  		 :py:class:`ReactionTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.ReactionTriggers.ReactionTrigger>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Operation.ReactionTriggers, self).__init__()

                self.yang_name = "reaction-triggers"
                self.yang_parent_name = "operation"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reaction-trigger", ("reaction_trigger", Ipsla.Operation.ReactionTriggers.ReactionTrigger))])
                self._leafs = OrderedDict()

                self.reaction_trigger = YList(self)
                self._segment_path = lambda: "reaction-triggers"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Operation.ReactionTriggers, [], name, value)


            class ReactionTrigger(Entity):
                """
                Reaction trigger for an operation
                
                .. attribute:: operation_id  (key)
                
                	Operation number of the operation generating a trigger
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: triggered_op_id
                
                	Operation number of the operation to be triggered
                	**type**\: int
                
                	**range:** 1..2048
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Operation.ReactionTriggers.ReactionTrigger, self).__init__()

                    self.yang_name = "reaction-trigger"
                    self.yang_parent_name = "reaction-triggers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['operation_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                        ('triggered_op_id', (YLeaf(YType.uint32, 'triggered-op-id'), ['int'])),
                    ])
                    self.operation_id = None
                    self.triggered_op_id = None
                    self._segment_path = lambda: "reaction-trigger" + "[operation-id='" + str(self.operation_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/reaction-triggers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Operation.ReactionTriggers.ReactionTrigger, ['operation_id', 'triggered_op_id'], name, value)


        class Definitions(Entity):
            """
            Operation definition table
            
            .. attribute:: definition
            
            	Operation definition
            	**type**\: list of  		 :py:class:`Definition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Operation.Definitions, self).__init__()

                self.yang_name = "definitions"
                self.yang_parent_name = "operation"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("definition", ("definition", Ipsla.Operation.Definitions.Definition))])
                self._leafs = OrderedDict()

                self.definition = YList(self)
                self._segment_path = lambda: "definitions"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Operation.Definitions, [], name, value)


            class Definition(Entity):
                """
                Operation definition
                
                .. attribute:: operation_id  (key)
                
                	Operation number
                	**type**\: int
                
                	**range:** 1..2048
                
                .. attribute:: operation_type
                
                	Operation type specification
                	**type**\:  :py:class:`OperationType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Operation.Definitions.Definition, self).__init__()

                    self.yang_name = "definition"
                    self.yang_parent_name = "definitions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['operation_id']
                    self._child_classes = OrderedDict([("operation-type", ("operation_type", Ipsla.Operation.Definitions.Definition.OperationType))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                    ])
                    self.operation_id = None

                    self.operation_type = Ipsla.Operation.Definitions.Definition.OperationType()
                    self.operation_type.parent = self
                    self._children_name_map["operation_type"] = "operation-type"
                    self._segment_path = lambda: "definition" + "[operation-id='" + str(self.operation_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/operation/definitions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Operation.Definitions.Definition, ['operation_id'], name, value)


                class OperationType(Entity):
                    """
                    Operation type specification
                    
                    .. attribute:: icmp_echo
                    
                    	ICMPEcho Operation type
                    	**type**\:  :py:class:`IcmpEcho <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho>`
                    
                    .. attribute:: mpls_lsp_ping
                    
                    	MPLS LSP Ping Operation type
                    	**type**\:  :py:class:`MplsLspPing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing>`
                    
                    .. attribute:: udp_echo
                    
                    	UDPEcho Operation type
                    	**type**\:  :py:class:`UdpEcho <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho>`
                    
                    .. attribute:: mpls_lsp_trace
                    
                    	MPLS LSP Trace Operation type
                    	**type**\:  :py:class:`MplsLspTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace>`
                    
                    .. attribute:: udp_jitter
                    
                    	UDPJitter Operation type
                    	**type**\:  :py:class:`UdpJitter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter>`
                    
                    .. attribute:: icmp_path_echo
                    
                    	ICMPPathEcho Operation type
                    	**type**\:  :py:class:`IcmpPathEcho <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho>`
                    
                    .. attribute:: icmp_path_jitter
                    
                    	ICMPPathJitter Operation type
                    	**type**\:  :py:class:`IcmpPathJitter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter>`
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.Operation.Definitions.Definition.OperationType, self).__init__()

                        self.yang_name = "operation-type"
                        self.yang_parent_name = "definition"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("icmp-echo", ("icmp_echo", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho)), ("mpls-lsp-ping", ("mpls_lsp_ping", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing)), ("udp-echo", ("udp_echo", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho)), ("mpls-lsp-trace", ("mpls_lsp_trace", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace)), ("udp-jitter", ("udp_jitter", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter)), ("icmp-path-echo", ("icmp_path_echo", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho)), ("icmp-path-jitter", ("icmp_path_jitter", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter))])
                        self._leafs = OrderedDict()

                        self.icmp_echo = Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho()
                        self.icmp_echo.parent = self
                        self._children_name_map["icmp_echo"] = "icmp-echo"

                        self.mpls_lsp_ping = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing()
                        self.mpls_lsp_ping.parent = self
                        self._children_name_map["mpls_lsp_ping"] = "mpls-lsp-ping"

                        self.udp_echo = Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho()
                        self.udp_echo.parent = self
                        self._children_name_map["udp_echo"] = "udp-echo"

                        self.mpls_lsp_trace = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace()
                        self.mpls_lsp_trace.parent = self
                        self._children_name_map["mpls_lsp_trace"] = "mpls-lsp-trace"

                        self.udp_jitter = Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter()
                        self.udp_jitter.parent = self
                        self._children_name_map["udp_jitter"] = "udp-jitter"

                        self.icmp_path_echo = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho()
                        self.icmp_path_echo.parent = self
                        self._children_name_map["icmp_path_echo"] = "icmp-path-echo"

                        self.icmp_path_jitter = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter()
                        self.icmp_path_jitter.parent = self
                        self._children_name_map["icmp_path_jitter"] = "icmp-path-jitter"
                        self._segment_path = lambda: "operation-type"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType, [], name, value)


                    class IcmpEcho(Entity):
                        """
                        ICMPEcho Operation type
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize>`
                        
                        .. attribute:: source_address_v6
                        
                        	Enter IPv6 address of the source device
                        	**type**\: str
                        
                        .. attribute:: dest_address_v6
                        
                        	Enter IPv6 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: tos
                        
                        	Type of service setting in probe packet
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**default value**\: 0
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics>`
                        
                        .. attribute:: vrf
                        
                        	Configure IPSLA for a VPN Routing/Forwarding instance)
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: history
                        
                        	Configure the history parameters for this operation
                        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: dest_address
                        
                        	Enter IPv4 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: enhanced_stats
                        
                        	Table of statistics collection intervals
                        	**type**\:  :py:class:`EnhancedStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho, self).__init__()

                            self.yang_name = "icmp-echo"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics)), ("history", ("history", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History)), ("enhanced-stats", ("enhanced_stats", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats))])
                            self._leafs = OrderedDict([
                                ('source_address_v6', (YLeaf(YType.str, 'source-address-v6'), ['str'])),
                                ('dest_address_v6', (YLeaf(YType.str, 'dest-address-v6'), ['str'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.source_address_v6 = None
                            self.dest_address_v6 = None
                            self.source_address = None
                            self.tos = None
                            self.create = None
                            self.vrf = None
                            self.timeout = None
                            self.frequency = None
                            self.dest_address = None
                            self.tag = None

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.history = Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History()
                            self.history.parent = self
                            self._children_name_map["history"] = "history"

                            self.enhanced_stats = Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats()
                            self.enhanced_stats.parent = self
                            self._children_name_map["enhanced_stats"] = "enhanced-stats"
                            self._segment_path = lambda: "icmp-echo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho, ['source_address_v6', 'dest_address_v6', 'source_address', 'tos', 'create', 'vrf', 'timeout', 'frequency', 'dest_address', 'tag'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 0..16384
                            
                            	**units**\: byte
                            
                            	**default value**\: 36
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "icmp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.DataSize, ['request'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "icmp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                ])
                                self.hours = None
                                self.dist_interval = None
                                self.dist_count = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.Statistics, ['hours', 'dist_interval', 'dist_count'], name, value)


                        class History(Entity):
                            """
                            Configure the history parameters for this
                            operation
                            
                            .. attribute:: lives
                            
                            	Specify number of lives to be kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**default value**\: 0
                            
                            .. attribute:: history_filter
                            
                            	Choose type of data to be stored in history buffer
                            	**type**\:  :py:class:`IpslaHistoryFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaHistoryFilter>`
                            
                            .. attribute:: buckets
                            
                            	Specify number of history buckets
                            	**type**\: int
                            
                            	**range:** 1..60
                            
                            	**default value**\: 15
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History, self).__init__()

                                self.yang_name = "history"
                                self.yang_parent_name = "icmp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lives', (YLeaf(YType.uint32, 'lives'), ['int'])),
                                    ('history_filter', (YLeaf(YType.enumeration, 'history-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter', '')])),
                                    ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                ])
                                self.lives = None
                                self.history_filter = None
                                self.buckets = None
                                self._segment_path = lambda: "history"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.History, ['lives', 'history_filter', 'buckets'], name, value)


                        class EnhancedStats(Entity):
                            """
                            Table of statistics collection intervals
                            
                            .. attribute:: enhanced_stat
                            
                            	Statistics for a specified time interval
                            	**type**\: list of  		 :py:class:`EnhancedStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats, self).__init__()

                                self.yang_name = "enhanced-stats"
                                self.yang_parent_name = "icmp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enhanced-stat", ("enhanced_stat", Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat))])
                                self._leafs = OrderedDict()

                                self.enhanced_stat = YList(self)
                                self._segment_path = lambda: "enhanced-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats, [], name, value)


                            class EnhancedStat(Entity):
                                """
                                Statistics for a specified time interval
                                
                                .. attribute:: interval  (key)
                                
                                	Interval in seconds
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                	**units**\: second
                                
                                .. attribute:: buckets
                                
                                	Buckets of enhanced statistics kept
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**default value**\: 15
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat, self).__init__()

                                    self.yang_name = "enhanced-stat"
                                    self.yang_parent_name = "enhanced-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interval']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                    ])
                                    self.interval = None
                                    self.buckets = None
                                    self._segment_path = lambda: "enhanced-stat" + "[interval='" + str(self.interval) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpEcho.EnhancedStats.EnhancedStat, ['interval', 'buckets'], name, value)


                    class MplsLspPing(Entity):
                        """
                        MPLS LSP Ping Operation type
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize>`
                        
                        .. attribute:: reply
                        
                        	Echo reply options for the MPLS LSP operation
                        	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply>`
                        
                        .. attribute:: target
                        
                        	Target for the MPLS LSP operation
                        	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target>`
                        
                        .. attribute:: ttl
                        
                        	Time to live value
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 255
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: output_nexthop
                        
                        	Echo request output nexthop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: lsp_selector
                        
                        	Attributes used for path selection during LSP load balancing
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 1.0.0.127
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics>`
                        
                        .. attribute:: exp_bits
                        
                        	EXP bits in MPLS LSP echo reply header
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 0
                        
                        .. attribute:: force_explicit_null
                        
                        	Forced option for the MPLS LSP operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: history
                        
                        	Configure the history parameters for this operation
                        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: output_interface
                        
                        	Echo request output interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: enhanced_stats
                        
                        	Table of statistics collection intervals
                        	**type**\:  :py:class:`EnhancedStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing, self).__init__()

                            self.yang_name = "mpls-lsp-ping"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize)), ("reply", ("reply", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply)), ("target", ("target", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics)), ("history", ("history", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History)), ("enhanced-stats", ("enhanced_stats", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats))])
                            self._leafs = OrderedDict([
                                ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('output_nexthop', (YLeaf(YType.str, 'output-nexthop'), ['str'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                ('exp_bits', (YLeaf(YType.uint32, 'exp-bits'), ['int'])),
                                ('force_explicit_null', (YLeaf(YType.empty, 'force-explicit-null'), ['Empty'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.ttl = None
                            self.source_address = None
                            self.output_nexthop = None
                            self.create = None
                            self.lsp_selector = None
                            self.exp_bits = None
                            self.force_explicit_null = None
                            self.timeout = None
                            self.output_interface = None
                            self.frequency = None
                            self.tag = None

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.reply = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply()
                            self.reply.parent = self
                            self._children_name_map["reply"] = "reply"

                            self.target = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target()
                            self.target.parent = self
                            self._children_name_map["target"] = "target"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.history = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History()
                            self.history.parent = self
                            self._children_name_map["history"] = "history"

                            self.enhanced_stats = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats()
                            self.enhanced_stats.parent = self
                            self._children_name_map["enhanced_stats"] = "enhanced-stats"
                            self._segment_path = lambda: "mpls-lsp-ping"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing, ['ttl', 'source_address', 'output_nexthop', 'create', 'lsp_selector', 'exp_bits', 'force_explicit_null', 'timeout', 'output_interface', 'frequency', 'tag'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 100..17986
                            
                            	**default value**\: 100
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.DataSize, ['request'], name, value)


                        class Reply(Entity):
                            """
                            Echo reply options for the MPLS LSP
                            operation
                            
                            .. attribute:: mode
                            
                            	Enables use of router alert in echo reply packets
                            	**type**\:  :py:class:`IpslaLspPingReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspPingReplyMode>`
                            
                            .. attribute:: dscp_bits
                            
                            	DSCP bits in the reply IP header
                            	**type**\: union of the below types:
                            
                            		**type**\:  :py:class:`IpslaLspReplyDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspReplyDscp>`
                            
                            		**type**\: int
                            
                            			**range:** 0..63
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply, self).__init__()

                                self.yang_name = "reply"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspPingReplyMode', '')])),
                                    ('dscp_bits', (YLeaf(YType.str, 'dscp-bits'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp', ''),'int'])),
                                ])
                                self.mode = None
                                self.dscp_bits = None
                                self._segment_path = lambda: "reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Reply, ['mode', 'dscp_bits'], name, value)


                        class Target(Entity):
                            """
                            Target for the MPLS LSP operation
                            
                            .. attribute:: traffic_engineering
                            
                            	Traffic engineering target
                            	**type**\:  :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering>`
                            
                            .. attribute:: ipv4
                            
                            	Target specified as an IPv4 address
                            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4>`
                            
                            .. attribute:: pseudowire
                            
                            	Pseudowire target
                            	**type**\:  :py:class:`Pseudowire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target, self).__init__()

                                self.yang_name = "target"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("traffic-engineering", ("traffic_engineering", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering)), ("ipv4", ("ipv4", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4)), ("pseudowire", ("pseudowire", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire))])
                                self._leafs = OrderedDict()

                                self.traffic_engineering = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering()
                                self.traffic_engineering.parent = self
                                self._children_name_map["traffic_engineering"] = "traffic-engineering"

                                self.ipv4 = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4()
                                self.ipv4.parent = self
                                self._children_name_map["ipv4"] = "ipv4"

                                self.pseudowire = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire()
                                self.pseudowire.parent = self
                                self._children_name_map["pseudowire"] = "pseudowire"
                                self._segment_path = lambda: "target"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target, [], name, value)


                            class TrafficEngineering(Entity):
                                """
                                Traffic engineering target
                                
                                .. attribute:: tunnel
                                
                                	Tunnel interface number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering, self).__init__()

                                    self.yang_name = "traffic-engineering"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tunnel', (YLeaf(YType.uint32, 'tunnel'), ['int'])),
                                    ])
                                    self.tunnel = None
                                    self._segment_path = lambda: "traffic-engineering"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.TrafficEngineering, ['tunnel'], name, value)


                            class Ipv4(Entity):
                                """
                                Target specified as an IPv4 address
                                
                                .. attribute:: fec_address
                                
                                	Target FEC address with mask
                                	**type**\:  :py:class:`FecAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4, self).__init__()

                                    self.yang_name = "ipv4"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("fec-address", ("fec_address", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress))])
                                    self._leafs = OrderedDict()

                                    self.fec_address = None
                                    self._children_name_map["fec_address"] = "fec-address"
                                    self._segment_path = lambda: "ipv4"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4, [], name, value)


                                class FecAddress(Entity):
                                    """
                                    Target FEC address with mask
                                    
                                    .. attribute:: address
                                    
                                    	IP address for target
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: mask
                                    
                                    	IP netmask for target
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'man-ipsla-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress, self).__init__()

                                        self.yang_name = "fec-address"
                                        self.yang_parent_name = "ipv4"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                                        ])
                                        self.address = None
                                        self.mask = None
                                        self._segment_path = lambda: "fec-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Ipv4.FecAddress, ['address', 'mask'], name, value)


                            class Pseudowire(Entity):
                                """
                                Pseudowire target
                                
                                .. attribute:: target_address
                                
                                	Target address
                                	**type**\:  :py:class:`TargetAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire, self).__init__()

                                    self.yang_name = "pseudowire"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("target-address", ("target_address", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress))])
                                    self._leafs = OrderedDict()

                                    self.target_address = None
                                    self._children_name_map["target_address"] = "target-address"
                                    self._segment_path = lambda: "pseudowire"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire, [], name, value)


                                class TargetAddress(Entity):
                                    """
                                    Target address
                                    
                                    .. attribute:: address
                                    
                                    	Target address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: vc_id
                                    
                                    	Virtual circuit ID
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'man-ipsla-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress, self).__init__()

                                        self.yang_name = "target-address"
                                        self.yang_parent_name = "pseudowire"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('vc_id', (YLeaf(YType.uint32, 'vc-id'), ['int'])),
                                        ])
                                        self.address = None
                                        self.vc_id = None
                                        self._segment_path = lambda: "target-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Target.Pseudowire.TargetAddress, ['address', 'vc_id'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                ])
                                self.hours = None
                                self.dist_interval = None
                                self.dist_count = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.Statistics, ['hours', 'dist_interval', 'dist_count'], name, value)


                        class History(Entity):
                            """
                            Configure the history parameters for this
                            operation
                            
                            .. attribute:: lives
                            
                            	Specify number of lives to be kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**default value**\: 0
                            
                            .. attribute:: history_filter
                            
                            	Choose type of data to be stored in history buffer
                            	**type**\:  :py:class:`IpslaHistoryFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaHistoryFilter>`
                            
                            .. attribute:: buckets
                            
                            	Specify number of history buckets
                            	**type**\: int
                            
                            	**range:** 1..60
                            
                            	**default value**\: 15
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History, self).__init__()

                                self.yang_name = "history"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lives', (YLeaf(YType.uint32, 'lives'), ['int'])),
                                    ('history_filter', (YLeaf(YType.enumeration, 'history-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter', '')])),
                                    ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                ])
                                self.lives = None
                                self.history_filter = None
                                self.buckets = None
                                self._segment_path = lambda: "history"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.History, ['lives', 'history_filter', 'buckets'], name, value)


                        class EnhancedStats(Entity):
                            """
                            Table of statistics collection intervals
                            
                            .. attribute:: enhanced_stat
                            
                            	Statistics for a specified time interval
                            	**type**\: list of  		 :py:class:`EnhancedStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats, self).__init__()

                                self.yang_name = "enhanced-stats"
                                self.yang_parent_name = "mpls-lsp-ping"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enhanced-stat", ("enhanced_stat", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat))])
                                self._leafs = OrderedDict()

                                self.enhanced_stat = YList(self)
                                self._segment_path = lambda: "enhanced-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats, [], name, value)


                            class EnhancedStat(Entity):
                                """
                                Statistics for a specified time interval
                                
                                .. attribute:: interval  (key)
                                
                                	Interval in seconds
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                	**units**\: second
                                
                                .. attribute:: buckets
                                
                                	Buckets of enhanced statistics kept
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**default value**\: 15
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat, self).__init__()

                                    self.yang_name = "enhanced-stat"
                                    self.yang_parent_name = "enhanced-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interval']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                    ])
                                    self.interval = None
                                    self.buckets = None
                                    self._segment_path = lambda: "enhanced-stat" + "[interval='" + str(self.interval) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspPing.EnhancedStats.EnhancedStat, ['interval', 'buckets'], name, value)


                    class UdpEcho(Entity):
                        """
                        UDPEcho Operation type
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize>`
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: tos
                        
                        	Type of service setting in probe packet
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**default value**\: 0
                        
                        .. attribute:: control_disable
                        
                        	Disable control packets
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_port
                        
                        	Port number on source device
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics>`
                        
                        .. attribute:: vrf
                        
                        	Configure IPSLA for a VPN Routing/Forwarding instance)
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: history
                        
                        	Configure the history parameters for this operation
                        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: dest_port
                        
                        	Port number on target device
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: verify_data
                        
                        	Check each IPSLA response for corruption
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: dest_address
                        
                        	Enter IPv4 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: enhanced_stats
                        
                        	Table of statistics collection intervals
                        	**type**\:  :py:class:`EnhancedStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho, self).__init__()

                            self.yang_name = "udp-echo"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics)), ("history", ("history", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History)), ("enhanced-stats", ("enhanced_stats", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats))])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                ('control_disable', (YLeaf(YType.empty, 'control-disable'), ['Empty'])),
                                ('source_port', (YLeaf(YType.uint16, 'source-port'), ['int'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('dest_port', (YLeaf(YType.uint16, 'dest-port'), ['int'])),
                                ('verify_data', (YLeaf(YType.empty, 'verify-data'), ['Empty'])),
                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.source_address = None
                            self.tos = None
                            self.control_disable = None
                            self.source_port = None
                            self.create = None
                            self.vrf = None
                            self.timeout = None
                            self.frequency = None
                            self.dest_port = None
                            self.verify_data = None
                            self.dest_address = None
                            self.tag = None

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.history = Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History()
                            self.history.parent = self
                            self._children_name_map["history"] = "history"

                            self.enhanced_stats = Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats()
                            self.enhanced_stats.parent = self
                            self._children_name_map["enhanced_stats"] = "enhanced-stats"
                            self._segment_path = lambda: "udp-echo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho, ['source_address', 'tos', 'control_disable', 'source_port', 'create', 'vrf', 'timeout', 'frequency', 'dest_port', 'verify_data', 'dest_address', 'tag'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 16..1500
                            
                            	**units**\: byte
                            
                            	**default value**\: 16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "udp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.DataSize, ['request'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "udp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                ])
                                self.hours = None
                                self.dist_interval = None
                                self.dist_count = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.Statistics, ['hours', 'dist_interval', 'dist_count'], name, value)


                        class History(Entity):
                            """
                            Configure the history parameters for this
                            operation
                            
                            .. attribute:: lives
                            
                            	Specify number of lives to be kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**default value**\: 0
                            
                            .. attribute:: history_filter
                            
                            	Choose type of data to be stored in history buffer
                            	**type**\:  :py:class:`IpslaHistoryFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaHistoryFilter>`
                            
                            .. attribute:: buckets
                            
                            	Specify number of history buckets
                            	**type**\: int
                            
                            	**range:** 1..60
                            
                            	**default value**\: 15
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History, self).__init__()

                                self.yang_name = "history"
                                self.yang_parent_name = "udp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lives', (YLeaf(YType.uint32, 'lives'), ['int'])),
                                    ('history_filter', (YLeaf(YType.enumeration, 'history-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter', '')])),
                                    ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                ])
                                self.lives = None
                                self.history_filter = None
                                self.buckets = None
                                self._segment_path = lambda: "history"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.History, ['lives', 'history_filter', 'buckets'], name, value)


                        class EnhancedStats(Entity):
                            """
                            Table of statistics collection intervals
                            
                            .. attribute:: enhanced_stat
                            
                            	Statistics for a specified time interval
                            	**type**\: list of  		 :py:class:`EnhancedStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats, self).__init__()

                                self.yang_name = "enhanced-stats"
                                self.yang_parent_name = "udp-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enhanced-stat", ("enhanced_stat", Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat))])
                                self._leafs = OrderedDict()

                                self.enhanced_stat = YList(self)
                                self._segment_path = lambda: "enhanced-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats, [], name, value)


                            class EnhancedStat(Entity):
                                """
                                Statistics for a specified time interval
                                
                                .. attribute:: interval  (key)
                                
                                	Interval in seconds
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                	**units**\: second
                                
                                .. attribute:: buckets
                                
                                	Buckets of enhanced statistics kept
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**default value**\: 15
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat, self).__init__()

                                    self.yang_name = "enhanced-stat"
                                    self.yang_parent_name = "enhanced-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interval']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                    ])
                                    self.interval = None
                                    self.buckets = None
                                    self._segment_path = lambda: "enhanced-stat" + "[interval='" + str(self.interval) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpEcho.EnhancedStats.EnhancedStat, ['interval', 'buckets'], name, value)


                    class MplsLspTrace(Entity):
                        """
                        MPLS LSP Trace Operation type
                        
                        .. attribute:: target
                        
                        	Target for the MPLS LSP operation
                        	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target>`
                        
                        .. attribute:: reply
                        
                        	Echo reply options for the MPLS LSP operation
                        	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply>`
                        
                        .. attribute:: ttl
                        
                        	Time to live value
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 30
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: output_nexthop
                        
                        	Echo request output nexthop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: lsp_selector
                        
                        	Attributes used for path selection during LSP load balancing
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 1.0.0.127
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics>`
                        
                        .. attribute:: exp_bits
                        
                        	EXP bits in MPLS LSP echo reply header
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 0
                        
                        .. attribute:: force_explicit_null
                        
                        	Forced option for the MPLS LSP operation
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: history
                        
                        	Configure the history parameters for this operation
                        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History>`
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: output_interface
                        
                        	Echo request output interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace, self).__init__()

                            self.yang_name = "mpls-lsp-trace"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("target", ("target", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target)), ("reply", ("reply", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics)), ("history", ("history", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History))])
                            self._leafs = OrderedDict([
                                ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('output_nexthop', (YLeaf(YType.str, 'output-nexthop'), ['str'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('lsp_selector', (YLeaf(YType.str, 'lsp-selector'), ['str'])),
                                ('exp_bits', (YLeaf(YType.uint32, 'exp-bits'), ['int'])),
                                ('force_explicit_null', (YLeaf(YType.empty, 'force-explicit-null'), ['Empty'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('output_interface', (YLeaf(YType.str, 'output-interface'), ['str'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.ttl = None
                            self.source_address = None
                            self.output_nexthop = None
                            self.create = None
                            self.lsp_selector = None
                            self.exp_bits = None
                            self.force_explicit_null = None
                            self.timeout = None
                            self.output_interface = None
                            self.frequency = None
                            self.tag = None

                            self.target = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target()
                            self.target.parent = self
                            self._children_name_map["target"] = "target"

                            self.reply = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply()
                            self.reply.parent = self
                            self._children_name_map["reply"] = "reply"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.history = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History()
                            self.history.parent = self
                            self._children_name_map["history"] = "history"
                            self._segment_path = lambda: "mpls-lsp-trace"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace, ['ttl', 'source_address', 'output_nexthop', 'create', 'lsp_selector', 'exp_bits', 'force_explicit_null', 'timeout', 'output_interface', 'frequency', 'tag'], name, value)


                        class Target(Entity):
                            """
                            Target for the MPLS LSP operation
                            
                            .. attribute:: traffic_engineering
                            
                            	Traffic engineering target
                            	**type**\:  :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering>`
                            
                            .. attribute:: ipv4
                            
                            	Target specified as an IPv4 address
                            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target, self).__init__()

                                self.yang_name = "target"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("traffic-engineering", ("traffic_engineering", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering)), ("ipv4", ("ipv4", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4))])
                                self._leafs = OrderedDict()

                                self.traffic_engineering = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering()
                                self.traffic_engineering.parent = self
                                self._children_name_map["traffic_engineering"] = "traffic-engineering"

                                self.ipv4 = Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4()
                                self.ipv4.parent = self
                                self._children_name_map["ipv4"] = "ipv4"
                                self._segment_path = lambda: "target"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target, [], name, value)


                            class TrafficEngineering(Entity):
                                """
                                Traffic engineering target
                                
                                .. attribute:: tunnel
                                
                                	Tunnel interface number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering, self).__init__()

                                    self.yang_name = "traffic-engineering"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tunnel', (YLeaf(YType.uint32, 'tunnel'), ['int'])),
                                    ])
                                    self.tunnel = None
                                    self._segment_path = lambda: "traffic-engineering"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.TrafficEngineering, ['tunnel'], name, value)


                            class Ipv4(Entity):
                                """
                                Target specified as an IPv4 address
                                
                                .. attribute:: fec_address
                                
                                	Target FEC address with mask
                                	**type**\:  :py:class:`FecAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4, self).__init__()

                                    self.yang_name = "ipv4"
                                    self.yang_parent_name = "target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("fec-address", ("fec_address", Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress))])
                                    self._leafs = OrderedDict()

                                    self.fec_address = None
                                    self._children_name_map["fec_address"] = "fec-address"
                                    self._segment_path = lambda: "ipv4"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4, [], name, value)


                                class FecAddress(Entity):
                                    """
                                    Target FEC address with mask
                                    
                                    .. attribute:: address
                                    
                                    	IP address for target
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: mask
                                    
                                    	IP netmask for target
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'man-ipsla-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress, self).__init__()

                                        self.yang_name = "fec-address"
                                        self.yang_parent_name = "ipv4"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                                        ])
                                        self.address = None
                                        self.mask = None
                                        self._segment_path = lambda: "fec-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Target.Ipv4.FecAddress, ['address', 'mask'], name, value)


                        class Reply(Entity):
                            """
                            Echo reply options for the MPLS LSP
                            operation
                            
                            .. attribute:: mode
                            
                            	Enables use of router alert in echo reply packets
                            	**type**\:  :py:class:`IpslaLspTraceReplyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspTraceReplyMode>`
                            
                            .. attribute:: dscp_bits
                            
                            	DSCP bits in the reply IP header
                            	**type**\: union of the below types:
                            
                            		**type**\:  :py:class:`IpslaLspReplyDscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaLspReplyDscp>`
                            
                            		**type**\: int
                            
                            			**range:** 0..63
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply, self).__init__()

                                self.yang_name = "reply"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspTraceReplyMode', '')])),
                                    ('dscp_bits', (YLeaf(YType.str, 'dscp-bits'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaLspReplyDscp', ''),'int'])),
                                ])
                                self.mode = None
                                self.dscp_bits = None
                                self._segment_path = lambda: "reply"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Reply, ['mode', 'dscp_bits'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                ])
                                self.hours = None
                                self.dist_interval = None
                                self.dist_count = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.Statistics, ['hours', 'dist_interval', 'dist_count'], name, value)


                        class History(Entity):
                            """
                            Configure the history parameters for this
                            operation
                            
                            .. attribute:: lives
                            
                            	Specify number of lives to be kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**default value**\: 0
                            
                            .. attribute:: history_filter
                            
                            	Choose type of data to be stored in history buffer
                            	**type**\:  :py:class:`IpslaHistoryFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaHistoryFilter>`
                            
                            .. attribute:: buckets
                            
                            	Specify number of history buckets
                            	**type**\: int
                            
                            	**range:** 1..60
                            
                            	**default value**\: 15
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History, self).__init__()

                                self.yang_name = "history"
                                self.yang_parent_name = "mpls-lsp-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lives', (YLeaf(YType.uint32, 'lives'), ['int'])),
                                    ('history_filter', (YLeaf(YType.enumeration, 'history-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter', '')])),
                                    ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                ])
                                self.lives = None
                                self.history_filter = None
                                self.buckets = None
                                self._segment_path = lambda: "history"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.MplsLspTrace.History, ['lives', 'history_filter', 'buckets'], name, value)


                    class UdpJitter(Entity):
                        """
                        UDPJitter Operation type
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize>`
                        
                        .. attribute:: packet
                        
                        	Probe packet stream configuration parameters
                        	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet>`
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: tos
                        
                        	Type of service setting in probe packet
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**default value**\: 0
                        
                        .. attribute:: control_disable
                        
                        	Disable control packets
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: source_port
                        
                        	Port number on source device
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics>`
                        
                        .. attribute:: vrf
                        
                        	Configure IPSLA for a VPN Routing/Forwarding instance)
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: dest_port
                        
                        	Port number on target device
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: verify_data
                        
                        	Check each IPSLA response for corruption
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: dest_address
                        
                        	Enter IPv4 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: enhanced_stats
                        
                        	Table of statistics collection intervals
                        	**type**\:  :py:class:`EnhancedStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats>`
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter, self).__init__()

                            self.yang_name = "udp-jitter"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize)), ("packet", ("packet", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics)), ("enhanced-stats", ("enhanced_stats", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats))])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                ('control_disable', (YLeaf(YType.empty, 'control-disable'), ['Empty'])),
                                ('source_port', (YLeaf(YType.uint16, 'source-port'), ['int'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('dest_port', (YLeaf(YType.uint16, 'dest-port'), ['int'])),
                                ('verify_data', (YLeaf(YType.empty, 'verify-data'), ['Empty'])),
                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.source_address = None
                            self.tos = None
                            self.control_disable = None
                            self.source_port = None
                            self.create = None
                            self.vrf = None
                            self.timeout = None
                            self.frequency = None
                            self.dest_port = None
                            self.verify_data = None
                            self.dest_address = None
                            self.tag = None

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.packet = Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet()
                            self.packet.parent = self
                            self._children_name_map["packet"] = "packet"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.enhanced_stats = Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats()
                            self.enhanced_stats.parent = self
                            self._children_name_map["enhanced_stats"] = "enhanced-stats"
                            self._segment_path = lambda: "udp-jitter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter, ['source_address', 'tos', 'control_disable', 'source_port', 'create', 'vrf', 'timeout', 'frequency', 'dest_port', 'verify_data', 'dest_address', 'tag'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 28..1500
                            
                            	**units**\: byte
                            
                            	**default value**\: 32
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "udp-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.DataSize, ['request'], name, value)


                        class Packet(Entity):
                            """
                            Probe packet stream configuration
                            parameters
                            
                            .. attribute:: count
                            
                            	Number of packets to be transmitted during a probe
                            	**type**\: int
                            
                            	**range:** 1..60000
                            
                            	**default value**\: 10
                            
                            .. attribute:: interval
                            
                            	Packet interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..60000
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet, self).__init__()

                                self.yang_name = "packet"
                                self.yang_parent_name = "udp-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.count = None
                                self.interval = None
                                self._segment_path = lambda: "packet"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Packet, ['count', 'interval'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an hour
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "udp-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                ])
                                self.hours = None
                                self.dist_interval = None
                                self.dist_count = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.Statistics, ['hours', 'dist_interval', 'dist_count'], name, value)


                        class EnhancedStats(Entity):
                            """
                            Table of statistics collection intervals
                            
                            .. attribute:: enhanced_stat
                            
                            	Statistics for a specified time interval
                            	**type**\: list of  		 :py:class:`EnhancedStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats, self).__init__()

                                self.yang_name = "enhanced-stats"
                                self.yang_parent_name = "udp-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enhanced-stat", ("enhanced_stat", Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat))])
                                self._leafs = OrderedDict()

                                self.enhanced_stat = YList(self)
                                self._segment_path = lambda: "enhanced-stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats, [], name, value)


                            class EnhancedStat(Entity):
                                """
                                Statistics for a specified time interval
                                
                                .. attribute:: interval  (key)
                                
                                	Interval in seconds
                                	**type**\: int
                                
                                	**range:** 1..3600
                                
                                	**units**\: second
                                
                                .. attribute:: buckets
                                
                                	Buckets of enhanced statistics kept
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**default value**\: 15
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat, self).__init__()

                                    self.yang_name = "enhanced-stat"
                                    self.yang_parent_name = "enhanced-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interval']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                    ])
                                    self.interval = None
                                    self.buckets = None
                                    self._segment_path = lambda: "enhanced-stat" + "[interval='" + str(self.interval) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.UdpJitter.EnhancedStats.EnhancedStat, ['interval', 'buckets'], name, value)


                    class IcmpPathEcho(Entity):
                        """
                        ICMPPathEcho Operation type
                        
                        .. attribute:: history
                        
                        	Configure the history parameters for this operation
                        	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History>`
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize>`
                        
                        .. attribute:: statistics
                        
                        	Statistics collection aggregated over an hour
                        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics>`
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: tos
                        
                        	Type of service setting in probe packet
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**default value**\: 0
                        
                        .. attribute:: lsr_path
                        
                        	Loose source routing path (up to 8 intermediate nodes)
                        	**type**\:  :py:class:`LsrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: vrf
                        
                        	Configure IPSLA for a VPN Routing/Forwarding instance)
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: dest_address
                        
                        	Enter IPv4 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho, self).__init__()

                            self.yang_name = "icmp-path-echo"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("history", ("history", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History)), ("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize)), ("statistics", ("statistics", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics)), ("lsr-path", ("lsr_path", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath))])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.source_address = None
                            self.tos = None
                            self.create = None
                            self.vrf = None
                            self.timeout = None
                            self.frequency = None
                            self.dest_address = None
                            self.tag = None

                            self.history = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History()
                            self.history.parent = self
                            self._children_name_map["history"] = "history"

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.statistics = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics()
                            self.statistics.parent = self
                            self._children_name_map["statistics"] = "statistics"

                            self.lsr_path = None
                            self._children_name_map["lsr_path"] = "lsr-path"
                            self._segment_path = lambda: "icmp-path-echo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho, ['source_address', 'tos', 'create', 'vrf', 'timeout', 'frequency', 'dest_address', 'tag'], name, value)


                        class History(Entity):
                            """
                            Configure the history parameters for this
                            operation
                            
                            .. attribute:: samples
                            
                            	Specify number of samples to keep
                            	**type**\: int
                            
                            	**range:** 1..30
                            
                            	**default value**\: 16
                            
                            .. attribute:: buckets
                            
                            	Specify number of history buckets
                            	**type**\: int
                            
                            	**range:** 1..60
                            
                            	**default value**\: 15
                            
                            .. attribute:: history_filter
                            
                            	Choose type of data to be stored in history buffer
                            	**type**\:  :py:class:`IpslaHistoryFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.IpslaHistoryFilter>`
                            
                            .. attribute:: lives
                            
                            	Specify number of lives to be kept
                            	**type**\: int
                            
                            	**range:** 0..2
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History, self).__init__()

                                self.yang_name = "history"
                                self.yang_parent_name = "icmp-path-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('samples', (YLeaf(YType.uint32, 'samples'), ['int'])),
                                    ('buckets', (YLeaf(YType.uint32, 'buckets'), ['int'])),
                                    ('history_filter', (YLeaf(YType.enumeration, 'history-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg', 'IpslaHistoryFilter', '')])),
                                    ('lives', (YLeaf(YType.uint32, 'lives'), ['int'])),
                                ])
                                self.samples = None
                                self.buckets = None
                                self.history_filter = None
                                self.lives = None
                                self._segment_path = lambda: "history"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.History, ['samples', 'buckets', 'history_filter', 'lives'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 0..16384
                            
                            	**units**\: byte
                            
                            	**default value**\: 36
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "icmp-path-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.DataSize, ['request'], name, value)


                        class Statistics(Entity):
                            """
                            Statistics collection aggregated over an
                            hour
                            
                            .. attribute:: paths
                            
                            	Maximum number of paths for which statistics are kept
                            	**type**\: int
                            
                            	**range:** 1..128
                            
                            	**default value**\: 5
                            
                            .. attribute:: dist_interval
                            
                            	Specify distribution interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            .. attribute:: dist_count
                            
                            	Count of distribution intervals maintained
                            	**type**\: int
                            
                            	**range:** 1..20
                            
                            	**default value**\: 1
                            
                            .. attribute:: hours
                            
                            	Number of hours for which hourly statistics are kept
                            	**type**\: int
                            
                            	**range:** 0..25
                            
                            	**units**\: hour
                            
                            	**default value**\: 2
                            
                            .. attribute:: hops
                            
                            	Maximum hops per path for which statistics are kept
                            	**type**\: int
                            
                            	**range:** 1..30
                            
                            	**default value**\: 16
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics, self).__init__()

                                self.yang_name = "statistics"
                                self.yang_parent_name = "icmp-path-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('paths', (YLeaf(YType.uint32, 'paths'), ['int'])),
                                    ('dist_interval', (YLeaf(YType.uint32, 'dist-interval'), ['int'])),
                                    ('dist_count', (YLeaf(YType.uint32, 'dist-count'), ['int'])),
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('hops', (YLeaf(YType.uint32, 'hops'), ['int'])),
                                ])
                                self.paths = None
                                self.dist_interval = None
                                self.dist_count = None
                                self.hours = None
                                self.hops = None
                                self._segment_path = lambda: "statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.Statistics, ['paths', 'dist_interval', 'dist_count', 'hours', 'hops'], name, value)


                        class LsrPath(Entity):
                            """
                            Loose source routing path (up to 8 intermediate
                            nodes)
                            
                            .. attribute:: node1
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: node2
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node3
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node4
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node5
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node6
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node7
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node8
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath, self).__init__()

                                self.yang_name = "lsr-path"
                                self.yang_parent_name = "icmp-path-echo"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('node1', (YLeaf(YType.str, 'node1'), ['str'])),
                                    ('node2', (YLeaf(YType.str, 'node2'), ['str'])),
                                    ('node3', (YLeaf(YType.str, 'node3'), ['str'])),
                                    ('node4', (YLeaf(YType.str, 'node4'), ['str'])),
                                    ('node5', (YLeaf(YType.str, 'node5'), ['str'])),
                                    ('node6', (YLeaf(YType.str, 'node6'), ['str'])),
                                    ('node7', (YLeaf(YType.str, 'node7'), ['str'])),
                                    ('node8', (YLeaf(YType.str, 'node8'), ['str'])),
                                ])
                                self.node1 = None
                                self.node2 = None
                                self.node3 = None
                                self.node4 = None
                                self.node5 = None
                                self.node6 = None
                                self.node7 = None
                                self.node8 = None
                                self._segment_path = lambda: "lsr-path"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathEcho.LsrPath, ['node1', 'node2', 'node3', 'node4', 'node5', 'node6', 'node7', 'node8'], name, value)


                    class IcmpPathJitter(Entity):
                        """
                        ICMPPathJitter Operation type
                        
                        .. attribute:: data_size
                        
                        	Protocol data size in payload of probe packets
                        	**type**\:  :py:class:`DataSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize>`
                        
                        .. attribute:: packet
                        
                        	Probe packet stream configuration parameters
                        	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet>`
                        
                        .. attribute:: source_address
                        
                        	Enter IPv4 address of the source device
                        	**type**\: str
                        
                        .. attribute:: tos
                        
                        	Type of service setting in probe packet
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**default value**\: 0
                        
                        .. attribute:: lsr_path
                        
                        	Loose source routing path (up to 8 intermediate nodes)
                        	**type**\:  :py:class:`LsrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: create
                        
                        	Create operation with specified type
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: vrf
                        
                        	Configure IPSLA for a VPN Routing/Forwarding instance)
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: timeout
                        
                        	Probe/Control timeout in milliseconds
                        	**type**\: int
                        
                        	**range:** 1..604800000
                        
                        	**units**\: millisecond
                        
                        	**default value**\: 5000
                        
                        .. attribute:: frequency
                        
                        	Probe interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..604800
                        
                        	**units**\: second
                        
                        	**default value**\: 60
                        
                        .. attribute:: dest_address
                        
                        	Enter IPv4 address of the destination device
                        	**type**\: str
                        
                        .. attribute:: tag
                        
                        	Add a tag for this operation
                        	**type**\: str
                        
                        	**length:** 1..100
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter, self).__init__()

                            self.yang_name = "icmp-path-jitter"
                            self.yang_parent_name = "operation-type"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("data-size", ("data_size", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize)), ("packet", ("packet", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet)), ("lsr-path", ("lsr_path", Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath))])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('frequency', (YLeaf(YType.uint32, 'frequency'), ['int'])),
                                ('dest_address', (YLeaf(YType.str, 'dest-address'), ['str'])),
                                ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ])
                            self.source_address = None
                            self.tos = None
                            self.create = None
                            self.vrf = None
                            self.timeout = None
                            self.frequency = None
                            self.dest_address = None
                            self.tag = None

                            self.data_size = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize()
                            self.data_size.parent = self
                            self._children_name_map["data_size"] = "data-size"

                            self.packet = Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet()
                            self.packet.parent = self
                            self._children_name_map["packet"] = "packet"

                            self.lsr_path = None
                            self._children_name_map["lsr_path"] = "lsr-path"
                            self._segment_path = lambda: "icmp-path-jitter"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter, ['source_address', 'tos', 'create', 'vrf', 'timeout', 'frequency', 'dest_address', 'tag'], name, value)


                        class DataSize(Entity):
                            """
                            Protocol data size in payload of probe
                            packets
                            
                            .. attribute:: request
                            
                            	Payload size in request probe packet
                            	**type**\: int
                            
                            	**range:** 0..16384
                            
                            	**units**\: byte
                            
                            	**default value**\: 36
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize, self).__init__()

                                self.yang_name = "data-size"
                                self.yang_parent_name = "icmp-path-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                ])
                                self.request = None
                                self._segment_path = lambda: "data-size"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.DataSize, ['request'], name, value)


                        class Packet(Entity):
                            """
                            Probe packet stream configuration
                            parameters
                            
                            .. attribute:: count
                            
                            	Number of packets to be transmitted during a probe
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**default value**\: 10
                            
                            .. attribute:: interval
                            
                            	Packet interval in milliseconds
                            	**type**\: int
                            
                            	**range:** 1..60000
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 20
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet, self).__init__()

                                self.yang_name = "packet"
                                self.yang_parent_name = "icmp-path-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.count = None
                                self.interval = None
                                self._segment_path = lambda: "packet"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.Packet, ['count', 'interval'], name, value)


                        class LsrPath(Entity):
                            """
                            Loose source routing path (up to 8 intermediate
                            nodes)
                            
                            .. attribute:: node1
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: node2
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node3
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node4
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node5
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node6
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node7
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: node8
                            
                            	IPv4 address of the intermediate node
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath, self).__init__()

                                self.yang_name = "lsr-path"
                                self.yang_parent_name = "icmp-path-jitter"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('node1', (YLeaf(YType.str, 'node1'), ['str'])),
                                    ('node2', (YLeaf(YType.str, 'node2'), ['str'])),
                                    ('node3', (YLeaf(YType.str, 'node3'), ['str'])),
                                    ('node4', (YLeaf(YType.str, 'node4'), ['str'])),
                                    ('node5', (YLeaf(YType.str, 'node5'), ['str'])),
                                    ('node6', (YLeaf(YType.str, 'node6'), ['str'])),
                                    ('node7', (YLeaf(YType.str, 'node7'), ['str'])),
                                    ('node8', (YLeaf(YType.str, 'node8'), ['str'])),
                                ])
                                self.node1 = None
                                self.node2 = None
                                self.node3 = None
                                self.node4 = None
                                self.node5 = None
                                self.node6 = None
                                self.node7 = None
                                self.node8 = None
                                self._segment_path = lambda: "lsr-path"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Operation.Definitions.Definition.OperationType.IcmpPathJitter.LsrPath, ['node1', 'node2', 'node3', 'node4', 'node5', 'node6', 'node7', 'node8'], name, value)


    class Responder(Entity):
        """
        Responder configuration
        
        .. attribute:: twamp
        
        	Responder TWAMP configuration
        	**type**\:  :py:class:`Twamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Twamp>`
        
        .. attribute:: type
        
        	Configure IPSLA Responder port type
        	**type**\:  :py:class:`Type <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type>`
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.Responder, self).__init__()

            self.yang_name = "responder"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("twamp", ("twamp", Ipsla.Responder.Twamp)), ("type", ("type", Ipsla.Responder.Type))])
            self._leafs = OrderedDict()

            self.twamp = Ipsla.Responder.Twamp()
            self.twamp.parent = self
            self._children_name_map["twamp"] = "twamp"

            self.type = Ipsla.Responder.Type()
            self.type.parent = self
            self._children_name_map["type"] = "type"
            self._segment_path = lambda: "responder"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.Responder, [], name, value)


        class Twamp(Entity):
            """
            Responder TWAMP configuration
            
            .. attribute:: timeout
            
            	Configure responder timeout value in seconds
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 900
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Responder.Twamp, self).__init__()

                self.yang_name = "twamp"
                self.yang_parent_name = "responder"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ])
                self.timeout = None
                self._segment_path = lambda: "twamp"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/responder/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Responder.Twamp, ['timeout'], name, value)


        class Type(Entity):
            """
            Configure IPSLA Responder port type
            
            .. attribute:: udp
            
            	Configure IPSLA Responder UDP address and port
            	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type.Udp>`
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.Responder.Type, self).__init__()

                self.yang_name = "type"
                self.yang_parent_name = "responder"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("udp", ("udp", Ipsla.Responder.Type.Udp))])
                self._leafs = OrderedDict()

                self.udp = Ipsla.Responder.Type.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
                self._segment_path = lambda: "type"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/responder/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.Responder.Type, [], name, value)


            class Udp(Entity):
                """
                Configure IPSLA Responder UDP address and port
                
                .. attribute:: addresses
                
                	Configure IP address
                	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type.Udp.Addresses>`
                
                

                """

                _prefix = 'man-ipsla-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipsla.Responder.Type.Udp, self).__init__()

                    self.yang_name = "udp"
                    self.yang_parent_name = "type"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("addresses", ("addresses", Ipsla.Responder.Type.Udp.Addresses))])
                    self._leafs = OrderedDict()

                    self.addresses = Ipsla.Responder.Type.Udp.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._segment_path = lambda: "udp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/responder/type/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipsla.Responder.Type.Udp, [], name, value)


                class Addresses(Entity):
                    """
                    Configure IP address
                    
                    .. attribute:: address
                    
                    	Configure IP address for the permanent port
                    	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type.Udp.Addresses.Address>`
                    
                    

                    """

                    _prefix = 'man-ipsla-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipsla.Responder.Type.Udp.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "udp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Ipsla.Responder.Type.Udp.Addresses.Address))])
                        self._leafs = OrderedDict()

                        self.address = YList(self)
                        self._segment_path = lambda: "addresses"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/responder/type/udp/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipsla.Responder.Type.Udp.Addresses, [], name, value)


                    class Address(Entity):
                        """
                        Configure IP address for the permanent port
                        
                        .. attribute:: local_address  (key)
                        
                        	IP address of the Responder
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ports
                        
                        	Configure port
                        	**type**\:  :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type.Udp.Addresses.Address.Ports>`
                        
                        

                        """

                        _prefix = 'man-ipsla-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipsla.Responder.Type.Udp.Addresses.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['local_address']
                            self._child_classes = OrderedDict([("ports", ("ports", Ipsla.Responder.Type.Udp.Addresses.Address.Ports))])
                            self._leafs = OrderedDict([
                                ('local_address', (YLeaf(YType.str, 'local-address'), ['str'])),
                            ])
                            self.local_address = None

                            self.ports = Ipsla.Responder.Type.Udp.Addresses.Address.Ports()
                            self.ports.parent = self
                            self._children_name_map["ports"] = "ports"
                            self._segment_path = lambda: "address" + "[local-address='" + str(self.local_address) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/responder/type/udp/addresses/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipsla.Responder.Type.Udp.Addresses.Address, ['local_address'], name, value)


                        class Ports(Entity):
                            """
                            Configure port
                            
                            .. attribute:: port
                            
                            	Configure port number for the permanent port
                            	**type**\: list of  		 :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port>`
                            
                            

                            """

                            _prefix = 'man-ipsla-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipsla.Responder.Type.Udp.Addresses.Address.Ports, self).__init__()

                                self.yang_name = "ports"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("port", ("port", Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port))])
                                self._leafs = OrderedDict()

                                self.port = YList(self)
                                self._segment_path = lambda: "ports"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipsla.Responder.Type.Udp.Addresses.Address.Ports, [], name, value)


                            class Port(Entity):
                                """
                                Configure port number for the permanent
                                port
                                
                                .. attribute:: port  (key)
                                
                                	Port number to be enabled
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'man-ipsla-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port, self).__init__()

                                    self.yang_name = "port"
                                    self.yang_parent_name = "ports"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['port']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                                    ])
                                    self.port = None
                                    self._segment_path = lambda: "port" + "[port='" + str(self.port) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipsla.Responder.Type.Udp.Addresses.Address.Ports.Port, ['port'], name, value)


    class MplsDiscovery(Entity):
        """
        Provider Edge(PE) discovery configuration
        
        .. attribute:: vpn
        
        	Layer 3 VPN PE discovery configuration
        	**type**\:  :py:class:`Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ipsla_cfg.Ipsla.MplsDiscovery.Vpn>`
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.MplsDiscovery, self).__init__()

            self.yang_name = "mpls-discovery"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vpn", ("vpn", Ipsla.MplsDiscovery.Vpn))])
            self._leafs = OrderedDict()

            self.vpn = Ipsla.MplsDiscovery.Vpn()
            self.vpn.parent = self
            self._children_name_map["vpn"] = "vpn"
            self._segment_path = lambda: "mpls-discovery"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.MplsDiscovery, [], name, value)


        class Vpn(Entity):
            """
            Layer 3 VPN PE discovery configuration
            
            .. attribute:: interval
            
            	Specify a discovery refresh interval
            	**type**\: int
            
            	**range:** 30..70560
            
            	**units**\: minute
            
            	**default value**\: 300
            
            

            """

            _prefix = 'man-ipsla-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipsla.MplsDiscovery.Vpn, self).__init__()

                self.yang_name = "vpn"
                self.yang_parent_name = "mpls-discovery"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                ])
                self.interval = None
                self._segment_path = lambda: "vpn"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/mpls-discovery/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipsla.MplsDiscovery.Vpn, ['interval'], name, value)


    class ServerTwamp(Entity):
        """
        IPPM Server configuration
        
        .. attribute:: inactivity_timer
        
        	Configure ippmserver inactivity timer value in seconds
        	**type**\: int
        
        	**range:** 1..6000
        
        	**units**\: second
        
        	**default value**\: 900
        
        .. attribute:: port
        
        	Configure port number for ippmserver listening port
        	**type**\: int
        
        	**range:** 1..65535
        
        	**default value**\: 862
        
        

        """

        _prefix = 'man-ipsla-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipsla.ServerTwamp, self).__init__()

            self.yang_name = "server-twamp"
            self.yang_parent_name = "ipsla"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('inactivity_timer', (YLeaf(YType.uint32, 'inactivity-timer'), ['int'])),
                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
            ])
            self.inactivity_timer = None
            self.port = None
            self._segment_path = lambda: "server-twamp"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ipsla-cfg:ipsla/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipsla.ServerTwamp, ['inactivity_timer', 'port'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipsla()
        return self._top_entity


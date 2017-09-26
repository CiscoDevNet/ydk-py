""" Cisco_IOS_XR_ethernet_link_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package operational data.

This module contains definitions
for the following management objects\:
  ether\-link\-oam\: Ethernet Link OAM operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Action(Enum):
    """
    Action

    Actions supported by an OAM interface

    .. data:: no_action = 1

    	Disabled (do nothing)

    .. data:: disable_interface = 2

    	Disable the interface

    .. data:: log = 3

    	Log the event and do nothing else

    .. data:: efd = 4

    	EFD the interface

    """

    no_action = Enum.YLeaf(1, "no-action")

    disable_interface = Enum.YLeaf(2, "disable-interface")

    log = Enum.YLeaf(3, "log")

    efd = Enum.YLeaf(4, "efd")


class Log(Enum):
    """
    Log

    The type of a log entry

    .. data:: log_type_symbol_event = 1

    	Log entry for an errored symbol event

    .. data:: log_type_period_event = 2

    	Log entry for an errored frame period event

    .. data:: log_type_frame_event = 3

    	Log entry for an errored frame event

    .. data:: log_type_secs_event = 4

    	Log entry for an errored frame seconds summary

    	event

    .. data:: log_type_link_fault = 256

    	Log entry for a link fault

    .. data:: log_type_dying_gasp = 257

    	Log entry for a dying gasp

    .. data:: log_type_critical_event = 258

    	Log entry for a critical event

    """

    log_type_symbol_event = Enum.YLeaf(1, "log-type-symbol-event")

    log_type_period_event = Enum.YLeaf(2, "log-type-period-event")

    log_type_frame_event = Enum.YLeaf(3, "log-type-frame-event")

    log_type_secs_event = Enum.YLeaf(4, "log-type-secs-event")

    log_type_link_fault = Enum.YLeaf(256, "log-type-link-fault")

    log_type_dying_gasp = Enum.YLeaf(257, "log-type-dying-gasp")

    log_type_critical_event = Enum.YLeaf(258, "log-type-critical-event")


class LogLocation(Enum):
    """
    LogLocation

    The location of the event that caused a log entry

    .. data:: log_location_local = 1

    	A local event

    .. data:: log_location_remote = 2

    	A remote event

    """

    log_location_local = Enum.YLeaf(1, "log-location-local")

    log_location_remote = Enum.YLeaf(2, "log-location-remote")


class LoopbackStatus(Enum):
    """
    LoopbackStatus

    The loopback mode of an OAM interface

    .. data:: none = 1

    	Loopback is not being performed

    .. data:: initiating = 2

    	Initiating master loopback

    .. data:: master_loopback = 3

    	In master loopback mode

    .. data:: terminating = 4

    	Terminating master loopback mode

    .. data:: local_loopback = 5

    	In slave loopback mode

    .. data:: unknown = 6

    	Parser and multiplexer combination unexpected

    """

    none = Enum.YLeaf(1, "none")

    initiating = Enum.YLeaf(2, "initiating")

    master_loopback = Enum.YLeaf(3, "master-loopback")

    terminating = Enum.YLeaf(4, "terminating")

    local_loopback = Enum.YLeaf(5, "local-loopback")

    unknown = Enum.YLeaf(6, "unknown")


class Mode(Enum):
    """
    Mode

    Mode of an OAM interface

    .. data:: passive = 0

    	Passive mode

    .. data:: active = 1

    	Active mode

    .. data:: dont_care = 2

    	Don't care what the mode is

    """

    passive = Enum.YLeaf(0, "passive")

    active = Enum.YLeaf(1, "active")

    dont_care = Enum.YLeaf(2, "dont-care")


class OperationalState(Enum):
    """
    OperationalState

    Operational state of an interface

    .. data:: disabled = 1

    	802.3 OAM is disabled

    .. data:: link_fault = 2

    	802.3 OAM has encountered a link fault

    .. data:: passive_wait = 3

    	Passive OAM entity waiting to see if peer is

    	OAM capable

    .. data:: active_send_local = 4

    	Active OAM entity trying to determine if peer

    	is OAM capable

    .. data:: send_local_and_remote = 5

    	OAM discovered peer but still to accept or

    	reject peer config

    .. data:: send_local_and_remote_ok = 6

    	OAM peering is allowed by local device

    .. data:: peering_locally_rejected = 7

    	OAM peering rejected by local device

    .. data:: peering_remotely_rejected = 8

    	OAM peering rejected by remote device

    .. data:: operational = 9

    	802.3 OAM is operational

    .. data:: operational_half_duplex = 10

    	802.3 OAM is operating in half-duplex mode

    """

    disabled = Enum.YLeaf(1, "disabled")

    link_fault = Enum.YLeaf(2, "link-fault")

    passive_wait = Enum.YLeaf(3, "passive-wait")

    active_send_local = Enum.YLeaf(4, "active-send-local")

    send_local_and_remote = Enum.YLeaf(5, "send-local-and-remote")

    send_local_and_remote_ok = Enum.YLeaf(6, "send-local-and-remote-ok")

    peering_locally_rejected = Enum.YLeaf(7, "peering-locally-rejected")

    peering_remotely_rejected = Enum.YLeaf(8, "peering-remotely-rejected")

    operational = Enum.YLeaf(9, "operational")

    operational_half_duplex = Enum.YLeaf(10, "operational-half-duplex")


class ProtocolState(Enum):
    """
    ProtocolState

    The state the protocol is in

    .. data:: protocol_state_inactive = 0

    	The protocol is in the INACTIVE state

    .. data:: protocol_state_fault = 1

    	The protocol is in the FAULT state

    .. data:: protocol_state_active_send_local = 2

    	The protocol is in the ACTIVE_SEND_LOCAL state

    .. data:: protocol_state_passive_wait = 3

    	The protocol is in the SEND_LOCAL_REMOTE state

    .. data:: protocol_state_send_local_remote = 4

    	The protocol is in the LOCAL_REMOTE state

    .. data:: protocol_state_send_local_remote_ok = 5

    	The protocol is in the LOCAL_REMOTE_OK state

    .. data:: protocol_state_send_any = 6

    	The protocol is in the SEND_ANY state

    """

    protocol_state_inactive = Enum.YLeaf(0, "protocol-state-inactive")

    protocol_state_fault = Enum.YLeaf(1, "protocol-state-fault")

    protocol_state_active_send_local = Enum.YLeaf(2, "protocol-state-active-send-local")

    protocol_state_passive_wait = Enum.YLeaf(3, "protocol-state-passive-wait")

    protocol_state_send_local_remote = Enum.YLeaf(4, "protocol-state-send-local-remote")

    protocol_state_send_local_remote_ok = Enum.YLeaf(5, "protocol-state-send-local-remote-ok")

    protocol_state_send_any = Enum.YLeaf(6, "protocol-state-send-any")



class EtherLinkOam(Entity):
    """
    Ethernet Link OAM operational data
    
    .. attribute:: discovery_info_interfaces
    
    	Table of Ethernet Link OAM enabled interfaces within Discovery Info container
    	**type**\:   :py:class:`DiscoveryInfoInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.DiscoveryInfoInterfaces>`
    
    .. attribute:: event_log_entry_interfaces
    
    	Table of Ethernet Link OAM enabled interfaces within Event Log Entry container
    	**type**\:   :py:class:`EventLogEntryInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.EventLogEntryInterfaces>`
    
    .. attribute:: interface_state_interfaces
    
    	Table of Ethernet Link OAM enabled interfaces within Interface State container
    	**type**\:   :py:class:`InterfaceStateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.InterfaceStateInterfaces>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.Nodes>`
    
    .. attribute:: running_config_interfaces
    
    	Table of Ethernet Link OAM enabled interfaces within Running Config container
    	**type**\:   :py:class:`RunningConfigInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.RunningConfigInterfaces>`
    
    .. attribute:: stats_interfaces
    
    	Table of Ethernet Link OAM enabled interfaces within Stats container
    	**type**\:   :py:class:`StatsInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.StatsInterfaces>`
    
    

    """

    _prefix = 'ethernet-link-oam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(EtherLinkOam, self).__init__()
        self._top_entity = None

        self.yang_name = "ether-link-oam"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-link-oam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"discovery-info-interfaces" : ("discovery_info_interfaces", EtherLinkOam.DiscoveryInfoInterfaces), "event-log-entry-interfaces" : ("event_log_entry_interfaces", EtherLinkOam.EventLogEntryInterfaces), "interface-state-interfaces" : ("interface_state_interfaces", EtherLinkOam.InterfaceStateInterfaces), "nodes" : ("nodes", EtherLinkOam.Nodes), "running-config-interfaces" : ("running_config_interfaces", EtherLinkOam.RunningConfigInterfaces), "stats-interfaces" : ("stats_interfaces", EtherLinkOam.StatsInterfaces)}
        self._child_list_classes = {}

        self.discovery_info_interfaces = EtherLinkOam.DiscoveryInfoInterfaces()
        self.discovery_info_interfaces.parent = self
        self._children_name_map["discovery_info_interfaces"] = "discovery-info-interfaces"
        self._children_yang_names.add("discovery-info-interfaces")

        self.event_log_entry_interfaces = EtherLinkOam.EventLogEntryInterfaces()
        self.event_log_entry_interfaces.parent = self
        self._children_name_map["event_log_entry_interfaces"] = "event-log-entry-interfaces"
        self._children_yang_names.add("event-log-entry-interfaces")

        self.interface_state_interfaces = EtherLinkOam.InterfaceStateInterfaces()
        self.interface_state_interfaces.parent = self
        self._children_name_map["interface_state_interfaces"] = "interface-state-interfaces"
        self._children_yang_names.add("interface-state-interfaces")

        self.nodes = EtherLinkOam.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.running_config_interfaces = EtherLinkOam.RunningConfigInterfaces()
        self.running_config_interfaces.parent = self
        self._children_name_map["running_config_interfaces"] = "running-config-interfaces"
        self._children_yang_names.add("running-config-interfaces")

        self.stats_interfaces = EtherLinkOam.StatsInterfaces()
        self.stats_interfaces.parent = self
        self._children_name_map["stats_interfaces"] = "stats-interfaces"
        self._children_yang_names.add("stats-interfaces")
        self._segment_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam"


    class DiscoveryInfoInterfaces(Entity):
        """
        Table of Ethernet Link OAM enabled interfaces
        within Discovery Info container
        
        .. attribute:: discovery_info_interface
        
        	Ethernet Link OAM interface to get Discovery Info for
        	**type**\: list of    :py:class:`DiscoveryInfoInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.DiscoveryInfoInterfaces, self).__init__()

            self.yang_name = "discovery-info-interfaces"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"discovery-info-interface" : ("discovery_info_interface", EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface)}

            self.discovery_info_interface = YList(self)
            self._segment_path = lambda: "discovery-info-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.DiscoveryInfoInterfaces, [], name, value)


        class DiscoveryInfoInterface(Entity):
            """
            Ethernet Link OAM interface to get Discovery
            Info for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: local_evaluating
            
            	Is the local OAM session evaluating?
            	**type**\:  bool
            
            .. attribute:: local_function_event
            
            	Local event support
            	**type**\:  bool
            
            .. attribute:: local_function_event_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_function_loopback
            
            	Local loopback support
            	**type**\:  bool
            
            .. attribute:: local_function_loopback_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_function_unidirectional
            
            	Local Unidirectional support
            	**type**\:  bool
            
            .. attribute:: local_function_unidirectional_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_functionvariable
            
            	Local variable retreival support
            	**type**\:  bool
            
            .. attribute:: local_functionvariable_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_mode
            
            	Local Mode (passive/active)
            	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Mode>`
            
            .. attribute:: local_mode_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_mtu
            
            	Local MTU
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mtu_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_mwd_key
            
            	Local Mis\-wiring Detection key
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mwd_key_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: local_operational
            
            	Is the local OAM session operational?
            	**type**\:  bool
            
            .. attribute:: local_revision
            
            	Local revision
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_revisionvalid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: loopback_mode
            
            	The loopback mode the interface is in
            	**type**\:   :py:class:`LoopbackStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.LoopbackStatus>`
            
            .. attribute:: loopback_mode_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: miswired
            
            	Has the interface mis\-wired?
            	**type**\:  bool
            
            .. attribute:: miswired_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: name
            
            	Interface Name
            	**type**\:  str
            
            .. attribute:: operational_status
            
            	Operational status
            	**type**\:   :py:class:`OperationalState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.OperationalState>`
            
            .. attribute:: operational_status_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: received_at_risk_notification_time_remaining
            
            	Number of seconds remaining that the peer has indicated it will be At Risk
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: second
            
            .. attribute:: received_at_risk_notification_timestamp
            
            	Timestamp of when the last At Risk notification was received (in seconds since the UNIX epoch), or 0 if the peer is not currently at risk
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: remote_event
            
            	Remote event support
            	**type**\:  bool
            
            .. attribute:: remote_event_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_loopback
            
            	Remote loopback support
            	**type**\:  bool
            
            .. attribute:: remote_loopback_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_mac_address
            
            	Remote MAC address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: remote_mac_address_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_mode
            
            	Remote Mode (passive/active)
            	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Mode>`
            
            .. attribute:: remote_mode_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_mtu
            
            	Remote MTU
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mtu_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_mwd_key
            
            	Remote Mis\-wiring Detection key
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mwd_key_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_revision
            
            	Remote revision
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: remote_revisionvalid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_unidirectional
            
            	Remote unidirectional support
            	**type**\:  bool
            
            .. attribute:: remote_unidirectional_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_variable
            
            	Remote variable retreival support
            	**type**\:  bool
            
            .. attribute:: remote_variable_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_vendor_info
            
            	Remote vendor info
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_vendor_info_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            .. attribute:: remote_vendor_oui
            
            	Remote vendor OUI
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: remote_vendor_oui_valid
            
            	Has this value been received successfully?
            	**type**\:  bool
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface, self).__init__()

                self.yang_name = "discovery-info-interface"
                self.yang_parent_name = "discovery-info-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.local_evaluating = YLeaf(YType.boolean, "local-evaluating")

                self.local_function_event = YLeaf(YType.boolean, "local-function-event")

                self.local_function_event_valid = YLeaf(YType.boolean, "local-function-event-valid")

                self.local_function_loopback = YLeaf(YType.boolean, "local-function-loopback")

                self.local_function_loopback_valid = YLeaf(YType.boolean, "local-function-loopback-valid")

                self.local_function_unidirectional = YLeaf(YType.boolean, "local-function-unidirectional")

                self.local_function_unidirectional_valid = YLeaf(YType.boolean, "local-function-unidirectional-valid")

                self.local_functionvariable = YLeaf(YType.boolean, "local-functionvariable")

                self.local_functionvariable_valid = YLeaf(YType.boolean, "local-functionvariable-valid")

                self.local_mode = YLeaf(YType.enumeration, "local-mode")

                self.local_mode_valid = YLeaf(YType.boolean, "local-mode-valid")

                self.local_mtu = YLeaf(YType.uint32, "local-mtu")

                self.local_mtu_valid = YLeaf(YType.boolean, "local-mtu-valid")

                self.local_mwd_key = YLeaf(YType.uint32, "local-mwd-key")

                self.local_mwd_key_valid = YLeaf(YType.boolean, "local-mwd-key-valid")

                self.local_operational = YLeaf(YType.boolean, "local-operational")

                self.local_revision = YLeaf(YType.uint32, "local-revision")

                self.local_revisionvalid = YLeaf(YType.boolean, "local-revisionvalid")

                self.loopback_mode = YLeaf(YType.enumeration, "loopback-mode")

                self.loopback_mode_valid = YLeaf(YType.boolean, "loopback-mode-valid")

                self.miswired = YLeaf(YType.boolean, "miswired")

                self.miswired_valid = YLeaf(YType.boolean, "miswired-valid")

                self.name = YLeaf(YType.str, "name")

                self.operational_status = YLeaf(YType.enumeration, "operational-status")

                self.operational_status_valid = YLeaf(YType.boolean, "operational-status-valid")

                self.received_at_risk_notification_time_remaining = YLeaf(YType.uint16, "received-at-risk-notification-time-remaining")

                self.received_at_risk_notification_timestamp = YLeaf(YType.uint64, "received-at-risk-notification-timestamp")

                self.remote_event = YLeaf(YType.boolean, "remote-event")

                self.remote_event_valid = YLeaf(YType.boolean, "remote-event-valid")

                self.remote_loopback = YLeaf(YType.boolean, "remote-loopback")

                self.remote_loopback_valid = YLeaf(YType.boolean, "remote-loopback-valid")

                self.remote_mac_address = YLeaf(YType.str, "remote-mac-address")

                self.remote_mac_address_valid = YLeaf(YType.boolean, "remote-mac-address-valid")

                self.remote_mode = YLeaf(YType.enumeration, "remote-mode")

                self.remote_mode_valid = YLeaf(YType.boolean, "remote-mode-valid")

                self.remote_mtu = YLeaf(YType.uint32, "remote-mtu")

                self.remote_mtu_valid = YLeaf(YType.boolean, "remote-mtu-valid")

                self.remote_mwd_key = YLeaf(YType.uint32, "remote-mwd-key")

                self.remote_mwd_key_valid = YLeaf(YType.boolean, "remote-mwd-key-valid")

                self.remote_revision = YLeaf(YType.uint16, "remote-revision")

                self.remote_revisionvalid = YLeaf(YType.boolean, "remote-revisionvalid")

                self.remote_unidirectional = YLeaf(YType.boolean, "remote-unidirectional")

                self.remote_unidirectional_valid = YLeaf(YType.boolean, "remote-unidirectional-valid")

                self.remote_variable = YLeaf(YType.boolean, "remote-variable")

                self.remote_variable_valid = YLeaf(YType.boolean, "remote-variable-valid")

                self.remote_vendor_info = YLeaf(YType.uint32, "remote-vendor-info")

                self.remote_vendor_info_valid = YLeaf(YType.boolean, "remote-vendor-info-valid")

                self.remote_vendor_oui = YLeaf(YType.str, "remote-vendor-oui")

                self.remote_vendor_oui_valid = YLeaf(YType.boolean, "remote-vendor-oui-valid")
                self._segment_path = lambda: "discovery-info-interface" + "[member-interface='" + self.member_interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/discovery-info-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface, ['member_interface', 'local_evaluating', 'local_function_event', 'local_function_event_valid', 'local_function_loopback', 'local_function_loopback_valid', 'local_function_unidirectional', 'local_function_unidirectional_valid', 'local_functionvariable', 'local_functionvariable_valid', 'local_mode', 'local_mode_valid', 'local_mtu', 'local_mtu_valid', 'local_mwd_key', 'local_mwd_key_valid', 'local_operational', 'local_revision', 'local_revisionvalid', 'loopback_mode', 'loopback_mode_valid', 'miswired', 'miswired_valid', 'name', 'operational_status', 'operational_status_valid', 'received_at_risk_notification_time_remaining', 'received_at_risk_notification_timestamp', 'remote_event', 'remote_event_valid', 'remote_loopback', 'remote_loopback_valid', 'remote_mac_address', 'remote_mac_address_valid', 'remote_mode', 'remote_mode_valid', 'remote_mtu', 'remote_mtu_valid', 'remote_mwd_key', 'remote_mwd_key_valid', 'remote_revision', 'remote_revisionvalid', 'remote_unidirectional', 'remote_unidirectional_valid', 'remote_variable', 'remote_variable_valid', 'remote_vendor_info', 'remote_vendor_info_valid', 'remote_vendor_oui', 'remote_vendor_oui_valid'], name, value)


    class EventLogEntryInterfaces(Entity):
        """
        Table of Ethernet Link OAM enabled interfaces
        within Event Log Entry container
        
        .. attribute:: event_log_entry_interface
        
        	Ethernet Link OAM enabled interface to get Event Log Entry for
        	**type**\: list of    :py:class:`EventLogEntryInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.EventLogEntryInterfaces, self).__init__()

            self.yang_name = "event-log-entry-interfaces"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"event-log-entry-interface" : ("event_log_entry_interface", EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface)}

            self.event_log_entry_interface = YList(self)
            self._segment_path = lambda: "event-log-entry-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.EventLogEntryInterfaces, [], name, value)


        class EventLogEntryInterface(Entity):
            """
            Ethernet Link OAM enabled interface to get
            Event Log Entry for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: event_log_entry_indexes
            
            	Table of Ethernet Link OAM Event Log entries on the interface
            	**type**\:   :py:class:`EventLogEntryIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes>`
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface, self).__init__()

                self.yang_name = "event-log-entry-interface"
                self.yang_parent_name = "event-log-entry-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"event-log-entry-indexes" : ("event_log_entry_indexes", EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes)}
                self._child_list_classes = {}

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.event_log_entry_indexes = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes()
                self.event_log_entry_indexes.parent = self
                self._children_name_map["event_log_entry_indexes"] = "event-log-entry-indexes"
                self._children_yang_names.add("event-log-entry-indexes")
                self._segment_path = lambda: "event-log-entry-interface" + "[member-interface='" + self.member_interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/event-log-entry-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface, ['member_interface'], name, value)


            class EventLogEntryIndexes(Entity):
                """
                Table of Ethernet Link OAM Event Log entries
                on the interface
                
                .. attribute:: event_log_entry_index
                
                	Ethernet Link OAM Event Log Entry Index to get data for
                	**type**\: list of    :py:class:`EventLogEntryIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex>`
                
                

                """

                _prefix = 'ethernet-link-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes, self).__init__()

                    self.yang_name = "event-log-entry-indexes"
                    self.yang_parent_name = "event-log-entry-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"event-log-entry-index" : ("event_log_entry_index", EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex)}

                    self.event_log_entry_index = YList(self)
                    self._segment_path = lambda: "event-log-entry-indexes"

                def __setattr__(self, name, value):
                    self._perform_setattr(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes, [], name, value)


                class EventLogEntryIndex(Entity):
                    """
                    Ethernet Link OAM Event Log Entry Index to
                    get data for
                    
                    .. attribute:: event_log_entry_index  <key>
                    
                    	Event Log Entry index
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: action_taken
                    
                    	Local action taken (If applicable)
                    	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
                    
                    .. attribute:: event_total
                    
                    	Total number of times event has occurred
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: handle
                    
                    	Interface handle for this log entry
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: index
                    
                    	Index in the log entries table
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_high_threshold
                    
                    	Size of the local high threshold (If applicable) . For remote threshold events this is scaled for comparison with the Breaching Value. This is to account for different local and remote window sizes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: local_high_threshold_config_units
                    
                    	The local high threshold in the units that are currently configured
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: location
                    
                    	Where the event occurred
                    	**type**\:   :py:class:`LogLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.LogLocation>`
                    
                    .. attribute:: oui
                    
                    	OUI for the log entry
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: running_total
                    
                    	The running total number of errors seen since OAM was enabled on the interface(If applicable)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: threshold
                    
                    	Size of the threshold (If applicable)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: threshold_config_units
                    
                    	The threshold in the units that are currently configured
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: threshold_units
                    
                    	The units in which the threshold size is configured
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: timestamp
                    
                    	Timestamp in hundredths of a second since unix epoch for when the event occurred
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: type
                    
                    	Type of event that this entry describes
                    	**type**\:   :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Log>`
                    
                    .. attribute:: value
                    
                    	Breaching value (If applicable)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: value_config_units
                    
                    	The breaching value in the units that are currently configured
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: window
                    
                    	Size of the window (If applicable)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: window_config_units
                    
                    	The window in the units that are currently configured
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: window_units
                    
                    	The units in which the window size is configured 
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ethernet-link-oam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex, self).__init__()

                        self.yang_name = "event-log-entry-index"
                        self.yang_parent_name = "event-log-entry-indexes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.event_log_entry_index = YLeaf(YType.str, "event-log-entry-index")

                        self.action_taken = YLeaf(YType.enumeration, "action-taken")

                        self.event_total = YLeaf(YType.uint32, "event-total")

                        self.handle = YLeaf(YType.str, "handle")

                        self.index = YLeaf(YType.uint32, "index")

                        self.local_high_threshold = YLeaf(YType.uint64, "local-high-threshold")

                        self.local_high_threshold_config_units = YLeaf(YType.uint64, "local-high-threshold-config-units")

                        self.location = YLeaf(YType.enumeration, "location")

                        self.oui = YLeaf(YType.str, "oui")

                        self.running_total = YLeaf(YType.uint64, "running-total")

                        self.threshold = YLeaf(YType.uint64, "threshold")

                        self.threshold_config_units = YLeaf(YType.uint64, "threshold-config-units")

                        self.threshold_units = YLeaf(YType.uint8, "threshold-units")

                        self.timestamp = YLeaf(YType.uint64, "timestamp")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.value = YLeaf(YType.uint64, "value")

                        self.value_config_units = YLeaf(YType.uint64, "value-config-units")

                        self.window = YLeaf(YType.uint64, "window")

                        self.window_config_units = YLeaf(YType.uint64, "window-config-units")

                        self.window_units = YLeaf(YType.uint8, "window-units")
                        self._segment_path = lambda: "event-log-entry-index" + "[event-log-entry-index='" + self.event_log_entry_index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex, ['event_log_entry_index', 'action_taken', 'event_total', 'handle', 'index', 'local_high_threshold', 'local_high_threshold_config_units', 'location', 'oui', 'running_total', 'threshold', 'threshold_config_units', 'threshold_units', 'timestamp', 'type', 'value', 'value_config_units', 'window', 'window_config_units', 'window_units'], name, value)


    class InterfaceStateInterfaces(Entity):
        """
        Table of Ethernet Link OAM enabled interfaces
        within Interface State container
        
        .. attribute:: interface_state_interface
        
        	Ethernet Link OAM interface to get Interface State for
        	**type**\: list of    :py:class:`InterfaceStateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.InterfaceStateInterfaces, self).__init__()

            self.yang_name = "interface-state-interfaces"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface-state-interface" : ("interface_state_interface", EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface)}

            self.interface_state_interface = YList(self)
            self._segment_path = lambda: "interface-state-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.InterfaceStateInterfaces, [], name, value)


        class InterfaceStateInterface(Entity):
            """
            Ethernet Link OAM interface to get Interface
            State for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: efd_triggers
            
            	Any present EFD triggers
            	**type**\:   :py:class:`EfdTriggers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers>`
            
            .. attribute:: errors
            
            	The errors that have occurred on this interface
            	**type**\:   :py:class:`Errors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors>`
            
            .. attribute:: local_mwd_key
            
            	The local MWD key
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocol_code
            
            	The state the protocol is in
            	**type**\:   :py:class:`ProtocolState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ProtocolState>`
            
            .. attribute:: remote_mwd_key
            
            	The remote MWD key
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mwd_key_present
            
            	Does the remote side have an MWD key?
            	**type**\:  bool
            
            .. attribute:: rx_fault
            
            	Has a uni\-directional link\-fault been detected?
            	**type**\:  bool
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface, self).__init__()

                self.yang_name = "interface-state-interface"
                self.yang_parent_name = "interface-state-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"efd-triggers" : ("efd_triggers", EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers), "errors" : ("errors", EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors)}
                self._child_list_classes = {}

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.local_mwd_key = YLeaf(YType.uint32, "local-mwd-key")

                self.protocol_code = YLeaf(YType.enumeration, "protocol-code")

                self.remote_mwd_key = YLeaf(YType.uint32, "remote-mwd-key")

                self.remote_mwd_key_present = YLeaf(YType.boolean, "remote-mwd-key-present")

                self.rx_fault = YLeaf(YType.boolean, "rx-fault")

                self.efd_triggers = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers()
                self.efd_triggers.parent = self
                self._children_name_map["efd_triggers"] = "efd-triggers"
                self._children_yang_names.add("efd-triggers")

                self.errors = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors()
                self.errors.parent = self
                self._children_name_map["errors"] = "errors"
                self._children_yang_names.add("errors")
                self._segment_path = lambda: "interface-state-interface" + "[member-interface='" + self.member_interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/interface-state-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface, ['member_interface', 'local_mwd_key', 'protocol_code', 'remote_mwd_key', 'remote_mwd_key_present', 'rx_fault'], name, value)


            class EfdTriggers(Entity):
                """
                Any present EFD triggers
                
                .. attribute:: capabilities_conflict
                
                	A capabilities conflict has been detected
                	**type**\:  bool
                
                .. attribute:: discovery_timed_out
                
                	The discovery process has timed out
                	**type**\:  bool
                
                .. attribute:: link_fault_received
                
                	Link\-fault messages being received
                	**type**\:  bool
                
                .. attribute:: session_down
                
                	The 802.3 OAM session is down
                	**type**\:  bool
                
                .. attribute:: wiring_conflict
                
                	A wiring conflict has been detected
                	**type**\:  bool
                
                

                """

                _prefix = 'ethernet-link-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers, self).__init__()

                    self.yang_name = "efd-triggers"
                    self.yang_parent_name = "interface-state-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.capabilities_conflict = YLeaf(YType.boolean, "capabilities-conflict")

                    self.discovery_timed_out = YLeaf(YType.boolean, "discovery-timed-out")

                    self.link_fault_received = YLeaf(YType.boolean, "link-fault-received")

                    self.session_down = YLeaf(YType.boolean, "session-down")

                    self.wiring_conflict = YLeaf(YType.boolean, "wiring-conflict")
                    self._segment_path = lambda: "efd-triggers"

                def __setattr__(self, name, value):
                    self._perform_setattr(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers, ['capabilities_conflict', 'discovery_timed_out', 'link_fault_received', 'session_down', 'wiring_conflict'], name, value)


            class Errors(Entity):
                """
                The errors that have occurred on this interface
                
                .. attribute:: caps_add_error_code
                
                	The caps add error/success code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: caps_add_reason
                
                	Reason for the caps add error (if applicable)
                	**type**\:  str
                
                .. attribute:: epi_error_code
                
                	The Packet error/success code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: epi_reason
                
                	Reason for the Packet error (if applicable)
                	**type**\:  str
                
                .. attribute:: pfi_error_code
                
                	The Interface Management error/success code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pfi_reason
                
                	Reason for the Interface Management error (if applicable)
                	**type**\:  str
                
                .. attribute:: platform_error_code
                
                	The platform error/success code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: platform_reason
                
                	Reason for the platform error (if applicable)
                	**type**\:  str
                
                .. attribute:: spio_error_code
                
                	The Packet I/O error/success code
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: spio_reason
                
                	Reason for the Packet I/O error (if applicable)
                	**type**\:  str
                
                

                """

                _prefix = 'ethernet-link-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors, self).__init__()

                    self.yang_name = "errors"
                    self.yang_parent_name = "interface-state-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.caps_add_error_code = YLeaf(YType.uint32, "caps-add-error-code")

                    self.caps_add_reason = YLeaf(YType.str, "caps-add-reason")

                    self.epi_error_code = YLeaf(YType.uint32, "epi-error-code")

                    self.epi_reason = YLeaf(YType.str, "epi-reason")

                    self.pfi_error_code = YLeaf(YType.uint32, "pfi-error-code")

                    self.pfi_reason = YLeaf(YType.str, "pfi-reason")

                    self.platform_error_code = YLeaf(YType.uint32, "platform-error-code")

                    self.platform_reason = YLeaf(YType.str, "platform-reason")

                    self.spio_error_code = YLeaf(YType.uint32, "spio-error-code")

                    self.spio_reason = YLeaf(YType.str, "spio-reason")
                    self._segment_path = lambda: "errors"

                def __setattr__(self, name, value):
                    self._perform_setattr(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors, ['caps_add_error_code', 'caps_add_reason', 'epi_error_code', 'epi_reason', 'pfi_error_code', 'pfi_reason', 'platform_error_code', 'platform_reason', 'spio_error_code', 'spio_reason'], name, value)


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", EtherLinkOam.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	Ethernet Link OAM Summary information for the entire node
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"summary" : ("summary", EtherLinkOam.Nodes.Node.Summary)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.summary = EtherLinkOam.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.Nodes.Node, ['node_name'], name, value)


            class Summary(Entity):
                """
                Ethernet Link OAM Summary information for the
                entire node
                
                .. attribute:: active_send
                
                	The number of interfaces in 'Active Send' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: evaluating
                
                	The number of interfaces in 'Evaluating' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: events
                
                	The number of events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: interfaces
                
                	The number of interfaces with 802.3 OAM configured
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_accept
                
                	The number of interfaces in 'Local Accept' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_events
                
                	The number of local events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_frame
                
                	The mumber of local frame error events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_frame_period
                
                	The number of local frame period events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_frame_seconds
                
                	The number of local frame second events recoded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_reject
                
                	The number of interfaces in 'Local Reject' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_symbol_period
                
                	The number of local symbol period events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: loopback_mode
                
                	The number of interfaces in loopback mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: miswired_connections
                
                	The number of miswired connections
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational
                
                	The number of interfaces in 'Operational' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: passive_wait
                
                	The number of interfaces in 'Passive Wait' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_down
                
                	The number of interfaces in 'Port Down' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_events
                
                	The number of remote events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_frame
                
                	The mumber of remote frame error events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_frame_period
                
                	The number of remote frame period events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_frame_seconds
                
                	The number of remote frame second events recoded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_reject
                
                	The number of interfaces in 'Remote Reject' state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_symbol_period
                
                	The number of remote symbol period events recorded
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ethernet-link-oam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EtherLinkOam.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active_send = YLeaf(YType.uint32, "active-send")

                    self.evaluating = YLeaf(YType.uint32, "evaluating")

                    self.events = YLeaf(YType.uint64, "events")

                    self.interfaces = YLeaf(YType.uint32, "interfaces")

                    self.local_accept = YLeaf(YType.uint32, "local-accept")

                    self.local_events = YLeaf(YType.uint64, "local-events")

                    self.local_frame = YLeaf(YType.uint64, "local-frame")

                    self.local_frame_period = YLeaf(YType.uint64, "local-frame-period")

                    self.local_frame_seconds = YLeaf(YType.uint64, "local-frame-seconds")

                    self.local_reject = YLeaf(YType.uint32, "local-reject")

                    self.local_symbol_period = YLeaf(YType.uint64, "local-symbol-period")

                    self.loopback_mode = YLeaf(YType.uint32, "loopback-mode")

                    self.miswired_connections = YLeaf(YType.uint32, "miswired-connections")

                    self.operational = YLeaf(YType.uint32, "operational")

                    self.passive_wait = YLeaf(YType.uint32, "passive-wait")

                    self.port_down = YLeaf(YType.uint32, "port-down")

                    self.remote_events = YLeaf(YType.uint64, "remote-events")

                    self.remote_frame = YLeaf(YType.uint64, "remote-frame")

                    self.remote_frame_period = YLeaf(YType.uint64, "remote-frame-period")

                    self.remote_frame_seconds = YLeaf(YType.uint64, "remote-frame-seconds")

                    self.remote_reject = YLeaf(YType.uint32, "remote-reject")

                    self.remote_symbol_period = YLeaf(YType.uint64, "remote-symbol-period")
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(EtherLinkOam.Nodes.Node.Summary, ['active_send', 'evaluating', 'events', 'interfaces', 'local_accept', 'local_events', 'local_frame', 'local_frame_period', 'local_frame_seconds', 'local_reject', 'local_symbol_period', 'loopback_mode', 'miswired_connections', 'operational', 'passive_wait', 'port_down', 'remote_events', 'remote_frame', 'remote_frame_period', 'remote_frame_seconds', 'remote_reject', 'remote_symbol_period'], name, value)


    class RunningConfigInterfaces(Entity):
        """
        Table of Ethernet Link OAM enabled interfaces
        within Running Config container
        
        .. attribute:: running_config_interface
        
        	Ethernet Link OAM interface to get Running Config for
        	**type**\: list of    :py:class:`RunningConfigInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.RunningConfigInterfaces, self).__init__()

            self.yang_name = "running-config-interfaces"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"running-config-interface" : ("running_config_interface", EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface)}

            self.running_config_interface = YList(self)
            self._segment_path = lambda: "running-config-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.RunningConfigInterfaces, [], name, value)


        class RunningConfigInterface(Entity):
            """
            Ethernet Link OAM interface to get Running
            Config for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: capabilities_conflict_action
            
            	Action to perform when a capabilities conflict occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: capabilities_conflict_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: connection_timeout
            
            	Connection timeout
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: connection_timeout_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: critical_event_action
            
            	Action to perform when a critical event occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: critical_event_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: discovery_timeout_action
            
            	Action to perform when a discovery timeout occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: discovery_timeout_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: dying_gasp_action
            
            	Action to perform when a dying gasp occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: dying_gasp_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: fast_hello_interval_enabled
            
            	Is 100ms hello interval time enabled?
            	**type**\:  bool
            
            .. attribute:: fast_hello_interval_enabled_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_period_threshold_high
            
            	Frame period event high threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_period_threshold_high_multiplier
            
            	Frame period event threshold high multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_period_threshold_high_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_period_threshold_low
            
            	Frame period event low threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_period_threshold_low_multiplier
            
            	Frame period event threshold low multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_period_threshold_low_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_period_threshold_units
            
            	Frame period event threshold units
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_period_window
            
            	Frame period event window size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frame_period_window_multiplier
            
            	Frame period event window multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_period_window_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_period_window_units
            
            	Frame period event window units
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_seconds_threshold_high
            
            	Frame seconds event high threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: frame_seconds_threshold_high_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_seconds_threshold_low
            
            	Frame seconds event high threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: frame_seconds_threshold_low_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_seconds_window
            
            	Frame seconds event high threshold
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: frame_seconds_window_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_threshold_high
            
            	Frame event high threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_threshold_high_multiplier
            
            	Frame event threshold high multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_threshold_high_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_threshold_low
            
            	Frame event low threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: frame_threshold_low_multiplier
            
            	Frame period event threshold low multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: frame_threshold_low_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: frame_window
            
            	Frame event window size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frame_window_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: high_threshold_action
            
            	Action to perform when a high threshold is breached
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: high_threshold_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: link_fault_action
            
            	Action to perform when a link fault occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: link_fault_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: link_monitor_enabled
            
            	Is link monitoring enabled?
            	**type**\:  bool
            
            .. attribute:: link_monitoring_enabled_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: mib_retrieval_enabled
            
            	Is MIB retrieval enabled?
            	**type**\:  bool
            
            .. attribute:: mib_retrieval_enabled_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: mode
            
            	Configured mode
            	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Mode>`
            
            .. attribute:: mode_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: remote_loopback_action
            
            	Action to perform when a session enters or exits remote loopback
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: remote_loopback_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: remote_loopback_enabled
            
            	Is remote loopback enabled?
            	**type**\:  bool
            
            .. attribute:: remote_loopback_enabled_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: require_link_monitoring
            
            	Require the remote peer to support link monitoring
            	**type**\:  bool
            
            .. attribute:: require_link_monitoring_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: require_loopback
            
            	Require the remote peer to support loopback mode
            	**type**\:  bool
            
            .. attribute:: require_loopback_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: require_mib_retrieval_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: require_mode_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: require_remote_mib_retrieval
            
            	Require the remote peer to support MIB retrieval
            	**type**\:  bool
            
            .. attribute:: require_remote_mode
            
            	The mode that is required of the remote peer
            	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Mode>`
            
            .. attribute:: session_down_action
            
            	Action to perform when a session comes down
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: session_down_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: session_up_action
            
            	Action to perform when a session comes up
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: session_up_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: symbol_period_threshold_high
            
            	Symbol period event high threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: symbol_period_threshold_high_multiplier
            
            	Symbol period event threshold high multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: symbol_period_threshold_high_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: symbol_period_threshold_low
            
            	Symbol period event low threshold
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: symbol_period_threshold_low_multiplier
            
            	Symbol period event threshold low multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: symbol_period_threshold_low_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: symbol_period_threshold_units
            
            	Symbol period event threshold units
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: symbol_period_window
            
            	Symbol period event window size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: symbol_period_window_multiplier
            
            	Symbol period event window multiplier
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: symbol_period_window_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: symbol_period_window_units
            
            	Symbol period event window units
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: udlf_enabled
            
            	Is uni\-directional link\-fault detection enabled?
            	**type**\:  bool
            
            .. attribute:: udlf_enabled_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: wiring_conflict_action
            
            	Action to perform when a wiring conflict occurs
            	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.Action>`
            
            .. attribute:: wiring_conflict_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface, self).__init__()

                self.yang_name = "running-config-interface"
                self.yang_parent_name = "running-config-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.capabilities_conflict_action = YLeaf(YType.enumeration, "capabilities-conflict-action")

                self.capabilities_conflict_action_overridden = YLeaf(YType.boolean, "capabilities-conflict-action-overridden")

                self.connection_timeout = YLeaf(YType.uint8, "connection-timeout")

                self.connection_timeout_overridden = YLeaf(YType.boolean, "connection-timeout-overridden")

                self.critical_event_action = YLeaf(YType.enumeration, "critical-event-action")

                self.critical_event_action_overridden = YLeaf(YType.boolean, "critical-event-action-overridden")

                self.discovery_timeout_action = YLeaf(YType.enumeration, "discovery-timeout-action")

                self.discovery_timeout_action_overridden = YLeaf(YType.boolean, "discovery-timeout-action-overridden")

                self.dying_gasp_action = YLeaf(YType.enumeration, "dying-gasp-action")

                self.dying_gasp_action_overridden = YLeaf(YType.boolean, "dying-gasp-action-overridden")

                self.fast_hello_interval_enabled = YLeaf(YType.boolean, "fast-hello-interval-enabled")

                self.fast_hello_interval_enabled_overridden = YLeaf(YType.boolean, "fast-hello-interval-enabled-overridden")

                self.frame_period_threshold_high = YLeaf(YType.uint64, "frame-period-threshold-high")

                self.frame_period_threshold_high_multiplier = YLeaf(YType.uint8, "frame-period-threshold-high-multiplier")

                self.frame_period_threshold_high_overridden = YLeaf(YType.boolean, "frame-period-threshold-high-overridden")

                self.frame_period_threshold_low = YLeaf(YType.uint64, "frame-period-threshold-low")

                self.frame_period_threshold_low_multiplier = YLeaf(YType.uint8, "frame-period-threshold-low-multiplier")

                self.frame_period_threshold_low_overridden = YLeaf(YType.boolean, "frame-period-threshold-low-overridden")

                self.frame_period_threshold_units = YLeaf(YType.uint8, "frame-period-threshold-units")

                self.frame_period_window = YLeaf(YType.uint32, "frame-period-window")

                self.frame_period_window_multiplier = YLeaf(YType.uint8, "frame-period-window-multiplier")

                self.frame_period_window_overridden = YLeaf(YType.boolean, "frame-period-window-overridden")

                self.frame_period_window_units = YLeaf(YType.uint8, "frame-period-window-units")

                self.frame_seconds_threshold_high = YLeaf(YType.uint64, "frame-seconds-threshold-high")

                self.frame_seconds_threshold_high_overridden = YLeaf(YType.boolean, "frame-seconds-threshold-high-overridden")

                self.frame_seconds_threshold_low = YLeaf(YType.uint64, "frame-seconds-threshold-low")

                self.frame_seconds_threshold_low_overridden = YLeaf(YType.boolean, "frame-seconds-threshold-low-overridden")

                self.frame_seconds_window = YLeaf(YType.uint32, "frame-seconds-window")

                self.frame_seconds_window_overridden = YLeaf(YType.boolean, "frame-seconds-window-overridden")

                self.frame_threshold_high = YLeaf(YType.uint64, "frame-threshold-high")

                self.frame_threshold_high_multiplier = YLeaf(YType.uint8, "frame-threshold-high-multiplier")

                self.frame_threshold_high_overridden = YLeaf(YType.boolean, "frame-threshold-high-overridden")

                self.frame_threshold_low = YLeaf(YType.uint64, "frame-threshold-low")

                self.frame_threshold_low_multiplier = YLeaf(YType.uint8, "frame-threshold-low-multiplier")

                self.frame_threshold_low_overridden = YLeaf(YType.boolean, "frame-threshold-low-overridden")

                self.frame_window = YLeaf(YType.uint32, "frame-window")

                self.frame_window_overridden = YLeaf(YType.boolean, "frame-window-overridden")

                self.high_threshold_action = YLeaf(YType.enumeration, "high-threshold-action")

                self.high_threshold_action_overridden = YLeaf(YType.boolean, "high-threshold-action-overridden")

                self.link_fault_action = YLeaf(YType.enumeration, "link-fault-action")

                self.link_fault_action_overridden = YLeaf(YType.boolean, "link-fault-action-overridden")

                self.link_monitor_enabled = YLeaf(YType.boolean, "link-monitor-enabled")

                self.link_monitoring_enabled_overridden = YLeaf(YType.boolean, "link-monitoring-enabled-overridden")

                self.mib_retrieval_enabled = YLeaf(YType.boolean, "mib-retrieval-enabled")

                self.mib_retrieval_enabled_overridden = YLeaf(YType.boolean, "mib-retrieval-enabled-overridden")

                self.mode = YLeaf(YType.enumeration, "mode")

                self.mode_overridden = YLeaf(YType.boolean, "mode-overridden")

                self.remote_loopback_action = YLeaf(YType.enumeration, "remote-loopback-action")

                self.remote_loopback_action_overridden = YLeaf(YType.boolean, "remote-loopback-action-overridden")

                self.remote_loopback_enabled = YLeaf(YType.boolean, "remote-loopback-enabled")

                self.remote_loopback_enabled_overridden = YLeaf(YType.boolean, "remote-loopback-enabled-overridden")

                self.require_link_monitoring = YLeaf(YType.boolean, "require-link-monitoring")

                self.require_link_monitoring_overridden = YLeaf(YType.boolean, "require-link-monitoring-overridden")

                self.require_loopback = YLeaf(YType.boolean, "require-loopback")

                self.require_loopback_overridden = YLeaf(YType.boolean, "require-loopback-overridden")

                self.require_mib_retrieval_overridden = YLeaf(YType.boolean, "require-mib-retrieval-overridden")

                self.require_mode_overridden = YLeaf(YType.boolean, "require-mode-overridden")

                self.require_remote_mib_retrieval = YLeaf(YType.boolean, "require-remote-mib-retrieval")

                self.require_remote_mode = YLeaf(YType.enumeration, "require-remote-mode")

                self.session_down_action = YLeaf(YType.enumeration, "session-down-action")

                self.session_down_action_overridden = YLeaf(YType.boolean, "session-down-action-overridden")

                self.session_up_action = YLeaf(YType.enumeration, "session-up-action")

                self.session_up_action_overridden = YLeaf(YType.boolean, "session-up-action-overridden")

                self.symbol_period_threshold_high = YLeaf(YType.uint64, "symbol-period-threshold-high")

                self.symbol_period_threshold_high_multiplier = YLeaf(YType.uint8, "symbol-period-threshold-high-multiplier")

                self.symbol_period_threshold_high_overridden = YLeaf(YType.boolean, "symbol-period-threshold-high-overridden")

                self.symbol_period_threshold_low = YLeaf(YType.uint64, "symbol-period-threshold-low")

                self.symbol_period_threshold_low_multiplier = YLeaf(YType.uint8, "symbol-period-threshold-low-multiplier")

                self.symbol_period_threshold_low_overridden = YLeaf(YType.boolean, "symbol-period-threshold-low-overridden")

                self.symbol_period_threshold_units = YLeaf(YType.uint8, "symbol-period-threshold-units")

                self.symbol_period_window = YLeaf(YType.uint32, "symbol-period-window")

                self.symbol_period_window_multiplier = YLeaf(YType.uint8, "symbol-period-window-multiplier")

                self.symbol_period_window_overridden = YLeaf(YType.boolean, "symbol-period-window-overridden")

                self.symbol_period_window_units = YLeaf(YType.uint8, "symbol-period-window-units")

                self.udlf_enabled = YLeaf(YType.boolean, "udlf-enabled")

                self.udlf_enabled_overridden = YLeaf(YType.boolean, "udlf-enabled-overridden")

                self.wiring_conflict_action = YLeaf(YType.enumeration, "wiring-conflict-action")

                self.wiring_conflict_action_overridden = YLeaf(YType.boolean, "wiring-conflict-action-overridden")
                self._segment_path = lambda: "running-config-interface" + "[member-interface='" + self.member_interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/running-config-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface, ['member_interface', 'capabilities_conflict_action', 'capabilities_conflict_action_overridden', 'connection_timeout', 'connection_timeout_overridden', 'critical_event_action', 'critical_event_action_overridden', 'discovery_timeout_action', 'discovery_timeout_action_overridden', 'dying_gasp_action', 'dying_gasp_action_overridden', 'fast_hello_interval_enabled', 'fast_hello_interval_enabled_overridden', 'frame_period_threshold_high', 'frame_period_threshold_high_multiplier', 'frame_period_threshold_high_overridden', 'frame_period_threshold_low', 'frame_period_threshold_low_multiplier', 'frame_period_threshold_low_overridden', 'frame_period_threshold_units', 'frame_period_window', 'frame_period_window_multiplier', 'frame_period_window_overridden', 'frame_period_window_units', 'frame_seconds_threshold_high', 'frame_seconds_threshold_high_overridden', 'frame_seconds_threshold_low', 'frame_seconds_threshold_low_overridden', 'frame_seconds_window', 'frame_seconds_window_overridden', 'frame_threshold_high', 'frame_threshold_high_multiplier', 'frame_threshold_high_overridden', 'frame_threshold_low', 'frame_threshold_low_multiplier', 'frame_threshold_low_overridden', 'frame_window', 'frame_window_overridden', 'high_threshold_action', 'high_threshold_action_overridden', 'link_fault_action', 'link_fault_action_overridden', 'link_monitor_enabled', 'link_monitoring_enabled_overridden', 'mib_retrieval_enabled', 'mib_retrieval_enabled_overridden', 'mode', 'mode_overridden', 'remote_loopback_action', 'remote_loopback_action_overridden', 'remote_loopback_enabled', 'remote_loopback_enabled_overridden', 'require_link_monitoring', 'require_link_monitoring_overridden', 'require_loopback', 'require_loopback_overridden', 'require_mib_retrieval_overridden', 'require_mode_overridden', 'require_remote_mib_retrieval', 'require_remote_mode', 'session_down_action', 'session_down_action_overridden', 'session_up_action', 'session_up_action_overridden', 'symbol_period_threshold_high', 'symbol_period_threshold_high_multiplier', 'symbol_period_threshold_high_overridden', 'symbol_period_threshold_low', 'symbol_period_threshold_low_multiplier', 'symbol_period_threshold_low_overridden', 'symbol_period_threshold_units', 'symbol_period_window', 'symbol_period_window_multiplier', 'symbol_period_window_overridden', 'symbol_period_window_units', 'udlf_enabled', 'udlf_enabled_overridden', 'wiring_conflict_action', 'wiring_conflict_action_overridden'], name, value)


    class StatsInterfaces(Entity):
        """
        Table of Ethernet Link OAM enabled interfaces
        within Stats container
        
        .. attribute:: stats_interface
        
        	Ethernet Link OAM interface to get Stats for
        	**type**\: list of    :py:class:`StatsInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.StatsInterfaces.StatsInterface>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(EtherLinkOam.StatsInterfaces, self).__init__()

            self.yang_name = "stats-interfaces"
            self.yang_parent_name = "ether-link-oam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"stats-interface" : ("stats_interface", EtherLinkOam.StatsInterfaces.StatsInterface)}

            self.stats_interface = YList(self)
            self._segment_path = lambda: "stats-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EtherLinkOam.StatsInterfaces, [], name, value)


        class StatsInterface(Entity):
            """
            Ethernet Link OAM interface to get Stats for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: duplicate_event_notification_rx
            
            	Number of duplicate event notification OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: duplicate_event_notification_tx
            
            	Number of duplicate event notification OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: fixed_frames_rx
            
            	Number of RX frames 'fixed' by OAM
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: frames_lost_due_to_oam
            
            	Number of frames lost due to OAM
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: information_rx
            
            	Number of information OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: information_tx
            
            	Number of information OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_error_frame_period_records
            
            	Number of local error frame period records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_error_frame_records
            
            	Number of local error frame records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_error_frame_second_records
            
            	Number of local error frame second records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_error_symbol_period_records
            
            	Number of local error symbol period records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: loopback_control_rx
            
            	Number of loopback control OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: loopback_control_tx
            
            	Number of loopback control OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: org_specific_rx
            
            	Number of organization specific OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: org_specific_tx
            
            	Number of organization specific OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_error_frame_period_records
            
            	Number of remote error frame period records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_error_frame_records
            
            	Number of remote error frame records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_error_frame_second_records
            
            	Number of remote error frame second records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_error_symbol_period_records
            
            	Number of remote error symbol period records
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unique_event_notification_rx
            
            	Number of unique event notification OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unique_event_notification_tx
            
            	Number of unique event notification OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unsupported_codes_rx
            
            	Number of OAMPDUs with unsupported codes received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unsupported_codes_tx
            
            	Number of OAMPDUs with unsupported codes transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: variable_request_rx
            
            	Number of variable request OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: variable_request_tx
            
            	Number of variable request OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: variable_response_rx
            
            	Number of variable response OAMPDUs received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: variable_response_tx
            
            	Number of variable response OAMPDUs transmitted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(EtherLinkOam.StatsInterfaces.StatsInterface, self).__init__()

                self.yang_name = "stats-interface"
                self.yang_parent_name = "stats-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.duplicate_event_notification_rx = YLeaf(YType.uint32, "duplicate-event-notification-rx")

                self.duplicate_event_notification_tx = YLeaf(YType.uint32, "duplicate-event-notification-tx")

                self.fixed_frames_rx = YLeaf(YType.uint32, "fixed-frames-rx")

                self.frames_lost_due_to_oam = YLeaf(YType.uint32, "frames-lost-due-to-oam")

                self.information_rx = YLeaf(YType.uint32, "information-rx")

                self.information_tx = YLeaf(YType.uint32, "information-tx")

                self.local_error_frame_period_records = YLeaf(YType.uint32, "local-error-frame-period-records")

                self.local_error_frame_records = YLeaf(YType.uint32, "local-error-frame-records")

                self.local_error_frame_second_records = YLeaf(YType.uint32, "local-error-frame-second-records")

                self.local_error_symbol_period_records = YLeaf(YType.uint32, "local-error-symbol-period-records")

                self.loopback_control_rx = YLeaf(YType.uint32, "loopback-control-rx")

                self.loopback_control_tx = YLeaf(YType.uint32, "loopback-control-tx")

                self.org_specific_rx = YLeaf(YType.uint32, "org-specific-rx")

                self.org_specific_tx = YLeaf(YType.uint32, "org-specific-tx")

                self.remote_error_frame_period_records = YLeaf(YType.uint32, "remote-error-frame-period-records")

                self.remote_error_frame_records = YLeaf(YType.uint32, "remote-error-frame-records")

                self.remote_error_frame_second_records = YLeaf(YType.uint32, "remote-error-frame-second-records")

                self.remote_error_symbol_period_records = YLeaf(YType.uint32, "remote-error-symbol-period-records")

                self.unique_event_notification_rx = YLeaf(YType.uint32, "unique-event-notification-rx")

                self.unique_event_notification_tx = YLeaf(YType.uint32, "unique-event-notification-tx")

                self.unsupported_codes_rx = YLeaf(YType.uint32, "unsupported-codes-rx")

                self.unsupported_codes_tx = YLeaf(YType.uint32, "unsupported-codes-tx")

                self.variable_request_rx = YLeaf(YType.uint32, "variable-request-rx")

                self.variable_request_tx = YLeaf(YType.uint32, "variable-request-tx")

                self.variable_response_rx = YLeaf(YType.uint32, "variable-response-rx")

                self.variable_response_tx = YLeaf(YType.uint32, "variable-response-tx")
                self._segment_path = lambda: "stats-interface" + "[member-interface='" + self.member_interface.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/stats-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EtherLinkOam.StatsInterfaces.StatsInterface, ['member_interface', 'duplicate_event_notification_rx', 'duplicate_event_notification_tx', 'fixed_frames_rx', 'frames_lost_due_to_oam', 'information_rx', 'information_tx', 'local_error_frame_period_records', 'local_error_frame_records', 'local_error_frame_second_records', 'local_error_symbol_period_records', 'loopback_control_rx', 'loopback_control_tx', 'org_specific_rx', 'org_specific_tx', 'remote_error_frame_period_records', 'remote_error_frame_records', 'remote_error_frame_second_records', 'remote_error_symbol_period_records', 'unique_event_notification_rx', 'unique_event_notification_tx', 'unsupported_codes_rx', 'unsupported_codes_tx', 'variable_request_rx', 'variable_request_tx', 'variable_response_rx', 'variable_response_tx'], name, value)

    def clone_ptr(self):
        self._top_entity = EtherLinkOam()
        return self._top_entity


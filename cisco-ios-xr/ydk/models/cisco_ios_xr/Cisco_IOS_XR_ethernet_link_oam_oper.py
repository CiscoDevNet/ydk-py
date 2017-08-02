""" Cisco_IOS_XR_ethernet_link_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package operational data.

This module contains definitions
for the following management objects\:
  ether\-link\-oam\: Ethernet Link OAM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.discovery_info_interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.DiscoveryInfoInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.DiscoveryInfoInterfaces, self).__setattr__(name, value)


        class DiscoveryInfoInterface(Entity):
            """
            Ethernet Link OAM interface to get Discovery
            Info for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("member_interface",
                                "local_evaluating",
                                "local_function_event",
                                "local_function_event_valid",
                                "local_function_loopback",
                                "local_function_loopback_valid",
                                "local_function_unidirectional",
                                "local_function_unidirectional_valid",
                                "local_functionvariable",
                                "local_functionvariable_valid",
                                "local_mode",
                                "local_mode_valid",
                                "local_mtu",
                                "local_mtu_valid",
                                "local_mwd_key",
                                "local_mwd_key_valid",
                                "local_operational",
                                "local_revision",
                                "local_revisionvalid",
                                "loopback_mode",
                                "loopback_mode_valid",
                                "miswired",
                                "miswired_valid",
                                "name",
                                "operational_status",
                                "operational_status_valid",
                                "received_at_risk_notification_time_remaining",
                                "received_at_risk_notification_timestamp",
                                "remote_event",
                                "remote_event_valid",
                                "remote_loopback",
                                "remote_loopback_valid",
                                "remote_mac_address",
                                "remote_mac_address_valid",
                                "remote_mode",
                                "remote_mode_valid",
                                "remote_mtu",
                                "remote_mtu_valid",
                                "remote_mwd_key",
                                "remote_mwd_key_valid",
                                "remote_revision",
                                "remote_revisionvalid",
                                "remote_unidirectional",
                                "remote_unidirectional_valid",
                                "remote_variable",
                                "remote_variable_valid",
                                "remote_vendor_info",
                                "remote_vendor_info_valid",
                                "remote_vendor_oui",
                                "remote_vendor_oui_valid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.member_interface.is_set or
                    self.local_evaluating.is_set or
                    self.local_function_event.is_set or
                    self.local_function_event_valid.is_set or
                    self.local_function_loopback.is_set or
                    self.local_function_loopback_valid.is_set or
                    self.local_function_unidirectional.is_set or
                    self.local_function_unidirectional_valid.is_set or
                    self.local_functionvariable.is_set or
                    self.local_functionvariable_valid.is_set or
                    self.local_mode.is_set or
                    self.local_mode_valid.is_set or
                    self.local_mtu.is_set or
                    self.local_mtu_valid.is_set or
                    self.local_mwd_key.is_set or
                    self.local_mwd_key_valid.is_set or
                    self.local_operational.is_set or
                    self.local_revision.is_set or
                    self.local_revisionvalid.is_set or
                    self.loopback_mode.is_set or
                    self.loopback_mode_valid.is_set or
                    self.miswired.is_set or
                    self.miswired_valid.is_set or
                    self.name.is_set or
                    self.operational_status.is_set or
                    self.operational_status_valid.is_set or
                    self.received_at_risk_notification_time_remaining.is_set or
                    self.received_at_risk_notification_timestamp.is_set or
                    self.remote_event.is_set or
                    self.remote_event_valid.is_set or
                    self.remote_loopback.is_set or
                    self.remote_loopback_valid.is_set or
                    self.remote_mac_address.is_set or
                    self.remote_mac_address_valid.is_set or
                    self.remote_mode.is_set or
                    self.remote_mode_valid.is_set or
                    self.remote_mtu.is_set or
                    self.remote_mtu_valid.is_set or
                    self.remote_mwd_key.is_set or
                    self.remote_mwd_key_valid.is_set or
                    self.remote_revision.is_set or
                    self.remote_revisionvalid.is_set or
                    self.remote_unidirectional.is_set or
                    self.remote_unidirectional_valid.is_set or
                    self.remote_variable.is_set or
                    self.remote_variable_valid.is_set or
                    self.remote_vendor_info.is_set or
                    self.remote_vendor_info_valid.is_set or
                    self.remote_vendor_oui.is_set or
                    self.remote_vendor_oui_valid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.member_interface.yfilter != YFilter.not_set or
                    self.local_evaluating.yfilter != YFilter.not_set or
                    self.local_function_event.yfilter != YFilter.not_set or
                    self.local_function_event_valid.yfilter != YFilter.not_set or
                    self.local_function_loopback.yfilter != YFilter.not_set or
                    self.local_function_loopback_valid.yfilter != YFilter.not_set or
                    self.local_function_unidirectional.yfilter != YFilter.not_set or
                    self.local_function_unidirectional_valid.yfilter != YFilter.not_set or
                    self.local_functionvariable.yfilter != YFilter.not_set or
                    self.local_functionvariable_valid.yfilter != YFilter.not_set or
                    self.local_mode.yfilter != YFilter.not_set or
                    self.local_mode_valid.yfilter != YFilter.not_set or
                    self.local_mtu.yfilter != YFilter.not_set or
                    self.local_mtu_valid.yfilter != YFilter.not_set or
                    self.local_mwd_key.yfilter != YFilter.not_set or
                    self.local_mwd_key_valid.yfilter != YFilter.not_set or
                    self.local_operational.yfilter != YFilter.not_set or
                    self.local_revision.yfilter != YFilter.not_set or
                    self.local_revisionvalid.yfilter != YFilter.not_set or
                    self.loopback_mode.yfilter != YFilter.not_set or
                    self.loopback_mode_valid.yfilter != YFilter.not_set or
                    self.miswired.yfilter != YFilter.not_set or
                    self.miswired_valid.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.operational_status.yfilter != YFilter.not_set or
                    self.operational_status_valid.yfilter != YFilter.not_set or
                    self.received_at_risk_notification_time_remaining.yfilter != YFilter.not_set or
                    self.received_at_risk_notification_timestamp.yfilter != YFilter.not_set or
                    self.remote_event.yfilter != YFilter.not_set or
                    self.remote_event_valid.yfilter != YFilter.not_set or
                    self.remote_loopback.yfilter != YFilter.not_set or
                    self.remote_loopback_valid.yfilter != YFilter.not_set or
                    self.remote_mac_address.yfilter != YFilter.not_set or
                    self.remote_mac_address_valid.yfilter != YFilter.not_set or
                    self.remote_mode.yfilter != YFilter.not_set or
                    self.remote_mode_valid.yfilter != YFilter.not_set or
                    self.remote_mtu.yfilter != YFilter.not_set or
                    self.remote_mtu_valid.yfilter != YFilter.not_set or
                    self.remote_mwd_key.yfilter != YFilter.not_set or
                    self.remote_mwd_key_valid.yfilter != YFilter.not_set or
                    self.remote_revision.yfilter != YFilter.not_set or
                    self.remote_revisionvalid.yfilter != YFilter.not_set or
                    self.remote_unidirectional.yfilter != YFilter.not_set or
                    self.remote_unidirectional_valid.yfilter != YFilter.not_set or
                    self.remote_variable.yfilter != YFilter.not_set or
                    self.remote_variable_valid.yfilter != YFilter.not_set or
                    self.remote_vendor_info.yfilter != YFilter.not_set or
                    self.remote_vendor_info_valid.yfilter != YFilter.not_set or
                    self.remote_vendor_oui.yfilter != YFilter.not_set or
                    self.remote_vendor_oui_valid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "discovery-info-interface" + "[member-interface='" + self.member_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/discovery-info-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.member_interface.is_set or self.member_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.member_interface.get_name_leafdata())
                if (self.local_evaluating.is_set or self.local_evaluating.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_evaluating.get_name_leafdata())
                if (self.local_function_event.is_set or self.local_function_event.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_event.get_name_leafdata())
                if (self.local_function_event_valid.is_set or self.local_function_event_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_event_valid.get_name_leafdata())
                if (self.local_function_loopback.is_set or self.local_function_loopback.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_loopback.get_name_leafdata())
                if (self.local_function_loopback_valid.is_set or self.local_function_loopback_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_loopback_valid.get_name_leafdata())
                if (self.local_function_unidirectional.is_set or self.local_function_unidirectional.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_unidirectional.get_name_leafdata())
                if (self.local_function_unidirectional_valid.is_set or self.local_function_unidirectional_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_function_unidirectional_valid.get_name_leafdata())
                if (self.local_functionvariable.is_set or self.local_functionvariable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_functionvariable.get_name_leafdata())
                if (self.local_functionvariable_valid.is_set or self.local_functionvariable_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_functionvariable_valid.get_name_leafdata())
                if (self.local_mode.is_set or self.local_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mode.get_name_leafdata())
                if (self.local_mode_valid.is_set or self.local_mode_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mode_valid.get_name_leafdata())
                if (self.local_mtu.is_set or self.local_mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mtu.get_name_leafdata())
                if (self.local_mtu_valid.is_set or self.local_mtu_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mtu_valid.get_name_leafdata())
                if (self.local_mwd_key.is_set or self.local_mwd_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mwd_key.get_name_leafdata())
                if (self.local_mwd_key_valid.is_set or self.local_mwd_key_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mwd_key_valid.get_name_leafdata())
                if (self.local_operational.is_set or self.local_operational.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_operational.get_name_leafdata())
                if (self.local_revision.is_set or self.local_revision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_revision.get_name_leafdata())
                if (self.local_revisionvalid.is_set or self.local_revisionvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_revisionvalid.get_name_leafdata())
                if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                if (self.loopback_mode_valid.is_set or self.loopback_mode_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.loopback_mode_valid.get_name_leafdata())
                if (self.miswired.is_set or self.miswired.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.miswired.get_name_leafdata())
                if (self.miswired_valid.is_set or self.miswired_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.miswired_valid.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.operational_status.is_set or self.operational_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operational_status.get_name_leafdata())
                if (self.operational_status_valid.is_set or self.operational_status_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.operational_status_valid.get_name_leafdata())
                if (self.received_at_risk_notification_time_remaining.is_set or self.received_at_risk_notification_time_remaining.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_at_risk_notification_time_remaining.get_name_leafdata())
                if (self.received_at_risk_notification_timestamp.is_set or self.received_at_risk_notification_timestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.received_at_risk_notification_timestamp.get_name_leafdata())
                if (self.remote_event.is_set or self.remote_event.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_event.get_name_leafdata())
                if (self.remote_event_valid.is_set or self.remote_event_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_event_valid.get_name_leafdata())
                if (self.remote_loopback.is_set or self.remote_loopback.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback.get_name_leafdata())
                if (self.remote_loopback_valid.is_set or self.remote_loopback_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback_valid.get_name_leafdata())
                if (self.remote_mac_address.is_set or self.remote_mac_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mac_address.get_name_leafdata())
                if (self.remote_mac_address_valid.is_set or self.remote_mac_address_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mac_address_valid.get_name_leafdata())
                if (self.remote_mode.is_set or self.remote_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mode.get_name_leafdata())
                if (self.remote_mode_valid.is_set or self.remote_mode_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mode_valid.get_name_leafdata())
                if (self.remote_mtu.is_set or self.remote_mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mtu.get_name_leafdata())
                if (self.remote_mtu_valid.is_set or self.remote_mtu_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mtu_valid.get_name_leafdata())
                if (self.remote_mwd_key.is_set or self.remote_mwd_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mwd_key.get_name_leafdata())
                if (self.remote_mwd_key_valid.is_set or self.remote_mwd_key_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mwd_key_valid.get_name_leafdata())
                if (self.remote_revision.is_set or self.remote_revision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_revision.get_name_leafdata())
                if (self.remote_revisionvalid.is_set or self.remote_revisionvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_revisionvalid.get_name_leafdata())
                if (self.remote_unidirectional.is_set or self.remote_unidirectional.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_unidirectional.get_name_leafdata())
                if (self.remote_unidirectional_valid.is_set or self.remote_unidirectional_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_unidirectional_valid.get_name_leafdata())
                if (self.remote_variable.is_set or self.remote_variable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_variable.get_name_leafdata())
                if (self.remote_variable_valid.is_set or self.remote_variable_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_variable_valid.get_name_leafdata())
                if (self.remote_vendor_info.is_set or self.remote_vendor_info.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_vendor_info.get_name_leafdata())
                if (self.remote_vendor_info_valid.is_set or self.remote_vendor_info_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_vendor_info_valid.get_name_leafdata())
                if (self.remote_vendor_oui.is_set or self.remote_vendor_oui.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_vendor_oui.get_name_leafdata())
                if (self.remote_vendor_oui_valid.is_set or self.remote_vendor_oui_valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_vendor_oui_valid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "member-interface" or name == "local-evaluating" or name == "local-function-event" or name == "local-function-event-valid" or name == "local-function-loopback" or name == "local-function-loopback-valid" or name == "local-function-unidirectional" or name == "local-function-unidirectional-valid" or name == "local-functionvariable" or name == "local-functionvariable-valid" or name == "local-mode" or name == "local-mode-valid" or name == "local-mtu" or name == "local-mtu-valid" or name == "local-mwd-key" or name == "local-mwd-key-valid" or name == "local-operational" or name == "local-revision" or name == "local-revisionvalid" or name == "loopback-mode" or name == "loopback-mode-valid" or name == "miswired" or name == "miswired-valid" or name == "name" or name == "operational-status" or name == "operational-status-valid" or name == "received-at-risk-notification-time-remaining" or name == "received-at-risk-notification-timestamp" or name == "remote-event" or name == "remote-event-valid" or name == "remote-loopback" or name == "remote-loopback-valid" or name == "remote-mac-address" or name == "remote-mac-address-valid" or name == "remote-mode" or name == "remote-mode-valid" or name == "remote-mtu" or name == "remote-mtu-valid" or name == "remote-mwd-key" or name == "remote-mwd-key-valid" or name == "remote-revision" or name == "remote-revisionvalid" or name == "remote-unidirectional" or name == "remote-unidirectional-valid" or name == "remote-variable" or name == "remote-variable-valid" or name == "remote-vendor-info" or name == "remote-vendor-info-valid" or name == "remote-vendor-oui" or name == "remote-vendor-oui-valid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "member-interface"):
                    self.member_interface = value
                    self.member_interface.value_namespace = name_space
                    self.member_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "local-evaluating"):
                    self.local_evaluating = value
                    self.local_evaluating.value_namespace = name_space
                    self.local_evaluating.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-event"):
                    self.local_function_event = value
                    self.local_function_event.value_namespace = name_space
                    self.local_function_event.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-event-valid"):
                    self.local_function_event_valid = value
                    self.local_function_event_valid.value_namespace = name_space
                    self.local_function_event_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-loopback"):
                    self.local_function_loopback = value
                    self.local_function_loopback.value_namespace = name_space
                    self.local_function_loopback.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-loopback-valid"):
                    self.local_function_loopback_valid = value
                    self.local_function_loopback_valid.value_namespace = name_space
                    self.local_function_loopback_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-unidirectional"):
                    self.local_function_unidirectional = value
                    self.local_function_unidirectional.value_namespace = name_space
                    self.local_function_unidirectional.value_namespace_prefix = name_space_prefix
                if(value_path == "local-function-unidirectional-valid"):
                    self.local_function_unidirectional_valid = value
                    self.local_function_unidirectional_valid.value_namespace = name_space
                    self.local_function_unidirectional_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-functionvariable"):
                    self.local_functionvariable = value
                    self.local_functionvariable.value_namespace = name_space
                    self.local_functionvariable.value_namespace_prefix = name_space_prefix
                if(value_path == "local-functionvariable-valid"):
                    self.local_functionvariable_valid = value
                    self.local_functionvariable_valid.value_namespace = name_space
                    self.local_functionvariable_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mode"):
                    self.local_mode = value
                    self.local_mode.value_namespace = name_space
                    self.local_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mode-valid"):
                    self.local_mode_valid = value
                    self.local_mode_valid.value_namespace = name_space
                    self.local_mode_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mtu"):
                    self.local_mtu = value
                    self.local_mtu.value_namespace = name_space
                    self.local_mtu.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mtu-valid"):
                    self.local_mtu_valid = value
                    self.local_mtu_valid.value_namespace = name_space
                    self.local_mtu_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mwd-key"):
                    self.local_mwd_key = value
                    self.local_mwd_key.value_namespace = name_space
                    self.local_mwd_key.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mwd-key-valid"):
                    self.local_mwd_key_valid = value
                    self.local_mwd_key_valid.value_namespace = name_space
                    self.local_mwd_key_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "local-operational"):
                    self.local_operational = value
                    self.local_operational.value_namespace = name_space
                    self.local_operational.value_namespace_prefix = name_space_prefix
                if(value_path == "local-revision"):
                    self.local_revision = value
                    self.local_revision.value_namespace = name_space
                    self.local_revision.value_namespace_prefix = name_space_prefix
                if(value_path == "local-revisionvalid"):
                    self.local_revisionvalid = value
                    self.local_revisionvalid.value_namespace = name_space
                    self.local_revisionvalid.value_namespace_prefix = name_space_prefix
                if(value_path == "loopback-mode"):
                    self.loopback_mode = value
                    self.loopback_mode.value_namespace = name_space
                    self.loopback_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "loopback-mode-valid"):
                    self.loopback_mode_valid = value
                    self.loopback_mode_valid.value_namespace = name_space
                    self.loopback_mode_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "miswired"):
                    self.miswired = value
                    self.miswired.value_namespace = name_space
                    self.miswired.value_namespace_prefix = name_space_prefix
                if(value_path == "miswired-valid"):
                    self.miswired_valid = value
                    self.miswired_valid.value_namespace = name_space
                    self.miswired_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "operational-status"):
                    self.operational_status = value
                    self.operational_status.value_namespace = name_space
                    self.operational_status.value_namespace_prefix = name_space_prefix
                if(value_path == "operational-status-valid"):
                    self.operational_status_valid = value
                    self.operational_status_valid.value_namespace = name_space
                    self.operational_status_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "received-at-risk-notification-time-remaining"):
                    self.received_at_risk_notification_time_remaining = value
                    self.received_at_risk_notification_time_remaining.value_namespace = name_space
                    self.received_at_risk_notification_time_remaining.value_namespace_prefix = name_space_prefix
                if(value_path == "received-at-risk-notification-timestamp"):
                    self.received_at_risk_notification_timestamp = value
                    self.received_at_risk_notification_timestamp.value_namespace = name_space
                    self.received_at_risk_notification_timestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-event"):
                    self.remote_event = value
                    self.remote_event.value_namespace = name_space
                    self.remote_event.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-event-valid"):
                    self.remote_event_valid = value
                    self.remote_event_valid.value_namespace = name_space
                    self.remote_event_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback"):
                    self.remote_loopback = value
                    self.remote_loopback.value_namespace = name_space
                    self.remote_loopback.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback-valid"):
                    self.remote_loopback_valid = value
                    self.remote_loopback_valid.value_namespace = name_space
                    self.remote_loopback_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mac-address"):
                    self.remote_mac_address = value
                    self.remote_mac_address.value_namespace = name_space
                    self.remote_mac_address.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mac-address-valid"):
                    self.remote_mac_address_valid = value
                    self.remote_mac_address_valid.value_namespace = name_space
                    self.remote_mac_address_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mode"):
                    self.remote_mode = value
                    self.remote_mode.value_namespace = name_space
                    self.remote_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mode-valid"):
                    self.remote_mode_valid = value
                    self.remote_mode_valid.value_namespace = name_space
                    self.remote_mode_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mtu"):
                    self.remote_mtu = value
                    self.remote_mtu.value_namespace = name_space
                    self.remote_mtu.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mtu-valid"):
                    self.remote_mtu_valid = value
                    self.remote_mtu_valid.value_namespace = name_space
                    self.remote_mtu_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mwd-key"):
                    self.remote_mwd_key = value
                    self.remote_mwd_key.value_namespace = name_space
                    self.remote_mwd_key.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mwd-key-valid"):
                    self.remote_mwd_key_valid = value
                    self.remote_mwd_key_valid.value_namespace = name_space
                    self.remote_mwd_key_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-revision"):
                    self.remote_revision = value
                    self.remote_revision.value_namespace = name_space
                    self.remote_revision.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-revisionvalid"):
                    self.remote_revisionvalid = value
                    self.remote_revisionvalid.value_namespace = name_space
                    self.remote_revisionvalid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-unidirectional"):
                    self.remote_unidirectional = value
                    self.remote_unidirectional.value_namespace = name_space
                    self.remote_unidirectional.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-unidirectional-valid"):
                    self.remote_unidirectional_valid = value
                    self.remote_unidirectional_valid.value_namespace = name_space
                    self.remote_unidirectional_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-variable"):
                    self.remote_variable = value
                    self.remote_variable.value_namespace = name_space
                    self.remote_variable.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-variable-valid"):
                    self.remote_variable_valid = value
                    self.remote_variable_valid.value_namespace = name_space
                    self.remote_variable_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-vendor-info"):
                    self.remote_vendor_info = value
                    self.remote_vendor_info.value_namespace = name_space
                    self.remote_vendor_info.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-vendor-info-valid"):
                    self.remote_vendor_info_valid = value
                    self.remote_vendor_info_valid.value_namespace = name_space
                    self.remote_vendor_info_valid.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-vendor-oui"):
                    self.remote_vendor_oui = value
                    self.remote_vendor_oui.value_namespace = name_space
                    self.remote_vendor_oui.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-vendor-oui-valid"):
                    self.remote_vendor_oui_valid = value
                    self.remote_vendor_oui_valid.value_namespace = name_space
                    self.remote_vendor_oui_valid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.discovery_info_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.discovery_info_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "discovery-info-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "discovery-info-interface"):
                for c in self.discovery_info_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.discovery_info_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "discovery-info-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.interface_state_interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.InterfaceStateInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.InterfaceStateInterfaces, self).__setattr__(name, value)


        class InterfaceStateInterface(Entity):
            """
            Ethernet Link OAM interface to get Interface
            State for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("member_interface",
                                "local_mwd_key",
                                "protocol_code",
                                "remote_mwd_key",
                                "remote_mwd_key_present",
                                "rx_fault") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("caps_add_error_code",
                                    "caps_add_reason",
                                    "epi_error_code",
                                    "epi_reason",
                                    "pfi_error_code",
                                    "pfi_reason",
                                    "platform_error_code",
                                    "platform_reason",
                                    "spio_error_code",
                                    "spio_reason") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.caps_add_error_code.is_set or
                        self.caps_add_reason.is_set or
                        self.epi_error_code.is_set or
                        self.epi_reason.is_set or
                        self.pfi_error_code.is_set or
                        self.pfi_reason.is_set or
                        self.platform_error_code.is_set or
                        self.platform_reason.is_set or
                        self.spio_error_code.is_set or
                        self.spio_reason.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.caps_add_error_code.yfilter != YFilter.not_set or
                        self.caps_add_reason.yfilter != YFilter.not_set or
                        self.epi_error_code.yfilter != YFilter.not_set or
                        self.epi_reason.yfilter != YFilter.not_set or
                        self.pfi_error_code.yfilter != YFilter.not_set or
                        self.pfi_reason.yfilter != YFilter.not_set or
                        self.platform_error_code.yfilter != YFilter.not_set or
                        self.platform_reason.yfilter != YFilter.not_set or
                        self.spio_error_code.yfilter != YFilter.not_set or
                        self.spio_reason.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "errors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.caps_add_error_code.is_set or self.caps_add_error_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.caps_add_error_code.get_name_leafdata())
                    if (self.caps_add_reason.is_set or self.caps_add_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.caps_add_reason.get_name_leafdata())
                    if (self.epi_error_code.is_set or self.epi_error_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.epi_error_code.get_name_leafdata())
                    if (self.epi_reason.is_set or self.epi_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.epi_reason.get_name_leafdata())
                    if (self.pfi_error_code.is_set or self.pfi_error_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pfi_error_code.get_name_leafdata())
                    if (self.pfi_reason.is_set or self.pfi_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pfi_reason.get_name_leafdata())
                    if (self.platform_error_code.is_set or self.platform_error_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.platform_error_code.get_name_leafdata())
                    if (self.platform_reason.is_set or self.platform_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.platform_reason.get_name_leafdata())
                    if (self.spio_error_code.is_set or self.spio_error_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.spio_error_code.get_name_leafdata())
                    if (self.spio_reason.is_set or self.spio_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.spio_reason.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "caps-add-error-code" or name == "caps-add-reason" or name == "epi-error-code" or name == "epi-reason" or name == "pfi-error-code" or name == "pfi-reason" or name == "platform-error-code" or name == "platform-reason" or name == "spio-error-code" or name == "spio-reason"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "caps-add-error-code"):
                        self.caps_add_error_code = value
                        self.caps_add_error_code.value_namespace = name_space
                        self.caps_add_error_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "caps-add-reason"):
                        self.caps_add_reason = value
                        self.caps_add_reason.value_namespace = name_space
                        self.caps_add_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "epi-error-code"):
                        self.epi_error_code = value
                        self.epi_error_code.value_namespace = name_space
                        self.epi_error_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "epi-reason"):
                        self.epi_reason = value
                        self.epi_reason.value_namespace = name_space
                        self.epi_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "pfi-error-code"):
                        self.pfi_error_code = value
                        self.pfi_error_code.value_namespace = name_space
                        self.pfi_error_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "pfi-reason"):
                        self.pfi_reason = value
                        self.pfi_reason.value_namespace = name_space
                        self.pfi_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "platform-error-code"):
                        self.platform_error_code = value
                        self.platform_error_code.value_namespace = name_space
                        self.platform_error_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "platform-reason"):
                        self.platform_reason = value
                        self.platform_reason.value_namespace = name_space
                        self.platform_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "spio-error-code"):
                        self.spio_error_code = value
                        self.spio_error_code.value_namespace = name_space
                        self.spio_error_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "spio-reason"):
                        self.spio_reason = value
                        self.spio_reason.value_namespace = name_space
                        self.spio_reason.value_namespace_prefix = name_space_prefix


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

                    self.capabilities_conflict = YLeaf(YType.boolean, "capabilities-conflict")

                    self.discovery_timed_out = YLeaf(YType.boolean, "discovery-timed-out")

                    self.link_fault_received = YLeaf(YType.boolean, "link-fault-received")

                    self.session_down = YLeaf(YType.boolean, "session-down")

                    self.wiring_conflict = YLeaf(YType.boolean, "wiring-conflict")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("capabilities_conflict",
                                    "discovery_timed_out",
                                    "link_fault_received",
                                    "session_down",
                                    "wiring_conflict") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.capabilities_conflict.is_set or
                        self.discovery_timed_out.is_set or
                        self.link_fault_received.is_set or
                        self.session_down.is_set or
                        self.wiring_conflict.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.capabilities_conflict.yfilter != YFilter.not_set or
                        self.discovery_timed_out.yfilter != YFilter.not_set or
                        self.link_fault_received.yfilter != YFilter.not_set or
                        self.session_down.yfilter != YFilter.not_set or
                        self.wiring_conflict.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "efd-triggers" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.capabilities_conflict.is_set or self.capabilities_conflict.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.capabilities_conflict.get_name_leafdata())
                    if (self.discovery_timed_out.is_set or self.discovery_timed_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discovery_timed_out.get_name_leafdata())
                    if (self.link_fault_received.is_set or self.link_fault_received.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_fault_received.get_name_leafdata())
                    if (self.session_down.is_set or self.session_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_down.get_name_leafdata())
                    if (self.wiring_conflict.is_set or self.wiring_conflict.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wiring_conflict.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "capabilities-conflict" or name == "discovery-timed-out" or name == "link-fault-received" or name == "session-down" or name == "wiring-conflict"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "capabilities-conflict"):
                        self.capabilities_conflict = value
                        self.capabilities_conflict.value_namespace = name_space
                        self.capabilities_conflict.value_namespace_prefix = name_space_prefix
                    if(value_path == "discovery-timed-out"):
                        self.discovery_timed_out = value
                        self.discovery_timed_out.value_namespace = name_space
                        self.discovery_timed_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-fault-received"):
                        self.link_fault_received = value
                        self.link_fault_received.value_namespace = name_space
                        self.link_fault_received.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-down"):
                        self.session_down = value
                        self.session_down.value_namespace = name_space
                        self.session_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "wiring-conflict"):
                        self.wiring_conflict = value
                        self.wiring_conflict.value_namespace = name_space
                        self.wiring_conflict.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.member_interface.is_set or
                    self.local_mwd_key.is_set or
                    self.protocol_code.is_set or
                    self.remote_mwd_key.is_set or
                    self.remote_mwd_key_present.is_set or
                    self.rx_fault.is_set or
                    (self.efd_triggers is not None and self.efd_triggers.has_data()) or
                    (self.errors is not None and self.errors.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.member_interface.yfilter != YFilter.not_set or
                    self.local_mwd_key.yfilter != YFilter.not_set or
                    self.protocol_code.yfilter != YFilter.not_set or
                    self.remote_mwd_key.yfilter != YFilter.not_set or
                    self.remote_mwd_key_present.yfilter != YFilter.not_set or
                    self.rx_fault.yfilter != YFilter.not_set or
                    (self.efd_triggers is not None and self.efd_triggers.has_operation()) or
                    (self.errors is not None and self.errors.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface-state-interface" + "[member-interface='" + self.member_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/interface-state-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.member_interface.is_set or self.member_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.member_interface.get_name_leafdata())
                if (self.local_mwd_key.is_set or self.local_mwd_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_mwd_key.get_name_leafdata())
                if (self.protocol_code.is_set or self.protocol_code.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol_code.get_name_leafdata())
                if (self.remote_mwd_key.is_set or self.remote_mwd_key.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mwd_key.get_name_leafdata())
                if (self.remote_mwd_key_present.is_set or self.remote_mwd_key_present.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_mwd_key_present.get_name_leafdata())
                if (self.rx_fault.is_set or self.rx_fault.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rx_fault.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "efd-triggers"):
                    if (self.efd_triggers is None):
                        self.efd_triggers = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers()
                        self.efd_triggers.parent = self
                        self._children_name_map["efd_triggers"] = "efd-triggers"
                    return self.efd_triggers

                if (child_yang_name == "errors"):
                    if (self.errors is None):
                        self.errors = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors()
                        self.errors.parent = self
                        self._children_name_map["errors"] = "errors"
                    return self.errors

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "efd-triggers" or name == "errors" or name == "member-interface" or name == "local-mwd-key" or name == "protocol-code" or name == "remote-mwd-key" or name == "remote-mwd-key-present" or name == "rx-fault"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "member-interface"):
                    self.member_interface = value
                    self.member_interface.value_namespace = name_space
                    self.member_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "local-mwd-key"):
                    self.local_mwd_key = value
                    self.local_mwd_key.value_namespace = name_space
                    self.local_mwd_key.value_namespace_prefix = name_space_prefix
                if(value_path == "protocol-code"):
                    self.protocol_code = value
                    self.protocol_code.value_namespace = name_space
                    self.protocol_code.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mwd-key"):
                    self.remote_mwd_key = value
                    self.remote_mwd_key.value_namespace = name_space
                    self.remote_mwd_key.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-mwd-key-present"):
                    self.remote_mwd_key_present = value
                    self.remote_mwd_key_present.value_namespace = name_space
                    self.remote_mwd_key_present.value_namespace_prefix = name_space_prefix
                if(value_path == "rx-fault"):
                    self.rx_fault = value
                    self.rx_fault.value_namespace = name_space
                    self.rx_fault.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface_state_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface_state_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface-state-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface-state-interface"):
                for c in self.interface_state_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface_state_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface-state-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.running_config_interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.RunningConfigInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.RunningConfigInterfaces, self).__setattr__(name, value)


        class RunningConfigInterface(Entity):
            """
            Ethernet Link OAM interface to get Running
            Config for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("member_interface",
                                "capabilities_conflict_action",
                                "capabilities_conflict_action_overridden",
                                "connection_timeout",
                                "connection_timeout_overridden",
                                "critical_event_action",
                                "critical_event_action_overridden",
                                "discovery_timeout_action",
                                "discovery_timeout_action_overridden",
                                "dying_gasp_action",
                                "dying_gasp_action_overridden",
                                "fast_hello_interval_enabled",
                                "fast_hello_interval_enabled_overridden",
                                "frame_period_threshold_high",
                                "frame_period_threshold_high_multiplier",
                                "frame_period_threshold_high_overridden",
                                "frame_period_threshold_low",
                                "frame_period_threshold_low_multiplier",
                                "frame_period_threshold_low_overridden",
                                "frame_period_threshold_units",
                                "frame_period_window",
                                "frame_period_window_multiplier",
                                "frame_period_window_overridden",
                                "frame_period_window_units",
                                "frame_seconds_threshold_high",
                                "frame_seconds_threshold_high_overridden",
                                "frame_seconds_threshold_low",
                                "frame_seconds_threshold_low_overridden",
                                "frame_seconds_window",
                                "frame_seconds_window_overridden",
                                "frame_threshold_high",
                                "frame_threshold_high_multiplier",
                                "frame_threshold_high_overridden",
                                "frame_threshold_low",
                                "frame_threshold_low_multiplier",
                                "frame_threshold_low_overridden",
                                "frame_window",
                                "frame_window_overridden",
                                "high_threshold_action",
                                "high_threshold_action_overridden",
                                "link_fault_action",
                                "link_fault_action_overridden",
                                "link_monitor_enabled",
                                "link_monitoring_enabled_overridden",
                                "mib_retrieval_enabled",
                                "mib_retrieval_enabled_overridden",
                                "mode",
                                "mode_overridden",
                                "remote_loopback_action",
                                "remote_loopback_action_overridden",
                                "remote_loopback_enabled",
                                "remote_loopback_enabled_overridden",
                                "require_link_monitoring",
                                "require_link_monitoring_overridden",
                                "require_loopback",
                                "require_loopback_overridden",
                                "require_mib_retrieval_overridden",
                                "require_mode_overridden",
                                "require_remote_mib_retrieval",
                                "require_remote_mode",
                                "session_down_action",
                                "session_down_action_overridden",
                                "session_up_action",
                                "session_up_action_overridden",
                                "symbol_period_threshold_high",
                                "symbol_period_threshold_high_multiplier",
                                "symbol_period_threshold_high_overridden",
                                "symbol_period_threshold_low",
                                "symbol_period_threshold_low_multiplier",
                                "symbol_period_threshold_low_overridden",
                                "symbol_period_threshold_units",
                                "symbol_period_window",
                                "symbol_period_window_multiplier",
                                "symbol_period_window_overridden",
                                "symbol_period_window_units",
                                "udlf_enabled",
                                "udlf_enabled_overridden",
                                "wiring_conflict_action",
                                "wiring_conflict_action_overridden") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.member_interface.is_set or
                    self.capabilities_conflict_action.is_set or
                    self.capabilities_conflict_action_overridden.is_set or
                    self.connection_timeout.is_set or
                    self.connection_timeout_overridden.is_set or
                    self.critical_event_action.is_set or
                    self.critical_event_action_overridden.is_set or
                    self.discovery_timeout_action.is_set or
                    self.discovery_timeout_action_overridden.is_set or
                    self.dying_gasp_action.is_set or
                    self.dying_gasp_action_overridden.is_set or
                    self.fast_hello_interval_enabled.is_set or
                    self.fast_hello_interval_enabled_overridden.is_set or
                    self.frame_period_threshold_high.is_set or
                    self.frame_period_threshold_high_multiplier.is_set or
                    self.frame_period_threshold_high_overridden.is_set or
                    self.frame_period_threshold_low.is_set or
                    self.frame_period_threshold_low_multiplier.is_set or
                    self.frame_period_threshold_low_overridden.is_set or
                    self.frame_period_threshold_units.is_set or
                    self.frame_period_window.is_set or
                    self.frame_period_window_multiplier.is_set or
                    self.frame_period_window_overridden.is_set or
                    self.frame_period_window_units.is_set or
                    self.frame_seconds_threshold_high.is_set or
                    self.frame_seconds_threshold_high_overridden.is_set or
                    self.frame_seconds_threshold_low.is_set or
                    self.frame_seconds_threshold_low_overridden.is_set or
                    self.frame_seconds_window.is_set or
                    self.frame_seconds_window_overridden.is_set or
                    self.frame_threshold_high.is_set or
                    self.frame_threshold_high_multiplier.is_set or
                    self.frame_threshold_high_overridden.is_set or
                    self.frame_threshold_low.is_set or
                    self.frame_threshold_low_multiplier.is_set or
                    self.frame_threshold_low_overridden.is_set or
                    self.frame_window.is_set or
                    self.frame_window_overridden.is_set or
                    self.high_threshold_action.is_set or
                    self.high_threshold_action_overridden.is_set or
                    self.link_fault_action.is_set or
                    self.link_fault_action_overridden.is_set or
                    self.link_monitor_enabled.is_set or
                    self.link_monitoring_enabled_overridden.is_set or
                    self.mib_retrieval_enabled.is_set or
                    self.mib_retrieval_enabled_overridden.is_set or
                    self.mode.is_set or
                    self.mode_overridden.is_set or
                    self.remote_loopback_action.is_set or
                    self.remote_loopback_action_overridden.is_set or
                    self.remote_loopback_enabled.is_set or
                    self.remote_loopback_enabled_overridden.is_set or
                    self.require_link_monitoring.is_set or
                    self.require_link_monitoring_overridden.is_set or
                    self.require_loopback.is_set or
                    self.require_loopback_overridden.is_set or
                    self.require_mib_retrieval_overridden.is_set or
                    self.require_mode_overridden.is_set or
                    self.require_remote_mib_retrieval.is_set or
                    self.require_remote_mode.is_set or
                    self.session_down_action.is_set or
                    self.session_down_action_overridden.is_set or
                    self.session_up_action.is_set or
                    self.session_up_action_overridden.is_set or
                    self.symbol_period_threshold_high.is_set or
                    self.symbol_period_threshold_high_multiplier.is_set or
                    self.symbol_period_threshold_high_overridden.is_set or
                    self.symbol_period_threshold_low.is_set or
                    self.symbol_period_threshold_low_multiplier.is_set or
                    self.symbol_period_threshold_low_overridden.is_set or
                    self.symbol_period_threshold_units.is_set or
                    self.symbol_period_window.is_set or
                    self.symbol_period_window_multiplier.is_set or
                    self.symbol_period_window_overridden.is_set or
                    self.symbol_period_window_units.is_set or
                    self.udlf_enabled.is_set or
                    self.udlf_enabled_overridden.is_set or
                    self.wiring_conflict_action.is_set or
                    self.wiring_conflict_action_overridden.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.member_interface.yfilter != YFilter.not_set or
                    self.capabilities_conflict_action.yfilter != YFilter.not_set or
                    self.capabilities_conflict_action_overridden.yfilter != YFilter.not_set or
                    self.connection_timeout.yfilter != YFilter.not_set or
                    self.connection_timeout_overridden.yfilter != YFilter.not_set or
                    self.critical_event_action.yfilter != YFilter.not_set or
                    self.critical_event_action_overridden.yfilter != YFilter.not_set or
                    self.discovery_timeout_action.yfilter != YFilter.not_set or
                    self.discovery_timeout_action_overridden.yfilter != YFilter.not_set or
                    self.dying_gasp_action.yfilter != YFilter.not_set or
                    self.dying_gasp_action_overridden.yfilter != YFilter.not_set or
                    self.fast_hello_interval_enabled.yfilter != YFilter.not_set or
                    self.fast_hello_interval_enabled_overridden.yfilter != YFilter.not_set or
                    self.frame_period_threshold_high.yfilter != YFilter.not_set or
                    self.frame_period_threshold_high_multiplier.yfilter != YFilter.not_set or
                    self.frame_period_threshold_high_overridden.yfilter != YFilter.not_set or
                    self.frame_period_threshold_low.yfilter != YFilter.not_set or
                    self.frame_period_threshold_low_multiplier.yfilter != YFilter.not_set or
                    self.frame_period_threshold_low_overridden.yfilter != YFilter.not_set or
                    self.frame_period_threshold_units.yfilter != YFilter.not_set or
                    self.frame_period_window.yfilter != YFilter.not_set or
                    self.frame_period_window_multiplier.yfilter != YFilter.not_set or
                    self.frame_period_window_overridden.yfilter != YFilter.not_set or
                    self.frame_period_window_units.yfilter != YFilter.not_set or
                    self.frame_seconds_threshold_high.yfilter != YFilter.not_set or
                    self.frame_seconds_threshold_high_overridden.yfilter != YFilter.not_set or
                    self.frame_seconds_threshold_low.yfilter != YFilter.not_set or
                    self.frame_seconds_threshold_low_overridden.yfilter != YFilter.not_set or
                    self.frame_seconds_window.yfilter != YFilter.not_set or
                    self.frame_seconds_window_overridden.yfilter != YFilter.not_set or
                    self.frame_threshold_high.yfilter != YFilter.not_set or
                    self.frame_threshold_high_multiplier.yfilter != YFilter.not_set or
                    self.frame_threshold_high_overridden.yfilter != YFilter.not_set or
                    self.frame_threshold_low.yfilter != YFilter.not_set or
                    self.frame_threshold_low_multiplier.yfilter != YFilter.not_set or
                    self.frame_threshold_low_overridden.yfilter != YFilter.not_set or
                    self.frame_window.yfilter != YFilter.not_set or
                    self.frame_window_overridden.yfilter != YFilter.not_set or
                    self.high_threshold_action.yfilter != YFilter.not_set or
                    self.high_threshold_action_overridden.yfilter != YFilter.not_set or
                    self.link_fault_action.yfilter != YFilter.not_set or
                    self.link_fault_action_overridden.yfilter != YFilter.not_set or
                    self.link_monitor_enabled.yfilter != YFilter.not_set or
                    self.link_monitoring_enabled_overridden.yfilter != YFilter.not_set or
                    self.mib_retrieval_enabled.yfilter != YFilter.not_set or
                    self.mib_retrieval_enabled_overridden.yfilter != YFilter.not_set or
                    self.mode.yfilter != YFilter.not_set or
                    self.mode_overridden.yfilter != YFilter.not_set or
                    self.remote_loopback_action.yfilter != YFilter.not_set or
                    self.remote_loopback_action_overridden.yfilter != YFilter.not_set or
                    self.remote_loopback_enabled.yfilter != YFilter.not_set or
                    self.remote_loopback_enabled_overridden.yfilter != YFilter.not_set or
                    self.require_link_monitoring.yfilter != YFilter.not_set or
                    self.require_link_monitoring_overridden.yfilter != YFilter.not_set or
                    self.require_loopback.yfilter != YFilter.not_set or
                    self.require_loopback_overridden.yfilter != YFilter.not_set or
                    self.require_mib_retrieval_overridden.yfilter != YFilter.not_set or
                    self.require_mode_overridden.yfilter != YFilter.not_set or
                    self.require_remote_mib_retrieval.yfilter != YFilter.not_set or
                    self.require_remote_mode.yfilter != YFilter.not_set or
                    self.session_down_action.yfilter != YFilter.not_set or
                    self.session_down_action_overridden.yfilter != YFilter.not_set or
                    self.session_up_action.yfilter != YFilter.not_set or
                    self.session_up_action_overridden.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_high.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_high_multiplier.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_high_overridden.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_low.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_low_multiplier.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_low_overridden.yfilter != YFilter.not_set or
                    self.symbol_period_threshold_units.yfilter != YFilter.not_set or
                    self.symbol_period_window.yfilter != YFilter.not_set or
                    self.symbol_period_window_multiplier.yfilter != YFilter.not_set or
                    self.symbol_period_window_overridden.yfilter != YFilter.not_set or
                    self.symbol_period_window_units.yfilter != YFilter.not_set or
                    self.udlf_enabled.yfilter != YFilter.not_set or
                    self.udlf_enabled_overridden.yfilter != YFilter.not_set or
                    self.wiring_conflict_action.yfilter != YFilter.not_set or
                    self.wiring_conflict_action_overridden.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "running-config-interface" + "[member-interface='" + self.member_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/running-config-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.member_interface.is_set or self.member_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.member_interface.get_name_leafdata())
                if (self.capabilities_conflict_action.is_set or self.capabilities_conflict_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capabilities_conflict_action.get_name_leafdata())
                if (self.capabilities_conflict_action_overridden.is_set or self.capabilities_conflict_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.capabilities_conflict_action_overridden.get_name_leafdata())
                if (self.connection_timeout.is_set or self.connection_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connection_timeout.get_name_leafdata())
                if (self.connection_timeout_overridden.is_set or self.connection_timeout_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connection_timeout_overridden.get_name_leafdata())
                if (self.critical_event_action.is_set or self.critical_event_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.critical_event_action.get_name_leafdata())
                if (self.critical_event_action_overridden.is_set or self.critical_event_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.critical_event_action_overridden.get_name_leafdata())
                if (self.discovery_timeout_action.is_set or self.discovery_timeout_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_timeout_action.get_name_leafdata())
                if (self.discovery_timeout_action_overridden.is_set or self.discovery_timeout_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discovery_timeout_action_overridden.get_name_leafdata())
                if (self.dying_gasp_action.is_set or self.dying_gasp_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dying_gasp_action.get_name_leafdata())
                if (self.dying_gasp_action_overridden.is_set or self.dying_gasp_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dying_gasp_action_overridden.get_name_leafdata())
                if (self.fast_hello_interval_enabled.is_set or self.fast_hello_interval_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fast_hello_interval_enabled.get_name_leafdata())
                if (self.fast_hello_interval_enabled_overridden.is_set or self.fast_hello_interval_enabled_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fast_hello_interval_enabled_overridden.get_name_leafdata())
                if (self.frame_period_threshold_high.is_set or self.frame_period_threshold_high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_high.get_name_leafdata())
                if (self.frame_period_threshold_high_multiplier.is_set or self.frame_period_threshold_high_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_high_multiplier.get_name_leafdata())
                if (self.frame_period_threshold_high_overridden.is_set or self.frame_period_threshold_high_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_high_overridden.get_name_leafdata())
                if (self.frame_period_threshold_low.is_set or self.frame_period_threshold_low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_low.get_name_leafdata())
                if (self.frame_period_threshold_low_multiplier.is_set or self.frame_period_threshold_low_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_low_multiplier.get_name_leafdata())
                if (self.frame_period_threshold_low_overridden.is_set or self.frame_period_threshold_low_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_low_overridden.get_name_leafdata())
                if (self.frame_period_threshold_units.is_set or self.frame_period_threshold_units.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_threshold_units.get_name_leafdata())
                if (self.frame_period_window.is_set or self.frame_period_window.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_window.get_name_leafdata())
                if (self.frame_period_window_multiplier.is_set or self.frame_period_window_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_window_multiplier.get_name_leafdata())
                if (self.frame_period_window_overridden.is_set or self.frame_period_window_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_window_overridden.get_name_leafdata())
                if (self.frame_period_window_units.is_set or self.frame_period_window_units.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_period_window_units.get_name_leafdata())
                if (self.frame_seconds_threshold_high.is_set or self.frame_seconds_threshold_high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_threshold_high.get_name_leafdata())
                if (self.frame_seconds_threshold_high_overridden.is_set or self.frame_seconds_threshold_high_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_threshold_high_overridden.get_name_leafdata())
                if (self.frame_seconds_threshold_low.is_set or self.frame_seconds_threshold_low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_threshold_low.get_name_leafdata())
                if (self.frame_seconds_threshold_low_overridden.is_set or self.frame_seconds_threshold_low_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_threshold_low_overridden.get_name_leafdata())
                if (self.frame_seconds_window.is_set or self.frame_seconds_window.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_window.get_name_leafdata())
                if (self.frame_seconds_window_overridden.is_set or self.frame_seconds_window_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_seconds_window_overridden.get_name_leafdata())
                if (self.frame_threshold_high.is_set or self.frame_threshold_high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_high.get_name_leafdata())
                if (self.frame_threshold_high_multiplier.is_set or self.frame_threshold_high_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_high_multiplier.get_name_leafdata())
                if (self.frame_threshold_high_overridden.is_set or self.frame_threshold_high_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_high_overridden.get_name_leafdata())
                if (self.frame_threshold_low.is_set or self.frame_threshold_low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_low.get_name_leafdata())
                if (self.frame_threshold_low_multiplier.is_set or self.frame_threshold_low_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_low_multiplier.get_name_leafdata())
                if (self.frame_threshold_low_overridden.is_set or self.frame_threshold_low_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_threshold_low_overridden.get_name_leafdata())
                if (self.frame_window.is_set or self.frame_window.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_window.get_name_leafdata())
                if (self.frame_window_overridden.is_set or self.frame_window_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frame_window_overridden.get_name_leafdata())
                if (self.high_threshold_action.is_set or self.high_threshold_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.high_threshold_action.get_name_leafdata())
                if (self.high_threshold_action_overridden.is_set or self.high_threshold_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.high_threshold_action_overridden.get_name_leafdata())
                if (self.link_fault_action.is_set or self.link_fault_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.link_fault_action.get_name_leafdata())
                if (self.link_fault_action_overridden.is_set or self.link_fault_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.link_fault_action_overridden.get_name_leafdata())
                if (self.link_monitor_enabled.is_set or self.link_monitor_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.link_monitor_enabled.get_name_leafdata())
                if (self.link_monitoring_enabled_overridden.is_set or self.link_monitoring_enabled_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.link_monitoring_enabled_overridden.get_name_leafdata())
                if (self.mib_retrieval_enabled.is_set or self.mib_retrieval_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mib_retrieval_enabled.get_name_leafdata())
                if (self.mib_retrieval_enabled_overridden.is_set or self.mib_retrieval_enabled_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mib_retrieval_enabled_overridden.get_name_leafdata())
                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode.get_name_leafdata())
                if (self.mode_overridden.is_set or self.mode_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode_overridden.get_name_leafdata())
                if (self.remote_loopback_action.is_set or self.remote_loopback_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback_action.get_name_leafdata())
                if (self.remote_loopback_action_overridden.is_set or self.remote_loopback_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback_action_overridden.get_name_leafdata())
                if (self.remote_loopback_enabled.is_set or self.remote_loopback_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback_enabled.get_name_leafdata())
                if (self.remote_loopback_enabled_overridden.is_set or self.remote_loopback_enabled_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_loopback_enabled_overridden.get_name_leafdata())
                if (self.require_link_monitoring.is_set or self.require_link_monitoring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_link_monitoring.get_name_leafdata())
                if (self.require_link_monitoring_overridden.is_set or self.require_link_monitoring_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_link_monitoring_overridden.get_name_leafdata())
                if (self.require_loopback.is_set or self.require_loopback.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_loopback.get_name_leafdata())
                if (self.require_loopback_overridden.is_set or self.require_loopback_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_loopback_overridden.get_name_leafdata())
                if (self.require_mib_retrieval_overridden.is_set or self.require_mib_retrieval_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_mib_retrieval_overridden.get_name_leafdata())
                if (self.require_mode_overridden.is_set or self.require_mode_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_mode_overridden.get_name_leafdata())
                if (self.require_remote_mib_retrieval.is_set or self.require_remote_mib_retrieval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_remote_mib_retrieval.get_name_leafdata())
                if (self.require_remote_mode.is_set or self.require_remote_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.require_remote_mode.get_name_leafdata())
                if (self.session_down_action.is_set or self.session_down_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_down_action.get_name_leafdata())
                if (self.session_down_action_overridden.is_set or self.session_down_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_down_action_overridden.get_name_leafdata())
                if (self.session_up_action.is_set or self.session_up_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_up_action.get_name_leafdata())
                if (self.session_up_action_overridden.is_set or self.session_up_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_up_action_overridden.get_name_leafdata())
                if (self.symbol_period_threshold_high.is_set or self.symbol_period_threshold_high.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_high.get_name_leafdata())
                if (self.symbol_period_threshold_high_multiplier.is_set or self.symbol_period_threshold_high_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_high_multiplier.get_name_leafdata())
                if (self.symbol_period_threshold_high_overridden.is_set or self.symbol_period_threshold_high_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_high_overridden.get_name_leafdata())
                if (self.symbol_period_threshold_low.is_set or self.symbol_period_threshold_low.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_low.get_name_leafdata())
                if (self.symbol_period_threshold_low_multiplier.is_set or self.symbol_period_threshold_low_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_low_multiplier.get_name_leafdata())
                if (self.symbol_period_threshold_low_overridden.is_set or self.symbol_period_threshold_low_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_low_overridden.get_name_leafdata())
                if (self.symbol_period_threshold_units.is_set or self.symbol_period_threshold_units.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_threshold_units.get_name_leafdata())
                if (self.symbol_period_window.is_set or self.symbol_period_window.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_window.get_name_leafdata())
                if (self.symbol_period_window_multiplier.is_set or self.symbol_period_window_multiplier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_window_multiplier.get_name_leafdata())
                if (self.symbol_period_window_overridden.is_set or self.symbol_period_window_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_window_overridden.get_name_leafdata())
                if (self.symbol_period_window_units.is_set or self.symbol_period_window_units.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.symbol_period_window_units.get_name_leafdata())
                if (self.udlf_enabled.is_set or self.udlf_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udlf_enabled.get_name_leafdata())
                if (self.udlf_enabled_overridden.is_set or self.udlf_enabled_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.udlf_enabled_overridden.get_name_leafdata())
                if (self.wiring_conflict_action.is_set or self.wiring_conflict_action.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.wiring_conflict_action.get_name_leafdata())
                if (self.wiring_conflict_action_overridden.is_set or self.wiring_conflict_action_overridden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.wiring_conflict_action_overridden.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "member-interface" or name == "capabilities-conflict-action" or name == "capabilities-conflict-action-overridden" or name == "connection-timeout" or name == "connection-timeout-overridden" or name == "critical-event-action" or name == "critical-event-action-overridden" or name == "discovery-timeout-action" or name == "discovery-timeout-action-overridden" or name == "dying-gasp-action" or name == "dying-gasp-action-overridden" or name == "fast-hello-interval-enabled" or name == "fast-hello-interval-enabled-overridden" or name == "frame-period-threshold-high" or name == "frame-period-threshold-high-multiplier" or name == "frame-period-threshold-high-overridden" or name == "frame-period-threshold-low" or name == "frame-period-threshold-low-multiplier" or name == "frame-period-threshold-low-overridden" or name == "frame-period-threshold-units" or name == "frame-period-window" or name == "frame-period-window-multiplier" or name == "frame-period-window-overridden" or name == "frame-period-window-units" or name == "frame-seconds-threshold-high" or name == "frame-seconds-threshold-high-overridden" or name == "frame-seconds-threshold-low" or name == "frame-seconds-threshold-low-overridden" or name == "frame-seconds-window" or name == "frame-seconds-window-overridden" or name == "frame-threshold-high" or name == "frame-threshold-high-multiplier" or name == "frame-threshold-high-overridden" or name == "frame-threshold-low" or name == "frame-threshold-low-multiplier" or name == "frame-threshold-low-overridden" or name == "frame-window" or name == "frame-window-overridden" or name == "high-threshold-action" or name == "high-threshold-action-overridden" or name == "link-fault-action" or name == "link-fault-action-overridden" or name == "link-monitor-enabled" or name == "link-monitoring-enabled-overridden" or name == "mib-retrieval-enabled" or name == "mib-retrieval-enabled-overridden" or name == "mode" or name == "mode-overridden" or name == "remote-loopback-action" or name == "remote-loopback-action-overridden" or name == "remote-loopback-enabled" or name == "remote-loopback-enabled-overridden" or name == "require-link-monitoring" or name == "require-link-monitoring-overridden" or name == "require-loopback" or name == "require-loopback-overridden" or name == "require-mib-retrieval-overridden" or name == "require-mode-overridden" or name == "require-remote-mib-retrieval" or name == "require-remote-mode" or name == "session-down-action" or name == "session-down-action-overridden" or name == "session-up-action" or name == "session-up-action-overridden" or name == "symbol-period-threshold-high" or name == "symbol-period-threshold-high-multiplier" or name == "symbol-period-threshold-high-overridden" or name == "symbol-period-threshold-low" or name == "symbol-period-threshold-low-multiplier" or name == "symbol-period-threshold-low-overridden" or name == "symbol-period-threshold-units" or name == "symbol-period-window" or name == "symbol-period-window-multiplier" or name == "symbol-period-window-overridden" or name == "symbol-period-window-units" or name == "udlf-enabled" or name == "udlf-enabled-overridden" or name == "wiring-conflict-action" or name == "wiring-conflict-action-overridden"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "member-interface"):
                    self.member_interface = value
                    self.member_interface.value_namespace = name_space
                    self.member_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "capabilities-conflict-action"):
                    self.capabilities_conflict_action = value
                    self.capabilities_conflict_action.value_namespace = name_space
                    self.capabilities_conflict_action.value_namespace_prefix = name_space_prefix
                if(value_path == "capabilities-conflict-action-overridden"):
                    self.capabilities_conflict_action_overridden = value
                    self.capabilities_conflict_action_overridden.value_namespace = name_space
                    self.capabilities_conflict_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "connection-timeout"):
                    self.connection_timeout = value
                    self.connection_timeout.value_namespace = name_space
                    self.connection_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "connection-timeout-overridden"):
                    self.connection_timeout_overridden = value
                    self.connection_timeout_overridden.value_namespace = name_space
                    self.connection_timeout_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "critical-event-action"):
                    self.critical_event_action = value
                    self.critical_event_action.value_namespace = name_space
                    self.critical_event_action.value_namespace_prefix = name_space_prefix
                if(value_path == "critical-event-action-overridden"):
                    self.critical_event_action_overridden = value
                    self.critical_event_action_overridden.value_namespace = name_space
                    self.critical_event_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "discovery-timeout-action"):
                    self.discovery_timeout_action = value
                    self.discovery_timeout_action.value_namespace = name_space
                    self.discovery_timeout_action.value_namespace_prefix = name_space_prefix
                if(value_path == "discovery-timeout-action-overridden"):
                    self.discovery_timeout_action_overridden = value
                    self.discovery_timeout_action_overridden.value_namespace = name_space
                    self.discovery_timeout_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "dying-gasp-action"):
                    self.dying_gasp_action = value
                    self.dying_gasp_action.value_namespace = name_space
                    self.dying_gasp_action.value_namespace_prefix = name_space_prefix
                if(value_path == "dying-gasp-action-overridden"):
                    self.dying_gasp_action_overridden = value
                    self.dying_gasp_action_overridden.value_namespace = name_space
                    self.dying_gasp_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "fast-hello-interval-enabled"):
                    self.fast_hello_interval_enabled = value
                    self.fast_hello_interval_enabled.value_namespace = name_space
                    self.fast_hello_interval_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "fast-hello-interval-enabled-overridden"):
                    self.fast_hello_interval_enabled_overridden = value
                    self.fast_hello_interval_enabled_overridden.value_namespace = name_space
                    self.fast_hello_interval_enabled_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-high"):
                    self.frame_period_threshold_high = value
                    self.frame_period_threshold_high.value_namespace = name_space
                    self.frame_period_threshold_high.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-high-multiplier"):
                    self.frame_period_threshold_high_multiplier = value
                    self.frame_period_threshold_high_multiplier.value_namespace = name_space
                    self.frame_period_threshold_high_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-high-overridden"):
                    self.frame_period_threshold_high_overridden = value
                    self.frame_period_threshold_high_overridden.value_namespace = name_space
                    self.frame_period_threshold_high_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-low"):
                    self.frame_period_threshold_low = value
                    self.frame_period_threshold_low.value_namespace = name_space
                    self.frame_period_threshold_low.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-low-multiplier"):
                    self.frame_period_threshold_low_multiplier = value
                    self.frame_period_threshold_low_multiplier.value_namespace = name_space
                    self.frame_period_threshold_low_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-low-overridden"):
                    self.frame_period_threshold_low_overridden = value
                    self.frame_period_threshold_low_overridden.value_namespace = name_space
                    self.frame_period_threshold_low_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-threshold-units"):
                    self.frame_period_threshold_units = value
                    self.frame_period_threshold_units.value_namespace = name_space
                    self.frame_period_threshold_units.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-window"):
                    self.frame_period_window = value
                    self.frame_period_window.value_namespace = name_space
                    self.frame_period_window.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-window-multiplier"):
                    self.frame_period_window_multiplier = value
                    self.frame_period_window_multiplier.value_namespace = name_space
                    self.frame_period_window_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-window-overridden"):
                    self.frame_period_window_overridden = value
                    self.frame_period_window_overridden.value_namespace = name_space
                    self.frame_period_window_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-period-window-units"):
                    self.frame_period_window_units = value
                    self.frame_period_window_units.value_namespace = name_space
                    self.frame_period_window_units.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-threshold-high"):
                    self.frame_seconds_threshold_high = value
                    self.frame_seconds_threshold_high.value_namespace = name_space
                    self.frame_seconds_threshold_high.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-threshold-high-overridden"):
                    self.frame_seconds_threshold_high_overridden = value
                    self.frame_seconds_threshold_high_overridden.value_namespace = name_space
                    self.frame_seconds_threshold_high_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-threshold-low"):
                    self.frame_seconds_threshold_low = value
                    self.frame_seconds_threshold_low.value_namespace = name_space
                    self.frame_seconds_threshold_low.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-threshold-low-overridden"):
                    self.frame_seconds_threshold_low_overridden = value
                    self.frame_seconds_threshold_low_overridden.value_namespace = name_space
                    self.frame_seconds_threshold_low_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-window"):
                    self.frame_seconds_window = value
                    self.frame_seconds_window.value_namespace = name_space
                    self.frame_seconds_window.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-seconds-window-overridden"):
                    self.frame_seconds_window_overridden = value
                    self.frame_seconds_window_overridden.value_namespace = name_space
                    self.frame_seconds_window_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-high"):
                    self.frame_threshold_high = value
                    self.frame_threshold_high.value_namespace = name_space
                    self.frame_threshold_high.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-high-multiplier"):
                    self.frame_threshold_high_multiplier = value
                    self.frame_threshold_high_multiplier.value_namespace = name_space
                    self.frame_threshold_high_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-high-overridden"):
                    self.frame_threshold_high_overridden = value
                    self.frame_threshold_high_overridden.value_namespace = name_space
                    self.frame_threshold_high_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-low"):
                    self.frame_threshold_low = value
                    self.frame_threshold_low.value_namespace = name_space
                    self.frame_threshold_low.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-low-multiplier"):
                    self.frame_threshold_low_multiplier = value
                    self.frame_threshold_low_multiplier.value_namespace = name_space
                    self.frame_threshold_low_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-threshold-low-overridden"):
                    self.frame_threshold_low_overridden = value
                    self.frame_threshold_low_overridden.value_namespace = name_space
                    self.frame_threshold_low_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-window"):
                    self.frame_window = value
                    self.frame_window.value_namespace = name_space
                    self.frame_window.value_namespace_prefix = name_space_prefix
                if(value_path == "frame-window-overridden"):
                    self.frame_window_overridden = value
                    self.frame_window_overridden.value_namespace = name_space
                    self.frame_window_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "high-threshold-action"):
                    self.high_threshold_action = value
                    self.high_threshold_action.value_namespace = name_space
                    self.high_threshold_action.value_namespace_prefix = name_space_prefix
                if(value_path == "high-threshold-action-overridden"):
                    self.high_threshold_action_overridden = value
                    self.high_threshold_action_overridden.value_namespace = name_space
                    self.high_threshold_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "link-fault-action"):
                    self.link_fault_action = value
                    self.link_fault_action.value_namespace = name_space
                    self.link_fault_action.value_namespace_prefix = name_space_prefix
                if(value_path == "link-fault-action-overridden"):
                    self.link_fault_action_overridden = value
                    self.link_fault_action_overridden.value_namespace = name_space
                    self.link_fault_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "link-monitor-enabled"):
                    self.link_monitor_enabled = value
                    self.link_monitor_enabled.value_namespace = name_space
                    self.link_monitor_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "link-monitoring-enabled-overridden"):
                    self.link_monitoring_enabled_overridden = value
                    self.link_monitoring_enabled_overridden.value_namespace = name_space
                    self.link_monitoring_enabled_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "mib-retrieval-enabled"):
                    self.mib_retrieval_enabled = value
                    self.mib_retrieval_enabled.value_namespace = name_space
                    self.mib_retrieval_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "mib-retrieval-enabled-overridden"):
                    self.mib_retrieval_enabled_overridden = value
                    self.mib_retrieval_enabled_overridden.value_namespace = name_space
                    self.mib_retrieval_enabled_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "mode"):
                    self.mode = value
                    self.mode.value_namespace = name_space
                    self.mode.value_namespace_prefix = name_space_prefix
                if(value_path == "mode-overridden"):
                    self.mode_overridden = value
                    self.mode_overridden.value_namespace = name_space
                    self.mode_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback-action"):
                    self.remote_loopback_action = value
                    self.remote_loopback_action.value_namespace = name_space
                    self.remote_loopback_action.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback-action-overridden"):
                    self.remote_loopback_action_overridden = value
                    self.remote_loopback_action_overridden.value_namespace = name_space
                    self.remote_loopback_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback-enabled"):
                    self.remote_loopback_enabled = value
                    self.remote_loopback_enabled.value_namespace = name_space
                    self.remote_loopback_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-loopback-enabled-overridden"):
                    self.remote_loopback_enabled_overridden = value
                    self.remote_loopback_enabled_overridden.value_namespace = name_space
                    self.remote_loopback_enabled_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "require-link-monitoring"):
                    self.require_link_monitoring = value
                    self.require_link_monitoring.value_namespace = name_space
                    self.require_link_monitoring.value_namespace_prefix = name_space_prefix
                if(value_path == "require-link-monitoring-overridden"):
                    self.require_link_monitoring_overridden = value
                    self.require_link_monitoring_overridden.value_namespace = name_space
                    self.require_link_monitoring_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "require-loopback"):
                    self.require_loopback = value
                    self.require_loopback.value_namespace = name_space
                    self.require_loopback.value_namespace_prefix = name_space_prefix
                if(value_path == "require-loopback-overridden"):
                    self.require_loopback_overridden = value
                    self.require_loopback_overridden.value_namespace = name_space
                    self.require_loopback_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "require-mib-retrieval-overridden"):
                    self.require_mib_retrieval_overridden = value
                    self.require_mib_retrieval_overridden.value_namespace = name_space
                    self.require_mib_retrieval_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "require-mode-overridden"):
                    self.require_mode_overridden = value
                    self.require_mode_overridden.value_namespace = name_space
                    self.require_mode_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "require-remote-mib-retrieval"):
                    self.require_remote_mib_retrieval = value
                    self.require_remote_mib_retrieval.value_namespace = name_space
                    self.require_remote_mib_retrieval.value_namespace_prefix = name_space_prefix
                if(value_path == "require-remote-mode"):
                    self.require_remote_mode = value
                    self.require_remote_mode.value_namespace = name_space
                    self.require_remote_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "session-down-action"):
                    self.session_down_action = value
                    self.session_down_action.value_namespace = name_space
                    self.session_down_action.value_namespace_prefix = name_space_prefix
                if(value_path == "session-down-action-overridden"):
                    self.session_down_action_overridden = value
                    self.session_down_action_overridden.value_namespace = name_space
                    self.session_down_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "session-up-action"):
                    self.session_up_action = value
                    self.session_up_action.value_namespace = name_space
                    self.session_up_action.value_namespace_prefix = name_space_prefix
                if(value_path == "session-up-action-overridden"):
                    self.session_up_action_overridden = value
                    self.session_up_action_overridden.value_namespace = name_space
                    self.session_up_action_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-high"):
                    self.symbol_period_threshold_high = value
                    self.symbol_period_threshold_high.value_namespace = name_space
                    self.symbol_period_threshold_high.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-high-multiplier"):
                    self.symbol_period_threshold_high_multiplier = value
                    self.symbol_period_threshold_high_multiplier.value_namespace = name_space
                    self.symbol_period_threshold_high_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-high-overridden"):
                    self.symbol_period_threshold_high_overridden = value
                    self.symbol_period_threshold_high_overridden.value_namespace = name_space
                    self.symbol_period_threshold_high_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-low"):
                    self.symbol_period_threshold_low = value
                    self.symbol_period_threshold_low.value_namespace = name_space
                    self.symbol_period_threshold_low.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-low-multiplier"):
                    self.symbol_period_threshold_low_multiplier = value
                    self.symbol_period_threshold_low_multiplier.value_namespace = name_space
                    self.symbol_period_threshold_low_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-low-overridden"):
                    self.symbol_period_threshold_low_overridden = value
                    self.symbol_period_threshold_low_overridden.value_namespace = name_space
                    self.symbol_period_threshold_low_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-threshold-units"):
                    self.symbol_period_threshold_units = value
                    self.symbol_period_threshold_units.value_namespace = name_space
                    self.symbol_period_threshold_units.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-window"):
                    self.symbol_period_window = value
                    self.symbol_period_window.value_namespace = name_space
                    self.symbol_period_window.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-window-multiplier"):
                    self.symbol_period_window_multiplier = value
                    self.symbol_period_window_multiplier.value_namespace = name_space
                    self.symbol_period_window_multiplier.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-window-overridden"):
                    self.symbol_period_window_overridden = value
                    self.symbol_period_window_overridden.value_namespace = name_space
                    self.symbol_period_window_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "symbol-period-window-units"):
                    self.symbol_period_window_units = value
                    self.symbol_period_window_units.value_namespace = name_space
                    self.symbol_period_window_units.value_namespace_prefix = name_space_prefix
                if(value_path == "udlf-enabled"):
                    self.udlf_enabled = value
                    self.udlf_enabled.value_namespace = name_space
                    self.udlf_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "udlf-enabled-overridden"):
                    self.udlf_enabled_overridden = value
                    self.udlf_enabled_overridden.value_namespace = name_space
                    self.udlf_enabled_overridden.value_namespace_prefix = name_space_prefix
                if(value_path == "wiring-conflict-action"):
                    self.wiring_conflict_action = value
                    self.wiring_conflict_action.value_namespace = name_space
                    self.wiring_conflict_action.value_namespace_prefix = name_space_prefix
                if(value_path == "wiring-conflict-action-overridden"):
                    self.wiring_conflict_action_overridden = value
                    self.wiring_conflict_action_overridden.value_namespace = name_space
                    self.wiring_conflict_action_overridden.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.running_config_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.running_config_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "running-config-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "running-config-interface"):
                for c in self.running_config_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.running_config_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "running-config-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.Nodes, self).__setattr__(name, value)


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

                self.node_name = YLeaf(YType.str, "node-name")

                self.summary = EtherLinkOam.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.Nodes.Node, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_send",
                                    "evaluating",
                                    "events",
                                    "interfaces",
                                    "local_accept",
                                    "local_events",
                                    "local_frame",
                                    "local_frame_period",
                                    "local_frame_seconds",
                                    "local_reject",
                                    "local_symbol_period",
                                    "loopback_mode",
                                    "miswired_connections",
                                    "operational",
                                    "passive_wait",
                                    "port_down",
                                    "remote_events",
                                    "remote_frame",
                                    "remote_frame_period",
                                    "remote_frame_seconds",
                                    "remote_reject",
                                    "remote_symbol_period") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EtherLinkOam.Nodes.Node.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EtherLinkOam.Nodes.Node.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_send.is_set or
                        self.evaluating.is_set or
                        self.events.is_set or
                        self.interfaces.is_set or
                        self.local_accept.is_set or
                        self.local_events.is_set or
                        self.local_frame.is_set or
                        self.local_frame_period.is_set or
                        self.local_frame_seconds.is_set or
                        self.local_reject.is_set or
                        self.local_symbol_period.is_set or
                        self.loopback_mode.is_set or
                        self.miswired_connections.is_set or
                        self.operational.is_set or
                        self.passive_wait.is_set or
                        self.port_down.is_set or
                        self.remote_events.is_set or
                        self.remote_frame.is_set or
                        self.remote_frame_period.is_set or
                        self.remote_frame_seconds.is_set or
                        self.remote_reject.is_set or
                        self.remote_symbol_period.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_send.yfilter != YFilter.not_set or
                        self.evaluating.yfilter != YFilter.not_set or
                        self.events.yfilter != YFilter.not_set or
                        self.interfaces.yfilter != YFilter.not_set or
                        self.local_accept.yfilter != YFilter.not_set or
                        self.local_events.yfilter != YFilter.not_set or
                        self.local_frame.yfilter != YFilter.not_set or
                        self.local_frame_period.yfilter != YFilter.not_set or
                        self.local_frame_seconds.yfilter != YFilter.not_set or
                        self.local_reject.yfilter != YFilter.not_set or
                        self.local_symbol_period.yfilter != YFilter.not_set or
                        self.loopback_mode.yfilter != YFilter.not_set or
                        self.miswired_connections.yfilter != YFilter.not_set or
                        self.operational.yfilter != YFilter.not_set or
                        self.passive_wait.yfilter != YFilter.not_set or
                        self.port_down.yfilter != YFilter.not_set or
                        self.remote_events.yfilter != YFilter.not_set or
                        self.remote_frame.yfilter != YFilter.not_set or
                        self.remote_frame_period.yfilter != YFilter.not_set or
                        self.remote_frame_seconds.yfilter != YFilter.not_set or
                        self.remote_reject.yfilter != YFilter.not_set or
                        self.remote_symbol_period.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_send.is_set or self.active_send.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_send.get_name_leafdata())
                    if (self.evaluating.is_set or self.evaluating.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.evaluating.get_name_leafdata())
                    if (self.events.is_set or self.events.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.events.get_name_leafdata())
                    if (self.interfaces.is_set or self.interfaces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interfaces.get_name_leafdata())
                    if (self.local_accept.is_set or self.local_accept.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_accept.get_name_leafdata())
                    if (self.local_events.is_set or self.local_events.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_events.get_name_leafdata())
                    if (self.local_frame.is_set or self.local_frame.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_frame.get_name_leafdata())
                    if (self.local_frame_period.is_set or self.local_frame_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_frame_period.get_name_leafdata())
                    if (self.local_frame_seconds.is_set or self.local_frame_seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_frame_seconds.get_name_leafdata())
                    if (self.local_reject.is_set or self.local_reject.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_reject.get_name_leafdata())
                    if (self.local_symbol_period.is_set or self.local_symbol_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_symbol_period.get_name_leafdata())
                    if (self.loopback_mode.is_set or self.loopback_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loopback_mode.get_name_leafdata())
                    if (self.miswired_connections.is_set or self.miswired_connections.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.miswired_connections.get_name_leafdata())
                    if (self.operational.is_set or self.operational.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational.get_name_leafdata())
                    if (self.passive_wait.is_set or self.passive_wait.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.passive_wait.get_name_leafdata())
                    if (self.port_down.is_set or self.port_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_down.get_name_leafdata())
                    if (self.remote_events.is_set or self.remote_events.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_events.get_name_leafdata())
                    if (self.remote_frame.is_set or self.remote_frame.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_frame.get_name_leafdata())
                    if (self.remote_frame_period.is_set or self.remote_frame_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_frame_period.get_name_leafdata())
                    if (self.remote_frame_seconds.is_set or self.remote_frame_seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_frame_seconds.get_name_leafdata())
                    if (self.remote_reject.is_set or self.remote_reject.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_reject.get_name_leafdata())
                    if (self.remote_symbol_period.is_set or self.remote_symbol_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_symbol_period.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-send" or name == "evaluating" or name == "events" or name == "interfaces" or name == "local-accept" or name == "local-events" or name == "local-frame" or name == "local-frame-period" or name == "local-frame-seconds" or name == "local-reject" or name == "local-symbol-period" or name == "loopback-mode" or name == "miswired-connections" or name == "operational" or name == "passive-wait" or name == "port-down" or name == "remote-events" or name == "remote-frame" or name == "remote-frame-period" or name == "remote-frame-seconds" or name == "remote-reject" or name == "remote-symbol-period"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-send"):
                        self.active_send = value
                        self.active_send.value_namespace = name_space
                        self.active_send.value_namespace_prefix = name_space_prefix
                    if(value_path == "evaluating"):
                        self.evaluating = value
                        self.evaluating.value_namespace = name_space
                        self.evaluating.value_namespace_prefix = name_space_prefix
                    if(value_path == "events"):
                        self.events = value
                        self.events.value_namespace = name_space
                        self.events.value_namespace_prefix = name_space_prefix
                    if(value_path == "interfaces"):
                        self.interfaces = value
                        self.interfaces.value_namespace = name_space
                        self.interfaces.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-accept"):
                        self.local_accept = value
                        self.local_accept.value_namespace = name_space
                        self.local_accept.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-events"):
                        self.local_events = value
                        self.local_events.value_namespace = name_space
                        self.local_events.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-frame"):
                        self.local_frame = value
                        self.local_frame.value_namespace = name_space
                        self.local_frame.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-frame-period"):
                        self.local_frame_period = value
                        self.local_frame_period.value_namespace = name_space
                        self.local_frame_period.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-frame-seconds"):
                        self.local_frame_seconds = value
                        self.local_frame_seconds.value_namespace = name_space
                        self.local_frame_seconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-reject"):
                        self.local_reject = value
                        self.local_reject.value_namespace = name_space
                        self.local_reject.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-symbol-period"):
                        self.local_symbol_period = value
                        self.local_symbol_period.value_namespace = name_space
                        self.local_symbol_period.value_namespace_prefix = name_space_prefix
                    if(value_path == "loopback-mode"):
                        self.loopback_mode = value
                        self.loopback_mode.value_namespace = name_space
                        self.loopback_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "miswired-connections"):
                        self.miswired_connections = value
                        self.miswired_connections.value_namespace = name_space
                        self.miswired_connections.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational"):
                        self.operational = value
                        self.operational.value_namespace = name_space
                        self.operational.value_namespace_prefix = name_space_prefix
                    if(value_path == "passive-wait"):
                        self.passive_wait = value
                        self.passive_wait.value_namespace = name_space
                        self.passive_wait.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-down"):
                        self.port_down = value
                        self.port_down.value_namespace = name_space
                        self.port_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-events"):
                        self.remote_events = value
                        self.remote_events.value_namespace = name_space
                        self.remote_events.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-frame"):
                        self.remote_frame = value
                        self.remote_frame.value_namespace = name_space
                        self.remote_frame.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-frame-period"):
                        self.remote_frame_period = value
                        self.remote_frame_period.value_namespace = name_space
                        self.remote_frame_period.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-frame-seconds"):
                        self.remote_frame_seconds = value
                        self.remote_frame_seconds.value_namespace = name_space
                        self.remote_frame_seconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-reject"):
                        self.remote_reject = value
                        self.remote_reject.value_namespace = name_space
                        self.remote_reject.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-symbol-period"):
                        self.remote_symbol_period = value
                        self.remote_symbol_period.value_namespace = name_space
                        self.remote_symbol_period.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = EtherLinkOam.Nodes.Node.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "summary" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.event_log_entry_interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.EventLogEntryInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.EventLogEntryInterfaces, self).__setattr__(name, value)


        class EventLogEntryInterface(Entity):
            """
            Ethernet Link OAM enabled interface to get
            Event Log Entry for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

                self.member_interface = YLeaf(YType.str, "member-interface")

                self.event_log_entry_indexes = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes()
                self.event_log_entry_indexes.parent = self
                self._children_name_map["event_log_entry_indexes"] = "event-log-entry-indexes"
                self._children_yang_names.add("event-log-entry-indexes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("member_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface, self).__setattr__(name, value)


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

                    self.event_log_entry_index = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes, self).__setattr__(name, value)


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
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("event_log_entry_index",
                                        "action_taken",
                                        "event_total",
                                        "handle",
                                        "index",
                                        "local_high_threshold",
                                        "local_high_threshold_config_units",
                                        "location",
                                        "oui",
                                        "running_total",
                                        "threshold",
                                        "threshold_config_units",
                                        "threshold_units",
                                        "timestamp",
                                        "type",
                                        "value",
                                        "value_config_units",
                                        "window",
                                        "window_config_units",
                                        "window_units") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.event_log_entry_index.is_set or
                            self.action_taken.is_set or
                            self.event_total.is_set or
                            self.handle.is_set or
                            self.index.is_set or
                            self.local_high_threshold.is_set or
                            self.local_high_threshold_config_units.is_set or
                            self.location.is_set or
                            self.oui.is_set or
                            self.running_total.is_set or
                            self.threshold.is_set or
                            self.threshold_config_units.is_set or
                            self.threshold_units.is_set or
                            self.timestamp.is_set or
                            self.type.is_set or
                            self.value.is_set or
                            self.value_config_units.is_set or
                            self.window.is_set or
                            self.window_config_units.is_set or
                            self.window_units.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.event_log_entry_index.yfilter != YFilter.not_set or
                            self.action_taken.yfilter != YFilter.not_set or
                            self.event_total.yfilter != YFilter.not_set or
                            self.handle.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            self.local_high_threshold.yfilter != YFilter.not_set or
                            self.local_high_threshold_config_units.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            self.oui.yfilter != YFilter.not_set or
                            self.running_total.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set or
                            self.threshold_config_units.yfilter != YFilter.not_set or
                            self.threshold_units.yfilter != YFilter.not_set or
                            self.timestamp.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set or
                            self.value_config_units.yfilter != YFilter.not_set or
                            self.window.yfilter != YFilter.not_set or
                            self.window_config_units.yfilter != YFilter.not_set or
                            self.window_units.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "event-log-entry-index" + "[event-log-entry-index='" + self.event_log_entry_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.event_log_entry_index.is_set or self.event_log_entry_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.event_log_entry_index.get_name_leafdata())
                        if (self.action_taken.is_set or self.action_taken.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.action_taken.get_name_leafdata())
                        if (self.event_total.is_set or self.event_total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.event_total.get_name_leafdata())
                        if (self.handle.is_set or self.handle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.handle.get_name_leafdata())
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())
                        if (self.local_high_threshold.is_set or self.local_high_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_high_threshold.get_name_leafdata())
                        if (self.local_high_threshold_config_units.is_set or self.local_high_threshold_config_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_high_threshold_config_units.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())
                        if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oui.get_name_leafdata())
                        if (self.running_total.is_set or self.running_total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.running_total.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())
                        if (self.threshold_config_units.is_set or self.threshold_config_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_config_units.get_name_leafdata())
                        if (self.threshold_units.is_set or self.threshold_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_units.get_name_leafdata())
                        if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timestamp.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value.get_name_leafdata())
                        if (self.value_config_units.is_set or self.value_config_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value_config_units.get_name_leafdata())
                        if (self.window.is_set or self.window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.window.get_name_leafdata())
                        if (self.window_config_units.is_set or self.window_config_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.window_config_units.get_name_leafdata())
                        if (self.window_units.is_set or self.window_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.window_units.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "event-log-entry-index" or name == "action-taken" or name == "event-total" or name == "handle" or name == "index" or name == "local-high-threshold" or name == "local-high-threshold-config-units" or name == "location" or name == "oui" or name == "running-total" or name == "threshold" or name == "threshold-config-units" or name == "threshold-units" or name == "timestamp" or name == "type" or name == "value" or name == "value-config-units" or name == "window" or name == "window-config-units" or name == "window-units"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "event-log-entry-index"):
                            self.event_log_entry_index = value
                            self.event_log_entry_index.value_namespace = name_space
                            self.event_log_entry_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "action-taken"):
                            self.action_taken = value
                            self.action_taken.value_namespace = name_space
                            self.action_taken.value_namespace_prefix = name_space_prefix
                        if(value_path == "event-total"):
                            self.event_total = value
                            self.event_total.value_namespace = name_space
                            self.event_total.value_namespace_prefix = name_space_prefix
                        if(value_path == "handle"):
                            self.handle = value
                            self.handle.value_namespace = name_space
                            self.handle.value_namespace_prefix = name_space_prefix
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-high-threshold"):
                            self.local_high_threshold = value
                            self.local_high_threshold.value_namespace = name_space
                            self.local_high_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-high-threshold-config-units"):
                            self.local_high_threshold_config_units = value
                            self.local_high_threshold_config_units.value_namespace = name_space
                            self.local_high_threshold_config_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix
                        if(value_path == "oui"):
                            self.oui = value
                            self.oui.value_namespace = name_space
                            self.oui.value_namespace_prefix = name_space_prefix
                        if(value_path == "running-total"):
                            self.running_total = value
                            self.running_total.value_namespace = name_space
                            self.running_total.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold-config-units"):
                            self.threshold_config_units = value
                            self.threshold_config_units.value_namespace = name_space
                            self.threshold_config_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold-units"):
                            self.threshold_units = value
                            self.threshold_units.value_namespace = name_space
                            self.threshold_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "timestamp"):
                            self.timestamp = value
                            self.timestamp.value_namespace = name_space
                            self.timestamp.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix
                        if(value_path == "value-config-units"):
                            self.value_config_units = value
                            self.value_config_units.value_namespace = name_space
                            self.value_config_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "window"):
                            self.window = value
                            self.window.value_namespace = name_space
                            self.window.value_namespace_prefix = name_space_prefix
                        if(value_path == "window-config-units"):
                            self.window_config_units = value
                            self.window_config_units.value_namespace = name_space
                            self.window_config_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "window-units"):
                            self.window_units = value
                            self.window_units.value_namespace = name_space
                            self.window_units.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.event_log_entry_index:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.event_log_entry_index:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "event-log-entry-indexes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "event-log-entry-index"):
                        for c in self.event_log_entry_index:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.event_log_entry_index.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "event-log-entry-index"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.member_interface.is_set or
                    (self.event_log_entry_indexes is not None and self.event_log_entry_indexes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.member_interface.yfilter != YFilter.not_set or
                    (self.event_log_entry_indexes is not None and self.event_log_entry_indexes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "event-log-entry-interface" + "[member-interface='" + self.member_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/event-log-entry-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.member_interface.is_set or self.member_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.member_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "event-log-entry-indexes"):
                    if (self.event_log_entry_indexes is None):
                        self.event_log_entry_indexes = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes()
                        self.event_log_entry_indexes.parent = self
                        self._children_name_map["event_log_entry_indexes"] = "event-log-entry-indexes"
                    return self.event_log_entry_indexes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "event-log-entry-indexes" or name == "member-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "member-interface"):
                    self.member_interface = value
                    self.member_interface.value_namespace = name_space
                    self.member_interface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.event_log_entry_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.event_log_entry_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "event-log-entry-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "event-log-entry-interface"):
                for c in self.event_log_entry_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.event_log_entry_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "event-log-entry-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.stats_interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EtherLinkOam.StatsInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherLinkOam.StatsInterfaces, self).__setattr__(name, value)


        class StatsInterface(Entity):
            """
            Ethernet Link OAM interface to get Stats for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("member_interface",
                                "duplicate_event_notification_rx",
                                "duplicate_event_notification_tx",
                                "fixed_frames_rx",
                                "frames_lost_due_to_oam",
                                "information_rx",
                                "information_tx",
                                "local_error_frame_period_records",
                                "local_error_frame_records",
                                "local_error_frame_second_records",
                                "local_error_symbol_period_records",
                                "loopback_control_rx",
                                "loopback_control_tx",
                                "org_specific_rx",
                                "org_specific_tx",
                                "remote_error_frame_period_records",
                                "remote_error_frame_records",
                                "remote_error_frame_second_records",
                                "remote_error_symbol_period_records",
                                "unique_event_notification_rx",
                                "unique_event_notification_tx",
                                "unsupported_codes_rx",
                                "unsupported_codes_tx",
                                "variable_request_rx",
                                "variable_request_tx",
                                "variable_response_rx",
                                "variable_response_tx") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherLinkOam.StatsInterfaces.StatsInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherLinkOam.StatsInterfaces.StatsInterface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.member_interface.is_set or
                    self.duplicate_event_notification_rx.is_set or
                    self.duplicate_event_notification_tx.is_set or
                    self.fixed_frames_rx.is_set or
                    self.frames_lost_due_to_oam.is_set or
                    self.information_rx.is_set or
                    self.information_tx.is_set or
                    self.local_error_frame_period_records.is_set or
                    self.local_error_frame_records.is_set or
                    self.local_error_frame_second_records.is_set or
                    self.local_error_symbol_period_records.is_set or
                    self.loopback_control_rx.is_set or
                    self.loopback_control_tx.is_set or
                    self.org_specific_rx.is_set or
                    self.org_specific_tx.is_set or
                    self.remote_error_frame_period_records.is_set or
                    self.remote_error_frame_records.is_set or
                    self.remote_error_frame_second_records.is_set or
                    self.remote_error_symbol_period_records.is_set or
                    self.unique_event_notification_rx.is_set or
                    self.unique_event_notification_tx.is_set or
                    self.unsupported_codes_rx.is_set or
                    self.unsupported_codes_tx.is_set or
                    self.variable_request_rx.is_set or
                    self.variable_request_tx.is_set or
                    self.variable_response_rx.is_set or
                    self.variable_response_tx.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.member_interface.yfilter != YFilter.not_set or
                    self.duplicate_event_notification_rx.yfilter != YFilter.not_set or
                    self.duplicate_event_notification_tx.yfilter != YFilter.not_set or
                    self.fixed_frames_rx.yfilter != YFilter.not_set or
                    self.frames_lost_due_to_oam.yfilter != YFilter.not_set or
                    self.information_rx.yfilter != YFilter.not_set or
                    self.information_tx.yfilter != YFilter.not_set or
                    self.local_error_frame_period_records.yfilter != YFilter.not_set or
                    self.local_error_frame_records.yfilter != YFilter.not_set or
                    self.local_error_frame_second_records.yfilter != YFilter.not_set or
                    self.local_error_symbol_period_records.yfilter != YFilter.not_set or
                    self.loopback_control_rx.yfilter != YFilter.not_set or
                    self.loopback_control_tx.yfilter != YFilter.not_set or
                    self.org_specific_rx.yfilter != YFilter.not_set or
                    self.org_specific_tx.yfilter != YFilter.not_set or
                    self.remote_error_frame_period_records.yfilter != YFilter.not_set or
                    self.remote_error_frame_records.yfilter != YFilter.not_set or
                    self.remote_error_frame_second_records.yfilter != YFilter.not_set or
                    self.remote_error_symbol_period_records.yfilter != YFilter.not_set or
                    self.unique_event_notification_rx.yfilter != YFilter.not_set or
                    self.unique_event_notification_tx.yfilter != YFilter.not_set or
                    self.unsupported_codes_rx.yfilter != YFilter.not_set or
                    self.unsupported_codes_tx.yfilter != YFilter.not_set or
                    self.variable_request_rx.yfilter != YFilter.not_set or
                    self.variable_request_tx.yfilter != YFilter.not_set or
                    self.variable_response_rx.yfilter != YFilter.not_set or
                    self.variable_response_tx.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stats-interface" + "[member-interface='" + self.member_interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/stats-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.member_interface.is_set or self.member_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.member_interface.get_name_leafdata())
                if (self.duplicate_event_notification_rx.is_set or self.duplicate_event_notification_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_event_notification_rx.get_name_leafdata())
                if (self.duplicate_event_notification_tx.is_set or self.duplicate_event_notification_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.duplicate_event_notification_tx.get_name_leafdata())
                if (self.fixed_frames_rx.is_set or self.fixed_frames_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fixed_frames_rx.get_name_leafdata())
                if (self.frames_lost_due_to_oam.is_set or self.frames_lost_due_to_oam.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.frames_lost_due_to_oam.get_name_leafdata())
                if (self.information_rx.is_set or self.information_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.information_rx.get_name_leafdata())
                if (self.information_tx.is_set or self.information_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.information_tx.get_name_leafdata())
                if (self.local_error_frame_period_records.is_set or self.local_error_frame_period_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_error_frame_period_records.get_name_leafdata())
                if (self.local_error_frame_records.is_set or self.local_error_frame_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_error_frame_records.get_name_leafdata())
                if (self.local_error_frame_second_records.is_set or self.local_error_frame_second_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_error_frame_second_records.get_name_leafdata())
                if (self.local_error_symbol_period_records.is_set or self.local_error_symbol_period_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_error_symbol_period_records.get_name_leafdata())
                if (self.loopback_control_rx.is_set or self.loopback_control_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.loopback_control_rx.get_name_leafdata())
                if (self.loopback_control_tx.is_set or self.loopback_control_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.loopback_control_tx.get_name_leafdata())
                if (self.org_specific_rx.is_set or self.org_specific_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.org_specific_rx.get_name_leafdata())
                if (self.org_specific_tx.is_set or self.org_specific_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.org_specific_tx.get_name_leafdata())
                if (self.remote_error_frame_period_records.is_set or self.remote_error_frame_period_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_error_frame_period_records.get_name_leafdata())
                if (self.remote_error_frame_records.is_set or self.remote_error_frame_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_error_frame_records.get_name_leafdata())
                if (self.remote_error_frame_second_records.is_set or self.remote_error_frame_second_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_error_frame_second_records.get_name_leafdata())
                if (self.remote_error_symbol_period_records.is_set or self.remote_error_symbol_period_records.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_error_symbol_period_records.get_name_leafdata())
                if (self.unique_event_notification_rx.is_set or self.unique_event_notification_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unique_event_notification_rx.get_name_leafdata())
                if (self.unique_event_notification_tx.is_set or self.unique_event_notification_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unique_event_notification_tx.get_name_leafdata())
                if (self.unsupported_codes_rx.is_set or self.unsupported_codes_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unsupported_codes_rx.get_name_leafdata())
                if (self.unsupported_codes_tx.is_set or self.unsupported_codes_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unsupported_codes_tx.get_name_leafdata())
                if (self.variable_request_rx.is_set or self.variable_request_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.variable_request_rx.get_name_leafdata())
                if (self.variable_request_tx.is_set or self.variable_request_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.variable_request_tx.get_name_leafdata())
                if (self.variable_response_rx.is_set or self.variable_response_rx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.variable_response_rx.get_name_leafdata())
                if (self.variable_response_tx.is_set or self.variable_response_tx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.variable_response_tx.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "member-interface" or name == "duplicate-event-notification-rx" or name == "duplicate-event-notification-tx" or name == "fixed-frames-rx" or name == "frames-lost-due-to-oam" or name == "information-rx" or name == "information-tx" or name == "local-error-frame-period-records" or name == "local-error-frame-records" or name == "local-error-frame-second-records" or name == "local-error-symbol-period-records" or name == "loopback-control-rx" or name == "loopback-control-tx" or name == "org-specific-rx" or name == "org-specific-tx" or name == "remote-error-frame-period-records" or name == "remote-error-frame-records" or name == "remote-error-frame-second-records" or name == "remote-error-symbol-period-records" or name == "unique-event-notification-rx" or name == "unique-event-notification-tx" or name == "unsupported-codes-rx" or name == "unsupported-codes-tx" or name == "variable-request-rx" or name == "variable-request-tx" or name == "variable-response-rx" or name == "variable-response-tx"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "member-interface"):
                    self.member_interface = value
                    self.member_interface.value_namespace = name_space
                    self.member_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-event-notification-rx"):
                    self.duplicate_event_notification_rx = value
                    self.duplicate_event_notification_rx.value_namespace = name_space
                    self.duplicate_event_notification_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "duplicate-event-notification-tx"):
                    self.duplicate_event_notification_tx = value
                    self.duplicate_event_notification_tx.value_namespace = name_space
                    self.duplicate_event_notification_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "fixed-frames-rx"):
                    self.fixed_frames_rx = value
                    self.fixed_frames_rx.value_namespace = name_space
                    self.fixed_frames_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "frames-lost-due-to-oam"):
                    self.frames_lost_due_to_oam = value
                    self.frames_lost_due_to_oam.value_namespace = name_space
                    self.frames_lost_due_to_oam.value_namespace_prefix = name_space_prefix
                if(value_path == "information-rx"):
                    self.information_rx = value
                    self.information_rx.value_namespace = name_space
                    self.information_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "information-tx"):
                    self.information_tx = value
                    self.information_tx.value_namespace = name_space
                    self.information_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "local-error-frame-period-records"):
                    self.local_error_frame_period_records = value
                    self.local_error_frame_period_records.value_namespace = name_space
                    self.local_error_frame_period_records.value_namespace_prefix = name_space_prefix
                if(value_path == "local-error-frame-records"):
                    self.local_error_frame_records = value
                    self.local_error_frame_records.value_namespace = name_space
                    self.local_error_frame_records.value_namespace_prefix = name_space_prefix
                if(value_path == "local-error-frame-second-records"):
                    self.local_error_frame_second_records = value
                    self.local_error_frame_second_records.value_namespace = name_space
                    self.local_error_frame_second_records.value_namespace_prefix = name_space_prefix
                if(value_path == "local-error-symbol-period-records"):
                    self.local_error_symbol_period_records = value
                    self.local_error_symbol_period_records.value_namespace = name_space
                    self.local_error_symbol_period_records.value_namespace_prefix = name_space_prefix
                if(value_path == "loopback-control-rx"):
                    self.loopback_control_rx = value
                    self.loopback_control_rx.value_namespace = name_space
                    self.loopback_control_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "loopback-control-tx"):
                    self.loopback_control_tx = value
                    self.loopback_control_tx.value_namespace = name_space
                    self.loopback_control_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "org-specific-rx"):
                    self.org_specific_rx = value
                    self.org_specific_rx.value_namespace = name_space
                    self.org_specific_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "org-specific-tx"):
                    self.org_specific_tx = value
                    self.org_specific_tx.value_namespace = name_space
                    self.org_specific_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-error-frame-period-records"):
                    self.remote_error_frame_period_records = value
                    self.remote_error_frame_period_records.value_namespace = name_space
                    self.remote_error_frame_period_records.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-error-frame-records"):
                    self.remote_error_frame_records = value
                    self.remote_error_frame_records.value_namespace = name_space
                    self.remote_error_frame_records.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-error-frame-second-records"):
                    self.remote_error_frame_second_records = value
                    self.remote_error_frame_second_records.value_namespace = name_space
                    self.remote_error_frame_second_records.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-error-symbol-period-records"):
                    self.remote_error_symbol_period_records = value
                    self.remote_error_symbol_period_records.value_namespace = name_space
                    self.remote_error_symbol_period_records.value_namespace_prefix = name_space_prefix
                if(value_path == "unique-event-notification-rx"):
                    self.unique_event_notification_rx = value
                    self.unique_event_notification_rx.value_namespace = name_space
                    self.unique_event_notification_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "unique-event-notification-tx"):
                    self.unique_event_notification_tx = value
                    self.unique_event_notification_tx.value_namespace = name_space
                    self.unique_event_notification_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "unsupported-codes-rx"):
                    self.unsupported_codes_rx = value
                    self.unsupported_codes_rx.value_namespace = name_space
                    self.unsupported_codes_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "unsupported-codes-tx"):
                    self.unsupported_codes_tx = value
                    self.unsupported_codes_tx.value_namespace = name_space
                    self.unsupported_codes_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "variable-request-rx"):
                    self.variable_request_rx = value
                    self.variable_request_rx.value_namespace = name_space
                    self.variable_request_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "variable-request-tx"):
                    self.variable_request_tx = value
                    self.variable_request_tx.value_namespace = name_space
                    self.variable_request_tx.value_namespace_prefix = name_space_prefix
                if(value_path == "variable-response-rx"):
                    self.variable_response_rx = value
                    self.variable_response_rx.value_namespace = name_space
                    self.variable_response_rx.value_namespace_prefix = name_space_prefix
                if(value_path == "variable-response-tx"):
                    self.variable_response_tx = value
                    self.variable_response_tx.value_namespace = name_space
                    self.variable_response_tx.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stats_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stats_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "stats-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stats-interface"):
                for c in self.stats_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherLinkOam.StatsInterfaces.StatsInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stats_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stats-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.discovery_info_interfaces is not None and self.discovery_info_interfaces.has_data()) or
            (self.event_log_entry_interfaces is not None and self.event_log_entry_interfaces.has_data()) or
            (self.interface_state_interfaces is not None and self.interface_state_interfaces.has_data()) or
            (self.nodes is not None and self.nodes.has_data()) or
            (self.running_config_interfaces is not None and self.running_config_interfaces.has_data()) or
            (self.stats_interfaces is not None and self.stats_interfaces.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.discovery_info_interfaces is not None and self.discovery_info_interfaces.has_operation()) or
            (self.event_log_entry_interfaces is not None and self.event_log_entry_interfaces.has_operation()) or
            (self.interface_state_interfaces is not None and self.interface_state_interfaces.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()) or
            (self.running_config_interfaces is not None and self.running_config_interfaces.has_operation()) or
            (self.stats_interfaces is not None and self.stats_interfaces.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "discovery-info-interfaces"):
            if (self.discovery_info_interfaces is None):
                self.discovery_info_interfaces = EtherLinkOam.DiscoveryInfoInterfaces()
                self.discovery_info_interfaces.parent = self
                self._children_name_map["discovery_info_interfaces"] = "discovery-info-interfaces"
            return self.discovery_info_interfaces

        if (child_yang_name == "event-log-entry-interfaces"):
            if (self.event_log_entry_interfaces is None):
                self.event_log_entry_interfaces = EtherLinkOam.EventLogEntryInterfaces()
                self.event_log_entry_interfaces.parent = self
                self._children_name_map["event_log_entry_interfaces"] = "event-log-entry-interfaces"
            return self.event_log_entry_interfaces

        if (child_yang_name == "interface-state-interfaces"):
            if (self.interface_state_interfaces is None):
                self.interface_state_interfaces = EtherLinkOam.InterfaceStateInterfaces()
                self.interface_state_interfaces.parent = self
                self._children_name_map["interface_state_interfaces"] = "interface-state-interfaces"
            return self.interface_state_interfaces

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = EtherLinkOam.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        if (child_yang_name == "running-config-interfaces"):
            if (self.running_config_interfaces is None):
                self.running_config_interfaces = EtherLinkOam.RunningConfigInterfaces()
                self.running_config_interfaces.parent = self
                self._children_name_map["running_config_interfaces"] = "running-config-interfaces"
            return self.running_config_interfaces

        if (child_yang_name == "stats-interfaces"):
            if (self.stats_interfaces is None):
                self.stats_interfaces = EtherLinkOam.StatsInterfaces()
                self.stats_interfaces.parent = self
                self._children_name_map["stats_interfaces"] = "stats-interfaces"
            return self.stats_interfaces

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "discovery-info-interfaces" or name == "event-log-entry-interfaces" or name == "interface-state-interfaces" or name == "nodes" or name == "running-config-interfaces" or name == "stats-interfaces"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EtherLinkOam()
        return self._top_entity


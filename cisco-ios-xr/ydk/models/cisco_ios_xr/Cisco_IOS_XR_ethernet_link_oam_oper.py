""" Cisco_IOS_XR_ethernet_link_oam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package operational data.

This module contains definitions
for the following management objects\:
  ether\-link\-oam\: Ethernet Link OAM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ActionEnum(Enum):
    """
    ActionEnum

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

    no_action = 1

    disable_interface = 2

    log = 3

    efd = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['ActionEnum']


class LogEnum(Enum):
    """
    LogEnum

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

    log_type_symbol_event = 1

    log_type_period_event = 2

    log_type_frame_event = 3

    log_type_secs_event = 4

    log_type_link_fault = 256

    log_type_dying_gasp = 257

    log_type_critical_event = 258


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['LogEnum']


class LogLocationEnum(Enum):
    """
    LogLocationEnum

    The location of the event that caused a log entry

    .. data:: log_location_local = 1

    	A local event

    .. data:: log_location_remote = 2

    	A remote event

    """

    log_location_local = 1

    log_location_remote = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['LogLocationEnum']


class LoopbackStatusEnum(Enum):
    """
    LoopbackStatusEnum

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

    none = 1

    initiating = 2

    master_loopback = 3

    terminating = 4

    local_loopback = 5

    unknown = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['LoopbackStatusEnum']


class ModeEnum(Enum):
    """
    ModeEnum

    Mode of an OAM interface

    .. data:: passive = 0

    	Passive mode

    .. data:: active = 1

    	Active mode

    .. data:: dont_care = 2

    	Don't care what the mode is

    """

    passive = 0

    active = 1

    dont_care = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['ModeEnum']


class OperationalStateEnum(Enum):
    """
    OperationalStateEnum

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

    disabled = 1

    link_fault = 2

    passive_wait = 3

    active_send_local = 4

    send_local_and_remote = 5

    send_local_and_remote_ok = 6

    peering_locally_rejected = 7

    peering_remotely_rejected = 8

    operational = 9

    operational_half_duplex = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['OperationalStateEnum']


class ProtocolStateEnum(Enum):
    """
    ProtocolStateEnum

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

    protocol_state_inactive = 0

    protocol_state_fault = 1

    protocol_state_active_send_local = 2

    protocol_state_passive_wait = 3

    protocol_state_send_local_remote = 4

    protocol_state_send_local_remote_ok = 5

    protocol_state_send_any = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['ProtocolStateEnum']



class EtherLinkOam(object):
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
        self.discovery_info_interfaces = EtherLinkOam.DiscoveryInfoInterfaces()
        self.discovery_info_interfaces.parent = self
        self.event_log_entry_interfaces = EtherLinkOam.EventLogEntryInterfaces()
        self.event_log_entry_interfaces.parent = self
        self.interface_state_interfaces = EtherLinkOam.InterfaceStateInterfaces()
        self.interface_state_interfaces.parent = self
        self.nodes = EtherLinkOam.Nodes()
        self.nodes.parent = self
        self.running_config_interfaces = EtherLinkOam.RunningConfigInterfaces()
        self.running_config_interfaces.parent = self
        self.stats_interfaces = EtherLinkOam.StatsInterfaces()
        self.stats_interfaces.parent = self


    class DiscoveryInfoInterfaces(object):
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
            self.parent = None
            self.discovery_info_interface = YList()
            self.discovery_info_interface.parent = self
            self.discovery_info_interface.name = 'discovery_info_interface'


        class DiscoveryInfoInterface(object):
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
            	**type**\:   :py:class:`ModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ModeEnum>`
            
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
            	**type**\:   :py:class:`LoopbackStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.LoopbackStatusEnum>`
            
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
            	**type**\:   :py:class:`OperationalStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.OperationalStateEnum>`
            
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
            	**type**\:   :py:class:`ModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ModeEnum>`
            
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
                self.parent = None
                self.member_interface = None
                self.local_evaluating = None
                self.local_function_event = None
                self.local_function_event_valid = None
                self.local_function_loopback = None
                self.local_function_loopback_valid = None
                self.local_function_unidirectional = None
                self.local_function_unidirectional_valid = None
                self.local_functionvariable = None
                self.local_functionvariable_valid = None
                self.local_mode = None
                self.local_mode_valid = None
                self.local_mtu = None
                self.local_mtu_valid = None
                self.local_mwd_key = None
                self.local_mwd_key_valid = None
                self.local_operational = None
                self.local_revision = None
                self.local_revisionvalid = None
                self.loopback_mode = None
                self.loopback_mode_valid = None
                self.miswired = None
                self.miswired_valid = None
                self.name = None
                self.operational_status = None
                self.operational_status_valid = None
                self.received_at_risk_notification_time_remaining = None
                self.received_at_risk_notification_timestamp = None
                self.remote_event = None
                self.remote_event_valid = None
                self.remote_loopback = None
                self.remote_loopback_valid = None
                self.remote_mac_address = None
                self.remote_mac_address_valid = None
                self.remote_mode = None
                self.remote_mode_valid = None
                self.remote_mtu = None
                self.remote_mtu_valid = None
                self.remote_mwd_key = None
                self.remote_mwd_key_valid = None
                self.remote_revision = None
                self.remote_revisionvalid = None
                self.remote_unidirectional = None
                self.remote_unidirectional_valid = None
                self.remote_variable = None
                self.remote_variable_valid = None
                self.remote_vendor_info = None
                self.remote_vendor_info_valid = None
                self.remote_vendor_oui = None
                self.remote_vendor_oui_valid = None

            @property
            def _common_path(self):
                if self.member_interface is None:
                    raise YPYModelError('Key property member_interface is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:discovery-info-interfaces/Cisco-IOS-XR-ethernet-link-oam-oper:discovery-info-interface[Cisco-IOS-XR-ethernet-link-oam-oper:member-interface = ' + str(self.member_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_interface is not None:
                    return True

                if self.local_evaluating is not None:
                    return True

                if self.local_function_event is not None:
                    return True

                if self.local_function_event_valid is not None:
                    return True

                if self.local_function_loopback is not None:
                    return True

                if self.local_function_loopback_valid is not None:
                    return True

                if self.local_function_unidirectional is not None:
                    return True

                if self.local_function_unidirectional_valid is not None:
                    return True

                if self.local_functionvariable is not None:
                    return True

                if self.local_functionvariable_valid is not None:
                    return True

                if self.local_mode is not None:
                    return True

                if self.local_mode_valid is not None:
                    return True

                if self.local_mtu is not None:
                    return True

                if self.local_mtu_valid is not None:
                    return True

                if self.local_mwd_key is not None:
                    return True

                if self.local_mwd_key_valid is not None:
                    return True

                if self.local_operational is not None:
                    return True

                if self.local_revision is not None:
                    return True

                if self.local_revisionvalid is not None:
                    return True

                if self.loopback_mode is not None:
                    return True

                if self.loopback_mode_valid is not None:
                    return True

                if self.miswired is not None:
                    return True

                if self.miswired_valid is not None:
                    return True

                if self.name is not None:
                    return True

                if self.operational_status is not None:
                    return True

                if self.operational_status_valid is not None:
                    return True

                if self.received_at_risk_notification_time_remaining is not None:
                    return True

                if self.received_at_risk_notification_timestamp is not None:
                    return True

                if self.remote_event is not None:
                    return True

                if self.remote_event_valid is not None:
                    return True

                if self.remote_loopback is not None:
                    return True

                if self.remote_loopback_valid is not None:
                    return True

                if self.remote_mac_address is not None:
                    return True

                if self.remote_mac_address_valid is not None:
                    return True

                if self.remote_mode is not None:
                    return True

                if self.remote_mode_valid is not None:
                    return True

                if self.remote_mtu is not None:
                    return True

                if self.remote_mtu_valid is not None:
                    return True

                if self.remote_mwd_key is not None:
                    return True

                if self.remote_mwd_key_valid is not None:
                    return True

                if self.remote_revision is not None:
                    return True

                if self.remote_revisionvalid is not None:
                    return True

                if self.remote_unidirectional is not None:
                    return True

                if self.remote_unidirectional_valid is not None:
                    return True

                if self.remote_variable is not None:
                    return True

                if self.remote_variable_valid is not None:
                    return True

                if self.remote_vendor_info is not None:
                    return True

                if self.remote_vendor_info_valid is not None:
                    return True

                if self.remote_vendor_oui is not None:
                    return True

                if self.remote_vendor_oui_valid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:discovery-info-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.discovery_info_interface is not None:
                for child_ref in self.discovery_info_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.DiscoveryInfoInterfaces']['meta_info']


    class InterfaceStateInterfaces(object):
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
            self.parent = None
            self.interface_state_interface = YList()
            self.interface_state_interface.parent = self
            self.interface_state_interface.name = 'interface_state_interface'


        class InterfaceStateInterface(object):
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
            	**type**\:   :py:class:`ProtocolStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ProtocolStateEnum>`
            
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
                self.parent = None
                self.member_interface = None
                self.efd_triggers = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers()
                self.efd_triggers.parent = self
                self.errors = EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors()
                self.errors.parent = self
                self.local_mwd_key = None
                self.protocol_code = None
                self.remote_mwd_key = None
                self.remote_mwd_key_present = None
                self.rx_fault = None


            class Errors(object):
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
                    self.parent = None
                    self.caps_add_error_code = None
                    self.caps_add_reason = None
                    self.epi_error_code = None
                    self.epi_reason = None
                    self.pfi_error_code = None
                    self.pfi_reason = None
                    self.platform_error_code = None
                    self.platform_reason = None
                    self.spio_error_code = None
                    self.spio_reason = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-oper:errors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.caps_add_error_code is not None:
                        return True

                    if self.caps_add_reason is not None:
                        return True

                    if self.epi_error_code is not None:
                        return True

                    if self.epi_reason is not None:
                        return True

                    if self.pfi_error_code is not None:
                        return True

                    if self.pfi_reason is not None:
                        return True

                    if self.platform_error_code is not None:
                        return True

                    if self.platform_reason is not None:
                        return True

                    if self.spio_error_code is not None:
                        return True

                    if self.spio_reason is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                    return meta._meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors']['meta_info']


            class EfdTriggers(object):
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
                    self.parent = None
                    self.capabilities_conflict = None
                    self.discovery_timed_out = None
                    self.link_fault_received = None
                    self.session_down = None
                    self.wiring_conflict = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-oper:efd-triggers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.capabilities_conflict is not None:
                        return True

                    if self.discovery_timed_out is not None:
                        return True

                    if self.link_fault_received is not None:
                        return True

                    if self.session_down is not None:
                        return True

                    if self.wiring_conflict is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                    return meta._meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers']['meta_info']

            @property
            def _common_path(self):
                if self.member_interface is None:
                    raise YPYModelError('Key property member_interface is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:interface-state-interfaces/Cisco-IOS-XR-ethernet-link-oam-oper:interface-state-interface[Cisco-IOS-XR-ethernet-link-oam-oper:member-interface = ' + str(self.member_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_interface is not None:
                    return True

                if self.efd_triggers is not None and self.efd_triggers._has_data():
                    return True

                if self.errors is not None and self.errors._has_data():
                    return True

                if self.local_mwd_key is not None:
                    return True

                if self.protocol_code is not None:
                    return True

                if self.remote_mwd_key is not None:
                    return True

                if self.remote_mwd_key_present is not None:
                    return True

                if self.rx_fault is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:interface-state-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_state_interface is not None:
                for child_ref in self.interface_state_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.InterfaceStateInterfaces']['meta_info']


    class RunningConfigInterfaces(object):
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
            self.parent = None
            self.running_config_interface = YList()
            self.running_config_interface.parent = self
            self.running_config_interface.name = 'running_config_interface'


        class RunningConfigInterface(object):
            """
            Ethernet Link OAM interface to get Running
            Config for
            
            .. attribute:: member_interface  <key>
            
            	Member Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: capabilities_conflict_action
            
            	Action to perform when a capabilities conflict occurs
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
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
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
            .. attribute:: critical_event_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: discovery_timeout_action
            
            	Action to perform when a discovery timeout occurs
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
            .. attribute:: discovery_timeout_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: dying_gasp_action
            
            	Action to perform when a dying gasp occurs
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
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
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
            .. attribute:: high_threshold_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: link_fault_action
            
            	Action to perform when a link fault occurs
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
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
            	**type**\:   :py:class:`ModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ModeEnum>`
            
            .. attribute:: mode_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: remote_loopback_action
            
            	Action to perform when a session enters or exits remote loopback
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
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
            	**type**\:   :py:class:`ModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ModeEnum>`
            
            .. attribute:: session_down_action
            
            	Action to perform when a session comes down
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
            .. attribute:: session_down_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            .. attribute:: session_up_action
            
            	Action to perform when a session comes up
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
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
            	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
            
            .. attribute:: wiring_conflict_action_overridden
            
            	Is this configuration information an interface override?
            	**type**\:  bool
            
            

            """

            _prefix = 'ethernet-link-oam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.member_interface = None
                self.capabilities_conflict_action = None
                self.capabilities_conflict_action_overridden = None
                self.connection_timeout = None
                self.connection_timeout_overridden = None
                self.critical_event_action = None
                self.critical_event_action_overridden = None
                self.discovery_timeout_action = None
                self.discovery_timeout_action_overridden = None
                self.dying_gasp_action = None
                self.dying_gasp_action_overridden = None
                self.fast_hello_interval_enabled = None
                self.fast_hello_interval_enabled_overridden = None
                self.frame_period_threshold_high = None
                self.frame_period_threshold_high_multiplier = None
                self.frame_period_threshold_high_overridden = None
                self.frame_period_threshold_low = None
                self.frame_period_threshold_low_multiplier = None
                self.frame_period_threshold_low_overridden = None
                self.frame_period_threshold_units = None
                self.frame_period_window = None
                self.frame_period_window_multiplier = None
                self.frame_period_window_overridden = None
                self.frame_period_window_units = None
                self.frame_seconds_threshold_high = None
                self.frame_seconds_threshold_high_overridden = None
                self.frame_seconds_threshold_low = None
                self.frame_seconds_threshold_low_overridden = None
                self.frame_seconds_window = None
                self.frame_seconds_window_overridden = None
                self.frame_threshold_high = None
                self.frame_threshold_high_multiplier = None
                self.frame_threshold_high_overridden = None
                self.frame_threshold_low = None
                self.frame_threshold_low_multiplier = None
                self.frame_threshold_low_overridden = None
                self.frame_window = None
                self.frame_window_overridden = None
                self.high_threshold_action = None
                self.high_threshold_action_overridden = None
                self.link_fault_action = None
                self.link_fault_action_overridden = None
                self.link_monitor_enabled = None
                self.link_monitoring_enabled_overridden = None
                self.mib_retrieval_enabled = None
                self.mib_retrieval_enabled_overridden = None
                self.mode = None
                self.mode_overridden = None
                self.remote_loopback_action = None
                self.remote_loopback_action_overridden = None
                self.remote_loopback_enabled = None
                self.remote_loopback_enabled_overridden = None
                self.require_link_monitoring = None
                self.require_link_monitoring_overridden = None
                self.require_loopback = None
                self.require_loopback_overridden = None
                self.require_mib_retrieval_overridden = None
                self.require_mode_overridden = None
                self.require_remote_mib_retrieval = None
                self.require_remote_mode = None
                self.session_down_action = None
                self.session_down_action_overridden = None
                self.session_up_action = None
                self.session_up_action_overridden = None
                self.symbol_period_threshold_high = None
                self.symbol_period_threshold_high_multiplier = None
                self.symbol_period_threshold_high_overridden = None
                self.symbol_period_threshold_low = None
                self.symbol_period_threshold_low_multiplier = None
                self.symbol_period_threshold_low_overridden = None
                self.symbol_period_threshold_units = None
                self.symbol_period_window = None
                self.symbol_period_window_multiplier = None
                self.symbol_period_window_overridden = None
                self.symbol_period_window_units = None
                self.udlf_enabled = None
                self.udlf_enabled_overridden = None
                self.wiring_conflict_action = None
                self.wiring_conflict_action_overridden = None

            @property
            def _common_path(self):
                if self.member_interface is None:
                    raise YPYModelError('Key property member_interface is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:running-config-interfaces/Cisco-IOS-XR-ethernet-link-oam-oper:running-config-interface[Cisco-IOS-XR-ethernet-link-oam-oper:member-interface = ' + str(self.member_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_interface is not None:
                    return True

                if self.capabilities_conflict_action is not None:
                    return True

                if self.capabilities_conflict_action_overridden is not None:
                    return True

                if self.connection_timeout is not None:
                    return True

                if self.connection_timeout_overridden is not None:
                    return True

                if self.critical_event_action is not None:
                    return True

                if self.critical_event_action_overridden is not None:
                    return True

                if self.discovery_timeout_action is not None:
                    return True

                if self.discovery_timeout_action_overridden is not None:
                    return True

                if self.dying_gasp_action is not None:
                    return True

                if self.dying_gasp_action_overridden is not None:
                    return True

                if self.fast_hello_interval_enabled is not None:
                    return True

                if self.fast_hello_interval_enabled_overridden is not None:
                    return True

                if self.frame_period_threshold_high is not None:
                    return True

                if self.frame_period_threshold_high_multiplier is not None:
                    return True

                if self.frame_period_threshold_high_overridden is not None:
                    return True

                if self.frame_period_threshold_low is not None:
                    return True

                if self.frame_period_threshold_low_multiplier is not None:
                    return True

                if self.frame_period_threshold_low_overridden is not None:
                    return True

                if self.frame_period_threshold_units is not None:
                    return True

                if self.frame_period_window is not None:
                    return True

                if self.frame_period_window_multiplier is not None:
                    return True

                if self.frame_period_window_overridden is not None:
                    return True

                if self.frame_period_window_units is not None:
                    return True

                if self.frame_seconds_threshold_high is not None:
                    return True

                if self.frame_seconds_threshold_high_overridden is not None:
                    return True

                if self.frame_seconds_threshold_low is not None:
                    return True

                if self.frame_seconds_threshold_low_overridden is not None:
                    return True

                if self.frame_seconds_window is not None:
                    return True

                if self.frame_seconds_window_overridden is not None:
                    return True

                if self.frame_threshold_high is not None:
                    return True

                if self.frame_threshold_high_multiplier is not None:
                    return True

                if self.frame_threshold_high_overridden is not None:
                    return True

                if self.frame_threshold_low is not None:
                    return True

                if self.frame_threshold_low_multiplier is not None:
                    return True

                if self.frame_threshold_low_overridden is not None:
                    return True

                if self.frame_window is not None:
                    return True

                if self.frame_window_overridden is not None:
                    return True

                if self.high_threshold_action is not None:
                    return True

                if self.high_threshold_action_overridden is not None:
                    return True

                if self.link_fault_action is not None:
                    return True

                if self.link_fault_action_overridden is not None:
                    return True

                if self.link_monitor_enabled is not None:
                    return True

                if self.link_monitoring_enabled_overridden is not None:
                    return True

                if self.mib_retrieval_enabled is not None:
                    return True

                if self.mib_retrieval_enabled_overridden is not None:
                    return True

                if self.mode is not None:
                    return True

                if self.mode_overridden is not None:
                    return True

                if self.remote_loopback_action is not None:
                    return True

                if self.remote_loopback_action_overridden is not None:
                    return True

                if self.remote_loopback_enabled is not None:
                    return True

                if self.remote_loopback_enabled_overridden is not None:
                    return True

                if self.require_link_monitoring is not None:
                    return True

                if self.require_link_monitoring_overridden is not None:
                    return True

                if self.require_loopback is not None:
                    return True

                if self.require_loopback_overridden is not None:
                    return True

                if self.require_mib_retrieval_overridden is not None:
                    return True

                if self.require_mode_overridden is not None:
                    return True

                if self.require_remote_mib_retrieval is not None:
                    return True

                if self.require_remote_mode is not None:
                    return True

                if self.session_down_action is not None:
                    return True

                if self.session_down_action_overridden is not None:
                    return True

                if self.session_up_action is not None:
                    return True

                if self.session_up_action_overridden is not None:
                    return True

                if self.symbol_period_threshold_high is not None:
                    return True

                if self.symbol_period_threshold_high_multiplier is not None:
                    return True

                if self.symbol_period_threshold_high_overridden is not None:
                    return True

                if self.symbol_period_threshold_low is not None:
                    return True

                if self.symbol_period_threshold_low_multiplier is not None:
                    return True

                if self.symbol_period_threshold_low_overridden is not None:
                    return True

                if self.symbol_period_threshold_units is not None:
                    return True

                if self.symbol_period_window is not None:
                    return True

                if self.symbol_period_window_multiplier is not None:
                    return True

                if self.symbol_period_window_overridden is not None:
                    return True

                if self.symbol_period_window_units is not None:
                    return True

                if self.udlf_enabled is not None:
                    return True

                if self.udlf_enabled_overridden is not None:
                    return True

                if self.wiring_conflict_action is not None:
                    return True

                if self.wiring_conflict_action_overridden is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:running-config-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.running_config_interface is not None:
                for child_ref in self.running_config_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.RunningConfigInterfaces']['meta_info']


    class Nodes(object):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.EtherLinkOam.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-link-oam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.summary = EtherLinkOam.Nodes.Node.Summary()
                self.summary.parent = self


            class Summary(object):
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
                    self.parent = None
                    self.active_send = None
                    self.evaluating = None
                    self.events = None
                    self.interfaces = None
                    self.local_accept = None
                    self.local_events = None
                    self.local_frame = None
                    self.local_frame_period = None
                    self.local_frame_seconds = None
                    self.local_reject = None
                    self.local_symbol_period = None
                    self.loopback_mode = None
                    self.miswired_connections = None
                    self.operational = None
                    self.passive_wait = None
                    self.port_down = None
                    self.remote_events = None
                    self.remote_frame = None
                    self.remote_frame_period = None
                    self.remote_frame_seconds = None
                    self.remote_reject = None
                    self.remote_symbol_period = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active_send is not None:
                        return True

                    if self.evaluating is not None:
                        return True

                    if self.events is not None:
                        return True

                    if self.interfaces is not None:
                        return True

                    if self.local_accept is not None:
                        return True

                    if self.local_events is not None:
                        return True

                    if self.local_frame is not None:
                        return True

                    if self.local_frame_period is not None:
                        return True

                    if self.local_frame_seconds is not None:
                        return True

                    if self.local_reject is not None:
                        return True

                    if self.local_symbol_period is not None:
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.miswired_connections is not None:
                        return True

                    if self.operational is not None:
                        return True

                    if self.passive_wait is not None:
                        return True

                    if self.port_down is not None:
                        return True

                    if self.remote_events is not None:
                        return True

                    if self.remote_frame is not None:
                        return True

                    if self.remote_frame_period is not None:
                        return True

                    if self.remote_frame_seconds is not None:
                        return True

                    if self.remote_reject is not None:
                        return True

                    if self.remote_symbol_period is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                    return meta._meta_table['EtherLinkOam.Nodes.Node.Summary']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:nodes/Cisco-IOS-XR-ethernet-link-oam-oper:node[Cisco-IOS-XR-ethernet-link-oam-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.Nodes']['meta_info']


    class EventLogEntryInterfaces(object):
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
            self.parent = None
            self.event_log_entry_interface = YList()
            self.event_log_entry_interface.parent = self
            self.event_log_entry_interface.name = 'event_log_entry_interface'


        class EventLogEntryInterface(object):
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
                self.parent = None
                self.member_interface = None
                self.event_log_entry_indexes = EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes()
                self.event_log_entry_indexes.parent = self


            class EventLogEntryIndexes(object):
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
                    self.parent = None
                    self.event_log_entry_index = YList()
                    self.event_log_entry_index.parent = self
                    self.event_log_entry_index.name = 'event_log_entry_index'


                class EventLogEntryIndex(object):
                    """
                    Ethernet Link OAM Event Log Entry Index to
                    get data for
                    
                    .. attribute:: event_log_entry_index  <key>
                    
                    	Event Log Entry index
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: action_taken
                    
                    	Local action taken (If applicable)
                    	**type**\:   :py:class:`ActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.ActionEnum>`
                    
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
                    	**type**\:   :py:class:`LogLocationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.LogLocationEnum>`
                    
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
                    	**type**\:   :py:class:`LogEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_oper.LogEnum>`
                    
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
                        self.parent = None
                        self.event_log_entry_index = None
                        self.action_taken = None
                        self.event_total = None
                        self.handle = None
                        self.index = None
                        self.local_high_threshold = None
                        self.local_high_threshold_config_units = None
                        self.location = None
                        self.oui = None
                        self.running_total = None
                        self.threshold = None
                        self.threshold_config_units = None
                        self.threshold_units = None
                        self.timestamp = None
                        self.type = None
                        self.value = None
                        self.value_config_units = None
                        self.window = None
                        self.window_config_units = None
                        self.window_units = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.event_log_entry_index is None:
                            raise YPYModelError('Key property event_log_entry_index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-index[Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-index = ' + str(self.event_log_entry_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.event_log_entry_index is not None:
                            return True

                        if self.action_taken is not None:
                            return True

                        if self.event_total is not None:
                            return True

                        if self.handle is not None:
                            return True

                        if self.index is not None:
                            return True

                        if self.local_high_threshold is not None:
                            return True

                        if self.local_high_threshold_config_units is not None:
                            return True

                        if self.location is not None:
                            return True

                        if self.oui is not None:
                            return True

                        if self.running_total is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        if self.threshold_config_units is not None:
                            return True

                        if self.threshold_units is not None:
                            return True

                        if self.timestamp is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.value is not None:
                            return True

                        if self.value_config_units is not None:
                            return True

                        if self.window is not None:
                            return True

                        if self.window_config_units is not None:
                            return True

                        if self.window_units is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                        return meta._meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-indexes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.event_log_entry_index is not None:
                        for child_ref in self.event_log_entry_index:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                    return meta._meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes']['meta_info']

            @property
            def _common_path(self):
                if self.member_interface is None:
                    raise YPYModelError('Key property member_interface is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-interfaces/Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-interface[Cisco-IOS-XR-ethernet-link-oam-oper:member-interface = ' + str(self.member_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_interface is not None:
                    return True

                if self.event_log_entry_indexes is not None and self.event_log_entry_indexes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:event-log-entry-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.event_log_entry_interface is not None:
                for child_ref in self.event_log_entry_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.EventLogEntryInterfaces']['meta_info']


    class StatsInterfaces(object):
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
            self.parent = None
            self.stats_interface = YList()
            self.stats_interface.parent = self
            self.stats_interface.name = 'stats_interface'


        class StatsInterface(object):
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
                self.parent = None
                self.member_interface = None
                self.duplicate_event_notification_rx = None
                self.duplicate_event_notification_tx = None
                self.fixed_frames_rx = None
                self.frames_lost_due_to_oam = None
                self.information_rx = None
                self.information_tx = None
                self.local_error_frame_period_records = None
                self.local_error_frame_records = None
                self.local_error_frame_second_records = None
                self.local_error_symbol_period_records = None
                self.loopback_control_rx = None
                self.loopback_control_tx = None
                self.org_specific_rx = None
                self.org_specific_tx = None
                self.remote_error_frame_period_records = None
                self.remote_error_frame_records = None
                self.remote_error_frame_second_records = None
                self.remote_error_symbol_period_records = None
                self.unique_event_notification_rx = None
                self.unique_event_notification_tx = None
                self.unsupported_codes_rx = None
                self.unsupported_codes_tx = None
                self.variable_request_rx = None
                self.variable_request_tx = None
                self.variable_response_rx = None
                self.variable_response_tx = None

            @property
            def _common_path(self):
                if self.member_interface is None:
                    raise YPYModelError('Key property member_interface is None')

                return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:stats-interfaces/Cisco-IOS-XR-ethernet-link-oam-oper:stats-interface[Cisco-IOS-XR-ethernet-link-oam-oper:member-interface = ' + str(self.member_interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.member_interface is not None:
                    return True

                if self.duplicate_event_notification_rx is not None:
                    return True

                if self.duplicate_event_notification_tx is not None:
                    return True

                if self.fixed_frames_rx is not None:
                    return True

                if self.frames_lost_due_to_oam is not None:
                    return True

                if self.information_rx is not None:
                    return True

                if self.information_tx is not None:
                    return True

                if self.local_error_frame_period_records is not None:
                    return True

                if self.local_error_frame_records is not None:
                    return True

                if self.local_error_frame_second_records is not None:
                    return True

                if self.local_error_symbol_period_records is not None:
                    return True

                if self.loopback_control_rx is not None:
                    return True

                if self.loopback_control_tx is not None:
                    return True

                if self.org_specific_rx is not None:
                    return True

                if self.org_specific_tx is not None:
                    return True

                if self.remote_error_frame_period_records is not None:
                    return True

                if self.remote_error_frame_records is not None:
                    return True

                if self.remote_error_frame_second_records is not None:
                    return True

                if self.remote_error_symbol_period_records is not None:
                    return True

                if self.unique_event_notification_rx is not None:
                    return True

                if self.unique_event_notification_tx is not None:
                    return True

                if self.unsupported_codes_rx is not None:
                    return True

                if self.unsupported_codes_tx is not None:
                    return True

                if self.variable_request_rx is not None:
                    return True

                if self.variable_request_tx is not None:
                    return True

                if self.variable_response_rx is not None:
                    return True

                if self.variable_response_tx is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
                return meta._meta_table['EtherLinkOam.StatsInterfaces.StatsInterface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam/Cisco-IOS-XR-ethernet-link-oam-oper:stats-interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.stats_interface is not None:
                for child_ref in self.stats_interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
            return meta._meta_table['EtherLinkOam.StatsInterfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ethernet-link-oam-oper:ether-link-oam'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.discovery_info_interfaces is not None and self.discovery_info_interfaces._has_data():
            return True

        if self.event_log_entry_interfaces is not None and self.event_log_entry_interfaces._has_data():
            return True

        if self.interface_state_interfaces is not None and self.interface_state_interfaces._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.running_config_interfaces is not None and self.running_config_interfaces._has_data():
            return True

        if self.stats_interfaces is not None and self.stats_interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_oper as meta
        return meta._meta_table['EtherLinkOam']['meta_info']



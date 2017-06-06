""" Cisco_IOS_XR_ethernet_cfm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package operational data.

This module contains definitions
for the following management objects\:
  cfm\: CFM operational data

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-sla\-oper
module with state data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CfmAisDirEnum(Enum):
    """
    CfmAisDirEnum

    Cfm ais dir

    .. data:: up = 0

    	Packets sent inward

    .. data:: down = 1

    	Packets sent outward

    """

    up = 0

    down = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmAisDirEnum']


class CfmBagAisIntervalEnum(Enum):
    """
    CfmBagAisIntervalEnum

    CFM AIS intervals

    .. data:: ais_interval_none = 0

    	Invalid AIS interval

    .. data:: ais_interval1s = 4

    	Interval of 1s

    .. data:: ais_interval1m = 6

    	Interval of 1 min

    """

    ais_interval_none = 0

    ais_interval1s = 4

    ais_interval1m = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagAisIntervalEnum']


class CfmBagBdidFmtEnum(Enum):
    """
    CfmBagBdidFmtEnum

    Bridge domain identifier format

    .. data:: invalid = 0

    	Invalid BDID identifier format

    .. data:: bd_id = 1

    	Identifier is a bridge domain ID

    .. data:: xc_p2p_id = 2

    	Identifier is a P2P cross-connect ID

    .. data:: xc_mp2mp_id = 3

    	Identifier is a MP2MP cross-connect ID

    .. data:: down_only = 4

    	Identifier is a maintenance association name

    """

    invalid = 0

    bd_id = 1

    xc_p2p_id = 2

    xc_mp2mp_id = 3

    down_only = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagBdidFmtEnum']


class CfmBagCcmIntervalEnum(Enum):
    """
    CfmBagCcmIntervalEnum

    CFM CCM intervals

    .. data:: interval_none = 0

    	Invalid CCM interval

    .. data:: interval3_3ms = 1

    	Interval of 3.3ms

    .. data:: interval10ms = 2

    	Interval of 10ms

    .. data:: interval100ms = 3

    	Interval of 100ms

    .. data:: interval1s = 4

    	Interval of 1s

    .. data:: interval10s = 5

    	Interval of 10s

    .. data:: interval1m = 6

    	Interval of 1 min

    .. data:: interval10m = 7

    	Interval of 10 mins

    """

    interval_none = 0

    interval3_3ms = 1

    interval10ms = 2

    interval100ms = 3

    interval1s = 4

    interval10s = 5

    interval1m = 6

    interval10m = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagCcmIntervalEnum']


class CfmBagCcmOffloadEnum(Enum):
    """
    CfmBagCcmOffloadEnum

    Offload status of CCM processing

    .. data:: offload_none = 0

    	CCM processing has not been offloaded

    .. data:: offload_software = 1

    	CCM processing has been offloaded to software

    .. data:: offload_hardware = 2

    	CCM processing has been offloaded to hardware

    """

    offload_none = 0

    offload_software = 1

    offload_hardware = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagCcmOffloadEnum']


class CfmBagDirectionEnum(Enum):
    """
    CfmBagDirectionEnum

    MEP direction

    .. data:: direction_up = 0

    	Up

    .. data:: direction_down = 1

    	Down

    .. data:: direction_invalid = 2

    	Invalid direction

    """

    direction_up = 0

    direction_down = 1

    direction_invalid = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagDirectionEnum']


class CfmBagIssuRoleEnum(Enum):
    """
    CfmBagIssuRoleEnum

    CFM ISSU role

    .. data:: unknown = 0

    	Unknown

    .. data:: primary = 1

    	Primary

    .. data:: secondary = 2

    	Secondary

    """

    unknown = 0

    primary = 1

    secondary = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagIssuRoleEnum']


class CfmBagIwStateEnum(Enum):
    """
    CfmBagIwStateEnum

    CFM Interworking state

    .. data:: interworking_up = 0

    	Interface is UP

    .. data:: interworking_test = 1

    	Interface is in TEST mode

    """

    interworking_up = 0

    interworking_test = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagIwStateEnum']


class CfmBagMdLevelEnum(Enum):
    """
    CfmBagMdLevelEnum

    CFM level

    .. data:: level0 = 0

    	CFM level 0

    .. data:: level1 = 1

    	CFM level 1

    .. data:: level2 = 2

    	CFM level 2

    .. data:: level3 = 3

    	CFM level 3

    .. data:: level4 = 4

    	CFM level 4

    .. data:: level5 = 5

    	CFM level 5

    .. data:: level6 = 6

    	CFM level 6

    .. data:: level7 = 7

    	CFM level 7

    .. data:: level_invalid = 8

    	Invalid CFM level

    """

    level0 = 0

    level1 = 1

    level2 = 2

    level3 = 3

    level4 = 4

    level5 = 5

    level6 = 6

    level7 = 7

    level_invalid = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagMdLevelEnum']


class CfmBagMdidFmtEnum(Enum):
    """
    CfmBagMdidFmtEnum

    CFM MDID format

    .. data:: mdid_null = 1

    	MDID is explicity NULL

    .. data:: mdid_dns_like = 2

    	MDID is based on a DNS name

    .. data:: mdid_mac_address = 3

    	MDID is a (MAC address, integer) pair

    .. data:: mdid_string = 4

    	MDID is a character string

    .. data:: mdid_unknown = 5

    	Unknown MDID format

    """

    mdid_null = 1

    mdid_dns_like = 2

    mdid_mac_address = 3

    mdid_string = 4

    mdid_unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagMdidFmtEnum']


class CfmBagOpcodeEnum(Enum):
    """
    CfmBagOpcodeEnum

    CFM Opcode

    .. data:: reserved = 0

    	Reserved

    .. data:: ccm = 1

    	Continuity Check

    .. data:: lbr = 2

    	Loopback Reply

    .. data:: lbm = 3

    	Loopback Message

    .. data:: ltr = 4

    	Linktrace Reply

    .. data:: ltm = 5

    	Linktrace Message

    """

    reserved = 0

    ccm = 1

    lbr = 2

    lbm = 3

    ltr = 4

    ltm = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagOpcodeEnum']


class CfmBagSmanFmtEnum(Enum):
    """
    CfmBagSmanFmtEnum

    Short MA Name format

    .. data:: sman_vlan_id = 1

    	Short MA Name is a 12-bit VLAN-ID

    .. data:: sman_string = 2

    	Short MA Name is a character string

    .. data:: sman_uint16 = 3

    	Short MA Name is a 16-bit unsigned integer

    .. data:: sman_vpn_id = 4

    	Short MA Name is a global VPN identifier

    .. data:: sman_icc = 32

    	Short MA Name uses the ICC-based format

    .. data:: sman_unknown = 33

    	Unknown Short MA Name format

    """

    sman_vlan_id = 1

    sman_string = 2

    sman_uint16 = 3

    sman_vpn_id = 4

    sman_icc = 32

    sman_unknown = 33


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagSmanFmtEnum']


class CfmBagStpStateEnum(Enum):
    """
    CfmBagStpStateEnum

    CFM STP state

    .. data:: stp_up = 0

    	Interface is UP

    .. data:: stp_blocked = 1

    	Interface is STP-blocked

    .. data:: stp_unknown = 2

    	Unknown Interface STP state

    """

    stp_up = 0

    stp_blocked = 1

    stp_unknown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagStpStateEnum']


class CfmMaMpVarietyEnum(Enum):
    """
    CfmMaMpVarietyEnum

    CFM MA Maintenance Point varieties

    .. data:: mip = 0

    	MIP

    .. data:: up_mep = 1

    	Up MEP

    .. data:: downmep = 2

    	Down MEP

    .. data:: unknown_mep = 3

    	Unknown MEP

    """

    mip = 0

    up_mep = 1

    downmep = 2

    unknown_mep = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmMaMpVarietyEnum']


class CfmPmAddlIntfStatusEnum(Enum):
    """
    CfmPmAddlIntfStatusEnum

    Additional interface status

    .. data:: unknown = 0

    	Additional interface status unknown

    .. data:: administratively_down = 1

    	Interface is explicitly shutdown in

    	configuration

    .. data:: remote_excessive_errors = 2

    	Remote interface has exceeded its 802.3 Link

    	OAM error threshold

    .. data:: local_excessive_errors = 3

    	Local interface has exceeded its 802.3 Link OAM

    	error threshold

    """

    unknown = 0

    administratively_down = 1

    remote_excessive_errors = 2

    local_excessive_errors = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAddlIntfStatusEnum']


class CfmPmAisReceiveEnum(Enum):
    """
    CfmPmAisReceiveEnum

    Enumeration of how the MEP is receiving the

    signal, directly or via AIS or LCK messages.

    .. data:: receive_none = 0

    	No signal received

    .. data:: receive_ais = 1

    	Receiving AIS messages

    .. data:: receive_lck = 2

    	Receiving LCK messages

    .. data:: receive_direct = 3

    	Receiving AIS directly from another MEP on the

    	same interface

    """

    receive_none = 0

    receive_ais = 1

    receive_lck = 2

    receive_direct = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAisReceiveEnum']


class CfmPmAisTransmitEnum(Enum):
    """
    CfmPmAisTransmitEnum

    Enumeration of how the MEP is transmitting AIS,

    via a MIP or directly to a higher MEP

    .. data:: transmit_none = 0

    	AIS not transmitted

    .. data:: transmit_ais = 1

    	AIS transmitted via MIP

    .. data:: transmit_ais_direct = 2

    	AIS signal passed directly to a higher MEP

    """

    transmit_none = 0

    transmit_ais = 1

    transmit_ais_direct = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAisTransmitEnum']


class CfmPmChassisIdFmtEnum(Enum):
    """
    CfmPmChassisIdFmtEnum

    Chassis ID type

    .. data:: chassis_id_chassis_component = 1

    	Chassis ID is a component name

    .. data:: chassis_id_interface_alias = 2

    	Chassis ID is an interface alias

    .. data:: chassis_id_port_component = 3

    	Chassis ID is a port component name

    .. data:: chassis_id_mac_address = 4

    	Chassis ID is a MAC address

    .. data:: chassis_id_network_address = 5

    	Chassis ID is a network address

    .. data:: chassis_id_interface_name = 6

    	Chassis ID is an interface name

    .. data:: chassis_id_local = 7

    	Chassis ID is a local name

    .. data:: chassis_id_unknown_type = 8

    	Unknown Chassis ID type

    """

    chassis_id_chassis_component = 1

    chassis_id_interface_alias = 2

    chassis_id_port_component = 3

    chassis_id_mac_address = 4

    chassis_id_network_address = 5

    chassis_id_interface_name = 6

    chassis_id_local = 7

    chassis_id_unknown_type = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmChassisIdFmtEnum']


class CfmPmEgressActionEnum(Enum):
    """
    CfmPmEgressActionEnum

    Egress action

    .. data:: egress_ok = 1

    	OK

    .. data:: egress_down = 2

    	Down

    .. data:: egress_blocked = 3

    	STP Blocked

    .. data:: egress_vid = 4

    	VID Blocked

    """

    egress_ok = 1

    egress_down = 2

    egress_blocked = 3

    egress_vid = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmEgressActionEnum']


class CfmPmElmReplyFilterEnum(Enum):
    """
    CfmPmElmReplyFilterEnum

    Reply filter used for Exploratory Linktrace

    operations

    .. data:: reply_filter_not_present = 0

    	Reply Filter not present

    .. data:: reply_filter_default = 1

    	Reply from ports which are not MAC-pruned,

    	VID-pruned, or STP-blocked

    .. data:: reply_filter_vlan_topology = 2

    	Reply from ports which are not VID-pruned or

    	STP-blocked

    .. data:: reply_filter_spanning_tree = 3

    	Reply from ports which are not STP-blocked

    .. data:: reply_filter_all_ports = 4

    	Reply from all ports

    """

    reply_filter_not_present = 0

    reply_filter_default = 1

    reply_filter_vlan_topology = 2

    reply_filter_spanning_tree = 3

    reply_filter_all_ports = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElmReplyFilterEnum']


class CfmPmElrEgressActionEnum(Enum):
    """
    CfmPmElrEgressActionEnum

    ELR Egress action

    .. data:: elr_egress_ok = 1

    	OK

    .. data:: elr_egress_down = 2

    	Down

    .. data:: elr_egress_blocked = 3

    	STP Blocked

    .. data:: elr_egress_vid = 4

    	VID Blocked

    .. data:: elr_egress_mac = 255

    	MAC Pruned

    """

    elr_egress_ok = 1

    elr_egress_down = 2

    elr_egress_blocked = 3

    elr_egress_vid = 4

    elr_egress_mac = 255


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrEgressActionEnum']


class CfmPmElrIngressActionEnum(Enum):
    """
    CfmPmElrIngressActionEnum

    ELR Ingress action

    .. data:: elr_ingress_ok = 1

    	OK

    .. data:: elr_ingress_down = 2

    	Down

    .. data:: elr_ingress_blocked = 3

    	STP Blocked

    .. data:: elr_ingress_vid = 4

    	VID Blocked

    """

    elr_ingress_ok = 1

    elr_ingress_down = 2

    elr_ingress_blocked = 3

    elr_ingress_vid = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrIngressActionEnum']


class CfmPmElrRelayActionEnum(Enum):
    """
    CfmPmElrRelayActionEnum

    ELR relay action

    .. data:: elr_relay_hit = 1

    	Target Hit

    .. data:: elr_relay_fdb = 2

    	Filtering database

    .. data:: elr_relay_flood = 3

    	Flood forwarded

    .. data:: elr_relay_drop = 4

    	Dropped

    """

    elr_relay_hit = 1

    elr_relay_fdb = 2

    elr_relay_flood = 3

    elr_relay_drop = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrRelayActionEnum']


class CfmPmEltDelayModelEnum(Enum):
    """
    CfmPmEltDelayModelEnum

    Delay model used for Exploratory Linktrace

    operations

    .. data:: delay_model_invalid = 0

    	Not a valid delay model

    .. data:: delay_model_logarithmic = 1

    	Reply using logarithmic delay model

    .. data:: delay_model_constant = 2

    	Reply using constant delay model

    """

    delay_model_invalid = 0

    delay_model_logarithmic = 1

    delay_model_constant = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmEltDelayModelEnum']


class CfmPmIdFmtEnum(Enum):
    """
    CfmPmIdFmtEnum

    ID format

    .. data:: id_format_is_string = 0

    	ID format is a string

    .. data:: id_format_is_mac_address = 1

    	ID format is a MAC address

    .. data:: id_format_is_raw_hex = 2

    	ID format is raw hex

    """

    id_format_is_string = 0

    id_format_is_mac_address = 1

    id_format_is_raw_hex = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIdFmtEnum']


class CfmPmIngressActionEnum(Enum):
    """
    CfmPmIngressActionEnum

    Ingress action

    .. data:: ingress_ok = 1

    	OK

    .. data:: ingress_down = 2

    	Down

    .. data:: ingress_blocked = 3

    	STP Blocked

    .. data:: ingress_vid = 4

    	VID Blocked

    """

    ingress_ok = 1

    ingress_down = 2

    ingress_blocked = 3

    ingress_vid = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIngressActionEnum']


class CfmPmIntfStatusEnum(Enum):
    """
    CfmPmIntfStatusEnum

    Interface status

    .. data:: interface_status_up = 1

    	Interface is up

    .. data:: interface_status_down = 2

    	Interface is down

    .. data:: interface_status_testing = 3

    	Interface is in testing mode

    .. data:: interface_status_unknown = 4

    	Unknown interface status

    .. data:: interface_status_dormant = 5

    	Interface is dormant

    .. data:: interface_status_not_present = 6

    	Interface status not found

    .. data:: interface_status_lower_layer_down = 7

    	Lower layer is down

    """

    interface_status_up = 1

    interface_status_down = 2

    interface_status_testing = 3

    interface_status_unknown = 4

    interface_status_dormant = 5

    interface_status_not_present = 6

    interface_status_lower_layer_down = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIntfStatusEnum']


class CfmPmLastHopFmtEnum(Enum):
    """
    CfmPmLastHopFmtEnum

    Last hop identifier format

    .. data:: last_hop_none = 0

    	No last hop identifier

    .. data:: last_hop_host_name = 1

    	Last hop identifier is a hostname

    .. data:: last_hop_egress_id = 2

    	Last hop identifier is an egress ID

    """

    last_hop_none = 0

    last_hop_host_name = 1

    last_hop_egress_id = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmLastHopFmtEnum']


class CfmPmLtModeEnum(Enum):
    """
    CfmPmLtModeEnum

    Type of Linktrace operation

    .. data:: cfm_pm_lt_mode_basic = 1

    	Basic IEEE 802.1ag Linktrace

    .. data:: cfm_pm_lt_mode_exploratory = 2

    	Cisco Exploratory Linktrace

    """

    cfm_pm_lt_mode_basic = 1

    cfm_pm_lt_mode_exploratory = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmLtModeEnum']


class CfmPmMepDefectEnum(Enum):
    """
    CfmPmMepDefectEnum

    Defects that can be reported by a MEP

    .. data:: defect_none = 0

    	No defect reported

    .. data:: defect_rdi_ccm = 1

    	Some Peer MEP's CCM has the RDI bit set

    .. data:: defect_ma_cstatus = 2

    	A Peer MEP port or interface status error has

    	been reported

    .. data:: defect_remote_ccm = 3

    	Not receiving valid CCMs from at least one Peer

    	MEP

    .. data:: defect_error_ccm = 4

    	Currently receiving invalid CCMs from at least

    	one Peer MEP

    .. data:: defect_cross_connect_ccm = 5

    	Currently receiving CCMs from an incorrect

    	service (MA)

    """

    defect_none = 0

    defect_rdi_ccm = 1

    defect_ma_cstatus = 2

    defect_remote_ccm = 3

    defect_error_ccm = 4

    defect_cross_connect_ccm = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmMepDefectEnum']


class CfmPmMepFngStateEnum(Enum):
    """
    CfmPmMepFngStateEnum

    Fault Notification Generation state machine

    states

    .. data:: fng_reset = 1

    	FNG in reset state

    .. data:: fng_defect = 2

    	FNG has detected but not yet reported a defect

    .. data:: fng_report_defect = 3

    	FNG is in the process of reporting a defect

    .. data:: fng_defect_reported = 4

    	FNG has reported a defect

    .. data:: fng_defect_clearing = 5

    	No defect present, but the reset timer has not

    	yet expired

    """

    fng_reset = 1

    fng_defect = 2

    fng_report_defect = 3

    fng_defect_reported = 4

    fng_defect_clearing = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmMepFngStateEnum']


class CfmPmPktActionEnum(Enum):
    """
    CfmPmPktActionEnum

    Action taken for received packet

    .. data:: packet_processed = 0

    	Packet processed successfully

    .. data:: packet_forwarded = 1

    	Packet forwarded

    .. data:: unknown_opcode = 2

    	Packet dropped at a MEP due to unknown opcode

    .. data:: filter_level = 3

    	Packet dropped due to level/opcode filtering at

    	a MEP

    .. data:: filter_blocked = 4

    	Packet dropped because interface is STP blocked

    .. data:: filter_local_mac = 5

    	Packet dropped due to local destination MAC

    .. data:: malformed_ccm_size = 6

    	CCM too short or too long

    .. data:: malformed_ccm_mep_id = 7

    	Invalid MEP-ID

    .. data:: malformed_too_short = 8

    	Packet too short

    .. data:: malformed_destination_mac_unicast = 9

    	Destination MAC address does not match

    	interface

    .. data:: malformed_destination_mac_multicast = 10

    	Invalid multicast destination MAC address

    .. data:: malformed_tlv_offset = 11

    	TLV offset too short or beyond the end of the

    	packet

    .. data:: malformed_lbm_source_mac = 12

    	Invalid source MAC address for LBM

    .. data:: malformed_ltr_relay_action = 13

    	Unknown LTR relay action

    .. data:: malformed_ltr_reply_tlv = 14

    	LTR has neither reply-ingress or reply-egress

    .. data:: malformed_lt_origin = 15

    	Invalid Linktrace Message origin MAC address

    .. data:: malformed_ltm_target = 16

    	Invalid LTM target MAC address

    .. data:: malformed_source_mac = 17

    	Invalid source MAC address

    .. data:: malformed_header_too_short = 18

    	Packet too short for CFM header

    .. data:: malformed_tlv_header_overrun = 19

    	TLV header extends beyond the end of the packet

    .. data:: malformed_tlv_overrun = 20

    	TLV extends beyond the end of the packet

    .. data:: malformed_duplicate_sender_id = 21

    	Multiple Sender-ID TLVs found

    .. data:: malformed_duplicate_port_status = 22

    	Multiple Port-status TLVs found

    .. data:: malformed_duplicate_interface_status = 23

    	Multiple Interface-state TLVs found

    .. data:: malformed_wrong_tlv = 24

    	Invalid TLV for this type of packet found

    .. data:: malformed_duplicate_data = 25

    	Multiple Data TLVs found

    .. data:: malformed_duplicate_ltr_egress_id = 26

    	Multiple LTR-Egress-ID TLVs found

    .. data:: malformed_duplicate_reply_ingress = 27

    	Multiple Reply-ingress TLVs found

    .. data:: malformed_duplicate_reply_egress = 28

    	Multiple Reply-egress TLVs found

    .. data:: malformed_duplicate_ltm_egress_id = 29

    	Multiple LTM-Egress-ID TLVs found

    .. data:: malformed_sender_id_size = 30

    	Sender-ID TLV is too short

    .. data:: malformed_chassis_id_size = 31

    	Sender-ID TLV is too short to contain the

    	Chassis ID

    .. data:: malformed_mgmt_address_domain_size = 32

    	Sender-ID TLV is too short to contain the

    	management address domain

    .. data:: malformed_mgmt_address_size = 33

    	Sender-ID TLV is too short to contain the

    	management address

    .. data:: malformed_port_status_size = 34

    	Port-status TLV is too short

    .. data:: malformed_port_status = 35

    	Invalid Port status value

    .. data:: malformed_interface_status_size = 36

    	Interface-status TLV is too short

    .. data:: malformed_interface_status = 37

    	Invalid Interface status value

    .. data:: malformed_organization_specific_tlv_size = 38

    	Organization-specific TLV is too short

    .. data:: malformed_duplicate_mep_name = 39

    	Multiple MEP-name TLVs found

    .. data:: malformed_duplicate_additional_interface_status = 40

    	Multiple additional-interface-status TLVs found

    .. data:: malformed_ltr_egress_id_size = 41

    	LTR-Egress-ID TLV is too short

    .. data:: malformed_reply_ingress_size = 42

    	Reply-ingress TLV is too short

    .. data:: malformed_ingress_action = 43

    	Invalid ingress-action value

    .. data:: malformed_reply_ingress_mac = 44

    	Reply-ingress TLV has invalid MAC address

    .. data:: malformed_ingress_port_length_size = 45

    	Reply-ingress TLV is too short to contain the

    	Port ID type

    .. data:: malformed_ingress_port_id_length = 46

    	Reply-ingress TLV has a zero Port ID length

    .. data:: malformed_ingress_port_id_size = 47

    	Reply-ingress TLV is too short to contain the

    	Port ID

    .. data:: malformed_reply_egress_size = 48

    	Reply-egress TLV is too short

    .. data:: malformed_egress_action = 49

    	Invalid egress-action value

    .. data:: malformed_reply_egress_mac = 50

    	Reply-egress TLV has invalid MAC address

    .. data:: malformed_egress_port_length_size = 51

    	Reply-egress TLV is too short to contain the

    	Port ID type

    .. data:: malformed_egress_port_id_length = 52

    	Reply-egress TLV has a zero Port ID length

    .. data:: malformed_egress_port_id_size = 53

    	Reply-egress TLV is too short to contain the

    	Port ID

    .. data:: malformed_ltm_egress_id_size = 54

    	LTM-Egress_ID TLV is too short

    .. data:: malformed_mep_name_size = 55

    	MEP-name TLV is too short

    .. data:: malformed_mep_name_name_length = 56

    	MEP-name TLV is too short to contain a MEP name

    .. data:: malformed_additional_interface_status_size = 57

    	Additional-interface-status is too short

    .. data:: malformed_additional_interface_status = 58

    	Invalid additional interface status

    .. data:: malformed_ccm_interval = 59

    	CCM has a zero CCM interval

    .. data:: malformed_mdid_mac_address_length = 60

    	CCM has a MAC-address MDID but the MDID is the

    	wrong length

    .. data:: malformed_mdid_length = 61

    	CCM has an invalid MDID length

    .. data:: malformed_sman_length = 62

    	CCM has an invalid Short MA Name length

    .. data:: malformed_sman2_byte_length = 63

    	CCM has a VID or 16-bit Short MA Name but a

    	mismatched length

    .. data:: malformed_sman_vpn_id_length = 64

    	CCM has a VPNID Short MA Name but a mismatched

    	length

    .. data:: malformed_elr_no_reply_tlv = 65

    	ELR has no ELR Reply TLVs

    .. data:: malformed_separate_elr_reply_egress = 66

    	ELR Reply Egress TLVs not all adjacent

    .. data:: malformed_dcm_destination_multicast = 67

    	DCM has a multicast destination MAC

    .. data:: malformed_dcm_embed_length = 68

    	DCM is too short to contain an Embedded PDU

    .. data:: malformed_dcm_embed_level = 69

    	DCM Embedded PDU level does not match DCM level

    .. data:: malformed_dcm_embed_version = 70

    	DCM Embedded PDU version does not match DCM

    	version

    .. data:: malformed_elr_relay_action = 71

    	Unknown ELR relay action

    .. data:: malformed_elr_tt_ls = 73

    	Reply Ingress TTL is not one greater than Reply

    	Egress TTL

    .. data:: malformed_elr_ttl_ingress = 74

    	Reply Ingress TTL present without ELR Reply

    	Ingress TLV

    .. data:: malformed_elr_ttl_egress = 75

    	Reply Egress TTL present without ELR Reply

    	Egress TLV

    .. data:: malformed_elm_destination_unicast = 76

    	ELM Destination MAC must not be unicast

    .. data:: malformed_elm_egress_id = 77

    	ELM has no LTM Egress ID TLV

    .. data:: malformed_dcm_embed_oui = 78

    	Embedded DCM OUI unrecognized

    .. data:: malformed_dcm_embed_opcode = 79

    	Embedded DCM Opcode is not ELM

    .. data:: malformed_elm_constant_zero = 80

    	ELM Constant Factor is zero

    .. data:: malformed_elr_timeout_zero = 81

    	ELR Next-Hop Timeout is zero

    .. data:: malformed_duplicate_test = 82

    	Multiple Test TLVs found

    .. data:: malformed_dmm_source_mac = 83

    	Invalid source MAC address for DMM

    .. data:: malformed_test_size = 84

    	Test TLV is too short

    .. data:: malformed_dmr_time_stamps = 85

    	DMR has exactly one of its Rxf and Txb

    	timestamps unspecified

    .. data:: malformed_dm_time_stamp_fmt = 86

    	The format of one or more timestamps is invalid

    .. data:: malformed_ais_interval = 87

    	AIS/LCK has invalid interval value (not 1

    	second or 1 minute)

    .. data:: filter_interface_down = 88

    	Packet dropped due to interface being down

    .. data:: filter_forward_standby = 89

    	Packet dropped - not forwarded because

    	interface is in standby mode

    .. data:: malformed_sman_icc_based_length = 90

    	CCM has an ICC-based format Short MA Name but a

    	mismatched length

    .. data:: filter_foward_issu_secondary = 120

    	Packet dropped - not forwarded in secondary HA

    	role

    .. data:: filter_response_standby = 121

    	Packet dropped - not responded to because

    	interface is in standby mode

    .. data:: filter_response_issu_secondary = 122

    	Packet dropped - not responded to in secondary

    	HA role

    """

    packet_processed = 0

    packet_forwarded = 1

    unknown_opcode = 2

    filter_level = 3

    filter_blocked = 4

    filter_local_mac = 5

    malformed_ccm_size = 6

    malformed_ccm_mep_id = 7

    malformed_too_short = 8

    malformed_destination_mac_unicast = 9

    malformed_destination_mac_multicast = 10

    malformed_tlv_offset = 11

    malformed_lbm_source_mac = 12

    malformed_ltr_relay_action = 13

    malformed_ltr_reply_tlv = 14

    malformed_lt_origin = 15

    malformed_ltm_target = 16

    malformed_source_mac = 17

    malformed_header_too_short = 18

    malformed_tlv_header_overrun = 19

    malformed_tlv_overrun = 20

    malformed_duplicate_sender_id = 21

    malformed_duplicate_port_status = 22

    malformed_duplicate_interface_status = 23

    malformed_wrong_tlv = 24

    malformed_duplicate_data = 25

    malformed_duplicate_ltr_egress_id = 26

    malformed_duplicate_reply_ingress = 27

    malformed_duplicate_reply_egress = 28

    malformed_duplicate_ltm_egress_id = 29

    malformed_sender_id_size = 30

    malformed_chassis_id_size = 31

    malformed_mgmt_address_domain_size = 32

    malformed_mgmt_address_size = 33

    malformed_port_status_size = 34

    malformed_port_status = 35

    malformed_interface_status_size = 36

    malformed_interface_status = 37

    malformed_organization_specific_tlv_size = 38

    malformed_duplicate_mep_name = 39

    malformed_duplicate_additional_interface_status = 40

    malformed_ltr_egress_id_size = 41

    malformed_reply_ingress_size = 42

    malformed_ingress_action = 43

    malformed_reply_ingress_mac = 44

    malformed_ingress_port_length_size = 45

    malformed_ingress_port_id_length = 46

    malformed_ingress_port_id_size = 47

    malformed_reply_egress_size = 48

    malformed_egress_action = 49

    malformed_reply_egress_mac = 50

    malformed_egress_port_length_size = 51

    malformed_egress_port_id_length = 52

    malformed_egress_port_id_size = 53

    malformed_ltm_egress_id_size = 54

    malformed_mep_name_size = 55

    malformed_mep_name_name_length = 56

    malformed_additional_interface_status_size = 57

    malformed_additional_interface_status = 58

    malformed_ccm_interval = 59

    malformed_mdid_mac_address_length = 60

    malformed_mdid_length = 61

    malformed_sman_length = 62

    malformed_sman2_byte_length = 63

    malformed_sman_vpn_id_length = 64

    malformed_elr_no_reply_tlv = 65

    malformed_separate_elr_reply_egress = 66

    malformed_dcm_destination_multicast = 67

    malformed_dcm_embed_length = 68

    malformed_dcm_embed_level = 69

    malformed_dcm_embed_version = 70

    malformed_elr_relay_action = 71

    malformed_elr_tt_ls = 73

    malformed_elr_ttl_ingress = 74

    malformed_elr_ttl_egress = 75

    malformed_elm_destination_unicast = 76

    malformed_elm_egress_id = 77

    malformed_dcm_embed_oui = 78

    malformed_dcm_embed_opcode = 79

    malformed_elm_constant_zero = 80

    malformed_elr_timeout_zero = 81

    malformed_duplicate_test = 82

    malformed_dmm_source_mac = 83

    malformed_test_size = 84

    malformed_dmr_time_stamps = 85

    malformed_dm_time_stamp_fmt = 86

    malformed_ais_interval = 87

    filter_interface_down = 88

    filter_forward_standby = 89

    malformed_sman_icc_based_length = 90

    filter_foward_issu_secondary = 120

    filter_response_standby = 121

    filter_response_issu_secondary = 122


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPktActionEnum']


class CfmPmPortIdFmtEnum(Enum):
    """
    CfmPmPortIdFmtEnum

    Port ID format

    .. data:: port_id_interface_alias = 1

    	Port ID is an interface alias

    .. data:: port_id_port_component = 2

    	Port ID is a component name

    .. data:: port_id_mac_address = 3

    	Port ID is a MAC address

    .. data:: port_id_network_address = 4

    	Port ID is a network address

    .. data:: port_id_interface_name = 5

    	Port ID is an interface name

    .. data:: port_id_agent_circuit_id = 6

    	Port ID is an agent name

    .. data:: port_id_local = 7

    	Port ID is a local name

    .. data:: port_id_unknown = 8

    	Port ID format unknown

    """

    port_id_interface_alias = 1

    port_id_port_component = 2

    port_id_mac_address = 3

    port_id_network_address = 4

    port_id_interface_name = 5

    port_id_agent_circuit_id = 6

    port_id_local = 7

    port_id_unknown = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPortIdFmtEnum']


class CfmPmPortStatusEnum(Enum):
    """
    CfmPmPortStatusEnum

    Port status

    .. data:: port_status_blocked = 1

    	Port is STP blocked

    .. data:: port_status_up = 2

    	Port is up

    .. data:: port_status_unknown = 3

    	Unknown port status

    """

    port_status_blocked = 1

    port_status_up = 2

    port_status_unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPortStatusEnum']


class CfmPmRelayActionEnum(Enum):
    """
    CfmPmRelayActionEnum

    LTR relay action

    .. data:: relay_hit = 1

    	Target Hit

    .. data:: relay_fdb = 2

    	Filtering database

    .. data:: relay_mpdb = 3

    	CCM Learning database

    """

    relay_hit = 1

    relay_fdb = 2

    relay_mpdb = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRelayActionEnum']


class CfmPmRmepStateEnum(Enum):
    """
    CfmPmRmepStateEnum

    State of the Peer MEP state machine

    .. data:: peer_mep_idle = 1

    	Momentary state during reset

    .. data:: peer_mep_start = 2

    	Loss timer not expired since reset, but no

    	valid CCM received

    .. data:: peer_mep_failed = 3

    	Loss timer has expired

    .. data:: peer_mep_ok = 4

    	Loss timer has not expired since last valid CCM

    """

    peer_mep_idle = 1

    peer_mep_start = 2

    peer_mep_failed = 3

    peer_mep_ok = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRmepStateEnum']


class CfmPmRmepXcStateEnum(Enum):
    """
    CfmPmRmepXcStateEnum

    Cross\-check state of a peer MEP

    .. data:: cross_check_ok = 0

    	Cross-check OK

    .. data:: cross_check_missing = 1

    	No CCMs received within loss time from peer MEP

    .. data:: cross_check_extra = 2

    	CCMs received from peer MEP not marked for

    	cross-check

    """

    cross_check_ok = 0

    cross_check_missing = 1

    cross_check_extra = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRmepXcStateEnum']


class SlaBucketSizeEnum(Enum):
    """
    SlaBucketSizeEnum

    Type of configuration of a bucket size

    .. data:: buckets_per_probe = 0

    	Bucket size is configured as buckets per probe

    .. data:: probes_per_bucket = 1

    	Bucket size is configured as probes per bucket

    """

    buckets_per_probe = 0

    probes_per_bucket = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaBucketSizeEnum']


class SlaOperBucketEnum(Enum):
    """
    SlaOperBucketEnum

    Type of SLA metric bucket

    .. data:: bucket_type_bins = 0

    	SLA metric bin

    .. data:: bucket_type_samples = 1

    	SLA metric sample

    """

    bucket_type_bins = 0

    bucket_type_samples = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperBucketEnum']


class SlaOperOperationEnum(Enum):
    """
    SlaOperOperationEnum

    Type of SLA operation

    .. data:: operation_type_configured = 0

    	Configured SLA operation

    .. data:: operation_type_ondemand = 1

    	On-demand SLA operation

    """

    operation_type_configured = 0

    operation_type_ondemand = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperOperationEnum']


class SlaOperPacketPriorityEnum(Enum):
    """
    SlaOperPacketPriorityEnum

    Priority scheme for packet priority

    .. data:: priority_none = 0

    	Packet does not use any specified priority.

    .. data:: priority_cos = 1

    	Packet uses a specified 3-bit COS priority

    	value.

    """

    priority_none = 0

    priority_cos = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperPacketPriorityEnum']


class SlaOperTestPatternSchemeEnum(Enum):
    """
    SlaOperTestPatternSchemeEnum

    Test pattern scheme for packet padding

    .. data:: hex = 0

    	Packet is padded with a user-specified string

    .. data:: pseudo_random = 1

    	Packet is padded with a pseudo-random bit

    	sequence

    """

    hex = 0

    pseudo_random = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperTestPatternSchemeEnum']


class SlaRecordableMetricEnum(Enum):
    """
    SlaRecordableMetricEnum

    Types of metrics that can be recorded by probes

    .. data:: metric_invalid = 0

    	Not a valid metric type

    .. data:: metric_round_trip_delay = 1

    	Round-trip Delay

    .. data:: metric_one_way_delay_sd = 2

    	One-way Delay (Source->Destination)

    .. data:: metric_one_way_delay_ds = 3

    	One-way Delay (Destination->Source)

    .. data:: metric_round_trip_jitter = 4

    	Round-trip Jitter

    .. data:: metric_one_way_jitter_sd = 5

    	One-way Jitter (Source->Destination)

    .. data:: metric_one_way_jitter_ds = 6

    	One-way Jitter (Destination->Source)

    .. data:: metric_one_way_flr_sd = 7

    	One-way Frame Loss Ratio (Source->Destination)

    .. data:: metric_one_way_flr_ds = 8

    	One-way Frame Loss Ratio (Destination->Source)

    """

    metric_invalid = 0

    metric_round_trip_delay = 1

    metric_one_way_delay_sd = 2

    metric_one_way_delay_ds = 3

    metric_round_trip_jitter = 4

    metric_one_way_jitter_sd = 5

    metric_one_way_jitter_ds = 6

    metric_one_way_flr_sd = 7

    metric_one_way_flr_ds = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaRecordableMetricEnum']



class Cfm(object):
    """
    CFM operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes>`
    
    

    """

    _prefix = 'ethernet-cfm-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_ = Cfm.Global_()
        self.global_.parent = self
        self.nodes = Cfm.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-cfm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ccm_learning_databases
            
            	CCMLearningDatabase table
            	**type**\:   :py:class:`CcmLearningDatabases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases>`
            
            .. attribute:: interface_aises
            
            	Interface AIS table
            	**type**\:   :py:class:`InterfaceAises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises>`
            
            .. attribute:: interface_statistics
            
            	Interface Statistics table
            	**type**\:   :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics>`
            
            .. attribute:: summary
            
            	Summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.ccm_learning_databases = Cfm.Nodes.Node.CcmLearningDatabases()
                self.ccm_learning_databases.parent = self
                self.interface_aises = Cfm.Nodes.Node.InterfaceAises()
                self.interface_aises.parent = self
                self.interface_statistics = Cfm.Nodes.Node.InterfaceStatistics()
                self.interface_statistics.parent = self
                self.summary = Cfm.Nodes.Node.Summary()
                self.summary.parent = self


            class InterfaceAises(object):
                """
                Interface AIS table
                
                .. attribute:: interface_ais
                
                	AIS statistics for a particular interface
                	**type**\: list of    :py:class:`InterfaceAis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_ais = YList()
                    self.interface_ais.parent = self
                    self.interface_ais.name = 'interface_ais'


                class InterfaceAis(object):
                    """
                    AIS statistics for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: direction  <key>
                    
                    	AIS Direction
                    	**type**\:   :py:class:`CfmAisDirEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmAisDirEnum>`
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_state
                    
                    	IM Interface state
                    	**type**\:  str
                    
                    .. attribute:: interworking_state
                    
                    	Interface interworking state
                    	**type**\:   :py:class:`CfmBagIwStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwStateEnum>`
                    
                    .. attribute:: statistics
                    
                    	AIS statistics
                    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics>`
                    
                    .. attribute:: stp_state
                    
                    	STP state
                    	**type**\:   :py:class:`CfmBagStpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpStateEnum>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.direction = None
                        self.interface = None
                        self.interface_state = None
                        self.interworking_state = None
                        self.statistics = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics()
                        self.statistics.parent = self
                        self.stp_state = None


                    class Statistics(object):
                        """
                        AIS statistics
                        
                        .. attribute:: defects
                        
                        	Defects detected
                        	**type**\:   :py:class:`Defects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects>`
                        
                        .. attribute:: direction
                        
                        	Direction of AIS packets
                        	**type**\:   :py:class:`CfmBagDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                        
                        .. attribute:: last_started
                        
                        	Time elapsed since sending last started
                        	**type**\:   :py:class:`LastStarted <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted>`
                        
                        .. attribute:: lowest_level
                        
                        	Level of the lowest MEP transmitting AIS
                        	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: sent_packets
                        
                        	Total number of packets sent by the transmitting MEP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmission_interval
                        
                        	Interval at which AIS packets are transmitted
                        	**type**\:   :py:class:`CfmBagAisIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                        
                        .. attribute:: transmission_level
                        
                        	Level that AIS packets are transmitted on
                        	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: via_level
                        
                        	Levels of other MEPs receiving AIS
                        	**type**\:  list of   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.defects = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects()
                            self.defects.parent = self
                            self.direction = None
                            self.last_started = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted()
                            self.last_started.parent = self
                            self.lowest_level = None
                            self.sent_packets = None
                            self.transmission_interval = None
                            self.transmission_level = None
                            self.via_level = YLeafList()
                            self.via_level.parent = self
                            self.via_level.name = 'via_level'


                        class Defects(object):
                            """
                            Defects detected
                            
                            .. attribute:: ais_received
                            
                            	AIS or LCK received
                            	**type**\:  bool
                            
                            .. attribute:: auto_missing
                            
                            	Number of missing auto cross\-check MEPs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_port_status
                            
                            	The local port or interface is down
                            	**type**\:  bool
                            
                            .. attribute:: missing
                            
                            	Number of missing peer MEPs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_meps_that_timed_out
                            
                            	Number of peer MEPs that have timed out
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_port_status
                            
                            	A peer port or interface is down
                            	**type**\:  bool
                            
                            .. attribute:: remote_meps_defects
                            
                            	Defects detected from remote MEPs
                            	**type**\:   :py:class:`RemoteMepsDefects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects>`
                            
                            .. attribute:: unexpected
                            
                            	Number of unexpected peer MEPs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ais_received = None
                                self.auto_missing = None
                                self.local_port_status = None
                                self.missing = None
                                self.peer_meps_that_timed_out = None
                                self.peer_port_status = None
                                self.remote_meps_defects = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects()
                                self.remote_meps_defects.parent = self
                                self.unexpected = None


                            class RemoteMepsDefects(object):
                                """
                                Defects detected from remote MEPs
                                
                                .. attribute:: invalid_ccm_interval
                                
                                	Invalid CCM interval
                                	**type**\:  bool
                                
                                .. attribute:: invalid_level
                                
                                	Invalid level
                                	**type**\:  bool
                                
                                .. attribute:: invalid_maid
                                
                                	Invalid MAID
                                	**type**\:  bool
                                
                                .. attribute:: loss_threshold_exceeded
                                
                                	Timed out (loss threshold exceeded)
                                	**type**\:  bool
                                
                                .. attribute:: received_our_mac
                                
                                	Loop detected (our MAC address received)
                                	**type**\:  bool
                                
                                .. attribute:: received_our_mep_id
                                
                                	Configuration Error (our MEP ID received)
                                	**type**\:  bool
                                
                                .. attribute:: received_rdi
                                
                                	Remote defection indication received
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.invalid_ccm_interval = None
                                    self.invalid_level = None
                                    self.invalid_maid = None
                                    self.loss_threshold_exceeded = None
                                    self.received_our_mac = None
                                    self.received_our_mep_id = None
                                    self.received_rdi = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:remote-meps-defects'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.invalid_ccm_interval is not None:
                                        return True

                                    if self.invalid_level is not None:
                                        return True

                                    if self.invalid_maid is not None:
                                        return True

                                    if self.loss_threshold_exceeded is not None:
                                        return True

                                    if self.received_our_mac is not None:
                                        return True

                                    if self.received_our_mep_id is not None:
                                        return True

                                    if self.received_rdi is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:defects'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ais_received is not None:
                                    return True

                                if self.auto_missing is not None:
                                    return True

                                if self.local_port_status is not None:
                                    return True

                                if self.missing is not None:
                                    return True

                                if self.peer_meps_that_timed_out is not None:
                                    return True

                                if self.peer_port_status is not None:
                                    return True

                                if self.remote_meps_defects is not None and self.remote_meps_defects._has_data():
                                    return True

                                if self.unexpected is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info']


                        class LastStarted(object):
                            """
                            Time elapsed since sending last started
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: nanosecond
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.nanoseconds = None
                                self.seconds = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-started'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.nanoseconds is not None:
                                    return True

                                if self.seconds is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.defects is not None and self.defects._has_data():
                                return True

                            if self.direction is not None:
                                return True

                            if self.last_started is not None and self.last_started._has_data():
                                return True

                            if self.lowest_level is not None:
                                return True

                            if self.sent_packets is not None:
                                return True

                            if self.transmission_interval is not None:
                                return True

                            if self.transmission_level is not None:
                                return True

                            if self.via_level is not None:
                                for child in self.via_level:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')
                        if self.direction is None:
                            raise YPYModelError('Key property direction is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-ais[Cisco-IOS-XR-ethernet-cfm-oper:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ethernet-cfm-oper:direction = ' + str(self.direction) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.direction is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.interface_state is not None:
                            return True

                        if self.interworking_state is not None:
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        if self.stp_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-aises'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_ais is not None:
                        for child_ref in self.interface_ais:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info']


            class InterfaceStatistics(object):
                """
                Interface Statistics table
                
                .. attribute:: interface_statistic
                
                	Counters for a particular interface
                	**type**\: list of    :py:class:`InterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_statistic = YList()
                    self.interface_statistic.parent = self
                    self.interface_statistic.name = 'interface_statistic'


                class InterfaceStatistic(object):
                    """
                    Counters for a particular interface
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: statistics
                    
                    	EFP statistics
                    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.interface_xr = None
                        self.statistics = Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics()
                        self.statistics.parent = self


                    class Statistics(object):
                        """
                        EFP statistics
                        
                        .. attribute:: dropped_packets
                        
                        	Number of packets dropped at this EFP
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_malformed_opcode
                        
                        	Opcode for last malformed packet
                        	**type**\:   :py:class:`CfmBagOpcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagOpcodeEnum>`
                        
                        .. attribute:: last_malformed_reason
                        
                        	Reason last malformed packet was malformed
                        	**type**\:   :py:class:`CfmPmPktActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPktActionEnum>`
                        
                        .. attribute:: malformed_packets
                        
                        	Number of malformed packets received at this EFP
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped_packets = None
                            self.last_malformed_opcode = None
                            self.last_malformed_reason = None
                            self.malformed_packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped_packets is not None:
                                return True

                            if self.last_malformed_opcode is not None:
                                return True

                            if self.last_malformed_reason is not None:
                                return True

                            if self.malformed_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-statistic[Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.interface_xr is not None:
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_statistic is not None:
                        for child_ref in self.interface_statistic:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info']


            class Summary(object):
                """
                Summary
                
                .. attribute:: bnm_enabled_links
                
                	Number of BNM Enabled Links
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bridge_domains_and_xconnects
                
                	Number or bridge domains and crossconnects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_learning_db_entries
                
                	Number of entries in the CCM learning database
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_rate
                
                	The combined rate of CCMs on this card
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_misconfigured
                
                	The number of local MEPs disabled due to configuration errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_operational_error
                
                	The number of local MEPs disabled due to operational errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_out_of_resources
                
                	The number of local MEPs disabled due to lack of resources
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: domains
                
                	The number of domains in the CFM database
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_meps
                
                	The number of down\-MEPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interfaces
                
                	The number of interfaces running CFM
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: issu_role
                
                	ISSU Role of CFM\-D, if any
                	**type**\:   :py:class:`CfmBagIssuRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIssuRoleEnum>`
                
                .. attribute:: local_meps
                
                	The number of local MEPs in the CFM database
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mips
                
                	The number of MIPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded
                
                	The number of MEPs for which CCM processing has been offloaded
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at10ms
                
                	The number of MEPs offloaded with CCMs at 10ms intervals
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at3_3ms
                
                	The number of MEPs offloaded with CCMs at 3.3ms intervals
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_local_meps
                
                	The number of operational local MEPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_peer_meps
                
                	The number of operational peer MEPs recorded in the CFM database
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps
                
                	The number of peer MEPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_timed_out
                
                	The number of peer MEPs that have timed out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_with_defects
                
                	The number of peer MEPs with defects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_without_defects
                
                	The number of peer MEPs without defects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: services
                
                	The number of services in the CFM database
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_cache_entries
                
                	Number of traceroute cache entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_cache_replies
                
                	Number of traceroute cache replies
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_meps
                
                	The number of up\-MEPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bnm_enabled_links = None
                    self.bridge_domains_and_xconnects = None
                    self.ccm_learning_db_entries = None
                    self.ccm_rate = None
                    self.disabled_misconfigured = None
                    self.disabled_operational_error = None
                    self.disabled_out_of_resources = None
                    self.domains = None
                    self.down_meps = None
                    self.interfaces = None
                    self.issu_role = None
                    self.local_meps = None
                    self.mips = None
                    self.offloaded = None
                    self.offloaded_at10ms = None
                    self.offloaded_at3_3ms = None
                    self.operational_local_meps = None
                    self.operational_peer_meps = None
                    self.peer_meps = None
                    self.peer_meps_timed_out = None
                    self.peer_meps_with_defects = None
                    self.peer_meps_without_defects = None
                    self.services = None
                    self.traceroute_cache_entries = None
                    self.traceroute_cache_replies = None
                    self.up_meps = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bnm_enabled_links is not None:
                        return True

                    if self.bridge_domains_and_xconnects is not None:
                        return True

                    if self.ccm_learning_db_entries is not None:
                        return True

                    if self.ccm_rate is not None:
                        return True

                    if self.disabled_misconfigured is not None:
                        return True

                    if self.disabled_operational_error is not None:
                        return True

                    if self.disabled_out_of_resources is not None:
                        return True

                    if self.domains is not None:
                        return True

                    if self.down_meps is not None:
                        return True

                    if self.interfaces is not None:
                        return True

                    if self.issu_role is not None:
                        return True

                    if self.local_meps is not None:
                        return True

                    if self.mips is not None:
                        return True

                    if self.offloaded is not None:
                        return True

                    if self.offloaded_at10ms is not None:
                        return True

                    if self.offloaded_at3_3ms is not None:
                        return True

                    if self.operational_local_meps is not None:
                        return True

                    if self.operational_peer_meps is not None:
                        return True

                    if self.peer_meps is not None:
                        return True

                    if self.peer_meps_timed_out is not None:
                        return True

                    if self.peer_meps_with_defects is not None:
                        return True

                    if self.peer_meps_without_defects is not None:
                        return True

                    if self.services is not None:
                        return True

                    if self.traceroute_cache_entries is not None:
                        return True

                    if self.traceroute_cache_replies is not None:
                        return True

                    if self.up_meps is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.Summary']['meta_info']


            class CcmLearningDatabases(object):
                """
                CCMLearningDatabase table
                
                .. attribute:: ccm_learning_database
                
                	CCM Learning Database entry
                	**type**\: list of    :py:class:`CcmLearningDatabase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ccm_learning_database = YList()
                    self.ccm_learning_database.parent = self
                    self.ccm_learning_database.name = 'ccm_learning_database'


                class CcmLearningDatabase(object):
                    """
                    CCM Learning Database entry
                    
                    .. attribute:: domain  <key>
                    
                    	Maintenance Domain
                    	**type**\:  str
                    
                    	**length:** 1..79
                    
                    .. attribute:: service  <key>
                    
                    	Service (Maintenance Association)
                    	**type**\:  str
                    
                    	**length:** 1..79
                    
                    .. attribute:: mac_address  <key>
                    
                    	MAC Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain_xr
                    
                    	Maintenance domain name
                    	**type**\:  str
                    
                    .. attribute:: ingress_interface
                    
                    	The XID of the ingress interface for the CCM
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ingress_interface_string
                    
                    	String representation of the Bridge Domain or Cross\-Connect associated with the ingress XID
                    	**type**\:  str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: service_xr
                    
                    	Maintenance association name
                    	**type**\:  str
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: stale
                    
                    	The XID is stale and may have been reused for a different interface
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.domain = None
                        self.service = None
                        self.mac_address = None
                        self.domain_xr = None
                        self.ingress_interface = None
                        self.ingress_interface_string = None
                        self.level = None
                        self.service_xr = None
                        self.source_mac_address = None
                        self.stale = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.domain is None:
                            raise YPYModelError('Key property domain is None')
                        if self.service is None:
                            raise YPYModelError('Key property service is None')
                        if self.mac_address is None:
                            raise YPYModelError('Key property mac_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ccm-learning-database[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:mac-address = ' + str(self.mac_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain is not None:
                            return True

                        if self.service is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.domain_xr is not None:
                            return True

                        if self.ingress_interface is not None:
                            return True

                        if self.ingress_interface_string is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.service_xr is not None:
                            return True

                        if self.source_mac_address is not None:
                            return True

                        if self.stale is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ccm-learning-databases'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ccm_learning_database is not None:
                        for child_ref in self.ccm_learning_database:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:nodes/Cisco-IOS-XR-ethernet-cfm-oper:node[Cisco-IOS-XR-ethernet-cfm-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.ccm_learning_databases is not None and self.ccm_learning_databases._has_data():
                    return True

                if self.interface_aises is not None and self.interface_aises._has_data():
                    return True

                if self.interface_statistics is not None and self.interface_statistics._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
            return meta._meta_table['Cfm.Nodes']['meta_info']


    class Global_(object):
        """
        Global operational data
        
        .. attribute:: global_configuration_errors
        
        	Global configuration errors table
        	**type**\:   :py:class:`GlobalConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.GlobalConfigurationErrors>`
        
        .. attribute:: incomplete_traceroutes
        
        	Incomplete Traceroute table
        	**type**\:   :py:class:`IncompleteTraceroutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes>`
        
        .. attribute:: local_meps
        
        	Local MEPs table
        	**type**\:   :py:class:`LocalMeps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps>`
        
        .. attribute:: maintenance_points
        
        	Maintenance Points table
        	**type**\:   :py:class:`MaintenancePoints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MaintenancePoints>`
        
        .. attribute:: mep_configuration_errors
        
        	MEP configuration errors table
        	**type**\:   :py:class:`MepConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors>`
        
        .. attribute:: peer_me_pv2s
        
        	Peer MEPs table Version 2
        	**type**\:   :py:class:`PeerMePv2S <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S>`
        
        .. attribute:: traceroute_caches
        
        	Traceroute Cache table
        	**type**\:   :py:class:`TracerouteCaches <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches>`
        
        

        """

        _prefix = 'ethernet-cfm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_configuration_errors = Cfm.Global_.GlobalConfigurationErrors()
            self.global_configuration_errors.parent = self
            self.incomplete_traceroutes = Cfm.Global_.IncompleteTraceroutes()
            self.incomplete_traceroutes.parent = self
            self.local_meps = Cfm.Global_.LocalMeps()
            self.local_meps.parent = self
            self.maintenance_points = Cfm.Global_.MaintenancePoints()
            self.maintenance_points.parent = self
            self.mep_configuration_errors = Cfm.Global_.MepConfigurationErrors()
            self.mep_configuration_errors.parent = self
            self.peer_me_pv2s = Cfm.Global_.PeerMePv2S()
            self.peer_me_pv2s.parent = self
            self.traceroute_caches = Cfm.Global_.TracerouteCaches()
            self.traceroute_caches.parent = self


        class IncompleteTraceroutes(object):
            """
            Incomplete Traceroute table
            
            .. attribute:: incomplete_traceroute
            
            	Information about a traceroute operation that has not yet timed out
            	**type**\: list of    :py:class:`IncompleteTraceroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.incomplete_traceroute = YList()
                self.incomplete_traceroute.parent = self
                self.incomplete_traceroute.name = 'incomplete_traceroute'


            class IncompleteTraceroute(object):
                """
                Information about a traceroute operation that
                has not yet timed out
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  <key>
                
                	MEP ID
                	**type**\:  int
                
                	**range:** 1..8191
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: transaction_id  <key>
                
                	Transaction ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: time_left
                
                	Time (in seconds) before the traceroute completes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\:   :py:class:`TracerouteInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.transaction_id = None
                    self.time_left = None
                    self.traceroute_information = Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation()
                    self.traceroute_information.parent = self


                class TracerouteInformation(object):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\:  str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options>`
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\:  str
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mep_id
                    
                    	Target MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: timestamp
                    
                    	Timestamp of initiation time (seconds)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.directed_mac_address = None
                        self.domain = None
                        self.level = None
                        self.options = Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options()
                        self.options.parent = self
                        self.service = None
                        self.source_interface = None
                        self.source_mac_address = None
                        self.source_mep_id = None
                        self.target_mac_address = None
                        self.target_mep_id = None
                        self.timestamp = None
                        self.transaction_id = None
                        self.ttl = None


                    class Options(object):
                        """
                        Options affecting traceroute behavior
                        
                        .. attribute:: basic_options
                        
                        	Options for a basic IEEE 802.1ag Linktrace
                        	**type**\:   :py:class:`BasicOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\:   :py:class:`ExploratoryOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\:   :py:class:`CfmPmLtModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtModeEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.basic_options = Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self.exploratory_options = Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self.mode = None


                        class BasicOptions(object):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\:  bool
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fdb_only = None
                                self.is_auto = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:basic-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fdb_only is not None:
                                    return True

                                if self.is_auto is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions']['meta_info']


                        class ExploratoryOptions(object):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\:   :py:class:`CfmPmEltDelayModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\:   :py:class:`CfmPmElmReplyFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilterEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_constant_factor = None
                                self.delay_model = None
                                self.reply_filter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.delay_constant_factor is not None:
                                    return True

                                if self.delay_model is not None:
                                    return True

                                if self.reply_filter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.basic_options is not None and self.basic_options._has_data():
                                return True

                            if self.exploratory_options is not None and self.exploratory_options._has_data():
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.directed_mac_address is not None:
                            return True

                        if self.domain is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.options is not None and self.options._has_data():
                            return True

                        if self.service is not None:
                            return True

                        if self.source_interface is not None:
                            return True

                        if self.source_mac_address is not None:
                            return True

                        if self.source_mep_id is not None:
                            return True

                        if self.target_mac_address is not None:
                            return True

                        if self.target_mep_id is not None:
                            return True

                        if self.timestamp is not None:
                            return True

                        if self.transaction_id is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.mep_id is None:
                        raise YPYModelError('Key property mep_id is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')
                    if self.transaction_id is None:
                        raise YPYModelError('Key property transaction_id is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroutes/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroute[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:transaction-id = ' + str(self.transaction_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.transaction_id is not None:
                        return True

                    if self.time_left is not None:
                        return True

                    if self.traceroute_information is not None and self.traceroute_information._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroutes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.incomplete_traceroute is not None:
                    for child_ref in self.incomplete_traceroute:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.IncompleteTraceroutes']['meta_info']


        class MaintenancePoints(object):
            """
            Maintenance Points table
            
            .. attribute:: maintenance_point
            
            	Information about a particular Maintenance Point
            	**type**\: list of    :py:class:`MaintenancePoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MaintenancePoints.MaintenancePoint>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.maintenance_point = YList()
                self.maintenance_point.parent = self
                self.maintenance_point.name = 'maintenance_point'


            class MaintenancePoint(object):
                """
                Information about a particular Maintenance
                Point
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: maintenance_point
                
                	Maintenance Point
                	**type**\:   :py:class:`MaintenancePoint_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_>`
                
                .. attribute:: mep_has_error
                
                	MEP error flag
                	**type**\:  bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.interface = None
                    self.mac_address = None
                    self.maintenance_point = Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_()
                    self.maintenance_point.parent = self
                    self.mep_has_error = None


                class MaintenancePoint_(object):
                    """
                    Maintenance Point
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\:   :py:class:`CfmMaMpVarietyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVarietyEnum>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.domain_name = None
                        self.interface = None
                        self.level = None
                        self.maintenance_point_type = None
                        self.mep_id = None
                        self.service_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-point'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_name is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.maintenance_point_type is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.service_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-points/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-point[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.maintenance_point is not None and self.maintenance_point._has_data():
                        return True

                    if self.mep_has_error is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.MaintenancePoints.MaintenancePoint']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-points'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.maintenance_point is not None:
                    for child_ref in self.maintenance_point:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.MaintenancePoints']['meta_info']


        class GlobalConfigurationErrors(object):
            """
            Global configuration errors table
            
            .. attribute:: global_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of    :py:class:`GlobalConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.global_configuration_error = YList()
                self.global_configuration_error.parent = self
                self.global_configuration_error.name = 'global_configuration_error'


            class GlobalConfigurationError(object):
                """
                Information about a particular configuration
                error
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: bridge_domain_id
                
                	BD/XC ID, or Service name if the Service is 'down\-only'
                	**type**\:   :py:class:`BridgeDomainId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId>`
                
                .. attribute:: bridge_domain_is_configured
                
                	The BD/XC is configured globally
                	**type**\:  bool
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                .. attribute:: l2_fib_download_error
                
                	The BD/XC could not be downloaded to L2FIB
                	**type**\:  bool
                
                .. attribute:: level
                
                	Level
                	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: service_name
                
                	Service name
                	**type**\:  str
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.bridge_domain_id = Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId()
                    self.bridge_domain_id.parent = self
                    self.bridge_domain_is_configured = None
                    self.domain_name = None
                    self.l2_fib_download_error = None
                    self.level = None
                    self.service_name = None


                class BridgeDomainId(object):
                    """
                    BD/XC ID, or Service name if the Service is
                    'down\-only'
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:   :py:class:`CfmBagBdidFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\:  str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\:  str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bridge_domain_id_format = None
                        self.ce_id = None
                        self.group = None
                        self.name = None
                        self.remote_ce_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:bridge-domain-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bridge_domain_id_format is not None:
                            return True

                        if self.ce_id is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.remote_ce_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-errors/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-error[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.bridge_domain_id is not None and self.bridge_domain_id._has_data():
                        return True

                    if self.bridge_domain_is_configured is not None:
                        return True

                    if self.domain_name is not None:
                        return True

                    if self.l2_fib_download_error is not None:
                        return True

                    if self.level is not None:
                        return True

                    if self.service_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-errors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.global_configuration_error is not None:
                    for child_ref in self.global_configuration_error:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.GlobalConfigurationErrors']['meta_info']


        class MepConfigurationErrors(object):
            """
            MEP configuration errors table
            
            .. attribute:: mep_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of    :py:class:`MepConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mep_configuration_error = YList()
                self.mep_configuration_error.parent = self
                self.mep_configuration_error.name = 'mep_configuration_error'


            class MepConfigurationError(object):
                """
                Information about a particular configuration
                error
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: ais_configured
                
                	AIS is configured on the same interface as the down MEP
                	**type**\:  bool
                
                .. attribute:: bridge_domain_mismatch
                
                	The MEP's EFP is not in the Service's Bridge Domain
                	**type**\:  bool
                
                .. attribute:: bridge_domain_not_in_bd_infra
                
                	A BD/XC specified in the MEG config, but it does not exist globally
                	**type**\:  bool
                
                .. attribute:: bundle_level0
                
                	The MEP is configured in a domain at level 0, on a bundle interface or sub\-interface.  This is not supported
                	**type**\:  bool
                
                .. attribute:: ccm_interval
                
                	Interval between CCMs sent on this MEP
                	**type**\:   :py:class:`CfmBagCcmIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                
                .. attribute:: ccm_interval_not_supported
                
                	CCM Interval is less than minimum interval supported by hardware
                	**type**\:  bool
                
                .. attribute:: fatal_offload_error
                
                	The platform returned a fatal error when passed the offload session
                	**type**\:  bool
                
                .. attribute:: interface_bridge_domain
                
                	ID of the BD/XC that the MEP's EFP is in, if any
                	**type**\:   :py:class:`InterfaceBridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain>`
                
                .. attribute:: level_conflict
                
                	Another MEP facing in the same direction is at the same Maintenance Level
                	**type**\:  bool
                
                .. attribute:: maid_format_not_supported
                
                	The configured MAID format is not supported for hardware offload
                	**type**\:  bool
                
                .. attribute:: mep
                
                	The MEP that has errors
                	**type**\:   :py:class:`Mep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep>`
                
                .. attribute:: no_domain
                
                	The MEP's Domain is not configured
                	**type**\:  bool
                
                .. attribute:: no_interface_type
                
                	We haven't yet been able to look up the interface type to find whether the interface is a bundle
                	**type**\:  bool
                
                .. attribute:: no_mlacp
                
                	The EFP is a bundle and the mLACP mode is not yet known
                	**type**\:  bool
                
                .. attribute:: no_service
                
                	The MEP's Service is not configured
                	**type**\:  bool
                
                .. attribute:: no_valid_mac_address
                
                	The EFP doesn't have a valid MAC address yet. This will also get set if the MAC address we have is a multicast address
                	**type**\:  bool
                
                .. attribute:: not_in_im
                
                	The EFP has been deleted from IM
                	**type**\:  bool
                
                .. attribute:: offload_mep_direction_not_supported
                
                	The MEP direction does not support offload
                	**type**\:  bool
                
                .. attribute:: offload_multiple_local_mep
                
                	Multiple offloaded MEPs on the same interface are not supported
                	**type**\:  bool
                
                .. attribute:: offload_multiple_peer_meps
                
                	The MEP should be offloaded but multiple crosscheck MEPs have been configured, and this is not supported
                	**type**\:  bool
                
                .. attribute:: offload_no_cross_check
                
                	The MEP should be offloaded but crosscheck has not been configured
                	**type**\:  bool
                
                .. attribute:: offload_out_of_resources
                
                	Offload resource limits have been exceeded
                	**type**\:  bool
                
                .. attribute:: satellite_capabilities
                
                	Satellite Capabilities
                	**type**\:   :py:class:`SatelliteCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities>`
                
                .. attribute:: satellite_error_string
                
                	Error string returned from satellite
                	**type**\:  str
                
                .. attribute:: satellite_id
                
                	ID of the satellite
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: satellite_limitation
                
                	A satellite limitation is preventing MEP being offloaded to satellite
                	**type**\:  bool
                
                .. attribute:: service_bridge_domain
                
                	BD/XC ID for the MEP's Service, or Service name if the Service is 'down\-only'
                	**type**\:   :py:class:`ServiceBridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain>`
                
                .. attribute:: sla_delay_measurement_operations_disabled
                
                	In\-progress Ethernet SLA delay measurement operations are disabled due to satellite having delay measurement responder\-only capabilities
                	**type**\:  bool
                
                .. attribute:: sla_loopback_operations_disabled
                
                	In\-progress Ethernet SLA loopback operations are disabled due to satellite having loopback responder\-only capabilities
                	**type**\:  bool
                
                .. attribute:: sla_synthetic_loss_operations_disabled
                
                	In\-progress Ethernet SLA synthetic loss measurement operations are disabled due to satellite having synthetic loss measurement responder\-only capabilities
                	**type**\:  bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.interface = None
                    self.ais_configured = None
                    self.bridge_domain_mismatch = None
                    self.bridge_domain_not_in_bd_infra = None
                    self.bundle_level0 = None
                    self.ccm_interval = None
                    self.ccm_interval_not_supported = None
                    self.fatal_offload_error = None
                    self.interface_bridge_domain = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain()
                    self.interface_bridge_domain.parent = self
                    self.level_conflict = None
                    self.maid_format_not_supported = None
                    self.mep = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep()
                    self.mep.parent = self
                    self.no_domain = None
                    self.no_interface_type = None
                    self.no_mlacp = None
                    self.no_service = None
                    self.no_valid_mac_address = None
                    self.not_in_im = None
                    self.offload_mep_direction_not_supported = None
                    self.offload_multiple_local_mep = None
                    self.offload_multiple_peer_meps = None
                    self.offload_no_cross_check = None
                    self.offload_out_of_resources = None
                    self.satellite_capabilities = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities()
                    self.satellite_capabilities.parent = self
                    self.satellite_error_string = None
                    self.satellite_id = None
                    self.satellite_limitation = None
                    self.service_bridge_domain = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain()
                    self.service_bridge_domain.parent = self
                    self.sla_delay_measurement_operations_disabled = None
                    self.sla_loopback_operations_disabled = None
                    self.sla_synthetic_loss_operations_disabled = None


                class Mep(object):
                    """
                    The MEP that has errors
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\:  str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\:   :py:class:`CfmMaMpVarietyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVarietyEnum>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.domain_name = None
                        self.interface = None
                        self.level = None
                        self.maintenance_point_type = None
                        self.mep_id = None
                        self.service_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.domain_name is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.maintenance_point_type is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.service_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep']['meta_info']


                class ServiceBridgeDomain(object):
                    """
                    BD/XC ID for the MEP's Service, or Service name
                    if the Service is 'down\-only'
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:   :py:class:`CfmBagBdidFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\:  str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\:  str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bridge_domain_id_format = None
                        self.ce_id = None
                        self.group = None
                        self.name = None
                        self.remote_ce_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:service-bridge-domain'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bridge_domain_id_format is not None:
                            return True

                        if self.ce_id is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.remote_ce_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain']['meta_info']


                class InterfaceBridgeDomain(object):
                    """
                    ID of the BD/XC that the MEP's EFP is in, if any
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:   :py:class:`CfmBagBdidFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\:  str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\:  str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bridge_domain_id_format = None
                        self.ce_id = None
                        self.group = None
                        self.name = None
                        self.remote_ce_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-bridge-domain'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bridge_domain_id_format is not None:
                            return True

                        if self.ce_id is not None:
                            return True

                        if self.group is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.remote_ce_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain']['meta_info']


                class SatelliteCapabilities(object):
                    """
                    Satellite Capabilities
                    
                    .. attribute:: delay_measurement
                    
                    	Delay Measurement
                    	**type**\:   :py:class:`DelayMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement>`
                    
                    .. attribute:: loopback
                    
                    	Loopback
                    	**type**\:   :py:class:`Loopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback>`
                    
                    .. attribute:: synthetic_loss_measurement
                    
                    	Synthetic Loss Measurement
                    	**type**\:   :py:class:`SyntheticLossMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.delay_measurement = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement()
                        self.delay_measurement.parent = self
                        self.loopback = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback()
                        self.loopback.parent = self
                        self.synthetic_loss_measurement = Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement()
                        self.synthetic_loss_measurement.parent = self


                    class Loopback(object):
                        """
                        Loopback
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\:  bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.controller = None
                            self.responder = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:loopback'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback']['meta_info']


                    class DelayMeasurement(object):
                        """
                        Delay Measurement
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\:  bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.controller = None
                            self.responder = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:delay-measurement'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement']['meta_info']


                    class SyntheticLossMeasurement(object):
                        """
                        Synthetic Loss Measurement
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\:  bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.controller = None
                            self.responder = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:synthetic-loss-measurement'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:satellite-capabilities'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.delay_measurement is not None and self.delay_measurement._has_data():
                            return True

                        if self.loopback is not None and self.loopback._has_data():
                            return True

                        if self.synthetic_loss_measurement is not None and self.synthetic_loss_measurement._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-errors/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-error[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.ais_configured is not None:
                        return True

                    if self.bridge_domain_mismatch is not None:
                        return True

                    if self.bridge_domain_not_in_bd_infra is not None:
                        return True

                    if self.bundle_level0 is not None:
                        return True

                    if self.ccm_interval is not None:
                        return True

                    if self.ccm_interval_not_supported is not None:
                        return True

                    if self.fatal_offload_error is not None:
                        return True

                    if self.interface_bridge_domain is not None and self.interface_bridge_domain._has_data():
                        return True

                    if self.level_conflict is not None:
                        return True

                    if self.maid_format_not_supported is not None:
                        return True

                    if self.mep is not None and self.mep._has_data():
                        return True

                    if self.no_domain is not None:
                        return True

                    if self.no_interface_type is not None:
                        return True

                    if self.no_mlacp is not None:
                        return True

                    if self.no_service is not None:
                        return True

                    if self.no_valid_mac_address is not None:
                        return True

                    if self.not_in_im is not None:
                        return True

                    if self.offload_mep_direction_not_supported is not None:
                        return True

                    if self.offload_multiple_local_mep is not None:
                        return True

                    if self.offload_multiple_peer_meps is not None:
                        return True

                    if self.offload_no_cross_check is not None:
                        return True

                    if self.offload_out_of_resources is not None:
                        return True

                    if self.satellite_capabilities is not None and self.satellite_capabilities._has_data():
                        return True

                    if self.satellite_error_string is not None:
                        return True

                    if self.satellite_id is not None:
                        return True

                    if self.satellite_limitation is not None:
                        return True

                    if self.service_bridge_domain is not None and self.service_bridge_domain._has_data():
                        return True

                    if self.sla_delay_measurement_operations_disabled is not None:
                        return True

                    if self.sla_loopback_operations_disabled is not None:
                        return True

                    if self.sla_synthetic_loss_operations_disabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-errors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.mep_configuration_error is not None:
                    for child_ref in self.mep_configuration_error:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.MepConfigurationErrors']['meta_info']


        class TracerouteCaches(object):
            """
            Traceroute Cache table
            
            .. attribute:: traceroute_cache
            
            	Information about a particular traceroute operation
            	**type**\: list of    :py:class:`TracerouteCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.traceroute_cache = YList()
                self.traceroute_cache.parent = self
                self.traceroute_cache.name = 'traceroute_cache'


            class TracerouteCache(object):
                """
                Information about a particular traceroute
                operation
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  <key>
                
                	MEP ID
                	**type**\:  int
                
                	**range:** 1..8191
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: transaction_id  <key>
                
                	Transaction ID
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: exploratory_linktrace_reply
                
                	Received exploratory linktrace replies
                	**type**\: list of    :py:class:`ExploratoryLinktraceReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply>`
                
                .. attribute:: linktrace_reply
                
                	Received linktrace replies
                	**type**\: list of    :py:class:`LinktraceReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply>`
                
                .. attribute:: replies_dropped
                
                	Count of ignored replies for this request
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\:   :py:class:`TracerouteInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.transaction_id = None
                    self.exploratory_linktrace_reply = YList()
                    self.exploratory_linktrace_reply.parent = self
                    self.exploratory_linktrace_reply.name = 'exploratory_linktrace_reply'
                    self.linktrace_reply = YList()
                    self.linktrace_reply.parent = self
                    self.linktrace_reply.name = 'linktrace_reply'
                    self.replies_dropped = None
                    self.traceroute_information = Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation()
                    self.traceroute_information.parent = self


                class TracerouteInformation(object):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\:  str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options>`
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\:  str
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mep_id
                    
                    	Target MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: timestamp
                    
                    	Timestamp of initiation time (seconds)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.directed_mac_address = None
                        self.domain = None
                        self.level = None
                        self.options = Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options()
                        self.options.parent = self
                        self.service = None
                        self.source_interface = None
                        self.source_mac_address = None
                        self.source_mep_id = None
                        self.target_mac_address = None
                        self.target_mep_id = None
                        self.timestamp = None
                        self.transaction_id = None
                        self.ttl = None


                    class Options(object):
                        """
                        Options affecting traceroute behavior
                        
                        .. attribute:: basic_options
                        
                        	Options for a basic IEEE 802.1ag Linktrace
                        	**type**\:   :py:class:`BasicOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\:   :py:class:`ExploratoryOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\:   :py:class:`CfmPmLtModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtModeEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.basic_options = Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self.exploratory_options = Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self.mode = None


                        class BasicOptions(object):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\:  bool
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fdb_only = None
                                self.is_auto = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:basic-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fdb_only is not None:
                                    return True

                                if self.is_auto is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions']['meta_info']


                        class ExploratoryOptions(object):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\:   :py:class:`CfmPmEltDelayModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\:   :py:class:`CfmPmElmReplyFilterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilterEnum>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_constant_factor = None
                                self.delay_model = None
                                self.reply_filter = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.delay_constant_factor is not None:
                                    return True

                                if self.delay_model is not None:
                                    return True

                                if self.reply_filter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.basic_options is not None and self.basic_options._has_data():
                                return True

                            if self.exploratory_options is not None and self.exploratory_options._has_data():
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.directed_mac_address is not None:
                            return True

                        if self.domain is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.options is not None and self.options._has_data():
                            return True

                        if self.service is not None:
                            return True

                        if self.source_interface is not None:
                            return True

                        if self.source_mac_address is not None:
                            return True

                        if self.source_mep_id is not None:
                            return True

                        if self.target_mac_address is not None:
                            return True

                        if self.target_mep_id is not None:
                            return True

                        if self.timestamp is not None:
                            return True

                        if self.transaction_id is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info']


                class LinktraceReply(object):
                    """
                    Received linktrace replies
                    
                    .. attribute:: egress_id
                    
                    	Egress ID TLV
                    	**type**\:   :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId>`
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\:   :py:class:`LastHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop>`
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of    :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\:   :py:class:`ReplyEgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\:   :py:class:`ReplyIngress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\:   :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of    :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId()
                        self.egress_id.parent = self
                        self.header = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header()
                        self.header.parent = self
                        self.last_hop = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self.organization_specific_tlv = YList()
                        self.organization_specific_tlv.parent = self
                        self.organization_specific_tlv.name = 'organization_specific_tlv'
                        self.raw_data = None
                        self.reply_egress = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self.reply_ingress = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self.sender_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self.unknown_tlv = YList()
                        self.unknown_tlv.parent = self
                        self.unknown_tlv.name = 'unknown_tlv'


                    class Header(object):
                        """
                        Frame header
                        
                        .. attribute:: forwarded
                        
                        	LTR was forwarded
                        	**type**\:  bool
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\:   :py:class:`CfmPmRelayActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRelayActionEnum>`
                        
                        .. attribute:: terminal_mep
                        
                        	Terminal MEP reached
                        	**type**\:  bool
                        
                        .. attribute:: transaction_id
                        
                        	Transaction ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ttl
                        
                        	TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: use_fdb_only
                        
                        	Use filtering DB only
                        	**type**\:  bool
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.forwarded = None
                            self.level = None
                            self.relay_action = None
                            self.terminal_mep = None
                            self.transaction_id = None
                            self.ttl = None
                            self.use_fdb_only = None
                            self.version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.forwarded is not None:
                                return True

                            if self.level is not None:
                                return True

                            if self.relay_action is not None:
                                return True

                            if self.terminal_mep is not None:
                                return True

                            if self.transaction_id is not None:
                                return True

                            if self.ttl is not None:
                                return True

                            if self.use_fdb_only is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header']['meta_info']


                    class SenderId(object):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\:   :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.chassis_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self.management_address = None
                            self.management_address_domain = None


                        class ChassisId(object):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\:   :py:class:`CfmPmChassisIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\:   :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self


                            class ChassisIdValue(object):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id_format = None
                                    self.chassis_id_mac = None
                                    self.chassis_id_raw = None
                                    self.chassis_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id_format is not None:
                                        return True

                                    if self.chassis_id_mac is not None:
                                        return True

                                    if self.chassis_id_raw is not None:
                                        return True

                                    if self.chassis_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None:
                                    return True

                                if self.chassis_id_type is not None:
                                    return True

                                if self.chassis_id_type_value is not None:
                                    return True

                                if self.chassis_id_value is not None and self.chassis_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.chassis_id is not None and self.chassis_id._has_data():
                                return True

                            if self.management_address is not None:
                                return True

                            if self.management_address_domain is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info']


                    class EgressId(object):
                        """
                        Egress ID TLV
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\:   :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId>`
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\:   :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.last_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId()
                            self.last_egress_id.parent = self
                            self.next_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId()
                            self.next_egress_id.parent = self


                        class LastEgressId(object):
                            """
                            Last egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.last_egress_id is not None and self.last_egress_id._has_data():
                                return True

                            if self.next_egress_id is not None and self.next_egress_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']


                    class ReplyIngress(object):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: action
                        
                        	Reply ingress action
                        	**type**\:   :py:class:`CfmPmIngressActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIngressActionEnum>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:   :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.mac_address = None
                            self.port_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:   :py:class:`CfmPmPortIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:   :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.port_id_format = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self.port_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.port_id_format is not None:
                                        return True

                                    if self.port_id_mac is not None:
                                        return True

                                    if self.port_id_raw is not None:
                                        return True

                                    if self.port_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.port_id is not None:
                                    return True

                                if self.port_id_type is not None:
                                    return True

                                if self.port_id_type_value is not None:
                                    return True

                                if self.port_id_value is not None and self.port_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-ingress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info']


                    class ReplyEgress(object):
                        """
                        Reply egress TLV
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\:   :py:class:`CfmPmEgressActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEgressActionEnum>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:   :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.mac_address = None
                            self.port_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:   :py:class:`CfmPmPortIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:   :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.port_id_format = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self.port_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.port_id_format is not None:
                                        return True

                                    if self.port_id_mac is not None:
                                        return True

                                    if self.port_id_raw is not None:
                                        return True

                                    if self.port_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.port_id is not None:
                                    return True

                                if self.port_id_type is not None:
                                    return True

                                if self.port_id_type_value is not None:
                                    return True

                                if self.port_id_value is not None and self.port_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-egress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info']


                    class LastHop(object):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\:   :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\:  str
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\:   :py:class:`CfmPmLastHopFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmtEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self.host_name = None
                            self.last_hop_format = None


                        class EgressId(object):
                            """
                            Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.egress_id is not None and self.egress_id._has_data():
                                return True

                            if self.host_name is not None:
                                return True

                            if self.last_hop_format is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info']


                    class OrganizationSpecificTlv(object):
                        """
                        Organizational\-specific TLVs
                        
                        .. attribute:: oui
                        
                        	Organizationally\-unique ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: subtype
                        
                        	Subtype of TLV
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.oui = None
                            self.subtype = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.oui is not None:
                                return True

                            if self.subtype is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv']['meta_info']


                    class UnknownTlv(object):
                        """
                        Unknown TLVs
                        
                        .. attribute:: typecode
                        
                        	Type code of TLV
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.typecode = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.typecode is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:linktrace-reply'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.egress_id is not None and self.egress_id._has_data():
                            return True

                        if self.header is not None and self.header._has_data():
                            return True

                        if self.last_hop is not None and self.last_hop._has_data():
                            return True

                        if self.organization_specific_tlv is not None:
                            for child_ref in self.organization_specific_tlv:
                                if child_ref._has_data():
                                    return True

                        if self.raw_data is not None:
                            return True

                        if self.reply_egress is not None and self.reply_egress._has_data():
                            return True

                        if self.reply_ingress is not None and self.reply_ingress._has_data():
                            return True

                        if self.sender_id is not None and self.sender_id._has_data():
                            return True

                        if self.unknown_tlv is not None:
                            for child_ref in self.unknown_tlv:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']


                class ExploratoryLinktraceReply(object):
                    """
                    Received exploratory linktrace replies
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\:   :py:class:`LastHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop>`
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of    :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\:   :py:class:`ReplyEgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\:   :py:class:`ReplyIngress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\:   :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of    :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.header = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header()
                        self.header.parent = self
                        self.last_hop = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self.organization_specific_tlv = YList()
                        self.organization_specific_tlv.parent = self
                        self.organization_specific_tlv.name = 'organization_specific_tlv'
                        self.raw_data = None
                        self.reply_egress = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self.reply_ingress = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self.sender_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self.unknown_tlv = YList()
                        self.unknown_tlv.parent = self
                        self.unknown_tlv.name = 'unknown_tlv'


                    class Header(object):
                        """
                        Frame header
                        
                        .. attribute:: delay_model
                        
                        	Delay Model
                        	**type**\:   :py:class:`CfmPmEltDelayModelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                        
                        .. attribute:: forwarded
                        
                        	ELR was forwarded
                        	**type**\:  bool
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: next_hop_timeout
                        
                        	Next Hop Timeout, in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\:   :py:class:`CfmPmElrRelayActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrRelayActionEnum>`
                        
                        .. attribute:: reply_filter_unknown
                        
                        	Reply Filter unrecognized
                        	**type**\:  bool
                        
                        .. attribute:: terminal_mep
                        
                        	Terminal MEP reached
                        	**type**\:  bool
                        
                        .. attribute:: transaction_id
                        
                        	Transaction ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ttl
                        
                        	TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.delay_model = None
                            self.forwarded = None
                            self.level = None
                            self.next_hop_timeout = None
                            self.relay_action = None
                            self.reply_filter_unknown = None
                            self.terminal_mep = None
                            self.transaction_id = None
                            self.ttl = None
                            self.version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.delay_model is not None:
                                return True

                            if self.forwarded is not None:
                                return True

                            if self.level is not None:
                                return True

                            if self.next_hop_timeout is not None:
                                return True

                            if self.relay_action is not None:
                                return True

                            if self.reply_filter_unknown is not None:
                                return True

                            if self.terminal_mep is not None:
                                return True

                            if self.transaction_id is not None:
                                return True

                            if self.ttl is not None:
                                return True

                            if self.version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header']['meta_info']


                    class SenderId(object):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\:   :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.chassis_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self.management_address = None
                            self.management_address_domain = None


                        class ChassisId(object):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\:   :py:class:`CfmPmChassisIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\:   :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self


                            class ChassisIdValue(object):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id_format = None
                                    self.chassis_id_mac = None
                                    self.chassis_id_raw = None
                                    self.chassis_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id_format is not None:
                                        return True

                                    if self.chassis_id_mac is not None:
                                        return True

                                    if self.chassis_id_raw is not None:
                                        return True

                                    if self.chassis_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None:
                                    return True

                                if self.chassis_id_type is not None:
                                    return True

                                if self.chassis_id_type_value is not None:
                                    return True

                                if self.chassis_id_value is not None and self.chassis_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.chassis_id is not None and self.chassis_id._has_data():
                                return True

                            if self.management_address is not None:
                                return True

                            if self.management_address_domain is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info']


                    class ReplyIngress(object):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: action
                        
                        	ELR Reply ingress action
                        	**type**\:   :py:class:`CfmPmElrIngressActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrIngressActionEnum>`
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\:   :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\:   :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:   :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.last_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId()
                            self.last_egress_id.parent = self
                            self.mac_address = None
                            self.next_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId()
                            self.next_egress_id.parent = self
                            self.port_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self


                        class LastEgressId(object):
                            """
                            Last egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId']['meta_info']


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:   :py:class:`CfmPmPortIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:   :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.port_id_format = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self.port_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.port_id_format is not None:
                                        return True

                                    if self.port_id_mac is not None:
                                        return True

                                    if self.port_id_raw is not None:
                                        return True

                                    if self.port_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.port_id is not None:
                                    return True

                                if self.port_id_type is not None:
                                    return True

                                if self.port_id_type_value is not None:
                                    return True

                                if self.port_id_value is not None and self.port_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-ingress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.last_egress_id is not None and self.last_egress_id._has_data():
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.next_egress_id is not None and self.next_egress_id._has_data():
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']


                    class ReplyEgress(object):
                        """
                        Reply egress TLV
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\:   :py:class:`CfmPmElrEgressActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrEgressActionEnum>`
                        
                        .. attribute:: last_egress_id
                        
                        	Last Egress ID
                        	**type**\:   :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address of egress interface
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: next_egress_id
                        
                        	Next Egress ID
                        	**type**\:   :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:   :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.last_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId()
                            self.last_egress_id.parent = self
                            self.mac_address = None
                            self.next_egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId()
                            self.next_egress_id.parent = self
                            self.port_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self


                        class LastEgressId(object):
                            """
                            Last Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId']['meta_info']


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:   :py:class:`CfmPmPortIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:   :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.port_id_format = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self.port_id_string = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.port_id_format is not None:
                                        return True

                                    if self.port_id_mac is not None:
                                        return True

                                    if self.port_id_raw is not None:
                                        return True

                                    if self.port_id_string is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.port_id is not None:
                                    return True

                                if self.port_id_type is not None:
                                    return True

                                if self.port_id_type_value is not None:
                                    return True

                                if self.port_id_value is not None and self.port_id_value._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-egress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.last_egress_id is not None and self.last_egress_id._has_data():
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.next_egress_id is not None and self.next_egress_id._has_data():
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']


                    class LastHop(object):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\:   :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\:  str
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\:   :py:class:`CfmPmLastHopFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmtEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.egress_id = Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self.host_name = None
                            self.last_hop_format = None


                        class EgressId(object):
                            """
                            Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mac_address = None
                                self.unique_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.egress_id is not None and self.egress_id._has_data():
                                return True

                            if self.host_name is not None:
                                return True

                            if self.last_hop_format is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info']


                    class OrganizationSpecificTlv(object):
                        """
                        Organizational\-specific TLVs
                        
                        .. attribute:: oui
                        
                        	Organizationally\-unique ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: subtype
                        
                        	Subtype of TLV
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.oui = None
                            self.subtype = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.oui is not None:
                                return True

                            if self.subtype is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv']['meta_info']


                    class UnknownTlv(object):
                        """
                        Unknown TLVs
                        
                        .. attribute:: typecode
                        
                        	Type code of TLV
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.typecode = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.typecode is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-linktrace-reply'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.header is not None and self.header._has_data():
                            return True

                        if self.last_hop is not None and self.last_hop._has_data():
                            return True

                        if self.organization_specific_tlv is not None:
                            for child_ref in self.organization_specific_tlv:
                                if child_ref._has_data():
                                    return True

                        if self.raw_data is not None:
                            return True

                        if self.reply_egress is not None and self.reply_egress._has_data():
                            return True

                        if self.reply_ingress is not None and self.reply_ingress._has_data():
                            return True

                        if self.sender_id is not None and self.sender_id._has_data():
                            return True

                        if self.unknown_tlv is not None:
                            for child_ref in self.unknown_tlv:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.mep_id is None:
                        raise YPYModelError('Key property mep_id is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')
                    if self.transaction_id is None:
                        raise YPYModelError('Key property transaction_id is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-caches/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-cache[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:transaction-id = ' + str(self.transaction_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.transaction_id is not None:
                        return True

                    if self.exploratory_linktrace_reply is not None:
                        for child_ref in self.exploratory_linktrace_reply:
                            if child_ref._has_data():
                                return True

                    if self.linktrace_reply is not None:
                        for child_ref in self.linktrace_reply:
                            if child_ref._has_data():
                                return True

                    if self.replies_dropped is not None:
                        return True

                    if self.traceroute_information is not None and self.traceroute_information._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-caches'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.traceroute_cache is not None:
                    for child_ref in self.traceroute_cache:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.TracerouteCaches']['meta_info']


        class LocalMeps(object):
            """
            Local MEPs table
            
            .. attribute:: local_mep
            
            	Information about a particular local MEP
            	**type**\: list of    :py:class:`LocalMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.local_mep = YList()
                self.local_mep.parent = self
                self.local_mep.name = 'local_mep'


            class LocalMep(object):
                """
                Information about a particular local MEP
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  <key>
                
                	MEP ID
                	**type**\:  int
                
                	**range:** 1..8191
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: ais_statistics
                
                	MEP AIS statistics
                	**type**\:   :py:class:`AisStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.AisStatistics>`
                
                .. attribute:: ccm_generation_enabled
                
                	CCM generation enabled
                	**type**\:  bool
                
                .. attribute:: ccm_interval
                
                	The interval between CCMs
                	**type**\:   :py:class:`CfmBagCcmIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                
                .. attribute:: ccm_offload
                
                	Offload status of CCM processing
                	**type**\:   :py:class:`CfmBagCcmOffloadEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffloadEnum>`
                
                .. attribute:: cos
                
                	CoS bits the MEP will use for sent packets, if configured
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: cross_connect_ccm_defect
                
                	A cross\-connect CCM error has been reported
                	**type**\:  bool
                
                .. attribute:: defects
                
                	Defects detected from peer MEPs
                	**type**\:   :py:class:`Defects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.Defects>`
                
                .. attribute:: defects_ignored
                
                	Defects present but ignored due to 'report defects' configuration
                	**type**\:  bool
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\:  str
                
                .. attribute:: efd_triggered
                
                	EFD triggered on the interface
                	**type**\:  bool
                
                .. attribute:: error_ccm_defect
                
                	A CCM error has been reported
                	**type**\:  bool
                
                .. attribute:: fault_notification_state
                
                	Fault Notification Generation state
                	**type**\:   :py:class:`CfmPmMepFngStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepFngStateEnum>`
                
                .. attribute:: hairpin
                
                	MEP is on a sub\-interface in the same bridge\-domain and on the same trunk interface as another sub\-interface
                	**type**\:  bool
                
                .. attribute:: highest_defect
                
                	Highest\-priority defect present since last FNG reset
                	**type**\:   :py:class:`CfmPmMepDefectEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepDefectEnum>`
                
                .. attribute:: interface_state
                
                	IM Interface state
                	**type**\:  str
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interworking_state
                
                	Interface interworking state
                	**type**\:   :py:class:`CfmBagIwStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwStateEnum>`
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mac_status_defect
                
                	A peer MEP port or interface status error has been reported
                	**type**\:  bool
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\:   :py:class:`CfmBagDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                
                .. attribute:: mep_id_xr
                
                	MEP ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: next_lbm_id
                
                	Next Transaction ID to be sent in a Loopback Message
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_ltm_id
                
                	Next Transaction ID to be sent in a Linktrace Message
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_mep_ccm_defect
                
                	A peer MEP CCM error has been reported
                	**type**\:  bool
                
                .. attribute:: peer_meps_detected
                
                	Number of peer MEPs detected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_with_errors_detected
                
                	Number of peer MEPs detected with errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rdi_defect
                
                	A peer MEP RDI defect has been reported
                	**type**\:  bool
                
                .. attribute:: remote_defect
                
                	Remote defect indicated
                	**type**\:  bool
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\:  str
                
                .. attribute:: standby
                
                	The local MEP is on an interface in standby mode
                	**type**\:  bool
                
                .. attribute:: statistics
                
                	MEP statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.Statistics>`
                
                .. attribute:: stp_state
                
                	STP state
                	**type**\:   :py:class:`CfmBagStpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpStateEnum>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.ais_statistics = Cfm.Global_.LocalMeps.LocalMep.AisStatistics()
                    self.ais_statistics.parent = self
                    self.ccm_generation_enabled = None
                    self.ccm_interval = None
                    self.ccm_offload = None
                    self.cos = None
                    self.cross_connect_ccm_defect = None
                    self.defects = Cfm.Global_.LocalMeps.LocalMep.Defects()
                    self.defects.parent = self
                    self.defects_ignored = None
                    self.domain_xr = None
                    self.efd_triggered = None
                    self.error_ccm_defect = None
                    self.fault_notification_state = None
                    self.hairpin = None
                    self.highest_defect = None
                    self.interface_state = None
                    self.interface_xr = None
                    self.interworking_state = None
                    self.level = None
                    self.mac_address = None
                    self.mac_status_defect = None
                    self.mep_direction = None
                    self.mep_id_xr = None
                    self.next_lbm_id = None
                    self.next_ltm_id = None
                    self.peer_mep_ccm_defect = None
                    self.peer_meps_detected = None
                    self.peer_meps_with_errors_detected = None
                    self.rdi_defect = None
                    self.remote_defect = None
                    self.service_xr = None
                    self.standby = None
                    self.statistics = Cfm.Global_.LocalMeps.LocalMep.Statistics()
                    self.statistics.parent = self
                    self.stp_state = None


                class Statistics(object):
                    """
                    MEP statistics
                    
                    .. attribute:: ai_ss_received
                    
                    	Number of AIS messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ai_ss_sent
                    
                    	Number of AIS messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_discarded
                    
                    	Number of BNM messages discarded
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_received
                    
                    	Number of BNM messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_discarded
                    
                    	Number of CCMs discarded because maximum MEPs limit was reached
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_out_of_sequence
                    
                    	Number of CCMs received out\-of\-sequence
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_received
                    
                    	Number of CCMs received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_sent
                    
                    	Number of CCMs sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_received
                    
                    	Number of DMM messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_sent
                    
                    	Number of DMM messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_received
                    
                    	Number of DMR messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_sent
                    
                    	Number of DMR messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_received
                    
                    	Number of LBMs received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_sent
                    
                    	Number of LBMs sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_bad_data
                    
                    	Number of LBRs received with non\-matching user\-specified data
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_out_of_sequence
                    
                    	Number of LBRs received out\-of\-sequence
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_received
                    
                    	Number of LBRs received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_sent
                    
                    	Number of LBRs sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lc_ks_received
                    
                    	Number of LCK messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_received
                    
                    	Number of LMM messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_sent
                    
                    	Number of LMM messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_received
                    
                    	Number of LMR messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_sent
                    
                    	Number of LMR messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lt_rs_received_unexpected
                    
                    	Number of unexpected LTRs received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_received
                    
                    	Number of SLM messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_sent
                    
                    	Number of SLM messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_received
                    
                    	Number of SLR messages received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_sent
                    
                    	Number of SLR messages sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ai_ss_received = None
                        self.ai_ss_sent = None
                        self.bn_ms_discarded = None
                        self.bn_ms_received = None
                        self.ccms_discarded = None
                        self.ccms_out_of_sequence = None
                        self.ccms_received = None
                        self.ccms_sent = None
                        self.dm_ms_received = None
                        self.dm_ms_sent = None
                        self.dm_rs_received = None
                        self.dm_rs_sent = None
                        self.lb_ms_received = None
                        self.lb_ms_sent = None
                        self.lb_rs_bad_data = None
                        self.lb_rs_out_of_sequence = None
                        self.lb_rs_received = None
                        self.lb_rs_sent = None
                        self.lc_ks_received = None
                        self.lm_ms_received = None
                        self.lm_ms_sent = None
                        self.lm_rs_received = None
                        self.lm_rs_sent = None
                        self.lt_rs_received_unexpected = None
                        self.sl_ms_received = None
                        self.sl_ms_sent = None
                        self.sl_rs_received = None
                        self.sl_rs_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ai_ss_received is not None:
                            return True

                        if self.ai_ss_sent is not None:
                            return True

                        if self.bn_ms_discarded is not None:
                            return True

                        if self.bn_ms_received is not None:
                            return True

                        if self.ccms_discarded is not None:
                            return True

                        if self.ccms_out_of_sequence is not None:
                            return True

                        if self.ccms_received is not None:
                            return True

                        if self.ccms_sent is not None:
                            return True

                        if self.dm_ms_received is not None:
                            return True

                        if self.dm_ms_sent is not None:
                            return True

                        if self.dm_rs_received is not None:
                            return True

                        if self.dm_rs_sent is not None:
                            return True

                        if self.lb_ms_received is not None:
                            return True

                        if self.lb_ms_sent is not None:
                            return True

                        if self.lb_rs_bad_data is not None:
                            return True

                        if self.lb_rs_out_of_sequence is not None:
                            return True

                        if self.lb_rs_received is not None:
                            return True

                        if self.lb_rs_sent is not None:
                            return True

                        if self.lc_ks_received is not None:
                            return True

                        if self.lm_ms_received is not None:
                            return True

                        if self.lm_ms_sent is not None:
                            return True

                        if self.lm_rs_received is not None:
                            return True

                        if self.lm_rs_sent is not None:
                            return True

                        if self.lt_rs_received_unexpected is not None:
                            return True

                        if self.sl_ms_received is not None:
                            return True

                        if self.sl_ms_sent is not None:
                            return True

                        if self.sl_rs_received is not None:
                            return True

                        if self.sl_rs_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.Statistics']['meta_info']


                class AisStatistics(object):
                    """
                    MEP AIS statistics
                    
                    .. attribute:: interval
                    
                    	AIS transmission interval
                    	**type**\:   :py:class:`CfmBagAisIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                    
                    .. attribute:: last_interval
                    
                    	The interval of the last received AIS packet
                    	**type**\:   :py:class:`CfmBagAisIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                    
                    .. attribute:: last_mac_address
                    
                    	Source MAC address of the last received AIS packet
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: level
                    
                    	AIS transmission level
                    	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: receiving_ais
                    
                    	Details of how the signal is being received
                    	**type**\:   :py:class:`CfmPmAisReceiveEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisReceiveEnum>`
                    
                    .. attribute:: receiving_start
                    
                    	Time elapsed since AIS receiving started
                    	**type**\:   :py:class:`ReceivingStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart>`
                    
                    .. attribute:: sending_ais
                    
                    	Details of how AIS is being transmitted
                    	**type**\:   :py:class:`CfmPmAisTransmitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisTransmitEnum>`
                    
                    .. attribute:: sending_start
                    
                    	Time elapsed since AIS sending started
                    	**type**\:   :py:class:`SendingStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interval = None
                        self.last_interval = None
                        self.last_mac_address = None
                        self.level = None
                        self.receiving_ais = None
                        self.receiving_start = Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart()
                        self.receiving_start.parent = self
                        self.sending_ais = None
                        self.sending_start = Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart()
                        self.sending_start.parent = self


                    class SendingStart(object):
                        """
                        Time elapsed since AIS sending started
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sending-start'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart']['meta_info']


                    class ReceivingStart(object):
                        """
                        Time elapsed since AIS receiving started
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:receiving-start'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ais-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interval is not None:
                            return True

                        if self.last_interval is not None:
                            return True

                        if self.last_mac_address is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.receiving_ais is not None:
                            return True

                        if self.receiving_start is not None and self.receiving_start._has_data():
                            return True

                        if self.sending_ais is not None:
                            return True

                        if self.sending_start is not None and self.sending_start._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics']['meta_info']


                class Defects(object):
                    """
                    Defects detected from peer MEPs
                    
                    .. attribute:: ais_received
                    
                    	AIS or LCK received
                    	**type**\:  bool
                    
                    .. attribute:: auto_missing
                    
                    	Number of missing auto cross\-check MEPs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_port_status
                    
                    	The local port or interface is down
                    	**type**\:  bool
                    
                    .. attribute:: missing
                    
                    	Number of missing peer MEPs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_meps_that_timed_out
                    
                    	Number of peer MEPs that have timed out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_port_status
                    
                    	A peer port or interface is down
                    	**type**\:  bool
                    
                    .. attribute:: remote_meps_defects
                    
                    	Defects detected from remote MEPs
                    	**type**\:   :py:class:`RemoteMepsDefects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects>`
                    
                    .. attribute:: unexpected
                    
                    	Number of unexpected peer MEPs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ais_received = None
                        self.auto_missing = None
                        self.local_port_status = None
                        self.missing = None
                        self.peer_meps_that_timed_out = None
                        self.peer_port_status = None
                        self.remote_meps_defects = Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects()
                        self.remote_meps_defects.parent = self
                        self.unexpected = None


                    class RemoteMepsDefects(object):
                        """
                        Defects detected from remote MEPs
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\:  bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\:  bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\:  bool
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
                        	**type**\:  bool
                        
                        .. attribute:: received_our_mac
                        
                        	Loop detected (our MAC address received)
                        	**type**\:  bool
                        
                        .. attribute:: received_our_mep_id
                        
                        	Configuration Error (our MEP ID received)
                        	**type**\:  bool
                        
                        .. attribute:: received_rdi
                        
                        	Remote defection indication received
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.invalid_ccm_interval = None
                            self.invalid_level = None
                            self.invalid_maid = None
                            self.loss_threshold_exceeded = None
                            self.received_our_mac = None
                            self.received_our_mep_id = None
                            self.received_rdi = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:remote-meps-defects'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.invalid_ccm_interval is not None:
                                return True

                            if self.invalid_level is not None:
                                return True

                            if self.invalid_maid is not None:
                                return True

                            if self.loss_threshold_exceeded is not None:
                                return True

                            if self.received_our_mac is not None:
                                return True

                            if self.received_our_mep_id is not None:
                                return True

                            if self.received_rdi is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:defects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ais_received is not None:
                            return True

                        if self.auto_missing is not None:
                            return True

                        if self.local_port_status is not None:
                            return True

                        if self.missing is not None:
                            return True

                        if self.peer_meps_that_timed_out is not None:
                            return True

                        if self.peer_port_status is not None:
                            return True

                        if self.remote_meps_defects is not None and self.remote_meps_defects._has_data():
                            return True

                        if self.unexpected is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep.Defects']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.mep_id is None:
                        raise YPYModelError('Key property mep_id is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:local-meps/Cisco-IOS-XR-ethernet-cfm-oper:local-mep[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.ais_statistics is not None and self.ais_statistics._has_data():
                        return True

                    if self.ccm_generation_enabled is not None:
                        return True

                    if self.ccm_interval is not None:
                        return True

                    if self.ccm_offload is not None:
                        return True

                    if self.cos is not None:
                        return True

                    if self.cross_connect_ccm_defect is not None:
                        return True

                    if self.defects is not None and self.defects._has_data():
                        return True

                    if self.defects_ignored is not None:
                        return True

                    if self.domain_xr is not None:
                        return True

                    if self.efd_triggered is not None:
                        return True

                    if self.error_ccm_defect is not None:
                        return True

                    if self.fault_notification_state is not None:
                        return True

                    if self.hairpin is not None:
                        return True

                    if self.highest_defect is not None:
                        return True

                    if self.interface_state is not None:
                        return True

                    if self.interface_xr is not None:
                        return True

                    if self.interworking_state is not None:
                        return True

                    if self.level is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.mac_status_defect is not None:
                        return True

                    if self.mep_direction is not None:
                        return True

                    if self.mep_id_xr is not None:
                        return True

                    if self.next_lbm_id is not None:
                        return True

                    if self.next_ltm_id is not None:
                        return True

                    if self.peer_mep_ccm_defect is not None:
                        return True

                    if self.peer_meps_detected is not None:
                        return True

                    if self.peer_meps_with_errors_detected is not None:
                        return True

                    if self.rdi_defect is not None:
                        return True

                    if self.remote_defect is not None:
                        return True

                    if self.service_xr is not None:
                        return True

                    if self.standby is not None:
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.stp_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.LocalMeps.LocalMep']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:local-meps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_mep is not None:
                    for child_ref in self.local_mep:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.LocalMeps']['meta_info']


        class PeerMePv2S(object):
            """
            Peer MEPs table Version 2
            
            .. attribute:: peer_me_pv2
            
            	Information about a peer MEP for a particular local MEP
            	**type**\: list of    :py:class:`PeerMePv2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.peer_me_pv2 = YList()
                self.peer_me_pv2.parent = self
                self.peer_me_pv2.name = 'peer_me_pv2'


            class PeerMePv2(object):
                """
                Information about a peer MEP for a particular
                local MEP
                
                .. attribute:: domain  <key>
                
                	Maintenance Domain
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: service  <key>
                
                	Service (Maintenance Association)
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: local_mep_id  <key>
                
                	MEP ID of Local MEP
                	**type**\:  int
                
                	**range:** 1..8191
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: peer_mep_id  <key>
                
                	MEP ID of Peer MEP
                	**type**\:  int
                
                	**range:** 1..8191
                
                .. attribute:: peer_mac_address  <key>
                
                	Peer MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\:  str
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\:   :py:class:`CfmBagDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: peer_mep
                
                	Peer MEP
                	**type**\:   :py:class:`PeerMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep>`
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\:  str
                
                .. attribute:: standby
                
                	The local MEP is on an interface in standby mode
                	**type**\:  bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.local_mep_id = None
                    self.interface = None
                    self.peer_mep_id = None
                    self.peer_mac_address = None
                    self.domain_xr = None
                    self.interface_xr = None
                    self.level = None
                    self.mep_direction = None
                    self.mep_id = None
                    self.peer_mep = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep()
                    self.peer_mep.parent = self
                    self.service_xr = None
                    self.standby = None


                class PeerMep(object):
                    """
                    Peer MEP
                    
                    .. attribute:: ccm_offload
                    
                    	Offload status of received CCM handling
                    	**type**\:   :py:class:`CfmBagCcmOffloadEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffloadEnum>`
                    
                    .. attribute:: cross_check_state
                    
                    	Cross\-check state
                    	**type**\:   :py:class:`CfmPmRmepXcStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepXcStateEnum>`
                    
                    .. attribute:: error_state
                    
                    	Error state
                    	**type**\:   :py:class:`ErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState>`
                    
                    .. attribute:: last_ccm_received
                    
                    	Last CCM received from the peer MEP
                    	**type**\:   :py:class:`LastCcmReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived>`
                    
                    .. attribute:: last_up_down_time
                    
                    	Elapsed time since peer MEP became active or timed out
                    	**type**\:   :py:class:`LastUpDownTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime>`
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: peer_mep_state
                    
                    	State of the peer MEP state machine
                    	**type**\:   :py:class:`CfmPmRmepStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepStateEnum>`
                    
                    .. attribute:: statistics
                    
                    	Peer MEP statistics
                    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ccm_offload = None
                        self.cross_check_state = None
                        self.error_state = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState()
                        self.error_state.parent = self
                        self.last_ccm_received = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived()
                        self.last_ccm_received.parent = self
                        self.last_up_down_time = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime()
                        self.last_up_down_time.parent = self
                        self.mac_address = None
                        self.mep_id = None
                        self.peer_mep_state = None
                        self.statistics = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics()
                        self.statistics.parent = self


                    class ErrorState(object):
                        """
                        Error state
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\:  bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\:  bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\:  bool
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
                        	**type**\:  bool
                        
                        .. attribute:: received_our_mac
                        
                        	Loop detected (our MAC address received)
                        	**type**\:  bool
                        
                        .. attribute:: received_our_mep_id
                        
                        	Configuration Error (our MEP ID received)
                        	**type**\:  bool
                        
                        .. attribute:: received_rdi
                        
                        	Remote defection indication received
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.invalid_ccm_interval = None
                            self.invalid_level = None
                            self.invalid_maid = None
                            self.loss_threshold_exceeded = None
                            self.received_our_mac = None
                            self.received_our_mep_id = None
                            self.received_rdi = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:error-state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.invalid_ccm_interval is not None:
                                return True

                            if self.invalid_level is not None:
                                return True

                            if self.invalid_maid is not None:
                                return True

                            if self.loss_threshold_exceeded is not None:
                                return True

                            if self.received_our_mac is not None:
                                return True

                            if self.received_our_mep_id is not None:
                                return True

                            if self.received_rdi is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState']['meta_info']


                    class LastUpDownTime(object):
                        """
                        Elapsed time since peer MEP became active or
                        timed out
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nanoseconds = None
                            self.seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-up-down-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime']['meta_info']


                    class LastCcmReceived(object):
                        """
                        Last CCM received from the peer MEP
                        
                        .. attribute:: additional_interface_status
                        
                        	Additional interface status
                        	**type**\:   :py:class:`CfmPmAddlIntfStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAddlIntfStatusEnum>`
                        
                        .. attribute:: header
                        
                        	Frame header
                        	**type**\:   :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header>`
                        
                        .. attribute:: interface_status
                        
                        	Interface status
                        	**type**\:   :py:class:`CfmPmIntfStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIntfStatusEnum>`
                        
                        .. attribute:: mep_name
                        
                        	MEP name
                        	**type**\:   :py:class:`MepName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName>`
                        
                        .. attribute:: organization_specific_tlv
                        
                        	Organizational\-specific TLVs
                        	**type**\: list of    :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv>`
                        
                        .. attribute:: port_status
                        
                        	Port status
                        	**type**\:   :py:class:`CfmPmPortStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortStatusEnum>`
                        
                        .. attribute:: raw_data
                        
                        	Undecoded frame
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: sender_id
                        
                        	Sender ID TLV
                        	**type**\:   :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId>`
                        
                        .. attribute:: unknown_tlv
                        
                        	Unknown TLVs
                        	**type**\: list of    :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.additional_interface_status = None
                            self.header = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header()
                            self.header.parent = self
                            self.interface_status = None
                            self.mep_name = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName()
                            self.mep_name.parent = self
                            self.organization_specific_tlv = YList()
                            self.organization_specific_tlv.parent = self
                            self.organization_specific_tlv.name = 'organization_specific_tlv'
                            self.port_status = None
                            self.raw_data = None
                            self.sender_id = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId()
                            self.sender_id.parent = self
                            self.unknown_tlv = YList()
                            self.unknown_tlv.parent = self
                            self.unknown_tlv.name = 'unknown_tlv'


                        class Header(object):
                            """
                            Frame header
                            
                            .. attribute:: interval
                            
                            	CCM interval
                            	**type**\:   :py:class:`CfmBagCcmIntervalEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                            
                            .. attribute:: level
                            
                            	MD level
                            	**type**\:   :py:class:`CfmBagMdLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                            
                            .. attribute:: mdid
                            
                            	MDID
                            	**type**\:   :py:class:`Mdid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid>`
                            
                            .. attribute:: mdid_format
                            
                            	MDID Format
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mep_id
                            
                            	MEP ID
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rdi
                            
                            	Remote defect indicated
                            	**type**\:  bool
                            
                            .. attribute:: sequence_number
                            
                            	CCM sequence number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: short_ma_name
                            
                            	Short MA Name
                            	**type**\:   :py:class:`ShortMaName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName>`
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name format
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interval = None
                                self.level = None
                                self.mdid = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid()
                                self.mdid.parent = self
                                self.mdid_format = None
                                self.mep_id = None
                                self.rdi = None
                                self.sequence_number = None
                                self.short_ma_name = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName()
                                self.short_ma_name.parent = self
                                self.short_ma_name_format = None
                                self.version = None


                            class Mdid(object):
                                """
                                MDID
                                
                                .. attribute:: dns_like_name
                                
                                	DNS\-like name
                                	**type**\:  str
                                
                                .. attribute:: mac_name
                                
                                	MAC address name
                                	**type**\:   :py:class:`MacName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName>`
                                
                                .. attribute:: mdid_data
                                
                                	Hex data
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: mdid_format_value
                                
                                	MDIDFormatValue
                                	**type**\:   :py:class:`CfmBagMdidFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdidFmtEnum>`
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dns_like_name = None
                                    self.mac_name = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName()
                                    self.mac_name.parent = self
                                    self.mdid_data = None
                                    self.mdid_format_value = None
                                    self.string_name = None


                                class MacName(object):
                                    """
                                    MAC address name
                                    
                                    .. attribute:: integer
                                    
                                    	Integer
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.integer = None
                                        self.mac_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mac-name'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.integer is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mdid'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.dns_like_name is not None:
                                        return True

                                    if self.mac_name is not None and self.mac_name._has_data():
                                        return True

                                    if self.mdid_data is not None:
                                        return True

                                    if self.mdid_format_value is not None:
                                        return True

                                    if self.string_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid']['meta_info']


                            class ShortMaName(object):
                                """
                                Short MA Name
                                
                                .. attribute:: icc_based
                                
                                	ICC\-based format
                                	**type**\:  str
                                
                                .. attribute:: integer_name
                                
                                	Unsigned integer name
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: short_ma_name_data
                                
                                	Hex data
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: short_ma_name_format_value
                                
                                	ShortMANameFormatValue
                                	**type**\:   :py:class:`CfmBagSmanFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagSmanFmtEnum>`
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\:  str
                                
                                .. attribute:: vlan_id_name
                                
                                	VLAN ID name
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: vpn_id_name
                                
                                	VPN ID name
                                	**type**\:   :py:class:`VpnIdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.icc_based = None
                                    self.integer_name = None
                                    self.short_ma_name_data = None
                                    self.short_ma_name_format_value = None
                                    self.string_name = None
                                    self.vlan_id_name = None
                                    self.vpn_id_name = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName()
                                    self.vpn_id_name.parent = self


                                class VpnIdName(object):
                                    """
                                    VPN ID name
                                    
                                    .. attribute:: index
                                    
                                    	VPN index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: oui
                                    
                                    	VPN authority organizationally\-unique ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.index = None
                                        self.oui = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:vpn-id-name'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.index is not None:
                                            return True

                                        if self.oui is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:short-ma-name'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.icc_based is not None:
                                        return True

                                    if self.integer_name is not None:
                                        return True

                                    if self.short_ma_name_data is not None:
                                        return True

                                    if self.short_ma_name_format_value is not None:
                                        return True

                                    if self.string_name is not None:
                                        return True

                                    if self.vlan_id_name is not None:
                                        return True

                                    if self.vpn_id_name is not None and self.vpn_id_name._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interval is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.mdid is not None and self.mdid._has_data():
                                    return True

                                if self.mdid_format is not None:
                                    return True

                                if self.mep_id is not None:
                                    return True

                                if self.rdi is not None:
                                    return True

                                if self.sequence_number is not None:
                                    return True

                                if self.short_ma_name is not None and self.short_ma_name._has_data():
                                    return True

                                if self.short_ma_name_format is not None:
                                    return True

                                if self.version is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header']['meta_info']


                        class SenderId(object):
                            """
                            Sender ID TLV
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID
                            	**type**\:   :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId>`
                            
                            .. attribute:: management_address
                            
                            	Management address
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: management_address_domain
                            
                            	Management address domain
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId()
                                self.chassis_id.parent = self
                                self.management_address = None
                                self.management_address_domain = None


                            class ChassisId(object):
                                """
                                Chassis ID
                                
                                .. attribute:: chassis_id
                                
                                	Chassis ID (Deprecated)
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_type
                                
                                	Chassis ID Type
                                	**type**\:   :py:class:`CfmPmChassisIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                                
                                .. attribute:: chassis_id_type_value
                                
                                	Chassis ID Type
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id_value
                                
                                	Chassis ID (Current)
                                	**type**\:   :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id = None
                                    self.chassis_id_type = None
                                    self.chassis_id_type_value = None
                                    self.chassis_id_value = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue()
                                    self.chassis_id_value.parent = self


                                class ChassisIdValue(object):
                                    """
                                    Chassis ID (Current)
                                    
                                    .. attribute:: chassis_id_format
                                    
                                    	ChassisIDFormat
                                    	**type**\:   :py:class:`CfmPmIdFmtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                    
                                    .. attribute:: chassis_id_mac
                                    
                                    	Chassis ID MAC Address
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: chassis_id_raw
                                    
                                    	Raw Chassis ID
                                    	**type**\:  str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    .. attribute:: chassis_id_string
                                    
                                    	Chassis ID String
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.chassis_id_format = None
                                        self.chassis_id_mac = None
                                        self.chassis_id_raw = None
                                        self.chassis_id_string = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.chassis_id_format is not None:
                                            return True

                                        if self.chassis_id_mac is not None:
                                            return True

                                        if self.chassis_id_raw is not None:
                                            return True

                                        if self.chassis_id_string is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.chassis_id is not None:
                                        return True

                                    if self.chassis_id_type is not None:
                                        return True

                                    if self.chassis_id_type_value is not None:
                                        return True

                                    if self.chassis_id_value is not None and self.chassis_id_value._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.chassis_id is not None and self.chassis_id._has_data():
                                    return True

                                if self.management_address is not None:
                                    return True

                                if self.management_address_domain is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId']['meta_info']


                        class MepName(object):
                            """
                            MEP name
                            
                            .. attribute:: name
                            
                            	MEP name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mep-name'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName']['meta_info']


                        class OrganizationSpecificTlv(object):
                            """
                            Organizational\-specific TLVs
                            
                            .. attribute:: oui
                            
                            	Organizationally\-unique ID
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: subtype
                            
                            	Subtype of TLV
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: value
                            
                            	Binary data in TLV
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.oui = None
                                self.subtype = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.oui is not None:
                                    return True

                                if self.subtype is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv']['meta_info']


                        class UnknownTlv(object):
                            """
                            Unknown TLVs
                            
                            .. attribute:: typecode
                            
                            	Type code of TLV
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: value
                            
                            	Binary data in TLV
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.typecode = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.typecode is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-ccm-received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.additional_interface_status is not None:
                                return True

                            if self.header is not None and self.header._has_data():
                                return True

                            if self.interface_status is not None:
                                return True

                            if self.mep_name is not None and self.mep_name._has_data():
                                return True

                            if self.organization_specific_tlv is not None:
                                for child_ref in self.organization_specific_tlv:
                                    if child_ref._has_data():
                                        return True

                            if self.port_status is not None:
                                return True

                            if self.raw_data is not None:
                                return True

                            if self.sender_id is not None and self.sender_id._has_data():
                                return True

                            if self.unknown_tlv is not None:
                                for child_ref in self.unknown_tlv:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']


                    class Statistics(object):
                        """
                        Peer MEP statistics
                        
                        .. attribute:: ccms_invalid_interval
                        
                        	Number of CCMs received with an invalid interval
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_maid
                        
                        	Number of CCMs received with an invalid MAID
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_source_mac_address
                        
                        	Number of CCMs received with an invalid source MAC address
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_our_mep_id
                        
                        	Number of CCMs received with our MEP ID
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_out_of_sequence
                        
                        	Number of CCMs received out\-of\-sequence
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_rdi
                        
                        	Number of CCMs received with the Remote Defect Indication bit set
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_received
                        
                        	Number of CCMs received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_wrong_level
                        
                        	Number of CCMs received with an invalid level
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_ccm_received_time
                        
                        	Elapsed time since last CCM received
                        	**type**\:   :py:class:`LastCcmReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime>`
                        
                        .. attribute:: last_ccm_sequence_number
                        
                        	Sequence number of last CCM received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ccms_invalid_interval = None
                            self.ccms_invalid_maid = None
                            self.ccms_invalid_source_mac_address = None
                            self.ccms_our_mep_id = None
                            self.ccms_out_of_sequence = None
                            self.ccms_rdi = None
                            self.ccms_received = None
                            self.ccms_wrong_level = None
                            self.last_ccm_received_time = Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime()
                            self.last_ccm_received_time.parent = self
                            self.last_ccm_sequence_number = None


                        class LastCcmReceivedTime(object):
                            """
                            Elapsed time since last CCM received
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: nanosecond
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.nanoseconds = None
                                self.seconds = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-ccm-received-time'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.nanoseconds is not None:
                                    return True

                                if self.seconds is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ccms_invalid_interval is not None:
                                return True

                            if self.ccms_invalid_maid is not None:
                                return True

                            if self.ccms_invalid_source_mac_address is not None:
                                return True

                            if self.ccms_our_mep_id is not None:
                                return True

                            if self.ccms_out_of_sequence is not None:
                                return True

                            if self.ccms_rdi is not None:
                                return True

                            if self.ccms_received is not None:
                                return True

                            if self.ccms_wrong_level is not None:
                                return True

                            if self.last_ccm_received_time is not None and self.last_ccm_received_time._has_data():
                                return True

                            if self.last_ccm_sequence_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:peer-mep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ccm_offload is not None:
                            return True

                        if self.cross_check_state is not None:
                            return True

                        if self.error_state is not None and self.error_state._has_data():
                            return True

                        if self.last_ccm_received is not None and self.last_ccm_received._has_data():
                            return True

                        if self.last_up_down_time is not None and self.last_up_down_time._has_data():
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id is not None:
                            return True

                        if self.peer_mep_state is not None:
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYModelError('Key property domain is None')
                    if self.service is None:
                        raise YPYModelError('Key property service is None')
                    if self.local_mep_id is None:
                        raise YPYModelError('Key property local_mep_id is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')
                    if self.peer_mep_id is None:
                        raise YPYModelError('Key property peer_mep_id is None')
                    if self.peer_mac_address is None:
                        raise YPYModelError('Key property peer_mac_address is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:peer-me-pv2s/Cisco-IOS-XR-ethernet-cfm-oper:peer-me-pv2[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:local-mep-id = ' + str(self.local_mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:peer-mep-id = ' + str(self.peer_mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:peer-mac-address = ' + str(self.peer_mac_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain is not None:
                        return True

                    if self.service is not None:
                        return True

                    if self.local_mep_id is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.peer_mep_id is not None:
                        return True

                    if self.peer_mac_address is not None:
                        return True

                    if self.domain_xr is not None:
                        return True

                    if self.interface_xr is not None:
                        return True

                    if self.level is not None:
                        return True

                    if self.mep_direction is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.peer_mep is not None and self.peer_mep._has_data():
                        return True

                    if self.service_xr is not None:
                        return True

                    if self.standby is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:peer-me-pv2s'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_me_pv2 is not None:
                    for child_ref in self.peer_me_pv2:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global_.PeerMePv2S']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.global_configuration_errors is not None and self.global_configuration_errors._has_data():
                return True

            if self.incomplete_traceroutes is not None and self.incomplete_traceroutes._has_data():
                return True

            if self.local_meps is not None and self.local_meps._has_data():
                return True

            if self.maintenance_points is not None and self.maintenance_points._has_data():
                return True

            if self.mep_configuration_errors is not None and self.mep_configuration_errors._has_data():
                return True

            if self.peer_me_pv2s is not None and self.peer_me_pv2s._has_data():
                return True

            if self.traceroute_caches is not None and self.traceroute_caches._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
            return meta._meta_table['Cfm.Global_']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['Cfm']['meta_info']



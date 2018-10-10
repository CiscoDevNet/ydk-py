""" Cisco_IOS_XR_ethernet_cfm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package operational data.

This module contains definitions
for the following management objects\:
  cfm\: CFM operational data

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-sla\-oper
module with state data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CfmAisDir(Enum):
    """
    CfmAisDir (Enum Class)

    Cfm ais dir

    .. data:: up = 0

    	Packets sent inward

    .. data:: down = 1

    	Packets sent outward

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")


class CfmBagAisInterval(Enum):
    """
    CfmBagAisInterval (Enum Class)

    CFM AIS intervals

    .. data:: ais_interval_none = 0

    	Invalid AIS interval

    .. data:: ais_interval1s = 4

    	Interval of 1s

    .. data:: ais_interval1m = 6

    	Interval of 1 min

    """

    ais_interval_none = Enum.YLeaf(0, "ais-interval-none")

    ais_interval1s = Enum.YLeaf(4, "ais-interval1s")

    ais_interval1m = Enum.YLeaf(6, "ais-interval1m")


class CfmBagBdidFmt(Enum):
    """
    CfmBagBdidFmt (Enum Class)

    Bridge domain identifier format

    .. data:: invalid = 0

    	Invalid BDID identifier format

    .. data:: bd_id = 1

    	Identifier is a bridge domain ID

    .. data:: xc_p2p_id = 2

    	Identifier is a P2P cross-connect ID

    .. data:: xc_mp2mp_id = 3

    	Identifier is a MP2MP cross-connect ID

    .. data:: fxc_vlan_aware_id = 4

    	Identifier is a VLAN-aware flexible

    	cross-connect ID

    .. data:: fxc_vlan_unaware_id = 5

    	Identifier is a VLAN-unaware flexible

    	cross-connect ID

    .. data:: down_only = 6

    	Identifier is a maintenance association name

    """

    invalid = Enum.YLeaf(0, "invalid")

    bd_id = Enum.YLeaf(1, "bd-id")

    xc_p2p_id = Enum.YLeaf(2, "xc-p2p-id")

    xc_mp2mp_id = Enum.YLeaf(3, "xc-mp2mp-id")

    fxc_vlan_aware_id = Enum.YLeaf(4, "fxc-vlan-aware-id")

    fxc_vlan_unaware_id = Enum.YLeaf(5, "fxc-vlan-unaware-id")

    down_only = Enum.YLeaf(6, "down-only")


class CfmBagCcmInterval(Enum):
    """
    CfmBagCcmInterval (Enum Class)

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

    interval_none = Enum.YLeaf(0, "interval-none")

    interval3_3ms = Enum.YLeaf(1, "interval3-3ms")

    interval10ms = Enum.YLeaf(2, "interval10ms")

    interval100ms = Enum.YLeaf(3, "interval100ms")

    interval1s = Enum.YLeaf(4, "interval1s")

    interval10s = Enum.YLeaf(5, "interval10s")

    interval1m = Enum.YLeaf(6, "interval1m")

    interval10m = Enum.YLeaf(7, "interval10m")


class CfmBagCcmOffload(Enum):
    """
    CfmBagCcmOffload (Enum Class)

    Offload status of CCM processing

    .. data:: offload_none = 0

    	CCM processing has not been offloaded

    .. data:: offload_software = 1

    	CCM processing has been offloaded to software

    .. data:: offload_hardware = 2

    	CCM processing has been offloaded to hardware

    """

    offload_none = Enum.YLeaf(0, "offload-none")

    offload_software = Enum.YLeaf(1, "offload-software")

    offload_hardware = Enum.YLeaf(2, "offload-hardware")


class CfmBagDirection(Enum):
    """
    CfmBagDirection (Enum Class)

    MEP direction

    .. data:: direction_up = 0

    	Up

    .. data:: direction_down = 1

    	Down

    .. data:: direction_invalid = 2

    	Invalid direction

    """

    direction_up = Enum.YLeaf(0, "direction-up")

    direction_down = Enum.YLeaf(1, "direction-down")

    direction_invalid = Enum.YLeaf(2, "direction-invalid")


class CfmBagIssuRole(Enum):
    """
    CfmBagIssuRole (Enum Class)

    CFM ISSU role

    .. data:: unknown = 0

    	Unknown

    .. data:: primary = 1

    	Primary

    .. data:: secondary = 2

    	Secondary

    """

    unknown = Enum.YLeaf(0, "unknown")

    primary = Enum.YLeaf(1, "primary")

    secondary = Enum.YLeaf(2, "secondary")


class CfmBagIwState(Enum):
    """
    CfmBagIwState (Enum Class)

    CFM Interworking state

    .. data:: interworking_up = 0

    	Interface is UP

    .. data:: interworking_test = 1

    	Interface is in TEST mode

    """

    interworking_up = Enum.YLeaf(0, "interworking-up")

    interworking_test = Enum.YLeaf(1, "interworking-test")


class CfmBagMdLevel(Enum):
    """
    CfmBagMdLevel (Enum Class)

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

    level0 = Enum.YLeaf(0, "level0")

    level1 = Enum.YLeaf(1, "level1")

    level2 = Enum.YLeaf(2, "level2")

    level3 = Enum.YLeaf(3, "level3")

    level4 = Enum.YLeaf(4, "level4")

    level5 = Enum.YLeaf(5, "level5")

    level6 = Enum.YLeaf(6, "level6")

    level7 = Enum.YLeaf(7, "level7")

    level_invalid = Enum.YLeaf(8, "level-invalid")


class CfmBagMdidFmt(Enum):
    """
    CfmBagMdidFmt (Enum Class)

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

    mdid_null = Enum.YLeaf(1, "mdid-null")

    mdid_dns_like = Enum.YLeaf(2, "mdid-dns-like")

    mdid_mac_address = Enum.YLeaf(3, "mdid-mac-address")

    mdid_string = Enum.YLeaf(4, "mdid-string")

    mdid_unknown = Enum.YLeaf(5, "mdid-unknown")


class CfmBagOpcode(Enum):
    """
    CfmBagOpcode (Enum Class)

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

    reserved = Enum.YLeaf(0, "reserved")

    ccm = Enum.YLeaf(1, "ccm")

    lbr = Enum.YLeaf(2, "lbr")

    lbm = Enum.YLeaf(3, "lbm")

    ltr = Enum.YLeaf(4, "ltr")

    ltm = Enum.YLeaf(5, "ltm")


class CfmBagSmanFmt(Enum):
    """
    CfmBagSmanFmt (Enum Class)

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

    sman_vlan_id = Enum.YLeaf(1, "sman-vlan-id")

    sman_string = Enum.YLeaf(2, "sman-string")

    sman_uint16 = Enum.YLeaf(3, "sman-uint16")

    sman_vpn_id = Enum.YLeaf(4, "sman-vpn-id")

    sman_icc = Enum.YLeaf(32, "sman-icc")

    sman_unknown = Enum.YLeaf(33, "sman-unknown")


class CfmBagStpState(Enum):
    """
    CfmBagStpState (Enum Class)

    CFM STP state

    .. data:: stp_up = 0

    	Interface is UP

    .. data:: stp_blocked = 1

    	Interface is STP-blocked

    .. data:: stp_unknown = 2

    	Unknown Interface STP state

    """

    stp_up = Enum.YLeaf(0, "stp-up")

    stp_blocked = Enum.YLeaf(1, "stp-blocked")

    stp_unknown = Enum.YLeaf(2, "stp-unknown")


class CfmMaMpVariety(Enum):
    """
    CfmMaMpVariety (Enum Class)

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

    mip = Enum.YLeaf(0, "mip")

    up_mep = Enum.YLeaf(1, "up-mep")

    downmep = Enum.YLeaf(2, "downmep")

    unknown_mep = Enum.YLeaf(3, "unknown-mep")


class CfmPmAddlIntfStatus(Enum):
    """
    CfmPmAddlIntfStatus (Enum Class)

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

    unknown = Enum.YLeaf(0, "unknown")

    administratively_down = Enum.YLeaf(1, "administratively-down")

    remote_excessive_errors = Enum.YLeaf(2, "remote-excessive-errors")

    local_excessive_errors = Enum.YLeaf(3, "local-excessive-errors")


class CfmPmAisReceive(Enum):
    """
    CfmPmAisReceive (Enum Class)

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

    receive_none = Enum.YLeaf(0, "receive-none")

    receive_ais = Enum.YLeaf(1, "receive-ais")

    receive_lck = Enum.YLeaf(2, "receive-lck")

    receive_direct = Enum.YLeaf(3, "receive-direct")


class CfmPmAisTransmit(Enum):
    """
    CfmPmAisTransmit (Enum Class)

    Enumeration of how the MEP is transmitting AIS,

    via a MIP or directly to a higher MEP

    .. data:: transmit_none = 0

    	AIS not transmitted

    .. data:: transmit_ais = 1

    	AIS transmitted via MIP

    .. data:: transmit_ais_direct = 2

    	AIS signal passed directly to a higher MEP

    """

    transmit_none = Enum.YLeaf(0, "transmit-none")

    transmit_ais = Enum.YLeaf(1, "transmit-ais")

    transmit_ais_direct = Enum.YLeaf(2, "transmit-ais-direct")


class CfmPmChassisIdFmt(Enum):
    """
    CfmPmChassisIdFmt (Enum Class)

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

    chassis_id_chassis_component = Enum.YLeaf(1, "chassis-id-chassis-component")

    chassis_id_interface_alias = Enum.YLeaf(2, "chassis-id-interface-alias")

    chassis_id_port_component = Enum.YLeaf(3, "chassis-id-port-component")

    chassis_id_mac_address = Enum.YLeaf(4, "chassis-id-mac-address")

    chassis_id_network_address = Enum.YLeaf(5, "chassis-id-network-address")

    chassis_id_interface_name = Enum.YLeaf(6, "chassis-id-interface-name")

    chassis_id_local = Enum.YLeaf(7, "chassis-id-local")

    chassis_id_unknown_type = Enum.YLeaf(8, "chassis-id-unknown-type")


class CfmPmEgressAction(Enum):
    """
    CfmPmEgressAction (Enum Class)

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

    egress_ok = Enum.YLeaf(1, "egress-ok")

    egress_down = Enum.YLeaf(2, "egress-down")

    egress_blocked = Enum.YLeaf(3, "egress-blocked")

    egress_vid = Enum.YLeaf(4, "egress-vid")


class CfmPmElmReplyFilter(Enum):
    """
    CfmPmElmReplyFilter (Enum Class)

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

    reply_filter_not_present = Enum.YLeaf(0, "reply-filter-not-present")

    reply_filter_default = Enum.YLeaf(1, "reply-filter-default")

    reply_filter_vlan_topology = Enum.YLeaf(2, "reply-filter-vlan-topology")

    reply_filter_spanning_tree = Enum.YLeaf(3, "reply-filter-spanning-tree")

    reply_filter_all_ports = Enum.YLeaf(4, "reply-filter-all-ports")


class CfmPmElrEgressAction(Enum):
    """
    CfmPmElrEgressAction (Enum Class)

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

    elr_egress_ok = Enum.YLeaf(1, "elr-egress-ok")

    elr_egress_down = Enum.YLeaf(2, "elr-egress-down")

    elr_egress_blocked = Enum.YLeaf(3, "elr-egress-blocked")

    elr_egress_vid = Enum.YLeaf(4, "elr-egress-vid")

    elr_egress_mac = Enum.YLeaf(255, "elr-egress-mac")


class CfmPmElrIngressAction(Enum):
    """
    CfmPmElrIngressAction (Enum Class)

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

    elr_ingress_ok = Enum.YLeaf(1, "elr-ingress-ok")

    elr_ingress_down = Enum.YLeaf(2, "elr-ingress-down")

    elr_ingress_blocked = Enum.YLeaf(3, "elr-ingress-blocked")

    elr_ingress_vid = Enum.YLeaf(4, "elr-ingress-vid")


class CfmPmElrRelayAction(Enum):
    """
    CfmPmElrRelayAction (Enum Class)

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

    elr_relay_hit = Enum.YLeaf(1, "elr-relay-hit")

    elr_relay_fdb = Enum.YLeaf(2, "elr-relay-fdb")

    elr_relay_flood = Enum.YLeaf(3, "elr-relay-flood")

    elr_relay_drop = Enum.YLeaf(4, "elr-relay-drop")


class CfmPmEltDelayModel(Enum):
    """
    CfmPmEltDelayModel (Enum Class)

    Delay model used for Exploratory Linktrace

    operations

    .. data:: delay_model_invalid = 0

    	Not a valid delay model

    .. data:: delay_model_logarithmic = 1

    	Reply using logarithmic delay model

    .. data:: delay_model_constant = 2

    	Reply using constant delay model

    """

    delay_model_invalid = Enum.YLeaf(0, "delay-model-invalid")

    delay_model_logarithmic = Enum.YLeaf(1, "delay-model-logarithmic")

    delay_model_constant = Enum.YLeaf(2, "delay-model-constant")


class CfmPmIdFmt(Enum):
    """
    CfmPmIdFmt (Enum Class)

    ID format

    .. data:: id_format_is_string = 0

    	ID format is a string

    .. data:: id_format_is_mac_address = 1

    	ID format is a MAC address

    .. data:: id_format_is_raw_hex = 2

    	ID format is raw hex

    """

    id_format_is_string = Enum.YLeaf(0, "id-format-is-string")

    id_format_is_mac_address = Enum.YLeaf(1, "id-format-is-mac-address")

    id_format_is_raw_hex = Enum.YLeaf(2, "id-format-is-raw-hex")


class CfmPmIngressAction(Enum):
    """
    CfmPmIngressAction (Enum Class)

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

    ingress_ok = Enum.YLeaf(1, "ingress-ok")

    ingress_down = Enum.YLeaf(2, "ingress-down")

    ingress_blocked = Enum.YLeaf(3, "ingress-blocked")

    ingress_vid = Enum.YLeaf(4, "ingress-vid")


class CfmPmIntfStatus(Enum):
    """
    CfmPmIntfStatus (Enum Class)

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

    interface_status_up = Enum.YLeaf(1, "interface-status-up")

    interface_status_down = Enum.YLeaf(2, "interface-status-down")

    interface_status_testing = Enum.YLeaf(3, "interface-status-testing")

    interface_status_unknown = Enum.YLeaf(4, "interface-status-unknown")

    interface_status_dormant = Enum.YLeaf(5, "interface-status-dormant")

    interface_status_not_present = Enum.YLeaf(6, "interface-status-not-present")

    interface_status_lower_layer_down = Enum.YLeaf(7, "interface-status-lower-layer-down")


class CfmPmLastHopFmt(Enum):
    """
    CfmPmLastHopFmt (Enum Class)

    Last hop identifier format

    .. data:: last_hop_none = 0

    	No last hop identifier

    .. data:: last_hop_host_name = 1

    	Last hop identifier is a hostname

    .. data:: last_hop_egress_id = 2

    	Last hop identifier is an egress ID

    """

    last_hop_none = Enum.YLeaf(0, "last-hop-none")

    last_hop_host_name = Enum.YLeaf(1, "last-hop-host-name")

    last_hop_egress_id = Enum.YLeaf(2, "last-hop-egress-id")


class CfmPmLtMode(Enum):
    """
    CfmPmLtMode (Enum Class)

    Type of Linktrace operation

    .. data:: cfm_pm_lt_mode_basic = 1

    	Basic IEEE 802.1ag Linktrace

    .. data:: cfm_pm_lt_mode_exploratory = 2

    	Cisco Exploratory Linktrace

    """

    cfm_pm_lt_mode_basic = Enum.YLeaf(1, "cfm-pm-lt-mode-basic")

    cfm_pm_lt_mode_exploratory = Enum.YLeaf(2, "cfm-pm-lt-mode-exploratory")


class CfmPmMepDefect(Enum):
    """
    CfmPmMepDefect (Enum Class)

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

    defect_none = Enum.YLeaf(0, "defect-none")

    defect_rdi_ccm = Enum.YLeaf(1, "defect-rdi-ccm")

    defect_ma_cstatus = Enum.YLeaf(2, "defect-ma-cstatus")

    defect_remote_ccm = Enum.YLeaf(3, "defect-remote-ccm")

    defect_error_ccm = Enum.YLeaf(4, "defect-error-ccm")

    defect_cross_connect_ccm = Enum.YLeaf(5, "defect-cross-connect-ccm")


class CfmPmMepFngState(Enum):
    """
    CfmPmMepFngState (Enum Class)

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

    fng_reset = Enum.YLeaf(1, "fng-reset")

    fng_defect = Enum.YLeaf(2, "fng-defect")

    fng_report_defect = Enum.YLeaf(3, "fng-report-defect")

    fng_defect_reported = Enum.YLeaf(4, "fng-defect-reported")

    fng_defect_clearing = Enum.YLeaf(5, "fng-defect-clearing")


class CfmPmPktAction(Enum):
    """
    CfmPmPktAction (Enum Class)

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

    packet_processed = Enum.YLeaf(0, "packet-processed")

    packet_forwarded = Enum.YLeaf(1, "packet-forwarded")

    unknown_opcode = Enum.YLeaf(2, "unknown-opcode")

    filter_level = Enum.YLeaf(3, "filter-level")

    filter_blocked = Enum.YLeaf(4, "filter-blocked")

    filter_local_mac = Enum.YLeaf(5, "filter-local-mac")

    malformed_ccm_size = Enum.YLeaf(6, "malformed-ccm-size")

    malformed_ccm_mep_id = Enum.YLeaf(7, "malformed-ccm-mep-id")

    malformed_too_short = Enum.YLeaf(8, "malformed-too-short")

    malformed_destination_mac_unicast = Enum.YLeaf(9, "malformed-destination-mac-unicast")

    malformed_destination_mac_multicast = Enum.YLeaf(10, "malformed-destination-mac-multicast")

    malformed_tlv_offset = Enum.YLeaf(11, "malformed-tlv-offset")

    malformed_lbm_source_mac = Enum.YLeaf(12, "malformed-lbm-source-mac")

    malformed_ltr_relay_action = Enum.YLeaf(13, "malformed-ltr-relay-action")

    malformed_ltr_reply_tlv = Enum.YLeaf(14, "malformed-ltr-reply-tlv")

    malformed_lt_origin = Enum.YLeaf(15, "malformed-lt-origin")

    malformed_ltm_target = Enum.YLeaf(16, "malformed-ltm-target")

    malformed_source_mac = Enum.YLeaf(17, "malformed-source-mac")

    malformed_header_too_short = Enum.YLeaf(18, "malformed-header-too-short")

    malformed_tlv_header_overrun = Enum.YLeaf(19, "malformed-tlv-header-overrun")

    malformed_tlv_overrun = Enum.YLeaf(20, "malformed-tlv-overrun")

    malformed_duplicate_sender_id = Enum.YLeaf(21, "malformed-duplicate-sender-id")

    malformed_duplicate_port_status = Enum.YLeaf(22, "malformed-duplicate-port-status")

    malformed_duplicate_interface_status = Enum.YLeaf(23, "malformed-duplicate-interface-status")

    malformed_wrong_tlv = Enum.YLeaf(24, "malformed-wrong-tlv")

    malformed_duplicate_data = Enum.YLeaf(25, "malformed-duplicate-data")

    malformed_duplicate_ltr_egress_id = Enum.YLeaf(26, "malformed-duplicate-ltr-egress-id")

    malformed_duplicate_reply_ingress = Enum.YLeaf(27, "malformed-duplicate-reply-ingress")

    malformed_duplicate_reply_egress = Enum.YLeaf(28, "malformed-duplicate-reply-egress")

    malformed_duplicate_ltm_egress_id = Enum.YLeaf(29, "malformed-duplicate-ltm-egress-id")

    malformed_sender_id_size = Enum.YLeaf(30, "malformed-sender-id-size")

    malformed_chassis_id_size = Enum.YLeaf(31, "malformed-chassis-id-size")

    malformed_mgmt_address_domain_size = Enum.YLeaf(32, "malformed-mgmt-address-domain-size")

    malformed_mgmt_address_size = Enum.YLeaf(33, "malformed-mgmt-address-size")

    malformed_port_status_size = Enum.YLeaf(34, "malformed-port-status-size")

    malformed_port_status = Enum.YLeaf(35, "malformed-port-status")

    malformed_interface_status_size = Enum.YLeaf(36, "malformed-interface-status-size")

    malformed_interface_status = Enum.YLeaf(37, "malformed-interface-status")

    malformed_organization_specific_tlv_size = Enum.YLeaf(38, "malformed-organization-specific-tlv-size")

    malformed_duplicate_mep_name = Enum.YLeaf(39, "malformed-duplicate-mep-name")

    malformed_duplicate_additional_interface_status = Enum.YLeaf(40, "malformed-duplicate-additional-interface-status")

    malformed_ltr_egress_id_size = Enum.YLeaf(41, "malformed-ltr-egress-id-size")

    malformed_reply_ingress_size = Enum.YLeaf(42, "malformed-reply-ingress-size")

    malformed_ingress_action = Enum.YLeaf(43, "malformed-ingress-action")

    malformed_reply_ingress_mac = Enum.YLeaf(44, "malformed-reply-ingress-mac")

    malformed_ingress_port_length_size = Enum.YLeaf(45, "malformed-ingress-port-length-size")

    malformed_ingress_port_id_length = Enum.YLeaf(46, "malformed-ingress-port-id-length")

    malformed_ingress_port_id_size = Enum.YLeaf(47, "malformed-ingress-port-id-size")

    malformed_reply_egress_size = Enum.YLeaf(48, "malformed-reply-egress-size")

    malformed_egress_action = Enum.YLeaf(49, "malformed-egress-action")

    malformed_reply_egress_mac = Enum.YLeaf(50, "malformed-reply-egress-mac")

    malformed_egress_port_length_size = Enum.YLeaf(51, "malformed-egress-port-length-size")

    malformed_egress_port_id_length = Enum.YLeaf(52, "malformed-egress-port-id-length")

    malformed_egress_port_id_size = Enum.YLeaf(53, "malformed-egress-port-id-size")

    malformed_ltm_egress_id_size = Enum.YLeaf(54, "malformed-ltm-egress-id-size")

    malformed_mep_name_size = Enum.YLeaf(55, "malformed-mep-name-size")

    malformed_mep_name_name_length = Enum.YLeaf(56, "malformed-mep-name-name-length")

    malformed_additional_interface_status_size = Enum.YLeaf(57, "malformed-additional-interface-status-size")

    malformed_additional_interface_status = Enum.YLeaf(58, "malformed-additional-interface-status")

    malformed_ccm_interval = Enum.YLeaf(59, "malformed-ccm-interval")

    malformed_mdid_mac_address_length = Enum.YLeaf(60, "malformed-mdid-mac-address-length")

    malformed_mdid_length = Enum.YLeaf(61, "malformed-mdid-length")

    malformed_sman_length = Enum.YLeaf(62, "malformed-sman-length")

    malformed_sman2_byte_length = Enum.YLeaf(63, "malformed-sman2-byte-length")

    malformed_sman_vpn_id_length = Enum.YLeaf(64, "malformed-sman-vpn-id-length")

    malformed_elr_no_reply_tlv = Enum.YLeaf(65, "malformed-elr-no-reply-tlv")

    malformed_separate_elr_reply_egress = Enum.YLeaf(66, "malformed-separate-elr-reply-egress")

    malformed_dcm_destination_multicast = Enum.YLeaf(67, "malformed-dcm-destination-multicast")

    malformed_dcm_embed_length = Enum.YLeaf(68, "malformed-dcm-embed-length")

    malformed_dcm_embed_level = Enum.YLeaf(69, "malformed-dcm-embed-level")

    malformed_dcm_embed_version = Enum.YLeaf(70, "malformed-dcm-embed-version")

    malformed_elr_relay_action = Enum.YLeaf(71, "malformed-elr-relay-action")

    malformed_elr_tt_ls = Enum.YLeaf(73, "malformed-elr-tt-ls")

    malformed_elr_ttl_ingress = Enum.YLeaf(74, "malformed-elr-ttl-ingress")

    malformed_elr_ttl_egress = Enum.YLeaf(75, "malformed-elr-ttl-egress")

    malformed_elm_destination_unicast = Enum.YLeaf(76, "malformed-elm-destination-unicast")

    malformed_elm_egress_id = Enum.YLeaf(77, "malformed-elm-egress-id")

    malformed_dcm_embed_oui = Enum.YLeaf(78, "malformed-dcm-embed-oui")

    malformed_dcm_embed_opcode = Enum.YLeaf(79, "malformed-dcm-embed-opcode")

    malformed_elm_constant_zero = Enum.YLeaf(80, "malformed-elm-constant-zero")

    malformed_elr_timeout_zero = Enum.YLeaf(81, "malformed-elr-timeout-zero")

    malformed_duplicate_test = Enum.YLeaf(82, "malformed-duplicate-test")

    malformed_dmm_source_mac = Enum.YLeaf(83, "malformed-dmm-source-mac")

    malformed_test_size = Enum.YLeaf(84, "malformed-test-size")

    malformed_dmr_time_stamps = Enum.YLeaf(85, "malformed-dmr-time-stamps")

    malformed_dm_time_stamp_fmt = Enum.YLeaf(86, "malformed-dm-time-stamp-fmt")

    malformed_ais_interval = Enum.YLeaf(87, "malformed-ais-interval")

    filter_interface_down = Enum.YLeaf(88, "filter-interface-down")

    filter_forward_standby = Enum.YLeaf(89, "filter-forward-standby")

    malformed_sman_icc_based_length = Enum.YLeaf(90, "malformed-sman-icc-based-length")

    filter_foward_issu_secondary = Enum.YLeaf(120, "filter-foward-issu-secondary")

    filter_response_standby = Enum.YLeaf(121, "filter-response-standby")

    filter_response_issu_secondary = Enum.YLeaf(122, "filter-response-issu-secondary")


class CfmPmPortIdFmt(Enum):
    """
    CfmPmPortIdFmt (Enum Class)

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

    port_id_interface_alias = Enum.YLeaf(1, "port-id-interface-alias")

    port_id_port_component = Enum.YLeaf(2, "port-id-port-component")

    port_id_mac_address = Enum.YLeaf(3, "port-id-mac-address")

    port_id_network_address = Enum.YLeaf(4, "port-id-network-address")

    port_id_interface_name = Enum.YLeaf(5, "port-id-interface-name")

    port_id_agent_circuit_id = Enum.YLeaf(6, "port-id-agent-circuit-id")

    port_id_local = Enum.YLeaf(7, "port-id-local")

    port_id_unknown = Enum.YLeaf(8, "port-id-unknown")


class CfmPmPortStatus(Enum):
    """
    CfmPmPortStatus (Enum Class)

    Port status

    .. data:: port_status_blocked = 1

    	Port is STP blocked

    .. data:: port_status_up = 2

    	Port is up

    .. data:: port_status_unknown = 3

    	Unknown port status

    """

    port_status_blocked = Enum.YLeaf(1, "port-status-blocked")

    port_status_up = Enum.YLeaf(2, "port-status-up")

    port_status_unknown = Enum.YLeaf(3, "port-status-unknown")


class CfmPmRelayAction(Enum):
    """
    CfmPmRelayAction (Enum Class)

    LTR relay action

    .. data:: relay_hit = 1

    	Target Hit

    .. data:: relay_fdb = 2

    	Filtering database

    .. data:: relay_mpdb = 3

    	CCM Learning database

    """

    relay_hit = Enum.YLeaf(1, "relay-hit")

    relay_fdb = Enum.YLeaf(2, "relay-fdb")

    relay_mpdb = Enum.YLeaf(3, "relay-mpdb")


class CfmPmRmepState(Enum):
    """
    CfmPmRmepState (Enum Class)

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

    peer_mep_idle = Enum.YLeaf(1, "peer-mep-idle")

    peer_mep_start = Enum.YLeaf(2, "peer-mep-start")

    peer_mep_failed = Enum.YLeaf(3, "peer-mep-failed")

    peer_mep_ok = Enum.YLeaf(4, "peer-mep-ok")


class CfmPmRmepXcState(Enum):
    """
    CfmPmRmepXcState (Enum Class)

    Cross\-check state of a peer MEP

    .. data:: cross_check_ok = 0

    	Cross-check OK

    .. data:: cross_check_missing = 1

    	No CCMs received within loss time from peer MEP

    .. data:: cross_check_extra = 2

    	CCMs received from peer MEP not marked for

    	cross-check

    """

    cross_check_ok = Enum.YLeaf(0, "cross-check-ok")

    cross_check_missing = Enum.YLeaf(1, "cross-check-missing")

    cross_check_extra = Enum.YLeaf(2, "cross-check-extra")


class SlaBucketSize(Enum):
    """
    SlaBucketSize (Enum Class)

    Type of configuration of a bucket size

    .. data:: buckets_per_probe = 0

    	Bucket size is configured as buckets per probe

    .. data:: probes_per_bucket = 1

    	Bucket size is configured as probes per bucket

    """

    buckets_per_probe = Enum.YLeaf(0, "buckets-per-probe")

    probes_per_bucket = Enum.YLeaf(1, "probes-per-bucket")


class SlaOperBucket(Enum):
    """
    SlaOperBucket (Enum Class)

    Type of SLA metric bucket

    .. data:: bucket_type_bins = 0

    	SLA metric bin

    .. data:: bucket_type_samples = 1

    	SLA metric sample

    """

    bucket_type_bins = Enum.YLeaf(0, "bucket-type-bins")

    bucket_type_samples = Enum.YLeaf(1, "bucket-type-samples")


class SlaOperOperation(Enum):
    """
    SlaOperOperation (Enum Class)

    Type of SLA operation

    .. data:: operation_type_configured = 0

    	Configured SLA operation

    .. data:: operation_type_ondemand = 1

    	On-demand SLA operation

    """

    operation_type_configured = Enum.YLeaf(0, "operation-type-configured")

    operation_type_ondemand = Enum.YLeaf(1, "operation-type-ondemand")


class SlaOperPacketPriority(Enum):
    """
    SlaOperPacketPriority (Enum Class)

    Priority scheme for packet priority

    .. data:: priority_none = 0

    	Packet does not use any specified priority.

    .. data:: priority_cos = 1

    	Packet uses a specified 3-bit COS priority

    	value.

    """

    priority_none = Enum.YLeaf(0, "priority-none")

    priority_cos = Enum.YLeaf(1, "priority-cos")


class SlaOperTestPatternScheme(Enum):
    """
    SlaOperTestPatternScheme (Enum Class)

    Test pattern scheme for packet padding

    .. data:: hex = 0

    	Packet is padded with a user-specified string

    .. data:: pseudo_random = 1

    	Packet is padded with a pseudo-random bit

    	sequence

    """

    hex = Enum.YLeaf(0, "hex")

    pseudo_random = Enum.YLeaf(1, "pseudo-random")


class SlaRecordableMetric(Enum):
    """
    SlaRecordableMetric (Enum Class)

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

    metric_invalid = Enum.YLeaf(0, "metric-invalid")

    metric_round_trip_delay = Enum.YLeaf(1, "metric-round-trip-delay")

    metric_one_way_delay_sd = Enum.YLeaf(2, "metric-one-way-delay-sd")

    metric_one_way_delay_ds = Enum.YLeaf(3, "metric-one-way-delay-ds")

    metric_round_trip_jitter = Enum.YLeaf(4, "metric-round-trip-jitter")

    metric_one_way_jitter_sd = Enum.YLeaf(5, "metric-one-way-jitter-sd")

    metric_one_way_jitter_ds = Enum.YLeaf(6, "metric-one-way-jitter-ds")

    metric_one_way_flr_sd = Enum.YLeaf(7, "metric-one-way-flr-sd")

    metric_one_way_flr_ds = Enum.YLeaf(8, "metric-one-way-flr-ds")



class Cfm(Entity):
    """
    CFM operational data
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes>`
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global>`
    
    

    """

    _prefix = 'ethernet-cfm-oper'
    _revision = '2017-10-06'

    def __init__(self):
        super(Cfm, self).__init__()
        self._top_entity = None

        self.yang_name = "cfm"
        self.yang_parent_name = "Cisco-IOS-XR-ethernet-cfm-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Cfm.Nodes)), ("global", ("global_", Cfm.Global))])
        self._leafs = OrderedDict()

        self.nodes = Cfm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.global_ = Cfm.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._segment_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Cfm, [], name, value)


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-cfm-oper'
        _revision = '2017-10-06'

        def __init__(self):
            super(Cfm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "cfm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Cfm.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cfm.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_aises
            
            	Interface AIS table
            	**type**\:  :py:class:`InterfaceAises <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises>`
            
            .. attribute:: interface_statistics
            
            	Interface Statistics table
            	**type**\:  :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics>`
            
            .. attribute:: summary
            
            	Summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.Summary>`
            
            .. attribute:: ccm_learning_databases
            
            	CCMLearningDatabase table
            	**type**\:  :py:class:`CcmLearningDatabases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("interface-aises", ("interface_aises", Cfm.Nodes.Node.InterfaceAises)), ("interface-statistics", ("interface_statistics", Cfm.Nodes.Node.InterfaceStatistics)), ("summary", ("summary", Cfm.Nodes.Node.Summary)), ("ccm-learning-databases", ("ccm_learning_databases", Cfm.Nodes.Node.CcmLearningDatabases))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.interface_aises = Cfm.Nodes.Node.InterfaceAises()
                self.interface_aises.parent = self
                self._children_name_map["interface_aises"] = "interface-aises"

                self.interface_statistics = Cfm.Nodes.Node.InterfaceStatistics()
                self.interface_statistics.parent = self
                self._children_name_map["interface_statistics"] = "interface-statistics"

                self.summary = Cfm.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.ccm_learning_databases = Cfm.Nodes.Node.CcmLearningDatabases()
                self.ccm_learning_databases.parent = self
                self._children_name_map["ccm_learning_databases"] = "ccm-learning-databases"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Nodes.Node, ['node'], name, value)


            class InterfaceAises(Entity):
                """
                Interface AIS table
                
                .. attribute:: interface_ais
                
                	AIS statistics for a particular interface
                	**type**\: list of  		 :py:class:`InterfaceAis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Nodes.Node.InterfaceAises, self).__init__()

                    self.yang_name = "interface-aises"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-ais", ("interface_ais", Cfm.Nodes.Node.InterfaceAises.InterfaceAis))])
                    self._leafs = OrderedDict()

                    self.interface_ais = YList(self)
                    self._segment_path = lambda: "interface-aises"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Nodes.Node.InterfaceAises, [], name, value)


                class InterfaceAis(Entity):
                    """
                    AIS statistics for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: direction  (key)
                    
                    	AIS Direction
                    	**type**\:  :py:class:`CfmAisDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmAisDir>`
                    
                    .. attribute:: statistics
                    
                    	AIS statistics
                    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics>`
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: interface_state
                    
                    	IM Interface state
                    	**type**\: str
                    
                    .. attribute:: interworking_state
                    
                    	Interface interworking state
                    	**type**\:  :py:class:`CfmBagIwState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwState>`
                    
                    .. attribute:: stp_state
                    
                    	STP state
                    	**type**\:  :py:class:`CfmBagStpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpState>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Nodes.Node.InterfaceAises.InterfaceAis, self).__init__()

                        self.yang_name = "interface-ais"
                        self.yang_parent_name = "interface-aises"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name','direction']
                        self._child_classes = OrderedDict([("statistics", ("statistics", Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmAisDir', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('interface_state', (YLeaf(YType.str, 'interface-state'), ['str'])),
                            ('interworking_state', (YLeaf(YType.enumeration, 'interworking-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwState', '')])),
                            ('stp_state', (YLeaf(YType.enumeration, 'stp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpState', '')])),
                        ])
                        self.interface_name = None
                        self.direction = None
                        self.interface = None
                        self.interface_state = None
                        self.interworking_state = None
                        self.stp_state = None

                        self.statistics = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._segment_path = lambda: "interface-ais" + "[interface-name='" + str(self.interface_name) + "']" + "[direction='" + str(self.direction) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Nodes.Node.InterfaceAises.InterfaceAis, ['interface_name', 'direction', 'interface', 'interface_state', 'interworking_state', 'stp_state'], name, value)


                    class Statistics(Entity):
                        """
                        AIS statistics
                        
                        .. attribute:: defects
                        
                        	Defects detected
                        	**type**\:  :py:class:`Defects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects>`
                        
                        .. attribute:: last_started
                        
                        	Time elapsed since sending last started
                        	**type**\:  :py:class:`LastStarted <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted>`
                        
                        .. attribute:: direction
                        
                        	Direction of AIS packets
                        	**type**\:  :py:class:`CfmBagDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirection>`
                        
                        .. attribute:: lowest_level
                        
                        	Level of the lowest MEP transmitting AIS
                        	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                        
                        .. attribute:: transmission_level
                        
                        	Level that AIS packets are transmitted on
                        	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                        
                        .. attribute:: transmission_interval
                        
                        	Interval at which AIS packets are transmitted
                        	**type**\:  :py:class:`CfmBagAisInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisInterval>`
                        
                        .. attribute:: sent_packets
                        
                        	Total number of packets sent by the transmitting MEP
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: via_level
                        
                        	Levels of other MEPs receiving AIS
                        	**type**\: list of   :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "interface-ais"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("defects", ("defects", Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects)), ("last-started", ("last_started", Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted))])
                            self._leafs = OrderedDict([
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection', '')])),
                                ('lowest_level', (YLeaf(YType.enumeration, 'lowest-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                                ('transmission_level', (YLeaf(YType.enumeration, 'transmission-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                                ('transmission_interval', (YLeaf(YType.enumeration, 'transmission-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval', '')])),
                                ('sent_packets', (YLeaf(YType.uint32, 'sent-packets'), ['int'])),
                                ('via_level', (YLeafList(YType.enumeration, 'via-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ])
                            self.direction = None
                            self.lowest_level = None
                            self.transmission_level = None
                            self.transmission_interval = None
                            self.sent_packets = None
                            self.via_level = []

                            self.defects = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects()
                            self.defects.parent = self
                            self._children_name_map["defects"] = "defects"

                            self.last_started = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted()
                            self.last_started.parent = self
                            self._children_name_map["last_started"] = "last-started"
                            self._segment_path = lambda: "statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics, ['direction', 'lowest_level', 'transmission_level', 'transmission_interval', 'sent_packets', 'via_level'], name, value)


                        class Defects(Entity):
                            """
                            Defects detected
                            
                            .. attribute:: remote_meps_defects
                            
                            	Defects detected from remote MEPs
                            	**type**\:  :py:class:`RemoteMepsDefects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects>`
                            
                            .. attribute:: ais_received
                            
                            	AIS or LCK received
                            	**type**\: bool
                            
                            .. attribute:: peer_meps_that_timed_out
                            
                            	Number of peer MEPs that have timed out
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing
                            
                            	Number of missing peer MEPs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_missing
                            
                            	Number of missing auto cross\-check MEPs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unexpected
                            
                            	Number of unexpected peer MEPs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_port_status
                            
                            	The local port or interface is down
                            	**type**\: bool
                            
                            .. attribute:: peer_port_status
                            
                            	A peer port or interface is down
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects, self).__init__()

                                self.yang_name = "defects"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("remote-meps-defects", ("remote_meps_defects", Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects))])
                                self._leafs = OrderedDict([
                                    ('ais_received', (YLeaf(YType.boolean, 'ais-received'), ['bool'])),
                                    ('peer_meps_that_timed_out', (YLeaf(YType.uint32, 'peer-meps-that-timed-out'), ['int'])),
                                    ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                                    ('auto_missing', (YLeaf(YType.uint32, 'auto-missing'), ['int'])),
                                    ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                                    ('local_port_status', (YLeaf(YType.boolean, 'local-port-status'), ['bool'])),
                                    ('peer_port_status', (YLeaf(YType.boolean, 'peer-port-status'), ['bool'])),
                                ])
                                self.ais_received = None
                                self.peer_meps_that_timed_out = None
                                self.missing = None
                                self.auto_missing = None
                                self.unexpected = None
                                self.local_port_status = None
                                self.peer_port_status = None

                                self.remote_meps_defects = Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects()
                                self.remote_meps_defects.parent = self
                                self._children_name_map["remote_meps_defects"] = "remote-meps-defects"
                                self._segment_path = lambda: "defects"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects, ['ais_received', 'peer_meps_that_timed_out', 'missing', 'auto_missing', 'unexpected', 'local_port_status', 'peer_port_status'], name, value)


                            class RemoteMepsDefects(Entity):
                                """
                                Defects detected from remote MEPs
                                
                                .. attribute:: loss_threshold_exceeded
                                
                                	Timed out (loss threshold exceeded)
                                	**type**\: bool
                                
                                .. attribute:: invalid_level
                                
                                	Invalid level
                                	**type**\: bool
                                
                                .. attribute:: invalid_maid
                                
                                	Invalid MAID
                                	**type**\: bool
                                
                                .. attribute:: invalid_ccm_interval
                                
                                	Invalid CCM interval
                                	**type**\: bool
                                
                                .. attribute:: received_our_mac
                                
                                	Loop detected (our MAC address received)
                                	**type**\: bool
                                
                                .. attribute:: received_our_mep_id
                                
                                	Configuration Error (our MEP ID received)
                                	**type**\: bool
                                
                                .. attribute:: received_rdi
                                
                                	Remote defection indication received
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects, self).__init__()

                                    self.yang_name = "remote-meps-defects"
                                    self.yang_parent_name = "defects"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('loss_threshold_exceeded', (YLeaf(YType.boolean, 'loss-threshold-exceeded'), ['bool'])),
                                        ('invalid_level', (YLeaf(YType.boolean, 'invalid-level'), ['bool'])),
                                        ('invalid_maid', (YLeaf(YType.boolean, 'invalid-maid'), ['bool'])),
                                        ('invalid_ccm_interval', (YLeaf(YType.boolean, 'invalid-ccm-interval'), ['bool'])),
                                        ('received_our_mac', (YLeaf(YType.boolean, 'received-our-mac'), ['bool'])),
                                        ('received_our_mep_id', (YLeaf(YType.boolean, 'received-our-mep-id'), ['bool'])),
                                        ('received_rdi', (YLeaf(YType.boolean, 'received-rdi'), ['bool'])),
                                    ])
                                    self.loss_threshold_exceeded = None
                                    self.invalid_level = None
                                    self.invalid_maid = None
                                    self.invalid_ccm_interval = None
                                    self.received_our_mac = None
                                    self.received_our_mep_id = None
                                    self.received_rdi = None
                                    self._segment_path = lambda: "remote-meps-defects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects, ['loss_threshold_exceeded', 'invalid_level', 'invalid_maid', 'invalid_ccm_interval', 'received_our_mac', 'received_our_mep_id', 'received_rdi'], name, value)


                        class LastStarted(Entity):
                            """
                            Time elapsed since sending last started
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: nanosecond
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted, self).__init__()

                                self.yang_name = "last-started"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                                ])
                                self.seconds = None
                                self.nanoseconds = None
                                self._segment_path = lambda: "last-started"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted, ['seconds', 'nanoseconds'], name, value)


            class InterfaceStatistics(Entity):
                """
                Interface Statistics table
                
                .. attribute:: interface_statistic
                
                	Counters for a particular interface
                	**type**\: list of  		 :py:class:`InterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Nodes.Node.InterfaceStatistics, self).__init__()

                    self.yang_name = "interface-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-statistic", ("interface_statistic", Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic))])
                    self._leafs = OrderedDict()

                    self.interface_statistic = YList(self)
                    self._segment_path = lambda: "interface-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Nodes.Node.InterfaceStatistics, [], name, value)


                class InterfaceStatistic(Entity):
                    """
                    Counters for a particular interface
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: statistics
                    
                    	EFP statistics
                    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics>`
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic, self).__init__()

                        self.yang_name = "interface-statistic"
                        self.yang_parent_name = "interface-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_classes = OrderedDict([("statistics", ("statistics", Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                        ])
                        self.interface = None
                        self.interface_xr = None

                        self.statistics = Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._segment_path = lambda: "interface-statistic" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic, ['interface', 'interface_xr'], name, value)


                    class Statistics(Entity):
                        """
                        EFP statistics
                        
                        .. attribute:: malformed_packets
                        
                        	Number of malformed packets received at this EFP
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_packets
                        
                        	Number of packets dropped at this EFP
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_malformed_opcode
                        
                        	Opcode for last malformed packet
                        	**type**\:  :py:class:`CfmBagOpcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagOpcode>`
                        
                        .. attribute:: last_malformed_reason
                        
                        	Reason last malformed packet was malformed
                        	**type**\:  :py:class:`CfmPmPktAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPktAction>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "interface-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('malformed_packets', (YLeaf(YType.uint64, 'malformed-packets'), ['int'])),
                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                ('last_malformed_opcode', (YLeaf(YType.enumeration, 'last-malformed-opcode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagOpcode', '')])),
                                ('last_malformed_reason', (YLeaf(YType.enumeration, 'last-malformed-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPktAction', '')])),
                            ])
                            self.malformed_packets = None
                            self.dropped_packets = None
                            self.last_malformed_opcode = None
                            self.last_malformed_reason = None
                            self._segment_path = lambda: "statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics, ['malformed_packets', 'dropped_packets', 'last_malformed_opcode', 'last_malformed_reason'], name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: domains
                
                	The number of domains in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: services
                
                	The number of services in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_rate
                
                	The combined rate of CCMs on this card
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_meps
                
                	The number of local MEPs in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_local_meps
                
                	The number of operational local MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_meps
                
                	The number of down\-MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_meps
                
                	The number of up\-MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded
                
                	The number of MEPs for which CCM processing has been offloaded
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at3_3ms
                
                	The number of MEPs offloaded with CCMs at 3.3ms intervals
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at10ms
                
                	The number of MEPs offloaded with CCMs at 10ms intervals
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_misconfigured
                
                	The number of local MEPs disabled due to configuration errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_out_of_resources
                
                	The number of local MEPs disabled due to lack of resources
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_operational_error
                
                	The number of local MEPs disabled due to operational errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps
                
                	The number of peer MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_peer_meps
                
                	The number of operational peer MEPs recorded in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_with_defects
                
                	The number of peer MEPs with defects
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_without_defects
                
                	The number of peer MEPs without defects
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_timed_out
                
                	The number of peer MEPs that have timed out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mips
                
                	The number of MIPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interfaces
                
                	The number of interfaces running CFM
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bridge_domains_and_xconnects
                
                	Number or bridge domains and crossconnects
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_cache_entries
                
                	Number of traceroute cache entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_cache_replies
                
                	Number of traceroute cache replies
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_learning_db_entries
                
                	Number of entries in the CCM learning database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: issu_role
                
                	ISSU Role of CFM\-D, if any
                	**type**\:  :py:class:`CfmBagIssuRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIssuRole>`
                
                .. attribute:: bnm_enabled_links
                
                	Number of BNM Enabled Links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('domains', (YLeaf(YType.uint32, 'domains'), ['int'])),
                        ('services', (YLeaf(YType.uint32, 'services'), ['int'])),
                        ('ccm_rate', (YLeaf(YType.uint32, 'ccm-rate'), ['int'])),
                        ('local_meps', (YLeaf(YType.uint32, 'local-meps'), ['int'])),
                        ('operational_local_meps', (YLeaf(YType.uint32, 'operational-local-meps'), ['int'])),
                        ('down_meps', (YLeaf(YType.uint32, 'down-meps'), ['int'])),
                        ('up_meps', (YLeaf(YType.uint32, 'up-meps'), ['int'])),
                        ('offloaded', (YLeaf(YType.uint32, 'offloaded'), ['int'])),
                        ('offloaded_at3_3ms', (YLeaf(YType.uint32, 'offloaded-at3-3ms'), ['int'])),
                        ('offloaded_at10ms', (YLeaf(YType.uint32, 'offloaded-at10ms'), ['int'])),
                        ('disabled_misconfigured', (YLeaf(YType.uint32, 'disabled-misconfigured'), ['int'])),
                        ('disabled_out_of_resources', (YLeaf(YType.uint32, 'disabled-out-of-resources'), ['int'])),
                        ('disabled_operational_error', (YLeaf(YType.uint32, 'disabled-operational-error'), ['int'])),
                        ('peer_meps', (YLeaf(YType.uint32, 'peer-meps'), ['int'])),
                        ('operational_peer_meps', (YLeaf(YType.uint32, 'operational-peer-meps'), ['int'])),
                        ('peer_meps_with_defects', (YLeaf(YType.uint32, 'peer-meps-with-defects'), ['int'])),
                        ('peer_meps_without_defects', (YLeaf(YType.uint32, 'peer-meps-without-defects'), ['int'])),
                        ('peer_meps_timed_out', (YLeaf(YType.uint32, 'peer-meps-timed-out'), ['int'])),
                        ('mips', (YLeaf(YType.uint32, 'mips'), ['int'])),
                        ('interfaces', (YLeaf(YType.uint32, 'interfaces'), ['int'])),
                        ('bridge_domains_and_xconnects', (YLeaf(YType.uint32, 'bridge-domains-and-xconnects'), ['int'])),
                        ('traceroute_cache_entries', (YLeaf(YType.uint32, 'traceroute-cache-entries'), ['int'])),
                        ('traceroute_cache_replies', (YLeaf(YType.uint32, 'traceroute-cache-replies'), ['int'])),
                        ('ccm_learning_db_entries', (YLeaf(YType.uint32, 'ccm-learning-db-entries'), ['int'])),
                        ('issu_role', (YLeaf(YType.enumeration, 'issu-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIssuRole', '')])),
                        ('bnm_enabled_links', (YLeaf(YType.uint32, 'bnm-enabled-links'), ['int'])),
                    ])
                    self.domains = None
                    self.services = None
                    self.ccm_rate = None
                    self.local_meps = None
                    self.operational_local_meps = None
                    self.down_meps = None
                    self.up_meps = None
                    self.offloaded = None
                    self.offloaded_at3_3ms = None
                    self.offloaded_at10ms = None
                    self.disabled_misconfigured = None
                    self.disabled_out_of_resources = None
                    self.disabled_operational_error = None
                    self.peer_meps = None
                    self.operational_peer_meps = None
                    self.peer_meps_with_defects = None
                    self.peer_meps_without_defects = None
                    self.peer_meps_timed_out = None
                    self.mips = None
                    self.interfaces = None
                    self.bridge_domains_and_xconnects = None
                    self.traceroute_cache_entries = None
                    self.traceroute_cache_replies = None
                    self.ccm_learning_db_entries = None
                    self.issu_role = None
                    self.bnm_enabled_links = None
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Nodes.Node.Summary, [u'domains', u'services', u'ccm_rate', u'local_meps', u'operational_local_meps', u'down_meps', u'up_meps', u'offloaded', u'offloaded_at3_3ms', u'offloaded_at10ms', u'disabled_misconfigured', u'disabled_out_of_resources', u'disabled_operational_error', u'peer_meps', u'operational_peer_meps', u'peer_meps_with_defects', u'peer_meps_without_defects', u'peer_meps_timed_out', u'mips', u'interfaces', u'bridge_domains_and_xconnects', u'traceroute_cache_entries', u'traceroute_cache_replies', u'ccm_learning_db_entries', u'issu_role', u'bnm_enabled_links'], name, value)


            class CcmLearningDatabases(Entity):
                """
                CCMLearningDatabase table
                
                .. attribute:: ccm_learning_database
                
                	CCM Learning Database entry
                	**type**\: list of  		 :py:class:`CcmLearningDatabase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Nodes.Node.CcmLearningDatabases, self).__init__()

                    self.yang_name = "ccm-learning-databases"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ccm-learning-database", ("ccm_learning_database", Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase))])
                    self._leafs = OrderedDict()

                    self.ccm_learning_database = YList(self)
                    self._segment_path = lambda: "ccm-learning-databases"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Nodes.Node.CcmLearningDatabases, [], name, value)


                class CcmLearningDatabase(Entity):
                    """
                    CCM Learning Database entry
                    
                    .. attribute:: domain  (key)
                    
                    	Maintenance Domain
                    	**type**\: str
                    
                    	**length:** 1..79
                    
                    .. attribute:: service  (key)
                    
                    	Service (Maintenance Association)
                    	**type**\: str
                    
                    	**length:** 1..79
                    
                    .. attribute:: mac_address  (key)
                    
                    	MAC Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain_xr
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: service_xr
                    
                    	Maintenance association name
                    	**type**\: str
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: ingress_interface
                    
                    	The XID of the ingress interface for the CCM
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stale
                    
                    	The XID is stale and may have been reused for a different interface
                    	**type**\: bool
                    
                    .. attribute:: ingress_interface_string
                    
                    	String representation of the Bridge Domain or Cross\-Connect associated with the ingress XID
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase, self).__init__()

                        self.yang_name = "ccm-learning-database"
                        self.yang_parent_name = "ccm-learning-databases"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['domain','service','mac_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                            ('service', (YLeaf(YType.str, 'service'), ['str'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('domain_xr', (YLeaf(YType.str, 'domain-xr'), ['str'])),
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('service_xr', (YLeaf(YType.str, 'service-xr'), ['str'])),
                            ('source_mac_address', (YLeaf(YType.str, 'source-mac-address'), ['str'])),
                            ('ingress_interface', (YLeaf(YType.uint32, 'ingress-interface'), ['int'])),
                            ('stale', (YLeaf(YType.boolean, 'stale'), ['bool'])),
                            ('ingress_interface_string', (YLeaf(YType.str, 'ingress-interface-string'), ['str'])),
                        ])
                        self.domain = None
                        self.service = None
                        self.mac_address = None
                        self.domain_xr = None
                        self.level = None
                        self.service_xr = None
                        self.source_mac_address = None
                        self.ingress_interface = None
                        self.stale = None
                        self.ingress_interface_string = None
                        self._segment_path = lambda: "ccm-learning-database" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[mac-address='" + str(self.mac_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase, ['domain', 'service', 'mac_address', 'domain_xr', 'level', 'service_xr', 'source_mac_address', 'ingress_interface', 'stale', 'ingress_interface_string'], name, value)


    class Global(Entity):
        """
        Global operational data
        
        .. attribute:: incomplete_traceroutes
        
        	Incomplete Traceroute table
        	**type**\:  :py:class:`IncompleteTraceroutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes>`
        
        .. attribute:: maintenance_points
        
        	Maintenance Points table
        	**type**\:  :py:class:`MaintenancePoints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints>`
        
        .. attribute:: global_configuration_errors
        
        	Global configuration errors table
        	**type**\:  :py:class:`GlobalConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors>`
        
        .. attribute:: mep_configuration_errors
        
        	MEP configuration errors table
        	**type**\:  :py:class:`MepConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors>`
        
        .. attribute:: traceroute_caches
        
        	Traceroute Cache table
        	**type**\:  :py:class:`TracerouteCaches <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches>`
        
        .. attribute:: local_meps
        
        	Local MEPs table
        	**type**\:  :py:class:`LocalMeps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps>`
        
        .. attribute:: peer_me_pv2s
        
        	Peer MEPs table Version 2
        	**type**\:  :py:class:`PeerMePv2s <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s>`
        
        

        """

        _prefix = 'ethernet-cfm-oper'
        _revision = '2017-10-06'

        def __init__(self):
            super(Cfm.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "cfm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("incomplete-traceroutes", ("incomplete_traceroutes", Cfm.Global.IncompleteTraceroutes)), ("maintenance-points", ("maintenance_points", Cfm.Global.MaintenancePoints)), ("global-configuration-errors", ("global_configuration_errors", Cfm.Global.GlobalConfigurationErrors)), ("mep-configuration-errors", ("mep_configuration_errors", Cfm.Global.MepConfigurationErrors)), ("traceroute-caches", ("traceroute_caches", Cfm.Global.TracerouteCaches)), ("local-meps", ("local_meps", Cfm.Global.LocalMeps)), ("peer-me-pv2s", ("peer_me_pv2s", Cfm.Global.PeerMePv2s))])
            self._leafs = OrderedDict()

            self.incomplete_traceroutes = Cfm.Global.IncompleteTraceroutes()
            self.incomplete_traceroutes.parent = self
            self._children_name_map["incomplete_traceroutes"] = "incomplete-traceroutes"

            self.maintenance_points = Cfm.Global.MaintenancePoints()
            self.maintenance_points.parent = self
            self._children_name_map["maintenance_points"] = "maintenance-points"

            self.global_configuration_errors = Cfm.Global.GlobalConfigurationErrors()
            self.global_configuration_errors.parent = self
            self._children_name_map["global_configuration_errors"] = "global-configuration-errors"

            self.mep_configuration_errors = Cfm.Global.MepConfigurationErrors()
            self.mep_configuration_errors.parent = self
            self._children_name_map["mep_configuration_errors"] = "mep-configuration-errors"

            self.traceroute_caches = Cfm.Global.TracerouteCaches()
            self.traceroute_caches.parent = self
            self._children_name_map["traceroute_caches"] = "traceroute-caches"

            self.local_meps = Cfm.Global.LocalMeps()
            self.local_meps.parent = self
            self._children_name_map["local_meps"] = "local-meps"

            self.peer_me_pv2s = Cfm.Global.PeerMePv2s()
            self.peer_me_pv2s.parent = self
            self._children_name_map["peer_me_pv2s"] = "peer-me-pv2s"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Cfm.Global, [], name, value)


        class IncompleteTraceroutes(Entity):
            """
            Incomplete Traceroute table
            
            .. attribute:: incomplete_traceroute
            
            	Information about a traceroute operation that has not yet timed out
            	**type**\: list of  		 :py:class:`IncompleteTraceroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.IncompleteTraceroutes, self).__init__()

                self.yang_name = "incomplete-traceroutes"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("incomplete-traceroute", ("incomplete_traceroute", Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute))])
                self._leafs = OrderedDict()

                self.incomplete_traceroute = YList(self)
                self._segment_path = lambda: "incomplete-traceroutes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.IncompleteTraceroutes, [], name, value)


            class IncompleteTraceroute(Entity):
                """
                Information about a traceroute operation that
                has not yet timed out
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  (key)
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: transaction_id  (key)
                
                	Transaction ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\:  :py:class:`TracerouteInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation>`
                
                .. attribute:: time_left
                
                	Time (in seconds) before the traceroute completes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute, self).__init__()

                    self.yang_name = "incomplete-traceroute"
                    self.yang_parent_name = "incomplete-traceroutes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','mep_id','interface','transaction_id']
                    self._child_classes = OrderedDict([("traceroute-information", ("traceroute_information", Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                        ('time_left', (YLeaf(YType.uint64, 'time-left'), ['int'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.transaction_id = None
                    self.time_left = None

                    self.traceroute_information = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation()
                    self.traceroute_information.parent = self
                    self._children_name_map["traceroute_information"] = "traceroute-information"
                    self._segment_path = lambda: "incomplete-traceroute" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[mep-id='" + str(self.mep_id) + "']" + "[interface='" + str(self.interface) + "']" + "[transaction-id='" + str(self.transaction_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/incomplete-traceroutes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute, ['domain', 'service', 'mep_id', 'interface', 'transaction_id', 'time_left'], name, value)


                class TracerouteInformation(Entity):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options>`
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mep_id
                    
                    	Target MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: timestamp
                    
                    	Timestamp of initiation time (seconds)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation, self).__init__()

                        self.yang_name = "traceroute-information"
                        self.yang_parent_name = "incomplete-traceroute"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("options", ("options", Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options))])
                        self._leafs = OrderedDict([
                            ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                            ('service', (YLeaf(YType.str, 'service'), ['str'])),
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('source_mep_id', (YLeaf(YType.uint16, 'source-mep-id'), ['int'])),
                            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                            ('source_mac_address', (YLeaf(YType.str, 'source-mac-address'), ['str'])),
                            ('target_mac_address', (YLeaf(YType.str, 'target-mac-address'), ['str'])),
                            ('directed_mac_address', (YLeaf(YType.str, 'directed-mac-address'), ['str'])),
                            ('target_mep_id', (YLeaf(YType.uint16, 'target-mep-id'), ['int'])),
                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                            ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                            ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                        ])
                        self.domain = None
                        self.service = None
                        self.level = None
                        self.source_mep_id = None
                        self.source_interface = None
                        self.source_mac_address = None
                        self.target_mac_address = None
                        self.directed_mac_address = None
                        self.target_mep_id = None
                        self.timestamp = None
                        self.ttl = None
                        self.transaction_id = None

                        self.options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options()
                        self.options.parent = self
                        self._children_name_map["options"] = "options"
                        self._segment_path = lambda: "traceroute-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation, ['domain', 'service', 'level', 'source_mep_id', 'source_interface', 'source_mac_address', 'target_mac_address', 'directed_mac_address', 'target_mep_id', 'timestamp', 'ttl', 'transaction_id'], name, value)


                    class Options(Entity):
                        """
                        Options affecting traceroute behavior
                        
                        .. attribute:: basic_options
                        
                        	Options for a basic IEEE 802.1ag Linktrace
                        	**type**\:  :py:class:`BasicOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\:  :py:class:`ExploratoryOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\:  :py:class:`CfmPmLtMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtMode>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options, self).__init__()

                            self.yang_name = "options"
                            self.yang_parent_name = "traceroute-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("basic-options", ("basic_options", Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions)), ("exploratory-options", ("exploratory_options", Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions))])
                            self._leafs = OrderedDict([
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtMode', '')])),
                            ])
                            self.mode = None

                            self.basic_options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self._children_name_map["basic_options"] = "basic-options"

                            self.exploratory_options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self._children_name_map["exploratory_options"] = "exploratory-options"
                            self._segment_path = lambda: "options"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options, ['mode'], name, value)


                        class BasicOptions(Entity):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\: bool
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions, self).__init__()

                                self.yang_name = "basic-options"
                                self.yang_parent_name = "options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_auto', (YLeaf(YType.boolean, 'is-auto'), ['bool'])),
                                    ('fdb_only', (YLeaf(YType.boolean, 'fdb-only'), ['bool'])),
                                ])
                                self.is_auto = None
                                self.fdb_only = None
                                self._segment_path = lambda: "basic-options"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions, ['is_auto', 'fdb_only'], name, value)


                        class ExploratoryOptions(Entity):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\:  :py:class:`CfmPmEltDelayModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModel>`
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\:  :py:class:`CfmPmElmReplyFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilter>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions, self).__init__()

                                self.yang_name = "exploratory-options"
                                self.yang_parent_name = "options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('delay_model', (YLeaf(YType.enumeration, 'delay-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel', '')])),
                                    ('delay_constant_factor', (YLeaf(YType.uint32, 'delay-constant-factor'), ['int'])),
                                    ('reply_filter', (YLeaf(YType.enumeration, 'reply-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilter', '')])),
                                ])
                                self.delay_model = None
                                self.delay_constant_factor = None
                                self.reply_filter = None
                                self._segment_path = lambda: "exploratory-options"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions, ['delay_model', 'delay_constant_factor', 'reply_filter'], name, value)


        class MaintenancePoints(Entity):
            """
            Maintenance Points table
            
            .. attribute:: maintenance_point
            
            	Information about a particular Maintenance Point
            	**type**\: list of  		 :py:class:`MaintenancePoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints.MaintenancePoint>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.MaintenancePoints, self).__init__()

                self.yang_name = "maintenance-points"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("maintenance-point", ("maintenance_point", Cfm.Global.MaintenancePoints.MaintenancePoint))])
                self._leafs = OrderedDict()

                self.maintenance_point = YList(self)
                self._segment_path = lambda: "maintenance-points"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.MaintenancePoints, [], name, value)


            class MaintenancePoint(Entity):
                """
                Information about a particular Maintenance
                Point
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: maintenance_point
                
                	Maintenance Point
                	**type**\:  :py:class:`MaintenancePoint_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint_>`
                
                .. attribute:: mep_has_error
                
                	MEP error flag
                	**type**\: bool
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.MaintenancePoints.MaintenancePoint, self).__init__()

                    self.yang_name = "maintenance-point"
                    self.yang_parent_name = "maintenance-points"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','interface']
                    self._child_classes = OrderedDict([("maintenance-point", ("maintenance_point", Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint_))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('mep_has_error', (YLeaf(YType.boolean, 'mep-has-error'), ['bool'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.interface = None
                    self.mep_has_error = None
                    self.mac_address = None

                    self.maintenance_point = Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint_()
                    self.maintenance_point.parent = self
                    self._children_name_map["maintenance_point"] = "maintenance-point"
                    self._segment_path = lambda: "maintenance-point" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/maintenance-points/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.MaintenancePoints.MaintenancePoint, ['domain', 'service', 'interface', u'mep_has_error', u'mac_address'], name, value)


                class MaintenancePoint_(Entity):
                    """
                    Maintenance Point
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\:  :py:class:`CfmMaMpVariety <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVariety>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint_, self).__init__()

                        self.yang_name = "maintenance-point"
                        self.yang_parent_name = "maintenance-point"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('maintenance_point_type', (YLeaf(YType.enumeration, 'maintenance-point-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVariety', '')])),
                            ('mep_id', (YLeaf(YType.uint16, 'mep-id'), ['int'])),
                        ])
                        self.domain_name = None
                        self.level = None
                        self.service_name = None
                        self.interface = None
                        self.maintenance_point_type = None
                        self.mep_id = None
                        self._segment_path = lambda: "maintenance-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint_, [u'domain_name', u'level', u'service_name', u'interface', u'maintenance_point_type', u'mep_id'], name, value)


        class GlobalConfigurationErrors(Entity):
            """
            Global configuration errors table
            
            .. attribute:: global_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of  		 :py:class:`GlobalConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.GlobalConfigurationErrors, self).__init__()

                self.yang_name = "global-configuration-errors"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("global-configuration-error", ("global_configuration_error", Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError))])
                self._leafs = OrderedDict()

                self.global_configuration_error = YList(self)
                self._segment_path = lambda: "global-configuration-errors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.GlobalConfigurationErrors, [], name, value)


            class GlobalConfigurationError(Entity):
                """
                Information about a particular configuration
                error
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: bridge_domain_id
                
                	BD/XC ID, or Service name if the Service is 'down\-only'
                	**type**\:  :py:class:`BridgeDomainId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId>`
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                .. attribute:: level
                
                	Level
                	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                
                .. attribute:: service_name
                
                	Service name
                	**type**\: str
                
                .. attribute:: bridge_domain_is_configured
                
                	The BD/XC is configured globally
                	**type**\: bool
                
                .. attribute:: l2_fib_download_error
                
                	The BD/XC could not be downloaded to L2FIB
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError, self).__init__()

                    self.yang_name = "global-configuration-error"
                    self.yang_parent_name = "global-configuration-errors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service']
                    self._child_classes = OrderedDict([("bridge-domain-id", ("bridge_domain_id", Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                        ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                        ('bridge_domain_is_configured', (YLeaf(YType.boolean, 'bridge-domain-is-configured'), ['bool'])),
                        ('l2_fib_download_error', (YLeaf(YType.boolean, 'l2-fib-download-error'), ['bool'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.domain_name = None
                    self.level = None
                    self.service_name = None
                    self.bridge_domain_is_configured = None
                    self.l2_fib_download_error = None

                    self.bridge_domain_id = Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId()
                    self.bridge_domain_id.parent = self
                    self._children_name_map["bridge_domain_id"] = "bridge-domain-id"
                    self._segment_path = lambda: "global-configuration-error" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/global-configuration-errors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError, ['domain', 'service', 'domain_name', 'level', 'service_name', 'bridge_domain_is_configured', 'l2_fib_download_error'], name, value)


                class BridgeDomainId(Entity):
                    """
                    BD/XC ID, or Service name if the Service is
                    'down\-only'
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:  :py:class:`CfmBagBdidFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmt>`
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: evi
                    
                    	EVPN ID for VLAN\-aware flexible cross\-connects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId, self).__init__()

                        self.yang_name = "bridge-domain-id"
                        self.yang_parent_name = "global-configuration-error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bridge_domain_id_format', (YLeaf(YType.enumeration, 'bridge-domain-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt', '')])),
                            ('group', (YLeaf(YType.str, 'group'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('ce_id', (YLeaf(YType.uint16, 'ce-id'), ['int'])),
                            ('remote_ce_id', (YLeaf(YType.uint16, 'remote-ce-id'), ['int'])),
                            ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ])
                        self.bridge_domain_id_format = None
                        self.group = None
                        self.name = None
                        self.ce_id = None
                        self.remote_ce_id = None
                        self.evi = None
                        self._segment_path = lambda: "bridge-domain-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId, [u'bridge_domain_id_format', u'group', u'name', u'ce_id', u'remote_ce_id', u'evi'], name, value)


        class MepConfigurationErrors(Entity):
            """
            MEP configuration errors table
            
            .. attribute:: mep_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of  		 :py:class:`MepConfigurationError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.MepConfigurationErrors, self).__init__()

                self.yang_name = "mep-configuration-errors"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mep-configuration-error", ("mep_configuration_error", Cfm.Global.MepConfigurationErrors.MepConfigurationError))])
                self._leafs = OrderedDict()

                self.mep_configuration_error = YList(self)
                self._segment_path = lambda: "mep-configuration-errors"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.MepConfigurationErrors, [], name, value)


            class MepConfigurationError(Entity):
                """
                Information about a particular configuration
                error
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: mep
                
                	The MEP that has errors
                	**type**\:  :py:class:`Mep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep>`
                
                .. attribute:: service_bridge_domain
                
                	BD/XC ID for the MEP's Service, or Service name if the Service is 'down\-only'
                	**type**\:  :py:class:`ServiceBridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain>`
                
                .. attribute:: interface_bridge_domain
                
                	ID of the BD/XC that the MEP's EFP is in, if any
                	**type**\:  :py:class:`InterfaceBridgeDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain>`
                
                .. attribute:: satellite_capabilities
                
                	Satellite Capabilities
                	**type**\:  :py:class:`SatelliteCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities>`
                
                .. attribute:: ccm_interval
                
                	Interval between CCMs sent on this MEP
                	**type**\:  :py:class:`CfmBagCcmInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmInterval>`
                
                .. attribute:: no_domain
                
                	The MEP's Domain is not configured
                	**type**\: bool
                
                .. attribute:: no_service
                
                	The MEP's Service is not configured
                	**type**\: bool
                
                .. attribute:: bridge_domain_mismatch
                
                	The MEP's EFP is not in the Service's Bridge Domain
                	**type**\: bool
                
                .. attribute:: level_conflict
                
                	Another MEP facing in the same direction is at the same Maintenance Level
                	**type**\: bool
                
                .. attribute:: ccm_interval_not_supported
                
                	CCM Interval is less than minimum interval supported by hardware
                	**type**\: bool
                
                .. attribute:: offload_out_of_resources
                
                	Offload resource limits have been exceeded
                	**type**\: bool
                
                .. attribute:: offload_multiple_local_mep
                
                	Multiple offloaded MEPs on the same interface are not supported
                	**type**\: bool
                
                .. attribute:: offload_no_cross_check
                
                	The MEP should be offloaded but crosscheck has not been configured
                	**type**\: bool
                
                .. attribute:: offload_multiple_peer_meps
                
                	The MEP should be offloaded but multiple crosscheck MEPs have been configured, and this is not supported
                	**type**\: bool
                
                .. attribute:: offload_mep_direction_not_supported
                
                	The MEP direction does not support offload
                	**type**\: bool
                
                .. attribute:: ais_configured
                
                	AIS is configured on the same interface as the down MEP
                	**type**\: bool
                
                .. attribute:: bundle_level0
                
                	The MEP is configured in a domain at level 0, on a bundle interface or sub\-interface.  This is not supported
                	**type**\: bool
                
                .. attribute:: bridge_domain_not_in_bd_infra
                
                	A BD/XC specified in the MEG config, but it does not exist globally
                	**type**\: bool
                
                .. attribute:: maid_format_not_supported
                
                	The configured MAID format is not supported for hardware offload
                	**type**\: bool
                
                .. attribute:: sman_format_not_supported
                
                	The configured SMAN format is not supported for hardware offload
                	**type**\: bool
                
                .. attribute:: mdid_format_not_supported
                
                	The configured MDID format is not supported for hardware offload
                	**type**\: bool
                
                .. attribute:: fatal_offload_error
                
                	The platform returned a fatal error when passed the offload session
                	**type**\: bool
                
                .. attribute:: satellite_limitation
                
                	A satellite limitation is preventing MEP being offloaded to satellite
                	**type**\: bool
                
                .. attribute:: sla_loopback_operations_disabled
                
                	In\-progress Ethernet SLA loopback operations are disabled due to satellite having loopback responder\-only capabilities
                	**type**\: bool
                
                .. attribute:: sla_synthetic_loss_operations_disabled
                
                	In\-progress Ethernet SLA synthetic loss measurement operations are disabled due to satellite having synthetic loss measurement responder\-only capabilities
                	**type**\: bool
                
                .. attribute:: sla_delay_measurement_operations_disabled
                
                	In\-progress Ethernet SLA delay measurement operations are disabled due to satellite having delay measurement responder\-only capabilities
                	**type**\: bool
                
                .. attribute:: no_valid_mac_address
                
                	The EFP doesn't have a valid MAC address yet. This will also get set if the MAC address we have is a multicast address
                	**type**\: bool
                
                .. attribute:: no_interface_type
                
                	We haven't yet been able to look up the interface type to find whether the interface is a bundle
                	**type**\: bool
                
                .. attribute:: not_in_im
                
                	The EFP has been deleted from IM
                	**type**\: bool
                
                .. attribute:: no_mlacp
                
                	The EFP is a bundle and the mLACP mode is not yet known
                	**type**\: bool
                
                .. attribute:: satellite_error_string
                
                	Error string returned from satellite
                	**type**\: str
                
                .. attribute:: satellite_id
                
                	ID of the satellite
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.MepConfigurationErrors.MepConfigurationError, self).__init__()

                    self.yang_name = "mep-configuration-error"
                    self.yang_parent_name = "mep-configuration-errors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','interface']
                    self._child_classes = OrderedDict([("mep", ("mep", Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep)), ("service-bridge-domain", ("service_bridge_domain", Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain)), ("interface-bridge-domain", ("interface_bridge_domain", Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain)), ("satellite-capabilities", ("satellite_capabilities", Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('ccm_interval', (YLeaf(YType.enumeration, 'ccm-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval', '')])),
                        ('no_domain', (YLeaf(YType.boolean, 'no-domain'), ['bool'])),
                        ('no_service', (YLeaf(YType.boolean, 'no-service'), ['bool'])),
                        ('bridge_domain_mismatch', (YLeaf(YType.boolean, 'bridge-domain-mismatch'), ['bool'])),
                        ('level_conflict', (YLeaf(YType.boolean, 'level-conflict'), ['bool'])),
                        ('ccm_interval_not_supported', (YLeaf(YType.boolean, 'ccm-interval-not-supported'), ['bool'])),
                        ('offload_out_of_resources', (YLeaf(YType.boolean, 'offload-out-of-resources'), ['bool'])),
                        ('offload_multiple_local_mep', (YLeaf(YType.boolean, 'offload-multiple-local-mep'), ['bool'])),
                        ('offload_no_cross_check', (YLeaf(YType.boolean, 'offload-no-cross-check'), ['bool'])),
                        ('offload_multiple_peer_meps', (YLeaf(YType.boolean, 'offload-multiple-peer-meps'), ['bool'])),
                        ('offload_mep_direction_not_supported', (YLeaf(YType.boolean, 'offload-mep-direction-not-supported'), ['bool'])),
                        ('ais_configured', (YLeaf(YType.boolean, 'ais-configured'), ['bool'])),
                        ('bundle_level0', (YLeaf(YType.boolean, 'bundle-level0'), ['bool'])),
                        ('bridge_domain_not_in_bd_infra', (YLeaf(YType.boolean, 'bridge-domain-not-in-bd-infra'), ['bool'])),
                        ('maid_format_not_supported', (YLeaf(YType.boolean, 'maid-format-not-supported'), ['bool'])),
                        ('sman_format_not_supported', (YLeaf(YType.boolean, 'sman-format-not-supported'), ['bool'])),
                        ('mdid_format_not_supported', (YLeaf(YType.boolean, 'mdid-format-not-supported'), ['bool'])),
                        ('fatal_offload_error', (YLeaf(YType.boolean, 'fatal-offload-error'), ['bool'])),
                        ('satellite_limitation', (YLeaf(YType.boolean, 'satellite-limitation'), ['bool'])),
                        ('sla_loopback_operations_disabled', (YLeaf(YType.boolean, 'sla-loopback-operations-disabled'), ['bool'])),
                        ('sla_synthetic_loss_operations_disabled', (YLeaf(YType.boolean, 'sla-synthetic-loss-operations-disabled'), ['bool'])),
                        ('sla_delay_measurement_operations_disabled', (YLeaf(YType.boolean, 'sla-delay-measurement-operations-disabled'), ['bool'])),
                        ('no_valid_mac_address', (YLeaf(YType.boolean, 'no-valid-mac-address'), ['bool'])),
                        ('no_interface_type', (YLeaf(YType.boolean, 'no-interface-type'), ['bool'])),
                        ('not_in_im', (YLeaf(YType.boolean, 'not-in-im'), ['bool'])),
                        ('no_mlacp', (YLeaf(YType.boolean, 'no-mlacp'), ['bool'])),
                        ('satellite_error_string', (YLeaf(YType.str, 'satellite-error-string'), ['str'])),
                        ('satellite_id', (YLeaf(YType.uint16, 'satellite-id'), ['int'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.interface = None
                    self.ccm_interval = None
                    self.no_domain = None
                    self.no_service = None
                    self.bridge_domain_mismatch = None
                    self.level_conflict = None
                    self.ccm_interval_not_supported = None
                    self.offload_out_of_resources = None
                    self.offload_multiple_local_mep = None
                    self.offload_no_cross_check = None
                    self.offload_multiple_peer_meps = None
                    self.offload_mep_direction_not_supported = None
                    self.ais_configured = None
                    self.bundle_level0 = None
                    self.bridge_domain_not_in_bd_infra = None
                    self.maid_format_not_supported = None
                    self.sman_format_not_supported = None
                    self.mdid_format_not_supported = None
                    self.fatal_offload_error = None
                    self.satellite_limitation = None
                    self.sla_loopback_operations_disabled = None
                    self.sla_synthetic_loss_operations_disabled = None
                    self.sla_delay_measurement_operations_disabled = None
                    self.no_valid_mac_address = None
                    self.no_interface_type = None
                    self.not_in_im = None
                    self.no_mlacp = None
                    self.satellite_error_string = None
                    self.satellite_id = None

                    self.mep = Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep()
                    self.mep.parent = self
                    self._children_name_map["mep"] = "mep"

                    self.service_bridge_domain = Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain()
                    self.service_bridge_domain.parent = self
                    self._children_name_map["service_bridge_domain"] = "service-bridge-domain"

                    self.interface_bridge_domain = Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain()
                    self.interface_bridge_domain.parent = self
                    self._children_name_map["interface_bridge_domain"] = "interface-bridge-domain"

                    self.satellite_capabilities = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities()
                    self.satellite_capabilities.parent = self
                    self._children_name_map["satellite_capabilities"] = "satellite-capabilities"
                    self._segment_path = lambda: "mep-configuration-error" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/mep-configuration-errors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError, ['domain', 'service', 'interface', u'ccm_interval', u'no_domain', u'no_service', u'bridge_domain_mismatch', u'level_conflict', u'ccm_interval_not_supported', u'offload_out_of_resources', u'offload_multiple_local_mep', u'offload_no_cross_check', u'offload_multiple_peer_meps', u'offload_mep_direction_not_supported', u'ais_configured', u'bundle_level0', u'bridge_domain_not_in_bd_infra', u'maid_format_not_supported', u'sman_format_not_supported', u'mdid_format_not_supported', u'fatal_offload_error', u'satellite_limitation', u'sla_loopback_operations_disabled', u'sla_synthetic_loss_operations_disabled', u'sla_delay_measurement_operations_disabled', u'no_valid_mac_address', u'no_interface_type', u'not_in_im', u'no_mlacp', u'satellite_error_string', u'satellite_id'], name, value)


                class Mep(Entity):
                    """
                    The MEP that has errors
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\:  :py:class:`CfmMaMpVariety <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVariety>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep, self).__init__()

                        self.yang_name = "mep"
                        self.yang_parent_name = "mep-configuration-error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('maintenance_point_type', (YLeaf(YType.enumeration, 'maintenance-point-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVariety', '')])),
                            ('mep_id', (YLeaf(YType.uint16, 'mep-id'), ['int'])),
                        ])
                        self.domain_name = None
                        self.level = None
                        self.service_name = None
                        self.interface = None
                        self.maintenance_point_type = None
                        self.mep_id = None
                        self._segment_path = lambda: "mep"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep, [u'domain_name', u'level', u'service_name', u'interface', u'maintenance_point_type', u'mep_id'], name, value)


                class ServiceBridgeDomain(Entity):
                    """
                    BD/XC ID for the MEP's Service, or Service name
                    if the Service is 'down\-only'
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:  :py:class:`CfmBagBdidFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmt>`
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: evi
                    
                    	EVPN ID for VLAN\-aware flexible cross\-connects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain, self).__init__()

                        self.yang_name = "service-bridge-domain"
                        self.yang_parent_name = "mep-configuration-error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bridge_domain_id_format', (YLeaf(YType.enumeration, 'bridge-domain-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt', '')])),
                            ('group', (YLeaf(YType.str, 'group'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('ce_id', (YLeaf(YType.uint16, 'ce-id'), ['int'])),
                            ('remote_ce_id', (YLeaf(YType.uint16, 'remote-ce-id'), ['int'])),
                            ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ])
                        self.bridge_domain_id_format = None
                        self.group = None
                        self.name = None
                        self.ce_id = None
                        self.remote_ce_id = None
                        self.evi = None
                        self._segment_path = lambda: "service-bridge-domain"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain, [u'bridge_domain_id_format', u'group', u'name', u'ce_id', u'remote_ce_id', u'evi'], name, value)


                class InterfaceBridgeDomain(Entity):
                    """
                    ID of the BD/XC that the MEP's EFP is in, if any
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\:  :py:class:`CfmBagBdidFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmt>`
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: evi
                    
                    	EVPN ID for VLAN\-aware flexible cross\-connects
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain, self).__init__()

                        self.yang_name = "interface-bridge-domain"
                        self.yang_parent_name = "mep-configuration-error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bridge_domain_id_format', (YLeaf(YType.enumeration, 'bridge-domain-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt', '')])),
                            ('group', (YLeaf(YType.str, 'group'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('ce_id', (YLeaf(YType.uint16, 'ce-id'), ['int'])),
                            ('remote_ce_id', (YLeaf(YType.uint16, 'remote-ce-id'), ['int'])),
                            ('evi', (YLeaf(YType.uint32, 'evi'), ['int'])),
                        ])
                        self.bridge_domain_id_format = None
                        self.group = None
                        self.name = None
                        self.ce_id = None
                        self.remote_ce_id = None
                        self.evi = None
                        self._segment_path = lambda: "interface-bridge-domain"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain, [u'bridge_domain_id_format', u'group', u'name', u'ce_id', u'remote_ce_id', u'evi'], name, value)


                class SatelliteCapabilities(Entity):
                    """
                    Satellite Capabilities
                    
                    .. attribute:: loopback
                    
                    	Loopback
                    	**type**\:  :py:class:`Loopback <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback>`
                    
                    .. attribute:: delay_measurement
                    
                    	Delay Measurement
                    	**type**\:  :py:class:`DelayMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement>`
                    
                    .. attribute:: synthetic_loss_measurement
                    
                    	Synthetic Loss Measurement
                    	**type**\:  :py:class:`SyntheticLossMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities, self).__init__()

                        self.yang_name = "satellite-capabilities"
                        self.yang_parent_name = "mep-configuration-error"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("loopback", ("loopback", Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback)), ("delay-measurement", ("delay_measurement", Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement)), ("synthetic-loss-measurement", ("synthetic_loss_measurement", Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement))])
                        self._leafs = OrderedDict()

                        self.loopback = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback()
                        self.loopback.parent = self
                        self._children_name_map["loopback"] = "loopback"

                        self.delay_measurement = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement()
                        self.delay_measurement.parent = self
                        self._children_name_map["delay_measurement"] = "delay-measurement"

                        self.synthetic_loss_measurement = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement()
                        self.synthetic_loss_measurement.parent = self
                        self._children_name_map["synthetic_loss_measurement"] = "synthetic-loss-measurement"
                        self._segment_path = lambda: "satellite-capabilities"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities, [], name, value)


                    class Loopback(Entity):
                        """
                        Loopback
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback, self).__init__()

                            self.yang_name = "loopback"
                            self.yang_parent_name = "satellite-capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('responder', (YLeaf(YType.boolean, 'responder'), ['bool'])),
                                ('controller', (YLeaf(YType.boolean, 'controller'), ['bool'])),
                            ])
                            self.responder = None
                            self.controller = None
                            self._segment_path = lambda: "loopback"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback, [u'responder', u'controller'], name, value)


                    class DelayMeasurement(Entity):
                        """
                        Delay Measurement
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement, self).__init__()

                            self.yang_name = "delay-measurement"
                            self.yang_parent_name = "satellite-capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('responder', (YLeaf(YType.boolean, 'responder'), ['bool'])),
                                ('controller', (YLeaf(YType.boolean, 'controller'), ['bool'])),
                            ])
                            self.responder = None
                            self.controller = None
                            self._segment_path = lambda: "delay-measurement"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement, [u'responder', u'controller'], name, value)


                    class SyntheticLossMeasurement(Entity):
                        """
                        Synthetic Loss Measurement
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement, self).__init__()

                            self.yang_name = "synthetic-loss-measurement"
                            self.yang_parent_name = "satellite-capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('responder', (YLeaf(YType.boolean, 'responder'), ['bool'])),
                                ('controller', (YLeaf(YType.boolean, 'controller'), ['bool'])),
                            ])
                            self.responder = None
                            self.controller = None
                            self._segment_path = lambda: "synthetic-loss-measurement"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement, [u'responder', u'controller'], name, value)


        class TracerouteCaches(Entity):
            """
            Traceroute Cache table
            
            .. attribute:: traceroute_cache
            
            	Information about a particular traceroute operation
            	**type**\: list of  		 :py:class:`TracerouteCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.TracerouteCaches, self).__init__()

                self.yang_name = "traceroute-caches"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traceroute-cache", ("traceroute_cache", Cfm.Global.TracerouteCaches.TracerouteCache))])
                self._leafs = OrderedDict()

                self.traceroute_cache = YList(self)
                self._segment_path = lambda: "traceroute-caches"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.TracerouteCaches, [], name, value)


            class TracerouteCache(Entity):
                """
                Information about a particular traceroute
                operation
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  (key)
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: transaction_id  (key)
                
                	Transaction ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\:  :py:class:`TracerouteInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation>`
                
                .. attribute:: replies_dropped
                
                	Count of ignored replies for this request
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: linktrace_reply
                
                	Received linktrace replies
                	**type**\: list of  		 :py:class:`LinktraceReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply>`
                
                .. attribute:: exploratory_linktrace_reply
                
                	Received exploratory linktrace replies
                	**type**\: list of  		 :py:class:`ExploratoryLinktraceReply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.TracerouteCaches.TracerouteCache, self).__init__()

                    self.yang_name = "traceroute-cache"
                    self.yang_parent_name = "traceroute-caches"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','mep_id','interface','transaction_id']
                    self._child_classes = OrderedDict([("traceroute-information", ("traceroute_information", Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation)), ("linktrace-reply", ("linktrace_reply", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply)), ("exploratory-linktrace-reply", ("exploratory_linktrace_reply", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                        ('replies_dropped', (YLeaf(YType.uint32, 'replies-dropped'), ['int'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.transaction_id = None
                    self.replies_dropped = None

                    self.traceroute_information = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation()
                    self.traceroute_information.parent = self
                    self._children_name_map["traceroute_information"] = "traceroute-information"

                    self.linktrace_reply = YList(self)
                    self.exploratory_linktrace_reply = YList(self)
                    self._segment_path = lambda: "traceroute-cache" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[mep-id='" + str(self.mep_id) + "']" + "[interface='" + str(self.interface) + "']" + "[transaction-id='" + str(self.transaction_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/traceroute-caches/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache, ['domain', 'service', 'mep_id', 'interface', 'transaction_id', 'replies_dropped'], name, value)


                class TracerouteInformation(Entity):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options>`
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: target_mep_id
                    
                    	Target MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: timestamp
                    
                    	Timestamp of initiation time (seconds)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation, self).__init__()

                        self.yang_name = "traceroute-information"
                        self.yang_parent_name = "traceroute-cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("options", ("options", Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options))])
                        self._leafs = OrderedDict([
                            ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                            ('service', (YLeaf(YType.str, 'service'), ['str'])),
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('source_mep_id', (YLeaf(YType.uint16, 'source-mep-id'), ['int'])),
                            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                            ('source_mac_address', (YLeaf(YType.str, 'source-mac-address'), ['str'])),
                            ('target_mac_address', (YLeaf(YType.str, 'target-mac-address'), ['str'])),
                            ('directed_mac_address', (YLeaf(YType.str, 'directed-mac-address'), ['str'])),
                            ('target_mep_id', (YLeaf(YType.uint16, 'target-mep-id'), ['int'])),
                            ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                            ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                            ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                        ])
                        self.domain = None
                        self.service = None
                        self.level = None
                        self.source_mep_id = None
                        self.source_interface = None
                        self.source_mac_address = None
                        self.target_mac_address = None
                        self.directed_mac_address = None
                        self.target_mep_id = None
                        self.timestamp = None
                        self.ttl = None
                        self.transaction_id = None

                        self.options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options()
                        self.options.parent = self
                        self._children_name_map["options"] = "options"
                        self._segment_path = lambda: "traceroute-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation, ['domain', 'service', 'level', 'source_mep_id', 'source_interface', 'source_mac_address', 'target_mac_address', 'directed_mac_address', 'target_mep_id', 'timestamp', 'ttl', 'transaction_id'], name, value)


                    class Options(Entity):
                        """
                        Options affecting traceroute behavior
                        
                        .. attribute:: basic_options
                        
                        	Options for a basic IEEE 802.1ag Linktrace
                        	**type**\:  :py:class:`BasicOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\:  :py:class:`ExploratoryOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\:  :py:class:`CfmPmLtMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtMode>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options, self).__init__()

                            self.yang_name = "options"
                            self.yang_parent_name = "traceroute-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("basic-options", ("basic_options", Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions)), ("exploratory-options", ("exploratory_options", Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions))])
                            self._leafs = OrderedDict([
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtMode', '')])),
                            ])
                            self.mode = None

                            self.basic_options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self._children_name_map["basic_options"] = "basic-options"

                            self.exploratory_options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self._children_name_map["exploratory_options"] = "exploratory-options"
                            self._segment_path = lambda: "options"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options, ['mode'], name, value)


                        class BasicOptions(Entity):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\: bool
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions, self).__init__()

                                self.yang_name = "basic-options"
                                self.yang_parent_name = "options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_auto', (YLeaf(YType.boolean, 'is-auto'), ['bool'])),
                                    ('fdb_only', (YLeaf(YType.boolean, 'fdb-only'), ['bool'])),
                                ])
                                self.is_auto = None
                                self.fdb_only = None
                                self._segment_path = lambda: "basic-options"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions, ['is_auto', 'fdb_only'], name, value)


                        class ExploratoryOptions(Entity):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\:  :py:class:`CfmPmEltDelayModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModel>`
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\:  :py:class:`CfmPmElmReplyFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilter>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions, self).__init__()

                                self.yang_name = "exploratory-options"
                                self.yang_parent_name = "options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('delay_model', (YLeaf(YType.enumeration, 'delay-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel', '')])),
                                    ('delay_constant_factor', (YLeaf(YType.uint32, 'delay-constant-factor'), ['int'])),
                                    ('reply_filter', (YLeaf(YType.enumeration, 'reply-filter'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilter', '')])),
                                ])
                                self.delay_model = None
                                self.delay_constant_factor = None
                                self.reply_filter = None
                                self._segment_path = lambda: "exploratory-options"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions, ['delay_model', 'delay_constant_factor', 'reply_filter'], name, value)


                class LinktraceReply(Entity):
                    """
                    Received linktrace replies
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\:  :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId>`
                    
                    .. attribute:: egress_id
                    
                    	Egress ID TLV
                    	**type**\:  :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\:  :py:class:`ReplyIngress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress>`
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\:  :py:class:`ReplyEgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\:  :py:class:`LastHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of  		 :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply, self).__init__()

                        self.yang_name = "linktrace-reply"
                        self.yang_parent_name = "traceroute-cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("header", ("header", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header)), ("sender-id", ("sender_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId)), ("egress-id", ("egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId)), ("reply-ingress", ("reply_ingress", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress)), ("reply-egress", ("reply_egress", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress)), ("last-hop", ("last_hop", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop)), ("organization-specific-tlv", ("organization_specific_tlv", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv)), ("unknown-tlv", ("unknown_tlv", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv))])
                        self._leafs = OrderedDict([
                            ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                        ])
                        self.raw_data = None

                        self.header = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header()
                        self.header.parent = self
                        self._children_name_map["header"] = "header"

                        self.sender_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self._children_name_map["sender_id"] = "sender-id"

                        self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId()
                        self.egress_id.parent = self
                        self._children_name_map["egress_id"] = "egress-id"

                        self.reply_ingress = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self._children_name_map["reply_ingress"] = "reply-ingress"

                        self.reply_egress = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self._children_name_map["reply_egress"] = "reply-egress"

                        self.last_hop = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self._children_name_map["last_hop"] = "last-hop"

                        self.organization_specific_tlv = YList(self)
                        self.unknown_tlv = YList(self)
                        self._segment_path = lambda: "linktrace-reply"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply, ['raw_data'], name, value)


                    class Header(Entity):
                        """
                        Frame header
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: use_fdb_only
                        
                        	Use filtering DB only
                        	**type**\: bool
                        
                        .. attribute:: forwarded
                        
                        	LTR was forwarded
                        	**type**\: bool
                        
                        .. attribute:: terminal_mep
                        
                        	Terminal MEP reached
                        	**type**\: bool
                        
                        .. attribute:: transaction_id
                        
                        	Transaction ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ttl
                        
                        	TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\:  :py:class:`CfmPmRelayAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRelayAction>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header, self).__init__()

                            self.yang_name = "header"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                                ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                                ('use_fdb_only', (YLeaf(YType.boolean, 'use-fdb-only'), ['bool'])),
                                ('forwarded', (YLeaf(YType.boolean, 'forwarded'), ['bool'])),
                                ('terminal_mep', (YLeaf(YType.boolean, 'terminal-mep'), ['bool'])),
                                ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                                ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                                ('relay_action', (YLeaf(YType.enumeration, 'relay-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRelayAction', '')])),
                            ])
                            self.level = None
                            self.version = None
                            self.use_fdb_only = None
                            self.forwarded = None
                            self.terminal_mep = None
                            self.transaction_id = None
                            self.ttl = None
                            self.relay_action = None
                            self._segment_path = lambda: "header"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header, ['level', 'version', 'use_fdb_only', 'forwarded', 'terminal_mep', 'transaction_id', 'ttl', 'relay_action'], name, value)


                    class SenderId(Entity):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\:  :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId, self).__init__()

                            self.yang_name = "sender-id"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("chassis-id", ("chassis_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId))])
                            self._leafs = OrderedDict([
                                ('management_address_domain', (YLeaf(YType.str, 'management-address-domain'), ['str'])),
                                ('management_address', (YLeaf(YType.str, 'management-address'), ['str'])),
                            ])
                            self.management_address_domain = None
                            self.management_address = None

                            self.chassis_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self._children_name_map["chassis_id"] = "chassis-id"
                            self._segment_path = lambda: "sender-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId, ['management_address_domain', 'management_address'], name, value)


                        class ChassisId(Entity):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\:  :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\:  :py:class:`CfmPmChassisIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmt>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId, self).__init__()

                                self.yang_name = "chassis-id"
                                self.yang_parent_name = "sender-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("chassis-id-value", ("chassis_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue))])
                                self._leafs = OrderedDict([
                                    ('chassis_id_type', (YLeaf(YType.enumeration, 'chassis-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt', '')])),
                                    ('chassis_id_type_value', (YLeaf(YType.uint8, 'chassis-id-type-value'), ['int'])),
                                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                ])
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id = None

                                self.chassis_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self
                                self._children_name_map["chassis_id_value"] = "chassis-id-value"
                                self._segment_path = lambda: "chassis-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId, ['chassis_id_type', 'chassis_id_type_value', 'chassis_id'], name, value)


                            class ChassisIdValue(Entity):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\: str
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue, self).__init__()

                                    self.yang_name = "chassis-id-value"
                                    self.yang_parent_name = "chassis-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('chassis_id_format', (YLeaf(YType.enumeration, 'chassis-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('chassis_id_string', (YLeaf(YType.str, 'chassis-id-string'), ['str'])),
                                        ('chassis_id_mac', (YLeaf(YType.str, 'chassis-id-mac'), ['str'])),
                                        ('chassis_id_raw', (YLeaf(YType.str, 'chassis-id-raw'), ['str'])),
                                    ])
                                    self.chassis_id_format = None
                                    self.chassis_id_string = None
                                    self.chassis_id_mac = None
                                    self.chassis_id_raw = None
                                    self._segment_path = lambda: "chassis-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue, ['chassis_id_format', 'chassis_id_string', 'chassis_id_mac', 'chassis_id_raw'], name, value)


                    class EgressId(Entity):
                        """
                        Egress ID TLV
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\:  :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId>`
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\:  :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId, self).__init__()

                            self.yang_name = "egress-id"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("last-egress-id", ("last_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId)), ("next-egress-id", ("next_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId))])
                            self._leafs = OrderedDict()

                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId()
                            self.last_egress_id.parent = self
                            self._children_name_map["last_egress_id"] = "last-egress-id"

                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId()
                            self.next_egress_id.parent = self
                            self._children_name_map["next_egress_id"] = "next-egress-id"
                            self._segment_path = lambda: "egress-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId, [], name, value)


                        class LastEgressId(Entity):
                            """
                            Last egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId, self).__init__()

                                self.yang_name = "last-egress-id"
                                self.yang_parent_name = "egress-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "last-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId, ['unique_id', 'mac_address'], name, value)


                        class NextEgressId(Entity):
                            """
                            Next egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId, self).__init__()

                                self.yang_name = "next-egress-id"
                                self.yang_parent_name = "egress-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "next-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId, ['unique_id', 'mac_address'], name, value)


                    class ReplyIngress(Entity):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:  :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId>`
                        
                        .. attribute:: action
                        
                        	Reply ingress action
                        	**type**\:  :py:class:`CfmPmIngressAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIngressAction>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress, self).__init__()

                            self.yang_name = "reply-ingress"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("port-id", ("port_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId))])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIngressAction', '')])),
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ])
                            self.action = None
                            self.mac_address = None

                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self
                            self._children_name_map["port_id"] = "port-id"
                            self._segment_path = lambda: "reply-ingress"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress, ['action', 'mac_address'], name, value)


                        class PortId(Entity):
                            """
                            Port ID
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:  :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:  :py:class:`CfmPmPortIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmt>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId, self).__init__()

                                self.yang_name = "port-id"
                                self.yang_parent_name = "reply-ingress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("port-id-value", ("port_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue))])
                                self._leafs = OrderedDict([
                                    ('port_id_type', (YLeaf(YType.enumeration, 'port-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt', '')])),
                                    ('port_id_type_value', (YLeaf(YType.uint8, 'port-id-type-value'), ['int'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                ])
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id = None

                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self
                                self._children_name_map["port_id_value"] = "port-id-value"
                                self._segment_path = lambda: "port-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId, ['port_id_type', 'port_id_type_value', 'port_id'], name, value)


                            class PortIdValue(Entity):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue, self).__init__()

                                    self.yang_name = "port-id-value"
                                    self.yang_parent_name = "port-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port_id_format', (YLeaf(YType.enumeration, 'port-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('port_id_string', (YLeaf(YType.str, 'port-id-string'), ['str'])),
                                        ('port_id_mac', (YLeaf(YType.str, 'port-id-mac'), ['str'])),
                                        ('port_id_raw', (YLeaf(YType.str, 'port-id-raw'), ['str'])),
                                    ])
                                    self.port_id_format = None
                                    self.port_id_string = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self._segment_path = lambda: "port-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue, ['port_id_format', 'port_id_string', 'port_id_mac', 'port_id_raw'], name, value)


                    class ReplyEgress(Entity):
                        """
                        Reply egress TLV
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:  :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId>`
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\:  :py:class:`CfmPmEgressAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEgressAction>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress, self).__init__()

                            self.yang_name = "reply-egress"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("port-id", ("port_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId))])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEgressAction', '')])),
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ])
                            self.action = None
                            self.mac_address = None

                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self
                            self._children_name_map["port_id"] = "port-id"
                            self._segment_path = lambda: "reply-egress"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress, ['action', 'mac_address'], name, value)


                        class PortId(Entity):
                            """
                            Port ID
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:  :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:  :py:class:`CfmPmPortIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmt>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId, self).__init__()

                                self.yang_name = "port-id"
                                self.yang_parent_name = "reply-egress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("port-id-value", ("port_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue))])
                                self._leafs = OrderedDict([
                                    ('port_id_type', (YLeaf(YType.enumeration, 'port-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt', '')])),
                                    ('port_id_type_value', (YLeaf(YType.uint8, 'port-id-type-value'), ['int'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                ])
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id = None

                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self
                                self._children_name_map["port_id_value"] = "port-id-value"
                                self._segment_path = lambda: "port-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId, ['port_id_type', 'port_id_type_value', 'port_id'], name, value)


                            class PortIdValue(Entity):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue, self).__init__()

                                    self.yang_name = "port-id-value"
                                    self.yang_parent_name = "port-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port_id_format', (YLeaf(YType.enumeration, 'port-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('port_id_string', (YLeaf(YType.str, 'port-id-string'), ['str'])),
                                        ('port_id_mac', (YLeaf(YType.str, 'port-id-mac'), ['str'])),
                                        ('port_id_raw', (YLeaf(YType.str, 'port-id-raw'), ['str'])),
                                    ])
                                    self.port_id_format = None
                                    self.port_id_string = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self._segment_path = lambda: "port-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue, ['port_id_format', 'port_id_string', 'port_id_mac', 'port_id_raw'], name, value)


                    class LastHop(Entity):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\:  :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\:  :py:class:`CfmPmLastHopFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmt>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop, self).__init__()

                            self.yang_name = "last-hop"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("egress-id", ("egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId))])
                            self._leafs = OrderedDict([
                                ('last_hop_format', (YLeaf(YType.enumeration, 'last-hop-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmt', '')])),
                                ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ])
                            self.last_hop_format = None
                            self.host_name = None

                            self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self._children_name_map["egress_id"] = "egress-id"
                            self._segment_path = lambda: "last-hop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop, ['last_hop_format', 'host_name'], name, value)


                        class EgressId(Entity):
                            """
                            Egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId, self).__init__()

                                self.yang_name = "egress-id"
                                self.yang_parent_name = "last-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId, ['unique_id', 'mac_address'], name, value)


                    class OrganizationSpecificTlv(Entity):
                        """
                        Organizational\-specific TLVs
                        
                        .. attribute:: oui
                        
                        	Organizationally\-unique ID
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: subtype
                        
                        	Subtype of TLV
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv, self).__init__()

                            self.yang_name = "organization-specific-tlv"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oui', (YLeaf(YType.str, 'oui'), ['str'])),
                                ('subtype', (YLeaf(YType.uint8, 'subtype'), ['int'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.oui = None
                            self.subtype = None
                            self.value = None
                            self._segment_path = lambda: "organization-specific-tlv"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv, ['oui', 'subtype', 'value'], name, value)


                    class UnknownTlv(Entity):
                        """
                        Unknown TLVs
                        
                        .. attribute:: typecode
                        
                        	Type code of TLV
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv, self).__init__()

                            self.yang_name = "unknown-tlv"
                            self.yang_parent_name = "linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('typecode', (YLeaf(YType.uint8, 'typecode'), ['int'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.typecode = None
                            self.value = None
                            self._segment_path = lambda: "unknown-tlv"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv, ['typecode', 'value'], name, value)


                class ExploratoryLinktraceReply(Entity):
                    """
                    Received exploratory linktrace replies
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\:  :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\:  :py:class:`ReplyIngress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress>`
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\:  :py:class:`ReplyEgress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\:  :py:class:`LastHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of  		 :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply, self).__init__()

                        self.yang_name = "exploratory-linktrace-reply"
                        self.yang_parent_name = "traceroute-cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("header", ("header", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header)), ("sender-id", ("sender_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId)), ("reply-ingress", ("reply_ingress", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress)), ("reply-egress", ("reply_egress", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress)), ("last-hop", ("last_hop", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop)), ("organization-specific-tlv", ("organization_specific_tlv", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv)), ("unknown-tlv", ("unknown_tlv", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv))])
                        self._leafs = OrderedDict([
                            ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                        ])
                        self.raw_data = None

                        self.header = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header()
                        self.header.parent = self
                        self._children_name_map["header"] = "header"

                        self.sender_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self._children_name_map["sender_id"] = "sender-id"

                        self.reply_ingress = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self._children_name_map["reply_ingress"] = "reply-ingress"

                        self.reply_egress = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self._children_name_map["reply_egress"] = "reply-egress"

                        self.last_hop = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self._children_name_map["last_hop"] = "last-hop"

                        self.organization_specific_tlv = YList(self)
                        self.unknown_tlv = YList(self)
                        self._segment_path = lambda: "exploratory-linktrace-reply"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply, ['raw_data'], name, value)


                    class Header(Entity):
                        """
                        Frame header
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: forwarded
                        
                        	ELR was forwarded
                        	**type**\: bool
                        
                        .. attribute:: terminal_mep
                        
                        	Terminal MEP reached
                        	**type**\: bool
                        
                        .. attribute:: reply_filter_unknown
                        
                        	Reply Filter unrecognized
                        	**type**\: bool
                        
                        .. attribute:: transaction_id
                        
                        	Transaction ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ttl
                        
                        	TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\:  :py:class:`CfmPmElrRelayAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrRelayAction>`
                        
                        .. attribute:: next_hop_timeout
                        
                        	Next Hop Timeout, in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: delay_model
                        
                        	Delay Model
                        	**type**\:  :py:class:`CfmPmEltDelayModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModel>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header, self).__init__()

                            self.yang_name = "header"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                                ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                                ('forwarded', (YLeaf(YType.boolean, 'forwarded'), ['bool'])),
                                ('terminal_mep', (YLeaf(YType.boolean, 'terminal-mep'), ['bool'])),
                                ('reply_filter_unknown', (YLeaf(YType.boolean, 'reply-filter-unknown'), ['bool'])),
                                ('transaction_id', (YLeaf(YType.uint32, 'transaction-id'), ['int'])),
                                ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                                ('relay_action', (YLeaf(YType.enumeration, 'relay-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrRelayAction', '')])),
                                ('next_hop_timeout', (YLeaf(YType.uint32, 'next-hop-timeout'), ['int'])),
                                ('delay_model', (YLeaf(YType.enumeration, 'delay-model'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel', '')])),
                            ])
                            self.level = None
                            self.version = None
                            self.forwarded = None
                            self.terminal_mep = None
                            self.reply_filter_unknown = None
                            self.transaction_id = None
                            self.ttl = None
                            self.relay_action = None
                            self.next_hop_timeout = None
                            self.delay_model = None
                            self._segment_path = lambda: "header"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header, ['level', 'version', 'forwarded', 'terminal_mep', 'reply_filter_unknown', 'transaction_id', 'ttl', 'relay_action', 'next_hop_timeout', 'delay_model'], name, value)


                    class SenderId(Entity):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\:  :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId, self).__init__()

                            self.yang_name = "sender-id"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("chassis-id", ("chassis_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId))])
                            self._leafs = OrderedDict([
                                ('management_address_domain', (YLeaf(YType.str, 'management-address-domain'), ['str'])),
                                ('management_address', (YLeaf(YType.str, 'management-address'), ['str'])),
                            ])
                            self.management_address_domain = None
                            self.management_address = None

                            self.chassis_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self._children_name_map["chassis_id"] = "chassis-id"
                            self._segment_path = lambda: "sender-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId, ['management_address_domain', 'management_address'], name, value)


                        class ChassisId(Entity):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\:  :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\:  :py:class:`CfmPmChassisIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmt>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId, self).__init__()

                                self.yang_name = "chassis-id"
                                self.yang_parent_name = "sender-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("chassis-id-value", ("chassis_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue))])
                                self._leafs = OrderedDict([
                                    ('chassis_id_type', (YLeaf(YType.enumeration, 'chassis-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt', '')])),
                                    ('chassis_id_type_value', (YLeaf(YType.uint8, 'chassis-id-type-value'), ['int'])),
                                    ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                ])
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id = None

                                self.chassis_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self
                                self._children_name_map["chassis_id_value"] = "chassis-id-value"
                                self._segment_path = lambda: "chassis-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId, ['chassis_id_type', 'chassis_id_type_value', 'chassis_id'], name, value)


                            class ChassisIdValue(Entity):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\: str
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue, self).__init__()

                                    self.yang_name = "chassis-id-value"
                                    self.yang_parent_name = "chassis-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('chassis_id_format', (YLeaf(YType.enumeration, 'chassis-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('chassis_id_string', (YLeaf(YType.str, 'chassis-id-string'), ['str'])),
                                        ('chassis_id_mac', (YLeaf(YType.str, 'chassis-id-mac'), ['str'])),
                                        ('chassis_id_raw', (YLeaf(YType.str, 'chassis-id-raw'), ['str'])),
                                    ])
                                    self.chassis_id_format = None
                                    self.chassis_id_string = None
                                    self.chassis_id_mac = None
                                    self.chassis_id_raw = None
                                    self._segment_path = lambda: "chassis-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue, ['chassis_id_format', 'chassis_id_string', 'chassis_id_mac', 'chassis_id_raw'], name, value)


                    class ReplyIngress(Entity):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\:  :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId>`
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\:  :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:  :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId>`
                        
                        .. attribute:: action
                        
                        	ELR Reply ingress action
                        	**type**\:  :py:class:`CfmPmElrIngressAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrIngressAction>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress, self).__init__()

                            self.yang_name = "reply-ingress"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("last-egress-id", ("last_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId)), ("next-egress-id", ("next_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId)), ("port-id", ("port_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId))])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrIngressAction', '')])),
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ])
                            self.action = None
                            self.mac_address = None

                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId()
                            self.last_egress_id.parent = self
                            self._children_name_map["last_egress_id"] = "last-egress-id"

                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId()
                            self.next_egress_id.parent = self
                            self._children_name_map["next_egress_id"] = "next-egress-id"

                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self
                            self._children_name_map["port_id"] = "port-id"
                            self._segment_path = lambda: "reply-ingress"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress, ['action', 'mac_address'], name, value)


                        class LastEgressId(Entity):
                            """
                            Last egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId, self).__init__()

                                self.yang_name = "last-egress-id"
                                self.yang_parent_name = "reply-ingress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "last-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId, ['unique_id', 'mac_address'], name, value)


                        class NextEgressId(Entity):
                            """
                            Next egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId, self).__init__()

                                self.yang_name = "next-egress-id"
                                self.yang_parent_name = "reply-ingress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "next-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId, ['unique_id', 'mac_address'], name, value)


                        class PortId(Entity):
                            """
                            Port ID
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:  :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:  :py:class:`CfmPmPortIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmt>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId, self).__init__()

                                self.yang_name = "port-id"
                                self.yang_parent_name = "reply-ingress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("port-id-value", ("port_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue))])
                                self._leafs = OrderedDict([
                                    ('port_id_type', (YLeaf(YType.enumeration, 'port-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt', '')])),
                                    ('port_id_type_value', (YLeaf(YType.uint8, 'port-id-type-value'), ['int'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                ])
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id = None

                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self
                                self._children_name_map["port_id_value"] = "port-id-value"
                                self._segment_path = lambda: "port-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId, ['port_id_type', 'port_id_type_value', 'port_id'], name, value)


                            class PortIdValue(Entity):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue, self).__init__()

                                    self.yang_name = "port-id-value"
                                    self.yang_parent_name = "port-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port_id_format', (YLeaf(YType.enumeration, 'port-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('port_id_string', (YLeaf(YType.str, 'port-id-string'), ['str'])),
                                        ('port_id_mac', (YLeaf(YType.str, 'port-id-mac'), ['str'])),
                                        ('port_id_raw', (YLeaf(YType.str, 'port-id-raw'), ['str'])),
                                    ])
                                    self.port_id_format = None
                                    self.port_id_string = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self._segment_path = lambda: "port-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue, ['port_id_format', 'port_id_string', 'port_id_mac', 'port_id_raw'], name, value)


                    class ReplyEgress(Entity):
                        """
                        Reply egress TLV
                        
                        .. attribute:: last_egress_id
                        
                        	Last Egress ID
                        	**type**\:  :py:class:`LastEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId>`
                        
                        .. attribute:: next_egress_id
                        
                        	Next Egress ID
                        	**type**\:  :py:class:`NextEgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\:  :py:class:`PortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId>`
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\:  :py:class:`CfmPmElrEgressAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrEgressAction>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address of egress interface
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress, self).__init__()

                            self.yang_name = "reply-egress"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("last-egress-id", ("last_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId)), ("next-egress-id", ("next_egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId)), ("port-id", ("port_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId))])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrEgressAction', '')])),
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ])
                            self.action = None
                            self.mac_address = None

                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId()
                            self.last_egress_id.parent = self
                            self._children_name_map["last_egress_id"] = "last-egress-id"

                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId()
                            self.next_egress_id.parent = self
                            self._children_name_map["next_egress_id"] = "next-egress-id"

                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self
                            self._children_name_map["port_id"] = "port-id"
                            self._segment_path = lambda: "reply-egress"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress, ['action', 'mac_address'], name, value)


                        class LastEgressId(Entity):
                            """
                            Last Egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId, self).__init__()

                                self.yang_name = "last-egress-id"
                                self.yang_parent_name = "reply-egress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "last-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId, ['unique_id', 'mac_address'], name, value)


                        class NextEgressId(Entity):
                            """
                            Next Egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId, self).__init__()

                                self.yang_name = "next-egress-id"
                                self.yang_parent_name = "reply-egress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "next-egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId, ['unique_id', 'mac_address'], name, value)


                        class PortId(Entity):
                            """
                            Port ID
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\:  :py:class:`PortIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\:  :py:class:`CfmPmPortIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmt>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId, self).__init__()

                                self.yang_name = "port-id"
                                self.yang_parent_name = "reply-egress"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("port-id-value", ("port_id_value", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue))])
                                self._leafs = OrderedDict([
                                    ('port_id_type', (YLeaf(YType.enumeration, 'port-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt', '')])),
                                    ('port_id_type_value', (YLeaf(YType.uint8, 'port-id-type-value'), ['int'])),
                                    ('port_id', (YLeaf(YType.str, 'port-id'), ['str'])),
                                ])
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id = None

                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self
                                self._children_name_map["port_id_value"] = "port-id-value"
                                self._segment_path = lambda: "port-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId, ['port_id_type', 'port_id_type_value', 'port_id'], name, value)


                            class PortIdValue(Entity):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue, self).__init__()

                                    self.yang_name = "port-id-value"
                                    self.yang_parent_name = "port-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('port_id_format', (YLeaf(YType.enumeration, 'port-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                        ('port_id_string', (YLeaf(YType.str, 'port-id-string'), ['str'])),
                                        ('port_id_mac', (YLeaf(YType.str, 'port-id-mac'), ['str'])),
                                        ('port_id_raw', (YLeaf(YType.str, 'port-id-raw'), ['str'])),
                                    ])
                                    self.port_id_format = None
                                    self.port_id_string = None
                                    self.port_id_mac = None
                                    self.port_id_raw = None
                                    self._segment_path = lambda: "port-id-value"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue, ['port_id_format', 'port_id_string', 'port_id_mac', 'port_id_raw'], name, value)


                    class LastHop(Entity):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\:  :py:class:`EgressId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\:  :py:class:`CfmPmLastHopFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmt>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop, self).__init__()

                            self.yang_name = "last-hop"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("egress-id", ("egress_id", Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId))])
                            self._leafs = OrderedDict([
                                ('last_hop_format', (YLeaf(YType.enumeration, 'last-hop-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmt', '')])),
                                ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                            ])
                            self.last_hop_format = None
                            self.host_name = None

                            self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self._children_name_map["egress_id"] = "egress-id"
                            self._segment_path = lambda: "last-hop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop, ['last_hop_format', 'host_name'], name, value)


                        class EgressId(Entity):
                            """
                            Egress ID
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId, self).__init__()

                                self.yang_name = "egress-id"
                                self.yang_parent_name = "last-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('unique_id', (YLeaf(YType.uint16, 'unique-id'), ['int'])),
                                    ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ])
                                self.unique_id = None
                                self.mac_address = None
                                self._segment_path = lambda: "egress-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId, ['unique_id', 'mac_address'], name, value)


                    class OrganizationSpecificTlv(Entity):
                        """
                        Organizational\-specific TLVs
                        
                        .. attribute:: oui
                        
                        	Organizationally\-unique ID
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: subtype
                        
                        	Subtype of TLV
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv, self).__init__()

                            self.yang_name = "organization-specific-tlv"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('oui', (YLeaf(YType.str, 'oui'), ['str'])),
                                ('subtype', (YLeaf(YType.uint8, 'subtype'), ['int'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.oui = None
                            self.subtype = None
                            self.value = None
                            self._segment_path = lambda: "organization-specific-tlv"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv, ['oui', 'subtype', 'value'], name, value)


                    class UnknownTlv(Entity):
                        """
                        Unknown TLVs
                        
                        .. attribute:: typecode
                        
                        	Type code of TLV
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Binary data in TLV
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv, self).__init__()

                            self.yang_name = "unknown-tlv"
                            self.yang_parent_name = "exploratory-linktrace-reply"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('typecode', (YLeaf(YType.uint8, 'typecode'), ['int'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.typecode = None
                            self.value = None
                            self._segment_path = lambda: "unknown-tlv"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv, ['typecode', 'value'], name, value)


        class LocalMeps(Entity):
            """
            Local MEPs table
            
            .. attribute:: local_mep
            
            	Information about a particular local MEP
            	**type**\: list of  		 :py:class:`LocalMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.LocalMeps, self).__init__()

                self.yang_name = "local-meps"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("local-mep", ("local_mep", Cfm.Global.LocalMeps.LocalMep))])
                self._leafs = OrderedDict()

                self.local_mep = YList(self)
                self._segment_path = lambda: "local-meps"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.LocalMeps, [], name, value)


            class LocalMep(Entity):
                """
                Information about a particular local MEP
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: mep_id  (key)
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: statistics
                
                	MEP statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Statistics>`
                
                .. attribute:: ais_statistics
                
                	MEP AIS statistics
                	**type**\:  :py:class:`AisStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics>`
                
                .. attribute:: defects
                
                	Defects detected from peer MEPs
                	**type**\:  :py:class:`Defects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Defects>`
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\: str
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\: str
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                
                .. attribute:: mep_id_xr
                
                	MEP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_state
                
                	IM Interface state
                	**type**\: str
                
                .. attribute:: interworking_state
                
                	Interface interworking state
                	**type**\:  :py:class:`CfmBagIwState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwState>`
                
                .. attribute:: stp_state
                
                	STP state
                	**type**\:  :py:class:`CfmBagStpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpState>`
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\:  :py:class:`CfmBagDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirection>`
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: peer_meps_detected
                
                	Number of peer MEPs detected
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_with_errors_detected
                
                	Number of peer MEPs detected with errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_defect
                
                	Remote defect indicated
                	**type**\: bool
                
                .. attribute:: fault_notification_state
                
                	Fault Notification Generation state
                	**type**\:  :py:class:`CfmPmMepFngState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepFngState>`
                
                .. attribute:: ccm_generation_enabled
                
                	CCM generation enabled
                	**type**\: bool
                
                .. attribute:: ccm_interval
                
                	The interval between CCMs
                	**type**\:  :py:class:`CfmBagCcmInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmInterval>`
                
                .. attribute:: ccm_offload
                
                	Offload status of CCM processing
                	**type**\:  :py:class:`CfmBagCcmOffload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffload>`
                
                .. attribute:: highest_defect
                
                	Highest\-priority defect present since last FNG reset
                	**type**\:  :py:class:`CfmPmMepDefect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepDefect>`
                
                .. attribute:: rdi_defect
                
                	A peer MEP RDI defect has been reported
                	**type**\: bool
                
                .. attribute:: mac_status_defect
                
                	A peer MEP port or interface status error has been reported
                	**type**\: bool
                
                .. attribute:: peer_mep_ccm_defect
                
                	A peer MEP CCM error has been reported
                	**type**\: bool
                
                .. attribute:: error_ccm_defect
                
                	A CCM error has been reported
                	**type**\: bool
                
                .. attribute:: cross_connect_ccm_defect
                
                	A cross\-connect CCM error has been reported
                	**type**\: bool
                
                .. attribute:: next_lbm_id
                
                	Next Transaction ID to be sent in a Loopback Message
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_ltm_id
                
                	Next Transaction ID to be sent in a Linktrace Message
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: cos
                
                	CoS bits the MEP will use for sent packets, if configured
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: efd_triggered
                
                	EFD triggered on the interface
                	**type**\: bool
                
                .. attribute:: standby
                
                	The local MEP is on an interface in standby mode
                	**type**\: bool
                
                .. attribute:: hairpin
                
                	MEP is on a sub\-interface in the same bridge\-domain and on the same trunk interface as another sub\-interface
                	**type**\: bool
                
                .. attribute:: defects_ignored
                
                	Defects present but ignored due to 'report defects' configuration
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.LocalMeps.LocalMep, self).__init__()

                    self.yang_name = "local-mep"
                    self.yang_parent_name = "local-meps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','mep_id','interface']
                    self._child_classes = OrderedDict([("statistics", ("statistics", Cfm.Global.LocalMeps.LocalMep.Statistics)), ("ais-statistics", ("ais_statistics", Cfm.Global.LocalMeps.LocalMep.AisStatistics)), ("defects", ("defects", Cfm.Global.LocalMeps.LocalMep.Defects))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('mep_id', (YLeaf(YType.uint32, 'mep-id'), ['int'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('domain_xr', (YLeaf(YType.str, 'domain-xr'), ['str'])),
                        ('service_xr', (YLeaf(YType.str, 'service-xr'), ['str'])),
                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                        ('mep_id_xr', (YLeaf(YType.uint16, 'mep-id-xr'), ['int'])),
                        ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                        ('interface_state', (YLeaf(YType.str, 'interface-state'), ['str'])),
                        ('interworking_state', (YLeaf(YType.enumeration, 'interworking-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwState', '')])),
                        ('stp_state', (YLeaf(YType.enumeration, 'stp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpState', '')])),
                        ('mep_direction', (YLeaf(YType.enumeration, 'mep-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection', '')])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('peer_meps_detected', (YLeaf(YType.uint32, 'peer-meps-detected'), ['int'])),
                        ('peer_meps_with_errors_detected', (YLeaf(YType.uint32, 'peer-meps-with-errors-detected'), ['int'])),
                        ('remote_defect', (YLeaf(YType.boolean, 'remote-defect'), ['bool'])),
                        ('fault_notification_state', (YLeaf(YType.enumeration, 'fault-notification-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepFngState', '')])),
                        ('ccm_generation_enabled', (YLeaf(YType.boolean, 'ccm-generation-enabled'), ['bool'])),
                        ('ccm_interval', (YLeaf(YType.enumeration, 'ccm-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval', '')])),
                        ('ccm_offload', (YLeaf(YType.enumeration, 'ccm-offload'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffload', '')])),
                        ('highest_defect', (YLeaf(YType.enumeration, 'highest-defect'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepDefect', '')])),
                        ('rdi_defect', (YLeaf(YType.boolean, 'rdi-defect'), ['bool'])),
                        ('mac_status_defect', (YLeaf(YType.boolean, 'mac-status-defect'), ['bool'])),
                        ('peer_mep_ccm_defect', (YLeaf(YType.boolean, 'peer-mep-ccm-defect'), ['bool'])),
                        ('error_ccm_defect', (YLeaf(YType.boolean, 'error-ccm-defect'), ['bool'])),
                        ('cross_connect_ccm_defect', (YLeaf(YType.boolean, 'cross-connect-ccm-defect'), ['bool'])),
                        ('next_lbm_id', (YLeaf(YType.uint32, 'next-lbm-id'), ['int'])),
                        ('next_ltm_id', (YLeaf(YType.uint32, 'next-ltm-id'), ['int'])),
                        ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                        ('efd_triggered', (YLeaf(YType.boolean, 'efd-triggered'), ['bool'])),
                        ('standby', (YLeaf(YType.boolean, 'standby'), ['bool'])),
                        ('hairpin', (YLeaf(YType.boolean, 'hairpin'), ['bool'])),
                        ('defects_ignored', (YLeaf(YType.boolean, 'defects-ignored'), ['bool'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.mep_id = None
                    self.interface = None
                    self.domain_xr = None
                    self.service_xr = None
                    self.level = None
                    self.mep_id_xr = None
                    self.interface_xr = None
                    self.interface_state = None
                    self.interworking_state = None
                    self.stp_state = None
                    self.mep_direction = None
                    self.mac_address = None
                    self.peer_meps_detected = None
                    self.peer_meps_with_errors_detected = None
                    self.remote_defect = None
                    self.fault_notification_state = None
                    self.ccm_generation_enabled = None
                    self.ccm_interval = None
                    self.ccm_offload = None
                    self.highest_defect = None
                    self.rdi_defect = None
                    self.mac_status_defect = None
                    self.peer_mep_ccm_defect = None
                    self.error_ccm_defect = None
                    self.cross_connect_ccm_defect = None
                    self.next_lbm_id = None
                    self.next_ltm_id = None
                    self.cos = None
                    self.efd_triggered = None
                    self.standby = None
                    self.hairpin = None
                    self.defects_ignored = None

                    self.statistics = Cfm.Global.LocalMeps.LocalMep.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"

                    self.ais_statistics = Cfm.Global.LocalMeps.LocalMep.AisStatistics()
                    self.ais_statistics.parent = self
                    self._children_name_map["ais_statistics"] = "ais-statistics"

                    self.defects = Cfm.Global.LocalMeps.LocalMep.Defects()
                    self.defects.parent = self
                    self._children_name_map["defects"] = "defects"
                    self._segment_path = lambda: "local-mep" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[mep-id='" + str(self.mep_id) + "']" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/local-meps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.LocalMeps.LocalMep, ['domain', 'service', 'mep_id', 'interface', 'domain_xr', 'service_xr', 'level', 'mep_id_xr', 'interface_xr', 'interface_state', 'interworking_state', 'stp_state', 'mep_direction', 'mac_address', 'peer_meps_detected', 'peer_meps_with_errors_detected', 'remote_defect', 'fault_notification_state', 'ccm_generation_enabled', 'ccm_interval', 'ccm_offload', 'highest_defect', 'rdi_defect', 'mac_status_defect', 'peer_mep_ccm_defect', 'error_ccm_defect', 'cross_connect_ccm_defect', 'next_lbm_id', 'next_ltm_id', 'cos', 'efd_triggered', 'standby', 'hairpin', 'defects_ignored'], name, value)


                class Statistics(Entity):
                    """
                    MEP statistics
                    
                    .. attribute:: ccms_sent
                    
                    	Number of CCMs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_received
                    
                    	Number of CCMs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_out_of_sequence
                    
                    	Number of CCMs received out\-of\-sequence
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_discarded
                    
                    	Number of CCMs discarded because maximum MEPs limit was reached
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_sent
                    
                    	Number of LBMs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_sent
                    
                    	Number of LBRs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_received
                    
                    	Number of LBRs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_out_of_sequence
                    
                    	Number of LBRs received out\-of\-sequence
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_bad_data
                    
                    	Number of LBRs received with non\-matching user\-specified data
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_received
                    
                    	Number of LBMs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lt_rs_received_unexpected
                    
                    	Number of unexpected LTRs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ai_ss_sent
                    
                    	Number of AIS messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ai_ss_received
                    
                    	Number of AIS messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lc_ks_received
                    
                    	Number of LCK messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_sent
                    
                    	Number of DMM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_received
                    
                    	Number of DMM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_sent
                    
                    	Number of DMR messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_received
                    
                    	Number of DMR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_sent
                    
                    	Number of SLM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_received
                    
                    	Number of SLM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_sent
                    
                    	Number of SLR messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_received
                    
                    	Number of SLR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_sent
                    
                    	Number of LMM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_received
                    
                    	Number of LMM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_sent
                    
                    	Number of LMR messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_received
                    
                    	Number of LMR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_received
                    
                    	Number of BNM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_discarded
                    
                    	Number of BNM messages discarded
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.LocalMeps.LocalMep.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "local-mep"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ccms_sent', (YLeaf(YType.uint64, 'ccms-sent'), ['int'])),
                            ('ccms_received', (YLeaf(YType.uint64, 'ccms-received'), ['int'])),
                            ('ccms_out_of_sequence', (YLeaf(YType.uint64, 'ccms-out-of-sequence'), ['int'])),
                            ('ccms_discarded', (YLeaf(YType.uint64, 'ccms-discarded'), ['int'])),
                            ('lb_ms_sent', (YLeaf(YType.uint64, 'lb-ms-sent'), ['int'])),
                            ('lb_rs_sent', (YLeaf(YType.uint64, 'lb-rs-sent'), ['int'])),
                            ('lb_rs_received', (YLeaf(YType.uint64, 'lb-rs-received'), ['int'])),
                            ('lb_rs_out_of_sequence', (YLeaf(YType.uint64, 'lb-rs-out-of-sequence'), ['int'])),
                            ('lb_rs_bad_data', (YLeaf(YType.uint64, 'lb-rs-bad-data'), ['int'])),
                            ('lb_ms_received', (YLeaf(YType.uint64, 'lb-ms-received'), ['int'])),
                            ('lt_rs_received_unexpected', (YLeaf(YType.uint64, 'lt-rs-received-unexpected'), ['int'])),
                            ('ai_ss_sent', (YLeaf(YType.uint64, 'ai-ss-sent'), ['int'])),
                            ('ai_ss_received', (YLeaf(YType.uint64, 'ai-ss-received'), ['int'])),
                            ('lc_ks_received', (YLeaf(YType.uint64, 'lc-ks-received'), ['int'])),
                            ('dm_ms_sent', (YLeaf(YType.uint64, 'dm-ms-sent'), ['int'])),
                            ('dm_ms_received', (YLeaf(YType.uint64, 'dm-ms-received'), ['int'])),
                            ('dm_rs_sent', (YLeaf(YType.uint64, 'dm-rs-sent'), ['int'])),
                            ('dm_rs_received', (YLeaf(YType.uint64, 'dm-rs-received'), ['int'])),
                            ('sl_ms_sent', (YLeaf(YType.uint64, 'sl-ms-sent'), ['int'])),
                            ('sl_ms_received', (YLeaf(YType.uint64, 'sl-ms-received'), ['int'])),
                            ('sl_rs_sent', (YLeaf(YType.uint64, 'sl-rs-sent'), ['int'])),
                            ('sl_rs_received', (YLeaf(YType.uint64, 'sl-rs-received'), ['int'])),
                            ('lm_ms_sent', (YLeaf(YType.uint64, 'lm-ms-sent'), ['int'])),
                            ('lm_ms_received', (YLeaf(YType.uint64, 'lm-ms-received'), ['int'])),
                            ('lm_rs_sent', (YLeaf(YType.uint64, 'lm-rs-sent'), ['int'])),
                            ('lm_rs_received', (YLeaf(YType.uint64, 'lm-rs-received'), ['int'])),
                            ('bn_ms_received', (YLeaf(YType.uint64, 'bn-ms-received'), ['int'])),
                            ('bn_ms_discarded', (YLeaf(YType.uint64, 'bn-ms-discarded'), ['int'])),
                        ])
                        self.ccms_sent = None
                        self.ccms_received = None
                        self.ccms_out_of_sequence = None
                        self.ccms_discarded = None
                        self.lb_ms_sent = None
                        self.lb_rs_sent = None
                        self.lb_rs_received = None
                        self.lb_rs_out_of_sequence = None
                        self.lb_rs_bad_data = None
                        self.lb_ms_received = None
                        self.lt_rs_received_unexpected = None
                        self.ai_ss_sent = None
                        self.ai_ss_received = None
                        self.lc_ks_received = None
                        self.dm_ms_sent = None
                        self.dm_ms_received = None
                        self.dm_rs_sent = None
                        self.dm_rs_received = None
                        self.sl_ms_sent = None
                        self.sl_ms_received = None
                        self.sl_rs_sent = None
                        self.sl_rs_received = None
                        self.lm_ms_sent = None
                        self.lm_ms_received = None
                        self.lm_rs_sent = None
                        self.lm_rs_received = None
                        self.bn_ms_received = None
                        self.bn_ms_discarded = None
                        self._segment_path = lambda: "statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.Statistics, ['ccms_sent', 'ccms_received', 'ccms_out_of_sequence', 'ccms_discarded', 'lb_ms_sent', 'lb_rs_sent', 'lb_rs_received', 'lb_rs_out_of_sequence', 'lb_rs_bad_data', 'lb_ms_received', 'lt_rs_received_unexpected', 'ai_ss_sent', 'ai_ss_received', 'lc_ks_received', 'dm_ms_sent', 'dm_ms_received', 'dm_rs_sent', 'dm_rs_received', 'sl_ms_sent', 'sl_ms_received', 'sl_rs_sent', 'sl_rs_received', 'lm_ms_sent', 'lm_ms_received', 'lm_rs_sent', 'lm_rs_received', 'bn_ms_received', 'bn_ms_discarded'], name, value)


                class AisStatistics(Entity):
                    """
                    MEP AIS statistics
                    
                    .. attribute:: sending_start
                    
                    	Time elapsed since AIS sending started
                    	**type**\:  :py:class:`SendingStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart>`
                    
                    .. attribute:: receiving_start
                    
                    	Time elapsed since AIS receiving started
                    	**type**\:  :py:class:`ReceivingStart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart>`
                    
                    .. attribute:: level
                    
                    	AIS transmission level
                    	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                    
                    .. attribute:: interval
                    
                    	AIS transmission interval
                    	**type**\:  :py:class:`CfmBagAisInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisInterval>`
                    
                    .. attribute:: sending_ais
                    
                    	Details of how AIS is being transmitted
                    	**type**\:  :py:class:`CfmPmAisTransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisTransmit>`
                    
                    .. attribute:: receiving_ais
                    
                    	Details of how the signal is being received
                    	**type**\:  :py:class:`CfmPmAisReceive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisReceive>`
                    
                    .. attribute:: last_interval
                    
                    	The interval of the last received AIS packet
                    	**type**\:  :py:class:`CfmBagAisInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisInterval>`
                    
                    .. attribute:: last_mac_address
                    
                    	Source MAC address of the last received AIS packet
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.LocalMeps.LocalMep.AisStatistics, self).__init__()

                        self.yang_name = "ais-statistics"
                        self.yang_parent_name = "local-mep"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sending-start", ("sending_start", Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart)), ("receiving-start", ("receiving_start", Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart))])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                            ('interval', (YLeaf(YType.enumeration, 'interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval', '')])),
                            ('sending_ais', (YLeaf(YType.enumeration, 'sending-ais'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisTransmit', '')])),
                            ('receiving_ais', (YLeaf(YType.enumeration, 'receiving-ais'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisReceive', '')])),
                            ('last_interval', (YLeaf(YType.enumeration, 'last-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval', '')])),
                            ('last_mac_address', (YLeaf(YType.str, 'last-mac-address'), ['str'])),
                        ])
                        self.level = None
                        self.interval = None
                        self.sending_ais = None
                        self.receiving_ais = None
                        self.last_interval = None
                        self.last_mac_address = None

                        self.sending_start = Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart()
                        self.sending_start.parent = self
                        self._children_name_map["sending_start"] = "sending-start"

                        self.receiving_start = Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart()
                        self.receiving_start.parent = self
                        self._children_name_map["receiving_start"] = "receiving-start"
                        self._segment_path = lambda: "ais-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.AisStatistics, ['level', 'interval', 'sending_ais', 'receiving_ais', 'last_interval', 'last_mac_address'], name, value)


                    class SendingStart(Entity):
                        """
                        Time elapsed since AIS sending started
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart, self).__init__()

                            self.yang_name = "sending-start"
                            self.yang_parent_name = "ais-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "sending-start"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart, ['seconds', 'nanoseconds'], name, value)


                    class ReceivingStart(Entity):
                        """
                        Time elapsed since AIS receiving started
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart, self).__init__()

                            self.yang_name = "receiving-start"
                            self.yang_parent_name = "ais-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "receiving-start"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart, ['seconds', 'nanoseconds'], name, value)


                class Defects(Entity):
                    """
                    Defects detected from peer MEPs
                    
                    .. attribute:: remote_meps_defects
                    
                    	Defects detected from remote MEPs
                    	**type**\:  :py:class:`RemoteMepsDefects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects>`
                    
                    .. attribute:: ais_received
                    
                    	AIS or LCK received
                    	**type**\: bool
                    
                    .. attribute:: peer_meps_that_timed_out
                    
                    	Number of peer MEPs that have timed out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: missing
                    
                    	Number of missing peer MEPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auto_missing
                    
                    	Number of missing auto cross\-check MEPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected
                    
                    	Number of unexpected peer MEPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_port_status
                    
                    	The local port or interface is down
                    	**type**\: bool
                    
                    .. attribute:: peer_port_status
                    
                    	A peer port or interface is down
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.LocalMeps.LocalMep.Defects, self).__init__()

                        self.yang_name = "defects"
                        self.yang_parent_name = "local-mep"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("remote-meps-defects", ("remote_meps_defects", Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects))])
                        self._leafs = OrderedDict([
                            ('ais_received', (YLeaf(YType.boolean, 'ais-received'), ['bool'])),
                            ('peer_meps_that_timed_out', (YLeaf(YType.uint32, 'peer-meps-that-timed-out'), ['int'])),
                            ('missing', (YLeaf(YType.uint32, 'missing'), ['int'])),
                            ('auto_missing', (YLeaf(YType.uint32, 'auto-missing'), ['int'])),
                            ('unexpected', (YLeaf(YType.uint32, 'unexpected'), ['int'])),
                            ('local_port_status', (YLeaf(YType.boolean, 'local-port-status'), ['bool'])),
                            ('peer_port_status', (YLeaf(YType.boolean, 'peer-port-status'), ['bool'])),
                        ])
                        self.ais_received = None
                        self.peer_meps_that_timed_out = None
                        self.missing = None
                        self.auto_missing = None
                        self.unexpected = None
                        self.local_port_status = None
                        self.peer_port_status = None

                        self.remote_meps_defects = Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects()
                        self.remote_meps_defects.parent = self
                        self._children_name_map["remote_meps_defects"] = "remote-meps-defects"
                        self._segment_path = lambda: "defects"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.Defects, ['ais_received', 'peer_meps_that_timed_out', 'missing', 'auto_missing', 'unexpected', 'local_port_status', 'peer_port_status'], name, value)


                    class RemoteMepsDefects(Entity):
                        """
                        Defects detected from remote MEPs
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
                        	**type**\: bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\: bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\: bool
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\: bool
                        
                        .. attribute:: received_our_mac
                        
                        	Loop detected (our MAC address received)
                        	**type**\: bool
                        
                        .. attribute:: received_our_mep_id
                        
                        	Configuration Error (our MEP ID received)
                        	**type**\: bool
                        
                        .. attribute:: received_rdi
                        
                        	Remote defection indication received
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects, self).__init__()

                            self.yang_name = "remote-meps-defects"
                            self.yang_parent_name = "defects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('loss_threshold_exceeded', (YLeaf(YType.boolean, 'loss-threshold-exceeded'), ['bool'])),
                                ('invalid_level', (YLeaf(YType.boolean, 'invalid-level'), ['bool'])),
                                ('invalid_maid', (YLeaf(YType.boolean, 'invalid-maid'), ['bool'])),
                                ('invalid_ccm_interval', (YLeaf(YType.boolean, 'invalid-ccm-interval'), ['bool'])),
                                ('received_our_mac', (YLeaf(YType.boolean, 'received-our-mac'), ['bool'])),
                                ('received_our_mep_id', (YLeaf(YType.boolean, 'received-our-mep-id'), ['bool'])),
                                ('received_rdi', (YLeaf(YType.boolean, 'received-rdi'), ['bool'])),
                            ])
                            self.loss_threshold_exceeded = None
                            self.invalid_level = None
                            self.invalid_maid = None
                            self.invalid_ccm_interval = None
                            self.received_our_mac = None
                            self.received_our_mep_id = None
                            self.received_rdi = None
                            self._segment_path = lambda: "remote-meps-defects"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects, ['loss_threshold_exceeded', 'invalid_level', 'invalid_maid', 'invalid_ccm_interval', 'received_our_mac', 'received_our_mep_id', 'received_rdi'], name, value)


        class PeerMePv2s(Entity):
            """
            Peer MEPs table Version 2
            
            .. attribute:: peer_me_pv2
            
            	Information about a peer MEP for a particular local MEP
            	**type**\: list of  		 :py:class:`PeerMePv2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2017-10-06'

            def __init__(self):
                super(Cfm.Global.PeerMePv2s, self).__init__()

                self.yang_name = "peer-me-pv2s"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("peer-me-pv2", ("peer_me_pv2", Cfm.Global.PeerMePv2s.PeerMePv2))])
                self._leafs = OrderedDict()

                self.peer_me_pv2 = YList(self)
                self._segment_path = lambda: "peer-me-pv2s"
                self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Cfm.Global.PeerMePv2s, [], name, value)


            class PeerMePv2(Entity):
                """
                Information about a peer MEP for a particular
                local MEP
                
                .. attribute:: domain  (key)
                
                	Maintenance Domain
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: service  (key)
                
                	Service (Maintenance Association)
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: local_mep_id  (key)
                
                	MEP ID of Local MEP
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: peer_mep_id  (key)
                
                	MEP ID of Peer MEP
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: peer_mac_address  (key)
                
                	Peer MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: peer_mep
                
                	Peer MEP
                	**type**\:  :py:class:`PeerMep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep>`
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\: str
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\: str
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\:  :py:class:`CfmBagDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirection>`
                
                .. attribute:: standby
                
                	The local MEP is on an interface in standby mode
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2017-10-06'

                def __init__(self):
                    super(Cfm.Global.PeerMePv2s.PeerMePv2, self).__init__()

                    self.yang_name = "peer-me-pv2"
                    self.yang_parent_name = "peer-me-pv2s"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain','service','local_mep_id','interface','peer_mep_id','peer_mac_address']
                    self._child_classes = OrderedDict([("peer-mep", ("peer_mep", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep))])
                    self._leafs = OrderedDict([
                        ('domain', (YLeaf(YType.str, 'domain'), ['str'])),
                        ('service', (YLeaf(YType.str, 'service'), ['str'])),
                        ('local_mep_id', (YLeaf(YType.uint32, 'local-mep-id'), ['int'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('peer_mep_id', (YLeaf(YType.uint32, 'peer-mep-id'), ['int'])),
                        ('peer_mac_address', (YLeaf(YType.str, 'peer-mac-address'), ['str'])),
                        ('domain_xr', (YLeaf(YType.str, 'domain-xr'), ['str'])),
                        ('service_xr', (YLeaf(YType.str, 'service-xr'), ['str'])),
                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                        ('mep_id', (YLeaf(YType.uint16, 'mep-id'), ['int'])),
                        ('interface_xr', (YLeaf(YType.str, 'interface-xr'), ['str'])),
                        ('mep_direction', (YLeaf(YType.enumeration, 'mep-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection', '')])),
                        ('standby', (YLeaf(YType.boolean, 'standby'), ['bool'])),
                    ])
                    self.domain = None
                    self.service = None
                    self.local_mep_id = None
                    self.interface = None
                    self.peer_mep_id = None
                    self.peer_mac_address = None
                    self.domain_xr = None
                    self.service_xr = None
                    self.level = None
                    self.mep_id = None
                    self.interface_xr = None
                    self.mep_direction = None
                    self.standby = None

                    self.peer_mep = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep()
                    self.peer_mep.parent = self
                    self._children_name_map["peer_mep"] = "peer-mep"
                    self._segment_path = lambda: "peer-me-pv2" + "[domain='" + str(self.domain) + "']" + "[service='" + str(self.service) + "']" + "[local-mep-id='" + str(self.local_mep_id) + "']" + "[interface='" + str(self.interface) + "']" + "[peer-mep-id='" + str(self.peer_mep_id) + "']" + "[peer-mac-address='" + str(self.peer_mac_address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ethernet-cfm-oper:cfm/global/peer-me-pv2s/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2, ['domain', 'service', 'local_mep_id', 'interface', 'peer_mep_id', 'peer_mac_address', 'domain_xr', 'service_xr', 'level', 'mep_id', 'interface_xr', 'mep_direction', 'standby'], name, value)


                class PeerMep(Entity):
                    """
                    Peer MEP
                    
                    .. attribute:: error_state
                    
                    	Error state
                    	**type**\:  :py:class:`ErrorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.ErrorState>`
                    
                    .. attribute:: last_up_down_time
                    
                    	Elapsed time since peer MEP became active or timed out
                    	**type**\:  :py:class:`LastUpDownTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastUpDownTime>`
                    
                    .. attribute:: last_ccm_received
                    
                    	Last CCM received from the peer MEP
                    	**type**\:  :py:class:`LastCcmReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived>`
                    
                    .. attribute:: statistics
                    
                    	Peer MEP statistics
                    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: cross_check_state
                    
                    	Cross\-check state
                    	**type**\:  :py:class:`CfmPmRmepXcState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepXcState>`
                    
                    .. attribute:: peer_mep_state
                    
                    	State of the peer MEP state machine
                    	**type**\:  :py:class:`CfmPmRmepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepState>`
                    
                    .. attribute:: ccm_offload
                    
                    	Offload status of received CCM handling
                    	**type**\:  :py:class:`CfmBagCcmOffload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffload>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2017-10-06'

                    def __init__(self):
                        super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep, self).__init__()

                        self.yang_name = "peer-mep"
                        self.yang_parent_name = "peer-me-pv2"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("error-state", ("error_state", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.ErrorState)), ("last-up-down-time", ("last_up_down_time", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastUpDownTime)), ("last-ccm-received", ("last_ccm_received", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived)), ("statistics", ("statistics", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics))])
                        self._leafs = OrderedDict([
                            ('mep_id', (YLeaf(YType.uint16, 'mep-id'), ['int'])),
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('cross_check_state', (YLeaf(YType.enumeration, 'cross-check-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepXcState', '')])),
                            ('peer_mep_state', (YLeaf(YType.enumeration, 'peer-mep-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepState', '')])),
                            ('ccm_offload', (YLeaf(YType.enumeration, 'ccm-offload'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffload', '')])),
                        ])
                        self.mep_id = None
                        self.mac_address = None
                        self.cross_check_state = None
                        self.peer_mep_state = None
                        self.ccm_offload = None

                        self.error_state = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.ErrorState()
                        self.error_state.parent = self
                        self._children_name_map["error_state"] = "error-state"

                        self.last_up_down_time = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastUpDownTime()
                        self.last_up_down_time.parent = self
                        self._children_name_map["last_up_down_time"] = "last-up-down-time"

                        self.last_ccm_received = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived()
                        self.last_ccm_received.parent = self
                        self._children_name_map["last_ccm_received"] = "last-ccm-received"

                        self.statistics = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                        self._segment_path = lambda: "peer-mep"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep, ['mep_id', 'mac_address', 'cross_check_state', 'peer_mep_state', 'ccm_offload'], name, value)


                    class ErrorState(Entity):
                        """
                        Error state
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
                        	**type**\: bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\: bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\: bool
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\: bool
                        
                        .. attribute:: received_our_mac
                        
                        	Loop detected (our MAC address received)
                        	**type**\: bool
                        
                        .. attribute:: received_our_mep_id
                        
                        	Configuration Error (our MEP ID received)
                        	**type**\: bool
                        
                        .. attribute:: received_rdi
                        
                        	Remote defection indication received
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.ErrorState, self).__init__()

                            self.yang_name = "error-state"
                            self.yang_parent_name = "peer-mep"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('loss_threshold_exceeded', (YLeaf(YType.boolean, 'loss-threshold-exceeded'), ['bool'])),
                                ('invalid_level', (YLeaf(YType.boolean, 'invalid-level'), ['bool'])),
                                ('invalid_maid', (YLeaf(YType.boolean, 'invalid-maid'), ['bool'])),
                                ('invalid_ccm_interval', (YLeaf(YType.boolean, 'invalid-ccm-interval'), ['bool'])),
                                ('received_our_mac', (YLeaf(YType.boolean, 'received-our-mac'), ['bool'])),
                                ('received_our_mep_id', (YLeaf(YType.boolean, 'received-our-mep-id'), ['bool'])),
                                ('received_rdi', (YLeaf(YType.boolean, 'received-rdi'), ['bool'])),
                            ])
                            self.loss_threshold_exceeded = None
                            self.invalid_level = None
                            self.invalid_maid = None
                            self.invalid_ccm_interval = None
                            self.received_our_mac = None
                            self.received_our_mep_id = None
                            self.received_rdi = None
                            self._segment_path = lambda: "error-state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.ErrorState, ['loss_threshold_exceeded', 'invalid_level', 'invalid_maid', 'invalid_ccm_interval', 'received_our_mac', 'received_our_mep_id', 'received_rdi'], name, value)


                    class LastUpDownTime(Entity):
                        """
                        Elapsed time since peer MEP became active or
                        timed out
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastUpDownTime, self).__init__()

                            self.yang_name = "last-up-down-time"
                            self.yang_parent_name = "peer-mep"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                            ])
                            self.seconds = None
                            self.nanoseconds = None
                            self._segment_path = lambda: "last-up-down-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastUpDownTime, ['seconds', 'nanoseconds'], name, value)


                    class LastCcmReceived(Entity):
                        """
                        Last CCM received from the peer MEP
                        
                        .. attribute:: header
                        
                        	Frame header
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header>`
                        
                        .. attribute:: sender_id
                        
                        	Sender ID TLV
                        	**type**\:  :py:class:`SenderId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId>`
                        
                        .. attribute:: mep_name
                        
                        	MEP name
                        	**type**\:  :py:class:`MepName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.MepName>`
                        
                        .. attribute:: port_status
                        
                        	Port status
                        	**type**\:  :py:class:`CfmPmPortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortStatus>`
                        
                        .. attribute:: interface_status
                        
                        	Interface status
                        	**type**\:  :py:class:`CfmPmIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIntfStatus>`
                        
                        .. attribute:: additional_interface_status
                        
                        	Additional interface status
                        	**type**\:  :py:class:`CfmPmAddlIntfStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAddlIntfStatus>`
                        
                        .. attribute:: raw_data
                        
                        	Undecoded frame
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: organization_specific_tlv
                        
                        	Organizational\-specific TLVs
                        	**type**\: list of  		 :py:class:`OrganizationSpecificTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv>`
                        
                        .. attribute:: unknown_tlv
                        
                        	Unknown TLVs
                        	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived, self).__init__()

                            self.yang_name = "last-ccm-received"
                            self.yang_parent_name = "peer-mep"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header)), ("sender-id", ("sender_id", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId)), ("mep-name", ("mep_name", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.MepName)), ("organization-specific-tlv", ("organization_specific_tlv", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv)), ("unknown-tlv", ("unknown_tlv", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv))])
                            self._leafs = OrderedDict([
                                ('port_status', (YLeaf(YType.enumeration, 'port-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortStatus', '')])),
                                ('interface_status', (YLeaf(YType.enumeration, 'interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIntfStatus', '')])),
                                ('additional_interface_status', (YLeaf(YType.enumeration, 'additional-interface-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAddlIntfStatus', '')])),
                                ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                            ])
                            self.port_status = None
                            self.interface_status = None
                            self.additional_interface_status = None
                            self.raw_data = None

                            self.header = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.sender_id = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId()
                            self.sender_id.parent = self
                            self._children_name_map["sender_id"] = "sender-id"

                            self.mep_name = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.MepName()
                            self.mep_name.parent = self
                            self._children_name_map["mep_name"] = "mep-name"

                            self.organization_specific_tlv = YList(self)
                            self.unknown_tlv = YList(self)
                            self._segment_path = lambda: "last-ccm-received"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived, ['port_status', 'interface_status', 'additional_interface_status', 'raw_data'], name, value)


                        class Header(Entity):
                            """
                            Frame header
                            
                            .. attribute:: mdid
                            
                            	MDID
                            	**type**\:  :py:class:`Mdid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid>`
                            
                            .. attribute:: short_ma_name
                            
                            	Short MA Name
                            	**type**\:  :py:class:`ShortMaName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName>`
                            
                            .. attribute:: level
                            
                            	MD level
                            	**type**\:  :py:class:`CfmBagMdLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevel>`
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: interval
                            
                            	CCM interval
                            	**type**\:  :py:class:`CfmBagCcmInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmInterval>`
                            
                            .. attribute:: rdi
                            
                            	Remote defect indicated
                            	**type**\: bool
                            
                            .. attribute:: sequence_number
                            
                            	CCM sequence number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mep_id
                            
                            	MEP ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mdid_format
                            
                            	MDID Format
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name format
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "last-ccm-received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("mdid", ("mdid", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid)), ("short-ma-name", ("short_ma_name", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName))])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel', '')])),
                                    ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                                    ('interval', (YLeaf(YType.enumeration, 'interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval', '')])),
                                    ('rdi', (YLeaf(YType.boolean, 'rdi'), ['bool'])),
                                    ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                                    ('mep_id', (YLeaf(YType.uint16, 'mep-id'), ['int'])),
                                    ('mdid_format', (YLeaf(YType.uint8, 'mdid-format'), ['int'])),
                                    ('short_ma_name_format', (YLeaf(YType.uint8, 'short-ma-name-format'), ['int'])),
                                ])
                                self.level = None
                                self.version = None
                                self.interval = None
                                self.rdi = None
                                self.sequence_number = None
                                self.mep_id = None
                                self.mdid_format = None
                                self.short_ma_name_format = None

                                self.mdid = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid()
                                self.mdid.parent = self
                                self._children_name_map["mdid"] = "mdid"

                                self.short_ma_name = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName()
                                self.short_ma_name.parent = self
                                self._children_name_map["short_ma_name"] = "short-ma-name"
                                self._segment_path = lambda: "header"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header, ['level', 'version', 'interval', 'rdi', 'sequence_number', 'mep_id', 'mdid_format', 'short_ma_name_format'], name, value)


                            class Mdid(Entity):
                                """
                                MDID
                                
                                .. attribute:: mac_name
                                
                                	MAC address name
                                	**type**\:  :py:class:`MacName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName>`
                                
                                .. attribute:: mdid_format_value
                                
                                	MDIDFormatValue
                                	**type**\:  :py:class:`CfmBagMdidFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdidFmt>`
                                
                                .. attribute:: dns_like_name
                                
                                	DNS\-like name
                                	**type**\: str
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\: str
                                
                                .. attribute:: mdid_data
                                
                                	Hex data
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid, self).__init__()

                                    self.yang_name = "mdid"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mac-name", ("mac_name", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName))])
                                    self._leafs = OrderedDict([
                                        ('mdid_format_value', (YLeaf(YType.enumeration, 'mdid-format-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdidFmt', '')])),
                                        ('dns_like_name', (YLeaf(YType.str, 'dns-like-name'), ['str'])),
                                        ('string_name', (YLeaf(YType.str, 'string-name'), ['str'])),
                                        ('mdid_data', (YLeaf(YType.str, 'mdid-data'), ['str'])),
                                    ])
                                    self.mdid_format_value = None
                                    self.dns_like_name = None
                                    self.string_name = None
                                    self.mdid_data = None

                                    self.mac_name = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName()
                                    self.mac_name.parent = self
                                    self._children_name_map["mac_name"] = "mac-name"
                                    self._segment_path = lambda: "mdid"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid, [u'mdid_format_value', u'dns_like_name', u'string_name', u'mdid_data'], name, value)


                                class MacName(Entity):
                                    """
                                    MAC address name
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: integer
                                    
                                    	Integer
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName, self).__init__()

                                        self.yang_name = "mac-name"
                                        self.yang_parent_name = "mdid"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                            ('integer', (YLeaf(YType.uint16, 'integer'), ['int'])),
                                        ])
                                        self.mac_address = None
                                        self.integer = None
                                        self._segment_path = lambda: "mac-name"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName, [u'mac_address', u'integer'], name, value)


                            class ShortMaName(Entity):
                                """
                                Short MA Name
                                
                                .. attribute:: vpn_id_name
                                
                                	VPN ID name
                                	**type**\:  :py:class:`VpnIdName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName>`
                                
                                .. attribute:: short_ma_name_format_value
                                
                                	ShortMANameFormatValue
                                	**type**\:  :py:class:`CfmBagSmanFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagSmanFmt>`
                                
                                .. attribute:: vlan_id_name
                                
                                	VLAN ID name
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\: str
                                
                                .. attribute:: integer_name
                                
                                	Unsigned integer name
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: icc_based
                                
                                	ICC\-based format
                                	**type**\: str
                                
                                .. attribute:: short_ma_name_data
                                
                                	Hex data
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName, self).__init__()

                                    self.yang_name = "short-ma-name"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("vpn-id-name", ("vpn_id_name", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName))])
                                    self._leafs = OrderedDict([
                                        ('short_ma_name_format_value', (YLeaf(YType.enumeration, 'short-ma-name-format-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagSmanFmt', '')])),
                                        ('vlan_id_name', (YLeaf(YType.uint16, 'vlan-id-name'), ['int'])),
                                        ('string_name', (YLeaf(YType.str, 'string-name'), ['str'])),
                                        ('integer_name', (YLeaf(YType.uint16, 'integer-name'), ['int'])),
                                        ('icc_based', (YLeaf(YType.str, 'icc-based'), ['str'])),
                                        ('short_ma_name_data', (YLeaf(YType.str, 'short-ma-name-data'), ['str'])),
                                    ])
                                    self.short_ma_name_format_value = None
                                    self.vlan_id_name = None
                                    self.string_name = None
                                    self.integer_name = None
                                    self.icc_based = None
                                    self.short_ma_name_data = None

                                    self.vpn_id_name = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName()
                                    self.vpn_id_name.parent = self
                                    self._children_name_map["vpn_id_name"] = "vpn-id-name"
                                    self._segment_path = lambda: "short-ma-name"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName, [u'short_ma_name_format_value', u'vlan_id_name', u'string_name', u'integer_name', u'icc_based', u'short_ma_name_data'], name, value)


                                class VpnIdName(Entity):
                                    """
                                    VPN ID name
                                    
                                    .. attribute:: oui
                                    
                                    	VPN authority organizationally\-unique ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: index
                                    
                                    	VPN index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName, self).__init__()

                                        self.yang_name = "vpn-id-name"
                                        self.yang_parent_name = "short-ma-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('oui', (YLeaf(YType.uint32, 'oui'), ['int'])),
                                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ])
                                        self.oui = None
                                        self.index = None
                                        self._segment_path = lambda: "vpn-id-name"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName, [u'oui', u'index'], name, value)


                        class SenderId(Entity):
                            """
                            Sender ID TLV
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID
                            	**type**\:  :py:class:`ChassisId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId>`
                            
                            .. attribute:: management_address_domain
                            
                            	Management address domain
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: management_address
                            
                            	Management address
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId, self).__init__()

                                self.yang_name = "sender-id"
                                self.yang_parent_name = "last-ccm-received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("chassis-id", ("chassis_id", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId))])
                                self._leafs = OrderedDict([
                                    ('management_address_domain', (YLeaf(YType.str, 'management-address-domain'), ['str'])),
                                    ('management_address', (YLeaf(YType.str, 'management-address'), ['str'])),
                                ])
                                self.management_address_domain = None
                                self.management_address = None

                                self.chassis_id = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId()
                                self.chassis_id.parent = self
                                self._children_name_map["chassis_id"] = "chassis-id"
                                self._segment_path = lambda: "sender-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId, ['management_address_domain', 'management_address'], name, value)


                            class ChassisId(Entity):
                                """
                                Chassis ID
                                
                                .. attribute:: chassis_id_value
                                
                                	Chassis ID (Current)
                                	**type**\:  :py:class:`ChassisIdValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue>`
                                
                                .. attribute:: chassis_id_type
                                
                                	Chassis ID Type
                                	**type**\:  :py:class:`CfmPmChassisIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmt>`
                                
                                .. attribute:: chassis_id_type_value
                                
                                	Chassis ID Type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id
                                
                                	Chassis ID (Deprecated)
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2017-10-06'

                                def __init__(self):
                                    super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId, self).__init__()

                                    self.yang_name = "chassis-id"
                                    self.yang_parent_name = "sender-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("chassis-id-value", ("chassis_id_value", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue))])
                                    self._leafs = OrderedDict([
                                        ('chassis_id_type', (YLeaf(YType.enumeration, 'chassis-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt', '')])),
                                        ('chassis_id_type_value', (YLeaf(YType.uint8, 'chassis-id-type-value'), ['int'])),
                                        ('chassis_id', (YLeaf(YType.str, 'chassis-id'), ['str'])),
                                    ])
                                    self.chassis_id_type = None
                                    self.chassis_id_type_value = None
                                    self.chassis_id = None

                                    self.chassis_id_value = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue()
                                    self.chassis_id_value.parent = self
                                    self._children_name_map["chassis_id_value"] = "chassis-id-value"
                                    self._segment_path = lambda: "chassis-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId, ['chassis_id_type', 'chassis_id_type_value', 'chassis_id'], name, value)


                                class ChassisIdValue(Entity):
                                    """
                                    Chassis ID (Current)
                                    
                                    .. attribute:: chassis_id_format
                                    
                                    	ChassisIDFormat
                                    	**type**\:  :py:class:`CfmPmIdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmt>`
                                    
                                    .. attribute:: chassis_id_string
                                    
                                    	Chassis ID String
                                    	**type**\: str
                                    
                                    .. attribute:: chassis_id_mac
                                    
                                    	Chassis ID MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: chassis_id_raw
                                    
                                    	Raw Chassis ID
                                    	**type**\: str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    

                                    """

                                    _prefix = 'ethernet-cfm-oper'
                                    _revision = '2017-10-06'

                                    def __init__(self):
                                        super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue, self).__init__()

                                        self.yang_name = "chassis-id-value"
                                        self.yang_parent_name = "chassis-id"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('chassis_id_format', (YLeaf(YType.enumeration, 'chassis-id-format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt', '')])),
                                            ('chassis_id_string', (YLeaf(YType.str, 'chassis-id-string'), ['str'])),
                                            ('chassis_id_mac', (YLeaf(YType.str, 'chassis-id-mac'), ['str'])),
                                            ('chassis_id_raw', (YLeaf(YType.str, 'chassis-id-raw'), ['str'])),
                                        ])
                                        self.chassis_id_format = None
                                        self.chassis_id_string = None
                                        self.chassis_id_mac = None
                                        self.chassis_id_raw = None
                                        self._segment_path = lambda: "chassis-id-value"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue, ['chassis_id_format', 'chassis_id_string', 'chassis_id_mac', 'chassis_id_raw'], name, value)


                        class MepName(Entity):
                            """
                            MEP name
                            
                            .. attribute:: name
                            
                            	MEP name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.MepName, self).__init__()

                                self.yang_name = "mep-name"
                                self.yang_parent_name = "last-ccm-received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.name = None
                                self._segment_path = lambda: "mep-name"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.MepName, ['name'], name, value)


                        class OrganizationSpecificTlv(Entity):
                            """
                            Organizational\-specific TLVs
                            
                            .. attribute:: oui
                            
                            	Organizationally\-unique ID
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: subtype
                            
                            	Subtype of TLV
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: value
                            
                            	Binary data in TLV
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv, self).__init__()

                                self.yang_name = "organization-specific-tlv"
                                self.yang_parent_name = "last-ccm-received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('oui', (YLeaf(YType.str, 'oui'), ['str'])),
                                    ('subtype', (YLeaf(YType.uint8, 'subtype'), ['int'])),
                                    ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                ])
                                self.oui = None
                                self.subtype = None
                                self.value = None
                                self._segment_path = lambda: "organization-specific-tlv"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv, ['oui', 'subtype', 'value'], name, value)


                        class UnknownTlv(Entity):
                            """
                            Unknown TLVs
                            
                            .. attribute:: typecode
                            
                            	Type code of TLV
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: value
                            
                            	Binary data in TLV
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv, self).__init__()

                                self.yang_name = "unknown-tlv"
                                self.yang_parent_name = "last-ccm-received"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('typecode', (YLeaf(YType.uint8, 'typecode'), ['int'])),
                                    ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                ])
                                self.typecode = None
                                self.value = None
                                self._segment_path = lambda: "unknown-tlv"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv, ['typecode', 'value'], name, value)


                    class Statistics(Entity):
                        """
                        Peer MEP statistics
                        
                        .. attribute:: last_ccm_received_time
                        
                        	Elapsed time since last CCM received
                        	**type**\:  :py:class:`LastCcmReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime>`
                        
                        .. attribute:: ccms_received
                        
                        	Number of CCMs received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_wrong_level
                        
                        	Number of CCMs received with an invalid level
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_maid
                        
                        	Number of CCMs received with an invalid MAID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_interval
                        
                        	Number of CCMs received with an invalid interval
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_source_mac_address
                        
                        	Number of CCMs received with an invalid source MAC address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_our_mep_id
                        
                        	Number of CCMs received with our MEP ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_rdi
                        
                        	Number of CCMs received with the Remote Defect Indication bit set
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_out_of_sequence
                        
                        	Number of CCMs received out\-of\-sequence
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_ccm_sequence_number
                        
                        	Sequence number of last CCM received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2017-10-06'

                        def __init__(self):
                            super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics, self).__init__()

                            self.yang_name = "statistics"
                            self.yang_parent_name = "peer-mep"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("last-ccm-received-time", ("last_ccm_received_time", Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime))])
                            self._leafs = OrderedDict([
                                ('ccms_received', (YLeaf(YType.uint64, 'ccms-received'), ['int'])),
                                ('ccms_wrong_level', (YLeaf(YType.uint64, 'ccms-wrong-level'), ['int'])),
                                ('ccms_invalid_maid', (YLeaf(YType.uint64, 'ccms-invalid-maid'), ['int'])),
                                ('ccms_invalid_interval', (YLeaf(YType.uint64, 'ccms-invalid-interval'), ['int'])),
                                ('ccms_invalid_source_mac_address', (YLeaf(YType.uint64, 'ccms-invalid-source-mac-address'), ['int'])),
                                ('ccms_our_mep_id', (YLeaf(YType.uint64, 'ccms-our-mep-id'), ['int'])),
                                ('ccms_rdi', (YLeaf(YType.uint64, 'ccms-rdi'), ['int'])),
                                ('ccms_out_of_sequence', (YLeaf(YType.uint64, 'ccms-out-of-sequence'), ['int'])),
                                ('last_ccm_sequence_number', (YLeaf(YType.uint32, 'last-ccm-sequence-number'), ['int'])),
                            ])
                            self.ccms_received = None
                            self.ccms_wrong_level = None
                            self.ccms_invalid_maid = None
                            self.ccms_invalid_interval = None
                            self.ccms_invalid_source_mac_address = None
                            self.ccms_our_mep_id = None
                            self.ccms_rdi = None
                            self.ccms_out_of_sequence = None
                            self.last_ccm_sequence_number = None

                            self.last_ccm_received_time = Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime()
                            self.last_ccm_received_time.parent = self
                            self._children_name_map["last_ccm_received_time"] = "last-ccm-received-time"
                            self._segment_path = lambda: "statistics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics, ['ccms_received', 'ccms_wrong_level', 'ccms_invalid_maid', 'ccms_invalid_interval', 'ccms_invalid_source_mac_address', 'ccms_our_mep_id', 'ccms_rdi', 'ccms_out_of_sequence', 'last_ccm_sequence_number'], name, value)


                        class LastCcmReceivedTime(Entity):
                            """
                            Elapsed time since last CCM received
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: nanosecond
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2017-10-06'

                            def __init__(self):
                                super(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime, self).__init__()

                                self.yang_name = "last-ccm-received-time"
                                self.yang_parent_name = "statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                                    ('nanoseconds', (YLeaf(YType.uint32, 'nanoseconds'), ['int'])),
                                ])
                                self.seconds = None
                                self.nanoseconds = None
                                self._segment_path = lambda: "last-ccm-received-time"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Cfm.Global.PeerMePv2s.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime, ['seconds', 'nanoseconds'], name, value)

    def clone_ptr(self):
        self._top_entity = Cfm()
        return self._top_entity


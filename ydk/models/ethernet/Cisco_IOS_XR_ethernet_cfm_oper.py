""" Cisco_IOS_XR_ethernet_cfm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-cfm package operational data.

This module contains definitions
for the following management objects\:
  cfm\: CFM operational data

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-sla\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CfmAisDirEnum(Enum):
    """
    CfmAisDirEnum

    Cfm ais dir

    .. data:: UP = 0

    	Packets sent inward

    .. data:: DOWN = 1

    	Packets sent outward

    """

    UP = 0

    DOWN = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmAisDirEnum']


class CfmBagAisIntervalEnum(Enum):
    """
    CfmBagAisIntervalEnum

    CFM AIS intervals

    .. data:: AIS_INTERVAL_NONE = 0

    	Invalid AIS interval

    .. data:: AIS_INTERVAL1S = 4

    	Interval of 1s

    .. data:: AIS_INTERVAL1M = 6

    	Interval of 1 min

    """

    AIS_INTERVAL_NONE = 0

    AIS_INTERVAL1S = 4

    AIS_INTERVAL1M = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagAisIntervalEnum']


class CfmBagBdidFmtEnum(Enum):
    """
    CfmBagBdidFmtEnum

    Bridge domain identifier format

    .. data:: INVALID = 0

    	Invalid BDID identifier format

    .. data:: BD_ID = 1

    	Identifier is a bridge domain ID

    .. data:: XC_P2P_ID = 2

    	Identifier is a P2P cross-connect ID

    .. data:: XC_MP2MP_ID = 3

    	Identifier is a MP2MP cross-connect ID

    .. data:: DOWN_ONLY = 4

    	Identifier is a maintenance association name

    """

    INVALID = 0

    BD_ID = 1

    XC_P2P_ID = 2

    XC_MP2MP_ID = 3

    DOWN_ONLY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagBdidFmtEnum']


class CfmBagCcmIntervalEnum(Enum):
    """
    CfmBagCcmIntervalEnum

    CFM CCM intervals

    .. data:: INTERVAL_NONE = 0

    	Invalid CCM interval

    .. data:: INTERVAL3_3MS = 1

    	Interval of 3.3ms

    .. data:: INTERVAL10MS = 2

    	Interval of 10ms

    .. data:: INTERVAL100MS = 3

    	Interval of 100ms

    .. data:: INTERVAL1S = 4

    	Interval of 1s

    .. data:: INTERVAL10S = 5

    	Interval of 10s

    .. data:: INTERVAL1M = 6

    	Interval of 1 min

    .. data:: INTERVAL10M = 7

    	Interval of 10 mins

    """

    INTERVAL_NONE = 0

    INTERVAL3_3MS = 1

    INTERVAL10MS = 2

    INTERVAL100MS = 3

    INTERVAL1S = 4

    INTERVAL10S = 5

    INTERVAL1M = 6

    INTERVAL10M = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagCcmIntervalEnum']


class CfmBagCcmOffloadEnum(Enum):
    """
    CfmBagCcmOffloadEnum

    Offload status of CCM processing

    .. data:: OFFLOAD_NONE = 0

    	CCM processing has not been offloaded

    .. data:: OFFLOAD_SOFTWARE = 1

    	CCM processing has been offloaded to software

    .. data:: OFFLOAD_HARDWARE = 2

    	CCM processing has been offloaded to hardware

    """

    OFFLOAD_NONE = 0

    OFFLOAD_SOFTWARE = 1

    OFFLOAD_HARDWARE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagCcmOffloadEnum']


class CfmBagDirectionEnum(Enum):
    """
    CfmBagDirectionEnum

    MEP direction

    .. data:: DIRECTION_UP = 0

    	Up

    .. data:: DIRECTION_DOWN = 1

    	Down

    .. data:: DIRECTION_INVALID = 2

    	Invalid direction

    """

    DIRECTION_UP = 0

    DIRECTION_DOWN = 1

    DIRECTION_INVALID = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagDirectionEnum']


class CfmBagIssuRoleEnum(Enum):
    """
    CfmBagIssuRoleEnum

    CFM ISSU role

    .. data:: UNKNOWN = 0

    	Unknown

    .. data:: PRIMARY = 1

    	Primary

    .. data:: SECONDARY = 2

    	Secondary

    """

    UNKNOWN = 0

    PRIMARY = 1

    SECONDARY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagIssuRoleEnum']


class CfmBagIwStateEnum(Enum):
    """
    CfmBagIwStateEnum

    CFM Interworking state

    .. data:: INTERWORKING_UP = 0

    	Interface is UP

    .. data:: INTERWORKING_TEST = 1

    	Interface is in TEST mode

    """

    INTERWORKING_UP = 0

    INTERWORKING_TEST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagIwStateEnum']


class CfmBagMdLevelEnum(Enum):
    """
    CfmBagMdLevelEnum

    CFM level

    .. data:: LEVEL0 = 0

    	CFM level 0

    .. data:: LEVEL1 = 1

    	CFM level 1

    .. data:: LEVEL2 = 2

    	CFM level 2

    .. data:: LEVEL3 = 3

    	CFM level 3

    .. data:: LEVEL4 = 4

    	CFM level 4

    .. data:: LEVEL5 = 5

    	CFM level 5

    .. data:: LEVEL6 = 6

    	CFM level 6

    .. data:: LEVEL7 = 7

    	CFM level 7

    .. data:: LEVEL_INVALID = 8

    	Invalid CFM level

    """

    LEVEL0 = 0

    LEVEL1 = 1

    LEVEL2 = 2

    LEVEL3 = 3

    LEVEL4 = 4

    LEVEL5 = 5

    LEVEL6 = 6

    LEVEL7 = 7

    LEVEL_INVALID = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagMdLevelEnum']


class CfmBagMdidFmtEnum(Enum):
    """
    CfmBagMdidFmtEnum

    CFM MDID format

    .. data:: MDID_NULL = 1

    	MDID is explicity NULL

    .. data:: MDID_DNS_LIKE = 2

    	MDID is based on a DNS name

    .. data:: MDID_MAC_ADDRESS = 3

    	MDID is a (MAC address, integer) pair

    .. data:: MDID_STRING = 4

    	MDID is a character string

    .. data:: MDID_UNKNOWN = 5

    	Unknown MDID format

    """

    MDID_NULL = 1

    MDID_DNS_LIKE = 2

    MDID_MAC_ADDRESS = 3

    MDID_STRING = 4

    MDID_UNKNOWN = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagMdidFmtEnum']


class CfmBagOpcodeEnum(Enum):
    """
    CfmBagOpcodeEnum

    CFM Opcode

    .. data:: RESERVED = 0

    	Reserved

    .. data:: CCM = 1

    	Continuity Check

    .. data:: LBR = 2

    	Loopback Reply

    .. data:: LBM = 3

    	Loopback Message

    .. data:: LTR = 4

    	Linktrace Reply

    .. data:: LTM = 5

    	Linktrace Message

    """

    RESERVED = 0

    CCM = 1

    LBR = 2

    LBM = 3

    LTR = 4

    LTM = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagOpcodeEnum']


class CfmBagSmanFmtEnum(Enum):
    """
    CfmBagSmanFmtEnum

    Short MA Name format

    .. data:: SMAN_VLAN_ID = 1

    	Short MA Name is a 12-bit VLAN-ID

    .. data:: SMAN_STRING = 2

    	Short MA Name is a character string

    .. data:: SMAN_UINT16 = 3

    	Short MA Name is a 16-bit unsigned integer

    .. data:: SMAN_VPN_ID = 4

    	Short MA Name is a global VPN identifier

    .. data:: SMAN_ICC = 32

    	Short MA Name uses the ICC-based format

    .. data:: SMAN_UNKNOWN = 33

    	Unknown Short MA Name format

    """

    SMAN_VLAN_ID = 1

    SMAN_STRING = 2

    SMAN_UINT16 = 3

    SMAN_VPN_ID = 4

    SMAN_ICC = 32

    SMAN_UNKNOWN = 33


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagSmanFmtEnum']


class CfmBagStpStateEnum(Enum):
    """
    CfmBagStpStateEnum

    CFM STP state

    .. data:: STP_UP = 0

    	Interface is UP

    .. data:: STP_BLOCKED = 1

    	Interface is STP-blocked

    .. data:: STP_UNKNOWN = 2

    	Unknown Interface STP state

    """

    STP_UP = 0

    STP_BLOCKED = 1

    STP_UNKNOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmBagStpStateEnum']


class CfmMaMpVarietyEnum(Enum):
    """
    CfmMaMpVarietyEnum

    CFM MA Maintenance Point varieties

    .. data:: MIP = 0

    	MIP

    .. data:: UP_MEP = 1

    	Up MEP

    .. data:: DOWNMEP = 2

    	Down MEP

    .. data:: UNKNOWN_MEP = 3

    	Unknown MEP

    """

    MIP = 0

    UP_MEP = 1

    DOWNMEP = 2

    UNKNOWN_MEP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmMaMpVarietyEnum']


class CfmPmAddlIntfStatusEnum(Enum):
    """
    CfmPmAddlIntfStatusEnum

    Additional interface status

    .. data:: UNKNOWN = 0

    	Additional interface status unknown

    .. data:: ADMINISTRATIVELY_DOWN = 1

    	Interface is explicitly shutdown in

    	configuration

    .. data:: REMOTE_EXCESSIVE_ERRORS = 2

    	Remote interface has exceeded its 802.3 Link

    	OAM error threshold

    .. data:: LOCAL_EXCESSIVE_ERRORS = 3

    	Local interface has exceeded its 802.3 Link OAM

    	error threshold

    """

    UNKNOWN = 0

    ADMINISTRATIVELY_DOWN = 1

    REMOTE_EXCESSIVE_ERRORS = 2

    LOCAL_EXCESSIVE_ERRORS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAddlIntfStatusEnum']


class CfmPmAisReceiveEnum(Enum):
    """
    CfmPmAisReceiveEnum

    Enumeration of how the MEP is receiving the

    signal, directly or via AIS or LCK messages.

    .. data:: RECEIVE_NONE = 0

    	No signal received

    .. data:: RECEIVE_AIS = 1

    	Receiving AIS messages

    .. data:: RECEIVE_LCK = 2

    	Receiving LCK messages

    .. data:: RECEIVE_DIRECT = 3

    	Receiving AIS directly from another MEP on the

    	same interface

    """

    RECEIVE_NONE = 0

    RECEIVE_AIS = 1

    RECEIVE_LCK = 2

    RECEIVE_DIRECT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAisReceiveEnum']


class CfmPmAisTransmitEnum(Enum):
    """
    CfmPmAisTransmitEnum

    Enumeration of how the MEP is transmitting AIS,

    via a MIP or directly to a higher MEP

    .. data:: TRANSMIT_NONE = 0

    	AIS not transmitted

    .. data:: TRANSMIT_AIS = 1

    	AIS transmitted via MIP

    .. data:: TRANSMIT_AIS_DIRECT = 2

    	AIS signal passed directly to a higher MEP

    """

    TRANSMIT_NONE = 0

    TRANSMIT_AIS = 1

    TRANSMIT_AIS_DIRECT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmAisTransmitEnum']


class CfmPmChassisIdFmtEnum(Enum):
    """
    CfmPmChassisIdFmtEnum

    Chassis ID type

    .. data:: CHASSIS_ID_CHASSIS_COMPONENT = 1

    	Chassis ID is a component name

    .. data:: CHASSIS_ID_INTERFACE_ALIAS = 2

    	Chassis ID is an interface alias

    .. data:: CHASSIS_ID_PORT_COMPONENT = 3

    	Chassis ID is a port component name

    .. data:: CHASSIS_ID_MAC_ADDRESS = 4

    	Chassis ID is a MAC address

    .. data:: CHASSIS_ID_NETWORK_ADDRESS = 5

    	Chassis ID is a network address

    .. data:: CHASSIS_ID_INTERFACE_NAME = 6

    	Chassis ID is an interface name

    .. data:: CHASSIS_ID_LOCAL = 7

    	Chassis ID is a local name

    .. data:: CHASSIS_ID_UNKNOWN_TYPE = 8

    	Unknown Chassis ID type

    """

    CHASSIS_ID_CHASSIS_COMPONENT = 1

    CHASSIS_ID_INTERFACE_ALIAS = 2

    CHASSIS_ID_PORT_COMPONENT = 3

    CHASSIS_ID_MAC_ADDRESS = 4

    CHASSIS_ID_NETWORK_ADDRESS = 5

    CHASSIS_ID_INTERFACE_NAME = 6

    CHASSIS_ID_LOCAL = 7

    CHASSIS_ID_UNKNOWN_TYPE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmChassisIdFmtEnum']


class CfmPmEgressActionEnum(Enum):
    """
    CfmPmEgressActionEnum

    Egress action

    .. data:: EGRESS_OK = 1

    	OK

    .. data:: EGRESS_DOWN = 2

    	Down

    .. data:: EGRESS_BLOCKED = 3

    	STP Blocked

    .. data:: EGRESS_VID = 4

    	VID Blocked

    """

    EGRESS_OK = 1

    EGRESS_DOWN = 2

    EGRESS_BLOCKED = 3

    EGRESS_VID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmEgressActionEnum']


class CfmPmElmReplyFilterEnum(Enum):
    """
    CfmPmElmReplyFilterEnum

    Reply filter used for Exploratory Linktrace

    operations

    .. data:: REPLY_FILTER_NOT_PRESENT = 0

    	Reply Filter not present

    .. data:: REPLY_FILTER_DEFAULT = 1

    	Reply from ports which are not MAC-pruned,

    	VID-pruned, or STP-blocked

    .. data:: REPLY_FILTER_VLAN_TOPOLOGY = 2

    	Reply from ports which are not VID-pruned or

    	STP-blocked

    .. data:: REPLY_FILTER_SPANNING_TREE = 3

    	Reply from ports which are not STP-blocked

    .. data:: REPLY_FILTER_ALL_PORTS = 4

    	Reply from all ports

    """

    REPLY_FILTER_NOT_PRESENT = 0

    REPLY_FILTER_DEFAULT = 1

    REPLY_FILTER_VLAN_TOPOLOGY = 2

    REPLY_FILTER_SPANNING_TREE = 3

    REPLY_FILTER_ALL_PORTS = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElmReplyFilterEnum']


class CfmPmElrEgressActionEnum(Enum):
    """
    CfmPmElrEgressActionEnum

    ELR Egress action

    .. data:: ELR_EGRESS_OK = 1

    	OK

    .. data:: ELR_EGRESS_DOWN = 2

    	Down

    .. data:: ELR_EGRESS_BLOCKED = 3

    	STP Blocked

    .. data:: ELR_EGRESS_VID = 4

    	VID Blocked

    .. data:: ELR_EGRESS_MAC = 255

    	MAC Pruned

    """

    ELR_EGRESS_OK = 1

    ELR_EGRESS_DOWN = 2

    ELR_EGRESS_BLOCKED = 3

    ELR_EGRESS_VID = 4

    ELR_EGRESS_MAC = 255


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrEgressActionEnum']


class CfmPmElrIngressActionEnum(Enum):
    """
    CfmPmElrIngressActionEnum

    ELR Ingress action

    .. data:: ELR_INGRESS_OK = 1

    	OK

    .. data:: ELR_INGRESS_DOWN = 2

    	Down

    .. data:: ELR_INGRESS_BLOCKED = 3

    	STP Blocked

    .. data:: ELR_INGRESS_VID = 4

    	VID Blocked

    """

    ELR_INGRESS_OK = 1

    ELR_INGRESS_DOWN = 2

    ELR_INGRESS_BLOCKED = 3

    ELR_INGRESS_VID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrIngressActionEnum']


class CfmPmElrRelayActionEnum(Enum):
    """
    CfmPmElrRelayActionEnum

    ELR relay action

    .. data:: ELR_RELAY_HIT = 1

    	Target Hit

    .. data:: ELR_RELAY_FDB = 2

    	Filtering database

    .. data:: ELR_RELAY_FLOOD = 3

    	Flood forwarded

    .. data:: ELR_RELAY_DROP = 4

    	Dropped

    """

    ELR_RELAY_HIT = 1

    ELR_RELAY_FDB = 2

    ELR_RELAY_FLOOD = 3

    ELR_RELAY_DROP = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmElrRelayActionEnum']


class CfmPmEltDelayModelEnum(Enum):
    """
    CfmPmEltDelayModelEnum

    Delay model used for Exploratory Linktrace

    operations

    .. data:: DELAY_MODEL_INVALID = 0

    	Not a valid delay model

    .. data:: DELAY_MODEL_LOGARITHMIC = 1

    	Reply using logarithmic delay model

    .. data:: DELAY_MODEL_CONSTANT = 2

    	Reply using constant delay model

    """

    DELAY_MODEL_INVALID = 0

    DELAY_MODEL_LOGARITHMIC = 1

    DELAY_MODEL_CONSTANT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmEltDelayModelEnum']


class CfmPmIdFmtEnum(Enum):
    """
    CfmPmIdFmtEnum

    ID format

    .. data:: ID_FORMAT_IS_STRING = 0

    	ID format is a string

    .. data:: ID_FORMAT_IS_MAC_ADDRESS = 1

    	ID format is a MAC address

    .. data:: ID_FORMAT_IS_RAW_HEX = 2

    	ID format is raw hex

    """

    ID_FORMAT_IS_STRING = 0

    ID_FORMAT_IS_MAC_ADDRESS = 1

    ID_FORMAT_IS_RAW_HEX = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIdFmtEnum']


class CfmPmIngressActionEnum(Enum):
    """
    CfmPmIngressActionEnum

    Ingress action

    .. data:: INGRESS_OK = 1

    	OK

    .. data:: INGRESS_DOWN = 2

    	Down

    .. data:: INGRESS_BLOCKED = 3

    	STP Blocked

    .. data:: INGRESS_VID = 4

    	VID Blocked

    """

    INGRESS_OK = 1

    INGRESS_DOWN = 2

    INGRESS_BLOCKED = 3

    INGRESS_VID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIngressActionEnum']


class CfmPmIntfStatusEnum(Enum):
    """
    CfmPmIntfStatusEnum

    Interface status

    .. data:: INTERFACE_STATUS_UP = 1

    	Interface is up

    .. data:: INTERFACE_STATUS_DOWN = 2

    	Interface is down

    .. data:: INTERFACE_STATUS_TESTING = 3

    	Interface is in testing mode

    .. data:: INTERFACE_STATUS_UNKNOWN = 4

    	Unknown interface status

    .. data:: INTERFACE_STATUS_DORMANT = 5

    	Interface is dormant

    .. data:: INTERFACE_STATUS_NOT_PRESENT = 6

    	Interface status not found

    .. data:: INTERFACE_STATUS_LOWER_LAYER_DOWN = 7

    	Lower layer is down

    """

    INTERFACE_STATUS_UP = 1

    INTERFACE_STATUS_DOWN = 2

    INTERFACE_STATUS_TESTING = 3

    INTERFACE_STATUS_UNKNOWN = 4

    INTERFACE_STATUS_DORMANT = 5

    INTERFACE_STATUS_NOT_PRESENT = 6

    INTERFACE_STATUS_LOWER_LAYER_DOWN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmIntfStatusEnum']


class CfmPmLastHopFmtEnum(Enum):
    """
    CfmPmLastHopFmtEnum

    Last hop identifier format

    .. data:: LAST_HOP_NONE = 0

    	No last hop identifier

    .. data:: LAST_HOP_HOST_NAME = 1

    	Last hop identifier is a hostname

    .. data:: LAST_HOP_EGRESS_ID = 2

    	Last hop identifier is an egress ID

    """

    LAST_HOP_NONE = 0

    LAST_HOP_HOST_NAME = 1

    LAST_HOP_EGRESS_ID = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmLastHopFmtEnum']


class CfmPmLtModeEnum(Enum):
    """
    CfmPmLtModeEnum

    Type of Linktrace operation

    .. data:: CFM_PM_LT_MODE_BASIC = 1

    	Basic IEEE 802.1ag Linktrace

    .. data:: CFM_PM_LT_MODE_EXPLORATORY = 2

    	Cisco Exploratory Linktrace

    """

    CFM_PM_LT_MODE_BASIC = 1

    CFM_PM_LT_MODE_EXPLORATORY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmLtModeEnum']


class CfmPmMepDefectEnum(Enum):
    """
    CfmPmMepDefectEnum

    Defects that can be reported by a MEP

    .. data:: DEFECT_NONE = 0

    	No defect reported

    .. data:: DEFECT_RDI_CCM = 1

    	Some Peer MEP's CCM has the RDI bit set

    .. data:: DEFECT_MA_CSTATUS = 2

    	A Peer MEP port or interface status error has

    	been reported

    .. data:: DEFECT_REMOTE_CCM = 3

    	Not receiving valid CCMs from at least one Peer

    	MEP

    .. data:: DEFECT_ERROR_CCM = 4

    	Currently receiving invalid CCMs from at least

    	one Peer MEP

    .. data:: DEFECT_CROSS_CONNECT_CCM = 5

    	Currently receiving CCMs from an incorrect

    	service (MA)

    """

    DEFECT_NONE = 0

    DEFECT_RDI_CCM = 1

    DEFECT_MA_CSTATUS = 2

    DEFECT_REMOTE_CCM = 3

    DEFECT_ERROR_CCM = 4

    DEFECT_CROSS_CONNECT_CCM = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmMepDefectEnum']


class CfmPmMepFngStateEnum(Enum):
    """
    CfmPmMepFngStateEnum

    Fault Notification Generation state machine

    states

    .. data:: FNG_RESET = 1

    	FNG in reset state

    .. data:: FNG_DEFECT = 2

    	FNG has detected but not yet reported a defect

    .. data:: FNG_REPORT_DEFECT = 3

    	FNG is in the process of reporting a defect

    .. data:: FNG_DEFECT_REPORTED = 4

    	FNG has reported a defect

    .. data:: FNG_DEFECT_CLEARING = 5

    	No defect present, but the reset timer has not

    	yet expired

    """

    FNG_RESET = 1

    FNG_DEFECT = 2

    FNG_REPORT_DEFECT = 3

    FNG_DEFECT_REPORTED = 4

    FNG_DEFECT_CLEARING = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmMepFngStateEnum']


class CfmPmPktActionEnum(Enum):
    """
    CfmPmPktActionEnum

    Action taken for received packet

    .. data:: PACKET_PROCESSED = 0

    	Packet processed successfully

    .. data:: PACKET_FORWARDED = 1

    	Packet forwarded

    .. data:: UNKNOWN_OPCODE = 2

    	Packet dropped at a MEP due to unknown opcode

    .. data:: FILTER_LEVEL = 3

    	Packet dropped due to level/opcode filtering at

    	a MEP

    .. data:: FILTER_BLOCKED = 4

    	Packet dropped because interface is STP blocked

    .. data:: FILTER_LOCAL_MAC = 5

    	Packet dropped due to local destination MAC

    .. data:: MALFORMED_CCM_SIZE = 6

    	CCM too short or too long

    .. data:: MALFORMED_CCM_MEP_ID = 7

    	Invalid MEP-ID

    .. data:: MALFORMED_TOO_SHORT = 8

    	Packet too short

    .. data:: MALFORMED_DESTINATION_MAC_UNICAST = 9

    	Destination MAC address does not match

    	interface

    .. data:: MALFORMED_DESTINATION_MAC_MULTICAST = 10

    	Invalid multicast destination MAC address

    .. data:: MALFORMED_TLV_OFFSET = 11

    	TLV offset too short or beyond the end of the

    	packet

    .. data:: MALFORMED_LBM_SOURCE_MAC = 12

    	Invalid source MAC address for LBM

    .. data:: MALFORMED_LTR_RELAY_ACTION = 13

    	Unknown LTR relay action

    .. data:: MALFORMED_LTR_REPLY_TLV = 14

    	LTR has neither reply-ingress or reply-egress

    .. data:: MALFORMED_LT_ORIGIN = 15

    	Invalid Linktrace Message origin MAC address

    .. data:: MALFORMED_LTM_TARGET = 16

    	Invalid LTM target MAC address

    .. data:: MALFORMED_SOURCE_MAC = 17

    	Invalid source MAC address

    .. data:: MALFORMED_HEADER_TOO_SHORT = 18

    	Packet too short for CFM header

    .. data:: MALFORMED_TLV_HEADER_OVERRUN = 19

    	TLV header extends beyond the end of the packet

    .. data:: MALFORMED_TLV_OVERRUN = 20

    	TLV extends beyond the end of the packet

    .. data:: MALFORMED_DUPLICATE_SENDER_ID = 21

    	Multiple Sender-ID TLVs found

    .. data:: MALFORMED_DUPLICATE_PORT_STATUS = 22

    	Multiple Port-status TLVs found

    .. data:: MALFORMED_DUPLICATE_INTERFACE_STATUS = 23

    	Multiple Interface-state TLVs found

    .. data:: MALFORMED_WRONG_TLV = 24

    	Invalid TLV for this type of packet found

    .. data:: MALFORMED_DUPLICATE_DATA = 25

    	Multiple Data TLVs found

    .. data:: MALFORMED_DUPLICATE_LTR_EGRESS_ID = 26

    	Multiple LTR-Egress-ID TLVs found

    .. data:: MALFORMED_DUPLICATE_REPLY_INGRESS = 27

    	Multiple Reply-ingress TLVs found

    .. data:: MALFORMED_DUPLICATE_REPLY_EGRESS = 28

    	Multiple Reply-egress TLVs found

    .. data:: MALFORMED_DUPLICATE_LTM_EGRESS_ID = 29

    	Multiple LTM-Egress-ID TLVs found

    .. data:: MALFORMED_SENDER_ID_SIZE = 30

    	Sender-ID TLV is too short

    .. data:: MALFORMED_CHASSIS_ID_SIZE = 31

    	Sender-ID TLV is too short to contain the

    	Chassis ID

    .. data:: MALFORMED_MGMT_ADDRESS_DOMAIN_SIZE = 32

    	Sender-ID TLV is too short to contain the

    	management address domain

    .. data:: MALFORMED_MGMT_ADDRESS_SIZE = 33

    	Sender-ID TLV is too short to contain the

    	management address

    .. data:: MALFORMED_PORT_STATUS_SIZE = 34

    	Port-status TLV is too short

    .. data:: MALFORMED_PORT_STATUS = 35

    	Invalid Port status value

    .. data:: MALFORMED_INTERFACE_STATUS_SIZE = 36

    	Interface-status TLV is too short

    .. data:: MALFORMED_INTERFACE_STATUS = 37

    	Invalid Interface status value

    .. data:: MALFORMED_ORGANIZATION_SPECIFIC_TLV_SIZE = 38

    	Organization-specific TLV is too short

    .. data:: MALFORMED_DUPLICATE_MEP_NAME = 39

    	Multiple MEP-name TLVs found

    .. data:: MALFORMED_DUPLICATE_ADDITIONAL_INTERFACE_STATUS = 40

    	Multiple additional-interface-status TLVs found

    .. data:: MALFORMED_LTR_EGRESS_ID_SIZE = 41

    	LTR-Egress-ID TLV is too short

    .. data:: MALFORMED_REPLY_INGRESS_SIZE = 42

    	Reply-ingress TLV is too short

    .. data:: MALFORMED_INGRESS_ACTION = 43

    	Invalid ingress-action value

    .. data:: MALFORMED_REPLY_INGRESS_MAC = 44

    	Reply-ingress TLV has invalid MAC address

    .. data:: MALFORMED_INGRESS_PORT_LENGTH_SIZE = 45

    	Reply-ingress TLV is too short to contain the

    	Port ID type

    .. data:: MALFORMED_INGRESS_PORT_ID_LENGTH = 46

    	Reply-ingress TLV has a zero Port ID length

    .. data:: MALFORMED_INGRESS_PORT_ID_SIZE = 47

    	Reply-ingress TLV is too short to contain the

    	Port ID

    .. data:: MALFORMED_REPLY_EGRESS_SIZE = 48

    	Reply-egress TLV is too short

    .. data:: MALFORMED_EGRESS_ACTION = 49

    	Invalid egress-action value

    .. data:: MALFORMED_REPLY_EGRESS_MAC = 50

    	Reply-egress TLV has invalid MAC address

    .. data:: MALFORMED_EGRESS_PORT_LENGTH_SIZE = 51

    	Reply-egress TLV is too short to contain the

    	Port ID type

    .. data:: MALFORMED_EGRESS_PORT_ID_LENGTH = 52

    	Reply-egress TLV has a zero Port ID length

    .. data:: MALFORMED_EGRESS_PORT_ID_SIZE = 53

    	Reply-egress TLV is too short to contain the

    	Port ID

    .. data:: MALFORMED_LTM_EGRESS_ID_SIZE = 54

    	LTM-Egress_ID TLV is too short

    .. data:: MALFORMED_MEP_NAME_SIZE = 55

    	MEP-name TLV is too short

    .. data:: MALFORMED_MEP_NAME_NAME_LENGTH = 56

    	MEP-name TLV is too short to contain a MEP name

    .. data:: MALFORMED_ADDITIONAL_INTERFACE_STATUS_SIZE = 57

    	Additional-interface-status is too short

    .. data:: MALFORMED_ADDITIONAL_INTERFACE_STATUS = 58

    	Invalid additional interface status

    .. data:: MALFORMED_CCM_INTERVAL = 59

    	CCM has a zero CCM interval

    .. data:: MALFORMED_MDID_MAC_ADDRESS_LENGTH = 60

    	CCM has a MAC-address MDID but the MDID is the

    	wrong length

    .. data:: MALFORMED_MDID_LENGTH = 61

    	CCM has an invalid MDID length

    .. data:: MALFORMED_SMAN_LENGTH = 62

    	CCM has an invalid Short MA Name length

    .. data:: MALFORMED_SMAN2_BYTE_LENGTH = 63

    	CCM has a VID or 16-bit Short MA Name but a

    	mismatched length

    .. data:: MALFORMED_SMAN_VPN_ID_LENGTH = 64

    	CCM has a VPNID Short MA Name but a mismatched

    	length

    .. data:: MALFORMED_ELR_NO_REPLY_TLV = 65

    	ELR has no ELR Reply TLVs

    .. data:: MALFORMED_SEPARATE_ELR_REPLY_EGRESS = 66

    	ELR Reply Egress TLVs not all adjacent

    .. data:: MALFORMED_DCM_DESTINATION_MULTICAST = 67

    	DCM has a multicast destination MAC

    .. data:: MALFORMED_DCM_EMBED_LENGTH = 68

    	DCM is too short to contain an Embedded PDU

    .. data:: MALFORMED_DCM_EMBED_LEVEL = 69

    	DCM Embedded PDU level does not match DCM level

    .. data:: MALFORMED_DCM_EMBED_VERSION = 70

    	DCM Embedded PDU version does not match DCM

    	version

    .. data:: MALFORMED_ELR_RELAY_ACTION = 71

    	Unknown ELR relay action

    .. data:: MALFORMED_ELR_TT_LS = 73

    	Reply Ingress TTL is not one greater than Reply

    	Egress TTL

    .. data:: MALFORMED_ELR_TTL_INGRESS = 74

    	Reply Ingress TTL present without ELR Reply

    	Ingress TLV

    .. data:: MALFORMED_ELR_TTL_EGRESS = 75

    	Reply Egress TTL present without ELR Reply

    	Egress TLV

    .. data:: MALFORMED_ELM_DESTINATION_UNICAST = 76

    	ELM Destination MAC must not be unicast

    .. data:: MALFORMED_ELM_EGRESS_ID = 77

    	ELM has no LTM Egress ID TLV

    .. data:: MALFORMED_DCM_EMBED_OUI = 78

    	Embedded DCM OUI unrecognized

    .. data:: MALFORMED_DCM_EMBED_OPCODE = 79

    	Embedded DCM Opcode is not ELM

    .. data:: MALFORMED_ELM_CONSTANT_ZERO = 80

    	ELM Constant Factor is zero

    .. data:: MALFORMED_ELR_TIMEOUT_ZERO = 81

    	ELR Next-Hop Timeout is zero

    .. data:: MALFORMED_DUPLICATE_TEST = 82

    	Multiple Test TLVs found

    .. data:: MALFORMED_DMM_SOURCE_MAC = 83

    	Invalid source MAC address for DMM

    .. data:: MALFORMED_TEST_SIZE = 84

    	Test TLV is too short

    .. data:: MALFORMED_DMR_TIME_STAMPS = 85

    	DMR has exactly one of its Rxf and Txb

    	timestamps unspecified

    .. data:: MALFORMED_DM_TIME_STAMP_FMT = 86

    	The format of one or more timestamps is invalid

    .. data:: MALFORMED_AIS_INTERVAL = 87

    	AIS/LCK has invalid interval value (not 1

    	second or 1 minute)

    .. data:: FILTER_INTERFACE_DOWN = 88

    	Packet dropped due to interface being down

    .. data:: FILTER_FORWARD_STANDBY = 89

    	Packet dropped - not forwarded because

    	interface is a standby bundle

    .. data:: MALFORMED_SMAN_ICC_BASED_LENGTH = 90

    	CCM has an ICC-based format Short MA Name but a

    	mismatched length

    .. data:: FILTER_FOWARD_ISSU_SECONDARY = 120

    	Packet dropped - not forwarded in secondary HA

    	role

    .. data:: FILTER_RESPONSE_STANDBY = 121

    	Packet dropped - not responded to because

    	interface is a standby bundle

    .. data:: FILTER_RESPONSE_ISSU_SECONDARY = 122

    	Packet dropped - not responded to in secondary

    	HA role

    """

    PACKET_PROCESSED = 0

    PACKET_FORWARDED = 1

    UNKNOWN_OPCODE = 2

    FILTER_LEVEL = 3

    FILTER_BLOCKED = 4

    FILTER_LOCAL_MAC = 5

    MALFORMED_CCM_SIZE = 6

    MALFORMED_CCM_MEP_ID = 7

    MALFORMED_TOO_SHORT = 8

    MALFORMED_DESTINATION_MAC_UNICAST = 9

    MALFORMED_DESTINATION_MAC_MULTICAST = 10

    MALFORMED_TLV_OFFSET = 11

    MALFORMED_LBM_SOURCE_MAC = 12

    MALFORMED_LTR_RELAY_ACTION = 13

    MALFORMED_LTR_REPLY_TLV = 14

    MALFORMED_LT_ORIGIN = 15

    MALFORMED_LTM_TARGET = 16

    MALFORMED_SOURCE_MAC = 17

    MALFORMED_HEADER_TOO_SHORT = 18

    MALFORMED_TLV_HEADER_OVERRUN = 19

    MALFORMED_TLV_OVERRUN = 20

    MALFORMED_DUPLICATE_SENDER_ID = 21

    MALFORMED_DUPLICATE_PORT_STATUS = 22

    MALFORMED_DUPLICATE_INTERFACE_STATUS = 23

    MALFORMED_WRONG_TLV = 24

    MALFORMED_DUPLICATE_DATA = 25

    MALFORMED_DUPLICATE_LTR_EGRESS_ID = 26

    MALFORMED_DUPLICATE_REPLY_INGRESS = 27

    MALFORMED_DUPLICATE_REPLY_EGRESS = 28

    MALFORMED_DUPLICATE_LTM_EGRESS_ID = 29

    MALFORMED_SENDER_ID_SIZE = 30

    MALFORMED_CHASSIS_ID_SIZE = 31

    MALFORMED_MGMT_ADDRESS_DOMAIN_SIZE = 32

    MALFORMED_MGMT_ADDRESS_SIZE = 33

    MALFORMED_PORT_STATUS_SIZE = 34

    MALFORMED_PORT_STATUS = 35

    MALFORMED_INTERFACE_STATUS_SIZE = 36

    MALFORMED_INTERFACE_STATUS = 37

    MALFORMED_ORGANIZATION_SPECIFIC_TLV_SIZE = 38

    MALFORMED_DUPLICATE_MEP_NAME = 39

    MALFORMED_DUPLICATE_ADDITIONAL_INTERFACE_STATUS = 40

    MALFORMED_LTR_EGRESS_ID_SIZE = 41

    MALFORMED_REPLY_INGRESS_SIZE = 42

    MALFORMED_INGRESS_ACTION = 43

    MALFORMED_REPLY_INGRESS_MAC = 44

    MALFORMED_INGRESS_PORT_LENGTH_SIZE = 45

    MALFORMED_INGRESS_PORT_ID_LENGTH = 46

    MALFORMED_INGRESS_PORT_ID_SIZE = 47

    MALFORMED_REPLY_EGRESS_SIZE = 48

    MALFORMED_EGRESS_ACTION = 49

    MALFORMED_REPLY_EGRESS_MAC = 50

    MALFORMED_EGRESS_PORT_LENGTH_SIZE = 51

    MALFORMED_EGRESS_PORT_ID_LENGTH = 52

    MALFORMED_EGRESS_PORT_ID_SIZE = 53

    MALFORMED_LTM_EGRESS_ID_SIZE = 54

    MALFORMED_MEP_NAME_SIZE = 55

    MALFORMED_MEP_NAME_NAME_LENGTH = 56

    MALFORMED_ADDITIONAL_INTERFACE_STATUS_SIZE = 57

    MALFORMED_ADDITIONAL_INTERFACE_STATUS = 58

    MALFORMED_CCM_INTERVAL = 59

    MALFORMED_MDID_MAC_ADDRESS_LENGTH = 60

    MALFORMED_MDID_LENGTH = 61

    MALFORMED_SMAN_LENGTH = 62

    MALFORMED_SMAN2_BYTE_LENGTH = 63

    MALFORMED_SMAN_VPN_ID_LENGTH = 64

    MALFORMED_ELR_NO_REPLY_TLV = 65

    MALFORMED_SEPARATE_ELR_REPLY_EGRESS = 66

    MALFORMED_DCM_DESTINATION_MULTICAST = 67

    MALFORMED_DCM_EMBED_LENGTH = 68

    MALFORMED_DCM_EMBED_LEVEL = 69

    MALFORMED_DCM_EMBED_VERSION = 70

    MALFORMED_ELR_RELAY_ACTION = 71

    MALFORMED_ELR_TT_LS = 73

    MALFORMED_ELR_TTL_INGRESS = 74

    MALFORMED_ELR_TTL_EGRESS = 75

    MALFORMED_ELM_DESTINATION_UNICAST = 76

    MALFORMED_ELM_EGRESS_ID = 77

    MALFORMED_DCM_EMBED_OUI = 78

    MALFORMED_DCM_EMBED_OPCODE = 79

    MALFORMED_ELM_CONSTANT_ZERO = 80

    MALFORMED_ELR_TIMEOUT_ZERO = 81

    MALFORMED_DUPLICATE_TEST = 82

    MALFORMED_DMM_SOURCE_MAC = 83

    MALFORMED_TEST_SIZE = 84

    MALFORMED_DMR_TIME_STAMPS = 85

    MALFORMED_DM_TIME_STAMP_FMT = 86

    MALFORMED_AIS_INTERVAL = 87

    FILTER_INTERFACE_DOWN = 88

    FILTER_FORWARD_STANDBY = 89

    MALFORMED_SMAN_ICC_BASED_LENGTH = 90

    FILTER_FOWARD_ISSU_SECONDARY = 120

    FILTER_RESPONSE_STANDBY = 121

    FILTER_RESPONSE_ISSU_SECONDARY = 122


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPktActionEnum']


class CfmPmPortIdFmtEnum(Enum):
    """
    CfmPmPortIdFmtEnum

    Port ID format

    .. data:: PORT_ID_INTERFACE_ALIAS = 1

    	Port ID is an interface alias

    .. data:: PORT_ID_PORT_COMPONENT = 2

    	Port ID is a component name

    .. data:: PORT_ID_MAC_ADDRESS = 3

    	Port ID is a MAC address

    .. data:: PORT_ID_NETWORK_ADDRESS = 4

    	Port ID is a network address

    .. data:: PORT_ID_INTERFACE_NAME = 5

    	Port ID is an interface name

    .. data:: PORT_ID_AGENT_CIRCUIT_ID = 6

    	Port ID is an agent name

    .. data:: PORT_ID_LOCAL = 7

    	Port ID is a local name

    .. data:: PORT_ID_UNKNOWN = 8

    	Port ID format unknown

    """

    PORT_ID_INTERFACE_ALIAS = 1

    PORT_ID_PORT_COMPONENT = 2

    PORT_ID_MAC_ADDRESS = 3

    PORT_ID_NETWORK_ADDRESS = 4

    PORT_ID_INTERFACE_NAME = 5

    PORT_ID_AGENT_CIRCUIT_ID = 6

    PORT_ID_LOCAL = 7

    PORT_ID_UNKNOWN = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPortIdFmtEnum']


class CfmPmPortStatusEnum(Enum):
    """
    CfmPmPortStatusEnum

    Port status

    .. data:: PORT_STATUS_BLOCKED = 1

    	Port is STP blocked

    .. data:: PORT_STATUS_UP = 2

    	Port is up

    .. data:: PORT_STATUS_UNKNOWN = 3

    	Unknown port status

    """

    PORT_STATUS_BLOCKED = 1

    PORT_STATUS_UP = 2

    PORT_STATUS_UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmPortStatusEnum']


class CfmPmRelayActionEnum(Enum):
    """
    CfmPmRelayActionEnum

    LTR relay action

    .. data:: RELAY_HIT = 1

    	Target Hit

    .. data:: RELAY_FDB = 2

    	Filtering database

    .. data:: RELAY_MPDB = 3

    	CCM Learning database

    """

    RELAY_HIT = 1

    RELAY_FDB = 2

    RELAY_MPDB = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRelayActionEnum']


class CfmPmRmepStateEnum(Enum):
    """
    CfmPmRmepStateEnum

    State of the Peer MEP state machine

    .. data:: PEER_MEP_IDLE = 1

    	Momentary state during reset

    .. data:: PEER_MEP_START = 2

    	Loss timer not expired since reset, but no

    	valid CCM received

    .. data:: PEER_MEP_FAILED = 3

    	Loss timer has expired

    .. data:: PEER_MEP_OK = 4

    	Loss timer has not expired since last valid CCM

    """

    PEER_MEP_IDLE = 1

    PEER_MEP_START = 2

    PEER_MEP_FAILED = 3

    PEER_MEP_OK = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRmepStateEnum']


class CfmPmRmepXcStateEnum(Enum):
    """
    CfmPmRmepXcStateEnum

    Cross\-check state of a peer MEP

    .. data:: CROSS_CHECK_OK = 0

    	Cross-check OK

    .. data:: CROSS_CHECK_MISSING = 1

    	No CCMs received within loss time from peer MEP

    .. data:: CROSS_CHECK_EXTRA = 2

    	CCMs received from peer MEP not marked for

    	cross-check

    """

    CROSS_CHECK_OK = 0

    CROSS_CHECK_MISSING = 1

    CROSS_CHECK_EXTRA = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['CfmPmRmepXcStateEnum']


class SlaBucketSizeEnum(Enum):
    """
    SlaBucketSizeEnum

    Type of configuration of a bucket size

    .. data:: BUCKETS_PER_PROBE = 0

    	Bucket size is configured as buckets per probe

    .. data:: PROBES_PER_BUCKET = 1

    	Bucket size is configured as probes per bucket

    """

    BUCKETS_PER_PROBE = 0

    PROBES_PER_BUCKET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaBucketSizeEnum']


class SlaOperBucketEnum(Enum):
    """
    SlaOperBucketEnum

    Type of SLA metric bucket

    .. data:: BUCKET_TYPE_BINS = 0

    	SLA metric bin

    .. data:: BUCKET_TYPE_SAMPLES = 1

    	SLA metric sample

    """

    BUCKET_TYPE_BINS = 0

    BUCKET_TYPE_SAMPLES = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperBucketEnum']


class SlaOperOperationEnum(Enum):
    """
    SlaOperOperationEnum

    Type of SLA operation

    .. data:: OPERATION_TYPE_CONFIGURED = 0

    	Configured SLA operation

    .. data:: OPERATION_TYPE_ONDEMAND = 1

    	On-demand SLA operation

    """

    OPERATION_TYPE_CONFIGURED = 0

    OPERATION_TYPE_ONDEMAND = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperOperationEnum']


class SlaOperPacketPriorityEnum(Enum):
    """
    SlaOperPacketPriorityEnum

    Priority scheme for packet priority

    .. data:: PRIORITY_NONE = 0

    	Packet does not use any specified priority.

    .. data:: PRIORITY_COS = 1

    	Packet uses a specified 3-bit COS priority

    	value.

    """

    PRIORITY_NONE = 0

    PRIORITY_COS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperPacketPriorityEnum']


class SlaOperTestPatternSchemeEnum(Enum):
    """
    SlaOperTestPatternSchemeEnum

    Test pattern scheme for packet padding

    .. data:: HEX = 0

    	Packet is padded with a user-specified string

    .. data:: PSEUDO_RANDOM = 1

    	Packet is padded with a pseudo-random bit

    	sequence

    """

    HEX = 0

    PSEUDO_RANDOM = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaOperTestPatternSchemeEnum']


class SlaRecordableMetricEnum(Enum):
    """
    SlaRecordableMetricEnum

    Types of metrics that can be recorded by probes

    .. data:: METRIC_INVALID = 0

    	Not a valid metric type

    .. data:: METRIC_ROUND_TRIP_DELAY = 1

    	Round-trip Delay

    .. data:: METRIC_ONE_WAY_DELAY_SD = 2

    	One-way Delay (Source->Destination)

    .. data:: METRIC_ONE_WAY_DELAY_DS = 3

    	One-way Delay (Destination->Source)

    .. data:: METRIC_ROUND_TRIP_JITTER = 4

    	Round-trip Jitter

    .. data:: METRIC_ONE_WAY_JITTER_SD = 5

    	One-way Jitter (Source->Destination)

    .. data:: METRIC_ONE_WAY_JITTER_DS = 6

    	One-way Jitter (Destination->Source)

    .. data:: METRIC_ONE_WAY_FLR_SD = 7

    	One-way Frame Loss Ratio (Source->Destination)

    .. data:: METRIC_ONE_WAY_FLR_DS = 8

    	One-way Frame Loss Ratio (Destination->Source)

    """

    METRIC_INVALID = 0

    METRIC_ROUND_TRIP_DELAY = 1

    METRIC_ONE_WAY_DELAY_SD = 2

    METRIC_ONE_WAY_DELAY_DS = 3

    METRIC_ROUND_TRIP_JITTER = 4

    METRIC_ONE_WAY_JITTER_SD = 5

    METRIC_ONE_WAY_JITTER_DS = 6

    METRIC_ONE_WAY_FLR_SD = 7

    METRIC_ONE_WAY_FLR_DS = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['SlaRecordableMetricEnum']



class Cfm(object):
    """
    CFM operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\: :py:class:`Global <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\: :py:class:`Nodes <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes>`
    
    

    """

    _prefix = 'ethernet-cfm-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_ = Cfm.Global()
        self.global_.parent = self
        self.nodes = Cfm.Nodes()
        self.nodes.parent = self


    class Global(object):
        """
        Global operational data
        
        .. attribute:: global_configuration_errors
        
        	Global configuration errors table
        	**type**\: :py:class:`GlobalConfigurationErrors <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors>`
        
        .. attribute:: incomplete_traceroutes
        
        	Incomplete Traceroute table
        	**type**\: :py:class:`IncompleteTraceroutes <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes>`
        
        .. attribute:: local_meps
        
        	Local MEPs table
        	**type**\: :py:class:`LocalMeps <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps>`
        
        .. attribute:: maintenance_points
        
        	Maintenance Points table
        	**type**\: :py:class:`MaintenancePoints <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints>`
        
        .. attribute:: mep_configuration_errors
        
        	MEP configuration errors table
        	**type**\: :py:class:`MepConfigurationErrors <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors>`
        
        .. attribute:: peer_meps
        
        	Peer MEPs table
        	**type**\: :py:class:`PeerMeps <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps>`
        
        .. attribute:: traceroute_caches
        
        	Traceroute Cache table
        	**type**\: :py:class:`TracerouteCaches <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches>`
        
        

        """

        _prefix = 'ethernet-cfm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_configuration_errors = Cfm.Global.GlobalConfigurationErrors()
            self.global_configuration_errors.parent = self
            self.incomplete_traceroutes = Cfm.Global.IncompleteTraceroutes()
            self.incomplete_traceroutes.parent = self
            self.local_meps = Cfm.Global.LocalMeps()
            self.local_meps.parent = self
            self.maintenance_points = Cfm.Global.MaintenancePoints()
            self.maintenance_points.parent = self
            self.mep_configuration_errors = Cfm.Global.MepConfigurationErrors()
            self.mep_configuration_errors.parent = self
            self.peer_meps = Cfm.Global.PeerMeps()
            self.peer_meps.parent = self
            self.traceroute_caches = Cfm.Global.TracerouteCaches()
            self.traceroute_caches.parent = self


        class GlobalConfigurationErrors(object):
            """
            Global configuration errors table
            
            .. attribute:: global_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of :py:class:`GlobalConfigurationError <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: bridge_domain_id
                
                	BD/XC ID, or Service name if the Service is 'down\-only'
                	**type**\: :py:class:`BridgeDomainId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId>`
                
                .. attribute:: bridge_domain_is_configured
                
                	The BD/XC is configured globally
                	**type**\: bool
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                .. attribute:: l2_fib_download_error
                
                	The BD/XC could not be downloaded to L2FIB
                	**type**\: bool
                
                .. attribute:: level
                
                	Level
                	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: service_name
                
                	Service name
                	**type**\: str
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.service = None
                    self.bridge_domain_id = Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId()
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
                    	**type**\: :py:class:`CfmBagBdidFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:bridge-domain-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-errors/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-error[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:global-configuration-errors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.global_configuration_error is not None:
                    for child_ref in self.global_configuration_error:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.GlobalConfigurationErrors']['meta_info']


        class IncompleteTraceroutes(object):
            """
            Incomplete Traceroute table
            
            .. attribute:: incomplete_traceroute
            
            	Information about a traceroute operation that has not yet timed out
            	**type**\: list of :py:class:`IncompleteTraceroute <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: transaction_id
                
                	Transaction ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: time_left
                
                	Time (in seconds) before the traceroute completes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\: :py:class:`TracerouteInformation <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.mep_id = None
                    self.service = None
                    self.transaction_id = None
                    self.time_left = None
                    self.traceroute_information = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation()
                    self.traceroute_information.parent = self


                class TracerouteInformation(object):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\: :py:class:`Options <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options>`
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
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
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.directed_mac_address = None
                        self.domain = None
                        self.level = None
                        self.options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options()
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
                        	**type**\: :py:class:`BasicOptions <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\: :py:class:`ExploratoryOptions <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\: :py:class:`CfmPmLtModeEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtModeEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.basic_options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self.exploratory_options = Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self.mode = None


                        class BasicOptions(object):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\: bool
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\: bool
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:basic-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.fdb_only is not None:
                                    return True

                                if self.is_auto is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions']['meta_info']


                        class ExploratoryOptions(object):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\: :py:class:`CfmPmEltDelayModelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\: :py:class:`CfmPmElmReplyFilterEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilterEnum>`
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.delay_constant_factor is not None:
                                    return True

                                if self.delay_model is not None:
                                    return True

                                if self.reply_filter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.basic_options is not None and self.basic_options._has_data():
                                return True

                            if self.exploratory_options is not None and self.exploratory_options._has_data():
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.mep_id is None:
                        raise YPYDataValidationError('Key property mep_id is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')
                    if self.transaction_id is None:
                        raise YPYDataValidationError('Key property transaction_id is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroutes/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroute[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:transaction-id = ' + str(self.transaction_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.service is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:incomplete-traceroutes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.incomplete_traceroute is not None:
                    for child_ref in self.incomplete_traceroute:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.IncompleteTraceroutes']['meta_info']


        class LocalMeps(object):
            """
            Local MEPs table
            
            .. attribute:: local_mep
            
            	Information about a particular local MEP
            	**type**\: list of :py:class:`LocalMep <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: ais_statistics
                
                	MEP AIS statistics
                	**type**\: :py:class:`AisStatistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics>`
                
                .. attribute:: ccm_generation_enabled
                
                	CCM generation enabled
                	**type**\: bool
                
                .. attribute:: ccm_interval
                
                	The interval between CCMs
                	**type**\: :py:class:`CfmBagCcmIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                
                .. attribute:: ccm_offload
                
                	Offload status of CCM processing
                	**type**\: :py:class:`CfmBagCcmOffloadEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffloadEnum>`
                
                .. attribute:: cos
                
                	CoS bits the MEP will use for sent packets, if configured
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: cross_connect_ccm_defect
                
                	A cross\-connect CCM error has been reported
                	**type**\: bool
                
                .. attribute:: defects
                
                	Defects detected from peer MEPs
                	**type**\: :py:class:`Defects <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Defects>`
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\: str
                
                .. attribute:: efd_triggered
                
                	EFD triggered on the interface
                	**type**\: bool
                
                .. attribute:: error_ccm_defect
                
                	A CCM error has been reported
                	**type**\: bool
                
                .. attribute:: fault_notification_state
                
                	Fault Notification Generation state
                	**type**\: :py:class:`CfmPmMepFngStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepFngStateEnum>`
                
                .. attribute:: highest_defect
                
                	Highest\-priority defect present since last FNG reset
                	**type**\: :py:class:`CfmPmMepDefectEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmMepDefectEnum>`
                
                .. attribute:: interface_state
                
                	IM Interface state
                	**type**\: str
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interworking_state
                
                	Interface interworking state
                	**type**\: :py:class:`CfmBagIwStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwStateEnum>`
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mac_status_defect
                
                	A peer MEP port or interface status error has been reported
                	**type**\: bool
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\: :py:class:`CfmBagDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                
                .. attribute:: mep_id_xr
                
                	MEP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: next_lbm_id
                
                	Next Transaction ID to be sent in a Loopback Message
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_ltm_id
                
                	Next Transaction ID to be sent in a Linktrace Message
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_mep_ccm_defect
                
                	A peer MEP CCM error has been reported
                	**type**\: bool
                
                .. attribute:: peer_meps_detected
                
                	Number of peer MEPs detected
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_with_errors_detected
                
                	Number of peer MEPs detected with errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rdi_defect
                
                	A peer MEP RDI defect has been reported
                	**type**\: bool
                
                .. attribute:: remote_defect
                
                	Remote defect indicated
                	**type**\: bool
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\: str
                
                .. attribute:: standby
                
                	The MEP is on a standby bundle interface
                	**type**\: bool
                
                .. attribute:: statistics
                
                	MEP statistics
                	**type**\: :py:class:`Statistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Statistics>`
                
                .. attribute:: stp_state
                
                	STP state
                	**type**\: :py:class:`CfmBagStpStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpStateEnum>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.mep_id = None
                    self.service = None
                    self.ais_statistics = Cfm.Global.LocalMeps.LocalMep.AisStatistics()
                    self.ais_statistics.parent = self
                    self.ccm_generation_enabled = None
                    self.ccm_interval = None
                    self.ccm_offload = None
                    self.cos = None
                    self.cross_connect_ccm_defect = None
                    self.defects = Cfm.Global.LocalMeps.LocalMep.Defects()
                    self.defects.parent = self
                    self.domain_xr = None
                    self.efd_triggered = None
                    self.error_ccm_defect = None
                    self.fault_notification_state = None
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
                    self.statistics = Cfm.Global.LocalMeps.LocalMep.Statistics()
                    self.statistics.parent = self
                    self.stp_state = None


                class AisStatistics(object):
                    """
                    MEP AIS statistics
                    
                    .. attribute:: interval
                    
                    	AIS transmission interval
                    	**type**\: :py:class:`CfmBagAisIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                    
                    .. attribute:: last_interval
                    
                    	The interval of the last received AIS packet
                    	**type**\: :py:class:`CfmBagAisIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                    
                    .. attribute:: last_mac_address
                    
                    	Source MAC address of the last received AIS packet
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: level
                    
                    	AIS transmission level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: receiving_ais
                    
                    	Details of how the signal is being received
                    	**type**\: :py:class:`CfmPmAisReceiveEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisReceiveEnum>`
                    
                    .. attribute:: receiving_start
                    
                    	Time elapsed since AIS receiving started
                    	**type**\: :py:class:`ReceivingStart <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart>`
                    
                    .. attribute:: sending_ais
                    
                    	Details of how AIS is being transmitted
                    	**type**\: :py:class:`CfmPmAisTransmitEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAisTransmitEnum>`
                    
                    .. attribute:: sending_start
                    
                    	Time elapsed since AIS sending started
                    	**type**\: :py:class:`SendingStart <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart>`
                    
                    

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
                        self.receiving_start = Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart()
                        self.receiving_start.parent = self
                        self.sending_ais = None
                        self.sending_start = Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart()
                        self.sending_start.parent = self


                    class ReceivingStart(object):
                        """
                        Time elapsed since AIS receiving started
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:receiving-start'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart']['meta_info']


                    class SendingStart(object):
                        """
                        Time elapsed since AIS sending started
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sending-start'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ais-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics']['meta_info']


                class Defects(object):
                    """
                    Defects detected from peer MEPs
                    
                    .. attribute:: ais_received
                    
                    	AIS or LCK received
                    	**type**\: bool
                    
                    .. attribute:: auto_missing
                    
                    	Number of missing auto cross\-check MEPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_port_status
                    
                    	The local port or interface is down
                    	**type**\: bool
                    
                    .. attribute:: missing
                    
                    	Number of missing peer MEPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_meps_that_timed_out
                    
                    	Number of peer MEPs that have timed out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_port_status
                    
                    	A peer port or interface is down
                    	**type**\: bool
                    
                    .. attribute:: remote_meps_defects
                    
                    	Defects detected from remote MEPs
                    	**type**\: :py:class:`RemoteMepsDefects <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects>`
                    
                    .. attribute:: unexpected
                    
                    	Number of unexpected peer MEPs
                    	**type**\: int
                    
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
                        self.remote_meps_defects = Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects()
                        self.remote_meps_defects.parent = self
                        self.unexpected = None


                    class RemoteMepsDefects(object):
                        """
                        Defects detected from remote MEPs
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\: bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\: bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\: bool
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:remote-meps-defects'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:defects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.Defects']['meta_info']


                class Statistics(object):
                    """
                    MEP statistics
                    
                    .. attribute:: ai_ss_received
                    
                    	Number of AIS messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ai_ss_sent
                    
                    	Number of AIS messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_discarded
                    
                    	Number of BNM messages discarded
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bn_ms_received
                    
                    	Number of BNM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_discarded
                    
                    	Number of CCMs discarded because maximum MEPs limit was reached
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_out_of_sequence
                    
                    	Number of CCMs received out\-of\-sequence
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_received
                    
                    	Number of CCMs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ccms_sent
                    
                    	Number of CCMs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_received
                    
                    	Number of DMM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_ms_sent
                    
                    	Number of DMM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_received
                    
                    	Number of DMR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dm_rs_sent
                    
                    	Number of DMR messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_received
                    
                    	Number of LBMs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_ms_sent
                    
                    	Number of LBMs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_bad_data
                    
                    	Number of LBRs received with non\-matching user\-specified data
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_out_of_sequence
                    
                    	Number of LBRs received out\-of\-sequence
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_received
                    
                    	Number of LBRs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lb_rs_sent
                    
                    	Number of LBRs sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lc_ks_received
                    
                    	Number of LCK messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_received
                    
                    	Number of LMM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_ms_sent
                    
                    	Number of LMM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_received
                    
                    	Number of LMR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lm_rs_sent
                    
                    	Number of LMR messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: lt_rs_received_unexpected
                    
                    	Number of unexpected LTRs received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_received
                    
                    	Number of SLM messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_ms_sent
                    
                    	Number of SLM messages sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_received
                    
                    	Number of SLR messages received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sl_rs_sent
                    
                    	Number of SLR messages sent
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.LocalMeps.LocalMep.Statistics']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.mep_id is None:
                        raise YPYDataValidationError('Key property mep_id is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:local-meps/Cisco-IOS-XR-ethernet-cfm-oper:local-mep[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.service is not None:
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

                    if self.domain_xr is not None:
                        return True

                    if self.efd_triggered is not None:
                        return True

                    if self.error_ccm_defect is not None:
                        return True

                    if self.fault_notification_state is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.LocalMeps.LocalMep']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:local-meps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.local_mep is not None:
                    for child_ref in self.local_mep:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.LocalMeps']['meta_info']


        class MaintenancePoints(object):
            """
            Maintenance Points table
            
            .. attribute:: maintenance_point
            
            	Information about a particular Maintenance Point
            	**type**\: list of :py:class:`MaintenancePoint <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints.MaintenancePoint>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: maintenance_point
                
                	Maintenance Point
                	**type**\: :py:class:`MaintenancePoint <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint>`
                
                .. attribute:: mep_has_error
                
                	MEP error flag
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.service = None
                    self.mac_address = None
                    self.maintenance_point = Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint()
                    self.maintenance_point.parent = self
                    self.mep_has_error = None


                class MaintenancePoint(object):
                    """
                    Maintenance Point
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\: :py:class:`CfmMaMpVarietyEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVarietyEnum>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\: str
                    
                    

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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-point'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-points/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-point[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.service is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.MaintenancePoints.MaintenancePoint']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:maintenance-points'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.maintenance_point is not None:
                    for child_ref in self.maintenance_point:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.MaintenancePoints']['meta_info']


        class MepConfigurationErrors(object):
            """
            MEP configuration errors table
            
            .. attribute:: mep_configuration_error
            
            	Information about a particular configuration error
            	**type**\: list of :py:class:`MepConfigurationError <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: ais_configured
                
                	AIS is configured on the same interface as the down MEP
                	**type**\: bool
                
                .. attribute:: bridge_domain_mismatch
                
                	The MEP's EFP is not in the Service's Bridge Domain
                	**type**\: bool
                
                .. attribute:: bridge_domain_not_in_bd_infra
                
                	A BD/XC specified in the MEG config, but it does not exist globally
                	**type**\: bool
                
                .. attribute:: bundle_level0
                
                	The MEP is configured in a domain at level 0, on a bundle interface or sub\-interface.  This is not supported
                	**type**\: bool
                
                .. attribute:: ccm_interval
                
                	Interval between CCMs sent on this MEP
                	**type**\: :py:class:`CfmBagCcmIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                
                .. attribute:: ccm_interval_not_supported
                
                	CCM Interval is less than minimum interval supported by hardware
                	**type**\: bool
                
                .. attribute:: interface_bridge_domain
                
                	ID of the BD/XC that the MEP's EFP is in, if any
                	**type**\: :py:class:`InterfaceBridgeDomain <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain>`
                
                .. attribute:: level_conflict
                
                	Another MEP facing in the same direction is at the same Maintenance Level
                	**type**\: bool
                
                .. attribute:: mep
                
                	The MEP that has errors
                	**type**\: :py:class:`Mep <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep>`
                
                .. attribute:: no_domain
                
                	The MEP's Domain is not configured
                	**type**\: bool
                
                .. attribute:: no_interface_type
                
                	We haven't yet been able to look up the interface type to find whether the interface is a bundle
                	**type**\: bool
                
                .. attribute:: no_mlacp
                
                	The EFP is a bundle and the mLACP mode is not yet known
                	**type**\: bool
                
                .. attribute:: no_service
                
                	The MEP's Service is not configured
                	**type**\: bool
                
                .. attribute:: no_valid_mac_address
                
                	The EFP doesn't have a valid MAC address yet. This will also get set if the MAC address we have is a multicast address
                	**type**\: bool
                
                .. attribute:: not_in_im
                
                	The EFP has been deleted from IM
                	**type**\: bool
                
                .. attribute:: offload_mep_direction_not_supported
                
                	The MEP direction does not support offload
                	**type**\: bool
                
                .. attribute:: offload_multiple_local_mep
                
                	Multiple offloaded MEPs on the same interface are not supported
                	**type**\: bool
                
                .. attribute:: offload_multiple_peer_meps
                
                	The MEP should be offloaded but multiple crosscheck MEPs have been configured, and this is not supported
                	**type**\: bool
                
                .. attribute:: offload_no_cross_check
                
                	The MEP should be offloaded but crosscheck has not been configured
                	**type**\: bool
                
                .. attribute:: offload_out_of_resources
                
                	Offload resource limits have been exceeded
                	**type**\: bool
                
                .. attribute:: satellite_capabilities
                
                	Satellite Capabilities
                	**type**\: :py:class:`SatelliteCapabilities <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities>`
                
                .. attribute:: satellite_error_string
                
                	Error string returned from satellite
                	**type**\: str
                
                .. attribute:: satellite_id
                
                	ID of the satellite
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: satellite_limitation
                
                	A satellite limitation is preventing MEP being offloaded to satellite
                	**type**\: bool
                
                .. attribute:: service_bridge_domain
                
                	BD/XC ID for the MEP's Service, or Service name if the Service is 'down\-only'
                	**type**\: :py:class:`ServiceBridgeDomain <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain>`
                
                .. attribute:: sla_delay_measurement_operations_disabled
                
                	In\-progress Ethernet SLA delay measurement operations are disabled due to satellite having delay measurement responder\-only capabilities
                	**type**\: bool
                
                .. attribute:: sla_loopback_operations_disabled
                
                	In\-progress Ethernet SLA loopback operations are disabled due to satellite having loopback responder\-only capabilities
                	**type**\: bool
                
                .. attribute:: sla_synthetic_loss_operations_disabled
                
                	In\-progress Ethernet SLA synthetic loss measurement operations are disabled due to satellite having synthetic loss measurement responder\-only capabilities
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.service = None
                    self.ais_configured = None
                    self.bridge_domain_mismatch = None
                    self.bridge_domain_not_in_bd_infra = None
                    self.bundle_level0 = None
                    self.ccm_interval = None
                    self.ccm_interval_not_supported = None
                    self.interface_bridge_domain = Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain()
                    self.interface_bridge_domain.parent = self
                    self.level_conflict = None
                    self.mep = Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep()
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
                    self.satellite_capabilities = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities()
                    self.satellite_capabilities.parent = self
                    self.satellite_error_string = None
                    self.satellite_id = None
                    self.satellite_limitation = None
                    self.service_bridge_domain = Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain()
                    self.service_bridge_domain.parent = self
                    self.sla_delay_measurement_operations_disabled = None
                    self.sla_loopback_operations_disabled = None
                    self.sla_synthetic_loss_operations_disabled = None


                class InterfaceBridgeDomain(object):
                    """
                    ID of the BD/XC that the MEP's EFP is in, if any
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\: :py:class:`CfmBagBdidFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-bridge-domain'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain']['meta_info']


                class Mep(object):
                    """
                    The MEP that has errors
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: level
                    
                    	Domain level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: maintenance_point_type
                    
                    	Type of Maintenance Point
                    	**type**\: :py:class:`CfmMaMpVarietyEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmMaMpVarietyEnum>`
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: service_name
                    
                    	Service name
                    	**type**\: str
                    
                    

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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep']['meta_info']


                class SatelliteCapabilities(object):
                    """
                    Satellite Capabilities
                    
                    .. attribute:: delay_measurement
                    
                    	Delay Measurement
                    	**type**\: :py:class:`DelayMeasurement <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement>`
                    
                    .. attribute:: loopback
                    
                    	Loopback
                    	**type**\: :py:class:`Loopback <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback>`
                    
                    .. attribute:: synthetic_loss_measurement
                    
                    	Synthetic Loss Measurement
                    	**type**\: :py:class:`SyntheticLossMeasurement <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.delay_measurement = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement()
                        self.delay_measurement.parent = self
                        self.loopback = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback()
                        self.loopback.parent = self
                        self.synthetic_loss_measurement = Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement()
                        self.synthetic_loss_measurement.parent = self


                    class DelayMeasurement(object):
                        """
                        Delay Measurement
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:delay-measurement'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement']['meta_info']


                    class Loopback(object):
                        """
                        Loopback
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:loopback'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback']['meta_info']


                    class SyntheticLossMeasurement(object):
                        """
                        Synthetic Loss Measurement
                        
                        .. attribute:: controller
                        
                        	Controller
                        	**type**\: bool
                        
                        .. attribute:: responder
                        
                        	Responder
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:synthetic-loss-measurement'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.controller is not None:
                                return True

                            if self.responder is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:satellite-capabilities'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.delay_measurement is not None and self.delay_measurement._has_data():
                            return True

                        if self.loopback is not None and self.loopback._has_data():
                            return True

                        if self.synthetic_loss_measurement is not None and self.synthetic_loss_measurement._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']


                class ServiceBridgeDomain(object):
                    """
                    BD/XC ID for the MEP's Service, or Service name
                    if the Service is 'down\-only'
                    
                    .. attribute:: bridge_domain_id_format
                    
                    	Bridge domain identifier format
                    	**type**\: :py:class:`CfmBagBdidFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagBdidFmtEnum>`
                    
                    .. attribute:: ce_id
                    
                    	Local Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: group
                    
                    	Name of the Bridge/XConnect Group
                    	**type**\: str
                    
                    .. attribute:: name
                    
                    	Name of the Bridge Domain/XConnect
                    	**type**\: str
                    
                    .. attribute:: remote_ce_id
                    
                    	Remote Customer Edge Identifier (CE\-ID)
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:service-bridge-domain'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-errors/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-error[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.service is not None:
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

                    if self.interface_bridge_domain is not None and self.interface_bridge_domain._has_data():
                        return True

                    if self.level_conflict is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:mep-configuration-errors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.mep_configuration_error is not None:
                    for child_ref in self.mep_configuration_error:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.MepConfigurationErrors']['meta_info']


        class PeerMeps(object):
            """
            Peer MEPs table
            
            .. attribute:: peer_mep
            
            	Information about a peer MEP for a particular local MEP
            	**type**\: list of :py:class:`PeerMep <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep>`
            
            

            """

            _prefix = 'ethernet-cfm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.peer_mep = YList()
                self.peer_mep.parent = self
                self.peer_mep.name = 'peer_mep'


            class PeerMep(object):
                """
                Information about a peer MEP for a particular
                local MEP
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: local_mep_id
                
                	MEP ID of Local MEP
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: peer_mac_address
                
                	Peer MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: peer_mep_id
                
                	MEP ID of Peer MEP
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: domain_xr
                
                	Maintenance domain name
                	**type**\: str
                
                .. attribute:: interface_xr
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: level
                
                	Maintenance level
                	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                
                .. attribute:: mep_direction
                
                	MEP facing direction
                	**type**\: :py:class:`CfmBagDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: peer_mep
                
                	Peer MEP
                	**type**\: :py:class:`PeerMep <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep>`
                
                .. attribute:: service_xr
                
                	Service name
                	**type**\: str
                
                .. attribute:: standby
                
                	The local MEP is on a standby bundle interface
                	**type**\: bool
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.local_mep_id = None
                    self.peer_mac_address = None
                    self.peer_mep_id = None
                    self.service = None
                    self.domain_xr = None
                    self.interface_xr = None
                    self.level = None
                    self.mep_direction = None
                    self.mep_id = None
                    self.peer_mep = Cfm.Global.PeerMeps.PeerMep.PeerMep()
                    self.peer_mep.parent = self
                    self.service_xr = None
                    self.standby = None


                class PeerMep(object):
                    """
                    Peer MEP
                    
                    .. attribute:: ccm_offload
                    
                    	Offload status of received CCM handling
                    	**type**\: :py:class:`CfmBagCcmOffloadEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmOffloadEnum>`
                    
                    .. attribute:: cross_check_state
                    
                    	Cross\-check state
                    	**type**\: :py:class:`CfmPmRmepXcStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepXcStateEnum>`
                    
                    .. attribute:: error_state
                    
                    	Error state
                    	**type**\: :py:class:`ErrorState <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState>`
                    
                    .. attribute:: last_ccm_received
                    
                    	Last CCM received from the peer MEP
                    	**type**\: :py:class:`LastCcmReceived <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived>`
                    
                    .. attribute:: last_up_down_time
                    
                    	Elapsed time since peer MEP became active or timed out
                    	**type**\: :py:class:`LastUpDownTime <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime>`
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id
                    
                    	MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: peer_mep_state
                    
                    	State of the peer MEP state machine
                    	**type**\: :py:class:`CfmPmRmepStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRmepStateEnum>`
                    
                    .. attribute:: statistics
                    
                    	Peer MEP statistics
                    	**type**\: :py:class:`Statistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ccm_offload = None
                        self.cross_check_state = None
                        self.error_state = Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState()
                        self.error_state.parent = self
                        self.last_ccm_received = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived()
                        self.last_ccm_received.parent = self
                        self.last_up_down_time = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime()
                        self.last_up_down_time.parent = self
                        self.mac_address = None
                        self.mep_id = None
                        self.peer_mep_state = None
                        self.statistics = Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics()
                        self.statistics.parent = self


                    class ErrorState(object):
                        """
                        Error state
                        
                        .. attribute:: invalid_ccm_interval
                        
                        	Invalid CCM interval
                        	**type**\: bool
                        
                        .. attribute:: invalid_level
                        
                        	Invalid level
                        	**type**\: bool
                        
                        .. attribute:: invalid_maid
                        
                        	Invalid MAID
                        	**type**\: bool
                        
                        .. attribute:: loss_threshold_exceeded
                        
                        	Timed out (loss threshold exceeded)
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:error-state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState']['meta_info']


                    class LastCcmReceived(object):
                        """
                        Last CCM received from the peer MEP
                        
                        .. attribute:: additional_interface_status
                        
                        	Additional interface status
                        	**type**\: :py:class:`CfmPmAddlIntfStatusEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmAddlIntfStatusEnum>`
                        
                        .. attribute:: header
                        
                        	Frame header
                        	**type**\: :py:class:`Header <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header>`
                        
                        .. attribute:: interface_status
                        
                        	Interface status
                        	**type**\: :py:class:`CfmPmIntfStatusEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIntfStatusEnum>`
                        
                        .. attribute:: mep_name
                        
                        	MEP name
                        	**type**\: :py:class:`MepName <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName>`
                        
                        .. attribute:: organization_specific_tlv
                        
                        	Organizational\-specific TLVs
                        	**type**\: list of :py:class:`OrganizationSpecificTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv>`
                        
                        .. attribute:: port_status
                        
                        	Port status
                        	**type**\: :py:class:`CfmPmPortStatusEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortStatusEnum>`
                        
                        .. attribute:: raw_data
                        
                        	Undecoded frame
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: sender_id
                        
                        	Sender ID TLV
                        	**type**\: :py:class:`SenderId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId>`
                        
                        .. attribute:: unknown_tlv
                        
                        	Unknown TLVs
                        	**type**\: list of :py:class:`UnknownTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.additional_interface_status = None
                            self.header = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header()
                            self.header.parent = self
                            self.interface_status = None
                            self.mep_name = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName()
                            self.mep_name.parent = self
                            self.organization_specific_tlv = YList()
                            self.organization_specific_tlv.parent = self
                            self.organization_specific_tlv.name = 'organization_specific_tlv'
                            self.port_status = None
                            self.raw_data = None
                            self.sender_id = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId()
                            self.sender_id.parent = self
                            self.unknown_tlv = YList()
                            self.unknown_tlv.parent = self
                            self.unknown_tlv.name = 'unknown_tlv'


                        class Header(object):
                            """
                            Frame header
                            
                            .. attribute:: interval
                            
                            	CCM interval
                            	**type**\: :py:class:`CfmBagCcmIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagCcmIntervalEnum>`
                            
                            .. attribute:: level
                            
                            	MD level
                            	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                            
                            .. attribute:: mdid
                            
                            	MDID
                            	**type**\: :py:class:`Mdid <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid>`
                            
                            .. attribute:: mdid_format
                            
                            	MDID Format
                            	**type**\: :py:class:`CfmBagMdidFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdidFmtEnum>`
                            
                            .. attribute:: mep_id
                            
                            	MEP ID
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: rdi
                            
                            	Remote defect indicated
                            	**type**\: bool
                            
                            .. attribute:: sequence_number
                            
                            	CCM sequence number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: short_ma_name
                            
                            	Short MA Name
                            	**type**\: :py:class:`ShortMaName <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName>`
                            
                            .. attribute:: short_ma_name_format
                            
                            	Short MA Name format
                            	**type**\: :py:class:`CfmBagSmanFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagSmanFmtEnum>`
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interval = None
                                self.level = None
                                self.mdid = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid()
                                self.mdid.parent = self
                                self.mdid_format = None
                                self.mep_id = None
                                self.rdi = None
                                self.sequence_number = None
                                self.short_ma_name = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName()
                                self.short_ma_name.parent = self
                                self.short_ma_name_format = None
                                self.version = None


                            class Mdid(object):
                                """
                                MDID
                                
                                .. attribute:: dns_like_name
                                
                                	DNS\-like name
                                	**type**\: str
                                
                                .. attribute:: mac_name
                                
                                	MAC address name
                                	**type**\: :py:class:`MacName <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName>`
                                
                                .. attribute:: mdid_data
                                
                                	Hex data
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: mdid_format_value
                                
                                	MDIDFormatValue
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dns_like_name = None
                                    self.mac_name = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName()
                                    self.mac_name.parent = self
                                    self.mdid_data = None
                                    self.mdid_format_value = None
                                    self.string_name = None


                                class MacName(object):
                                    """
                                    MAC address name
                                    
                                    .. attribute:: integer
                                    
                                    	Integer
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
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
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mac-name'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.integer is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mdid'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid']['meta_info']


                            class ShortMaName(object):
                                """
                                Short MA Name
                                
                                .. attribute:: icc_based
                                
                                	ICC\-based format
                                	**type**\: str
                                
                                .. attribute:: integer_name
                                
                                	Unsigned integer name
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: short_ma_name_data
                                
                                	Hex data
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: short_ma_name_format_value
                                
                                	ShortMANameFormatValue
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: string_name
                                
                                	String name
                                	**type**\: str
                                
                                .. attribute:: vlan_id_name
                                
                                	VLAN ID name
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: vpn_id_name
                                
                                	VPN ID name
                                	**type**\: :py:class:`VpnIdName <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName>`
                                
                                

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
                                    self.vpn_id_name = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName()
                                    self.vpn_id_name.parent = self


                                class VpnIdName(object):
                                    """
                                    VPN ID name
                                    
                                    .. attribute:: index
                                    
                                    	VPN index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: oui
                                    
                                    	VPN authority organizationally\-unique ID
                                    	**type**\: int
                                    
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
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:vpn-id-name'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.index is not None:
                                            return True

                                        if self.oui is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:short-ma-name'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header']['meta_info']


                        class MepName(object):
                            """
                            MEP name
                            
                            .. attribute:: name
                            
                            	MEP name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:mep-name'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName']['meta_info']


                        class OrganizationSpecificTlv(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.oui = None
                                self.subtype = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.oui is not None:
                                    return True

                                if self.subtype is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv']['meta_info']


                        class SenderId(object):
                            """
                            Sender ID TLV
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID
                            	**type**\: :py:class:`ChassisId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId>`
                            
                            .. attribute:: management_address
                            
                            	Management address
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: management_address_domain
                            
                            	Management address domain
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId()
                                self.chassis_id.parent = self
                                self.management_address = None
                                self.management_address_domain = None


                            class ChassisId(object):
                                """
                                Chassis ID
                                
                                .. attribute:: chassis_id
                                
                                	Chassis ID (Deprecated)
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_type
                                
                                	Chassis ID Type
                                	**type**\: :py:class:`CfmPmChassisIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                                
                                .. attribute:: chassis_id_type_value
                                
                                	Chassis ID Type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: chassis_id_value
                                
                                	Chassis ID (Current)
                                	**type**\: :py:class:`ChassisIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue>`
                                
                                

                                """

                                _prefix = 'ethernet-cfm-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.chassis_id = None
                                    self.chassis_id_type = None
                                    self.chassis_id_type_value = None
                                    self.chassis_id_value = Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue()
                                    self.chassis_id_value.parent = self


                                class ChassisIdValue(object):
                                    """
                                    Chassis ID (Current)
                                    
                                    .. attribute:: chassis_id_format
                                    
                                    	ChassisIDFormat
                                    	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                    
                                    .. attribute:: chassis_id_mac
                                    
                                    	Chassis ID MAC Address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: chassis_id_raw
                                    
                                    	Raw Chassis ID
                                    	**type**\: str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    .. attribute:: chassis_id_string
                                    
                                    	Chassis ID String
                                    	**type**\: str
                                    
                                    

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
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
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
                                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                        return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.chassis_id is not None and self.chassis_id._has_data():
                                    return True

                                if self.management_address is not None:
                                    return True

                                if self.management_address_domain is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId']['meta_info']


                        class UnknownTlv(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.typecode = None
                                self.value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.typecode is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-ccm-received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']


                    class LastUpDownTime(object):
                        """
                        Elapsed time since peer MEP became active or
                        timed out
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-up-down-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nanoseconds is not None:
                                return True

                            if self.seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime']['meta_info']


                    class Statistics(object):
                        """
                        Peer MEP statistics
                        
                        .. attribute:: ccms_invalid_interval
                        
                        	Number of CCMs received with an invalid interval
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_invalid_maid
                        
                        	Number of CCMs received with an invalid MAID
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
                        
                        .. attribute:: ccms_out_of_sequence
                        
                        	Number of CCMs received out\-of\-sequence
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_rdi
                        
                        	Number of CCMs received with the Remote Defect Indication bit set
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_received
                        
                        	Number of CCMs received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: ccms_wrong_level
                        
                        	Number of CCMs received with an invalid level
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_ccm_received_time
                        
                        	Elapsed time since last CCM received
                        	**type**\: :py:class:`LastCcmReceivedTime <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime>`
                        
                        .. attribute:: last_ccm_sequence_number
                        
                        	Sequence number of last CCM received
                        	**type**\: int
                        
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
                            self.last_ccm_received_time = Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime()
                            self.last_ccm_received_time.parent = self
                            self.last_ccm_sequence_number = None


                        class LastCcmReceivedTime(object):
                            """
                            Elapsed time since last CCM received
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-ccm-received-time'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.nanoseconds is not None:
                                    return True

                                if self.seconds is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:peer-mep'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.local_mep_id is None:
                        raise YPYDataValidationError('Key property local_mep_id is None')
                    if self.peer_mac_address is None:
                        raise YPYDataValidationError('Key property peer_mac_address is None')
                    if self.peer_mep_id is None:
                        raise YPYDataValidationError('Key property peer_mep_id is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:peer-meps/Cisco-IOS-XR-ethernet-cfm-oper:peer-mep[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:local-mep-id = ' + str(self.local_mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:peer-mac-address = ' + str(self.peer_mac_address) + '][Cisco-IOS-XR-ethernet-cfm-oper:peer-mep-id = ' + str(self.peer_mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.local_mep_id is not None:
                        return True

                    if self.peer_mac_address is not None:
                        return True

                    if self.peer_mep_id is not None:
                        return True

                    if self.service is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.PeerMeps.PeerMep']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:peer-meps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.peer_mep is not None:
                    for child_ref in self.peer_mep:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.PeerMeps']['meta_info']


        class TracerouteCaches(object):
            """
            Traceroute Cache table
            
            .. attribute:: traceroute_cache
            
            	Information about a particular traceroute operation
            	**type**\: list of :py:class:`TracerouteCache <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache>`
            
            

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
                
                .. attribute:: domain
                
                	Maintenance Domain
                	**type**\: str
                
                .. attribute:: interface
                
                	Interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: mep_id
                
                	MEP ID
                	**type**\: int
                
                	**range:** 1..8191
                
                .. attribute:: service
                
                	Service (Maintenance Association)
                	**type**\: str
                
                .. attribute:: transaction_id
                
                	Transaction ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: exploratory_linktrace_reply
                
                	Received exploratory linktrace replies
                	**type**\: list of :py:class:`ExploratoryLinktraceReply <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply>`
                
                .. attribute:: linktrace_reply
                
                	Received linktrace replies
                	**type**\: list of :py:class:`LinktraceReply <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply>`
                
                .. attribute:: replies_dropped
                
                	Count of ignored replies for this request
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: traceroute_information
                
                	Information about the traceroute operation
                	**type**\: :py:class:`TracerouteInformation <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation>`
                
                

                """

                _prefix = 'ethernet-cfm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain = None
                    self.interface = None
                    self.mep_id = None
                    self.service = None
                    self.transaction_id = None
                    self.exploratory_linktrace_reply = YList()
                    self.exploratory_linktrace_reply.parent = self
                    self.exploratory_linktrace_reply.name = 'exploratory_linktrace_reply'
                    self.linktrace_reply = YList()
                    self.linktrace_reply.parent = self
                    self.linktrace_reply.name = 'linktrace_reply'
                    self.replies_dropped = None
                    self.traceroute_information = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation()
                    self.traceroute_information.parent = self


                class ExploratoryLinktraceReply(object):
                    """
                    Received exploratory linktrace replies
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\: :py:class:`Header <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\: :py:class:`LastHop <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop>`
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of :py:class:`OrganizationSpecificTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\: :py:class:`ReplyEgress <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\: :py:class:`ReplyIngress <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\: :py:class:`SenderId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of :py:class:`UnknownTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.header = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header()
                        self.header.parent = self
                        self.last_hop = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self.organization_specific_tlv = YList()
                        self.organization_specific_tlv.parent = self
                        self.organization_specific_tlv.name = 'organization_specific_tlv'
                        self.raw_data = None
                        self.reply_egress = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self.reply_ingress = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self.sender_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self.unknown_tlv = YList()
                        self.unknown_tlv.parent = self
                        self.unknown_tlv.name = 'unknown_tlv'


                    class Header(object):
                        """
                        Frame header
                        
                        .. attribute:: delay_model
                        
                        	Delay Model
                        	**type**\: :py:class:`CfmPmEltDelayModelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                        
                        .. attribute:: forwarded
                        
                        	ELR was forwarded
                        	**type**\: bool
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: next_hop_timeout
                        
                        	Next Hop Timeout, in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\: :py:class:`CfmPmElrRelayActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrRelayActionEnum>`
                        
                        .. attribute:: reply_filter_unknown
                        
                        	Reply Filter unrecognized
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
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: int
                        
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header']['meta_info']


                    class LastHop(object):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\: :py:class:`EgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\: str
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\: :py:class:`CfmPmLastHopFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmtEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self.host_name = None
                            self.last_hop_format = None


                        class EgressId(object):
                            """
                            Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.egress_id is not None and self.egress_id._has_data():
                                return True

                            if self.host_name is not None:
                                return True

                            if self.last_hop_format is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info']


                    class OrganizationSpecificTlv(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.oui = None
                            self.subtype = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.oui is not None:
                                return True

                            if self.subtype is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv']['meta_info']


                    class ReplyEgress(object):
                        """
                        Reply egress TLV
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\: :py:class:`CfmPmElrEgressActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrEgressActionEnum>`
                        
                        .. attribute:: last_egress_id
                        
                        	Last Egress ID
                        	**type**\: :py:class:`LastEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address of egress interface
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: next_egress_id
                        
                        	Next Egress ID
                        	**type**\: :py:class:`NextEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\: :py:class:`PortId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId()
                            self.last_egress_id.parent = self
                            self.mac_address = None
                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId()
                            self.next_egress_id.parent = self
                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self


                        class LastEgressId(object):
                            """
                            Last Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId']['meta_info']


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\: :py:class:`CfmPmPortIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\: :py:class:`PortIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-egress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']


                    class ReplyIngress(object):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: action
                        
                        	ELR Reply ingress action
                        	**type**\: :py:class:`CfmPmElrIngressActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElrIngressActionEnum>`
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\: :py:class:`LastEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\: :py:class:`NextEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId>`
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\: :py:class:`PortId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId()
                            self.last_egress_id.parent = self
                            self.mac_address = None
                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId()
                            self.next_egress_id.parent = self
                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self


                        class LastEgressId(object):
                            """
                            Last egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId']['meta_info']


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\: :py:class:`CfmPmPortIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\: :py:class:`PortIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-ingress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']


                    class SenderId(object):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\: :py:class:`ChassisId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.chassis_id = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self.management_address = None
                            self.management_address_domain = None


                        class ChassisId(object):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\: :py:class:`CfmPmChassisIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\: :py:class:`ChassisIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self


                            class ChassisIdValue(object):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.chassis_id is not None and self.chassis_id._has_data():
                                return True

                            if self.management_address is not None:
                                return True

                            if self.management_address_domain is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info']


                    class UnknownTlv(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.typecode = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.typecode is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-linktrace-reply'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']


                class LinktraceReply(object):
                    """
                    Received linktrace replies
                    
                    .. attribute:: egress_id
                    
                    	Egress ID TLV
                    	**type**\: :py:class:`EgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId>`
                    
                    .. attribute:: header
                    
                    	Frame header
                    	**type**\: :py:class:`Header <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header>`
                    
                    .. attribute:: last_hop
                    
                    	Last hop ID
                    	**type**\: :py:class:`LastHop <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop>`
                    
                    .. attribute:: organization_specific_tlv
                    
                    	Organizational\-specific TLVs
                    	**type**\: list of :py:class:`OrganizationSpecificTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv>`
                    
                    .. attribute:: raw_data
                    
                    	Undecoded frame
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: reply_egress
                    
                    	Reply egress TLV
                    	**type**\: :py:class:`ReplyEgress <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress>`
                    
                    .. attribute:: reply_ingress
                    
                    	Reply ingress TLV
                    	**type**\: :py:class:`ReplyIngress <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress>`
                    
                    .. attribute:: sender_id
                    
                    	Sender ID TLV
                    	**type**\: :py:class:`SenderId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId>`
                    
                    .. attribute:: unknown_tlv
                    
                    	Unknown TLVs
                    	**type**\: list of :py:class:`UnknownTlv <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId()
                        self.egress_id.parent = self
                        self.header = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header()
                        self.header.parent = self
                        self.last_hop = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop()
                        self.last_hop.parent = self
                        self.organization_specific_tlv = YList()
                        self.organization_specific_tlv.parent = self
                        self.organization_specific_tlv.name = 'organization_specific_tlv'
                        self.raw_data = None
                        self.reply_egress = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress()
                        self.reply_egress.parent = self
                        self.reply_ingress = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress()
                        self.reply_ingress.parent = self
                        self.sender_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId()
                        self.sender_id.parent = self
                        self.unknown_tlv = YList()
                        self.unknown_tlv.parent = self
                        self.unknown_tlv.name = 'unknown_tlv'


                    class EgressId(object):
                        """
                        Egress ID TLV
                        
                        .. attribute:: last_egress_id
                        
                        	Last egress ID
                        	**type**\: :py:class:`LastEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId>`
                        
                        .. attribute:: next_egress_id
                        
                        	Next egress ID
                        	**type**\: :py:class:`NextEgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.last_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId()
                            self.last_egress_id.parent = self
                            self.next_egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId()
                            self.next_egress_id.parent = self


                        class LastEgressId(object):
                            """
                            Last egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId']['meta_info']


                        class NextEgressId(object):
                            """
                            Next egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:next-egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.last_egress_id is not None and self.last_egress_id._has_data():
                                return True

                            if self.next_egress_id is not None and self.next_egress_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']


                    class Header(object):
                        """
                        Frame header
                        
                        .. attribute:: forwarded
                        
                        	LTR was forwarded
                        	**type**\: bool
                        
                        .. attribute:: level
                        
                        	MD level
                        	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: relay_action
                        
                        	Relay action
                        	**type**\: :py:class:`CfmPmRelayActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmRelayActionEnum>`
                        
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
                        
                        .. attribute:: use_fdb_only
                        
                        	Use filtering DB only
                        	**type**\: bool
                        
                        .. attribute:: version
                        
                        	Version
                        	**type**\: int
                        
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:header'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header']['meta_info']


                    class LastHop(object):
                        """
                        Last hop ID
                        
                        .. attribute:: egress_id
                        
                        	Egress ID
                        	**type**\: :py:class:`EgressId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId>`
                        
                        .. attribute:: host_name
                        
                        	Hostname
                        	**type**\: str
                        
                        .. attribute:: last_hop_format
                        
                        	LastHopFormat
                        	**type**\: :py:class:`CfmPmLastHopFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLastHopFmtEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.egress_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId()
                            self.egress_id.parent = self
                            self.host_name = None
                            self.last_hop_format = None


                        class EgressId(object):
                            """
                            Egress ID
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: unique_id
                            
                            	Unique ID
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:egress-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac_address is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.egress_id is not None and self.egress_id._has_data():
                                return True

                            if self.host_name is not None:
                                return True

                            if self.last_hop_format is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info']


                    class OrganizationSpecificTlv(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.oui = None
                            self.subtype = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:organization-specific-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.oui is not None:
                                return True

                            if self.subtype is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv']['meta_info']


                    class ReplyEgress(object):
                        """
                        Reply egress TLV
                        
                        .. attribute:: action
                        
                        	Reply egress action
                        	**type**\: :py:class:`CfmPmEgressActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEgressActionEnum>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\: :py:class:`PortId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.mac_address = None
                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId()
                            self.port_id.parent = self


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\: :py:class:`CfmPmPortIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\: :py:class:`PortIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-egress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.action is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info']


                    class ReplyIngress(object):
                        """
                        Reply ingress TLV
                        
                        .. attribute:: action
                        
                        	Reply ingress action
                        	**type**\: :py:class:`CfmPmIngressActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIngressActionEnum>`
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: port_id
                        
                        	Port ID
                        	**type**\: :py:class:`PortId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.mac_address = None
                            self.port_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId()
                            self.port_id.parent = self


                        class PortId(object):
                            """
                            Port ID
                            
                            .. attribute:: port_id
                            
                            	Port ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: port_id_type
                            
                            	Port ID type
                            	**type**\: :py:class:`CfmPmPortIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPortIdFmtEnum>`
                            
                            .. attribute:: port_id_type_value
                            
                            	Port ID type value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: port_id_value
                            
                            	Port ID (Current)
                            	**type**\: :py:class:`PortIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port_id = None
                                self.port_id_type = None
                                self.port_id_type_value = None
                                self.port_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue()
                                self.port_id_value.parent = self


                            class PortIdValue(object):
                                """
                                Port ID (Current)
                                
                                .. attribute:: port_id_format
                                
                                	PortIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: port_id_mac
                                
                                	Port ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: port_id_raw
                                
                                	Raw Port ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: port_id_string
                                
                                	Port ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:port-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:reply-ingress'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.action is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.port_id is not None and self.port_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info']


                    class SenderId(object):
                        """
                        Sender ID TLV
                        
                        .. attribute:: chassis_id
                        
                        	Chassis ID
                        	**type**\: :py:class:`ChassisId <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId>`
                        
                        .. attribute:: management_address
                        
                        	Management address
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: management_address_domain
                        
                        	Management address domain
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.chassis_id = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId()
                            self.chassis_id.parent = self
                            self.management_address = None
                            self.management_address_domain = None


                        class ChassisId(object):
                            """
                            Chassis ID
                            
                            .. attribute:: chassis_id
                            
                            	Chassis ID (Deprecated)
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: chassis_id_type
                            
                            	Chassis ID Type
                            	**type**\: :py:class:`CfmPmChassisIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmChassisIdFmtEnum>`
                            
                            .. attribute:: chassis_id_type_value
                            
                            	Chassis ID Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: chassis_id_value
                            
                            	Chassis ID (Current)
                            	**type**\: :py:class:`ChassisIdValue <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue>`
                            
                            

                            """

                            _prefix = 'ethernet-cfm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.chassis_id = None
                                self.chassis_id_type = None
                                self.chassis_id_type_value = None
                                self.chassis_id_value = Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue()
                                self.chassis_id_value.parent = self


                            class ChassisIdValue(object):
                                """
                                Chassis ID (Current)
                                
                                .. attribute:: chassis_id_format
                                
                                	ChassisIDFormat
                                	**type**\: :py:class:`CfmPmIdFmtEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmIdFmtEnum>`
                                
                                .. attribute:: chassis_id_mac
                                
                                	Chassis ID MAC Address
                                	**type**\: str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                .. attribute:: chassis_id_raw
                                
                                	Raw Chassis ID
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: chassis_id_string
                                
                                	Chassis ID String
                                	**type**\: str
                                
                                

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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id-value'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:chassis-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:sender-id'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.chassis_id is not None and self.chassis_id._has_data():
                                return True

                            if self.management_address is not None:
                                return True

                            if self.management_address_domain is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info']


                    class UnknownTlv(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.typecode = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:unknown-tlv'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.typecode is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:linktrace-reply'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']


                class TracerouteInformation(object):
                    """
                    Information about the traceroute operation
                    
                    .. attribute:: directed_mac_address
                    
                    	Directed MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: domain
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: options
                    
                    	Options affecting traceroute behavior
                    	**type**\: :py:class:`Options <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options>`
                    
                    .. attribute:: service
                    
                    	Service name
                    	**type**\: str
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mep_id
                    
                    	Source MEP ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: target_mac_address
                    
                    	Target MAC address
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
                    
                    .. attribute:: transaction_id
                    
                    	Transaction ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ttl
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.directed_mac_address = None
                        self.domain = None
                        self.level = None
                        self.options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options()
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
                        	**type**\: :py:class:`BasicOptions <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions>`
                        
                        .. attribute:: exploratory_options
                        
                        	Options for an Exploratory Linktrace
                        	**type**\: :py:class:`ExploratoryOptions <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions>`
                        
                        .. attribute:: mode
                        
                        	Mode
                        	**type**\: :py:class:`CfmPmLtModeEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmLtModeEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-cfm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.basic_options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions()
                            self.basic_options.parent = self
                            self.exploratory_options = Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions()
                            self.exploratory_options.parent = self
                            self.mode = None


                        class BasicOptions(object):
                            """
                            Options for a basic IEEE 802.1ag Linktrace
                            
                            .. attribute:: fdb_only
                            
                            	Only use the Filtering Database for forwarding lookups
                            	**type**\: bool
                            
                            .. attribute:: is_auto
                            
                            	Traceroute was initiated automatically
                            	**type**\: bool
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:basic-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.fdb_only is not None:
                                    return True

                                if self.is_auto is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions']['meta_info']


                        class ExploratoryOptions(object):
                            """
                            Options for an Exploratory Linktrace
                            
                            .. attribute:: delay_constant_factor
                            
                            	Constant Factor for delay calculations
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_model
                            
                            	Delay model for delay calculations
                            	**type**\: :py:class:`CfmPmEltDelayModelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmEltDelayModelEnum>`
                            
                            .. attribute:: reply_filter
                            
                            	Reply Filtering mode used by responders
                            	**type**\: :py:class:`CfmPmElmReplyFilterEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmElmReplyFilterEnum>`
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:exploratory-options'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.delay_constant_factor is not None:
                                    return True

                                if self.delay_model is not None:
                                    return True

                                if self.reply_filter is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.basic_options is not None and self.basic_options._has_data():
                                return True

                            if self.exploratory_options is not None and self.exploratory_options._has_data():
                                return True

                            if self.mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.domain is None:
                        raise YPYDataValidationError('Key property domain is None')
                    if self.interface is None:
                        raise YPYDataValidationError('Key property interface is None')
                    if self.mep_id is None:
                        raise YPYDataValidationError('Key property mep_id is None')
                    if self.service is None:
                        raise YPYDataValidationError('Key property service is None')
                    if self.transaction_id is None:
                        raise YPYDataValidationError('Key property transaction_id is None')

                    return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-caches/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-cache[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + '][Cisco-IOS-XR-ethernet-cfm-oper:mep-id = ' + str(self.mep_id) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + '][Cisco-IOS-XR-ethernet-cfm-oper:transaction-id = ' + str(self.transaction_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.domain is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.mep_id is not None:
                        return True

                    if self.service is not None:
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Global.TracerouteCaches.TracerouteCache']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global/Cisco-IOS-XR-ethernet-cfm-oper:traceroute-caches'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.traceroute_cache is not None:
                    for child_ref in self.traceroute_cache:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Global.TracerouteCaches']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
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

            if self.peer_meps is not None and self.peer_meps._has_data():
                return True

            if self.traceroute_caches is not None and self.traceroute_caches._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
            return meta._meta_table['Cfm.Global']['meta_info']


    class Nodes(object):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node>`
        
        

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
            
            .. attribute:: node
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ccm_learning_databases
            
            	CCMLearningDatabase table
            	**type**\: :py:class:`CcmLearningDatabases <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases>`
            
            .. attribute:: interface_aises
            
            	Interface AIS table
            	**type**\: :py:class:`InterfaceAises <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises>`
            
            .. attribute:: interface_statistics
            
            	Interface Statistics table
            	**type**\: :py:class:`InterfaceStatistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics>`
            
            .. attribute:: summary
            
            	Summary
            	**type**\: :py:class:`Summary <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.Summary>`
            
            

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


            class CcmLearningDatabases(object):
                """
                CCMLearningDatabase table
                
                .. attribute:: ccm_learning_database
                
                	CCM Learning Database entry
                	**type**\: list of :py:class:`CcmLearningDatabase <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase>`
                
                

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
                    
                    .. attribute:: domain
                    
                    	Maintenance Domain
                    	**type**\: str
                    
                    .. attribute:: mac_address
                    
                    	MAC Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: service
                    
                    	Service (Maintenance Association)
                    	**type**\: str
                    
                    .. attribute:: domain_xr
                    
                    	Maintenance domain name
                    	**type**\: str
                    
                    .. attribute:: ingress_interface
                    
                    	The XID of the ingress interface for the CCM
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ingress_interface_string
                    
                    	String representation of the Bridge Domain or Cross\-Connect associated with the ingress XID
                    	**type**\: str
                    
                    .. attribute:: level
                    
                    	Maintenance level
                    	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                    
                    .. attribute:: service_xr
                    
                    	Maintenance association name
                    	**type**\: str
                    
                    .. attribute:: source_mac_address
                    
                    	Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: stale
                    
                    	The XID is stale and may have been reused for a different interface
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.domain = None
                        self.mac_address = None
                        self.service = None
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.domain is None:
                            raise YPYDataValidationError('Key property domain is None')
                        if self.mac_address is None:
                            raise YPYDataValidationError('Key property mac_address is None')
                        if self.service is None:
                            raise YPYDataValidationError('Key property service is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ccm-learning-database[Cisco-IOS-XR-ethernet-cfm-oper:domain = ' + str(self.domain) + '][Cisco-IOS-XR-ethernet-cfm-oper:mac-address = ' + str(self.mac_address) + '][Cisco-IOS-XR-ethernet-cfm-oper:service = ' + str(self.service) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.domain is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.service is not None:
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:ccm-learning-databases'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ccm_learning_database is not None:
                        for child_ref in self.ccm_learning_database:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info']


            class InterfaceAises(object):
                """
                Interface AIS table
                
                .. attribute:: interface_ais
                
                	AIS statistics for a particular interface
                	**type**\: list of :py:class:`InterfaceAis <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis>`
                
                

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
                    
                    .. attribute:: direction
                    
                    	AIS Direction
                    	**type**\: :py:class:`CfmAisDirEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmAisDirEnum>`
                    
                    .. attribute:: interface_name
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_state
                    
                    	IM Interface state
                    	**type**\: str
                    
                    .. attribute:: interworking_state
                    
                    	Interface interworking state
                    	**type**\: :py:class:`CfmBagIwStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIwStateEnum>`
                    
                    .. attribute:: statistics
                    
                    	AIS statistics
                    	**type**\: :py:class:`Statistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics>`
                    
                    .. attribute:: stp_state
                    
                    	STP state
                    	**type**\: :py:class:`CfmBagStpStateEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagStpStateEnum>`
                    
                    

                    """

                    _prefix = 'ethernet-cfm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.direction = None
                        self.interface_name = None
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
                        	**type**\: :py:class:`Defects <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects>`
                        
                        .. attribute:: direction
                        
                        	Direction of AIS packets
                        	**type**\: :py:class:`CfmBagDirectionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagDirectionEnum>`
                        
                        .. attribute:: last_started
                        
                        	Time elapsed since sending last started
                        	**type**\: :py:class:`LastStarted <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted>`
                        
                        .. attribute:: lowest_level
                        
                        	Level of the lowest MEP transmitting AIS
                        	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: sent_packets
                        
                        	Total number of packets sent by the transmitting MEP
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transmission_interval
                        
                        	Interval at which AIS packets are transmitted
                        	**type**\: :py:class:`CfmBagAisIntervalEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagAisIntervalEnum>`
                        
                        .. attribute:: transmission_level
                        
                        	Level that AIS packets are transmitted on
                        	**type**\: :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        .. attribute:: via_level
                        
                        	Levels of other MEPs receiving AIS
                        	**type**\: list of :py:class:`CfmBagMdLevelEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagMdLevelEnum>`
                        
                        

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
                            self.via_level = []


                        class Defects(object):
                            """
                            Defects detected
                            
                            .. attribute:: ais_received
                            
                            	AIS or LCK received
                            	**type**\: bool
                            
                            .. attribute:: auto_missing
                            
                            	Number of missing auto cross\-check MEPs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_port_status
                            
                            	The local port or interface is down
                            	**type**\: bool
                            
                            .. attribute:: missing
                            
                            	Number of missing peer MEPs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_meps_that_timed_out
                            
                            	Number of peer MEPs that have timed out
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_port_status
                            
                            	A peer port or interface is down
                            	**type**\: bool
                            
                            .. attribute:: remote_meps_defects
                            
                            	Defects detected from remote MEPs
                            	**type**\: :py:class:`RemoteMepsDefects <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects>`
                            
                            .. attribute:: unexpected
                            
                            	Number of unexpected peer MEPs
                            	**type**\: int
                            
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
                                	**type**\: bool
                                
                                .. attribute:: invalid_level
                                
                                	Invalid level
                                	**type**\: bool
                                
                                .. attribute:: invalid_maid
                                
                                	Invalid MAID
                                	**type**\: bool
                                
                                .. attribute:: loss_threshold_exceeded
                                
                                	Timed out (loss threshold exceeded)
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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:remote-meps-defects'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
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
                                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                    return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:defects'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
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
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info']


                        class LastStarted(object):
                            """
                            Time elapsed since sending last started
                            
                            .. attribute:: nanoseconds
                            
                            	Nanoseconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seconds
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:last-started'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.nanoseconds is not None:
                                    return True

                                if self.seconds is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                                return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.direction is None:
                            raise YPYDataValidationError('Key property direction is None')
                        if self.interface_name is None:
                            raise YPYDataValidationError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-ais[Cisco-IOS-XR-ethernet-cfm-oper:direction = ' + str(self.direction) + '][Cisco-IOS-XR-ethernet-cfm-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.direction is not None:
                            return True

                        if self.interface_name is not None:
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
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-aises'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface_ais is not None:
                        for child_ref in self.interface_ais:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info']


            class InterfaceStatistics(object):
                """
                Interface Statistics table
                
                .. attribute:: interface_statistic
                
                	Counters for a particular interface
                	**type**\: list of :py:class:`InterfaceStatistic <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic>`
                
                

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
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_xr
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: statistics
                    
                    	EFP statistics
                    	**type**\: :py:class:`Statistics <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics>`
                    
                    

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
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_malformed_opcode
                        
                        	Opcode for last malformed packet
                        	**type**\: :py:class:`CfmBagOpcodeEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagOpcodeEnum>`
                        
                        .. attribute:: last_malformed_reason
                        
                        	Reason last malformed packet was malformed
                        	**type**\: :py:class:`CfmPmPktActionEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmPmPktActionEnum>`
                        
                        .. attribute:: malformed_packets
                        
                        	Number of malformed packets received at this EFP
                        	**type**\: int
                        
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
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
                            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                            return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYDataValidationError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-statistic[Cisco-IOS-XR-ethernet-cfm-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.interface_xr is not None:
                            return True

                        if self.statistics is not None and self.statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                        return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface_statistic is not None:
                        for child_ref in self.interface_statistic:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info']


            class Summary(object):
                """
                Summary
                
                .. attribute:: bnm_enabled_links
                
                	Number of BNM Enabled Links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bridge_domains_and_xconnects
                
                	Number or bridge domains and crossconnects
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_learning_db_entries
                
                	Number of entries in the CCM learning database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ccm_rate
                
                	The combined rate of CCMs on this card
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_misconfigured
                
                	The number of local MEPs disabled due to configuration errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_operational_error
                
                	The number of local MEPs disabled due to operational errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disabled_out_of_resources
                
                	The number of local MEPs disabled due to lack of resources
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: domains
                
                	The number of domains in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_meps
                
                	The number of down\-MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interfaces
                
                	The number of interfaces running CFM
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: issu_role
                
                	ISSU Role of CFM\-D, if any
                	**type**\: :py:class:`CfmBagIssuRoleEnum <ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper.CfmBagIssuRoleEnum>`
                
                .. attribute:: local_meps
                
                	The number of local MEPs in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mips
                
                	The number of MIPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded
                
                	The number of MEPs for which CCM processing has been offloaded
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at10ms
                
                	The number of MEPs offloaded with CCMs at 10ms intervals
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: offloaded_at3_3ms
                
                	The number of MEPs offloaded with CCMs at 3.3ms intervals
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_local_meps
                
                	The number of operational local MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_peer_meps
                
                	The number of operational peer MEPs recorded in the CFM database
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps
                
                	The number of peer MEPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_meps_timed_out
                
                	The number of peer MEPs that have timed out
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
                
                .. attribute:: services
                
                	The number of services in the CFM database
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
                
                .. attribute:: up_meps
                
                	The number of up\-MEPs
                	**type**\: int
                
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
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ethernet-cfm-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
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
                    from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                    return meta._meta_table['Cfm.Nodes.Node.Summary']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYDataValidationError('Key property node is None')

                return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:nodes/Cisco-IOS-XR-ethernet-cfm-oper:node[Cisco-IOS-XR-ethernet-cfm-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
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
                from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
                return meta._meta_table['Cfm.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm/Cisco-IOS-XR-ethernet-cfm-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
            return meta._meta_table['Cfm.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ethernet-cfm-oper:cfm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_oper as meta
        return meta._meta_table['Cfm']['meta_info']






import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CfmPmElrIngressAction_Enum' : _MetaInfoEnum('CfmPmElrIngressAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-ingress-ok':'ELR_INGRESS_OK',
            'elr-ingress-down':'ELR_INGRESS_DOWN',
            'elr-ingress-blocked':'ELR_INGRESS_BLOCKED',
            'elr-ingress-vid':'ELR_INGRESS_VID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmRelayAction_Enum' : _MetaInfoEnum('CfmPmRelayAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'relay-hit':'RELAY_HIT',
            'relay-fdb':'RELAY_FDB',
            'relay-mpdb':'RELAY_MPDB',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagSmanFmt_Enum' : _MetaInfoEnum('CfmBagSmanFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'sman-vlan-id':'SMAN_VLAN_ID',
            'sman-string':'SMAN_STRING',
            'sman-uint16':'SMAN_UINT16',
            'sman-vpn-id':'SMAN_VPN_ID',
            'sman-icc':'SMAN_ICC',
            'sman-unknown':'SMAN_UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmMepDefect_Enum' : _MetaInfoEnum('CfmPmMepDefect_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'defect-none':'DEFECT_NONE',
            'defect-rdi-ccm':'DEFECT_RDI_CCM',
            'defect-ma-cstatus':'DEFECT_MA_CSTATUS',
            'defect-remote-ccm':'DEFECT_REMOTE_CCM',
            'defect-error-ccm':'DEFECT_ERROR_CCM',
            'defect-cross-connect-ccm':'DEFECT_CROSS_CONNECT_CCM',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElrEgressAction_Enum' : _MetaInfoEnum('CfmPmElrEgressAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-egress-ok':'ELR_EGRESS_OK',
            'elr-egress-down':'ELR_EGRESS_DOWN',
            'elr-egress-blocked':'ELR_EGRESS_BLOCKED',
            'elr-egress-vid':'ELR_EGRESS_VID',
            'elr-egress-mac':'ELR_EGRESS_MAC',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIngressAction_Enum' : _MetaInfoEnum('CfmPmIngressAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'ingress-ok':'INGRESS_OK',
            'ingress-down':'INGRESS_DOWN',
            'ingress-blocked':'INGRESS_BLOCKED',
            'ingress-vid':'INGRESS_VID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagCcmInterval_Enum' : _MetaInfoEnum('CfmBagCcmInterval_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interval-none':'INTERVAL_NONE',
            'interval3-3ms':'INTERVAL3_3MS',
            'interval10ms':'INTERVAL10MS',
            'interval100ms':'INTERVAL100MS',
            'interval1s':'INTERVAL1S',
            'interval10s':'INTERVAL10S',
            'interval1m':'INTERVAL1M',
            'interval10m':'INTERVAL10M',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmChassisIdFmt_Enum' : _MetaInfoEnum('CfmPmChassisIdFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'chassis-id-chassis-component':'CHASSIS_ID_CHASSIS_COMPONENT',
            'chassis-id-interface-alias':'CHASSIS_ID_INTERFACE_ALIAS',
            'chassis-id-port-component':'CHASSIS_ID_PORT_COMPONENT',
            'chassis-id-mac-address':'CHASSIS_ID_MAC_ADDRESS',
            'chassis-id-network-address':'CHASSIS_ID_NETWORK_ADDRESS',
            'chassis-id-interface-name':'CHASSIS_ID_INTERFACE_NAME',
            'chassis-id-local':'CHASSIS_ID_LOCAL',
            'chassis-id-unknown-type':'CHASSIS_ID_UNKNOWN_TYPE',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperOperation_Enum' : _MetaInfoEnum('SlaOperOperation_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'operation-type-configured':'OPERATION_TYPE_CONFIGURED',
            'operation-type-ondemand':'OPERATION_TYPE_ONDEMAND',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmLastHopFmt_Enum' : _MetaInfoEnum('CfmPmLastHopFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'last-hop-none':'LAST_HOP_NONE',
            'last-hop-host-name':'LAST_HOP_HOST_NAME',
            'last-hop-egress-id':'LAST_HOP_EGRESS_ID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIdFmt_Enum' : _MetaInfoEnum('CfmPmIdFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'id-format-is-string':'ID_FORMAT_IS_STRING',
            'id-format-is-mac-address':'ID_FORMAT_IS_MAC_ADDRESS',
            'id-format-is-raw-hex':'ID_FORMAT_IS_RAW_HEX',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmRmepState_Enum' : _MetaInfoEnum('CfmPmRmepState_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'peer-mep-idle':'PEER_MEP_IDLE',
            'peer-mep-start':'PEER_MEP_START',
            'peer-mep-failed':'PEER_MEP_FAILED',
            'peer-mep-ok':'PEER_MEP_OK',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagCcmOffload_Enum' : _MetaInfoEnum('CfmBagCcmOffload_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'offload-none':'OFFLOAD_NONE',
            'offload-software':'OFFLOAD_SOFTWARE',
            'offload-hardware':'OFFLOAD_HARDWARE',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAisReceive_Enum' : _MetaInfoEnum('CfmPmAisReceive_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'receive-none':'RECEIVE_NONE',
            'receive-ais':'RECEIVE_AIS',
            'receive-lck':'RECEIVE_LCK',
            'receive-direct':'RECEIVE_DIRECT',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmMaMpVariety_Enum' : _MetaInfoEnum('CfmMaMpVariety_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'mip':'MIP',
            'up-mep':'UP_MEP',
            'downmep':'DOWNMEP',
            'unknown-mep':'UNKNOWN_MEP',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPktAction_Enum' : _MetaInfoEnum('CfmPmPktAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'packet-processed':'PACKET_PROCESSED',
            'packet-forwarded':'PACKET_FORWARDED',
            'unknown-opcode':'UNKNOWN_OPCODE',
            'filter-level':'FILTER_LEVEL',
            'filter-blocked':'FILTER_BLOCKED',
            'filter-local-mac':'FILTER_LOCAL_MAC',
            'malformed-ccm-size':'MALFORMED_CCM_SIZE',
            'malformed-ccm-mep-id':'MALFORMED_CCM_MEP_ID',
            'malformed-too-short':'MALFORMED_TOO_SHORT',
            'malformed-destination-mac-unicast':'MALFORMED_DESTINATION_MAC_UNICAST',
            'malformed-destination-mac-multicast':'MALFORMED_DESTINATION_MAC_MULTICAST',
            'malformed-tlv-offset':'MALFORMED_TLV_OFFSET',
            'malformed-lbm-source-mac':'MALFORMED_LBM_SOURCE_MAC',
            'malformed-ltr-relay-action':'MALFORMED_LTR_RELAY_ACTION',
            'malformed-ltr-reply-tlv':'MALFORMED_LTR_REPLY_TLV',
            'malformed-lt-origin':'MALFORMED_LT_ORIGIN',
            'malformed-ltm-target':'MALFORMED_LTM_TARGET',
            'malformed-source-mac':'MALFORMED_SOURCE_MAC',
            'malformed-header-too-short':'MALFORMED_HEADER_TOO_SHORT',
            'malformed-tlv-header-overrun':'MALFORMED_TLV_HEADER_OVERRUN',
            'malformed-tlv-overrun':'MALFORMED_TLV_OVERRUN',
            'malformed-duplicate-sender-id':'MALFORMED_DUPLICATE_SENDER_ID',
            'malformed-duplicate-port-status':'MALFORMED_DUPLICATE_PORT_STATUS',
            'malformed-duplicate-interface-status':'MALFORMED_DUPLICATE_INTERFACE_STATUS',
            'malformed-wrong-tlv':'MALFORMED_WRONG_TLV',
            'malformed-duplicate-data':'MALFORMED_DUPLICATE_DATA',
            'malformed-duplicate-ltr-egress-id':'MALFORMED_DUPLICATE_LTR_EGRESS_ID',
            'malformed-duplicate-reply-ingress':'MALFORMED_DUPLICATE_REPLY_INGRESS',
            'malformed-duplicate-reply-egress':'MALFORMED_DUPLICATE_REPLY_EGRESS',
            'malformed-duplicate-ltm-egress-id':'MALFORMED_DUPLICATE_LTM_EGRESS_ID',
            'malformed-sender-id-size':'MALFORMED_SENDER_ID_SIZE',
            'malformed-chassis-id-size':'MALFORMED_CHASSIS_ID_SIZE',
            'malformed-mgmt-address-domain-size':'MALFORMED_MGMT_ADDRESS_DOMAIN_SIZE',
            'malformed-mgmt-address-size':'MALFORMED_MGMT_ADDRESS_SIZE',
            'malformed-port-status-size':'MALFORMED_PORT_STATUS_SIZE',
            'malformed-port-status':'MALFORMED_PORT_STATUS',
            'malformed-interface-status-size':'MALFORMED_INTERFACE_STATUS_SIZE',
            'malformed-interface-status':'MALFORMED_INTERFACE_STATUS',
            'malformed-organization-specific-tlv-size':'MALFORMED_ORGANIZATION_SPECIFIC_TLV_SIZE',
            'malformed-duplicate-mep-name':'MALFORMED_DUPLICATE_MEP_NAME',
            'malformed-duplicate-additional-interface-status':'MALFORMED_DUPLICATE_ADDITIONAL_INTERFACE_STATUS',
            'malformed-ltr-egress-id-size':'MALFORMED_LTR_EGRESS_ID_SIZE',
            'malformed-reply-ingress-size':'MALFORMED_REPLY_INGRESS_SIZE',
            'malformed-ingress-action':'MALFORMED_INGRESS_ACTION',
            'malformed-reply-ingress-mac':'MALFORMED_REPLY_INGRESS_MAC',
            'malformed-ingress-port-length-size':'MALFORMED_INGRESS_PORT_LENGTH_SIZE',
            'malformed-ingress-port-id-length':'MALFORMED_INGRESS_PORT_ID_LENGTH',
            'malformed-ingress-port-id-size':'MALFORMED_INGRESS_PORT_ID_SIZE',
            'malformed-reply-egress-size':'MALFORMED_REPLY_EGRESS_SIZE',
            'malformed-egress-action':'MALFORMED_EGRESS_ACTION',
            'malformed-reply-egress-mac':'MALFORMED_REPLY_EGRESS_MAC',
            'malformed-egress-port-length-size':'MALFORMED_EGRESS_PORT_LENGTH_SIZE',
            'malformed-egress-port-id-length':'MALFORMED_EGRESS_PORT_ID_LENGTH',
            'malformed-egress-port-id-size':'MALFORMED_EGRESS_PORT_ID_SIZE',
            'malformed-ltm-egress-id-size':'MALFORMED_LTM_EGRESS_ID_SIZE',
            'malformed-mep-name-size':'MALFORMED_MEP_NAME_SIZE',
            'malformed-mep-name-name-length':'MALFORMED_MEP_NAME_NAME_LENGTH',
            'malformed-additional-interface-status-size':'MALFORMED_ADDITIONAL_INTERFACE_STATUS_SIZE',
            'malformed-additional-interface-status':'MALFORMED_ADDITIONAL_INTERFACE_STATUS',
            'malformed-ccm-interval':'MALFORMED_CCM_INTERVAL',
            'malformed-mdid-mac-address-length':'MALFORMED_MDID_MAC_ADDRESS_LENGTH',
            'malformed-mdid-length':'MALFORMED_MDID_LENGTH',
            'malformed-sman-length':'MALFORMED_SMAN_LENGTH',
            'malformed-sman2-byte-length':'MALFORMED_SMAN2_BYTE_LENGTH',
            'malformed-sman-vpn-id-length':'MALFORMED_SMAN_VPN_ID_LENGTH',
            'malformed-elr-no-reply-tlv':'MALFORMED_ELR_NO_REPLY_TLV',
            'malformed-separate-elr-reply-egress':'MALFORMED_SEPARATE_ELR_REPLY_EGRESS',
            'malformed-dcm-destination-multicast':'MALFORMED_DCM_DESTINATION_MULTICAST',
            'malformed-dcm-embed-length':'MALFORMED_DCM_EMBED_LENGTH',
            'malformed-dcm-embed-level':'MALFORMED_DCM_EMBED_LEVEL',
            'malformed-dcm-embed-version':'MALFORMED_DCM_EMBED_VERSION',
            'malformed-elr-relay-action':'MALFORMED_ELR_RELAY_ACTION',
            'malformed-elr-tt-ls':'MALFORMED_ELR_TT_LS',
            'malformed-elr-ttl-ingress':'MALFORMED_ELR_TTL_INGRESS',
            'malformed-elr-ttl-egress':'MALFORMED_ELR_TTL_EGRESS',
            'malformed-elm-destination-unicast':'MALFORMED_ELM_DESTINATION_UNICAST',
            'malformed-elm-egress-id':'MALFORMED_ELM_EGRESS_ID',
            'malformed-dcm-embed-oui':'MALFORMED_DCM_EMBED_OUI',
            'malformed-dcm-embed-opcode':'MALFORMED_DCM_EMBED_OPCODE',
            'malformed-elm-constant-zero':'MALFORMED_ELM_CONSTANT_ZERO',
            'malformed-elr-timeout-zero':'MALFORMED_ELR_TIMEOUT_ZERO',
            'malformed-duplicate-test':'MALFORMED_DUPLICATE_TEST',
            'malformed-dmm-source-mac':'MALFORMED_DMM_SOURCE_MAC',
            'malformed-test-size':'MALFORMED_TEST_SIZE',
            'malformed-dmr-time-stamps':'MALFORMED_DMR_TIME_STAMPS',
            'malformed-dm-time-stamp-fmt':'MALFORMED_DM_TIME_STAMP_FMT',
            'malformed-ais-interval':'MALFORMED_AIS_INTERVAL',
            'filter-interface-down':'FILTER_INTERFACE_DOWN',
            'filter-forward-standby':'FILTER_FORWARD_STANDBY',
            'malformed-sman-icc-based-length':'MALFORMED_SMAN_ICC_BASED_LENGTH',
            'filter-foward-issu-secondary':'FILTER_FOWARD_ISSU_SECONDARY',
            'filter-response-standby':'FILTER_RESPONSE_STANDBY',
            'filter-response-issu-secondary':'FILTER_RESPONSE_ISSU_SECONDARY',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaBucketSize_Enum' : _MetaInfoEnum('SlaBucketSize_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'buckets-per-probe':'BUCKETS_PER_PROBE',
            'probes-per-bucket':'PROBES_PER_BUCKET',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmEltDelayModel_Enum' : _MetaInfoEnum('CfmPmEltDelayModel_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'delay-model-invalid':'DELAY_MODEL_INVALID',
            'delay-model-logarithmic':'DELAY_MODEL_LOGARITHMIC',
            'delay-model-constant':'DELAY_MODEL_CONSTANT',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAisTransmit_Enum' : _MetaInfoEnum('CfmPmAisTransmit_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'transmit-none':'TRANSMIT_NONE',
            'transmit-ais':'TRANSMIT_AIS',
            'transmit-ais-direct':'TRANSMIT_AIS_DIRECT',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElrRelayAction_Enum' : _MetaInfoEnum('CfmPmElrRelayAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-relay-hit':'ELR_RELAY_HIT',
            'elr-relay-fdb':'ELR_RELAY_FDB',
            'elr-relay-flood':'ELR_RELAY_FLOOD',
            'elr-relay-drop':'ELR_RELAY_DROP',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPortStatus_Enum' : _MetaInfoEnum('CfmPmPortStatus_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'port-status-blocked':'PORT_STATUS_BLOCKED',
            'port-status-up':'PORT_STATUS_UP',
            'port-status-unknown':'PORT_STATUS_UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagIwState_Enum' : _MetaInfoEnum('CfmBagIwState_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interworking-up':'INTERWORKING_UP',
            'interworking-test':'INTERWORKING_TEST',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagMdidFmt_Enum' : _MetaInfoEnum('CfmBagMdidFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'mdid-null':'MDID_NULL',
            'mdid-dns-like':'MDID_DNS_LIKE',
            'mdid-mac-address':'MDID_MAC_ADDRESS',
            'mdid-string':'MDID_STRING',
            'mdid-unknown':'MDID_UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagBdidFmt_Enum' : _MetaInfoEnum('CfmBagBdidFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'invalid':'INVALID',
            'bd-id':'BD_ID',
            'xc-p2p-id':'XC_P2P_ID',
            'xc-mp2mp-id':'XC_MP2MP_ID',
            'down-only':'DOWN_ONLY',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagIssuRole_Enum' : _MetaInfoEnum('CfmBagIssuRole_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'unknown':'UNKNOWN',
            'primary':'PRIMARY',
            'secondary':'SECONDARY',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagStpState_Enum' : _MetaInfoEnum('CfmBagStpState_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'stp-up':'STP_UP',
            'stp-blocked':'STP_BLOCKED',
            'stp-unknown':'STP_UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagMdLevel_Enum' : _MetaInfoEnum('CfmBagMdLevel_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'level0':'LEVEL0',
            'level1':'LEVEL1',
            'level2':'LEVEL2',
            'level3':'LEVEL3',
            'level4':'LEVEL4',
            'level5':'LEVEL5',
            'level6':'LEVEL6',
            'level7':'LEVEL7',
            'level-invalid':'LEVEL_INVALID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperPacketPriority_Enum' : _MetaInfoEnum('SlaOperPacketPriority_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'priority-none':'PRIORITY_NONE',
            'priority-cos':'PRIORITY_COS',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagAisInterval_Enum' : _MetaInfoEnum('CfmBagAisInterval_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'ais-interval-none':'AIS_INTERVAL_NONE',
            'ais-interval1s':'AIS_INTERVAL1S',
            'ais-interval1m':'AIS_INTERVAL1M',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmRmepXcState_Enum' : _MetaInfoEnum('CfmPmRmepXcState_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'cross-check-ok':'CROSS_CHECK_OK',
            'cross-check-missing':'CROSS_CHECK_MISSING',
            'cross-check-extra':'CROSS_CHECK_EXTRA',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmLtMode_Enum' : _MetaInfoEnum('CfmPmLtMode_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'cfm-pm-lt-mode-basic':'CFM_PM_LT_MODE_BASIC',
            'cfm-pm-lt-mode-exploratory':'CFM_PM_LT_MODE_EXPLORATORY',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIntfStatus_Enum' : _MetaInfoEnum('CfmPmIntfStatus_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interface-status-up':'INTERFACE_STATUS_UP',
            'interface-status-down':'INTERFACE_STATUS_DOWN',
            'interface-status-testing':'INTERFACE_STATUS_TESTING',
            'interface-status-unknown':'INTERFACE_STATUS_UNKNOWN',
            'interface-status-dormant':'INTERFACE_STATUS_DORMANT',
            'interface-status-not-present':'INTERFACE_STATUS_NOT_PRESENT',
            'interface-status-lower-layer-down':'INTERFACE_STATUS_LOWER_LAYER_DOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagDirection_Enum' : _MetaInfoEnum('CfmBagDirection_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'direction-up':'DIRECTION_UP',
            'direction-down':'DIRECTION_DOWN',
            'direction-invalid':'DIRECTION_INVALID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmEgressAction_Enum' : _MetaInfoEnum('CfmPmEgressAction_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'egress-ok':'EGRESS_OK',
            'egress-down':'EGRESS_DOWN',
            'egress-blocked':'EGRESS_BLOCKED',
            'egress-vid':'EGRESS_VID',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElmReplyFilter_Enum' : _MetaInfoEnum('CfmPmElmReplyFilter_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'reply-filter-not-present':'REPLY_FILTER_NOT_PRESENT',
            'reply-filter-default':'REPLY_FILTER_DEFAULT',
            'reply-filter-vlan-topology':'REPLY_FILTER_VLAN_TOPOLOGY',
            'reply-filter-spanning-tree':'REPLY_FILTER_SPANNING_TREE',
            'reply-filter-all-ports':'REPLY_FILTER_ALL_PORTS',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmAisDir_Enum' : _MetaInfoEnum('CfmAisDir_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAddlIntfStatus_Enum' : _MetaInfoEnum('CfmPmAddlIntfStatus_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'unknown':'UNKNOWN',
            'administratively-down':'ADMINISTRATIVELY_DOWN',
            'remote-excessive-errors':'REMOTE_EXCESSIVE_ERRORS',
            'local-excessive-errors':'LOCAL_EXCESSIVE_ERRORS',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagOpcode_Enum' : _MetaInfoEnum('CfmBagOpcode_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'reserved':'RESERVED',
            'ccm':'CCM',
            'lbr':'LBR',
            'lbm':'LBM',
            'ltr':'LTR',
            'ltm':'LTM',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperTestPatternScheme_Enum' : _MetaInfoEnum('SlaOperTestPatternScheme_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'hex':'HEX',
            'pseudo-random':'PSEUDO_RANDOM',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmMepFngState_Enum' : _MetaInfoEnum('CfmPmMepFngState_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'fng-reset':'FNG_RESET',
            'fng-defect':'FNG_DEFECT',
            'fng-report-defect':'FNG_REPORT_DEFECT',
            'fng-defect-reported':'FNG_DEFECT_REPORTED',
            'fng-defect-clearing':'FNG_DEFECT_CLEARING',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPortIdFmt_Enum' : _MetaInfoEnum('CfmPmPortIdFmt_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'port-id-interface-alias':'PORT_ID_INTERFACE_ALIAS',
            'port-id-port-component':'PORT_ID_PORT_COMPONENT',
            'port-id-mac-address':'PORT_ID_MAC_ADDRESS',
            'port-id-network-address':'PORT_ID_NETWORK_ADDRESS',
            'port-id-interface-name':'PORT_ID_INTERFACE_NAME',
            'port-id-agent-circuit-id':'PORT_ID_AGENT_CIRCUIT_ID',
            'port-id-local':'PORT_ID_LOCAL',
            'port-id-unknown':'PORT_ID_UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperBucket_Enum' : _MetaInfoEnum('SlaOperBucket_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'bucket-type-bins':'BUCKET_TYPE_BINS',
            'bucket-type-samples':'BUCKET_TYPE_SAMPLES',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaRecordableMetric_Enum' : _MetaInfoEnum('SlaRecordableMetric_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'metric-invalid':'METRIC_INVALID',
            'metric-round-trip-delay':'METRIC_ROUND_TRIP_DELAY',
            'metric-one-way-delay-sd':'METRIC_ONE_WAY_DELAY_SD',
            'metric-one-way-delay-ds':'METRIC_ONE_WAY_DELAY_DS',
            'metric-round-trip-jitter':'METRIC_ROUND_TRIP_JITTER',
            'metric-one-way-jitter-sd':'METRIC_ONE_WAY_JITTER_SD',
            'metric-one-way-jitter-ds':'METRIC_ONE_WAY_JITTER_DS',
            'metric-one-way-flr-sd':'METRIC_ONE_WAY_FLR_SD',
            'metric-one-way-flr-ds':'METRIC_ONE_WAY_FLR_DS',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt_Enum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local Customer Edge Identifier (CE-ID)
                ''',
                'ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge/XConnect Group
                ''',
                'group',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge Domain/XConnect
                ''',
                'name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bridge-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('bridge-domain-id', REFERENCE_CLASS, 'BridgeDomainId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId', 
                [], [], 
                '''                BD/XC ID, or Service name if the Service is
                'down-only'
                ''',
                'bridge_domain_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bridge-domain-is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The BD/XC is configured globally
                ''',
                'bridge_domain_is_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('l2-fib-download-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The BD/XC could not be downloaded to L2FIB
                ''',
                'l2_fib_download_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'global-configuration-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.GlobalConfigurationErrors' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.GlobalConfigurationErrors',
            False, 
            [
            _MetaInfoClassMember('global-configuration-error', REFERENCE_LIST, 'GlobalConfigurationError' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError', 
                [], [], 
                '''                Information about a particular configuration
                error
                ''',
                'global_configuration_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'global-configuration-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions',
            False, 
            [
            _MetaInfoClassMember('fdb-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only use the Filtering Database for forwarding
                lookups
                ''',
                'fdb_only',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('is-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Traceroute was initiated automatically
                ''',
                'is_auto',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'basic-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions',
            False, 
            [
            _MetaInfoClassMember('delay-constant-factor', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Constant Factor for delay calculations
                ''',
                'delay_constant_factor',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel_Enum', 
                [], [], 
                '''                Delay model for delay calculations
                ''',
                'delay_model',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-filter', REFERENCE_ENUM_CLASS, 'CfmPmElmReplyFilter_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilter_Enum', 
                [], [], 
                '''                Reply Filtering mode used by responders
                ''',
                'reply_filter',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options',
            False, 
            [
            _MetaInfoClassMember('basic-options', REFERENCE_CLASS, 'BasicOptions' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions', 
                [], [], 
                '''                Options for a basic IEEE 802.1ag Linktrace
                ''',
                'basic_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('exploratory-options', REFERENCE_CLASS, 'ExploratoryOptions' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions', 
                [], [], 
                '''                Options for an Exploratory Linktrace
                ''',
                'exploratory_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'CfmPmLtMode_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtMode_Enum', 
                [], [], 
                '''                Mode
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation',
            False, 
            [
            _MetaInfoClassMember('directed-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Directed MAC address
                ''',
                'directed_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options', 
                [], [], 
                '''                Options affecting traceroute behavior
                ''',
                'options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address
                ''',
                'source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Source MEP ID
                ''',
                'source_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Target MAC address
                ''',
                'target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Target MEP ID
                ''',
                'target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Timestamp of initiation time (seconds)
                ''',
                'timestamp',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Time to live
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Time (in seconds) before the traceroute
                completes
                ''',
                'time_left',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-information', REFERENCE_CLASS, 'TracerouteInformation' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation', 
                [], [], 
                '''                Information about the traceroute operation
                ''',
                'traceroute_information',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'incomplete-traceroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.IncompleteTraceroutes' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.IncompleteTraceroutes',
            False, 
            [
            _MetaInfoClassMember('incomplete-traceroute', REFERENCE_LIST, 'IncompleteTraceroute' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute', 
                [], [], 
                '''                Information about a traceroute operation that
                has not yet timed out
                ''',
                'incomplete_traceroute',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'incomplete-traceroutes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'receiving-start',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sending-start',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.AisStatistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.AisStatistics',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'CfmBagAisInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval_Enum', 
                [], [], 
                '''                AIS transmission interval
                ''',
                'interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-interval', REFERENCE_ENUM_CLASS, 'CfmBagAisInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval_Enum', 
                [], [], 
                '''                The interval of the last received AIS packet
                ''',
                'last_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address of the last received AIS
                packet
                ''',
                'last_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                AIS transmission level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('receiving-ais', REFERENCE_ENUM_CLASS, 'CfmPmAisReceive_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisReceive_Enum', 
                [], [], 
                '''                Details of how the signal is being received
                ''',
                'receiving_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('receiving-start', REFERENCE_CLASS, 'ReceivingStart' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart', 
                [], [], 
                '''                Time elapsed since AIS receiving started
                ''',
                'receiving_start',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sending-ais', REFERENCE_ENUM_CLASS, 'CfmPmAisTransmit_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisTransmit_Enum', 
                [], [], 
                '''                Details of how AIS is being transmitted
                ''',
                'sending_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sending-start', REFERENCE_CLASS, 'SendingStart' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart', 
                [], [], 
                '''                Time elapsed since AIS sending started
                ''',
                'sending_start',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ais-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects',
            False, 
            [
            _MetaInfoClassMember('invalid-ccm-interval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid CCM interval
                ''',
                'invalid_ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid level
                ''',
                'invalid_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-maid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid MAID
                ''',
                'invalid_maid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('loss-threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Timed out (loss threshold exceeded)
                ''',
                'loss_threshold_exceeded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loop detected (our MAC address received)
                ''',
                'received_our_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mep-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configuration Error (our MEP ID received)
                ''',
                'received_our_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-rdi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote defection indication received
                ''',
                'received_rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'remote-meps-defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.Defects' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.Defects',
            False, 
            [
            _MetaInfoClassMember('ais-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AIS or LCK received
                ''',
                'ais_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('auto-missing', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of missing auto cross-check MEPs
                ''',
                'auto_missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-port-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The local port or interface is down
                ''',
                'local_port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('missing', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of missing peer MEPs
                ''',
                'missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-that-timed-out', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of peer MEPs that have timed out
                ''',
                'peer_meps_that_timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-port-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A peer port or interface is down
                ''',
                'peer_port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-meps-defects', REFERENCE_CLASS, 'RemoteMepsDefects' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects', 
                [], [], 
                '''                Defects detected from remote MEPs
                ''',
                'remote_meps_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unexpected', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unexpected peer MEPs
                ''',
                'unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep.Statistics',
            False, 
            [
            _MetaInfoClassMember('ai-ss-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of AIS messages received
                ''',
                'ai_ss_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ai-ss-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of AIS messages sent
                ''',
                'ai_ss_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bn-ms-discarded', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of BNM messages discarded
                ''',
                'bn_ms_discarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bn-ms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of BNM messages received
                ''',
                'bn_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-discarded', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs discarded because maximum MEPs
                limit was reached
                ''',
                'ccms_discarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received out-of-sequence
                ''',
                'ccms_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received
                ''',
                'ccms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs sent
                ''',
                'ccms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-ms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of DMM messages received
                ''',
                'dm_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of DMM messages sent
                ''',
                'dm_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-rs-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of DMR messages received
                ''',
                'dm_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of DMR messages sent
                ''',
                'dm_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-ms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBMs received
                ''',
                'lb_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBMs sent
                ''',
                'lb_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-bad-data', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBRs received with non-matching
                user-specified data
                ''',
                'lb_rs_bad_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBRs received out-of-sequence
                ''',
                'lb_rs_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBRs received
                ''',
                'lb_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LBRs sent
                ''',
                'lb_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lc-ks-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LCK messages received
                ''',
                'lc_ks_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-ms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LMM messages received
                ''',
                'lm_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LMM messages sent
                ''',
                'lm_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-rs-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LMR messages received
                ''',
                'lm_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of LMR messages sent
                ''',
                'lm_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lt-rs-received-unexpected', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of unexpected LTRs received
                ''',
                'lt_rs_received_unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-ms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of SLM messages received
                ''',
                'sl_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of SLM messages sent
                ''',
                'sl_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-rs-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of SLR messages received
                ''',
                'sl_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of SLR messages sent
                ''',
                'sl_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps.LocalMep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps.LocalMep',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('ais-statistics', REFERENCE_CLASS, 'AisStatistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.AisStatistics', 
                [], [], 
                '''                MEP AIS statistics
                ''',
                'ais_statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-generation-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                CCM generation enabled
                ''',
                'ccm_generation_enabled',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval_Enum', 
                [], [], 
                '''                The interval between CCMs
                ''',
                'ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-offload', REFERENCE_ENUM_CLASS, 'CfmBagCcmOffload_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffload_Enum', 
                [], [], 
                '''                Offload status of CCM processing
                ''',
                'ccm_offload',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                CoS bits the MEP will use for sent packets, if
                configured
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('cross-connect-ccm-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A cross-connect CCM error has been reported
                ''',
                'cross_connect_ccm_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('defects', REFERENCE_CLASS, 'Defects' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.Defects', 
                [], [], 
                '''                Defects detected from peer MEPs
                ''',
                'defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domain-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('efd-triggered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EFD triggered on the interface
                ''',
                'efd_triggered',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('error-ccm-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A CCM error has been reported
                ''',
                'error_ccm_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('fault-notification-state', REFERENCE_ENUM_CLASS, 'CfmPmMepFngState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepFngState_Enum', 
                [], [], 
                '''                Fault Notification Generation state
                ''',
                'fault_notification_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('highest-defect', REFERENCE_ENUM_CLASS, 'CfmPmMepDefect_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepDefect_Enum', 
                [], [], 
                '''                Highest-priority defect present since last FNG
                reset
                ''',
                'highest_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IM Interface state
                ''',
                'interface_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interworking-state', REFERENCE_ENUM_CLASS, 'CfmBagIwState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwState_Enum', 
                [], [], 
                '''                Interface interworking state
                ''',
                'interworking_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-status-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A peer MEP port or interface status error has
                been reported
                ''',
                'mac_status_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-direction', REFERENCE_ENUM_CLASS, 'CfmBagDirection_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection_Enum', 
                [], [], 
                '''                MEP facing direction
                ''',
                'mep_direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-lbm-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Next Transaction ID to be sent in a Loopback
                Message
                ''',
                'next_lbm_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-ltm-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Next Transaction ID to be sent in a Linktrace
                Message
                ''',
                'next_ltm_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-mep-ccm-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A peer MEP CCM error has been reported
                ''',
                'peer_mep_ccm_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-detected', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of peer MEPs detected
                ''',
                'peer_meps_detected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-with-errors-detected', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of peer MEPs detected with errors
                ''',
                'peer_meps_with_errors_detected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('rdi-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A peer MEP RDI defect has been reported
                ''',
                'rdi_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-defect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote defect indicated
                ''',
                'remote_defect',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP is on a standby bundle interface
                ''',
                'standby',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep.Statistics', 
                [], [], 
                '''                MEP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('stp-state', REFERENCE_ENUM_CLASS, 'CfmBagStpState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpState_Enum', 
                [], [], 
                '''                STP state
                ''',
                'stp_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'local-mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.LocalMeps' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.LocalMeps',
            False, 
            [
            _MetaInfoClassMember('local-mep', REFERENCE_LIST, 'LocalMep' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps.LocalMep', 
                [], [], 
                '''                Information about a particular local MEP
                ''',
                'local_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'local-meps',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Domain level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point-type', REFERENCE_ENUM_CLASS, 'CfmMaMpVariety_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVariety_Enum', 
                [], [], 
                '''                Type of Maintenance Point
                ''',
                'maintenance_point_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'maintenance-point',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MaintenancePoints.MaintenancePoint' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MaintenancePoints.MaintenancePoint',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point', REFERENCE_CLASS, 'MaintenancePoint' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint', 
                [], [], 
                '''                Maintenance Point
                ''',
                'maintenance_point',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-has-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MEP error flag
                ''',
                'mep_has_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'maintenance-point',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MaintenancePoints' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MaintenancePoints',
            False, 
            [
            _MetaInfoClassMember('maintenance-point', REFERENCE_LIST, 'MaintenancePoint' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MaintenancePoints.MaintenancePoint', 
                [], [], 
                '''                Information about a particular Maintenance
                Point
                ''',
                'maintenance_point',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'maintenance-points',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt_Enum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local Customer Edge Identifier (CE-ID)
                ''',
                'ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge/XConnect Group
                ''',
                'group',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge Domain/XConnect
                ''',
                'name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-bridge-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Domain level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point-type', REFERENCE_ENUM_CLASS, 'CfmMaMpVariety_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVariety_Enum', 
                [], [], 
                '''                Type of Maintenance Point
                ''',
                'maintenance_point_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement',
            False, 
            [
            _MetaInfoClassMember('controller', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controller
                ''',
                'controller',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('responder', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Responder
                ''',
                'responder',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'delay-measurement',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback',
            False, 
            [
            _MetaInfoClassMember('controller', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controller
                ''',
                'controller',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('responder', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Responder
                ''',
                'responder',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'loopback',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement',
            False, 
            [
            _MetaInfoClassMember('controller', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Controller
                ''',
                'controller',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('responder', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Responder
                ''',
                'responder',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'synthetic-loss-measurement',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities',
            False, 
            [
            _MetaInfoClassMember('delay-measurement', REFERENCE_CLASS, 'DelayMeasurement' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement', 
                [], [], 
                '''                Delay Measurement
                ''',
                'delay_measurement',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('loopback', REFERENCE_CLASS, 'Loopback' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback', 
                [], [], 
                '''                Loopback
                ''',
                'loopback',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('synthetic-loss-measurement', REFERENCE_CLASS, 'SyntheticLossMeasurement' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement', 
                [], [], 
                '''                Synthetic Loss Measurement
                ''',
                'synthetic_loss_measurement',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'satellite-capabilities',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmt_Enum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Local Customer Edge Identifier (CE-ID)
                ''',
                'ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge/XConnect Group
                ''',
                'group',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Bridge Domain/XConnect
                ''',
                'name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-ce-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'service-bridge-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors.MepConfigurationError' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors.MepConfigurationError',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('ais-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AIS is configured on the same interface as the
                down MEP
                ''',
                'ais_configured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bridge-domain-mismatch', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP's EFP is not in the Service's Bridge
                Domain
                ''',
                'bridge_domain_mismatch',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bridge-domain-not-in-bd-infra', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A BD/XC specified in the MEG config, but it does
                not exist globally.
                ''',
                'bridge_domain_not_in_bd_infra',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bundle-level0', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP is configured in a domain at level 0, on
                a bundle interface or sub-interface.  This is
                not supported
                ''',
                'bundle_level0',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval_Enum', 
                [], [], 
                '''                Interval between CCMs sent on this MEP.
                ''',
                'ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-interval-not-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                CCM Interval is less than minimum interval
                supported by hardware
                ''',
                'ccm_interval_not_supported',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-bridge-domain', REFERENCE_CLASS, 'InterfaceBridgeDomain' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain', 
                [], [], 
                '''                ID of the BD/XC that the MEP's EFP is in, if any
                ''',
                'interface_bridge_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level-conflict', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Another MEP facing in the same direction is at
                the same Maintenance Level
                ''',
                'level_conflict',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep', REFERENCE_CLASS, 'Mep' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep', 
                [], [], 
                '''                The MEP that has errors
                ''',
                'mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('no-domain', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP's Domain is not configured
                ''',
                'no_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('no-interface-type', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                We haven't yet been able to look up the
                interface type to find whether the interface is
                a bundle.
                ''',
                'no_interface_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('no-mlacp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The EFP is a bundle and the mLACP mode is not
                yet known.
                ''',
                'no_mlacp',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('no-service', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP's Service is not configured
                ''',
                'no_service',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('no-valid-mac-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The EFP doesn't have a valid MAC address yet.
                This will also get set if the MAC address we
                have is a multicast address.
                ''',
                'no_valid_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('not-in-im', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The EFP has been deleted from IM.
                ''',
                'not_in_im',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offload-mep-direction-not-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP direction does not support offload.
                ''',
                'offload_mep_direction_not_supported',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offload-multiple-local-mep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multiple offloaded MEPs on the same interface
                are not supported.
                ''',
                'offload_multiple_local_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offload-multiple-peer-meps', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP should be offloaded but multiple
                crosscheck MEPs have been configured, and this
                is not supported.
                ''',
                'offload_multiple_peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offload-no-cross-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The MEP should be offloaded but crosscheck has
                not been configured.
                ''',
                'offload_no_cross_check',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offload-out-of-resources', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Offload resource limits have been exceeded
                ''',
                'offload_out_of_resources',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('satellite-capabilities', REFERENCE_CLASS, 'SatelliteCapabilities' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities', 
                [], [], 
                '''                Satellite Capabilities
                ''',
                'satellite_capabilities',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('satellite-error-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error string returned from satellite
                ''',
                'satellite_error_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ID of the satellite
                ''',
                'satellite_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('satellite-limitation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A satellite limitation is preventing MEP being
                offloaded to satellite.
                ''',
                'satellite_limitation',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-bridge-domain', REFERENCE_CLASS, 'ServiceBridgeDomain' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain', 
                [], [], 
                '''                BD/XC ID for the MEP's Service, or Service name
                if the Service is 'down-only'
                ''',
                'service_bridge_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sla-delay-measurement-operations-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In-progress Ethernet SLA delay measurement
                operations are disabled due to satellite having
                delay measurement responder-only capabilities.
                ''',
                'sla_delay_measurement_operations_disabled',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sla-loopback-operations-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In-progress Ethernet SLA loopback operations are
                disabled due to satellite having loopback
                responder-only capabilities.
                ''',
                'sla_loopback_operations_disabled',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sla-synthetic-loss-operations-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In-progress Ethernet SLA synthetic loss
                measurement operations are disabled due to
                satellite having synthetic loss measurement
                responder-only capabilities.
                ''',
                'sla_synthetic_loss_operations_disabled',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mep-configuration-error',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.MepConfigurationErrors' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.MepConfigurationErrors',
            False, 
            [
            _MetaInfoClassMember('mep-configuration-error', REFERENCE_LIST, 'MepConfigurationError' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors.MepConfigurationError', 
                [], [], 
                '''                Information about a particular configuration
                error
                ''',
                'mep_configuration_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mep-configuration-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState',
            False, 
            [
            _MetaInfoClassMember('invalid-ccm-interval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid CCM interval
                ''',
                'invalid_ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid level
                ''',
                'invalid_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-maid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid MAID
                ''',
                'invalid_maid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('loss-threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Timed out (loss threshold exceeded)
                ''',
                'loss_threshold_exceeded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loop detected (our MAC address received)
                ''',
                'received_our_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mep-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configuration Error (our MEP ID received)
                ''',
                'received_our_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-rdi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote defection indication received
                ''',
                'received_rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'error-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName',
            False, 
            [
            _MetaInfoClassMember('integer', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Integer
                ''',
                'integer',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mac-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid',
            False, 
            [
            _MetaInfoClassMember('dns-like-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DNS-like name
                ''',
                'dns_like_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-name', REFERENCE_CLASS, 'MacName' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName', 
                [], [], 
                '''                MAC address name
                ''',
                'mac_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-data', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hex data
                ''',
                'mdid_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-format-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                MDIDFormatValue
                ''',
                'mdid_format_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('string-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String name
                ''',
                'string_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mdid',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VPN index
                ''',
                'index',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VPN authority organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'vpn-id-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName',
            False, 
            [
            _MetaInfoClassMember('icc-based', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ICC-based format
                ''',
                'icc_based',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('integer-name', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unsigned integer name
                ''',
                'integer_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-data', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hex data
                ''',
                'short_ma_name_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-format-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ShortMANameFormatValue
                ''',
                'short_ma_name_format_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('string-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String name
                ''',
                'string_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('vlan-id-name', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                VLAN ID name
                ''',
                'vlan_id_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('vpn-id-name', REFERENCE_CLASS, 'VpnIdName' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName', 
                [], [], 
                '''                VPN ID name
                ''',
                'vpn_id_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'short-ma-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmInterval_Enum', 
                [], [], 
                '''                CCM interval
                ''',
                'interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid', REFERENCE_CLASS, 'Mdid' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid', 
                [], [], 
                '''                MDID
                ''',
                'mdid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-format', REFERENCE_ENUM_CLASS, 'CfmBagMdidFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdidFmt_Enum', 
                [], [], 
                '''                MDID Format
                ''',
                'mdid_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('rdi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote defect indicated
                ''',
                'rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                CCM sequence number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name', REFERENCE_CLASS, 'ShortMaName' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName', 
                [], [], 
                '''                Short MA Name
                ''',
                'short_ma_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-format', REFERENCE_ENUM_CLASS, 'CfmBagSmanFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagSmanFmt_Enum', 
                [], [], 
                '''                Short MA Name format
                ''',
                'short_ma_name_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MEP name
                ''',
                'name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mep-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Chassis ID
                ''',
                'chassis_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis ID String
                ''',
                'chassis_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt_Enum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived',
            False, 
            [
            _MetaInfoClassMember('additional-interface-status', REFERENCE_ENUM_CLASS, 'CfmPmAddlIntfStatus_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAddlIntfStatus_Enum', 
                [], [], 
                '''                Additional interface status
                ''',
                'additional_interface_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'CfmPmIntfStatus_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIntfStatus_Enum', 
                [], [], 
                '''                Interface status
                ''',
                'interface_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-name', REFERENCE_CLASS, 'MepName' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName', 
                [], [], 
                '''                MEP name
                ''',
                'mep_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-status', REFERENCE_ENUM_CLASS, 'CfmPmPortStatus_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortStatus_Enum', 
                [], [], 
                '''                Port status
                ''',
                'port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-ccm-received',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-up-down-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-ccm-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics',
            False, 
            [
            _MetaInfoClassMember('ccms-invalid-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with an invalid interval
                ''',
                'ccms_invalid_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-invalid-maid', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with an invalid MAID
                ''',
                'ccms_invalid_maid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-invalid-source-mac-address', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with an invalid source
                MAC address
                ''',
                'ccms_invalid_source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-our-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with our MEP ID
                ''',
                'ccms_our_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received out-of-sequence
                ''',
                'ccms_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-rdi', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with the Remote Defect
                Indication bit set
                ''',
                'ccms_rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received
                ''',
                'ccms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-wrong-level', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of CCMs received with an invalid level
                ''',
                'ccms_wrong_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-received-time', REFERENCE_CLASS, 'LastCcmReceivedTime' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime', 
                [], [], 
                '''                Elapsed time since last CCM received
                ''',
                'last_ccm_received_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Sequence number of last CCM received
                ''',
                'last_ccm_sequence_number',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep.PeerMep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep.PeerMep',
            False, 
            [
            _MetaInfoClassMember('ccm-offload', REFERENCE_ENUM_CLASS, 'CfmBagCcmOffload_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffload_Enum', 
                [], [], 
                '''                Offload status of received CCM handling
                ''',
                'ccm_offload',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('cross-check-state', REFERENCE_ENUM_CLASS, 'CfmPmRmepXcState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepXcState_Enum', 
                [], [], 
                '''                Cross-check state
                ''',
                'cross_check_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_CLASS, 'ErrorState' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState', 
                [], [], 
                '''                Error state
                ''',
                'error_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-received', REFERENCE_CLASS, 'LastCcmReceived' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived', 
                [], [], 
                '''                Last CCM received from the peer MEP
                ''',
                'last_ccm_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-up-down-time', REFERENCE_CLASS, 'LastUpDownTime' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime', 
                [], [], 
                '''                Elapsed time since peer MEP became active or
                timed out
                ''',
                'last_up_down_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-mep-state', REFERENCE_ENUM_CLASS, 'CfmPmRmepState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepState_Enum', 
                [], [], 
                '''                State of the peer MEP state machine
                ''',
                'peer_mep_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics', 
                [], [], 
                '''                Peer MEP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps.PeerMep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps.PeerMep',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('local-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID of Local MEP
                ''',
                'local_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('peer-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Peer MAC address
                ''',
                'peer_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('peer-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID of Peer MEP
                ''',
                'peer_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('domain-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-direction', REFERENCE_ENUM_CLASS, 'CfmBagDirection_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection_Enum', 
                [], [], 
                '''                MEP facing direction
                ''',
                'mep_direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-mep', REFERENCE_CLASS, 'PeerMep' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep.PeerMep', 
                [], [], 
                '''                Peer MEP
                ''',
                'peer_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The local MEP is on a standby bundle interface
                ''',
                'standby',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.PeerMeps' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.PeerMeps',
            False, 
            [
            _MetaInfoClassMember('peer-mep', REFERENCE_LIST, 'PeerMep' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps.PeerMep', 
                [], [], 
                '''                Information about a peer MEP for a particular
                local MEP
                ''',
                'peer_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-meps',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header',
            False, 
            [
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel_Enum', 
                [], [], 
                '''                Delay Model
                ''',
                'delay_model',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('forwarded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ELR was forwarded
                ''',
                'forwarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-hop-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Next Hop Timeout, in seconds
                ''',
                'next_hop_timeout',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('relay-action', REFERENCE_ENUM_CLASS, 'CfmPmElrRelayAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrRelayAction_Enum', 
                [], [], 
                '''                Relay action
                ''',
                'relay_action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-filter-unknown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Reply Filter unrecognized
                ''',
                'reply_filter_unknown',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('terminal-mep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Terminal MEP reached
                ''',
                'terminal_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId', 
                [], [], 
                '''                Egress ID
                ''',
                'egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop-format', REFERENCE_ENUM_CLASS, 'CfmPmLastHopFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmt_Enum', 
                [], [], 
                '''                LastHopFormat
                ''',
                'last_hop_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Port ID
                ''',
                'port_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port ID String
                ''',
                'port_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt_Enum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmElrEgressAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrEgressAction_Enum', 
                [], [], 
                '''                Reply egress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId', 
                [], [], 
                '''                Last Egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of egress interface
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId', 
                [], [], 
                '''                Next Egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-egress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Port ID
                ''',
                'port_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port ID String
                ''',
                'port_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt_Enum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmElrIngressAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrIngressAction_Enum', 
                [], [], 
                '''                ELR Reply ingress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId', 
                [], [], 
                '''                Last egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId', 
                [], [], 
                '''                Next egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Chassis ID
                ''',
                'chassis_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis ID String
                ''',
                'chassis_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt_Enum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop', REFERENCE_CLASS, 'LastHop' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop', 
                [], [], 
                '''                Last hop ID
                ''',
                'last_hop',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-egress', REFERENCE_CLASS, 'ReplyEgress' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress', 
                [], [], 
                '''                Reply egress TLV
                ''',
                'reply_egress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-ingress', REFERENCE_CLASS, 'ReplyIngress' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress', 
                [], [], 
                '''                Reply ingress TLV
                ''',
                'reply_ingress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-linktrace-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId',
            False, 
            [
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId', 
                [], [], 
                '''                Last egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId', 
                [], [], 
                '''                Next egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header',
            False, 
            [
            _MetaInfoClassMember('forwarded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LTR was forwarded
                ''',
                'forwarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('relay-action', REFERENCE_ENUM_CLASS, 'CfmPmRelayAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRelayAction_Enum', 
                [], [], 
                '''                Relay action
                ''',
                'relay_action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('terminal-mep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Terminal MEP reached
                ''',
                'terminal_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('use-fdb-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use filtering DB only
                ''',
                'use_fdb_only',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId', 
                [], [], 
                '''                Egress ID
                ''',
                'egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop-format', REFERENCE_ENUM_CLASS, 'CfmPmLastHopFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmt_Enum', 
                [], [], 
                '''                LastHopFormat
                ''',
                'last_hop_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Port ID
                ''',
                'port_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port ID String
                ''',
                'port_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt_Enum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmEgressAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEgressAction_Enum', 
                [], [], 
                '''                Reply egress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-egress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Port ID
                ''',
                'port_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port ID String
                ''',
                'port_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmt_Enum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmIngressAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIngressAction_Enum', 
                [], [], 
                '''                Reply ingress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmt_Enum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Raw Chassis ID
                ''',
                'chassis_id_raw',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis ID String
                ''',
                'chassis_id_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmt_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmt_Enum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId', 
                [], [], 
                '''                Egress ID TLV
                ''',
                'egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop', REFERENCE_CLASS, 'LastHop' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop', 
                [], [], 
                '''                Last hop ID
                ''',
                'last_hop',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-egress', REFERENCE_CLASS, 'ReplyEgress' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress', 
                [], [], 
                '''                Reply egress TLV
                ''',
                'reply_egress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-ingress', REFERENCE_CLASS, 'ReplyIngress' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress', 
                [], [], 
                '''                Reply ingress TLV
                ''',
                'reply_ingress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'linktrace-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions',
            False, 
            [
            _MetaInfoClassMember('fdb-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only use the Filtering Database for forwarding
                lookups
                ''',
                'fdb_only',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('is-auto', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Traceroute was initiated automatically
                ''',
                'is_auto',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'basic-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions',
            False, 
            [
            _MetaInfoClassMember('delay-constant-factor', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Constant Factor for delay calculations
                ''',
                'delay_constant_factor',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModel_Enum', 
                [], [], 
                '''                Delay model for delay calculations
                ''',
                'delay_model',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-filter', REFERENCE_ENUM_CLASS, 'CfmPmElmReplyFilter_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilter_Enum', 
                [], [], 
                '''                Reply Filtering mode used by responders
                ''',
                'reply_filter',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options',
            False, 
            [
            _MetaInfoClassMember('basic-options', REFERENCE_CLASS, 'BasicOptions' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions', 
                [], [], 
                '''                Options for a basic IEEE 802.1ag Linktrace
                ''',
                'basic_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('exploratory-options', REFERENCE_CLASS, 'ExploratoryOptions' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions', 
                [], [], 
                '''                Options for an Exploratory Linktrace
                ''',
                'exploratory_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'CfmPmLtMode_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtMode_Enum', 
                [], [], 
                '''                Mode
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation',
            False, 
            [
            _MetaInfoClassMember('directed-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Directed MAC address
                ''',
                'directed_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options', 
                [], [], 
                '''                Options affecting traceroute behavior
                ''',
                'options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service name
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address
                ''',
                'source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Source MEP ID
                ''',
                'source_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Target MAC address
                ''',
                'target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Target MEP ID
                ''',
                'target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Timestamp of initiation time (seconds)
                ''',
                'timestamp',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Time to live
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches.TracerouteCache' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches.TracerouteCache',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('exploratory-linktrace-reply', REFERENCE_LIST, 'ExploratoryLinktraceReply' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply', 
                [], [], 
                '''                Received exploratory linktrace replies
                ''',
                'exploratory_linktrace_reply',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('linktrace-reply', REFERENCE_LIST, 'LinktraceReply' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply', 
                [], [], 
                '''                Received linktrace replies
                ''',
                'linktrace_reply',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('replies-dropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of ignored replies for this request
                ''',
                'replies_dropped',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-information', REFERENCE_CLASS, 'TracerouteInformation' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation', 
                [], [], 
                '''                Information about the traceroute operation
                ''',
                'traceroute_information',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global.TracerouteCaches' : {
        'meta_info' : _MetaInfoClass('Cfm.Global.TracerouteCaches',
            False, 
            [
            _MetaInfoClassMember('traceroute-cache', REFERENCE_LIST, 'TracerouteCache' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches.TracerouteCache', 
                [], [], 
                '''                Information about a particular traceroute
                operation
                ''',
                'traceroute_cache',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-caches',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global' : {
        'meta_info' : _MetaInfoClass('Cfm.Global',
            False, 
            [
            _MetaInfoClassMember('global-configuration-errors', REFERENCE_CLASS, 'GlobalConfigurationErrors' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.GlobalConfigurationErrors', 
                [], [], 
                '''                Global configuration errors table
                ''',
                'global_configuration_errors',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('incomplete-traceroutes', REFERENCE_CLASS, 'IncompleteTraceroutes' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.IncompleteTraceroutes', 
                [], [], 
                '''                Incomplete Traceroute table
                ''',
                'incomplete_traceroutes',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-meps', REFERENCE_CLASS, 'LocalMeps' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.LocalMeps', 
                [], [], 
                '''                Local MEPs table
                ''',
                'local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-points', REFERENCE_CLASS, 'MaintenancePoints' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MaintenancePoints', 
                [], [], 
                '''                Maintenance Points table
                ''',
                'maintenance_points',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-configuration-errors', REFERENCE_CLASS, 'MepConfigurationErrors' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.MepConfigurationErrors', 
                [], [], 
                '''                MEP configuration errors table
                ''',
                'mep_configuration_errors',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps', REFERENCE_CLASS, 'PeerMeps' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.PeerMeps', 
                [], [], 
                '''                Peer MEPs table
                ''',
                'peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-caches', REFERENCE_CLASS, 'TracerouteCaches' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global.TracerouteCaches', 
                [], [], 
                '''                Traceroute Cache table
                ''',
                'traceroute_caches',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('domain-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ingress-interface', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The XID of the ingress interface for the CCM
                ''',
                'ingress_interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ingress-interface-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the Bridge Domain or
                Cross-Connect associated with the ingress XID
                ''',
                'ingress_interface_string',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('service-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance association name
                ''',
                'service_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address
                ''',
                'source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The XID is stale and may have been reused for a
                different interface
                ''',
                'stale',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ccm-learning-database',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.CcmLearningDatabases' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.CcmLearningDatabases',
            False, 
            [
            _MetaInfoClassMember('ccm-learning-database', REFERENCE_LIST, 'CcmLearningDatabase' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase', 
                [], [], 
                '''                CCM Learning Database entry
                ''',
                'ccm_learning_database',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ccm-learning-databases',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects',
            False, 
            [
            _MetaInfoClassMember('invalid-ccm-interval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid CCM interval
                ''',
                'invalid_ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid level
                ''',
                'invalid_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('invalid-maid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Invalid MAID
                ''',
                'invalid_maid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('loss-threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Timed out (loss threshold exceeded)
                ''',
                'loss_threshold_exceeded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loop detected (our MAC address received)
                ''',
                'received_our_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-our-mep-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configuration Error (our MEP ID received)
                ''',
                'received_our_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('received-rdi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote defection indication received
                ''',
                'received_rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'remote-meps-defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects',
            False, 
            [
            _MetaInfoClassMember('ais-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AIS or LCK received
                ''',
                'ais_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('auto-missing', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of missing auto cross-check MEPs
                ''',
                'auto_missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-port-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The local port or interface is down
                ''',
                'local_port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('missing', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of missing peer MEPs
                ''',
                'missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-that-timed-out', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of peer MEPs that have timed out
                ''',
                'peer_meps_that_timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-port-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A peer port or interface is down
                ''',
                'peer_port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('remote-meps-defects', REFERENCE_CLASS, 'RemoteMepsDefects' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects', 
                [], [], 
                '''                Defects detected from remote MEPs
                ''',
                'remote_meps_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unexpected', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unexpected peer MEPs
                ''',
                'unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-started',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics',
            False, 
            [
            _MetaInfoClassMember('defects', REFERENCE_CLASS, 'Defects' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects', 
                [], [], 
                '''                Defects detected
                ''',
                'defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'CfmBagDirection_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirection_Enum', 
                [], [], 
                '''                Direction of AIS packets
                ''',
                'direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-started', REFERENCE_CLASS, 'LastStarted' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted', 
                [], [], 
                '''                Time elapsed since sending last started
                ''',
                'last_started',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lowest-level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Level of the lowest MEP transmitting AIS
                ''',
                'lowest_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sent-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of packets sent by the transmitting
                MEP
                ''',
                'sent_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transmission-interval', REFERENCE_ENUM_CLASS, 'CfmBagAisInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisInterval_Enum', 
                [], [], 
                '''                Interval at which AIS packets are transmitted
                ''',
                'transmission_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transmission-level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Level that AIS packets are transmitted on
                ''',
                'transmission_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('via-level', REFERENCE_LEAFLIST, 'CfmBagMdLevel_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevel_Enum', 
                [], [], 
                '''                Levels of other MEPs receiving AIS
                ''',
                'via_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'CfmAisDir_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmAisDir_Enum', 
                [], [], 
                '''                AIS Direction
                ''',
                'direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IM Interface state
                ''',
                'interface_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interworking-state', REFERENCE_ENUM_CLASS, 'CfmBagIwState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwState_Enum', 
                [], [], 
                '''                Interface interworking state
                ''',
                'interworking_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics', 
                [], [], 
                '''                AIS statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('stp-state', REFERENCE_ENUM_CLASS, 'CfmBagStpState_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpState_Enum', 
                [], [], 
                '''                STP state
                ''',
                'stp_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-ais',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises',
            False, 
            [
            _MetaInfoClassMember('interface-ais', REFERENCE_LIST, 'InterfaceAis' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis', 
                [], [], 
                '''                AIS statistics for a particular interface
                ''',
                'interface_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-aises',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of packets dropped at this EFP
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-malformed-opcode', REFERENCE_ENUM_CLASS, 'CfmBagOpcode_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagOpcode_Enum', 
                [], [], 
                '''                Opcode for last malformed packet
                ''',
                'last_malformed_opcode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-malformed-reason', REFERENCE_ENUM_CLASS, 'CfmPmPktAction_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPktAction_Enum', 
                [], [], 
                '''                Reason last malformed packet was malformed
                ''',
                'last_malformed_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('malformed-packets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of malformed packets received at this EFP
                ''',
                'malformed_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics', 
                [], [], 
                '''                EFP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics',
            False, 
            [
            _MetaInfoClassMember('interface-statistic', REFERENCE_LIST, 'InterfaceStatistic' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic', 
                [], [], 
                '''                Counters for a particular interface
                ''',
                'interface_statistic',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('bnm-enabled-links', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of BNM Enabled Links
                ''',
                'bnm_enabled_links',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bridge-domains-and-xconnects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number or bridge domains and crossconnects.
                ''',
                'bridge_domains_and_xconnects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-learning-db-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of entries in the CCM learning database.
                ''',
                'ccm_learning_db_entries',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The combined rate of CCMs on this card.
                ''',
                'ccm_rate',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-misconfigured', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local MEPs disabled due to
                configuration errors.
                ''',
                'disabled_misconfigured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-operational-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local MEPs disabled due to
                operational errors.
                ''',
                'disabled_operational_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-out-of-resources', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local MEPs disabled due to lack of
                resources.
                ''',
                'disabled_out_of_resources',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domains', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of domains in the CFM database.
                ''',
                'domains',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('down-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of down-MEPs.
                ''',
                'down_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces running CFM.
                ''',
                'interfaces',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('issu-role', REFERENCE_ENUM_CLASS, 'CfmBagIssuRole_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIssuRole_Enum', 
                [], [], 
                '''                ISSU Role of CFM-D, if any.
                ''',
                'issu_role',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local MEPs in the CFM database.
                ''',
                'local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mips', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MIPs
                ''',
                'mips',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MEPs for which CCM processing has
                been offloaded.
                ''',
                'offloaded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded-at10ms', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MEPs offloaded with CCMs at 10ms
                intervals.
                ''',
                'offloaded_at10ms',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded-at3-3ms', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MEPs offloaded with CCMs at 3.3ms
                intervals.
                ''',
                'offloaded_at3_3ms',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('operational-local-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of operational local MEPs.
                ''',
                'operational_local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('operational-peer-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of operational peer MEPs recorded in
                the CFM database.
                ''',
                'operational_peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of peer MEPs.
                ''',
                'peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-timed-out', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of peer MEPs that have timed out.
                ''',
                'peer_meps_timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-with-defects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of peer MEPs with defects.
                ''',
                'peer_meps_with_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-without-defects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of peer MEPs without defects.
                ''',
                'peer_meps_without_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('services', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of services in the CFM database.
                ''',
                'services',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-cache-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of traceroute cache entries.
                ''',
                'traceroute_cache_entries',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-cache-replies', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of traceroute cache replies.
                ''',
                'traceroute_cache_replies',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('up-meps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of up-MEPs.
                ''',
                'up_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('ccm-learning-databases', REFERENCE_CLASS, 'CcmLearningDatabases' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.CcmLearningDatabases', 
                [], [], 
                '''                CCMLearningDatabase table
                ''',
                'ccm_learning_databases',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-aises', REFERENCE_CLASS, 'InterfaceAises' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises', 
                [], [], 
                '''                Interface AIS table
                ''',
                'interface_aises',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-statistics', REFERENCE_CLASS, 'InterfaceStatistics' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics', 
                [], [], 
                '''                Interface Statistics table
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.Summary', 
                [], [], 
                '''                Summary
                ''',
                'summary',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node', 
                [], [], 
                '''                Node-specific data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm' : {
        'meta_info' : _MetaInfoClass('Cfm',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global', 
                [], [], 
                '''                Global operational data
                ''',
                'global_',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes', 
                [], [], 
                '''                Node table for node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'cfm',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
}
_meta_table['Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId']['meta_info'].parent =_meta_table['Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info']
_meta_table['Cfm.Global.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info'].parent =_meta_table['Cfm.Global.GlobalConfigurationErrors']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions']['meta_info'].parent =_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions']['meta_info'].parent =_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info'].parent =_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info'].parent =_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes.IncompleteTraceroute']['meta_info'].parent =_meta_table['Cfm.Global.IncompleteTraceroutes']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics.ReceivingStart']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics.SendingStart']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.Defects.RemoteMepsDefects']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep.Defects']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.AisStatistics']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.Defects']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep.Statistics']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global.LocalMeps.LocalMep']['meta_info'].parent =_meta_table['Cfm.Global.LocalMeps']['meta_info']
_meta_table['Cfm.Global.MaintenancePoints.MaintenancePoint.MaintenancePoint']['meta_info'].parent =_meta_table['Cfm.Global.MaintenancePoints.MaintenancePoint']['meta_info']
_meta_table['Cfm.Global.MaintenancePoints.MaintenancePoint']['meta_info'].parent =_meta_table['Cfm.Global.MaintenancePoints']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.Mep']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors.MepConfigurationError']['meta_info'].parent =_meta_table['Cfm.Global.MepConfigurationErrors']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid.MacName']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.Mdid']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.Header']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.MepName']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.SenderId']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics.LastCcmReceivedTime']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.ErrorState']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastCcmReceived']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.LastUpDownTime']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep.Statistics']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep.PeerMep']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps.PeerMep']['meta_info']
_meta_table['Cfm.Global.PeerMeps.PeerMep']['meta_info'].parent =_meta_table['Cfm.Global.PeerMeps']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.Header']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches.TracerouteCache']['meta_info'].parent =_meta_table['Cfm.Global.TracerouteCaches']['meta_info']
_meta_table['Cfm.Global.GlobalConfigurationErrors']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.IncompleteTraceroutes']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.LocalMeps']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.MaintenancePoints']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.MepConfigurationErrors']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.PeerMeps']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Global.TracerouteCaches']['meta_info'].parent =_meta_table['Cfm.Global']['meta_info']
_meta_table['Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info']
_meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.Summary']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node']['meta_info'].parent =_meta_table['Cfm.Nodes']['meta_info']
_meta_table['Cfm.Global']['meta_info'].parent =_meta_table['Cfm']['meta_info']
_meta_table['Cfm.Nodes']['meta_info'].parent =_meta_table['Cfm']['meta_info']

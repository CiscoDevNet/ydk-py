


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CfmPmRmepXcStateEnum' : _MetaInfoEnum('CfmPmRmepXcStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'cross-check-ok':'cross_check_ok',
            'cross-check-missing':'cross_check_missing',
            'cross-check-extra':'cross_check_extra',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagAisIntervalEnum' : _MetaInfoEnum('CfmBagAisIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'ais-interval-none':'ais_interval_none',
            'ais-interval1s':'ais_interval1s',
            'ais-interval1m':'ais_interval1m',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmAisDirEnum' : _MetaInfoEnum('CfmAisDirEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmChassisIdFmtEnum' : _MetaInfoEnum('CfmPmChassisIdFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'chassis-id-chassis-component':'chassis_id_chassis_component',
            'chassis-id-interface-alias':'chassis_id_interface_alias',
            'chassis-id-port-component':'chassis_id_port_component',
            'chassis-id-mac-address':'chassis_id_mac_address',
            'chassis-id-network-address':'chassis_id_network_address',
            'chassis-id-interface-name':'chassis_id_interface_name',
            'chassis-id-local':'chassis_id_local',
            'chassis-id-unknown-type':'chassis_id_unknown_type',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElmReplyFilterEnum' : _MetaInfoEnum('CfmPmElmReplyFilterEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'reply-filter-not-present':'reply_filter_not_present',
            'reply-filter-default':'reply_filter_default',
            'reply-filter-vlan-topology':'reply_filter_vlan_topology',
            'reply-filter-spanning-tree':'reply_filter_spanning_tree',
            'reply-filter-all-ports':'reply_filter_all_ports',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperBucketEnum' : _MetaInfoEnum('SlaOperBucketEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'bucket-type-bins':'bucket_type_bins',
            'bucket-type-samples':'bucket_type_samples',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIntfStatusEnum' : _MetaInfoEnum('CfmPmIntfStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interface-status-up':'interface_status_up',
            'interface-status-down':'interface_status_down',
            'interface-status-testing':'interface_status_testing',
            'interface-status-unknown':'interface_status_unknown',
            'interface-status-dormant':'interface_status_dormant',
            'interface-status-not-present':'interface_status_not_present',
            'interface-status-lower-layer-down':'interface_status_lower_layer_down',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElrRelayActionEnum' : _MetaInfoEnum('CfmPmElrRelayActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-relay-hit':'elr_relay_hit',
            'elr-relay-fdb':'elr_relay_fdb',
            'elr-relay-flood':'elr_relay_flood',
            'elr-relay-drop':'elr_relay_drop',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagMdLevelEnum' : _MetaInfoEnum('CfmBagMdLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'level0':'level0',
            'level1':'level1',
            'level2':'level2',
            'level3':'level3',
            'level4':'level4',
            'level5':'level5',
            'level6':'level6',
            'level7':'level7',
            'level-invalid':'level_invalid',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmEltDelayModelEnum' : _MetaInfoEnum('CfmPmEltDelayModelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'delay-model-invalid':'delay_model_invalid',
            'delay-model-logarithmic':'delay_model_logarithmic',
            'delay-model-constant':'delay_model_constant',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagIwStateEnum' : _MetaInfoEnum('CfmBagIwStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interworking-up':'interworking_up',
            'interworking-test':'interworking_test',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaBucketSizeEnum' : _MetaInfoEnum('SlaBucketSizeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'buckets-per-probe':'buckets_per_probe',
            'probes-per-bucket':'probes_per_bucket',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperOperationEnum' : _MetaInfoEnum('SlaOperOperationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'operation-type-configured':'operation_type_configured',
            'operation-type-ondemand':'operation_type_ondemand',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagStpStateEnum' : _MetaInfoEnum('CfmBagStpStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'stp-up':'stp_up',
            'stp-blocked':'stp_blocked',
            'stp-unknown':'stp_unknown',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmEgressActionEnum' : _MetaInfoEnum('CfmPmEgressActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'egress-ok':'egress_ok',
            'egress-down':'egress_down',
            'egress-blocked':'egress_blocked',
            'egress-vid':'egress_vid',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagCcmIntervalEnum' : _MetaInfoEnum('CfmBagCcmIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'interval-none':'interval_none',
            'interval3-3ms':'interval3_3ms',
            'interval10ms':'interval10ms',
            'interval100ms':'interval100ms',
            'interval1s':'interval1s',
            'interval10s':'interval10s',
            'interval1m':'interval1m',
            'interval10m':'interval10m',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElrEgressActionEnum' : _MetaInfoEnum('CfmPmElrEgressActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-egress-ok':'elr_egress_ok',
            'elr-egress-down':'elr_egress_down',
            'elr-egress-blocked':'elr_egress_blocked',
            'elr-egress-vid':'elr_egress_vid',
            'elr-egress-mac':'elr_egress_mac',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPktActionEnum' : _MetaInfoEnum('CfmPmPktActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'packet-processed':'packet_processed',
            'packet-forwarded':'packet_forwarded',
            'unknown-opcode':'unknown_opcode',
            'filter-level':'filter_level',
            'filter-blocked':'filter_blocked',
            'filter-local-mac':'filter_local_mac',
            'malformed-ccm-size':'malformed_ccm_size',
            'malformed-ccm-mep-id':'malformed_ccm_mep_id',
            'malformed-too-short':'malformed_too_short',
            'malformed-destination-mac-unicast':'malformed_destination_mac_unicast',
            'malformed-destination-mac-multicast':'malformed_destination_mac_multicast',
            'malformed-tlv-offset':'malformed_tlv_offset',
            'malformed-lbm-source-mac':'malformed_lbm_source_mac',
            'malformed-ltr-relay-action':'malformed_ltr_relay_action',
            'malformed-ltr-reply-tlv':'malformed_ltr_reply_tlv',
            'malformed-lt-origin':'malformed_lt_origin',
            'malformed-ltm-target':'malformed_ltm_target',
            'malformed-source-mac':'malformed_source_mac',
            'malformed-header-too-short':'malformed_header_too_short',
            'malformed-tlv-header-overrun':'malformed_tlv_header_overrun',
            'malformed-tlv-overrun':'malformed_tlv_overrun',
            'malformed-duplicate-sender-id':'malformed_duplicate_sender_id',
            'malformed-duplicate-port-status':'malformed_duplicate_port_status',
            'malformed-duplicate-interface-status':'malformed_duplicate_interface_status',
            'malformed-wrong-tlv':'malformed_wrong_tlv',
            'malformed-duplicate-data':'malformed_duplicate_data',
            'malformed-duplicate-ltr-egress-id':'malformed_duplicate_ltr_egress_id',
            'malformed-duplicate-reply-ingress':'malformed_duplicate_reply_ingress',
            'malformed-duplicate-reply-egress':'malformed_duplicate_reply_egress',
            'malformed-duplicate-ltm-egress-id':'malformed_duplicate_ltm_egress_id',
            'malformed-sender-id-size':'malformed_sender_id_size',
            'malformed-chassis-id-size':'malformed_chassis_id_size',
            'malformed-mgmt-address-domain-size':'malformed_mgmt_address_domain_size',
            'malformed-mgmt-address-size':'malformed_mgmt_address_size',
            'malformed-port-status-size':'malformed_port_status_size',
            'malformed-port-status':'malformed_port_status',
            'malformed-interface-status-size':'malformed_interface_status_size',
            'malformed-interface-status':'malformed_interface_status',
            'malformed-organization-specific-tlv-size':'malformed_organization_specific_tlv_size',
            'malformed-duplicate-mep-name':'malformed_duplicate_mep_name',
            'malformed-duplicate-additional-interface-status':'malformed_duplicate_additional_interface_status',
            'malformed-ltr-egress-id-size':'malformed_ltr_egress_id_size',
            'malformed-reply-ingress-size':'malformed_reply_ingress_size',
            'malformed-ingress-action':'malformed_ingress_action',
            'malformed-reply-ingress-mac':'malformed_reply_ingress_mac',
            'malformed-ingress-port-length-size':'malformed_ingress_port_length_size',
            'malformed-ingress-port-id-length':'malformed_ingress_port_id_length',
            'malformed-ingress-port-id-size':'malformed_ingress_port_id_size',
            'malformed-reply-egress-size':'malformed_reply_egress_size',
            'malformed-egress-action':'malformed_egress_action',
            'malformed-reply-egress-mac':'malformed_reply_egress_mac',
            'malformed-egress-port-length-size':'malformed_egress_port_length_size',
            'malformed-egress-port-id-length':'malformed_egress_port_id_length',
            'malformed-egress-port-id-size':'malformed_egress_port_id_size',
            'malformed-ltm-egress-id-size':'malformed_ltm_egress_id_size',
            'malformed-mep-name-size':'malformed_mep_name_size',
            'malformed-mep-name-name-length':'malformed_mep_name_name_length',
            'malformed-additional-interface-status-size':'malformed_additional_interface_status_size',
            'malformed-additional-interface-status':'malformed_additional_interface_status',
            'malformed-ccm-interval':'malformed_ccm_interval',
            'malformed-mdid-mac-address-length':'malformed_mdid_mac_address_length',
            'malformed-mdid-length':'malformed_mdid_length',
            'malformed-sman-length':'malformed_sman_length',
            'malformed-sman2-byte-length':'malformed_sman2_byte_length',
            'malformed-sman-vpn-id-length':'malformed_sman_vpn_id_length',
            'malformed-elr-no-reply-tlv':'malformed_elr_no_reply_tlv',
            'malformed-separate-elr-reply-egress':'malformed_separate_elr_reply_egress',
            'malformed-dcm-destination-multicast':'malformed_dcm_destination_multicast',
            'malformed-dcm-embed-length':'malformed_dcm_embed_length',
            'malformed-dcm-embed-level':'malformed_dcm_embed_level',
            'malformed-dcm-embed-version':'malformed_dcm_embed_version',
            'malformed-elr-relay-action':'malformed_elr_relay_action',
            'malformed-elr-tt-ls':'malformed_elr_tt_ls',
            'malformed-elr-ttl-ingress':'malformed_elr_ttl_ingress',
            'malformed-elr-ttl-egress':'malformed_elr_ttl_egress',
            'malformed-elm-destination-unicast':'malformed_elm_destination_unicast',
            'malformed-elm-egress-id':'malformed_elm_egress_id',
            'malformed-dcm-embed-oui':'malformed_dcm_embed_oui',
            'malformed-dcm-embed-opcode':'malformed_dcm_embed_opcode',
            'malformed-elm-constant-zero':'malformed_elm_constant_zero',
            'malformed-elr-timeout-zero':'malformed_elr_timeout_zero',
            'malformed-duplicate-test':'malformed_duplicate_test',
            'malformed-dmm-source-mac':'malformed_dmm_source_mac',
            'malformed-test-size':'malformed_test_size',
            'malformed-dmr-time-stamps':'malformed_dmr_time_stamps',
            'malformed-dm-time-stamp-fmt':'malformed_dm_time_stamp_fmt',
            'malformed-ais-interval':'malformed_ais_interval',
            'filter-interface-down':'filter_interface_down',
            'filter-forward-standby':'filter_forward_standby',
            'malformed-sman-icc-based-length':'malformed_sman_icc_based_length',
            'filter-foward-issu-secondary':'filter_foward_issu_secondary',
            'filter-response-standby':'filter_response_standby',
            'filter-response-issu-secondary':'filter_response_issu_secondary',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPortStatusEnum' : _MetaInfoEnum('CfmPmPortStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'port-status-blocked':'port_status_blocked',
            'port-status-up':'port_status_up',
            'port-status-unknown':'port_status_unknown',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagMdidFmtEnum' : _MetaInfoEnum('CfmBagMdidFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'mdid-null':'mdid_null',
            'mdid-dns-like':'mdid_dns_like',
            'mdid-mac-address':'mdid_mac_address',
            'mdid-string':'mdid_string',
            'mdid-unknown':'mdid_unknown',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagBdidFmtEnum' : _MetaInfoEnum('CfmBagBdidFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'invalid':'invalid',
            'bd-id':'bd_id',
            'xc-p2p-id':'xc_p2p_id',
            'xc-mp2mp-id':'xc_mp2mp_id',
            'down-only':'down_only',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmMepDefectEnum' : _MetaInfoEnum('CfmPmMepDefectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'defect-none':'defect_none',
            'defect-rdi-ccm':'defect_rdi_ccm',
            'defect-ma-cstatus':'defect_ma_cstatus',
            'defect-remote-ccm':'defect_remote_ccm',
            'defect-error-ccm':'defect_error_ccm',
            'defect-cross-connect-ccm':'defect_cross_connect_ccm',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmMaMpVarietyEnum' : _MetaInfoEnum('CfmMaMpVarietyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'mip':'mip',
            'up-mep':'up_mep',
            'downmep':'downmep',
            'unknown-mep':'unknown_mep',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagOpcodeEnum' : _MetaInfoEnum('CfmBagOpcodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'reserved':'reserved',
            'ccm':'ccm',
            'lbr':'lbr',
            'lbm':'lbm',
            'ltr':'ltr',
            'ltm':'ltm',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperPacketPriorityEnum' : _MetaInfoEnum('SlaOperPacketPriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'priority-none':'priority_none',
            'priority-cos':'priority_cos',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagCcmOffloadEnum' : _MetaInfoEnum('CfmBagCcmOffloadEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'offload-none':'offload_none',
            'offload-software':'offload_software',
            'offload-hardware':'offload_hardware',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIdFmtEnum' : _MetaInfoEnum('CfmPmIdFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'id-format-is-string':'id_format_is_string',
            'id-format-is-mac-address':'id_format_is_mac_address',
            'id-format-is-raw-hex':'id_format_is_raw_hex',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmElrIngressActionEnum' : _MetaInfoEnum('CfmPmElrIngressActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'elr-ingress-ok':'elr_ingress_ok',
            'elr-ingress-down':'elr_ingress_down',
            'elr-ingress-blocked':'elr_ingress_blocked',
            'elr-ingress-vid':'elr_ingress_vid',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAddlIntfStatusEnum' : _MetaInfoEnum('CfmPmAddlIntfStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'unknown':'unknown',
            'administratively-down':'administratively_down',
            'remote-excessive-errors':'remote_excessive_errors',
            'local-excessive-errors':'local_excessive_errors',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaRecordableMetricEnum' : _MetaInfoEnum('SlaRecordableMetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'metric-invalid':'metric_invalid',
            'metric-round-trip-delay':'metric_round_trip_delay',
            'metric-one-way-delay-sd':'metric_one_way_delay_sd',
            'metric-one-way-delay-ds':'metric_one_way_delay_ds',
            'metric-round-trip-jitter':'metric_round_trip_jitter',
            'metric-one-way-jitter-sd':'metric_one_way_jitter_sd',
            'metric-one-way-jitter-ds':'metric_one_way_jitter_ds',
            'metric-one-way-flr-sd':'metric_one_way_flr_sd',
            'metric-one-way-flr-ds':'metric_one_way_flr_ds',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmPortIdFmtEnum' : _MetaInfoEnum('CfmPmPortIdFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'port-id-interface-alias':'port_id_interface_alias',
            'port-id-port-component':'port_id_port_component',
            'port-id-mac-address':'port_id_mac_address',
            'port-id-network-address':'port_id_network_address',
            'port-id-interface-name':'port_id_interface_name',
            'port-id-agent-circuit-id':'port_id_agent_circuit_id',
            'port-id-local':'port_id_local',
            'port-id-unknown':'port_id_unknown',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmRmepStateEnum' : _MetaInfoEnum('CfmPmRmepStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'peer-mep-idle':'peer_mep_idle',
            'peer-mep-start':'peer_mep_start',
            'peer-mep-failed':'peer_mep_failed',
            'peer-mep-ok':'peer_mep_ok',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAisReceiveEnum' : _MetaInfoEnum('CfmPmAisReceiveEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'receive-none':'receive_none',
            'receive-ais':'receive_ais',
            'receive-lck':'receive_lck',
            'receive-direct':'receive_direct',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmIngressActionEnum' : _MetaInfoEnum('CfmPmIngressActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'ingress-ok':'ingress_ok',
            'ingress-down':'ingress_down',
            'ingress-blocked':'ingress_blocked',
            'ingress-vid':'ingress_vid',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmLastHopFmtEnum' : _MetaInfoEnum('CfmPmLastHopFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'last-hop-none':'last_hop_none',
            'last-hop-host-name':'last_hop_host_name',
            'last-hop-egress-id':'last_hop_egress_id',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmAisTransmitEnum' : _MetaInfoEnum('CfmPmAisTransmitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'transmit-none':'transmit_none',
            'transmit-ais':'transmit_ais',
            'transmit-ais-direct':'transmit_ais_direct',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'SlaOperTestPatternSchemeEnum' : _MetaInfoEnum('SlaOperTestPatternSchemeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'hex':'hex',
            'pseudo-random':'pseudo_random',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmMepFngStateEnum' : _MetaInfoEnum('CfmPmMepFngStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'fng-reset':'fng_reset',
            'fng-defect':'fng_defect',
            'fng-report-defect':'fng_report_defect',
            'fng-defect-reported':'fng_defect_reported',
            'fng-defect-clearing':'fng_defect_clearing',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagDirectionEnum' : _MetaInfoEnum('CfmBagDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'direction-up':'direction_up',
            'direction-down':'direction_down',
            'direction-invalid':'direction_invalid',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagSmanFmtEnum' : _MetaInfoEnum('CfmBagSmanFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'sman-vlan-id':'sman_vlan_id',
            'sman-string':'sman_string',
            'sman-uint16':'sman_uint16',
            'sman-vpn-id':'sman_vpn_id',
            'sman-icc':'sman_icc',
            'sman-unknown':'sman_unknown',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmBagIssuRoleEnum' : _MetaInfoEnum('CfmBagIssuRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'unknown':'unknown',
            'primary':'primary',
            'secondary':'secondary',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmLtModeEnum' : _MetaInfoEnum('CfmPmLtModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'cfm-pm-lt-mode-basic':'cfm_pm_lt_mode_basic',
            'cfm-pm-lt-mode-exploratory':'cfm_pm_lt_mode_exploratory',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
    'CfmPmRelayActionEnum' : _MetaInfoEnum('CfmPmRelayActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper',
        {
            'relay-hit':'relay_hit',
            'relay-fdb':'relay_fdb',
            'relay-mpdb':'relay_mpdb',
        }, 'Cisco-IOS-XR-ethernet-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper']),
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Number of missing peer MEPs
                ''',
                'missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-that-timed-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('remote-meps-defects', REFERENCE_CLASS, 'RemoteMepsDefects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects', 
                [], [], 
                '''                Defects detected from remote MEPs
                ''',
                'remote_meps_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unexpected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unexpected peer MEPs
                ''',
                'unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-started',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics',
            False, 
            [
            _MetaInfoClassMember('defects', REFERENCE_CLASS, 'Defects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects', 
                [], [], 
                '''                Defects detected
                ''',
                'defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'CfmBagDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirectionEnum', 
                [], [], 
                '''                Direction of AIS packets
                ''',
                'direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-started', REFERENCE_CLASS, 'LastStarted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted', 
                [], [], 
                '''                Time elapsed since sending last started
                ''',
                'last_started',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lowest-level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Level of the lowest MEP transmitting AIS
                ''',
                'lowest_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets sent by the transmitting
                MEP
                ''',
                'sent_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transmission-interval', REFERENCE_ENUM_CLASS, 'CfmBagAisIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisIntervalEnum', 
                [], [], 
                '''                Interval at which AIS packets are transmitted
                ''',
                'transmission_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transmission-level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Level that AIS packets are transmitted on
                ''',
                'transmission_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('via-level', REFERENCE_LEAFLIST, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Levels of other MEPs receiving AIS
                ''',
                'via_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises.InterfaceAis' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises.InterfaceAis',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'CfmAisDirEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmAisDirEnum', 
                [], [], 
                '''                AIS Direction
                ''',
                'direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
            _MetaInfoClassMember('interworking-state', REFERENCE_ENUM_CLASS, 'CfmBagIwStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwStateEnum', 
                [], [], 
                '''                Interface interworking state
                ''',
                'interworking_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics', 
                [], [], 
                '''                AIS statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('stp-state', REFERENCE_ENUM_CLASS, 'CfmBagStpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpStateEnum', 
                [], [], 
                '''                STP state
                ''',
                'stp_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-ais',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceAises' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceAises',
            False, 
            [
            _MetaInfoClassMember('interface-ais', REFERENCE_LIST, 'InterfaceAis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises.InterfaceAis', 
                [], [], 
                '''                AIS statistics for a particular interface
                ''',
                'interface_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-aises',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped at this EFP
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-malformed-opcode', REFERENCE_ENUM_CLASS, 'CfmBagOpcodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagOpcodeEnum', 
                [], [], 
                '''                Opcode for last malformed packet
                ''',
                'last_malformed_opcode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-malformed-reason', REFERENCE_ENUM_CLASS, 'CfmPmPktActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPktActionEnum', 
                [], [], 
                '''                Reason last malformed packet was malformed
                ''',
                'last_malformed_reason',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('malformed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of malformed packets received at this EFP
                ''',
                'malformed_packets',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics', 
                [], [], 
                '''                EFP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.InterfaceStatistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.InterfaceStatistics',
            False, 
            [
            _MetaInfoClassMember('interface-statistic', REFERENCE_LIST, 'InterfaceStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic', 
                [], [], 
                '''                Counters for a particular interface
                ''',
                'interface_statistic',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('bnm-enabled-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of BNM Enabled Links
                ''',
                'bnm_enabled_links',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bridge-domains-and-xconnects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number or bridge domains and crossconnects.
                ''',
                'bridge_domains_and_xconnects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-learning-db-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries in the CCM learning database.
                ''',
                'ccm_learning_db_entries',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The combined rate of CCMs on this card.
                ''',
                'ccm_rate',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-misconfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of local MEPs disabled due to
                configuration errors.
                ''',
                'disabled_misconfigured',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-operational-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of local MEPs disabled due to
                operational errors.
                ''',
                'disabled_operational_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('disabled-out-of-resources', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of local MEPs disabled due to lack of
                resources.
                ''',
                'disabled_out_of_resources',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('domains', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of domains in the CFM database.
                ''',
                'domains',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('down-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of down-MEPs.
                ''',
                'down_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of interfaces running CFM.
                ''',
                'interfaces',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('issu-role', REFERENCE_ENUM_CLASS, 'CfmBagIssuRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIssuRoleEnum', 
                [], [], 
                '''                ISSU Role of CFM-D, if any.
                ''',
                'issu_role',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of local MEPs in the CFM database.
                ''',
                'local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mips', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MIPs
                ''',
                'mips',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MEPs for which CCM processing has
                been offloaded.
                ''',
                'offloaded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded-at10ms', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MEPs offloaded with CCMs at 10ms
                intervals.
                ''',
                'offloaded_at10ms',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('offloaded-at3-3ms', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of MEPs offloaded with CCMs at 3.3ms
                intervals.
                ''',
                'offloaded_at3_3ms',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('operational-local-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of operational local MEPs.
                ''',
                'operational_local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('operational-peer-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of operational peer MEPs recorded in
                the CFM database.
                ''',
                'operational_peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of peer MEPs.
                ''',
                'peer_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-timed-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of peer MEPs that have timed out.
                ''',
                'peer_meps_timed_out',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-with-defects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of peer MEPs with defects.
                ''',
                'peer_meps_with_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-without-defects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of peer MEPs without defects.
                ''',
                'peer_meps_without_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('services', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of services in the CFM database.
                ''',
                'services',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-cache-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of traceroute cache entries.
                ''',
                'traceroute_cache_entries',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-cache-replies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of traceroute cache replies.
                ''',
                'traceroute_cache_replies',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('up-meps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of up-MEPs.
                ''',
                'up_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('domain-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ingress-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
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
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node.CcmLearningDatabases' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node.CcmLearningDatabases',
            False, 
            [
            _MetaInfoClassMember('ccm-learning-database', REFERENCE_LIST, 'CcmLearningDatabase' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase', 
                [], [], 
                '''                CCM Learning Database entry
                ''',
                'ccm_learning_database',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ccm-learning-databases',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('ccm-learning-databases', REFERENCE_CLASS, 'CcmLearningDatabases' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.CcmLearningDatabases', 
                [], [], 
                '''                CCMLearningDatabase table
                ''',
                'ccm_learning_databases',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-aises', REFERENCE_CLASS, 'InterfaceAises' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceAises', 
                [], [], 
                '''                Interface AIS table
                ''',
                'interface_aises',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-statistics', REFERENCE_CLASS, 'InterfaceStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.InterfaceStatistics', 
                [], [], 
                '''                Interface Statistics table
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node.Summary', 
                [], [], 
                '''                Summary
                ''',
                'summary',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Nodes' : {
        'meta_info' : _MetaInfoClass('Cfm.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes.Node', 
                [], [], 
                '''                Node-specific data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions',
            False, 
            [
            _MetaInfoClassMember('delay-constant-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Constant Factor for delay calculations
                ''',
                'delay_constant_factor',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModelEnum', 
                [], [], 
                '''                Delay model for delay calculations
                ''',
                'delay_model',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-filter', REFERENCE_ENUM_CLASS, 'CfmPmElmReplyFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilterEnum', 
                [], [], 
                '''                Reply Filtering mode used by responders
                ''',
                'reply_filter',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options',
            False, 
            [
            _MetaInfoClassMember('basic-options', REFERENCE_CLASS, 'BasicOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions', 
                [], [], 
                '''                Options for a basic IEEE 802.1ag Linktrace
                ''',
                'basic_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('exploratory-options', REFERENCE_CLASS, 'ExploratoryOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions', 
                [], [], 
                '''                Options for an Exploratory Linktrace
                ''',
                'exploratory_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'CfmPmLtModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtModeEnum', 
                [], [], 
                '''                Mode
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation',
            False, 
            [
            _MetaInfoClassMember('directed-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options', 
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
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address
                ''',
                'source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Source MEP ID
                ''',
                'source_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Target MAC address
                ''',
                'target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Target MEP ID
                ''',
                'target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of initiation time (seconds)
                ''',
                'timestamp',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8191')], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time (in seconds) before the traceroute
                completes
                ''',
                'time_left',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-information', REFERENCE_CLASS, 'TracerouteInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation', 
                [], [], 
                '''                Information about the traceroute operation
                ''',
                'traceroute_information',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'incomplete-traceroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.IncompleteTraceroutes' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.IncompleteTraceroutes',
            False, 
            [
            _MetaInfoClassMember('incomplete-traceroute', REFERENCE_LIST, 'IncompleteTraceroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Domain level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point-type', REFERENCE_ENUM_CLASS, 'CfmMaMpVarietyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVarietyEnum', 
                [], [], 
                '''                Type of Maintenance Point
                ''',
                'maintenance_point_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MaintenancePoints.MaintenancePoint' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MaintenancePoints.MaintenancePoint',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point', REFERENCE_CLASS, 'MaintenancePoint_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MaintenancePoints' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MaintenancePoints',
            False, 
            [
            _MetaInfoClassMember('maintenance-point', REFERENCE_LIST, 'MaintenancePoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MaintenancePoints.MaintenancePoint', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmtEnum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
                [('0', '65535')], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'bridge-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('bridge-domain-id', REFERENCE_CLASS, 'BridgeDomainId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId', 
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
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.GlobalConfigurationErrors' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.GlobalConfigurationErrors',
            False, 
            [
            _MetaInfoClassMember('global-configuration-error', REFERENCE_LIST, 'GlobalConfigurationError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Domain level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-point-type', REFERENCE_ENUM_CLASS, 'CfmMaMpVarietyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmMaMpVarietyEnum', 
                [], [], 
                '''                Type of Maintenance Point
                ''',
                'maintenance_point_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmtEnum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
                [('0', '65535')], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'service-bridge-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain',
            False, 
            [
            _MetaInfoClassMember('bridge-domain-id-format', REFERENCE_ENUM_CLASS, 'CfmBagBdidFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagBdidFmtEnum', 
                [], [], 
                '''                Bridge domain identifier format
                ''',
                'bridge_domain_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ce-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
                [('0', '65535')], [], 
                '''                Remote Customer Edge Identifier (CE-ID)
                ''',
                'remote_ce_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'interface-bridge-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities',
            False, 
            [
            _MetaInfoClassMember('delay-measurement', REFERENCE_CLASS, 'DelayMeasurement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement', 
                [], [], 
                '''                Delay Measurement
                ''',
                'delay_measurement',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('loopback', REFERENCE_CLASS, 'Loopback' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback', 
                [], [], 
                '''                Loopback
                ''',
                'loopback',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('synthetic-loss-measurement', REFERENCE_CLASS, 'SyntheticLossMeasurement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement', 
                [], [], 
                '''                Synthetic Loss Measurement
                ''',
                'synthetic_loss_measurement',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'satellite-capabilities',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors.MepConfigurationError' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors.MepConfigurationError',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
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
            _MetaInfoClassMember('ccm-interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmIntervalEnum', 
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
            _MetaInfoClassMember('fatal-offload-error', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The platform returned a fatal error when passed
                the offload session.
                ''',
                'fatal_offload_error',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-bridge-domain', REFERENCE_CLASS, 'InterfaceBridgeDomain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain', 
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
            _MetaInfoClassMember('maid-format-not-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The configured MAID format is not supported for
                hardware offload.
                ''',
                'maid_format_not_supported',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep', REFERENCE_CLASS, 'Mep' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep', 
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
            _MetaInfoClassMember('satellite-capabilities', REFERENCE_CLASS, 'SatelliteCapabilities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities', 
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
                [('0', '65535')], [], 
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
            _MetaInfoClassMember('service-bridge-domain', REFERENCE_CLASS, 'ServiceBridgeDomain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.MepConfigurationErrors' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.MepConfigurationErrors',
            False, 
            [
            _MetaInfoClassMember('mep-configuration-error', REFERENCE_LIST, 'MepConfigurationError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors.MepConfigurationError', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions',
            False, 
            [
            _MetaInfoClassMember('delay-constant-factor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Constant Factor for delay calculations
                ''',
                'delay_constant_factor',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModelEnum', 
                [], [], 
                '''                Delay model for delay calculations
                ''',
                'delay_model',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-filter', REFERENCE_ENUM_CLASS, 'CfmPmElmReplyFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElmReplyFilterEnum', 
                [], [], 
                '''                Reply Filtering mode used by responders
                ''',
                'reply_filter',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options',
            False, 
            [
            _MetaInfoClassMember('basic-options', REFERENCE_CLASS, 'BasicOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions', 
                [], [], 
                '''                Options for a basic IEEE 802.1ag Linktrace
                ''',
                'basic_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('exploratory-options', REFERENCE_CLASS, 'ExploratoryOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions', 
                [], [], 
                '''                Options for an Exploratory Linktrace
                ''',
                'exploratory_options',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'CfmPmLtModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLtModeEnum', 
                [], [], 
                '''                Mode
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation',
            False, 
            [
            _MetaInfoClassMember('directed-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options', 
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
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address
                ''',
                'source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('source-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Source MEP ID
                ''',
                'source_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Target MAC address
                ''',
                'target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('target-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Target MEP ID
                ''',
                'target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of initiation time (seconds)
                ''',
                'timestamp',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header',
            False, 
            [
            _MetaInfoClassMember('forwarded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LTR was forwarded
                ''',
                'forwarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('relay-action', REFERENCE_ENUM_CLASS, 'CfmPmRelayActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRelayActionEnum', 
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
                [('0', '4294967295')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
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
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmtEnum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId',
            False, 
            [
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId', 
                [], [], 
                '''                Last egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId', 
                [], [], 
                '''                Next egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmtEnum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmIngressActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIngressActionEnum', 
                [], [], 
                '''                Reply ingress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmtEnum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmEgressActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEgressActionEnum', 
                [], [], 
                '''                Reply egress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-egress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId', 
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
            _MetaInfoClassMember('last-hop-format', REFERENCE_ENUM_CLASS, 'CfmPmLastHopFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmtEnum', 
                [], [], 
                '''                LastHopFormat
                ''',
                'last_hop_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId', 
                [], [], 
                '''                Egress ID TLV
                ''',
                'egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop', REFERENCE_CLASS, 'LastHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop', 
                [], [], 
                '''                Last hop ID
                ''',
                'last_hop',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-egress', REFERENCE_CLASS, 'ReplyEgress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress', 
                [], [], 
                '''                Reply egress TLV
                ''',
                'reply_egress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-ingress', REFERENCE_CLASS, 'ReplyIngress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress', 
                [], [], 
                '''                Reply ingress TLV
                ''',
                'reply_ingress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'linktrace-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header',
            False, 
            [
            _MetaInfoClassMember('delay-model', REFERENCE_ENUM_CLASS, 'CfmPmEltDelayModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmEltDelayModelEnum', 
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
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-hop-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Hop Timeout, in seconds
                ''',
                'next_hop_timeout',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('relay-action', REFERENCE_ENUM_CLASS, 'CfmPmElrRelayActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrRelayActionEnum', 
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
                [('0', '4294967295')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmtEnum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmtEnum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmElrIngressActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrIngressActionEnum', 
                [], [], 
                '''                ELR Reply ingress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId', 
                [], [], 
                '''                Last egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId', 
                [], [], 
                '''                Next egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'next-egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue',
            False, 
            [
            _MetaInfoClassMember('port-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                PortIDFormat
                ''',
                'port_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Port ID MAC Address
                ''',
                'port_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId',
            False, 
            [
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Port ID (Deprecated)
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type', REFERENCE_ENUM_CLASS, 'CfmPmPortIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortIdFmtEnum', 
                [], [], 
                '''                Port ID type
                ''',
                'port_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID type value
                ''',
                'port_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id-value', REFERENCE_CLASS, 'PortIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue', 
                [], [], 
                '''                Port ID (Current)
                ''',
                'port_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CfmPmElrEgressActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmElrEgressActionEnum', 
                [], [], 
                '''                Reply egress action
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-egress-id', REFERENCE_CLASS, 'LastEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId', 
                [], [], 
                '''                Last Egress ID
                ''',
                'last_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of egress interface
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-egress-id', REFERENCE_CLASS, 'NextEgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId', 
                [], [], 
                '''                Next Egress ID
                ''',
                'next_egress_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-id', REFERENCE_CLASS, 'PortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId', 
                [], [], 
                '''                Port ID
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'reply-egress',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unique-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique ID
                ''',
                'unique_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'egress-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop',
            False, 
            [
            _MetaInfoClassMember('egress-id', REFERENCE_CLASS, 'EgressId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId', 
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
            _MetaInfoClassMember('last-hop-format', REFERENCE_ENUM_CLASS, 'CfmPmLastHopFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmLastHopFmtEnum', 
                [], [], 
                '''                LastHopFormat
                ''',
                'last_hop_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply',
            False, 
            [
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-hop', REFERENCE_CLASS, 'LastHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop', 
                [], [], 
                '''                Last hop ID
                ''',
                'last_hop',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-egress', REFERENCE_CLASS, 'ReplyEgress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress', 
                [], [], 
                '''                Reply egress TLV
                ''',
                'reply_egress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('reply-ingress', REFERENCE_CLASS, 'ReplyIngress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress', 
                [], [], 
                '''                Reply ingress TLV
                ''',
                'reply_ingress',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'exploratory-linktrace-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches.TracerouteCache' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches.TracerouteCache',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8191')], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transaction ID
                ''',
                'transaction_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('exploratory-linktrace-reply', REFERENCE_LIST, 'ExploratoryLinktraceReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply', 
                [], [], 
                '''                Received exploratory linktrace replies
                ''',
                'exploratory_linktrace_reply',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('linktrace-reply', REFERENCE_LIST, 'LinktraceReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply', 
                [], [], 
                '''                Received linktrace replies
                ''',
                'linktrace_reply',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('replies-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of ignored replies for this request
                ''',
                'replies_dropped',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-information', REFERENCE_CLASS, 'TracerouteInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation', 
                [], [], 
                '''                Information about the traceroute operation
                ''',
                'traceroute_information',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'traceroute-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.TracerouteCaches' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.TracerouteCaches',
            False, 
            [
            _MetaInfoClassMember('traceroute-cache', REFERENCE_LIST, 'TracerouteCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches.TracerouteCache', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.Statistics',
            False, 
            [
            _MetaInfoClassMember('ai-ss-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of AIS messages received
                ''',
                'ai_ss_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ai-ss-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of AIS messages sent
                ''',
                'ai_ss_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bn-ms-discarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BNM messages discarded
                ''',
                'bn_ms_discarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('bn-ms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BNM messages received
                ''',
                'bn_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-discarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs discarded because maximum MEPs
                limit was reached
                ''',
                'ccms_discarded',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received out-of-sequence
                ''',
                'ccms_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received
                ''',
                'ccms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs sent
                ''',
                'ccms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-ms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of DMM messages received
                ''',
                'dm_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of DMM messages sent
                ''',
                'dm_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-rs-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of DMR messages received
                ''',
                'dm_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('dm-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of DMR messages sent
                ''',
                'dm_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-ms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBMs received
                ''',
                'lb_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBMs sent
                ''',
                'lb_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-bad-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBRs received with non-matching
                user-specified data
                ''',
                'lb_rs_bad_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBRs received out-of-sequence
                ''',
                'lb_rs_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBRs received
                ''',
                'lb_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lb-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LBRs sent
                ''',
                'lb_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lc-ks-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LCK messages received
                ''',
                'lc_ks_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-ms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LMM messages received
                ''',
                'lm_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LMM messages sent
                ''',
                'lm_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-rs-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LMR messages received
                ''',
                'lm_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lm-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of LMR messages sent
                ''',
                'lm_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('lt-rs-received-unexpected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of unexpected LTRs received
                ''',
                'lt_rs_received_unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-ms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of SLM messages received
                ''',
                'sl_ms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-ms-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of SLM messages sent
                ''',
                'sl_ms_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-rs-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of SLR messages received
                ''',
                'sl_rs_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sl-rs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of SLR messages sent
                ''',
                'sl_rs_sent',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sending-start',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'receiving-start',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.AisStatistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.AisStatistics',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'CfmBagAisIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisIntervalEnum', 
                [], [], 
                '''                AIS transmission interval
                ''',
                'interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-interval', REFERENCE_ENUM_CLASS, 'CfmBagAisIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagAisIntervalEnum', 
                [], [], 
                '''                The interval of the last received AIS packet
                ''',
                'last_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address of the last received AIS
                packet
                ''',
                'last_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                AIS transmission level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('receiving-ais', REFERENCE_ENUM_CLASS, 'CfmPmAisReceiveEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisReceiveEnum', 
                [], [], 
                '''                Details of how the signal is being received
                ''',
                'receiving_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('receiving-start', REFERENCE_CLASS, 'ReceivingStart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart', 
                [], [], 
                '''                Time elapsed since AIS receiving started
                ''',
                'receiving_start',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sending-ais', REFERENCE_ENUM_CLASS, 'CfmPmAisTransmitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAisTransmitEnum', 
                [], [], 
                '''                Details of how AIS is being transmitted
                ''',
                'sending_ais',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sending-start', REFERENCE_CLASS, 'SendingStart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart', 
                [], [], 
                '''                Time elapsed since AIS sending started
                ''',
                'sending_start',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'ais-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep.Defects' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep.Defects',
            False, 
            [
            _MetaInfoClassMember('ais-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AIS or LCK received
                ''',
                'ais_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('auto-missing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Number of missing peer MEPs
                ''',
                'missing',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-that-timed-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('remote-meps-defects', REFERENCE_CLASS, 'RemoteMepsDefects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects', 
                [], [], 
                '''                Defects detected from remote MEPs
                ''',
                'remote_meps_defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unexpected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unexpected peer MEPs
                ''',
                'unexpected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'defects',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps.LocalMep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps.LocalMep',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8191')], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('ais-statistics', REFERENCE_CLASS, 'AisStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.AisStatistics', 
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
            _MetaInfoClassMember('ccm-interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmIntervalEnum', 
                [], [], 
                '''                The interval between CCMs
                ''',
                'ccm_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccm-offload', REFERENCE_ENUM_CLASS, 'CfmBagCcmOffloadEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffloadEnum', 
                [], [], 
                '''                Offload status of CCM processing
                ''',
                'ccm_offload',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
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
            _MetaInfoClassMember('defects', REFERENCE_CLASS, 'Defects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.Defects', 
                [], [], 
                '''                Defects detected from peer MEPs
                ''',
                'defects',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('defects-ignored', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Defects present but ignored due to 'report
                defects' configuration
                ''',
                'defects_ignored',
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
            _MetaInfoClassMember('fault-notification-state', REFERENCE_ENUM_CLASS, 'CfmPmMepFngStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepFngStateEnum', 
                [], [], 
                '''                Fault Notification Generation state
                ''',
                'fault_notification_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('hairpin', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MEP is on a sub-interface in the same
                bridge-domain and on the same trunk interface as
                another sub-interface
                ''',
                'hairpin',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('highest-defect', REFERENCE_ENUM_CLASS, 'CfmPmMepDefectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmMepDefectEnum', 
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
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interworking-state', REFERENCE_ENUM_CLASS, 'CfmBagIwStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagIwStateEnum', 
                [], [], 
                '''                Interface interworking state
                ''',
                'interworking_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
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
            _MetaInfoClassMember('mep-direction', REFERENCE_ENUM_CLASS, 'CfmBagDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirectionEnum', 
                [], [], 
                '''                MEP facing direction
                ''',
                'mep_direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MEP ID
                ''',
                'mep_id_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-lbm-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Transaction ID to be sent in a Loopback
                Message
                ''',
                'next_lbm_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('next-ltm-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Number of peer MEPs detected
                ''',
                'peer_meps_detected',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-meps-with-errors-detected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                '''                The local MEP is on an interface in standby mode
                ''',
                'standby',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep.Statistics', 
                [], [], 
                '''                MEP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('stp-state', REFERENCE_ENUM_CLASS, 'CfmBagStpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagStpStateEnum', 
                [], [], 
                '''                STP state
                ''',
                'stp_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'local-mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.LocalMeps' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.LocalMeps',
            False, 
            [
            _MetaInfoClassMember('local-mep', REFERENCE_LIST, 'LocalMep' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps.LocalMep', 
                [], [], 
                '''                Information about a particular local MEP
                ''',
                'local_mep',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'local-meps',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-up-down-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName',
            False, 
            [
            _MetaInfoClassMember('integer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Integer
                ''',
                'integer',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'mac-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid',
            False, 
            [
            _MetaInfoClassMember('dns-like-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DNS-like name
                ''',
                'dns_like_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-name', REFERENCE_CLASS, 'MacName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName', 
                [], [], 
                '''                MAC address name
                ''',
                'mac_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hex data
                ''',
                'mdid_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-format-value', REFERENCE_ENUM_CLASS, 'CfmBagMdidFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdidFmtEnum', 
                [], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPN index
                ''',
                'index',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPN authority organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'vpn-id-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName',
            False, 
            [
            _MetaInfoClassMember('icc-based', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ICC-based format
                ''',
                'icc_based',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('integer-name', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unsigned integer name
                ''',
                'integer_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hex data
                ''',
                'short_ma_name_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-format-value', REFERENCE_ENUM_CLASS, 'CfmBagSmanFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagSmanFmtEnum', 
                [], [], 
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
                [('0', '65535')], [], 
                '''                VLAN ID name
                ''',
                'vlan_id_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('vpn-id-name', REFERENCE_CLASS, 'VpnIdName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName', 
                [], [], 
                '''                VPN ID name
                ''',
                'vpn_id_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'short-ma-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header',
            False, 
            [
            _MetaInfoClassMember('interval', REFERENCE_ENUM_CLASS, 'CfmBagCcmIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmIntervalEnum', 
                [], [], 
                '''                CCM interval
                ''',
                'interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                MD level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid', REFERENCE_CLASS, 'Mdid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid', 
                [], [], 
                '''                MDID
                ''',
                'mdid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mdid-format', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MDID Format
                ''',
                'mdid_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
                [('0', '4294967295')], [], 
                '''                CCM sequence number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name', REFERENCE_CLASS, 'ShortMaName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName', 
                [], [], 
                '''                Short MA Name
                ''',
                'short_ma_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('short-ma-name-format', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Short MA Name format
                ''',
                'short_ma_name_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue',
            False, 
            [
            _MetaInfoClassMember('chassis-id-format', REFERENCE_ENUM_CLASS, 'CfmPmIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIdFmtEnum', 
                [], [], 
                '''                ChassisIDFormat
                ''',
                'chassis_id_format',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Chassis ID MAC Address
                ''',
                'chassis_id_mac',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-raw', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Chassis ID (Deprecated)
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type', REFERENCE_ENUM_CLASS, 'CfmPmChassisIdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmChassisIdFmtEnum', 
                [], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID Type
                ''',
                'chassis_id_type_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('chassis-id-value', REFERENCE_CLASS, 'ChassisIdValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue', 
                [], [], 
                '''                Chassis ID (Current)
                ''',
                'chassis_id_value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'chassis-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId',
            False, 
            [
            _MetaInfoClassMember('chassis-id', REFERENCE_CLASS, 'ChassisId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId', 
                [], [], 
                '''                Chassis ID
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('management-address-domain', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Management address domain
                ''',
                'management_address_domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'sender-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Organizationally-unique ID
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Subtype of TLV
                ''',
                'subtype',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'organization-specific-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('typecode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Type code of TLV
                ''',
                'typecode',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Binary data in TLV
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'unknown-tlv',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived',
            False, 
            [
            _MetaInfoClassMember('additional-interface-status', REFERENCE_ENUM_CLASS, 'CfmPmAddlIntfStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmAddlIntfStatusEnum', 
                [], [], 
                '''                Additional interface status
                ''',
                'additional_interface_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header', 
                [], [], 
                '''                Frame header
                ''',
                'header',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'CfmPmIntfStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmIntfStatusEnum', 
                [], [], 
                '''                Interface status
                ''',
                'interface_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-name', REFERENCE_CLASS, 'MepName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName', 
                [], [], 
                '''                MEP name
                ''',
                'mep_name',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('organization-specific-tlv', REFERENCE_LIST, 'OrganizationSpecificTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv', 
                [], [], 
                '''                Organizational-specific TLVs
                ''',
                'organization_specific_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('port-status', REFERENCE_ENUM_CLASS, 'CfmPmPortStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmPortStatusEnum', 
                [], [], 
                '''                Port status
                ''',
                'port_status',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Undecoded frame
                ''',
                'raw_data',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('sender-id', REFERENCE_CLASS, 'SenderId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId', 
                [], [], 
                '''                Sender ID TLV
                ''',
                'sender_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv', 
                [], [], 
                '''                Unknown TLVs
                ''',
                'unknown_tlv',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-ccm-received',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'last-ccm-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics',
            False, 
            [
            _MetaInfoClassMember('ccms-invalid-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with an invalid interval
                ''',
                'ccms_invalid_interval',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-invalid-maid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with an invalid MAID
                ''',
                'ccms_invalid_maid',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-invalid-source-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with an invalid source
                MAC address
                ''',
                'ccms_invalid_source_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-our-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with our MEP ID
                ''',
                'ccms_our_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-out-of-sequence', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received out-of-sequence
                ''',
                'ccms_out_of_sequence',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-rdi', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with the Remote Defect
                Indication bit set
                ''',
                'ccms_rdi',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received
                ''',
                'ccms_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('ccms-wrong-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of CCMs received with an invalid level
                ''',
                'ccms_wrong_level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-received-time', REFERENCE_CLASS, 'LastCcmReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime', 
                [], [], 
                '''                Elapsed time since last CCM received
                ''',
                'last_ccm_received_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence number of last CCM received
                ''',
                'last_ccm_sequence_number',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep',
            False, 
            [
            _MetaInfoClassMember('ccm-offload', REFERENCE_ENUM_CLASS, 'CfmBagCcmOffloadEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagCcmOffloadEnum', 
                [], [], 
                '''                Offload status of received CCM handling
                ''',
                'ccm_offload',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('cross-check-state', REFERENCE_ENUM_CLASS, 'CfmPmRmepXcStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepXcStateEnum', 
                [], [], 
                '''                Cross-check state
                ''',
                'cross_check_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_CLASS, 'ErrorState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState', 
                [], [], 
                '''                Error state
                ''',
                'error_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-ccm-received', REFERENCE_CLASS, 'LastCcmReceived' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived', 
                [], [], 
                '''                Last CCM received from the peer MEP
                ''',
                'last_ccm_received',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('last-up-down-time', REFERENCE_CLASS, 'LastUpDownTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime', 
                [], [], 
                '''                Elapsed time since peer MEP became active or
                timed out
                ''',
                'last_up_down_time',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-mep-state', REFERENCE_ENUM_CLASS, 'CfmPmRmepStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmPmRmepStateEnum', 
                [], [], 
                '''                State of the peer MEP state machine
                ''',
                'peer_mep_state',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics', 
                [], [], 
                '''                Peer MEP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S.PeerMePv2' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S.PeerMePv2',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('local-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8191')], [], 
                '''                MEP ID of Local MEP
                ''',
                'local_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('peer-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8191')], [], 
                '''                MEP ID of Peer MEP
                ''',
                'peer_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('peer-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Peer MAC address
                ''',
                'peer_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-oper', True),
            _MetaInfoClassMember('domain-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'domain_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'CfmBagMdLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagMdLevelEnum', 
                [], [], 
                '''                Maintenance level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-direction', REFERENCE_ENUM_CLASS, 'CfmBagDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'CfmBagDirectionEnum', 
                [], [], 
                '''                MEP facing direction
                ''',
                'mep_direction',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-mep', REFERENCE_CLASS, 'PeerMep' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep', 
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
                '''                The local MEP is on an interface in standby mode
                ''',
                'standby',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-me-pv2',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_.PeerMePv2S' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_.PeerMePv2S',
            False, 
            [
            _MetaInfoClassMember('peer-me-pv2', REFERENCE_LIST, 'PeerMePv2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S.PeerMePv2', 
                [], [], 
                '''                Information about a peer MEP for a particular
                local MEP
                ''',
                'peer_me_pv2',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'peer-me-pv2s',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm.Global_' : {
        'meta_info' : _MetaInfoClass('Cfm.Global_',
            False, 
            [
            _MetaInfoClassMember('global-configuration-errors', REFERENCE_CLASS, 'GlobalConfigurationErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.GlobalConfigurationErrors', 
                [], [], 
                '''                Global configuration errors table
                ''',
                'global_configuration_errors',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('incomplete-traceroutes', REFERENCE_CLASS, 'IncompleteTraceroutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.IncompleteTraceroutes', 
                [], [], 
                '''                Incomplete Traceroute table
                ''',
                'incomplete_traceroutes',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('local-meps', REFERENCE_CLASS, 'LocalMeps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.LocalMeps', 
                [], [], 
                '''                Local MEPs table
                ''',
                'local_meps',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('maintenance-points', REFERENCE_CLASS, 'MaintenancePoints' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MaintenancePoints', 
                [], [], 
                '''                Maintenance Points table
                ''',
                'maintenance_points',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('mep-configuration-errors', REFERENCE_CLASS, 'MepConfigurationErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.MepConfigurationErrors', 
                [], [], 
                '''                MEP configuration errors table
                ''',
                'mep_configuration_errors',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('peer-me-pv2s', REFERENCE_CLASS, 'PeerMePv2S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.PeerMePv2S', 
                [], [], 
                '''                Peer MEPs table Version 2
                ''',
                'peer_me_pv2s',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('traceroute-caches', REFERENCE_CLASS, 'TracerouteCaches' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_.TracerouteCaches', 
                [], [], 
                '''                Traceroute Cache table
                ''',
                'traceroute_caches',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
    'Cfm' : {
        'meta_info' : _MetaInfoClass('Cfm',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Global_', 
                [], [], 
                '''                Global operational data
                ''',
                'global_',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper', 'Cfm.Nodes', 
                [], [], 
                '''                Node table for node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ethernet-cfm-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-oper',
            'cfm',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_oper'
        ),
    },
}
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects.RemoteMepsDefects']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.Defects']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics.LastStarted']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis.Statistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises.InterfaceAis']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic.Statistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics.InterfaceStatistic']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info']
_meta_table['Cfm.Nodes.Node.CcmLearningDatabases.CcmLearningDatabase']['meta_info'].parent =_meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceAises']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.InterfaceStatistics']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.Summary']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node.CcmLearningDatabases']['meta_info'].parent =_meta_table['Cfm.Nodes.Node']['meta_info']
_meta_table['Cfm.Nodes.Node']['meta_info'].parent =_meta_table['Cfm.Nodes']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.BasicOptions']['meta_info'].parent =_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options.ExploratoryOptions']['meta_info'].parent =_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation.Options']['meta_info'].parent =_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute.TracerouteInformation']['meta_info'].parent =_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes.IncompleteTraceroute']['meta_info'].parent =_meta_table['Cfm.Global_.IncompleteTraceroutes']['meta_info']
_meta_table['Cfm.Global_.MaintenancePoints.MaintenancePoint.MaintenancePoint_']['meta_info'].parent =_meta_table['Cfm.Global_.MaintenancePoints.MaintenancePoint']['meta_info']
_meta_table['Cfm.Global_.MaintenancePoints.MaintenancePoint']['meta_info'].parent =_meta_table['Cfm.Global_.MaintenancePoints']['meta_info']
_meta_table['Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError.BridgeDomainId']['meta_info'].parent =_meta_table['Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info']
_meta_table['Cfm.Global_.GlobalConfigurationErrors.GlobalConfigurationError']['meta_info'].parent =_meta_table['Cfm.Global_.GlobalConfigurationErrors']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.Loopback']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.DelayMeasurement']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities.SyntheticLossMeasurement']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.Mep']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.ServiceBridgeDomain']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.InterfaceBridgeDomain']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError.SatelliteCapabilities']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors.MepConfigurationError']['meta_info'].parent =_meta_table['Cfm.Global_.MepConfigurationErrors']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.BasicOptions']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options.ExploratoryOptions']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation.Options']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress.PortId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress.PortId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop.EgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.Header']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.SenderId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.EgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyIngress']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.ReplyEgress']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.LastHop']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress.PortId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId.PortIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.LastEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.NextEgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress.PortId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop.EgressId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.Header']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.SenderId']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyIngress']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.ReplyEgress']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.LastHop']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.TracerouteInformation']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.LinktraceReply']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache.ExploratoryLinktraceReply']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches.TracerouteCache']['meta_info'].parent =_meta_table['Cfm.Global_.TracerouteCaches']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics.SendingStart']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics.ReceivingStart']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.Defects.RemoteMepsDefects']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep.Defects']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.Statistics']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.AisStatistics']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep.Defects']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps.LocalMep']['meta_info']
_meta_table['Cfm.Global_.LocalMeps.LocalMep']['meta_info'].parent =_meta_table['Cfm.Global_.LocalMeps']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid.MacName']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName.VpnIdName']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.Mdid']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header.ShortMaName']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId.ChassisIdValue']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId.ChassisId']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.Header']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.SenderId']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.MepName']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.OrganizationSpecificTlv']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived.UnknownTlv']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics.LastCcmReceivedTime']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.ErrorState']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastUpDownTime']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.LastCcmReceived']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep.Statistics']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2.PeerMep']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S.PeerMePv2']['meta_info'].parent =_meta_table['Cfm.Global_.PeerMePv2S']['meta_info']
_meta_table['Cfm.Global_.IncompleteTraceroutes']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.MaintenancePoints']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.GlobalConfigurationErrors']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.MepConfigurationErrors']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.TracerouteCaches']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.LocalMeps']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Global_.PeerMePv2S']['meta_info'].parent =_meta_table['Cfm.Global_']['meta_info']
_meta_table['Cfm.Nodes']['meta_info'].parent =_meta_table['Cfm']['meta_info']
_meta_table['Cfm.Global_']['meta_info'].parent =_meta_table['Cfm']['meta_info']

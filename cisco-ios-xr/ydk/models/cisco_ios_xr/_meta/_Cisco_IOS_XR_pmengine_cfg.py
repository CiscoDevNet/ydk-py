


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'OpticsThresholdEnum' : _MetaInfoEnum('OpticsThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-opt-min':'thresh_opt_min',
            'thresh-opr-min':'thresh_opr_min',
            'thresh-lbc-min':'thresh_lbc_min',
            'thresh-lbc-pc-min':'thresh_lbc_pc_min',
            'thresh-cd-min':'thresh_cd_min',
            'thresh-dgd-min':'thresh_dgd_min',
            'thresh-pmd-min':'thresh_pmd_min',
            'thresh-osnr-min':'thresh_osnr_min',
            'thresh-pdl-min':'thresh_pdl_min',
            'thresh-pcr-min':'thresh_pcr_min',
            'thresh-pn-min':'thresh_pn_min',
            'thresh-opt-max':'thresh_opt_max',
            'thresh-opr-max':'thresh_opr_max',
            'thresh-lbc-max':'thresh_lbc_max',
            'thresh-lbc-pc-max':'thresh_lbc_pc_max',
            'thresh-cd-max':'thresh_cd_max',
            'thresh-dgd-max':'thresh_dgd_max',
            'thresh-pmd-max':'thresh_pmd_max',
            'thresh-osnr-max':'thresh_osnr_max',
            'thresh-pdl-max':'thresh_pdl_max',
            'thresh-pcr-max':'thresh_pcr_max',
            'thresh-pn-max':'thresh_pn_max',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OtnThresholdEnum' : _MetaInfoEnum('OtnThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-es-sm-ne':'thresh_es_sm_ne',
            'thresh-ses-sm-ne':'thresh_ses_sm_ne',
            'thresh-uas-sm-ne':'thresh_uas_sm_ne',
            'thresh-bbe-sm-ne':'thresh_bbe_sm_ne',
            'thresh-fc-sm-ne':'thresh_fc_sm_ne',
            'thresh-esr-sm-ne':'thresh_esr_sm_ne',
            'thresh-sesr-sm-ne':'thresh_sesr_sm_ne',
            'thresh-bber-sm-ne':'thresh_bber_sm_ne',
            'thresh-es-pm-ne':'thresh_es_pm_ne',
            'thresh-ses-pm-ne':'thresh_ses_pm_ne',
            'thresh-uas-pm-ne':'thresh_uas_pm_ne',
            'thresh-bbe-pm-ne':'thresh_bbe_pm_ne',
            'thresh-fc-pm-ne':'thresh_fc_pm_ne',
            'thresh-esr-pm-ne':'thresh_esr_pm_ne',
            'thresh-sesr-pm-ne':'thresh_sesr_pm_ne',
            'thresh-bber-pm-ne':'thresh_bber_pm_ne',
            'thresh-es-sm-fe':'thresh_es_sm_fe',
            'thresh-ses-sm-fe':'thresh_ses_sm_fe',
            'thresh-uas-sm-fe':'thresh_uas_sm_fe',
            'thresh-bbe-sm-fe':'thresh_bbe_sm_fe',
            'thresh-fc-sm-fe':'thresh_fc_sm_fe',
            'thresh-esr-sm-fe':'thresh_esr_sm_fe',
            'thresh-sesr-sm-fe':'thresh_sesr_sm_fe',
            'thresh-bber-sm-fe':'thresh_bber_sm_fe',
            'thresh-es-pm-fe':'thresh_es_pm_fe',
            'thresh-ses-pm-fe':'thresh_ses_pm_fe',
            'thresh-uas-pm-fe':'thresh_uas_pm_fe',
            'thresh-bbe-pm-fe':'thresh_bbe_pm_fe',
            'thresh-fc-pm-fe':'thresh_fc_pm_fe',
            'thresh-esr-pm-fe':'thresh_esr_pm_fe',
            'thresh-sesr-pm-fe':'thresh_sesr_pm_fe',
            'thresh-bber-pm-fe':'thresh_bber_pm_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OtnTcmThresholdEnum' : _MetaInfoEnum('OtnTcmThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-es-tcm-fe':'thresh_es_tcm_fe',
            'thresh-ses-tcm-fe':'thresh_ses_tcm_fe',
            'thresh-uas-tcm-fe':'thresh_uas_tcm_fe',
            'thresh-bbe-tcm-fe':'thresh_bbe_tcm_fe',
            'thresh-fc-tcm-fe':'thresh_fc_tcm_fe',
            'thresh-esr-tcm-fe':'thresh_esr_tcm_fe',
            'thresh-sesr-tcm-fe':'thresh_sesr_tcm_fe',
            'thresh-bber-tcm-fe':'thresh_bber_tcm_fe',
            'thresh-es-tcm-ne':'thresh_es_tcm_ne',
            'thresh-ses-tcm-ne':'thresh_ses_tcm_ne',
            'thresh-uas-tcm-ne':'thresh_uas_tcm_ne',
            'thresh-bbe-tcm-ne':'thresh_bbe_tcm_ne',
            'thresh-fc-tcm-ne':'thresh_fc_tcm_ne',
            'thresh-esr-tcm-ne':'thresh_esr_tcm_ne',
            'thresh-sesr-tcm-ne':'thresh_sesr_tcm_ne',
            'thresh-bber-tcm-ne':'thresh_bber_tcm_ne',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'StsThresholdEnum' : _MetaInfoEnum('StsThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-cv':'thresh_cv',
            'thresh-es':'thresh_es',
            'thresh-ses':'thresh_ses',
            'thresh-uas':'thresh_uas',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'FecReportEnum' : _MetaInfoEnum('FecReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-ec-bits':'report_ec_bits',
            'report-uc-words':'report_uc_words',
            'report-pre-fec-ber-max':'report_pre_fec_ber_max',
            'report-post-fec-ber-max':'report_post_fec_ber_max',
            'report-q-max':'report_q_max',
            'report-q-margin-max':'report_q_margin_max',
            'report-pre-fec-ber-min':'report_pre_fec_ber_min',
            'report-post-fec-ber-min':'report_post_fec_ber_min',
            'report-q-min':'report_q_min',
            'report-q-margin-min':'report_q_margin_min',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'HoVcThresholdEnum' : _MetaInfoEnum('HoVcThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-eb':'thresh_eb',
            'thresh-es':'thresh_es',
            'thresh-esr':'thresh_esr',
            'thresh-ses':'thresh_ses',
            'thresh-sesr':'thresh_sesr',
            'thresh-bbe':'thresh_bbe',
            'thresh-bber':'thresh_bber',
            'thresh-uass':'thresh_uass',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'GfpThresholdEnum' : _MetaInfoEnum('GfpThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-rx-bit-err':'thresh_rx_bit_err',
            'thresh-rx-inv-typ':'thresh_rx_inv_typ',
            'thresh-rx-crc':'thresh_rx_crc',
            'thresh-rx-lfd':'thresh_rx_lfd',
            'thresh-rx-csf':'thresh_rx_csf',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'ReportEnum' : _MetaInfoEnum('ReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OtnTcmReportEnum' : _MetaInfoEnum('OtnTcmReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-es-tcm-fe':'report_es_tcm_fe',
            'report-ses-tcm-fe':'report_ses_tcm_fe',
            'report-uas-tcm-fe':'report_uas_tcm_fe',
            'report-bbe-tcm-fe':'report_bbe_tcm_fe',
            'report-fc-tcm-fe':'report_fc_tcm_fe',
            'report-esr-tcm-fe':'report_esr_tcm_fe',
            'report-sesr-tcm-fe':'report_sesr_tcm_fe',
            'report-bber-tcm-fe':'report_bber_tcm_fe',
            'report-es-tcm-ne':'report_es_tcm_ne',
            'report-ses-tcm-ne':'report_ses_tcm_ne',
            'report-uas-tcm-ne':'report_uas_tcm_ne',
            'report-bbe-tcm-ne':'report_bbe_tcm_ne',
            'report-fc-tcm-ne':'report_fc_tcm_ne',
            'report-esr-tcm-ne':'report_esr_tcm_ne',
            'report-sesr-tcm-ne':'report_sesr_tcm_ne',
            'report-bber-tcm-ne':'report_bber_tcm_ne',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OpticsReportEnum' : _MetaInfoEnum('OpticsReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-opt-min':'report_opt_min',
            'report-opr-min':'report_opr_min',
            'report-lbc-min':'report_lbc_min',
            'report-lbc-pc-min':'report_lbc_pc_min',
            'report-cd-min':'report_cd_min',
            'report-dgd-min':'report_dgd_min',
            'report-pmd-min':'report_pmd_min',
            'report-osnr-min':'report_osnr_min',
            'report-pdl-min':'report_pdl_min',
            'report-pcr-min':'report_pcr_min',
            'report-pn-min':'report_pn_min',
            'report-opt-max':'report_opt_max',
            'report-opr-max':'report_opr_max',
            'report-lbc-max':'report_lbc_max',
            'report-lbc-pc-max':'report_lbc_pc_max',
            'report-cd-max':'report_cd_max',
            'report-dgd-max':'report_dgd_max',
            'report-pmd-max':'report_pmd_max',
            'report-osnr-max':'report_osnr_max',
            'report-pdl-max':'report_pdl_max',
            'report-pcr-max':'report_pcr_max',
            'report-pn-max':'report_pn_max',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'GfpReportEnum' : _MetaInfoEnum('GfpReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-rx-bit-err':'report_rx_bit_err',
            'report-rx-inv-typ':'report_rx_inv_typ',
            'report-rx-crc':'report_rx_crc',
            'report-rx-lfd':'report_rx_lfd',
            'report-rx-csf':'report_rx_csf',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'HoVcReportEnum' : _MetaInfoEnum('HoVcReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-eb':'report_eb',
            'report-es':'report_es',
            'report-esr':'report_esr',
            'report-ses':'report_ses',
            'report-sesr':'report_sesr',
            'report-bbe':'report_bbe',
            'report-bber':'report_bber',
            'report-uass':'report_uass',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'StmReportEnum' : _MetaInfoEnum('StmReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-ebs':'report_ebs',
            'report-ess':'report_ess',
            'report-esrs':'report_esrs',
            'report-sess':'report_sess',
            'report-sesrs':'report_sesrs',
            'report-bbes':'report_bbes',
            'report-bbesr':'report_bbesr',
            'report-uass':'report_uass',
            'report-ebl-ne':'report_ebl_ne',
            'report-esl-ne':'report_esl_ne',
            'report-eslr-ne':'report_eslr_ne',
            'report-sesl-ne':'report_sesl_ne',
            'report-sesrl-ne':'report_sesrl_ne',
            'report-bbel-ne':'report_bbel_ne',
            'report-bberl-ne':'report_bberl_ne',
            'report-uasl-ne':'report_uasl_ne',
            'report-ebl-fe':'report_ebl_fe',
            'report-esl-fe':'report_esl_fe',
            'report-esrl-fe':'report_esrl_fe',
            'report-sesl-fe':'report_sesl_fe',
            'report-sesrl-fe':'report_sesrl_fe',
            'report-bbel-fe':'report_bbel_fe',
            'report-bberl-fe':'report_bberl_fe',
            'report-uasl-fe':'report_uasl_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'EtherThresholdEnum' : _MetaInfoEnum('EtherThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-rx-pkt':'thresh_rx_pkt',
            'thresh-rx-util':'thresh_rx_util',
            'thresh-tx-util':'thresh_tx_util',
            'thresh-stat-pkt':'thresh_stat_pkt',
            'thresh-octet-stat':'thresh_octet_stat',
            'thresh-over-size-pkt':'thresh_over_size_pkt',
            'thresh-fcs-err':'thresh_fcs_err',
            'thresh-long-frame-s':'thresh_long_frame_s',
            'thresh-jabber-stats':'thresh_jabber_stats',
            'thresh-64-octet':'thresh_64_octet',
            'thresh-65-127-octet':'thresh_65_127_octet',
            'thresh-128-255-octet':'thresh_128_255_octet',
            'thresh-256-511-octet':'thresh_256_511_octet',
            'thresh-512-1023-octet':'thresh_512_1023_octet',
            'thresh-1024-1518-octet':'thresh_1024_1518_octet',
            'thresh-in-ucast':'thresh_in_ucast',
            'thresh-in-mcast':'thresh_in_mcast',
            'thresh-in-bcast':'thresh_in_bcast',
            'thresh-out-ucast':'thresh_out_ucast',
            'thresh-out-mcast':'thresh_out_mcast',
            'thresh-out-bcast':'thresh_out_bcast',
            'thresh-tx-pkt':'thresh_tx_pkt',
            'thresh-ifin-error-s':'thresh_ifin_error_s',
            'thresh-ifin-octets':'thresh_ifin_octets',
            'thresh-ether-stat-multicast-pkt':'thresh_ether_stat_multicast_pkt',
            'thresh-ether-stat-broadcast-pkt':'thresh_ether_stat_broadcast_pkt',
            'thresh-ether-stat-under-size-d-pkt':'thresh_ether_stat_under_size_d_pkt',
            'thresh-out-octet':'thresh_out_octet',
            'thresh-in-pause-frame':'thresh_in_pause_frame',
            'thresh-in-go-od-bytes':'thresh_in_go_od_bytes',
            'thresh-in-802-1q-frame-s':'thresh_in_802_1q_frame_s',
            'thresh-in-pkts-1519-max-octets':'thresh_in_pkts_1519_max_octets',
            'thresh-in-go-od-pkts':'thresh_in_go_od_pkts',
            'thresh-in-drop-overrun':'thresh_in_drop_overrun',
            'thresh-in-drop-abort':'thresh_in_drop_abort',
            'thresh-in-drop-invalid-vlan':'thresh_in_drop_invalid_vlan',
            'thresh-in-drop-invalid-dmac':'thresh_in_drop_invalid_dmac',
            'thresh-in-drop-invalid-encap':'thresh_in_drop_invalid_encap',
            'thresh-in-drop-other':'thresh_in_drop_other',
            'thresh-in-mib-giant':'thresh_in_mib_giant',
            'thresh-in-mib-jabber':'thresh_in_mib_jabber',
            'thresh-in-mib-crc':'thresh_in_mib_crc',
            'thresh-in-error-collision-s':'thresh_in_error_collision_s',
            'thresh-in-error-symbol':'thresh_in_error_symbol',
            'thresh-out-go-od-bytes':'thresh_out_go_od_bytes',
            'thresh-out-802-1q-frame-s':'thresh_out_802_1q_frame_s',
            'thresh-out-pause-frame-s':'thresh_out_pause_frame_s',
            'thresh-out-pkts-1519-max-octets':'thresh_out_pkts_1519_max_octets',
            'thresh-out-go-od-pkts':'thresh_out_go_od_pkts',
            'thresh-out-drop-under-run':'thresh_out_drop_under_run',
            'thresh-out-drop-abort':'thresh_out_drop_abort',
            'thresh-out-drop-other':'thresh_out_drop_other',
            'thresh-out-error-other':'thresh_out_error_other',
            'thresh-in-error-giant':'thresh_in_error_giant',
            'thresh-in-error-runt':'thresh_in_error_runt',
            'thresh-in-error-jabbers':'thresh_in_error_jabbers',
            'thresh-in-error-fragments':'thresh_in_error_fragments',
            'thresh-in-error-other':'thresh_in_error_other',
            'thresh-in-pkt-64-octet':'thresh_in_pkt_64_octet',
            'thresh-in-pkts-65-127octets':'thresh_in_pkts_65_127octets',
            'thresh-in-pkts-128-255-octets':'thresh_in_pkts_128_255_octets',
            'thresh-in-pkts-256-511-octets':'thresh_in_pkts_256_511_octets',
            'thresh-in-pkts-512-1023-octets':'thresh_in_pkts_512_1023_octets',
            'thresh-in-pkts-1024-1518-octets':'thresh_in_pkts_1024_1518_octets',
            'thresh-out-pkt-64-octet':'thresh_out_pkt_64_octet',
            'thresh-out-pkts-65-127octets':'thresh_out_pkts_65_127octets',
            'thresh-out-pkts-128-255-octets':'thresh_out_pkts_128_255_octets',
            'thresh-out-pkts-256-511-octets':'thresh_out_pkts_256_511_octets',
            'thresh-out-pkts-512-1023-octets':'thresh_out_pkts_512_1023_octets',
            'thresh-out-pkts-1024-1518-octets':'thresh_out_pkts_1024_1518_octets',
            'thresh-tx-under-size-d-pkt':'thresh_tx_under_size_d_pkt',
            'thresh-tx-over-size-d-pkt':'thresh_tx_over_size_d_pkt',
            'thresh-tx-fragments':'thresh_tx_fragments',
            'thresh-tx-jabber':'thresh_tx_jabber',
            'thresh-tx-bad-fcs':'thresh_tx_bad_fcs',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'FecThresholdEnum' : _MetaInfoEnum('FecThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-ec-bits':'thresh_ec_bits',
            'thresh-uc-words':'thresh_uc_words',
            'thresh-pre-fec-ber-max':'thresh_pre_fec_ber_max',
            'thresh-post-fec-ber-max':'thresh_post_fec_ber_max',
            'thresh-q-max':'thresh_q_max',
            'thresh-q-margin-max':'thresh_q_margin_max',
            'thresh-pre-fec-ber-min':'thresh_pre_fec_ber_min',
            'thresh-post-fec-ber-min':'thresh_post_fec_ber_min',
            'thresh-q-min':'thresh_q_min',
            'thresh-q-margin-min':'thresh_q_margin_min',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'StsReportEnum' : _MetaInfoEnum('StsReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-cv':'report_cv',
            'report-es':'report_es',
            'report-ses':'report_ses',
            'report-uas':'report_uas',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OtnReportEnum' : _MetaInfoEnum('OtnReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-es-sm-ne':'report_es_sm_ne',
            'report-ses-sm-ne':'report_ses_sm_ne',
            'report-uas-sm-ne':'report_uas_sm_ne',
            'report-bbe-sm-ne':'report_bbe_sm_ne',
            'report-fc-sm-ne':'report_fc_sm_ne',
            'report-esr-sm-ne':'report_esr_sm_ne',
            'report-sesr-sm-ne':'report_sesr_sm_ne',
            'report-bber-sm-ne':'report_bber_sm_ne',
            'report-es-pm-ne':'report_es_pm_ne',
            'report-ses-pm-ne':'report_ses_pm_ne',
            'report-uas-pm-ne':'report_uas_pm_ne',
            'report-bbe-pm-ne':'report_bbe_pm_ne',
            'report-fc-pm-ne':'report_fc_pm_ne',
            'report-esr-pm-ne':'report_esr_pm_ne',
            'report-sesr-pm-ne':'report_sesr_pm_ne',
            'report-bber-pm-ne':'report_bber_pm_ne',
            'report-es-sm-fe':'report_es_sm_fe',
            'report-ses-sm-fe':'report_ses_sm_fe',
            'report-uas-sm-fe':'report_uas_sm_fe',
            'report-bbe-sm-fe':'report_bbe_sm_fe',
            'report-fc-sm-fe':'report_fc_sm_fe',
            'report-esr-sm-fe':'report_esr_sm_fe',
            'report-sesr-sm-fe':'report_sesr_sm_fe',
            'report-bber-sm-fe':'report_bber_sm_fe',
            'report-es-pm-fe':'report_es_pm_fe',
            'report-ses-pm-fe':'report_ses_pm_fe',
            'report-uas-pm-fe':'report_uas_pm_fe',
            'report-bbe-pm-fe':'report_bbe_pm_fe',
            'report-fc-pm-fe':'report_fc_pm_fe',
            'report-esr-pm-fe':'report_esr_pm_fe',
            'report-sesr-pm-fe':'report_sesr_pm_fe',
            'report-bber-pm-fe':'report_bber_pm_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OcnThresholdEnum' : _MetaInfoEnum('OcnThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-sefss':'thresh_sefss',
            'thresh-cvs':'thresh_cvs',
            'thresh-ess':'thresh_ess',
            'thresh-sess':'thresh_sess',
            'thresh-cvl-ne':'thresh_cvl_ne',
            'thresh-esl-ne':'thresh_esl_ne',
            'thresh-sesl-ne':'thresh_sesl_ne',
            'thresh-uasl-ne':'thresh_uasl_ne',
            'thresh-fcl-ne':'thresh_fcl_ne',
            'thresh-fcl-fe':'thresh_fcl_fe',
            'thresh-cvl-fe':'thresh_cvl_fe',
            'thresh-esl-fe':'thresh_esl_fe',
            'thresh-sesl-fe':'thresh_sesl_fe',
            'thresh-uasl-fe':'thresh_uasl_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'StmThresholdEnum' : _MetaInfoEnum('StmThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-ebs':'thresh_ebs',
            'thresh-ess':'thresh_ess',
            'thresh-esrs':'thresh_esrs',
            'thresh-sess':'thresh_sess',
            'thresh-sesrs':'thresh_sesrs',
            'thresh-bbes':'thresh_bbes',
            'thresh-bbesr':'thresh_bbesr',
            'thresh-uass':'thresh_uass',
            'thresh-ebl-ne':'thresh_ebl_ne',
            'thresh-esl-ne':'thresh_esl_ne',
            'thresh-eslr-ne':'thresh_eslr_ne',
            'thresh-sesl-ne':'thresh_sesl_ne',
            'thresh-sesrl-ne':'thresh_sesrl_ne',
            'thresh-bbel-ne':'thresh_bbel_ne',
            'thresh-bberl-ne':'thresh_bberl_ne',
            'thresh-uasl-ne':'thresh_uasl_ne',
            'thresh-ebl-fe':'thresh_ebl_fe',
            'thresh-esl-fe':'thresh_esl_fe',
            'thresh-esrl-fe':'thresh_esrl_fe',
            'thresh-sesl-fe':'thresh_sesl_fe',
            'thresh-sesrl-fe':'thresh_sesrl_fe',
            'thresh-bbel-fe':'thresh_bbel_fe',
            'thresh-bberl-fe':'thresh_bberl_fe',
            'thresh-uasl-fe':'thresh_uasl_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'OcnReportEnum' : _MetaInfoEnum('OcnReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-sefss':'report_sefss',
            'report-cvs':'report_cvs',
            'report-ess':'report_ess',
            'report-sess':'report_sess',
            'report-cvl-ne':'report_cvl_ne',
            'report-esl-ne':'report_esl_ne',
            'report-sesl-ne':'report_sesl_ne',
            'report-uasl-ne':'report_uasl_ne',
            'report-fcl-ne':'report_fcl_ne',
            'report-fcl-fe':'report_fcl_fe',
            'report-cvl-fe':'report_cvl_fe',
            'report-esl-fe':'report_esl_fe',
            'report-sesl-fe':'report_sesl_fe',
            'report-uasl-fe':'report_uasl_fe',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'EtherReportEnum' : _MetaInfoEnum('EtherReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-rx-pkt':'report_rx_pkt',
            'report-rx-util':'report_rx_util',
            'report-tx-util':'report_tx_util',
            'report-stat-pkt':'report_stat_pkt',
            'report-octet-stat':'report_octet_stat',
            'report-over-size-pkt':'report_over_size_pkt',
            'report-fcs-err':'report_fcs_err',
            'report-long-frame-s':'report_long_frame_s',
            'report-jabber-stats':'report_jabber_stats',
            'report-64-octet':'report_64_octet',
            'report-65-127-octet':'report_65_127_octet',
            'report-128-255-octet':'report_128_255_octet',
            'report-256-511-octet':'report_256_511_octet',
            'report-512-1023-octet':'report_512_1023_octet',
            'report-1024-1518-octet':'report_1024_1518_octet',
            'report-in-ucast':'report_in_ucast',
            'report-in-mcast':'report_in_mcast',
            'report-in-bcast':'report_in_bcast',
            'report-out-ucast':'report_out_ucast',
            'report-out-mcast':'report_out_mcast',
            'report-out-bcast':'report_out_bcast',
            'report-tx-pkt':'report_tx_pkt',
            'report-ifin-error-s':'report_ifin_error_s',
            'report-ifin-octets':'report_ifin_octets',
            'report-ether-stat-multicast-pkt':'report_ether_stat_multicast_pkt',
            'report-ether-stat-broadcast-pkt':'report_ether_stat_broadcast_pkt',
            'report-ether-stat-under-size-d-pkt':'report_ether_stat_under_size_d_pkt',
            'report-out-octet':'report_out_octet',
            'report-in-pause-frame':'report_in_pause_frame',
            'report-in-go-od-bytes':'report_in_go_od_bytes',
            'report-in-802-1q-frame-s':'report_in_802_1q_frame_s',
            'report-in-pkts-1519-max-octets':'report_in_pkts_1519_max_octets',
            'report-in-go-od-pkts':'report_in_go_od_pkts',
            'report-in-drop-overrun':'report_in_drop_overrun',
            'report-in-drop-abort':'report_in_drop_abort',
            'report-in-drop-invalid-vlan':'report_in_drop_invalid_vlan',
            'report-in-drop-invalid-dmac':'report_in_drop_invalid_dmac',
            'report-in-drop-invalid-encap':'report_in_drop_invalid_encap',
            'report-in-drop-other':'report_in_drop_other',
            'report-in-mib-giant':'report_in_mib_giant',
            'report-in-mib-jabber':'report_in_mib_jabber',
            'report-in-mib-crc':'report_in_mib_crc',
            'report-in-error-collision-s':'report_in_error_collision_s',
            'report-in-error-symbol':'report_in_error_symbol',
            'report-out-go-od-bytes':'report_out_go_od_bytes',
            'report-out-802-1q-frame-s':'report_out_802_1q_frame_s',
            'report-out-pause-frame-s':'report_out_pause_frame_s',
            'report-out-pkts-1519-max-octets':'report_out_pkts_1519_max_octets',
            'report-out-go-od-pkts':'report_out_go_od_pkts',
            'report-out-drop-under-run':'report_out_drop_under_run',
            'report-out-drop-abort':'report_out_drop_abort',
            'report-out-drop-other':'report_out_drop_other',
            'report-out-error-other':'report_out_error_other',
            'report-in-error-giant':'report_in_error_giant',
            'report-in-error-runt':'report_in_error_runt',
            'report-in-error-jabbers':'report_in_error_jabbers',
            'report-in-error-fragments':'report_in_error_fragments',
            'report-in-error-other':'report_in_error_other',
            'report-in-pkt-64-octet':'report_in_pkt_64_octet',
            'report-in-pkts-65-127octets':'report_in_pkts_65_127octets',
            'report-in-pkts-128-255-octets':'report_in_pkts_128_255_octets',
            'report-in-pkts-256-511-octets':'report_in_pkts_256_511_octets',
            'report-in-pkts-512-1023-octets':'report_in_pkts_512_1023_octets',
            'report-in-pkts-1024-1518-octets':'report_in_pkts_1024_1518_octets',
            'report-out-pkt-64-octet':'report_out_pkt_64_octet',
            'report-out-pkts-65-127octets':'report_out_pkts_65_127octets',
            'report-out-pkts-128-255-octets':'report_out_pkts_128_255_octets',
            'report-out-pkts-256-511-octets':'report_out_pkts_256_511_octets',
            'report-out-pkts-512-1023-octets':'report_out_pkts_512_1023_octets',
            'report-out-pkts-1024-1518-octets':'report_out_pkts_1024_1518_octets',
            'report-tx-under-size-d-pkt':'report_tx_under_size_d_pkt',
            'report-tx-over-size-d-pkt':'report_tx_over_size_d_pkt',
            'report-tx-fragments':'report_tx_fragments',
            'report-tx-jabber':'report_tx_jabber',
            'report-tx-bad-fcs':'report_tx_bad_fcs',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'PathThresholdEnum' : _MetaInfoEnum('PathThresholdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'thresh-cv':'thresh_cv',
            'thresh-es':'thresh_es',
            'thresh-ses':'thresh_ses',
            'thresh-uas':'thresh_uas',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
    'PathReportEnum' : _MetaInfoEnum('PathReportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pmengine_cfg',
        {
            'report-cv':'report_cv',
            'report-es':'report_es',
            'report-ses':'report_ses',
            'report-uas':'report_uas',
        }, 'Cisco-IOS-XR-pmengine-cfg', _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg']),
}

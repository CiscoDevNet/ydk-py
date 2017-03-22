""" Cisco_IOS_XR_pmengine_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pmengine package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EtherReportEnum(Enum):
    """
    EtherReportEnum

    Ether report

    .. data:: report_rx_pkt = 524288

    	PM Ether rx pkt report

    .. data:: report_rx_util = 524289

    	PM Ether rx util report

    .. data:: report_tx_util = 524290

    	PM Ether tx util report

    .. data:: report_stat_pkt = 524291

    	PM ether stat pkt threshold

    .. data:: report_octet_stat = 524292

    	PM Ether octet stat report

    .. data:: report_over_size_pkt = 524293

    	PM Ether oversize pkt report

    .. data:: report_fcs_err = 524294

    	PM Ether fcs error report

    .. data:: report_long_frame_s = 524295

    	PM Ether long frames report

    .. data:: report_jabber_stats = 524296

    	PM Ether jabber stats report

    .. data:: report_64_octet = 524297

    	PM Ether 64 octet report

    .. data:: report_65_127_octet = 524298

    	PM Ether 65 to 127 octet report

    .. data:: report_128_255_octet = 524299

    	PM Ether 128 to 255 octet report

    .. data:: report_256_511_octet = 524300

    	PM Ether 256 to 511 octet report

    .. data:: report_512_1023_octet = 524301

    	PM Ether 512 to 1023 octet report

    .. data:: report_1024_1518_octet = 524302

    	PM Ether 1024 to 1518 report

    .. data:: report_in_ucast = 524303

    	PM Ether rx ucast report

    .. data:: report_in_mcast = 524304

    	PM Ether rx mcast report

    .. data:: report_in_bcast = 524305

    	PM Ether rx bcast report

    .. data:: report_out_ucast = 524306

    	PM Ether tx ucast report

    .. data:: report_out_mcast = 524307

    	PM Ether tx mcast report

    .. data:: report_out_bcast = 524308

    	PM Ether tx bcast report

    .. data:: report_tx_pkt = 524309

    	PM Ether tx pkt threshold

    .. data:: report_ifin_error_s = 524310

    	PM ether ifIn errors threshold

    .. data:: report_ifin_octets = 524311

    	PM ether ifInOctets threshold

    .. data:: report_ether_stat_multicast_pkt = 524312

    	PM ether stat multicast pkt threshold

    .. data:: report_ether_stat_broadcast_pkt = 524313

    	PM ether stat broadcast pkt threshold

    .. data:: report_ether_stat_under_size_d_pkt = 524314

    	PM ether stat undersized pkt threshold

    .. data:: report_out_octet = 524315

    	PM ether out octets threshold

    .. data:: report_in_pause_frame = 524316

    	PM ether in pause frame report

    .. data:: report_in_go_od_bytes = 524317

    	PM in good bytes report

    .. data:: report_in_802_1q_frame_s = 524318

    	PM in 802_1 Q report

    .. data:: report_in_pkts_1519_max_octets = 524319

    	PM in pkts 1519 max octets report

    .. data:: report_in_go_od_pkts = 524320

    	PM in good pkts report

    .. data:: report_in_drop_overrun = 524321

    	PM in drop overrun report

    .. data:: report_in_drop_abort = 524322

    	PM in drop abort report

    .. data:: report_in_drop_invalid_vlan = 524323

    	PM in drop invalid vlan report

    .. data:: report_in_drop_invalid_dmac = 524324

    	PM in drop invalid DMAC report

    .. data:: report_in_drop_invalid_encap = 524325

    	PM in drop invalid encap report

    .. data:: report_in_drop_other = 524326

    	PM in drop other report

    .. data:: report_in_mib_giant = 524327

    	PM in MIB giant report

    .. data:: report_in_mib_jabber = 524328

    	PM in MIB jabber report

    .. data:: report_in_mib_crc = 524329

    	PM in MIB CRC report

    .. data:: report_in_error_collision_s = 524330

    	PM in error collisions report

    .. data:: report_in_error_symbol = 524331

    	PM in error symbol report

    .. data:: report_out_go_od_bytes = 524332

    	PM out good bytes report

    .. data:: report_out_802_1q_frame_s = 524333

    	PM out 802_1 Q report

    .. data:: report_out_pause_frame_s = 524334

    	PM out pause frame report

    .. data:: report_out_pkts_1519_max_octets = 524335

    	PM out pkts 1519 max octets report

    .. data:: report_out_go_od_pkts = 524336

    	PM out good pkts report

    .. data:: report_out_drop_under_run = 524337

    	PM out drop underrun report

    .. data:: report_out_drop_abort = 524338

    	PM out drop abort report

    .. data:: report_out_drop_other = 524339

    	PM out drop other report

    .. data:: report_out_error_other = 524340

    	PM out error other report

    .. data:: report_in_error_giant = 524341

    	PM in error giant report

    .. data:: report_in_error_runt = 524342

    	PM in error runt report

    .. data:: report_in_error_jabbers = 524343

    	PM in error jabber report

    .. data:: report_in_error_fragments = 524344

    	PM in error fragments report

    .. data:: report_in_error_other = 524345

    	PM in error other report

    .. data:: report_in_pkt_64_octet = 524346

    	PM in pkt 64 octet report

    .. data:: report_in_pkts_65_127octets = 524347

    	PM in pkts 65_127 octets report

    .. data:: report_in_pkts_128_255_octets = 524348

    	PM in pkts 128_255 octets report

    .. data:: report_in_pkts_256_511_octets = 524349

    	PM in pkts 256_511 octets report

    .. data:: report_in_pkts_512_1023_octets = 524350

    	PM in pkts 512_1023 octets report

    .. data:: report_in_pkts_1024_1518_octets = 524351

    	PM in pkts 1024_1058 octets report

    .. data:: report_out_pkt_64_octet = 524352

    	PM out pkt 64 octet report

    .. data:: report_out_pkts_65_127octets = 524353

    	PM out pkts 65_127 octets report

    .. data:: report_out_pkts_128_255_octets = 524354

    	PM out pkts 128_255 octets report

    .. data:: report_out_pkts_256_511_octets = 524355

    	PM out pkts 256_511 octets report

    .. data:: report_out_pkts_512_1023_octets = 524356

    	PM out pkts 512_1023 octets report

    .. data:: report_out_pkts_1024_1518_octets = 524357

    	PM out pkts 1024_1058 octets report

    .. data:: report_tx_under_size_d_pkt = 524358

    	PM tx undersized pkt report

    .. data:: report_tx_over_size_d_pkt = 524359

    	PM tx oversized pkt report

    .. data:: report_tx_fragments = 524360

    	PM tx fragments report

    .. data:: report_tx_jabber = 524361

    	PM tx jabber report

    .. data:: report_tx_bad_fcs = 524362

    	PM tx bad fcs report

    """

    report_rx_pkt = 524288

    report_rx_util = 524289

    report_tx_util = 524290

    report_stat_pkt = 524291

    report_octet_stat = 524292

    report_over_size_pkt = 524293

    report_fcs_err = 524294

    report_long_frame_s = 524295

    report_jabber_stats = 524296

    report_64_octet = 524297

    report_65_127_octet = 524298

    report_128_255_octet = 524299

    report_256_511_octet = 524300

    report_512_1023_octet = 524301

    report_1024_1518_octet = 524302

    report_in_ucast = 524303

    report_in_mcast = 524304

    report_in_bcast = 524305

    report_out_ucast = 524306

    report_out_mcast = 524307

    report_out_bcast = 524308

    report_tx_pkt = 524309

    report_ifin_error_s = 524310

    report_ifin_octets = 524311

    report_ether_stat_multicast_pkt = 524312

    report_ether_stat_broadcast_pkt = 524313

    report_ether_stat_under_size_d_pkt = 524314

    report_out_octet = 524315

    report_in_pause_frame = 524316

    report_in_go_od_bytes = 524317

    report_in_802_1q_frame_s = 524318

    report_in_pkts_1519_max_octets = 524319

    report_in_go_od_pkts = 524320

    report_in_drop_overrun = 524321

    report_in_drop_abort = 524322

    report_in_drop_invalid_vlan = 524323

    report_in_drop_invalid_dmac = 524324

    report_in_drop_invalid_encap = 524325

    report_in_drop_other = 524326

    report_in_mib_giant = 524327

    report_in_mib_jabber = 524328

    report_in_mib_crc = 524329

    report_in_error_collision_s = 524330

    report_in_error_symbol = 524331

    report_out_go_od_bytes = 524332

    report_out_802_1q_frame_s = 524333

    report_out_pause_frame_s = 524334

    report_out_pkts_1519_max_octets = 524335

    report_out_go_od_pkts = 524336

    report_out_drop_under_run = 524337

    report_out_drop_abort = 524338

    report_out_drop_other = 524339

    report_out_error_other = 524340

    report_in_error_giant = 524341

    report_in_error_runt = 524342

    report_in_error_jabbers = 524343

    report_in_error_fragments = 524344

    report_in_error_other = 524345

    report_in_pkt_64_octet = 524346

    report_in_pkts_65_127octets = 524347

    report_in_pkts_128_255_octets = 524348

    report_in_pkts_256_511_octets = 524349

    report_in_pkts_512_1023_octets = 524350

    report_in_pkts_1024_1518_octets = 524351

    report_out_pkt_64_octet = 524352

    report_out_pkts_65_127octets = 524353

    report_out_pkts_128_255_octets = 524354

    report_out_pkts_256_511_octets = 524355

    report_out_pkts_512_1023_octets = 524356

    report_out_pkts_1024_1518_octets = 524357

    report_tx_under_size_d_pkt = 524358

    report_tx_over_size_d_pkt = 524359

    report_tx_fragments = 524360

    report_tx_jabber = 524361

    report_tx_bad_fcs = 524362


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherReportEnum']


class EtherThresholdEnum(Enum):
    """
    EtherThresholdEnum

    Ether threshold

    .. data:: thresh_rx_pkt = 8388608

    	PM Ether rx pkt threshold

    .. data:: thresh_rx_util = 8388609

    	PM Ether rx util threshold

    .. data:: thresh_tx_util = 8388610

    	PM Ether tx util threshold

    .. data:: thresh_stat_pkt = 8388611

    	PM ether stat pkt threshold

    .. data:: thresh_octet_stat = 8388612

    	PM Ether octet stat threshold

    .. data:: thresh_over_size_pkt = 8388613

    	PM Ether oversize pkt threshold

    .. data:: thresh_fcs_err = 8388614

    	PMEther fcs error threshold

    .. data:: thresh_long_frame_s = 8388615

    	PM Ether long frames threshold

    .. data:: thresh_jabber_stats = 8388616

    	PM Ether jabber stats threshold

    .. data:: thresh_64_octet = 8388617

    	PM Ether 64 octet threshold

    .. data:: thresh_65_127_octet = 8388618

    	PM Ether 65 to 127 octet threshold

    .. data:: thresh_128_255_octet = 8388619

    	PM Ether 128 to 255 octet threshold

    .. data:: thresh_256_511_octet = 8388620

    	PM Ether 256 to 511 octet threshold

    .. data:: thresh_512_1023_octet = 8388621

    	PM Ether 512 to 1023 octet threshold

    .. data:: thresh_1024_1518_octet = 8388622

    	PM Ether 1024 to 1518 threshold

    .. data:: thresh_in_ucast = 8388623

    	PM Ether rx ucast threshold

    .. data:: thresh_in_mcast = 8388624

    	PM Ether rx mcast threshold

    .. data:: thresh_in_bcast = 8388625

    	PM Ether rx bcast threshold

    .. data:: thresh_out_ucast = 8388626

    	PM Ether tx ucast threshold

    .. data:: thresh_out_mcast = 8388627

    	PM Ether tx mcast threshold

    .. data:: thresh_out_bcast = 8388628

    	PM Ether tx bcast threshold

    .. data:: thresh_tx_pkt = 8388629

    	PM Ether tx pkt threshold

    .. data:: thresh_ifin_error_s = 8388630

    	PM ether ifIn errors threshold

    .. data:: thresh_ifin_octets = 8388631

    	PM ether ifInOctets threshold

    .. data:: thresh_ether_stat_multicast_pkt = 8388632

    	PM ether stat multicast pkt threshold

    .. data:: thresh_ether_stat_broadcast_pkt = 8388633

    	PM ether stat broadcast pkt threshold

    .. data:: thresh_ether_stat_under_size_d_pkt = 8388634

    	PM ether stat undersized pkt threshold

    .. data:: thresh_out_octet = 8388635

    	PM ether out octets threshold

    .. data:: thresh_in_pause_frame = 8388636

    	PM in pause frame threshold

    .. data:: thresh_in_go_od_bytes = 8388637

    	PM in good bytes threshold

    .. data:: thresh_in_802_1q_frame_s = 8388638

    	PM in 802_1 Q threshold

    .. data:: thresh_in_pkts_1519_max_octets = 8388639

    	PM in pkts 1519 max octets threshold

    .. data:: thresh_in_go_od_pkts = 8388640

    	PM in good pkts threshold

    .. data:: thresh_in_drop_overrun = 8388641

    	PM in drop overrun threshold

    .. data:: thresh_in_drop_abort = 8388642

    	PM in drop abort threshold

    .. data:: thresh_in_drop_invalid_vlan = 8388643

    	PM in drop invalid vlan threshold

    .. data:: thresh_in_drop_invalid_dmac = 8388644

    	PM in drop invalid DMAC threshold

    .. data:: thresh_in_drop_invalid_encap = 8388645

    	PM in drop invalid encap threshold

    .. data:: thresh_in_drop_other = 8388646

    	PM in drop other threshold

    .. data:: thresh_in_mib_giant = 8388647

    	PM in MIB giant threshold

    .. data:: thresh_in_mib_jabber = 8388648

    	PM in MIB jabber threshold

    .. data:: thresh_in_mib_crc = 8388649

    	PM in MIB CRC threshold

    .. data:: thresh_in_error_collision_s = 8388650

    	PM in error collisions threshold

    .. data:: thresh_in_error_symbol = 8388651

    	PM in error symbol threshold

    .. data:: thresh_out_go_od_bytes = 8388652

    	PM out good bytes threshold

    .. data:: thresh_out_802_1q_frame_s = 8388653

    	PM out 802_1 Q threshold

    .. data:: thresh_out_pause_frame_s = 8388654

    	PM out pause frame threshold

    .. data:: thresh_out_pkts_1519_max_octets = 8388655

    	PM out pkts 1519 max octets threshold

    .. data:: thresh_out_go_od_pkts = 8388656

    	PM out good pkts threshold

    .. data:: thresh_out_drop_under_run = 8388657

    	PM out drop underrun threshold

    .. data:: thresh_out_drop_abort = 8388658

    	PM out drop abort threshold

    .. data:: thresh_out_drop_other = 8388659

    	PM out drop other threshold

    .. data:: thresh_out_error_other = 8388660

    	PM out error other threshold

    .. data:: thresh_in_error_giant = 8388661

    	PM in error giant threshold

    .. data:: thresh_in_error_runt = 8388662

    	PM in error runt threshold

    .. data:: thresh_in_error_jabbers = 8388663

    	PM in error jabber threshold

    .. data:: thresh_in_error_fragments = 8388664

    	PM in error fragments threshold

    .. data:: thresh_in_error_other = 8388665

    	PM in error other threshold

    .. data:: thresh_in_pkt_64_octet = 8388666

    	PM in pkt 64 octet threshold

    .. data:: thresh_in_pkts_65_127octets = 8388667

    	PM in pkts 65_127 octets threshold

    .. data:: thresh_in_pkts_128_255_octets = 8388668

    	PM in pkts 128_255 octets threshold

    .. data:: thresh_in_pkts_256_511_octets = 8388669

    	PM in pkts 256_511 octets threshold

    .. data:: thresh_in_pkts_512_1023_octets = 8388670

    	PM in pkts 512_1023 octets threshold

    .. data:: thresh_in_pkts_1024_1518_octets = 8388671

    	PM in pkts 1024_1058 octets threshold

    .. data:: thresh_out_pkt_64_octet = 8388672

    	PM out pkt 64 octet threshold

    .. data:: thresh_out_pkts_65_127octets = 8388673

    	PM out pkts 65_127 octets threshold

    .. data:: thresh_out_pkts_128_255_octets = 8388674

    	PM out pkts 128_255 octets threshold

    .. data:: thresh_out_pkts_256_511_octets = 8388675

    	PM out pkts 256_511 octets threshold

    .. data:: thresh_out_pkts_512_1023_octets = 8388676

    	PM out pkts 512_1023 octets threshold

    .. data:: thresh_out_pkts_1024_1518_octets = 8388677

    	PM out pkts 1024_1058 octets threshold

    .. data:: thresh_tx_under_size_d_pkt = 8388678

    	PM tx undersized pkt threshold

    .. data:: thresh_tx_over_size_d_pkt = 8388679

    	PM tx oversized pkt threshold

    .. data:: thresh_tx_fragments = 8388680

    	PM tx fragments threshold

    .. data:: thresh_tx_jabber = 8388681

    	PM tx jabber threshold

    .. data:: thresh_tx_bad_fcs = 8388682

    	PM tx bad fcs threshold

    """

    thresh_rx_pkt = 8388608

    thresh_rx_util = 8388609

    thresh_tx_util = 8388610

    thresh_stat_pkt = 8388611

    thresh_octet_stat = 8388612

    thresh_over_size_pkt = 8388613

    thresh_fcs_err = 8388614

    thresh_long_frame_s = 8388615

    thresh_jabber_stats = 8388616

    thresh_64_octet = 8388617

    thresh_65_127_octet = 8388618

    thresh_128_255_octet = 8388619

    thresh_256_511_octet = 8388620

    thresh_512_1023_octet = 8388621

    thresh_1024_1518_octet = 8388622

    thresh_in_ucast = 8388623

    thresh_in_mcast = 8388624

    thresh_in_bcast = 8388625

    thresh_out_ucast = 8388626

    thresh_out_mcast = 8388627

    thresh_out_bcast = 8388628

    thresh_tx_pkt = 8388629

    thresh_ifin_error_s = 8388630

    thresh_ifin_octets = 8388631

    thresh_ether_stat_multicast_pkt = 8388632

    thresh_ether_stat_broadcast_pkt = 8388633

    thresh_ether_stat_under_size_d_pkt = 8388634

    thresh_out_octet = 8388635

    thresh_in_pause_frame = 8388636

    thresh_in_go_od_bytes = 8388637

    thresh_in_802_1q_frame_s = 8388638

    thresh_in_pkts_1519_max_octets = 8388639

    thresh_in_go_od_pkts = 8388640

    thresh_in_drop_overrun = 8388641

    thresh_in_drop_abort = 8388642

    thresh_in_drop_invalid_vlan = 8388643

    thresh_in_drop_invalid_dmac = 8388644

    thresh_in_drop_invalid_encap = 8388645

    thresh_in_drop_other = 8388646

    thresh_in_mib_giant = 8388647

    thresh_in_mib_jabber = 8388648

    thresh_in_mib_crc = 8388649

    thresh_in_error_collision_s = 8388650

    thresh_in_error_symbol = 8388651

    thresh_out_go_od_bytes = 8388652

    thresh_out_802_1q_frame_s = 8388653

    thresh_out_pause_frame_s = 8388654

    thresh_out_pkts_1519_max_octets = 8388655

    thresh_out_go_od_pkts = 8388656

    thresh_out_drop_under_run = 8388657

    thresh_out_drop_abort = 8388658

    thresh_out_drop_other = 8388659

    thresh_out_error_other = 8388660

    thresh_in_error_giant = 8388661

    thresh_in_error_runt = 8388662

    thresh_in_error_jabbers = 8388663

    thresh_in_error_fragments = 8388664

    thresh_in_error_other = 8388665

    thresh_in_pkt_64_octet = 8388666

    thresh_in_pkts_65_127octets = 8388667

    thresh_in_pkts_128_255_octets = 8388668

    thresh_in_pkts_256_511_octets = 8388669

    thresh_in_pkts_512_1023_octets = 8388670

    thresh_in_pkts_1024_1518_octets = 8388671

    thresh_out_pkt_64_octet = 8388672

    thresh_out_pkts_65_127octets = 8388673

    thresh_out_pkts_128_255_octets = 8388674

    thresh_out_pkts_256_511_octets = 8388675

    thresh_out_pkts_512_1023_octets = 8388676

    thresh_out_pkts_1024_1518_octets = 8388677

    thresh_tx_under_size_d_pkt = 8388678

    thresh_tx_over_size_d_pkt = 8388679

    thresh_tx_fragments = 8388680

    thresh_tx_jabber = 8388681

    thresh_tx_bad_fcs = 8388682


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherThresholdEnum']


class FecReportEnum(Enum):
    """
    FecReportEnum

    Fec report

    .. data:: report_ec_bits = 131072

    	PM Fec ec bits report

    .. data:: report_uc_words = 131076

    	PM Fec uc words report

    .. data:: report_pre_fec_ber_max = 131081

    	PM Fec pre fec ber max report

    .. data:: report_post_fec_ber_max = 131082

    	PM Fec post fec ber max report

    .. data:: report_q_max = 131083

    	PM Fec Q max report

    .. data:: report_q_margin_max = 131084

    	PM Fec Q_margin max report

    .. data:: report_pre_fec_ber_min = 131085

    	PM Fec pre fec ber min report

    .. data:: report_post_fec_ber_min = 131086

    	PM Fec post fec ber min report

    .. data:: report_q_min = 131087

    	PM Fec Q min report

    .. data:: report_q_margin_min = 131088

    	PM Fec Q_margin min report

    """

    report_ec_bits = 131072

    report_uc_words = 131076

    report_pre_fec_ber_max = 131081

    report_post_fec_ber_max = 131082

    report_q_max = 131083

    report_q_margin_max = 131084

    report_pre_fec_ber_min = 131085

    report_post_fec_ber_min = 131086

    report_q_min = 131087

    report_q_margin_min = 131088


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecReportEnum']


class FecThresholdEnum(Enum):
    """
    FecThresholdEnum

    Fec threshold

    .. data:: thresh_ec_bits = 131072

    	PM Fec ec bits threshold

    .. data:: thresh_uc_words = 131076

    	PM Fec uc words threshold

    .. data:: thresh_pre_fec_ber_max = 131081

    	PM Fec pre-fe-ber max threshold

    .. data:: thresh_post_fec_ber_max = 131082

    	PM Fec post-fec-ber max threshold

    .. data:: thresh_q_max = 131083

    	PM Fec Q max threshold

    .. data:: thresh_q_margin_max = 131084

    	PM Fec uc words max threshold

    .. data:: thresh_pre_fec_ber_min = 131085

    	PM Fec pre-fe-ber min threshold

    .. data:: thresh_post_fec_ber_min = 131086

    	PM Fec post-fec-ber min threshold

    .. data:: thresh_q_min = 131087

    	PM Fec Q min threshold

    .. data:: thresh_q_margin_min = 131088

    	PM Fec uc words min threshold

    """

    thresh_ec_bits = 131072

    thresh_uc_words = 131076

    thresh_pre_fec_ber_max = 131081

    thresh_post_fec_ber_max = 131082

    thresh_q_max = 131083

    thresh_q_margin_max = 131084

    thresh_pre_fec_ber_min = 131085

    thresh_post_fec_ber_min = 131086

    thresh_q_min = 131087

    thresh_q_margin_min = 131088


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecThresholdEnum']


class GfpReportEnum(Enum):
    """
    GfpReportEnum

    Gfp report

    .. data:: report_rx_bit_err = 6291456

    	PM GFP rx bit err report

    .. data:: report_rx_inv_typ = 6291457

    	PM GFP rx inv type report

    .. data:: report_rx_crc = 6291458

    	PM GFP rx crc report

    .. data:: report_rx_lfd = 6291459

    	PM GFP rx lfd report

    .. data:: report_rx_csf = 6291460

    	PM GFP rx csf report

    """

    report_rx_bit_err = 6291456

    report_rx_inv_typ = 6291457

    report_rx_crc = 6291458

    report_rx_lfd = 6291459

    report_rx_csf = 6291460


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpReportEnum']


class GfpThresholdEnum(Enum):
    """
    GfpThresholdEnum

    Gfp threshold

    .. data:: thresh_rx_bit_err = 67108864

    	PM GFP rx bit err threshold

    .. data:: thresh_rx_inv_typ = 67108865

    	PM GFP rx inv type threshold

    .. data:: thresh_rx_crc = 67108866

    	PM GFP rx crc threshold

    .. data:: thresh_rx_lfd = 67108867

    	PM GFP rx lfd threshold

    .. data:: thresh_rx_csf = 67108868

    	PM GFP rx csf threshold

    """

    thresh_rx_bit_err = 67108864

    thresh_rx_inv_typ = 67108865

    thresh_rx_crc = 67108866

    thresh_rx_lfd = 67108867

    thresh_rx_csf = 67108868


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpThresholdEnum']


class HoVcReportEnum(Enum):
    """
    HoVcReportEnum

    Ho vc report

    .. data:: report_eb = 33554432

    	PM EB report

    .. data:: report_es = 33554433

    	PM ES report

    .. data:: report_esr = 33554434

    	PM ESR report

    .. data:: report_ses = 33554435

    	PM SES report

    .. data:: report_sesr = 33554436

    	PM SESR report

    .. data:: report_bbe = 33554437

    	PM BBE report

    .. data:: report_bber = 33554438

    	PM BBER report

    .. data:: report_uass = 33554439

    	PM UASS report

    """

    report_eb = 33554432

    report_es = 33554433

    report_esr = 33554434

    report_ses = 33554435

    report_sesr = 33554436

    report_bbe = 33554437

    report_bber = 33554438

    report_uass = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcReportEnum']


class HoVcThresholdEnum(Enum):
    """
    HoVcThresholdEnum

    Ho vc threshold

    .. data:: thresh_eb = 33554432

    	PM EB threshold

    .. data:: thresh_es = 33554433

    	PM ES threshold

    .. data:: thresh_esr = 33554434

    	PM ESR threshold

    .. data:: thresh_ses = 33554435

    	PM SES threshold

    .. data:: thresh_sesr = 33554436

    	PM SESR threshold

    .. data:: thresh_bbe = 33554437

    	PM BBE threshold

    .. data:: thresh_bber = 33554438

    	PM BBER threshold

    .. data:: thresh_uass = 33554439

    	PM UASS threshold

    """

    thresh_eb = 33554432

    thresh_es = 33554433

    thresh_esr = 33554434

    thresh_ses = 33554435

    thresh_sesr = 33554436

    thresh_bbe = 33554437

    thresh_bber = 33554438

    thresh_uass = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcThresholdEnum']


class OcnReportEnum(Enum):
    """
    OcnReportEnum

    Ocn report

    .. data:: report_sefss = 3145728

    	PM SEFSS threshold

    .. data:: report_cvs = 3145729

    	PM CVS threshold

    .. data:: report_ess = 3145730

    	PM ESS threshold

    .. data:: report_sess = 3145731

    	PM SESS threshold

    .. data:: report_cvl_ne = 3145734

    	PM CVL-NE threshold

    .. data:: report_esl_ne = 3145735

    	PM ESL-NE threshold

    .. data:: report_sesl_ne = 3145736

    	PM SESL-NE threshold

    .. data:: report_uasl_ne = 3145738

    	PM UASL-NE threshold

    .. data:: report_fcl_ne = 3145739

    	PM FCL-NE threshold

    .. data:: report_fcl_fe = 3145751

    	PM FCL_FE threshold

    .. data:: report_cvl_fe = 3145752

    	PM CVL-FE threshold

    .. data:: report_esl_fe = 3145753

    	PM ESL_FE threshold

    .. data:: report_sesl_fe = 3145754

    	PM SESL_FE threshold

    .. data:: report_uasl_fe = 3145756

    	PM UASL_FEthreshold

    """

    report_sefss = 3145728

    report_cvs = 3145729

    report_ess = 3145730

    report_sess = 3145731

    report_cvl_ne = 3145734

    report_esl_ne = 3145735

    report_sesl_ne = 3145736

    report_uasl_ne = 3145738

    report_fcl_ne = 3145739

    report_fcl_fe = 3145751

    report_cvl_fe = 3145752

    report_esl_fe = 3145753

    report_sesl_fe = 3145754

    report_uasl_fe = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnReportEnum']


class OcnThresholdEnum(Enum):
    """
    OcnThresholdEnum

    Ocn threshold

    .. data:: thresh_sefss = 3145728

    	PM SEFSS threshold

    .. data:: thresh_cvs = 3145729

    	PM CVS threshold

    .. data:: thresh_ess = 3145730

    	PM ESS threshold

    .. data:: thresh_sess = 3145731

    	PM SESS threshold

    .. data:: thresh_cvl_ne = 3145734

    	PM CVL-NE threshold

    .. data:: thresh_esl_ne = 3145735

    	PM ESL-NE threshold

    .. data:: thresh_sesl_ne = 3145736

    	PM SESL-NE threshold

    .. data:: thresh_uasl_ne = 3145738

    	PM UASL-NE threshold

    .. data:: thresh_fcl_ne = 3145739

    	PM FCL-NE threshold

    .. data:: thresh_fcl_fe = 3145751

    	PM FCL_FE threshold

    .. data:: thresh_cvl_fe = 3145752

    	PM CVL-FE threshold

    .. data:: thresh_esl_fe = 3145753

    	PM ESL_FE threshold

    .. data:: thresh_sesl_fe = 3145754

    	PM SESL_FE threshold

    .. data:: thresh_uasl_fe = 3145756

    	PM UASL_FEthreshold

    """

    thresh_sefss = 3145728

    thresh_cvs = 3145729

    thresh_ess = 3145730

    thresh_sess = 3145731

    thresh_cvl_ne = 3145734

    thresh_esl_ne = 3145735

    thresh_sesl_ne = 3145736

    thresh_uasl_ne = 3145738

    thresh_fcl_ne = 3145739

    thresh_fcl_fe = 3145751

    thresh_cvl_fe = 3145752

    thresh_esl_fe = 3145753

    thresh_sesl_fe = 3145754

    thresh_uasl_fe = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnThresholdEnum']


class OpticsReportEnum(Enum):
    """
    OpticsReportEnum

    Optics report

    .. data:: report_opt_min = 65552

    	PM Optics opt min report

    .. data:: report_opr_min = 65553

    	PM Optics opr min report

    .. data:: report_lbc_min = 65554

    	PM Optics lbc min report

    .. data:: report_lbc_pc_min = 65555

    	PM Optics lbcpc min report

    .. data:: report_cd_min = 65559

    	PM Optics cd min report

    .. data:: report_dgd_min = 65560

    	PM Optics dgd min report

    .. data:: report_pmd_min = 65561

    	PM Optics sopmd min report

    .. data:: report_osnr_min = 65562

    	PM Optics osnr min report

    .. data:: report_pdl_min = 65563

    	PM Optics pdl min report

    .. data:: report_pcr_min = 65564

    	PM Optics pcr min report

    .. data:: report_pn_min = 65565

    	PM Optics pn min report

    .. data:: report_rx_sig_pow_min = 65566

    	PM Optics rx sig pow min report

    .. data:: report_low_sig_freq_off_min = 65567

    	PM Optics low sig freq off min report

    .. data:: report_opt_max = 65568

    	PM Optics opt max report

    .. data:: report_opr_max = 65569

    	PM Optics opr max report

    .. data:: report_lbc_max = 65570

    	PM Optics lbc max report

    .. data:: report_lbc_pc_max = 65571

    	PM Optics lbcpc max report

    .. data:: report_cd_max = 65575

    	PM Optics cd max report

    .. data:: report_dgd_max = 65576

    	PM Optics dgd max report

    .. data:: report_pmd_max = 65577

    	PM Optics sopmd max report

    .. data:: report_osnr_max = 65578

    	PM Optics osnr max report

    .. data:: report_pdl_max = 65579

    	PM Optics pdl max report

    .. data:: report_pcr_max = 65580

    	PM Optics pcr max report

    .. data:: report_pn_max = 65581

    	PM Optics pn max report

    .. data:: report_rx_sig_pow_max = 65582

    	PM Optics rx sig pow max report

    .. data:: report_low_sig_freq_off_max = 65583

    	PM Optics low sig freq off max report

    """

    report_opt_min = 65552

    report_opr_min = 65553

    report_lbc_min = 65554

    report_lbc_pc_min = 65555

    report_cd_min = 65559

    report_dgd_min = 65560

    report_pmd_min = 65561

    report_osnr_min = 65562

    report_pdl_min = 65563

    report_pcr_min = 65564

    report_pn_min = 65565

    report_rx_sig_pow_min = 65566

    report_low_sig_freq_off_min = 65567

    report_opt_max = 65568

    report_opr_max = 65569

    report_lbc_max = 65570

    report_lbc_pc_max = 65571

    report_cd_max = 65575

    report_dgd_max = 65576

    report_pmd_max = 65577

    report_osnr_max = 65578

    report_pdl_max = 65579

    report_pcr_max = 65580

    report_pn_max = 65581

    report_rx_sig_pow_max = 65582

    report_low_sig_freq_off_max = 65583


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsReportEnum']


class OpticsThresholdEnum(Enum):
    """
    OpticsThresholdEnum

    Optics threshold

    .. data:: thresh_opt_min = 65552

    	PM Optics opt min threshold in dbm or uW

    .. data:: thresh_opr_min = 65553

    	PM Optics opr min threshold in dbm or uW

    .. data:: thresh_lbc_min = 65554

    	PM Optics lbc min threshold

    .. data:: thresh_lbc_pc_min = 65555

    	PM Optics lbcpc min threshold

    .. data:: thresh_cd_min = 65559

    	PM Optics cd min threshold

    .. data:: thresh_dgd_min = 65560

    	PM Optics dgd min threshold

    .. data:: thresh_pmd_min = 65561

    	PM Optics sopmd min threshold

    .. data:: thresh_osnr_min = 65562

    	PM Optics osnr min threshold

    .. data:: thresh_pdl_min = 65563

    	PM Optics pdl min threshold

    .. data:: thresh_pcr_min = 65564

    	PM Optics pcr min threshold

    .. data:: thresh_pn_min = 65565

    	PM Optics pn min threshold

    .. data:: thresh_rx_sig_pow_min = 65566

    	PM Optics rx sig pow min threshold

    .. data:: thresh_low_sig_freq_off_min = 65567

    	PM Optics low sig freq off min threshold

    .. data:: thresh_opt_max = 65568

    	PM Optics opt max threshold in dbm or uW

    .. data:: thresh_opr_max = 65569

    	PM Optics opr max threshold in dbm or uW

    .. data:: thresh_lbc_max = 65570

    	PM Optics lbc max threshold

    .. data:: thresh_lbc_pc_max = 65571

    	PM Optics lbcpc max threshold

    .. data:: thresh_cd_max = 65575

    	PM Optics cd max threshold

    .. data:: thresh_dgd_max = 65576

    	PM Optics dgd max threshold

    .. data:: thresh_pmd_max = 65577

    	PM Optics sopmd max threshold

    .. data:: thresh_osnr_max = 65578

    	PM Optics osnr max threshold

    .. data:: thresh_pdl_max = 65579

    	PM Optics pdl max threshold

    .. data:: thresh_pcr_max = 65580

    	PM Optics pcr max threshold

    .. data:: thresh_pn_max = 65581

    	PM Optics pn max threshold

    .. data:: thresh_rx_sig_pow_max = 65582

    	PM Optics rx sig pow max threshold

    .. data:: thresh_low_sig_freq_off_max = 65583

    	PM Optics low sig freq off max threshold

    """

    thresh_opt_min = 65552

    thresh_opr_min = 65553

    thresh_lbc_min = 65554

    thresh_lbc_pc_min = 65555

    thresh_cd_min = 65559

    thresh_dgd_min = 65560

    thresh_pmd_min = 65561

    thresh_osnr_min = 65562

    thresh_pdl_min = 65563

    thresh_pcr_min = 65564

    thresh_pn_min = 65565

    thresh_rx_sig_pow_min = 65566

    thresh_low_sig_freq_off_min = 65567

    thresh_opt_max = 65568

    thresh_opr_max = 65569

    thresh_lbc_max = 65570

    thresh_lbc_pc_max = 65571

    thresh_cd_max = 65575

    thresh_dgd_max = 65576

    thresh_pmd_max = 65577

    thresh_osnr_max = 65578

    thresh_pdl_max = 65579

    thresh_pcr_max = 65580

    thresh_pn_max = 65581

    thresh_rx_sig_pow_max = 65582

    thresh_low_sig_freq_off_max = 65583


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsThresholdEnum']


class OtnReportEnum(Enum):
    """
    OtnReportEnum

    Otn report

    .. data:: report_es_sm_ne = 262144

    	PM Otn es sm ne report

    .. data:: report_ses_sm_ne = 262145

    	PM Otn ses sm ne report

    .. data:: report_uas_sm_ne = 262146

    	PM Otn uas sm ne report

    .. data:: report_bbe_sm_ne = 262147

    	PM Otn bbe sm ne report

    .. data:: report_fc_sm_ne = 262148

    	PM Otn fc sm ne report

    .. data:: report_esr_sm_ne = 262149

    	PM Otn esr sm ne report

    .. data:: report_sesr_sm_ne = 262150

    	PM Otn sesr sm ne report

    .. data:: report_bber_sm_ne = 262151

    	PM Otn bber sm ne report

    .. data:: report_es_pm_ne = 524288

    	PM Otn es pm ne report

    .. data:: report_ses_pm_ne = 524289

    	PM Otn ses pm ne report

    .. data:: report_uas_pm_ne = 524290

    	PM Otn uas pm ne report

    .. data:: report_bbe_pm_ne = 524291

    	PM Otn bbe pm ne report

    .. data:: report_fc_pm_ne = 524292

    	PM Otn fc pm ne report

    .. data:: report_esr_pm_ne = 524293

    	PM Otn esr pm ne report

    .. data:: report_sesr_pm_ne = 524294

    	PM Otn sesr pm ne report

    .. data:: report_bber_pm_ne = 524295

    	PM Otn bber pm ne report

    .. data:: report_es_sm_fe = 1048584

    	PM Otn es sm fe report

    .. data:: report_ses_sm_fe = 1048585

    	PM Otn ses sm fe report

    .. data:: report_uas_sm_fe = 1048586

    	PM Otn uas sm fe report

    .. data:: report_bbe_sm_fe = 1048587

    	PM Otn bbe sm fe report

    .. data:: report_fc_sm_fe = 1048588

    	PM Otn fc sm fe report

    .. data:: report_esr_sm_fe = 1048589

    	PM Otn esr sm fe report

    .. data:: report_sesr_sm_fe = 1048590

    	PM Otn sesr sm fe report

    .. data:: report_bber_sm_fe = 1048591

    	PM Otn bber sm fe report

    .. data:: report_es_pm_fe = 2097160

    	PM Otn es pm fe report

    .. data:: report_ses_pm_fe = 2097161

    	PM Otn ses pm fe report

    .. data:: report_uas_pm_fe = 2097162

    	PM Otn uas pm fe report

    .. data:: report_bbe_pm_fe = 2097163

    	PM Otn bbe pm fe report

    .. data:: report_fc_pm_fe = 2097164

    	PM Otn fc pm fe report

    .. data:: report_esr_pm_fe = 2097165

    	PM Otn esr pm fe report

    .. data:: report_sesr_pm_fe = 2097166

    	PM Otn sesr pm fe report

    .. data:: report_bber_pm_fe = 2097167

    	PM Otn bber pm fe report

    """

    report_es_sm_ne = 262144

    report_ses_sm_ne = 262145

    report_uas_sm_ne = 262146

    report_bbe_sm_ne = 262147

    report_fc_sm_ne = 262148

    report_esr_sm_ne = 262149

    report_sesr_sm_ne = 262150

    report_bber_sm_ne = 262151

    report_es_pm_ne = 524288

    report_ses_pm_ne = 524289

    report_uas_pm_ne = 524290

    report_bbe_pm_ne = 524291

    report_fc_pm_ne = 524292

    report_esr_pm_ne = 524293

    report_sesr_pm_ne = 524294

    report_bber_pm_ne = 524295

    report_es_sm_fe = 1048584

    report_ses_sm_fe = 1048585

    report_uas_sm_fe = 1048586

    report_bbe_sm_fe = 1048587

    report_fc_sm_fe = 1048588

    report_esr_sm_fe = 1048589

    report_sesr_sm_fe = 1048590

    report_bber_sm_fe = 1048591

    report_es_pm_fe = 2097160

    report_ses_pm_fe = 2097161

    report_uas_pm_fe = 2097162

    report_bbe_pm_fe = 2097163

    report_fc_pm_fe = 2097164

    report_esr_pm_fe = 2097165

    report_sesr_pm_fe = 2097166

    report_bber_pm_fe = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnReportEnum']


class OtnTcmReportEnum(Enum):
    """
    OtnTcmReportEnum

    Otn tcm report

    .. data:: report_es_tcm_fe = 16777224

    	PM Otn es TCM fe report

    .. data:: report_ses_tcm_fe = 16777225

    	PM Otn ses TCM fe report

    .. data:: report_uas_tcm_fe = 16777226

    	PM Otn uas TCM fe report

    .. data:: report_bbe_tcm_fe = 16777227

    	PM Otn bbe TCM fe report

    .. data:: report_fc_tcm_fe = 16777228

    	PM Otn fc TCM fe report

    .. data:: report_esr_tcm_fe = 16777229

    	PM Otn esr TCM fe report

    .. data:: report_sesr_tcm_fe = 16777230

    	PM Otn sesr TCM fe report

    .. data:: report_bber_tcm_fe = 16777231

    	PM Otn bber TCM fe report

    .. data:: report_es_tcm_ne = 33554432

    	PM Otn es TCM ne report

    .. data:: report_ses_tcm_ne = 33554433

    	PM Otn ses TCM ne report

    .. data:: report_uas_tcm_ne = 33554434

    	PM Otn uas TCM ne report

    .. data:: report_bbe_tcm_ne = 33554435

    	PM Otn bbe TCM ne report

    .. data:: report_fc_tcm_ne = 33554436

    	PM Otn fc TCM ne report

    .. data:: report_esr_tcm_ne = 33554437

    	PM Otn esr TCM ne report

    .. data:: report_sesr_tcm_ne = 33554438

    	PM Otn sesr TCM ne report

    .. data:: report_bber_tcm_ne = 33554439

    	PM Otn bber TCM ne report

    """

    report_es_tcm_fe = 16777224

    report_ses_tcm_fe = 16777225

    report_uas_tcm_fe = 16777226

    report_bbe_tcm_fe = 16777227

    report_fc_tcm_fe = 16777228

    report_esr_tcm_fe = 16777229

    report_sesr_tcm_fe = 16777230

    report_bber_tcm_fe = 16777231

    report_es_tcm_ne = 33554432

    report_ses_tcm_ne = 33554433

    report_uas_tcm_ne = 33554434

    report_bbe_tcm_ne = 33554435

    report_fc_tcm_ne = 33554436

    report_esr_tcm_ne = 33554437

    report_sesr_tcm_ne = 33554438

    report_bber_tcm_ne = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmReportEnum']


class OtnTcmThresholdEnum(Enum):
    """
    OtnTcmThresholdEnum

    Otn tcm threshold

    .. data:: thresh_es_tcm_fe = 16777224

    	PM Otn es TCM fe threshold

    .. data:: thresh_ses_tcm_fe = 16777225

    	PM Otn ses TCM fe threshold

    .. data:: thresh_uas_tcm_fe = 16777226

    	PM Otn uas TCM fe threshold

    .. data:: thresh_bbe_tcm_fe = 16777227

    	PM Otn bbe TCM fe threshold

    .. data:: thresh_fc_tcm_fe = 16777228

    	PM Otn fc TCM fe threshold

    .. data:: thresh_esr_tcm_fe = 16777229

    	PM Otn esr TCM fe threshold

    .. data:: thresh_sesr_tcm_fe = 16777230

    	PM Otn sesr TCM fe threshold

    .. data:: thresh_bber_tcm_fe = 16777231

    	PM Otn bber TCM fe threshold

    .. data:: thresh_es_tcm_ne = 33554432

    	PM Otn es TCM ne threshold

    .. data:: thresh_ses_tcm_ne = 33554433

    	PM Otn ses TCM ne threshold

    .. data:: thresh_uas_tcm_ne = 33554434

    	PM Otn uas TCM ne threshold

    .. data:: thresh_bbe_tcm_ne = 33554435

    	PM Otn bbe TCM ne threshold

    .. data:: thresh_fc_tcm_ne = 33554436

    	PM Otn fc TCM ne threshold

    .. data:: thresh_esr_tcm_ne = 33554437

    	PM Otn esr TCM ne threshold

    .. data:: thresh_sesr_tcm_ne = 33554438

    	PM Otn sesr TCM ne threshold

    .. data:: thresh_bber_tcm_ne = 33554439

    	PM Otn bber TCM ne threshold

    """

    thresh_es_tcm_fe = 16777224

    thresh_ses_tcm_fe = 16777225

    thresh_uas_tcm_fe = 16777226

    thresh_bbe_tcm_fe = 16777227

    thresh_fc_tcm_fe = 16777228

    thresh_esr_tcm_fe = 16777229

    thresh_sesr_tcm_fe = 16777230

    thresh_bber_tcm_fe = 16777231

    thresh_es_tcm_ne = 33554432

    thresh_ses_tcm_ne = 33554433

    thresh_uas_tcm_ne = 33554434

    thresh_bbe_tcm_ne = 33554435

    thresh_fc_tcm_ne = 33554436

    thresh_esr_tcm_ne = 33554437

    thresh_sesr_tcm_ne = 33554438

    thresh_bber_tcm_ne = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmThresholdEnum']


class OtnThresholdEnum(Enum):
    """
    OtnThresholdEnum

    Otn threshold

    .. data:: thresh_es_sm_ne = 262144

    	PM Otn es sm ne threshold

    .. data:: thresh_ses_sm_ne = 262145

    	PM Otn ses sm ne threshold

    .. data:: thresh_uas_sm_ne = 262146

    	PM Otn uas sm ne threshold

    .. data:: thresh_bbe_sm_ne = 262147

    	PM Otn bbe sm ne threshold

    .. data:: thresh_fc_sm_ne = 262148

    	PM Otn fc sm ne threshold

    .. data:: thresh_esr_sm_ne = 262149

    	PM Otn esr sm ne threshold

    .. data:: thresh_sesr_sm_ne = 262150

    	PM Otn sesr sm ne threshold

    .. data:: thresh_bber_sm_ne = 262151

    	PM Otn bber sm ne threshold

    .. data:: thresh_es_pm_ne = 524288

    	PM Otn es pm ne threshold

    .. data:: thresh_ses_pm_ne = 524289

    	PM Otn ses pm ne threshold

    .. data:: thresh_uas_pm_ne = 524290

    	PM Otn uas pm ne threshold

    .. data:: thresh_bbe_pm_ne = 524291

    	PM Otn bbe pm ne threshold

    .. data:: thresh_fc_pm_ne = 524292

    	PM Otn fc pm ne threshold

    .. data:: thresh_esr_pm_ne = 524293

    	PM Otn esr pm ne threshold

    .. data:: thresh_sesr_pm_ne = 524294

    	PM Otn sesr pm ne threshold

    .. data:: thresh_bber_pm_ne = 524295

    	PM Otn bber pm ne threshold

    .. data:: thresh_es_sm_fe = 1048584

    	PM Otn es sm fe threshold

    .. data:: thresh_ses_sm_fe = 1048585

    	PM Otn ses sm fe threshold

    .. data:: thresh_uas_sm_fe = 1048586

    	PM Otn uas sm fe threshold

    .. data:: thresh_bbe_sm_fe = 1048587

    	PM Otn bbe sm fe threshold

    .. data:: thresh_fc_sm_fe = 1048588

    	PM Otn fc sm fe threshold

    .. data:: thresh_esr_sm_fe = 1048589

    	PM Otn esr sm fe threshold

    .. data:: thresh_sesr_sm_fe = 1048590

    	PM Otn sesr sm fe threshold

    .. data:: thresh_bber_sm_fe = 1048591

    	PM Otn bber sm fe threshold

    .. data:: thresh_es_pm_fe = 2097160

    	PM Otn es pm fe threshold

    .. data:: thresh_ses_pm_fe = 2097161

    	PM Otn ses pm fe threshold

    .. data:: thresh_uas_pm_fe = 2097162

    	PM Otn uas pm fe threshold

    .. data:: thresh_bbe_pm_fe = 2097163

    	PM Otn bbe pm fe threshold

    .. data:: thresh_fc_pm_fe = 2097164

    	PM Otn fc pm fe threshold

    .. data:: thresh_esr_pm_fe = 2097165

    	PM Otn esr pm fe threshold

    .. data:: thresh_sesr_pm_fe = 2097166

    	PM Otn sesr pm fe threshold

    .. data:: thresh_bber_pm_fe = 2097167

    	PM Otn bber pm fe threshold

    """

    thresh_es_sm_ne = 262144

    thresh_ses_sm_ne = 262145

    thresh_uas_sm_ne = 262146

    thresh_bbe_sm_ne = 262147

    thresh_fc_sm_ne = 262148

    thresh_esr_sm_ne = 262149

    thresh_sesr_sm_ne = 262150

    thresh_bber_sm_ne = 262151

    thresh_es_pm_ne = 524288

    thresh_ses_pm_ne = 524289

    thresh_uas_pm_ne = 524290

    thresh_bbe_pm_ne = 524291

    thresh_fc_pm_ne = 524292

    thresh_esr_pm_ne = 524293

    thresh_sesr_pm_ne = 524294

    thresh_bber_pm_ne = 524295

    thresh_es_sm_fe = 1048584

    thresh_ses_sm_fe = 1048585

    thresh_uas_sm_fe = 1048586

    thresh_bbe_sm_fe = 1048587

    thresh_fc_sm_fe = 1048588

    thresh_esr_sm_fe = 1048589

    thresh_sesr_sm_fe = 1048590

    thresh_bber_sm_fe = 1048591

    thresh_es_pm_fe = 2097160

    thresh_ses_pm_fe = 2097161

    thresh_uas_pm_fe = 2097162

    thresh_bbe_pm_fe = 2097163

    thresh_fc_pm_fe = 2097164

    thresh_esr_pm_fe = 2097165

    thresh_sesr_pm_fe = 2097166

    thresh_bber_pm_fe = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnThresholdEnum']


class PathReportEnum(Enum):
    """
    PathReportEnum

    Path report

    .. data:: report_cv = 5242880

    	PM CV threshold

    .. data:: report_es = 5242881

    	PM ES threshold

    .. data:: report_ses = 5242882

    	PM SES threshold

    .. data:: report_uas = 5242883

    	PM UAS threshold

    """

    report_cv = 5242880

    report_es = 5242881

    report_ses = 5242882

    report_uas = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathReportEnum']


class PathThresholdEnum(Enum):
    """
    PathThresholdEnum

    Path threshold

    .. data:: thresh_cv = 5242880

    	PM CV threshold

    .. data:: thresh_es = 5242881

    	PM ES threshold

    .. data:: thresh_ses = 5242882

    	PM SES threshold

    .. data:: thresh_uas = 5242883

    	PM UAS threshold

    """

    thresh_cv = 5242880

    thresh_es = 5242881

    thresh_ses = 5242882

    thresh_uas = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathThresholdEnum']


class ReportEnum(Enum):
    """
    ReportEnum

    Report

    .. data:: false = 0

    	Performance Monitoring Disabled

    .. data:: true = 1

    	Performance Monitoring Enabled

    """

    false = 0

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['ReportEnum']


class StmReportEnum(Enum):
    """
    StmReportEnum

    Stm report

    .. data:: report_ebs = 16777217

    	PM EBS REPORT

    .. data:: report_ess = 16777218

    	PM ESS REPORT

    .. data:: report_esrs = 16777219

    	PM ESRS REPORT

    .. data:: report_sess = 16777220

    	PM SES REPORT

    .. data:: report_sesrs = 16777221

    	PM SESR REPORT

    .. data:: report_bbes = 16777222

    	PM BBES REPORT

    .. data:: report_bbesr = 16777223

    	PM BBESR REPORT

    .. data:: report_uass = 16777224

    	PM UASS REPORT

    .. data:: report_ebl_ne = 16777225

    	PM EBLNE REPORT

    .. data:: report_esl_ne = 16777226

    	PM ESLNE REPORT

    .. data:: report_eslr_ne = 16777227

    	PM ESLRNE REPORT

    .. data:: report_sesl_ne = 16777228

    	PM SESL REPORT

    .. data:: report_sesrl_ne = 16777229

    	PM SESRL REPORT

    .. data:: report_bbel_ne = 16777230

    	PM BBELNE REPORT

    .. data:: report_bberl_ne = 16777231

    	PM BBERLNE REPORT

    .. data:: report_uasl_ne = 16777232

    	PM UASNE REPORT

    .. data:: report_ebl_fe = 16777245

    	PM EBFE REPORT

    .. data:: report_esl_fe = 16777246

    	PM ESFE REPORT

    .. data:: report_esrl_fe = 16777247

    	PM EBFE REPORT

    .. data:: report_sesl_fe = 16777248

    	PM SESFE REPORT

    .. data:: report_sesrl_fe = 16777249

    	PM SESRLFE REPORT

    .. data:: report_bbel_fe = 16777250

    	PM BBELFE REPORT

    .. data:: report_bberl_fe = 16777251

    	PM ESFE REPORT

    .. data:: report_uasl_fe = 16777252

    	PM UASLFE REPORT

    """

    report_ebs = 16777217

    report_ess = 16777218

    report_esrs = 16777219

    report_sess = 16777220

    report_sesrs = 16777221

    report_bbes = 16777222

    report_bbesr = 16777223

    report_uass = 16777224

    report_ebl_ne = 16777225

    report_esl_ne = 16777226

    report_eslr_ne = 16777227

    report_sesl_ne = 16777228

    report_sesrl_ne = 16777229

    report_bbel_ne = 16777230

    report_bberl_ne = 16777231

    report_uasl_ne = 16777232

    report_ebl_fe = 16777245

    report_esl_fe = 16777246

    report_esrl_fe = 16777247

    report_sesl_fe = 16777248

    report_sesrl_fe = 16777249

    report_bbel_fe = 16777250

    report_bberl_fe = 16777251

    report_uasl_fe = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmReportEnum']


class StmThresholdEnum(Enum):
    """
    StmThresholdEnum

    Stm threshold

    .. data:: thresh_ebs = 16777217

    	PM EBS threshold

    .. data:: thresh_ess = 16777218

    	PM ESS threshold

    .. data:: thresh_esrs = 16777219

    	PM ESRS threshold

    .. data:: thresh_sess = 16777220

    	PM SES threshold

    .. data:: thresh_sesrs = 16777221

    	PM SESR threshold

    .. data:: thresh_bbes = 16777222

    	PM BBES threshold

    .. data:: thresh_bbesr = 16777223

    	PM BBESR threshold

    .. data:: thresh_uass = 16777224

    	PM UASS threshold

    .. data:: thresh_ebl_ne = 16777225

    	PM EBLNE threshold

    .. data:: thresh_esl_ne = 16777226

    	PM ESLNE threshold

    .. data:: thresh_eslr_ne = 16777227

    	PM ESLRNE threshold

    .. data:: thresh_sesl_ne = 16777228

    	PM SESL threshold

    .. data:: thresh_sesrl_ne = 16777229

    	PM SESRL threshold

    .. data:: thresh_bbel_ne = 16777230

    	PM BBERLNE threshold

    .. data:: thresh_bberl_ne = 16777231

    	PM BBERLNE threshold

    .. data:: thresh_uasl_ne = 16777232

    	PM UASNE threshold

    .. data:: thresh_ebl_fe = 16777245

    	PM EBFE threshold

    .. data:: thresh_esl_fe = 16777246

    	PM ESFE threshold

    .. data:: thresh_esrl_fe = 16777247

    	PM EBFE threshold

    .. data:: thresh_sesl_fe = 16777248

    	PM SESFE threshold

    .. data:: thresh_sesrl_fe = 16777249

    	PM SESRLFE threshold

    .. data:: thresh_bbel_fe = 16777250

    	PM BBEL threshold

    .. data:: thresh_bberl_fe = 16777251

    	PM BBELFE threshold

    .. data:: thresh_uasl_fe = 16777252

    	PM UASLFE threshold

    """

    thresh_ebs = 16777217

    thresh_ess = 16777218

    thresh_esrs = 16777219

    thresh_sess = 16777220

    thresh_sesrs = 16777221

    thresh_bbes = 16777222

    thresh_bbesr = 16777223

    thresh_uass = 16777224

    thresh_ebl_ne = 16777225

    thresh_esl_ne = 16777226

    thresh_eslr_ne = 16777227

    thresh_sesl_ne = 16777228

    thresh_sesrl_ne = 16777229

    thresh_bbel_ne = 16777230

    thresh_bberl_ne = 16777231

    thresh_uasl_ne = 16777232

    thresh_ebl_fe = 16777245

    thresh_esl_fe = 16777246

    thresh_esrl_fe = 16777247

    thresh_sesl_fe = 16777248

    thresh_sesrl_fe = 16777249

    thresh_bbel_fe = 16777250

    thresh_bberl_fe = 16777251

    thresh_uasl_fe = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmThresholdEnum']


class StsReportEnum(Enum):
    """
    StsReportEnum

    Sts report

    .. data:: report_cv = 4194304

    	PM CV threshold

    .. data:: report_es = 4194305

    	PM ES threshold

    .. data:: report_ses = 4194306

    	PM SES threshold

    .. data:: report_uas = 4194307

    	PM UAS threshold

    """

    report_cv = 4194304

    report_es = 4194305

    report_ses = 4194306

    report_uas = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsReportEnum']


class StsThresholdEnum(Enum):
    """
    StsThresholdEnum

    Sts threshold

    .. data:: thresh_cv = 4194304

    	PM CV threshold

    .. data:: thresh_es = 4194305

    	PM ES threshold

    .. data:: thresh_ses = 4194306

    	PM SES threshold

    .. data:: thresh_uas = 4194307

    	PM UAS threshold

    """

    thresh_cv = 4194304

    thresh_es = 4194305

    thresh_ses = 4194306

    thresh_uas = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsThresholdEnum']




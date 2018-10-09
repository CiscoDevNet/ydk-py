""" Cisco_IOS_XR_pmengine_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pmengine package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EtherReport(Enum):
    """
    EtherReport (Enum Class)

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

    report_rx_pkt = Enum.YLeaf(524288, "report-rx-pkt")

    report_rx_util = Enum.YLeaf(524289, "report-rx-util")

    report_tx_util = Enum.YLeaf(524290, "report-tx-util")

    report_stat_pkt = Enum.YLeaf(524291, "report-stat-pkt")

    report_octet_stat = Enum.YLeaf(524292, "report-octet-stat")

    report_over_size_pkt = Enum.YLeaf(524293, "report-over-size-pkt")

    report_fcs_err = Enum.YLeaf(524294, "report-fcs-err")

    report_long_frame_s = Enum.YLeaf(524295, "report-long-frame-s")

    report_jabber_stats = Enum.YLeaf(524296, "report-jabber-stats")

    report_64_octet = Enum.YLeaf(524297, "report-64-octet")

    report_65_127_octet = Enum.YLeaf(524298, "report-65-127-octet")

    report_128_255_octet = Enum.YLeaf(524299, "report-128-255-octet")

    report_256_511_octet = Enum.YLeaf(524300, "report-256-511-octet")

    report_512_1023_octet = Enum.YLeaf(524301, "report-512-1023-octet")

    report_1024_1518_octet = Enum.YLeaf(524302, "report-1024-1518-octet")

    report_in_ucast = Enum.YLeaf(524303, "report-in-ucast")

    report_in_mcast = Enum.YLeaf(524304, "report-in-mcast")

    report_in_bcast = Enum.YLeaf(524305, "report-in-bcast")

    report_out_ucast = Enum.YLeaf(524306, "report-out-ucast")

    report_out_mcast = Enum.YLeaf(524307, "report-out-mcast")

    report_out_bcast = Enum.YLeaf(524308, "report-out-bcast")

    report_tx_pkt = Enum.YLeaf(524309, "report-tx-pkt")

    report_ifin_error_s = Enum.YLeaf(524310, "report-ifin-error-s")

    report_ifin_octets = Enum.YLeaf(524311, "report-ifin-octets")

    report_ether_stat_multicast_pkt = Enum.YLeaf(524312, "report-ether-stat-multicast-pkt")

    report_ether_stat_broadcast_pkt = Enum.YLeaf(524313, "report-ether-stat-broadcast-pkt")

    report_ether_stat_under_size_d_pkt = Enum.YLeaf(524314, "report-ether-stat-under-size-d-pkt")

    report_out_octet = Enum.YLeaf(524315, "report-out-octet")

    report_in_pause_frame = Enum.YLeaf(524316, "report-in-pause-frame")

    report_in_go_od_bytes = Enum.YLeaf(524317, "report-in-go-od-bytes")

    report_in_802_1q_frame_s = Enum.YLeaf(524318, "report-in-802-1q-frame-s")

    report_in_pkts_1519_max_octets = Enum.YLeaf(524319, "report-in-pkts-1519-max-octets")

    report_in_go_od_pkts = Enum.YLeaf(524320, "report-in-go-od-pkts")

    report_in_drop_overrun = Enum.YLeaf(524321, "report-in-drop-overrun")

    report_in_drop_abort = Enum.YLeaf(524322, "report-in-drop-abort")

    report_in_drop_invalid_vlan = Enum.YLeaf(524323, "report-in-drop-invalid-vlan")

    report_in_drop_invalid_dmac = Enum.YLeaf(524324, "report-in-drop-invalid-dmac")

    report_in_drop_invalid_encap = Enum.YLeaf(524325, "report-in-drop-invalid-encap")

    report_in_drop_other = Enum.YLeaf(524326, "report-in-drop-other")

    report_in_mib_giant = Enum.YLeaf(524327, "report-in-mib-giant")

    report_in_mib_jabber = Enum.YLeaf(524328, "report-in-mib-jabber")

    report_in_mib_crc = Enum.YLeaf(524329, "report-in-mib-crc")

    report_in_error_collision_s = Enum.YLeaf(524330, "report-in-error-collision-s")

    report_in_error_symbol = Enum.YLeaf(524331, "report-in-error-symbol")

    report_out_go_od_bytes = Enum.YLeaf(524332, "report-out-go-od-bytes")

    report_out_802_1q_frame_s = Enum.YLeaf(524333, "report-out-802-1q-frame-s")

    report_out_pause_frame_s = Enum.YLeaf(524334, "report-out-pause-frame-s")

    report_out_pkts_1519_max_octets = Enum.YLeaf(524335, "report-out-pkts-1519-max-octets")

    report_out_go_od_pkts = Enum.YLeaf(524336, "report-out-go-od-pkts")

    report_out_drop_under_run = Enum.YLeaf(524337, "report-out-drop-under-run")

    report_out_drop_abort = Enum.YLeaf(524338, "report-out-drop-abort")

    report_out_drop_other = Enum.YLeaf(524339, "report-out-drop-other")

    report_out_error_other = Enum.YLeaf(524340, "report-out-error-other")

    report_in_error_giant = Enum.YLeaf(524341, "report-in-error-giant")

    report_in_error_runt = Enum.YLeaf(524342, "report-in-error-runt")

    report_in_error_jabbers = Enum.YLeaf(524343, "report-in-error-jabbers")

    report_in_error_fragments = Enum.YLeaf(524344, "report-in-error-fragments")

    report_in_error_other = Enum.YLeaf(524345, "report-in-error-other")

    report_in_pkt_64_octet = Enum.YLeaf(524346, "report-in-pkt-64-octet")

    report_in_pkts_65_127octets = Enum.YLeaf(524347, "report-in-pkts-65-127octets")

    report_in_pkts_128_255_octets = Enum.YLeaf(524348, "report-in-pkts-128-255-octets")

    report_in_pkts_256_511_octets = Enum.YLeaf(524349, "report-in-pkts-256-511-octets")

    report_in_pkts_512_1023_octets = Enum.YLeaf(524350, "report-in-pkts-512-1023-octets")

    report_in_pkts_1024_1518_octets = Enum.YLeaf(524351, "report-in-pkts-1024-1518-octets")

    report_out_pkt_64_octet = Enum.YLeaf(524352, "report-out-pkt-64-octet")

    report_out_pkts_65_127octets = Enum.YLeaf(524353, "report-out-pkts-65-127octets")

    report_out_pkts_128_255_octets = Enum.YLeaf(524354, "report-out-pkts-128-255-octets")

    report_out_pkts_256_511_octets = Enum.YLeaf(524355, "report-out-pkts-256-511-octets")

    report_out_pkts_512_1023_octets = Enum.YLeaf(524356, "report-out-pkts-512-1023-octets")

    report_out_pkts_1024_1518_octets = Enum.YLeaf(524357, "report-out-pkts-1024-1518-octets")

    report_tx_under_size_d_pkt = Enum.YLeaf(524358, "report-tx-under-size-d-pkt")

    report_tx_over_size_d_pkt = Enum.YLeaf(524359, "report-tx-over-size-d-pkt")

    report_tx_fragments = Enum.YLeaf(524360, "report-tx-fragments")

    report_tx_jabber = Enum.YLeaf(524361, "report-tx-jabber")

    report_tx_bad_fcs = Enum.YLeaf(524362, "report-tx-bad-fcs")


class EtherThreshold(Enum):
    """
    EtherThreshold (Enum Class)

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

    thresh_rx_pkt = Enum.YLeaf(8388608, "thresh-rx-pkt")

    thresh_rx_util = Enum.YLeaf(8388609, "thresh-rx-util")

    thresh_tx_util = Enum.YLeaf(8388610, "thresh-tx-util")

    thresh_stat_pkt = Enum.YLeaf(8388611, "thresh-stat-pkt")

    thresh_octet_stat = Enum.YLeaf(8388612, "thresh-octet-stat")

    thresh_over_size_pkt = Enum.YLeaf(8388613, "thresh-over-size-pkt")

    thresh_fcs_err = Enum.YLeaf(8388614, "thresh-fcs-err")

    thresh_long_frame_s = Enum.YLeaf(8388615, "thresh-long-frame-s")

    thresh_jabber_stats = Enum.YLeaf(8388616, "thresh-jabber-stats")

    thresh_64_octet = Enum.YLeaf(8388617, "thresh-64-octet")

    thresh_65_127_octet = Enum.YLeaf(8388618, "thresh-65-127-octet")

    thresh_128_255_octet = Enum.YLeaf(8388619, "thresh-128-255-octet")

    thresh_256_511_octet = Enum.YLeaf(8388620, "thresh-256-511-octet")

    thresh_512_1023_octet = Enum.YLeaf(8388621, "thresh-512-1023-octet")

    thresh_1024_1518_octet = Enum.YLeaf(8388622, "thresh-1024-1518-octet")

    thresh_in_ucast = Enum.YLeaf(8388623, "thresh-in-ucast")

    thresh_in_mcast = Enum.YLeaf(8388624, "thresh-in-mcast")

    thresh_in_bcast = Enum.YLeaf(8388625, "thresh-in-bcast")

    thresh_out_ucast = Enum.YLeaf(8388626, "thresh-out-ucast")

    thresh_out_mcast = Enum.YLeaf(8388627, "thresh-out-mcast")

    thresh_out_bcast = Enum.YLeaf(8388628, "thresh-out-bcast")

    thresh_tx_pkt = Enum.YLeaf(8388629, "thresh-tx-pkt")

    thresh_ifin_error_s = Enum.YLeaf(8388630, "thresh-ifin-error-s")

    thresh_ifin_octets = Enum.YLeaf(8388631, "thresh-ifin-octets")

    thresh_ether_stat_multicast_pkt = Enum.YLeaf(8388632, "thresh-ether-stat-multicast-pkt")

    thresh_ether_stat_broadcast_pkt = Enum.YLeaf(8388633, "thresh-ether-stat-broadcast-pkt")

    thresh_ether_stat_under_size_d_pkt = Enum.YLeaf(8388634, "thresh-ether-stat-under-size-d-pkt")

    thresh_out_octet = Enum.YLeaf(8388635, "thresh-out-octet")

    thresh_in_pause_frame = Enum.YLeaf(8388636, "thresh-in-pause-frame")

    thresh_in_go_od_bytes = Enum.YLeaf(8388637, "thresh-in-go-od-bytes")

    thresh_in_802_1q_frame_s = Enum.YLeaf(8388638, "thresh-in-802-1q-frame-s")

    thresh_in_pkts_1519_max_octets = Enum.YLeaf(8388639, "thresh-in-pkts-1519-max-octets")

    thresh_in_go_od_pkts = Enum.YLeaf(8388640, "thresh-in-go-od-pkts")

    thresh_in_drop_overrun = Enum.YLeaf(8388641, "thresh-in-drop-overrun")

    thresh_in_drop_abort = Enum.YLeaf(8388642, "thresh-in-drop-abort")

    thresh_in_drop_invalid_vlan = Enum.YLeaf(8388643, "thresh-in-drop-invalid-vlan")

    thresh_in_drop_invalid_dmac = Enum.YLeaf(8388644, "thresh-in-drop-invalid-dmac")

    thresh_in_drop_invalid_encap = Enum.YLeaf(8388645, "thresh-in-drop-invalid-encap")

    thresh_in_drop_other = Enum.YLeaf(8388646, "thresh-in-drop-other")

    thresh_in_mib_giant = Enum.YLeaf(8388647, "thresh-in-mib-giant")

    thresh_in_mib_jabber = Enum.YLeaf(8388648, "thresh-in-mib-jabber")

    thresh_in_mib_crc = Enum.YLeaf(8388649, "thresh-in-mib-crc")

    thresh_in_error_collision_s = Enum.YLeaf(8388650, "thresh-in-error-collision-s")

    thresh_in_error_symbol = Enum.YLeaf(8388651, "thresh-in-error-symbol")

    thresh_out_go_od_bytes = Enum.YLeaf(8388652, "thresh-out-go-od-bytes")

    thresh_out_802_1q_frame_s = Enum.YLeaf(8388653, "thresh-out-802-1q-frame-s")

    thresh_out_pause_frame_s = Enum.YLeaf(8388654, "thresh-out-pause-frame-s")

    thresh_out_pkts_1519_max_octets = Enum.YLeaf(8388655, "thresh-out-pkts-1519-max-octets")

    thresh_out_go_od_pkts = Enum.YLeaf(8388656, "thresh-out-go-od-pkts")

    thresh_out_drop_under_run = Enum.YLeaf(8388657, "thresh-out-drop-under-run")

    thresh_out_drop_abort = Enum.YLeaf(8388658, "thresh-out-drop-abort")

    thresh_out_drop_other = Enum.YLeaf(8388659, "thresh-out-drop-other")

    thresh_out_error_other = Enum.YLeaf(8388660, "thresh-out-error-other")

    thresh_in_error_giant = Enum.YLeaf(8388661, "thresh-in-error-giant")

    thresh_in_error_runt = Enum.YLeaf(8388662, "thresh-in-error-runt")

    thresh_in_error_jabbers = Enum.YLeaf(8388663, "thresh-in-error-jabbers")

    thresh_in_error_fragments = Enum.YLeaf(8388664, "thresh-in-error-fragments")

    thresh_in_error_other = Enum.YLeaf(8388665, "thresh-in-error-other")

    thresh_in_pkt_64_octet = Enum.YLeaf(8388666, "thresh-in-pkt-64-octet")

    thresh_in_pkts_65_127octets = Enum.YLeaf(8388667, "thresh-in-pkts-65-127octets")

    thresh_in_pkts_128_255_octets = Enum.YLeaf(8388668, "thresh-in-pkts-128-255-octets")

    thresh_in_pkts_256_511_octets = Enum.YLeaf(8388669, "thresh-in-pkts-256-511-octets")

    thresh_in_pkts_512_1023_octets = Enum.YLeaf(8388670, "thresh-in-pkts-512-1023-octets")

    thresh_in_pkts_1024_1518_octets = Enum.YLeaf(8388671, "thresh-in-pkts-1024-1518-octets")

    thresh_out_pkt_64_octet = Enum.YLeaf(8388672, "thresh-out-pkt-64-octet")

    thresh_out_pkts_65_127octets = Enum.YLeaf(8388673, "thresh-out-pkts-65-127octets")

    thresh_out_pkts_128_255_octets = Enum.YLeaf(8388674, "thresh-out-pkts-128-255-octets")

    thresh_out_pkts_256_511_octets = Enum.YLeaf(8388675, "thresh-out-pkts-256-511-octets")

    thresh_out_pkts_512_1023_octets = Enum.YLeaf(8388676, "thresh-out-pkts-512-1023-octets")

    thresh_out_pkts_1024_1518_octets = Enum.YLeaf(8388677, "thresh-out-pkts-1024-1518-octets")

    thresh_tx_under_size_d_pkt = Enum.YLeaf(8388678, "thresh-tx-under-size-d-pkt")

    thresh_tx_over_size_d_pkt = Enum.YLeaf(8388679, "thresh-tx-over-size-d-pkt")

    thresh_tx_fragments = Enum.YLeaf(8388680, "thresh-tx-fragments")

    thresh_tx_jabber = Enum.YLeaf(8388681, "thresh-tx-jabber")

    thresh_tx_bad_fcs = Enum.YLeaf(8388682, "thresh-tx-bad-fcs")


class FecReport(Enum):
    """
    FecReport (Enum Class)

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

    report_ec_bits = Enum.YLeaf(131072, "report-ec-bits")

    report_uc_words = Enum.YLeaf(131076, "report-uc-words")

    report_pre_fec_ber_max = Enum.YLeaf(131081, "report-pre-fec-ber-max")

    report_post_fec_ber_max = Enum.YLeaf(131082, "report-post-fec-ber-max")

    report_q_max = Enum.YLeaf(131083, "report-q-max")

    report_q_margin_max = Enum.YLeaf(131084, "report-q-margin-max")

    report_pre_fec_ber_min = Enum.YLeaf(131085, "report-pre-fec-ber-min")

    report_post_fec_ber_min = Enum.YLeaf(131086, "report-post-fec-ber-min")

    report_q_min = Enum.YLeaf(131087, "report-q-min")

    report_q_margin_min = Enum.YLeaf(131088, "report-q-margin-min")


class FecThreshold(Enum):
    """
    FecThreshold (Enum Class)

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

    thresh_ec_bits = Enum.YLeaf(131072, "thresh-ec-bits")

    thresh_uc_words = Enum.YLeaf(131076, "thresh-uc-words")

    thresh_pre_fec_ber_max = Enum.YLeaf(131081, "thresh-pre-fec-ber-max")

    thresh_post_fec_ber_max = Enum.YLeaf(131082, "thresh-post-fec-ber-max")

    thresh_q_max = Enum.YLeaf(131083, "thresh-q-max")

    thresh_q_margin_max = Enum.YLeaf(131084, "thresh-q-margin-max")

    thresh_pre_fec_ber_min = Enum.YLeaf(131085, "thresh-pre-fec-ber-min")

    thresh_post_fec_ber_min = Enum.YLeaf(131086, "thresh-post-fec-ber-min")

    thresh_q_min = Enum.YLeaf(131087, "thresh-q-min")

    thresh_q_margin_min = Enum.YLeaf(131088, "thresh-q-margin-min")


class GfpReport(Enum):
    """
    GfpReport (Enum Class)

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

    report_rx_bit_err = Enum.YLeaf(6291456, "report-rx-bit-err")

    report_rx_inv_typ = Enum.YLeaf(6291457, "report-rx-inv-typ")

    report_rx_crc = Enum.YLeaf(6291458, "report-rx-crc")

    report_rx_lfd = Enum.YLeaf(6291459, "report-rx-lfd")

    report_rx_csf = Enum.YLeaf(6291460, "report-rx-csf")


class GfpThreshold(Enum):
    """
    GfpThreshold (Enum Class)

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

    thresh_rx_bit_err = Enum.YLeaf(67108864, "thresh-rx-bit-err")

    thresh_rx_inv_typ = Enum.YLeaf(67108865, "thresh-rx-inv-typ")

    thresh_rx_crc = Enum.YLeaf(67108866, "thresh-rx-crc")

    thresh_rx_lfd = Enum.YLeaf(67108867, "thresh-rx-lfd")

    thresh_rx_csf = Enum.YLeaf(67108868, "thresh-rx-csf")


class HoVcReport(Enum):
    """
    HoVcReport (Enum Class)

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

    report_eb = Enum.YLeaf(33554432, "report-eb")

    report_es = Enum.YLeaf(33554433, "report-es")

    report_esr = Enum.YLeaf(33554434, "report-esr")

    report_ses = Enum.YLeaf(33554435, "report-ses")

    report_sesr = Enum.YLeaf(33554436, "report-sesr")

    report_bbe = Enum.YLeaf(33554437, "report-bbe")

    report_bber = Enum.YLeaf(33554438, "report-bber")

    report_uass = Enum.YLeaf(33554439, "report-uass")


class HoVcThreshold(Enum):
    """
    HoVcThreshold (Enum Class)

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

    thresh_eb = Enum.YLeaf(33554432, "thresh-eb")

    thresh_es = Enum.YLeaf(33554433, "thresh-es")

    thresh_esr = Enum.YLeaf(33554434, "thresh-esr")

    thresh_ses = Enum.YLeaf(33554435, "thresh-ses")

    thresh_sesr = Enum.YLeaf(33554436, "thresh-sesr")

    thresh_bbe = Enum.YLeaf(33554437, "thresh-bbe")

    thresh_bber = Enum.YLeaf(33554438, "thresh-bber")

    thresh_uass = Enum.YLeaf(33554439, "thresh-uass")


class OcnReport(Enum):
    """
    OcnReport (Enum Class)

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

    report_sefss = Enum.YLeaf(3145728, "report-sefss")

    report_cvs = Enum.YLeaf(3145729, "report-cvs")

    report_ess = Enum.YLeaf(3145730, "report-ess")

    report_sess = Enum.YLeaf(3145731, "report-sess")

    report_cvl_ne = Enum.YLeaf(3145734, "report-cvl-ne")

    report_esl_ne = Enum.YLeaf(3145735, "report-esl-ne")

    report_sesl_ne = Enum.YLeaf(3145736, "report-sesl-ne")

    report_uasl_ne = Enum.YLeaf(3145738, "report-uasl-ne")

    report_fcl_ne = Enum.YLeaf(3145739, "report-fcl-ne")

    report_fcl_fe = Enum.YLeaf(3145751, "report-fcl-fe")

    report_cvl_fe = Enum.YLeaf(3145752, "report-cvl-fe")

    report_esl_fe = Enum.YLeaf(3145753, "report-esl-fe")

    report_sesl_fe = Enum.YLeaf(3145754, "report-sesl-fe")

    report_uasl_fe = Enum.YLeaf(3145756, "report-uasl-fe")


class OcnThreshold(Enum):
    """
    OcnThreshold (Enum Class)

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

    thresh_sefss = Enum.YLeaf(3145728, "thresh-sefss")

    thresh_cvs = Enum.YLeaf(3145729, "thresh-cvs")

    thresh_ess = Enum.YLeaf(3145730, "thresh-ess")

    thresh_sess = Enum.YLeaf(3145731, "thresh-sess")

    thresh_cvl_ne = Enum.YLeaf(3145734, "thresh-cvl-ne")

    thresh_esl_ne = Enum.YLeaf(3145735, "thresh-esl-ne")

    thresh_sesl_ne = Enum.YLeaf(3145736, "thresh-sesl-ne")

    thresh_uasl_ne = Enum.YLeaf(3145738, "thresh-uasl-ne")

    thresh_fcl_ne = Enum.YLeaf(3145739, "thresh-fcl-ne")

    thresh_fcl_fe = Enum.YLeaf(3145751, "thresh-fcl-fe")

    thresh_cvl_fe = Enum.YLeaf(3145752, "thresh-cvl-fe")

    thresh_esl_fe = Enum.YLeaf(3145753, "thresh-esl-fe")

    thresh_sesl_fe = Enum.YLeaf(3145754, "thresh-sesl-fe")

    thresh_uasl_fe = Enum.YLeaf(3145756, "thresh-uasl-fe")


class OpticsReport(Enum):
    """
    OpticsReport (Enum Class)

    Optics report

    .. data:: report_opt_min = 65554

    	PM Optics opt min report

    .. data:: report_opr_min = 65555

    	PM Optics opr min report

    .. data:: report_lbc_min = 65556

    	PM Optics lbc min report

    .. data:: report_lbc_pc_min = 65557

    	PM Optics lbcpc min report

    .. data:: report_cd_min = 65561

    	PM Optics cd min report

    .. data:: report_dgd_min = 65562

    	PM Optics dgd min report

    .. data:: report_pmd_min = 65563

    	PM Optics sopmd min report

    .. data:: report_osnr_min = 65564

    	PM Optics osnr min report

    .. data:: report_pdl_min = 65565

    	PM Optics pdl min report

    .. data:: report_pcr_min = 65566

    	PM Optics pcr min report

    .. data:: report_pn_min = 65567

    	PM Optics pn min report

    .. data:: report_rx_sig_pow_min = 65568

    	PM Optics rx sig pow min report

    .. data:: report_low_sig_freq_off_min = 65569

    	PM Optics low sig freq off min report

    .. data:: report_ampli_gain_min = 65570

    	PM Optics ampli gain min report

    .. data:: report_ampli_gain_tilt_min = 65571

    	PM Optics ampli gain tilt min report

    .. data:: report_opt_max = 65572

    	PM Optics opt max report

    .. data:: report_opr_max = 65573

    	PM Optics opr max report

    .. data:: report_lbc_max = 65574

    	PM Optics lbc max report

    .. data:: report_lbc_pc_max = 65575

    	PM Optics lbcpc max report

    .. data:: report_cd_max = 65579

    	PM Optics cd max report

    .. data:: report_dgd_max = 65580

    	PM Optics dgd max report

    .. data:: report_pmd_max = 65581

    	PM Optics sopmd max report

    .. data:: report_osnr_max = 65582

    	PM Optics osnr max report

    .. data:: report_pdl_max = 65583

    	PM Optics pdl max report

    .. data:: report_pcr_max = 65584

    	PM Optics pcr max report

    .. data:: report_pn_max = 65585

    	PM Optics pn max report

    .. data:: report_rx_sig_pow_max = 65586

    	PM Optics rx sig pow max report

    .. data:: report_low_sig_freq_off_max = 65587

    	PM Optics low sig freq off max report

    .. data:: report_ampli_gain_max = 65588

    	PM Optics ampli gain max report

    .. data:: report_ampli_gain_tilt_max = 65589

    	PM Optics ampli gain tilt max report

    """

    report_opt_min = Enum.YLeaf(65554, "report-opt-min")

    report_opr_min = Enum.YLeaf(65555, "report-opr-min")

    report_lbc_min = Enum.YLeaf(65556, "report-lbc-min")

    report_lbc_pc_min = Enum.YLeaf(65557, "report-lbc-pc-min")

    report_cd_min = Enum.YLeaf(65561, "report-cd-min")

    report_dgd_min = Enum.YLeaf(65562, "report-dgd-min")

    report_pmd_min = Enum.YLeaf(65563, "report-pmd-min")

    report_osnr_min = Enum.YLeaf(65564, "report-osnr-min")

    report_pdl_min = Enum.YLeaf(65565, "report-pdl-min")

    report_pcr_min = Enum.YLeaf(65566, "report-pcr-min")

    report_pn_min = Enum.YLeaf(65567, "report-pn-min")

    report_rx_sig_pow_min = Enum.YLeaf(65568, "report-rx-sig-pow-min")

    report_low_sig_freq_off_min = Enum.YLeaf(65569, "report-low-sig-freq-off-min")

    report_ampli_gain_min = Enum.YLeaf(65570, "report-ampli-gain-min")

    report_ampli_gain_tilt_min = Enum.YLeaf(65571, "report-ampli-gain-tilt-min")

    report_opt_max = Enum.YLeaf(65572, "report-opt-max")

    report_opr_max = Enum.YLeaf(65573, "report-opr-max")

    report_lbc_max = Enum.YLeaf(65574, "report-lbc-max")

    report_lbc_pc_max = Enum.YLeaf(65575, "report-lbc-pc-max")

    report_cd_max = Enum.YLeaf(65579, "report-cd-max")

    report_dgd_max = Enum.YLeaf(65580, "report-dgd-max")

    report_pmd_max = Enum.YLeaf(65581, "report-pmd-max")

    report_osnr_max = Enum.YLeaf(65582, "report-osnr-max")

    report_pdl_max = Enum.YLeaf(65583, "report-pdl-max")

    report_pcr_max = Enum.YLeaf(65584, "report-pcr-max")

    report_pn_max = Enum.YLeaf(65585, "report-pn-max")

    report_rx_sig_pow_max = Enum.YLeaf(65586, "report-rx-sig-pow-max")

    report_low_sig_freq_off_max = Enum.YLeaf(65587, "report-low-sig-freq-off-max")

    report_ampli_gain_max = Enum.YLeaf(65588, "report-ampli-gain-max")

    report_ampli_gain_tilt_max = Enum.YLeaf(65589, "report-ampli-gain-tilt-max")


class OpticsThreshold(Enum):
    """
    OpticsThreshold (Enum Class)

    Optics threshold

    .. data:: thresh_opt_min = 65554

    	PM Optics opt min threshold in dbm or uW

    .. data:: thresh_opr_min = 65555

    	PM Optics opr min threshold in dbm or uW

    .. data:: thresh_lbc_min = 65556

    	PM Optics lbc min threshold

    .. data:: thresh_lbc_pc_min = 65557

    	PM Optics lbcpc min threshold

    .. data:: thresh_cd_min = 65561

    	PM Optics cd min threshold

    .. data:: thresh_dgd_min = 65562

    	PM Optics dgd min threshold

    .. data:: thresh_pmd_min = 65563

    	PM Optics sopmd min threshold

    .. data:: thresh_osnr_min = 65564

    	PM Optics osnr min threshold

    .. data:: thresh_pdl_min = 65565

    	PM Optics pdl min threshold

    .. data:: thresh_pcr_min = 65566

    	PM Optics pcr min threshold

    .. data:: thresh_pn_min = 65567

    	PM Optics pn min threshold

    .. data:: thresh_rx_sig_pow_min = 65568

    	PM Optics rx sig pow min threshold

    .. data:: thresh_low_sig_freq_off_min = 65569

    	PM Optics low sig freq off min threshold

    .. data:: thresh_ampli_gain_min = 65570

    	PM Optics ampli gain min threshold

    .. data:: thresh_ampli_gain_tilt_min = 65571

    	PM Optics ampli gain tilt min threshold

    .. data:: thresh_opt_max = 65572

    	PM Optics opt max threshold in dbm or uW

    .. data:: thresh_opr_max = 65573

    	PM Optics opr max threshold in dbm or uW

    .. data:: thresh_lbc_max = 65574

    	PM Optics lbc max threshold

    .. data:: thresh_lbc_pc_max = 65575

    	PM Optics lbcpc max threshold

    .. data:: thresh_cd_max = 65579

    	PM Optics cd max threshold

    .. data:: thresh_dgd_max = 65580

    	PM Optics dgd max threshold

    .. data:: thresh_pmd_max = 65581

    	PM Optics sopmd max threshold

    .. data:: thresh_osnr_max = 65582

    	PM Optics osnr max threshold

    .. data:: thresh_pdl_max = 65583

    	PM Optics pdl max threshold

    .. data:: thresh_pcr_max = 65584

    	PM Optics pcr max threshold

    .. data:: thresh_pn_max = 65585

    	PM Optics pn max threshold

    .. data:: thresh_rx_sig_pow_max = 65586

    	PM Optics rx sig pow max threshold

    .. data:: thresh_low_sig_freq_off_max = 65587

    	PM Optics low sig freq off max threshold

    .. data:: thresh_ampli_gain_max = 65588

    	PM Optics ampli gain max threshold

    .. data:: thresh_ampli_gain_tilt_max = 65589

    	PM Optics ampli gain tilt max threshold

    """

    thresh_opt_min = Enum.YLeaf(65554, "thresh-opt-min")

    thresh_opr_min = Enum.YLeaf(65555, "thresh-opr-min")

    thresh_lbc_min = Enum.YLeaf(65556, "thresh-lbc-min")

    thresh_lbc_pc_min = Enum.YLeaf(65557, "thresh-lbc-pc-min")

    thresh_cd_min = Enum.YLeaf(65561, "thresh-cd-min")

    thresh_dgd_min = Enum.YLeaf(65562, "thresh-dgd-min")

    thresh_pmd_min = Enum.YLeaf(65563, "thresh-pmd-min")

    thresh_osnr_min = Enum.YLeaf(65564, "thresh-osnr-min")

    thresh_pdl_min = Enum.YLeaf(65565, "thresh-pdl-min")

    thresh_pcr_min = Enum.YLeaf(65566, "thresh-pcr-min")

    thresh_pn_min = Enum.YLeaf(65567, "thresh-pn-min")

    thresh_rx_sig_pow_min = Enum.YLeaf(65568, "thresh-rx-sig-pow-min")

    thresh_low_sig_freq_off_min = Enum.YLeaf(65569, "thresh-low-sig-freq-off-min")

    thresh_ampli_gain_min = Enum.YLeaf(65570, "thresh-ampli-gain-min")

    thresh_ampli_gain_tilt_min = Enum.YLeaf(65571, "thresh-ampli-gain-tilt-min")

    thresh_opt_max = Enum.YLeaf(65572, "thresh-opt-max")

    thresh_opr_max = Enum.YLeaf(65573, "thresh-opr-max")

    thresh_lbc_max = Enum.YLeaf(65574, "thresh-lbc-max")

    thresh_lbc_pc_max = Enum.YLeaf(65575, "thresh-lbc-pc-max")

    thresh_cd_max = Enum.YLeaf(65579, "thresh-cd-max")

    thresh_dgd_max = Enum.YLeaf(65580, "thresh-dgd-max")

    thresh_pmd_max = Enum.YLeaf(65581, "thresh-pmd-max")

    thresh_osnr_max = Enum.YLeaf(65582, "thresh-osnr-max")

    thresh_pdl_max = Enum.YLeaf(65583, "thresh-pdl-max")

    thresh_pcr_max = Enum.YLeaf(65584, "thresh-pcr-max")

    thresh_pn_max = Enum.YLeaf(65585, "thresh-pn-max")

    thresh_rx_sig_pow_max = Enum.YLeaf(65586, "thresh-rx-sig-pow-max")

    thresh_low_sig_freq_off_max = Enum.YLeaf(65587, "thresh-low-sig-freq-off-max")

    thresh_ampli_gain_max = Enum.YLeaf(65588, "thresh-ampli-gain-max")

    thresh_ampli_gain_tilt_max = Enum.YLeaf(65589, "thresh-ampli-gain-tilt-max")


class OtnReport(Enum):
    """
    OtnReport (Enum Class)

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

    report_es_sm_ne = Enum.YLeaf(262144, "report-es-sm-ne")

    report_ses_sm_ne = Enum.YLeaf(262145, "report-ses-sm-ne")

    report_uas_sm_ne = Enum.YLeaf(262146, "report-uas-sm-ne")

    report_bbe_sm_ne = Enum.YLeaf(262147, "report-bbe-sm-ne")

    report_fc_sm_ne = Enum.YLeaf(262148, "report-fc-sm-ne")

    report_esr_sm_ne = Enum.YLeaf(262149, "report-esr-sm-ne")

    report_sesr_sm_ne = Enum.YLeaf(262150, "report-sesr-sm-ne")

    report_bber_sm_ne = Enum.YLeaf(262151, "report-bber-sm-ne")

    report_es_pm_ne = Enum.YLeaf(524288, "report-es-pm-ne")

    report_ses_pm_ne = Enum.YLeaf(524289, "report-ses-pm-ne")

    report_uas_pm_ne = Enum.YLeaf(524290, "report-uas-pm-ne")

    report_bbe_pm_ne = Enum.YLeaf(524291, "report-bbe-pm-ne")

    report_fc_pm_ne = Enum.YLeaf(524292, "report-fc-pm-ne")

    report_esr_pm_ne = Enum.YLeaf(524293, "report-esr-pm-ne")

    report_sesr_pm_ne = Enum.YLeaf(524294, "report-sesr-pm-ne")

    report_bber_pm_ne = Enum.YLeaf(524295, "report-bber-pm-ne")

    report_es_sm_fe = Enum.YLeaf(1048584, "report-es-sm-fe")

    report_ses_sm_fe = Enum.YLeaf(1048585, "report-ses-sm-fe")

    report_uas_sm_fe = Enum.YLeaf(1048586, "report-uas-sm-fe")

    report_bbe_sm_fe = Enum.YLeaf(1048587, "report-bbe-sm-fe")

    report_fc_sm_fe = Enum.YLeaf(1048588, "report-fc-sm-fe")

    report_esr_sm_fe = Enum.YLeaf(1048589, "report-esr-sm-fe")

    report_sesr_sm_fe = Enum.YLeaf(1048590, "report-sesr-sm-fe")

    report_bber_sm_fe = Enum.YLeaf(1048591, "report-bber-sm-fe")

    report_es_pm_fe = Enum.YLeaf(2097160, "report-es-pm-fe")

    report_ses_pm_fe = Enum.YLeaf(2097161, "report-ses-pm-fe")

    report_uas_pm_fe = Enum.YLeaf(2097162, "report-uas-pm-fe")

    report_bbe_pm_fe = Enum.YLeaf(2097163, "report-bbe-pm-fe")

    report_fc_pm_fe = Enum.YLeaf(2097164, "report-fc-pm-fe")

    report_esr_pm_fe = Enum.YLeaf(2097165, "report-esr-pm-fe")

    report_sesr_pm_fe = Enum.YLeaf(2097166, "report-sesr-pm-fe")

    report_bber_pm_fe = Enum.YLeaf(2097167, "report-bber-pm-fe")


class OtnTcmReport(Enum):
    """
    OtnTcmReport (Enum Class)

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

    report_es_tcm_fe = Enum.YLeaf(16777224, "report-es-tcm-fe")

    report_ses_tcm_fe = Enum.YLeaf(16777225, "report-ses-tcm-fe")

    report_uas_tcm_fe = Enum.YLeaf(16777226, "report-uas-tcm-fe")

    report_bbe_tcm_fe = Enum.YLeaf(16777227, "report-bbe-tcm-fe")

    report_fc_tcm_fe = Enum.YLeaf(16777228, "report-fc-tcm-fe")

    report_esr_tcm_fe = Enum.YLeaf(16777229, "report-esr-tcm-fe")

    report_sesr_tcm_fe = Enum.YLeaf(16777230, "report-sesr-tcm-fe")

    report_bber_tcm_fe = Enum.YLeaf(16777231, "report-bber-tcm-fe")

    report_es_tcm_ne = Enum.YLeaf(33554432, "report-es-tcm-ne")

    report_ses_tcm_ne = Enum.YLeaf(33554433, "report-ses-tcm-ne")

    report_uas_tcm_ne = Enum.YLeaf(33554434, "report-uas-tcm-ne")

    report_bbe_tcm_ne = Enum.YLeaf(33554435, "report-bbe-tcm-ne")

    report_fc_tcm_ne = Enum.YLeaf(33554436, "report-fc-tcm-ne")

    report_esr_tcm_ne = Enum.YLeaf(33554437, "report-esr-tcm-ne")

    report_sesr_tcm_ne = Enum.YLeaf(33554438, "report-sesr-tcm-ne")

    report_bber_tcm_ne = Enum.YLeaf(33554439, "report-bber-tcm-ne")


class OtnTcmThreshold(Enum):
    """
    OtnTcmThreshold (Enum Class)

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

    thresh_es_tcm_fe = Enum.YLeaf(16777224, "thresh-es-tcm-fe")

    thresh_ses_tcm_fe = Enum.YLeaf(16777225, "thresh-ses-tcm-fe")

    thresh_uas_tcm_fe = Enum.YLeaf(16777226, "thresh-uas-tcm-fe")

    thresh_bbe_tcm_fe = Enum.YLeaf(16777227, "thresh-bbe-tcm-fe")

    thresh_fc_tcm_fe = Enum.YLeaf(16777228, "thresh-fc-tcm-fe")

    thresh_esr_tcm_fe = Enum.YLeaf(16777229, "thresh-esr-tcm-fe")

    thresh_sesr_tcm_fe = Enum.YLeaf(16777230, "thresh-sesr-tcm-fe")

    thresh_bber_tcm_fe = Enum.YLeaf(16777231, "thresh-bber-tcm-fe")

    thresh_es_tcm_ne = Enum.YLeaf(33554432, "thresh-es-tcm-ne")

    thresh_ses_tcm_ne = Enum.YLeaf(33554433, "thresh-ses-tcm-ne")

    thresh_uas_tcm_ne = Enum.YLeaf(33554434, "thresh-uas-tcm-ne")

    thresh_bbe_tcm_ne = Enum.YLeaf(33554435, "thresh-bbe-tcm-ne")

    thresh_fc_tcm_ne = Enum.YLeaf(33554436, "thresh-fc-tcm-ne")

    thresh_esr_tcm_ne = Enum.YLeaf(33554437, "thresh-esr-tcm-ne")

    thresh_sesr_tcm_ne = Enum.YLeaf(33554438, "thresh-sesr-tcm-ne")

    thresh_bber_tcm_ne = Enum.YLeaf(33554439, "thresh-bber-tcm-ne")


class OtnThreshold(Enum):
    """
    OtnThreshold (Enum Class)

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

    thresh_es_sm_ne = Enum.YLeaf(262144, "thresh-es-sm-ne")

    thresh_ses_sm_ne = Enum.YLeaf(262145, "thresh-ses-sm-ne")

    thresh_uas_sm_ne = Enum.YLeaf(262146, "thresh-uas-sm-ne")

    thresh_bbe_sm_ne = Enum.YLeaf(262147, "thresh-bbe-sm-ne")

    thresh_fc_sm_ne = Enum.YLeaf(262148, "thresh-fc-sm-ne")

    thresh_esr_sm_ne = Enum.YLeaf(262149, "thresh-esr-sm-ne")

    thresh_sesr_sm_ne = Enum.YLeaf(262150, "thresh-sesr-sm-ne")

    thresh_bber_sm_ne = Enum.YLeaf(262151, "thresh-bber-sm-ne")

    thresh_es_pm_ne = Enum.YLeaf(524288, "thresh-es-pm-ne")

    thresh_ses_pm_ne = Enum.YLeaf(524289, "thresh-ses-pm-ne")

    thresh_uas_pm_ne = Enum.YLeaf(524290, "thresh-uas-pm-ne")

    thresh_bbe_pm_ne = Enum.YLeaf(524291, "thresh-bbe-pm-ne")

    thresh_fc_pm_ne = Enum.YLeaf(524292, "thresh-fc-pm-ne")

    thresh_esr_pm_ne = Enum.YLeaf(524293, "thresh-esr-pm-ne")

    thresh_sesr_pm_ne = Enum.YLeaf(524294, "thresh-sesr-pm-ne")

    thresh_bber_pm_ne = Enum.YLeaf(524295, "thresh-bber-pm-ne")

    thresh_es_sm_fe = Enum.YLeaf(1048584, "thresh-es-sm-fe")

    thresh_ses_sm_fe = Enum.YLeaf(1048585, "thresh-ses-sm-fe")

    thresh_uas_sm_fe = Enum.YLeaf(1048586, "thresh-uas-sm-fe")

    thresh_bbe_sm_fe = Enum.YLeaf(1048587, "thresh-bbe-sm-fe")

    thresh_fc_sm_fe = Enum.YLeaf(1048588, "thresh-fc-sm-fe")

    thresh_esr_sm_fe = Enum.YLeaf(1048589, "thresh-esr-sm-fe")

    thresh_sesr_sm_fe = Enum.YLeaf(1048590, "thresh-sesr-sm-fe")

    thresh_bber_sm_fe = Enum.YLeaf(1048591, "thresh-bber-sm-fe")

    thresh_es_pm_fe = Enum.YLeaf(2097160, "thresh-es-pm-fe")

    thresh_ses_pm_fe = Enum.YLeaf(2097161, "thresh-ses-pm-fe")

    thresh_uas_pm_fe = Enum.YLeaf(2097162, "thresh-uas-pm-fe")

    thresh_bbe_pm_fe = Enum.YLeaf(2097163, "thresh-bbe-pm-fe")

    thresh_fc_pm_fe = Enum.YLeaf(2097164, "thresh-fc-pm-fe")

    thresh_esr_pm_fe = Enum.YLeaf(2097165, "thresh-esr-pm-fe")

    thresh_sesr_pm_fe = Enum.YLeaf(2097166, "thresh-sesr-pm-fe")

    thresh_bber_pm_fe = Enum.YLeaf(2097167, "thresh-bber-pm-fe")


class PathReport(Enum):
    """
    PathReport (Enum Class)

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

    report_cv = Enum.YLeaf(5242880, "report-cv")

    report_es = Enum.YLeaf(5242881, "report-es")

    report_ses = Enum.YLeaf(5242882, "report-ses")

    report_uas = Enum.YLeaf(5242883, "report-uas")


class PathThreshold(Enum):
    """
    PathThreshold (Enum Class)

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

    thresh_cv = Enum.YLeaf(5242880, "thresh-cv")

    thresh_es = Enum.YLeaf(5242881, "thresh-es")

    thresh_ses = Enum.YLeaf(5242882, "thresh-ses")

    thresh_uas = Enum.YLeaf(5242883, "thresh-uas")


class PcsReport(Enum):
    """
    PcsReport (Enum Class)

    Pcs report

    .. data:: report_bip = 100663296

    	PM PCS Bip report

    .. data:: report_frm_err = 100663297

    	PM PCS frm-err report

    """

    report_bip = Enum.YLeaf(100663296, "report-bip")

    report_frm_err = Enum.YLeaf(100663297, "report-frm-err")


class PcsThreshold(Enum):
    """
    PcsThreshold (Enum Class)

    Pcs threshold

    .. data:: thresh_bip = 83886080

    	PM PCS Bip thresh

    .. data:: thresh_frm_err = 83886081

    	PM PCS frm-err thresh

    """

    thresh_bip = Enum.YLeaf(83886080, "thresh-bip")

    thresh_frm_err = Enum.YLeaf(83886081, "thresh-frm-err")


class Report(Enum):
    """
    Report (Enum Class)

    Report

    .. data:: false = 0

    	Performance Monitoring Disabled

    .. data:: true = 1

    	Performance Monitoring Enabled

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class SecyifReport(Enum):
    """
    SecyifReport (Enum Class)

    Secyif report

    .. data:: report_if_inpkts_untagged = 134217728

    	PM SECYIF if InPktsUntagged report

    .. data:: report_if_inpkts_not_ag = 134217729

    	PM SECYIF if InPktsNoTag report

    .. data:: report_if_inpktsbadtag = 134217730

    	PM SECYIF if InPktsBadTag report

    .. data:: report_if_inpkts_unknown_sci = 134217731

    	PM SECYIF if InPktsUnknownSCI report

    .. data:: report_if_inpktsnosci = 134217732

    	PM SECYIF if InPktsNoSCI report

    .. data:: report_if_inpkts_overrun = 134217733

    	PM SECYIF if InPktsOverrun report

    .. data:: report_if_inoctets_validate_d = 134217734

    	PM SECYIF if InOctetsValidated report

    .. data:: report_if_inoctetsdecrypted = 134217735

    	PM SECYIF if InOctetsDecrypted report

    .. data:: report_if_outpkts_untagged = 134217736

    	PM SECYIF if OutPktsUntagged report

    .. data:: report_if_outpkts_too_long = 134217737

    	PM SECYIF if OutPktsTooLong report

    .. data:: report_if_outoctetsprotected = 134217738

    	PM SECYIF if OutOctetsProtected report

    .. data:: report_if_outoctetsencrypted = 134217739

    	PM SECYIF if OutOctetsEncrypted report

    """

    report_if_inpkts_untagged = Enum.YLeaf(134217728, "report-if-inpkts-untagged")

    report_if_inpkts_not_ag = Enum.YLeaf(134217729, "report-if-inpkts-not-ag")

    report_if_inpktsbadtag = Enum.YLeaf(134217730, "report-if-inpktsbadtag")

    report_if_inpkts_unknown_sci = Enum.YLeaf(134217731, "report-if-inpkts-unknown-sci")

    report_if_inpktsnosci = Enum.YLeaf(134217732, "report-if-inpktsnosci")

    report_if_inpkts_overrun = Enum.YLeaf(134217733, "report-if-inpkts-overrun")

    report_if_inoctets_validate_d = Enum.YLeaf(134217734, "report-if-inoctets-validate-d")

    report_if_inoctetsdecrypted = Enum.YLeaf(134217735, "report-if-inoctetsdecrypted")

    report_if_outpkts_untagged = Enum.YLeaf(134217736, "report-if-outpkts-untagged")

    report_if_outpkts_too_long = Enum.YLeaf(134217737, "report-if-outpkts-too-long")

    report_if_outoctetsprotected = Enum.YLeaf(134217738, "report-if-outoctetsprotected")

    report_if_outoctetsencrypted = Enum.YLeaf(134217739, "report-if-outoctetsencrypted")


class SecyifThreshold(Enum):
    """
    SecyifThreshold (Enum Class)

    Secyif threshold

    .. data:: thresh_if_inpkts_untagged = 150994944

    	PM SECYIF if InPktsUntagged thresh

    .. data:: thresh_if_inpkts_not_ag = 150994945

    	PM SECYIF if InPktsNoTag thresh

    .. data:: thresh_if_inpktsbadtag = 150994946

    	PM SECYIF if InPktsBadTag thresh

    .. data:: thresh_if_inpktsunkownsci = 150994947

    	PM SECYIF if InPktsUnknownSCI thresh

    .. data:: thresh_if_inpktsnosci = 150994948

    	PM SECYIF if InPktsNoSCI thresh

    .. data:: thresh_if_inpkts_overrun = 150994949

    	PM SECYIF if InPktsOverrun thresh

    .. data:: thresh_if_inoctets_validate_d = 150994950

    	PM SECYIF if InOctetsValidated thresh

    .. data:: thresh_if_inoctetsdecrypted = 150994951

    	PM SECYIF if InOctetsDecrypted thresh

    .. data:: thresh_if_outpkts_untagged = 150994952

    	PM SECYIF if OutPktsUntagged thresh

    .. data:: thresh_if_thresh_outpkts_too_long = 150994953

    	PM SECYIF if OutPktsTooLong thresh

    .. data:: thresh_if_outoctetsprotected = 150994954

    	PM SECYIF if OutOctetsProtected thresh

    .. data:: thresh_if_outoctetsencrypted = 150994955

    	PM SECYIF if OutOctetsEncrypted thresh

    """

    thresh_if_inpkts_untagged = Enum.YLeaf(150994944, "thresh-if-inpkts-untagged")

    thresh_if_inpkts_not_ag = Enum.YLeaf(150994945, "thresh-if-inpkts-not-ag")

    thresh_if_inpktsbadtag = Enum.YLeaf(150994946, "thresh-if-inpktsbadtag")

    thresh_if_inpktsunkownsci = Enum.YLeaf(150994947, "thresh-if-inpktsunkownsci")

    thresh_if_inpktsnosci = Enum.YLeaf(150994948, "thresh-if-inpktsnosci")

    thresh_if_inpkts_overrun = Enum.YLeaf(150994949, "thresh-if-inpkts-overrun")

    thresh_if_inoctets_validate_d = Enum.YLeaf(150994950, "thresh-if-inoctets-validate-d")

    thresh_if_inoctetsdecrypted = Enum.YLeaf(150994951, "thresh-if-inoctetsdecrypted")

    thresh_if_outpkts_untagged = Enum.YLeaf(150994952, "thresh-if-outpkts-untagged")

    thresh_if_thresh_outpkts_too_long = Enum.YLeaf(150994953, "thresh-if-thresh-outpkts-too-long")

    thresh_if_outoctetsprotected = Enum.YLeaf(150994954, "thresh-if-outoctetsprotected")

    thresh_if_outoctetsencrypted = Enum.YLeaf(150994955, "thresh-if-outoctetsencrypted")


class SecyrxReport(Enum):
    """
    SecyrxReport (Enum Class)

    Secyrx report

    .. data:: report_rx_inpktsun_check_ed = 117440512

    	PM SECYRX rx InPktsUnchecked report

    .. data:: report_rx_inpkts_delayed = 117440513

    	PM SECYRX rx InPktsDelayed report

    .. data:: report_rx_inpktslate = 117440514

    	PM SECYRX rx InPktsLate report

    .. data:: report_rx_inpktsok = 117440515

    	PM SECYRX rx InPktsOK report

    .. data:: report_rx_inpkts_invalid = 117440516

    	PM SECYRX rx InPktsInvalid report

    .. data:: report_rx_inpkts_not_valid = 117440517

    	PM SECYRX rx InPktsNotValid report

    .. data:: report_rx_inpkts_not_usingsa = 117440518

    	PM SECYRX rx InPktsNotUsingSA sa report

    .. data:: report_rx_inpktsunusedsa = 117440519

    	PM SECYRX rx InPktsUnusedSA report

    .. data:: report_rx_inpkts_untagged_hit = 117440520

    	PM SECYRX rx InPktsUntaggedHit report

    .. data:: report_rx_inoctets_validate_d = 117440521

    	PM SECYRX rx InOctetsValidated report

    .. data:: report_rx_inoctetsdecrypted = 117440522

    	PM SECYRX rx InOctetsDecrypted report

    """

    report_rx_inpktsun_check_ed = Enum.YLeaf(117440512, "report-rx-inpktsun-check-ed")

    report_rx_inpkts_delayed = Enum.YLeaf(117440513, "report-rx-inpkts-delayed")

    report_rx_inpktslate = Enum.YLeaf(117440514, "report-rx-inpktslate")

    report_rx_inpktsok = Enum.YLeaf(117440515, "report-rx-inpktsok")

    report_rx_inpkts_invalid = Enum.YLeaf(117440516, "report-rx-inpkts-invalid")

    report_rx_inpkts_not_valid = Enum.YLeaf(117440517, "report-rx-inpkts-not-valid")

    report_rx_inpkts_not_usingsa = Enum.YLeaf(117440518, "report-rx-inpkts-not-usingsa")

    report_rx_inpktsunusedsa = Enum.YLeaf(117440519, "report-rx-inpktsunusedsa")

    report_rx_inpkts_untagged_hit = Enum.YLeaf(117440520, "report-rx-inpkts-untagged-hit")

    report_rx_inoctets_validate_d = Enum.YLeaf(117440521, "report-rx-inoctets-validate-d")

    report_rx_inoctetsdecrypted = Enum.YLeaf(117440522, "report-rx-inoctetsdecrypted")


class SecyrxThreshold(Enum):
    """
    SecyrxThreshold (Enum Class)

    Secyrx threshold

    .. data:: thresh_rx_inpktsun_check_ed = 117440512

    	PM SECYRX rx InPktsUnchecked thresh

    .. data:: thresh_rx_inpkts_delayed = 117440513

    	PM SECYRX rx InPktsDelayed thresh

    .. data:: thresh_rx_inpktslate = 117440514

    	PM SECYRX rx InPktsLate thresh

    .. data:: thresh_rx_inpktsok = 117440515

    	PM SECYRX rx InPktsOK thresh

    .. data:: thresh_rx_inpkts_invalid = 117440516

    	PM SECYRX rx InPktsInvalid thresh

    .. data:: thresh_rx_inpkts_not_valid = 117440517

    	PM SECYRX rx InPktsNotValid thresh

    .. data:: thresh_rx_inpkts_not_usingsa = 117440518

    	PM SECYRX rx InPktsNotUsingSA thresh

    .. data:: thresh_rx_inpktsunusedsa = 117440519

    	PM SECYRX rx InPktsUnusedSA thresh

    .. data:: thresh_rx_inpkts_untagged_hit = 117440520

    	PM SECYRX rx InPktsUntaggedHit thresh

    .. data:: thresh_rx_inoctets_validate_d = 117440521

    	PM SECYRX rx InOctetsValidated thresh

    .. data:: thresh_rx_inoctetsdecrypted = 117440522

    	PM SECYRX rx InOctetsDecrypted thresh

    """

    thresh_rx_inpktsun_check_ed = Enum.YLeaf(117440512, "thresh-rx-inpktsun-check-ed")

    thresh_rx_inpkts_delayed = Enum.YLeaf(117440513, "thresh-rx-inpkts-delayed")

    thresh_rx_inpktslate = Enum.YLeaf(117440514, "thresh-rx-inpktslate")

    thresh_rx_inpktsok = Enum.YLeaf(117440515, "thresh-rx-inpktsok")

    thresh_rx_inpkts_invalid = Enum.YLeaf(117440516, "thresh-rx-inpkts-invalid")

    thresh_rx_inpkts_not_valid = Enum.YLeaf(117440517, "thresh-rx-inpkts-not-valid")

    thresh_rx_inpkts_not_usingsa = Enum.YLeaf(117440518, "thresh-rx-inpkts-not-usingsa")

    thresh_rx_inpktsunusedsa = Enum.YLeaf(117440519, "thresh-rx-inpktsunusedsa")

    thresh_rx_inpkts_untagged_hit = Enum.YLeaf(117440520, "thresh-rx-inpkts-untagged-hit")

    thresh_rx_inoctets_validate_d = Enum.YLeaf(117440521, "thresh-rx-inoctets-validate-d")

    thresh_rx_inoctetsdecrypted = Enum.YLeaf(117440522, "thresh-rx-inoctetsdecrypted")


class SecytxReport(Enum):
    """
    SecytxReport (Enum Class)

    Secytx report

    .. data:: report_tx_outpktsprotected = 150994944

    	PM SECYTX tx OutPktsProtected report

    .. data:: report_tx_outpktsencrypted = 150994945

    	PM SECYTX tx OutPktsEncrypted report

    .. data:: report_tx_outoctetsprotected = 150994946

    	PM SECYTX tx OutOctetsProtected report

    .. data:: report_tx_outoctetsencrypted = 150994947

    	PM SECYTX tx OutOctetsEncrypted report

    .. data:: report_tx_outpkts_too_long = 150994948

    	PM SECYTX tx OutPktsTooLong report

    """

    report_tx_outpktsprotected = Enum.YLeaf(150994944, "report-tx-outpktsprotected")

    report_tx_outpktsencrypted = Enum.YLeaf(150994945, "report-tx-outpktsencrypted")

    report_tx_outoctetsprotected = Enum.YLeaf(150994946, "report-tx-outoctetsprotected")

    report_tx_outoctetsencrypted = Enum.YLeaf(150994947, "report-tx-outoctetsencrypted")

    report_tx_outpkts_too_long = Enum.YLeaf(150994948, "report-tx-outpkts-too-long")


class SecytxThreshold(Enum):
    """
    SecytxThreshold (Enum Class)

    Secytx threshold

    .. data:: thresh_tx_outpktsprotected = 134217728

    	PM SECYTX tx OutPktsProtected thresh

    .. data:: thresh_tx_outpktsencrypted = 134217729

    	PM SECYTX tx OutPktsEncrypted thresh

    .. data:: thresh_tx_outoctetsprotected = 134217730

    	PM SECYTX tx OutOctetsProtected thresh

    .. data:: thresh_tx_outoctetsencrypted = 134217731

    	PM SECYTX tx OutOctetsEncrypted thresh

    .. data:: thresh_tx_outpkts_too_long = 134217732

    	PM SECYTX tx OutPktsTooLong thresh

    """

    thresh_tx_outpktsprotected = Enum.YLeaf(134217728, "thresh-tx-outpktsprotected")

    thresh_tx_outpktsencrypted = Enum.YLeaf(134217729, "thresh-tx-outpktsencrypted")

    thresh_tx_outoctetsprotected = Enum.YLeaf(134217730, "thresh-tx-outoctetsprotected")

    thresh_tx_outoctetsencrypted = Enum.YLeaf(134217731, "thresh-tx-outoctetsencrypted")

    thresh_tx_outpkts_too_long = Enum.YLeaf(134217732, "thresh-tx-outpkts-too-long")


class StmReport(Enum):
    """
    StmReport (Enum Class)

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

    report_ebs = Enum.YLeaf(16777217, "report-ebs")

    report_ess = Enum.YLeaf(16777218, "report-ess")

    report_esrs = Enum.YLeaf(16777219, "report-esrs")

    report_sess = Enum.YLeaf(16777220, "report-sess")

    report_sesrs = Enum.YLeaf(16777221, "report-sesrs")

    report_bbes = Enum.YLeaf(16777222, "report-bbes")

    report_bbesr = Enum.YLeaf(16777223, "report-bbesr")

    report_uass = Enum.YLeaf(16777224, "report-uass")

    report_ebl_ne = Enum.YLeaf(16777225, "report-ebl-ne")

    report_esl_ne = Enum.YLeaf(16777226, "report-esl-ne")

    report_eslr_ne = Enum.YLeaf(16777227, "report-eslr-ne")

    report_sesl_ne = Enum.YLeaf(16777228, "report-sesl-ne")

    report_sesrl_ne = Enum.YLeaf(16777229, "report-sesrl-ne")

    report_bbel_ne = Enum.YLeaf(16777230, "report-bbel-ne")

    report_bberl_ne = Enum.YLeaf(16777231, "report-bberl-ne")

    report_uasl_ne = Enum.YLeaf(16777232, "report-uasl-ne")

    report_ebl_fe = Enum.YLeaf(16777245, "report-ebl-fe")

    report_esl_fe = Enum.YLeaf(16777246, "report-esl-fe")

    report_esrl_fe = Enum.YLeaf(16777247, "report-esrl-fe")

    report_sesl_fe = Enum.YLeaf(16777248, "report-sesl-fe")

    report_sesrl_fe = Enum.YLeaf(16777249, "report-sesrl-fe")

    report_bbel_fe = Enum.YLeaf(16777250, "report-bbel-fe")

    report_bberl_fe = Enum.YLeaf(16777251, "report-bberl-fe")

    report_uasl_fe = Enum.YLeaf(16777252, "report-uasl-fe")


class StmThreshold(Enum):
    """
    StmThreshold (Enum Class)

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

    thresh_ebs = Enum.YLeaf(16777217, "thresh-ebs")

    thresh_ess = Enum.YLeaf(16777218, "thresh-ess")

    thresh_esrs = Enum.YLeaf(16777219, "thresh-esrs")

    thresh_sess = Enum.YLeaf(16777220, "thresh-sess")

    thresh_sesrs = Enum.YLeaf(16777221, "thresh-sesrs")

    thresh_bbes = Enum.YLeaf(16777222, "thresh-bbes")

    thresh_bbesr = Enum.YLeaf(16777223, "thresh-bbesr")

    thresh_uass = Enum.YLeaf(16777224, "thresh-uass")

    thresh_ebl_ne = Enum.YLeaf(16777225, "thresh-ebl-ne")

    thresh_esl_ne = Enum.YLeaf(16777226, "thresh-esl-ne")

    thresh_eslr_ne = Enum.YLeaf(16777227, "thresh-eslr-ne")

    thresh_sesl_ne = Enum.YLeaf(16777228, "thresh-sesl-ne")

    thresh_sesrl_ne = Enum.YLeaf(16777229, "thresh-sesrl-ne")

    thresh_bbel_ne = Enum.YLeaf(16777230, "thresh-bbel-ne")

    thresh_bberl_ne = Enum.YLeaf(16777231, "thresh-bberl-ne")

    thresh_uasl_ne = Enum.YLeaf(16777232, "thresh-uasl-ne")

    thresh_ebl_fe = Enum.YLeaf(16777245, "thresh-ebl-fe")

    thresh_esl_fe = Enum.YLeaf(16777246, "thresh-esl-fe")

    thresh_esrl_fe = Enum.YLeaf(16777247, "thresh-esrl-fe")

    thresh_sesl_fe = Enum.YLeaf(16777248, "thresh-sesl-fe")

    thresh_sesrl_fe = Enum.YLeaf(16777249, "thresh-sesrl-fe")

    thresh_bbel_fe = Enum.YLeaf(16777250, "thresh-bbel-fe")

    thresh_bberl_fe = Enum.YLeaf(16777251, "thresh-bberl-fe")

    thresh_uasl_fe = Enum.YLeaf(16777252, "thresh-uasl-fe")


class StsReport(Enum):
    """
    StsReport (Enum Class)

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

    report_cv = Enum.YLeaf(4194304, "report-cv")

    report_es = Enum.YLeaf(4194305, "report-es")

    report_ses = Enum.YLeaf(4194306, "report-ses")

    report_uas = Enum.YLeaf(4194307, "report-uas")


class StsThreshold(Enum):
    """
    StsThreshold (Enum Class)

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

    thresh_cv = Enum.YLeaf(4194304, "thresh-cv")

    thresh_es = Enum.YLeaf(4194305, "thresh-es")

    thresh_ses = Enum.YLeaf(4194306, "thresh-ses")

    thresh_uas = Enum.YLeaf(4194307, "thresh-uas")




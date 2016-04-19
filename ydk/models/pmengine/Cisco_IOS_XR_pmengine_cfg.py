""" Cisco_IOS_XR_pmengine_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pmengine package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EtherReportEnum(Enum):
    """
    EtherReportEnum

    Ether report

    .. data:: REPORT_RX_PKT = 524290

    	PM Ether rx pkt report

    .. data:: REPORT_STAT_PKT = 524291

    	PM ether stat pkt threshold

    .. data:: REPORT_OCTET_STAT = 524292

    	PM Ether octet stat report

    .. data:: REPORT_OVER_SIZE_PKT = 524293

    	PM Ether oversize pkt report

    .. data:: REPORT_FCS_ERR = 524294

    	PM Ether fcs error report

    .. data:: REPORT_LONG_FRAME_S = 524295

    	PM Ether long frames report

    .. data:: REPORT_JABBER_STATS = 524296

    	PM Ether jabber stats report

    .. data:: REPORT_64_OCTET = 524297

    	PM Ether 64 octet report

    .. data:: REPORT_65_127_OCTET = 524298

    	PM Ether 65 to 127 octet report

    .. data:: REPORT_128_255_OCTET = 524299

    	PM Ether 128 to 255 octet report

    .. data:: REPORT_256_511_OCTET = 524300

    	PM Ether 256 to 511 octet report

    .. data:: REPORT_512_1023_OCTET = 524301

    	PM Ether 512 to 1023 octet report

    .. data:: REPORT_1024_1518_OCTET = 524302

    	PM Ether 1024 to 1518 report

    .. data:: REPORT_IN_UCAST = 524303

    	PM Ether rx ucast report

    .. data:: REPORT_IN_MCAST = 524304

    	PM Ether rx mcast report

    .. data:: REPORT_IN_BCAST = 524305

    	PM Ether rx bcast report

    .. data:: REPORT_OUT_UCAST = 524306

    	PM Ether tx ucast report

    .. data:: REPORT_OUT_MCAST = 524307

    	PM Ether tx mcast report

    .. data:: REPORT_OUT_BCAST = 524308

    	PM Ether tx bcast report

    .. data:: REPORT_TX_PKT = 524309

    	PM Ether tx pkt threshold

    .. data:: REPORT_IFIN_ERROR_S = 524310

    	PM ether ifIn errors threshold

    .. data:: REPORT_IFIN_OCTETS = 524311

    	PM ether ifInOctets threshold

    .. data:: REPORT_ETHER_STAT_MULTICAST_PKT = 524312

    	PM ether stat multicast pkt threshold

    .. data:: REPORT_ETHER_STAT_BROADCAST_PKT = 524313

    	PM ether stat broadcast pkt threshold

    .. data:: REPORT_ETHER_STAT_UNDER_SIZE_D_PKT = 524314

    	PM ether stat undersized pkt threshold

    .. data:: REPORT_OUT_OCTET = 524315

    	PM ether out octets threshold

    .. data:: REPORT_IN_PAUSE_FRAME = 524316

    	PM ether in pause frame report

    .. data:: REPORT_IN_GO_OD_BYTES = 524317

    	PM in good bytes report

    .. data:: REPORT_IN_802_1Q_FRAME_S = 524318

    	PM in 802_1 Q report

    .. data:: REPORT_IN_PKTS_1519_MAX_OCTETS = 524319

    	PM in pkts 1519 max octets report

    .. data:: REPORT_IN_GO_OD_PKTS = 524320

    	PM in good pkts report

    .. data:: REPORT_IN_DROP_OVERRUN = 524321

    	PM in drop overrun report

    .. data:: REPORT_IN_DROP_ABORT = 524322

    	PM in drop abort report

    .. data:: REPORT_IN_DROP_INVALID_VLAN = 524323

    	PM in drop invalid vlan report

    .. data:: REPORT_IN_DROP_INVALID_DMAC = 524324

    	PM in drop invalid DMAC report

    .. data:: REPORT_IN_DROP_INVALID_ENCAP = 524325

    	PM in drop invalid encap report

    .. data:: REPORT_IN_DROP_OTHER = 524326

    	PM in drop other report

    .. data:: REPORT_IN_MIB_GIANT = 524327

    	PM in MIB giant report

    .. data:: REPORT_IN_MIB_JABBER = 524328

    	PM in MIB jabber report

    .. data:: REPORT_IN_MIB_CRC = 524329

    	PM in MIB CRC report

    .. data:: REPORT_IN_ERROR_COLLISION_S = 524330

    	PM in error collisions report

    .. data:: REPORT_IN_ERROR_SYMBOL = 524331

    	PM in error symbol report

    .. data:: REPORT_OUT_GO_OD_BYTES = 524332

    	PM out good bytes report

    .. data:: REPORT_OUT_802_1Q_FRAME_S = 524333

    	PM out 802_1 Q report

    .. data:: REPORT_OUT_PAUSE_FRAME_S = 524334

    	PM out pause frame report

    .. data:: REPORT_OUT_PKTS_1519_MAX_OCTETS = 524335

    	PM out pkts 1519 max octets report

    .. data:: REPORT_OUT_GO_OD_PKTS = 524336

    	PM out good pkts report

    .. data:: REPORT_OUT_DROP_UNDER_RUN = 524337

    	PM out drop underrun report

    .. data:: REPORT_OUT_DROP_ABORT = 524338

    	PM out drop abort report

    .. data:: REPORT_OUT_DROP_OTHER = 524339

    	PM out drop other report

    .. data:: REPORT_OUT_ERROR_OTHER = 524340

    	PM out error other report

    .. data:: REPORT_IN_ERROR_GIANT = 524341

    	PM in error giant report

    .. data:: REPORT_IN_ERROR_RUNT = 524342

    	PM in error runt report

    .. data:: REPORT_IN_ERROR_JABBERS = 524343

    	PM in error jabber report

    .. data:: REPORT_IN_ERROR_FRAGMENTS = 524344

    	PM in error fragments report

    .. data:: REPORT_IN_ERROR_OTHER = 524345

    	PM in error other report

    .. data:: REPORT_IN_PKT_64_OCTET = 524346

    	PM in pkt 64 octet report

    .. data:: REPORT_IN_PKTS_65_127OCTETS = 524347

    	PM in pkts 65_127 octets report

    .. data:: REPORT_IN_PKTS_128_255_OCTETS = 524348

    	PM in pkts 128_255 octets report

    .. data:: REPORT_IN_PKTS_256_511_OCTETS = 524349

    	PM in pkts 256_511 octets report

    .. data:: REPORT_IN_PKTS_512_1023_OCTETS = 524350

    	PM in pkts 512_1023 octets report

    .. data:: REPORT_IN_PKTS_1024_1518_OCTETS = 524351

    	PM in pkts 1024_1058 octets report

    .. data:: REPORT_OUT_PKT_64_OCTET = 524352

    	PM out pkt 64 octet report

    .. data:: REPORT_OUT_PKTS_65_127OCTETS = 524353

    	PM out pkts 65_127 octets report

    .. data:: REPORT_OUT_PKTS_128_255_OCTETS = 524354

    	PM out pkts 128_255 octets report

    .. data:: REPORT_OUT_PKTS_256_511_OCTETS = 524355

    	PM out pkts 256_511 octets report

    .. data:: REPORT_OUT_PKTS_512_1023_OCTETS = 524356

    	PM out pkts 512_1023 octets report

    .. data:: REPORT_OUT_PKTS_1024_1518_OCTETS = 524357

    	PM out pkts 1024_1058 octets report

    """

    REPORT_RX_PKT = 524290

    REPORT_STAT_PKT = 524291

    REPORT_OCTET_STAT = 524292

    REPORT_OVER_SIZE_PKT = 524293

    REPORT_FCS_ERR = 524294

    REPORT_LONG_FRAME_S = 524295

    REPORT_JABBER_STATS = 524296

    REPORT_64_OCTET = 524297

    REPORT_65_127_OCTET = 524298

    REPORT_128_255_OCTET = 524299

    REPORT_256_511_OCTET = 524300

    REPORT_512_1023_OCTET = 524301

    REPORT_1024_1518_OCTET = 524302

    REPORT_IN_UCAST = 524303

    REPORT_IN_MCAST = 524304

    REPORT_IN_BCAST = 524305

    REPORT_OUT_UCAST = 524306

    REPORT_OUT_MCAST = 524307

    REPORT_OUT_BCAST = 524308

    REPORT_TX_PKT = 524309

    REPORT_IFIN_ERROR_S = 524310

    REPORT_IFIN_OCTETS = 524311

    REPORT_ETHER_STAT_MULTICAST_PKT = 524312

    REPORT_ETHER_STAT_BROADCAST_PKT = 524313

    REPORT_ETHER_STAT_UNDER_SIZE_D_PKT = 524314

    REPORT_OUT_OCTET = 524315

    REPORT_IN_PAUSE_FRAME = 524316

    REPORT_IN_GO_OD_BYTES = 524317

    REPORT_IN_802_1Q_FRAME_S = 524318

    REPORT_IN_PKTS_1519_MAX_OCTETS = 524319

    REPORT_IN_GO_OD_PKTS = 524320

    REPORT_IN_DROP_OVERRUN = 524321

    REPORT_IN_DROP_ABORT = 524322

    REPORT_IN_DROP_INVALID_VLAN = 524323

    REPORT_IN_DROP_INVALID_DMAC = 524324

    REPORT_IN_DROP_INVALID_ENCAP = 524325

    REPORT_IN_DROP_OTHER = 524326

    REPORT_IN_MIB_GIANT = 524327

    REPORT_IN_MIB_JABBER = 524328

    REPORT_IN_MIB_CRC = 524329

    REPORT_IN_ERROR_COLLISION_S = 524330

    REPORT_IN_ERROR_SYMBOL = 524331

    REPORT_OUT_GO_OD_BYTES = 524332

    REPORT_OUT_802_1Q_FRAME_S = 524333

    REPORT_OUT_PAUSE_FRAME_S = 524334

    REPORT_OUT_PKTS_1519_MAX_OCTETS = 524335

    REPORT_OUT_GO_OD_PKTS = 524336

    REPORT_OUT_DROP_UNDER_RUN = 524337

    REPORT_OUT_DROP_ABORT = 524338

    REPORT_OUT_DROP_OTHER = 524339

    REPORT_OUT_ERROR_OTHER = 524340

    REPORT_IN_ERROR_GIANT = 524341

    REPORT_IN_ERROR_RUNT = 524342

    REPORT_IN_ERROR_JABBERS = 524343

    REPORT_IN_ERROR_FRAGMENTS = 524344

    REPORT_IN_ERROR_OTHER = 524345

    REPORT_IN_PKT_64_OCTET = 524346

    REPORT_IN_PKTS_65_127OCTETS = 524347

    REPORT_IN_PKTS_128_255_OCTETS = 524348

    REPORT_IN_PKTS_256_511_OCTETS = 524349

    REPORT_IN_PKTS_512_1023_OCTETS = 524350

    REPORT_IN_PKTS_1024_1518_OCTETS = 524351

    REPORT_OUT_PKT_64_OCTET = 524352

    REPORT_OUT_PKTS_65_127OCTETS = 524353

    REPORT_OUT_PKTS_128_255_OCTETS = 524354

    REPORT_OUT_PKTS_256_511_OCTETS = 524355

    REPORT_OUT_PKTS_512_1023_OCTETS = 524356

    REPORT_OUT_PKTS_1024_1518_OCTETS = 524357


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherReportEnum']


class EtherThresholdEnum(Enum):
    """
    EtherThresholdEnum

    Ether threshold

    .. data:: THRESH_RX_PKT = 8388610

    	PM Ether rx pkt threshold

    .. data:: THRESH_STAT_PKT = 8388611

    	PM ether stat pkt threshold

    .. data:: THRESH_OCTET_STAT = 8388612

    	PM Ether octet stat threshold

    .. data:: THRESH_OVER_SIZE_PKT = 8388613

    	PM Ether oversize pkt threshold

    .. data:: THRESH_FCS_ERR = 8388614

    	PMEther fcs error threshold

    .. data:: THRESH_LONG_FRAME_S = 8388615

    	PM Ether long frames threshold

    .. data:: THRESH_JABBER_STATS = 8388616

    	PM Ether jabber stats threshold

    .. data:: THRESH_64_OCTET = 8388617

    	PM Ether 64 octet threshold

    .. data:: THRESH_65_127_OCTET = 8388618

    	PM Ether 65 to 127 octet threshold

    .. data:: THRESH_128_255_OCTET = 8388619

    	PM Ether 128 to 255 octet threshold

    .. data:: THRESH_256_511_OCTET = 8388620

    	PM Ether 256 to 511 octet threshold

    .. data:: THRESH_512_1023_OCTET = 8388621

    	PM Ether 512 to 1023 octet threshold

    .. data:: THRESH_1024_1518_OCTET = 8388622

    	PM Ether 1024 to 1518 threshold

    .. data:: THRESH_IN_UCAST = 8388623

    	PM Ether rx ucast threshold

    .. data:: THRESH_IN_MCAST = 8388624

    	PM Ether rx mcast threshold

    .. data:: THRESH_IN_BCAST = 8388625

    	PM Ether rx bcast threshold

    .. data:: THRESH_OUT_UCAST = 8388626

    	PM Ether tx ucast threshold

    .. data:: THRESH_OUT_MCAST = 8388627

    	PM Ether tx mcast threshold

    .. data:: THRESH_OUT_BCAST = 8388628

    	PM Ether tx bcast threshold

    .. data:: THRESH_TX_PKT = 8388629

    	PM Ether tx pkt threshold

    .. data:: THRESH_IFIN_ERROR_S = 8388630

    	PM ether ifIn errors threshold

    .. data:: THRESH_IFIN_OCTETS = 8388631

    	PM ether ifInOctets threshold

    .. data:: THRESH_ETHER_STAT_MULTICAST_PKT = 8388632

    	PM ether stat multicast pkt threshold

    .. data:: THRESH_ETHER_STAT_BROADCAST_PKT = 8388633

    	PM ether stat broadcast pkt threshold

    .. data:: THRESH_ETHER_STAT_UNDER_SIZE_D_PKT = 8388634

    	PM ether stat undersized pkt threshold

    .. data:: THRESH_OUT_OCTET = 8388635

    	PM ether out octets threshold

    .. data:: THRESH_IN_PAUSE_FRAME = 8388636

    	PM in pause frame threshold

    .. data:: THRESH_IN_GO_OD_BYTES = 8388637

    	PM in good bytes threshold

    .. data:: THRESH_IN_802_1Q_FRAME_S = 8388638

    	PM in 802_1 Q threshold

    .. data:: THRESH_IN_PKTS_1519_MAX_OCTETS = 8388639

    	PM in pkts 1519 max octets threshold

    .. data:: THRESH_IN_GO_OD_PKTS = 8388640

    	PM in good pkts threshold

    .. data:: THRESH_IN_DROP_OVERRUN = 8388641

    	PM in drop overrun threshold

    .. data:: THRESH_IN_DROP_ABORT = 8388642

    	PM in drop abort threshold

    .. data:: THRESH_IN_DROP_INVALID_VLAN = 8388643

    	PM in drop invalid vlan threshold

    .. data:: THRESH_IN_DROP_INVALID_DMAC = 8388644

    	PM in drop invalid DMAC threshold

    .. data:: THRESH_IN_DROP_INVALID_ENCAP = 8388645

    	PM in drop invalid encap threshold

    .. data:: THRESH_IN_DROP_OTHER = 8388646

    	PM in drop other threshold

    .. data:: THRESH_IN_MIB_GIANT = 8388647

    	PM in MIB giant threshold

    .. data:: THRESH_IN_MIB_JABBER = 8388648

    	PM in MIB jabber threshold

    .. data:: THRESH_IN_MIB_CRC = 8388649

    	PM in MIB CRC threshold

    .. data:: THRESH_IN_ERROR_COLLISION_S = 8388650

    	PM in error collisions threshold

    .. data:: THRESH_IN_ERROR_SYMBOL = 8388651

    	PM in error symbol threshold

    .. data:: THRESH_OUT_GO_OD_BYTES = 8388652

    	PM out good bytes threshold

    .. data:: THRESH_OUT_802_1Q_FRAME_S = 8388653

    	PM out 802_1 Q threshold

    .. data:: THRESH_OUT_PAUSE_FRAME_S = 8388654

    	PM out pause frame threshold

    .. data:: THRESH_OUT_PKTS_1519_MAX_OCTETS = 8388655

    	PM out pkts 1519 max octets threshold

    .. data:: THRESH_OUT_GO_OD_PKTS = 8388656

    	PM out good pkts threshold

    .. data:: THRESH_OUT_DROP_UNDER_RUN = 8388657

    	PM out drop underrun threshold

    .. data:: THRESH_OUT_DROP_ABORT = 8388658

    	PM out drop abort threshold

    .. data:: THRESH_OUT_DROP_OTHER = 8388659

    	PM out drop other threshold

    .. data:: THRESH_OUT_ERROR_OTHER = 8388660

    	PM out error other threshold

    .. data:: THRESH_IN_ERROR_GIANT = 8388661

    	PM in error giant threshold

    .. data:: THRESH_IN_ERROR_RUNT = 8388662

    	PM in error runt threshold

    .. data:: THRESH_IN_ERROR_JABBERS = 8388663

    	PM in error jabber threshold

    .. data:: THRESH_IN_ERROR_FRAGMENTS = 8388664

    	PM in error fragments threshold

    .. data:: THRESH_IN_ERROR_OTHER = 8388665

    	PM in error other threshold

    .. data:: THRESH_IN_PKT_64_OCTET = 8388666

    	PM in pkt 64 octet threshold

    .. data:: THRESH_IN_PKTS_65_127OCTETS = 8388667

    	PM in pkts 65_127 octets threshold

    .. data:: THRESH_IN_PKTS_128_255_OCTETS = 8388668

    	PM in pkts 128_255 octets threshold

    .. data:: THRESH_IN_PKTS_256_511_OCTETS = 8388669

    	PM in pkts 256_511 octets threshold

    .. data:: THRESH_IN_PKTS_512_1023_OCTETS = 8388670

    	PM in pkts 512_1023 octets threshold

    .. data:: THRESH_IN_PKTS_1024_1518_OCTETS = 8388671

    	PM in pkts 1024_1058 octets threshold

    .. data:: THRESH_OUT_PKT_64_OCTET = 8388672

    	PM out pkt 64 octet threshold

    .. data:: THRESH_OUT_PKTS_65_127OCTETS = 8388673

    	PM out pkts 65_127 octets threshold

    .. data:: THRESH_OUT_PKTS_128_255_OCTETS = 8388674

    	PM out pkts 128_255 octets threshold

    .. data:: THRESH_OUT_PKTS_256_511_OCTETS = 8388675

    	PM out pkts 256_511 octets threshold

    .. data:: THRESH_OUT_PKTS_512_1023_OCTETS = 8388676

    	PM out pkts 512_1023 octets threshold

    .. data:: THRESH_OUT_PKTS_1024_1518_OCTETS = 8388677

    	PM out pkts 1024_1058 octets threshold

    """

    THRESH_RX_PKT = 8388610

    THRESH_STAT_PKT = 8388611

    THRESH_OCTET_STAT = 8388612

    THRESH_OVER_SIZE_PKT = 8388613

    THRESH_FCS_ERR = 8388614

    THRESH_LONG_FRAME_S = 8388615

    THRESH_JABBER_STATS = 8388616

    THRESH_64_OCTET = 8388617

    THRESH_65_127_OCTET = 8388618

    THRESH_128_255_OCTET = 8388619

    THRESH_256_511_OCTET = 8388620

    THRESH_512_1023_OCTET = 8388621

    THRESH_1024_1518_OCTET = 8388622

    THRESH_IN_UCAST = 8388623

    THRESH_IN_MCAST = 8388624

    THRESH_IN_BCAST = 8388625

    THRESH_OUT_UCAST = 8388626

    THRESH_OUT_MCAST = 8388627

    THRESH_OUT_BCAST = 8388628

    THRESH_TX_PKT = 8388629

    THRESH_IFIN_ERROR_S = 8388630

    THRESH_IFIN_OCTETS = 8388631

    THRESH_ETHER_STAT_MULTICAST_PKT = 8388632

    THRESH_ETHER_STAT_BROADCAST_PKT = 8388633

    THRESH_ETHER_STAT_UNDER_SIZE_D_PKT = 8388634

    THRESH_OUT_OCTET = 8388635

    THRESH_IN_PAUSE_FRAME = 8388636

    THRESH_IN_GO_OD_BYTES = 8388637

    THRESH_IN_802_1Q_FRAME_S = 8388638

    THRESH_IN_PKTS_1519_MAX_OCTETS = 8388639

    THRESH_IN_GO_OD_PKTS = 8388640

    THRESH_IN_DROP_OVERRUN = 8388641

    THRESH_IN_DROP_ABORT = 8388642

    THRESH_IN_DROP_INVALID_VLAN = 8388643

    THRESH_IN_DROP_INVALID_DMAC = 8388644

    THRESH_IN_DROP_INVALID_ENCAP = 8388645

    THRESH_IN_DROP_OTHER = 8388646

    THRESH_IN_MIB_GIANT = 8388647

    THRESH_IN_MIB_JABBER = 8388648

    THRESH_IN_MIB_CRC = 8388649

    THRESH_IN_ERROR_COLLISION_S = 8388650

    THRESH_IN_ERROR_SYMBOL = 8388651

    THRESH_OUT_GO_OD_BYTES = 8388652

    THRESH_OUT_802_1Q_FRAME_S = 8388653

    THRESH_OUT_PAUSE_FRAME_S = 8388654

    THRESH_OUT_PKTS_1519_MAX_OCTETS = 8388655

    THRESH_OUT_GO_OD_PKTS = 8388656

    THRESH_OUT_DROP_UNDER_RUN = 8388657

    THRESH_OUT_DROP_ABORT = 8388658

    THRESH_OUT_DROP_OTHER = 8388659

    THRESH_OUT_ERROR_OTHER = 8388660

    THRESH_IN_ERROR_GIANT = 8388661

    THRESH_IN_ERROR_RUNT = 8388662

    THRESH_IN_ERROR_JABBERS = 8388663

    THRESH_IN_ERROR_FRAGMENTS = 8388664

    THRESH_IN_ERROR_OTHER = 8388665

    THRESH_IN_PKT_64_OCTET = 8388666

    THRESH_IN_PKTS_65_127OCTETS = 8388667

    THRESH_IN_PKTS_128_255_OCTETS = 8388668

    THRESH_IN_PKTS_256_511_OCTETS = 8388669

    THRESH_IN_PKTS_512_1023_OCTETS = 8388670

    THRESH_IN_PKTS_1024_1518_OCTETS = 8388671

    THRESH_OUT_PKT_64_OCTET = 8388672

    THRESH_OUT_PKTS_65_127OCTETS = 8388673

    THRESH_OUT_PKTS_128_255_OCTETS = 8388674

    THRESH_OUT_PKTS_256_511_OCTETS = 8388675

    THRESH_OUT_PKTS_512_1023_OCTETS = 8388676

    THRESH_OUT_PKTS_1024_1518_OCTETS = 8388677


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherThresholdEnum']


class FecReportEnum(Enum):
    """
    FecReportEnum

    Fec report

    .. data:: REPORT_EC_BITS = 131072

    	PM Fec ec bits report

    .. data:: REPORT_UC_WORDS = 131076

    	PM Fec uc words report

    """

    REPORT_EC_BITS = 131072

    REPORT_UC_WORDS = 131076


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecReportEnum']


class FecThresholdEnum(Enum):
    """
    FecThresholdEnum

    Fec threshold

    .. data:: THRESH_EC_BITS = 131072

    	PM Fec ec bits threshold

    .. data:: THRESH_UC_WORDS = 131076

    	PM Fec uc words threshold

    """

    THRESH_EC_BITS = 131072

    THRESH_UC_WORDS = 131076


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecThresholdEnum']


class GfpReportEnum(Enum):
    """
    GfpReportEnum

    Gfp report

    .. data:: REPORT_RX_BIT_ERR = 6291456

    	PM GFP rx bit err report

    .. data:: REPORT_RX_INV_TYP = 6291457

    	PM GFP rx inv type report

    .. data:: REPORT_RX_CRC = 6291458

    	PM GFP rx crc report

    .. data:: REPORT_RX_LFD = 6291459

    	PM GFP rx lfd report

    .. data:: REPORT_RX_CSF = 6291460

    	PM GFP rx csf report

    """

    REPORT_RX_BIT_ERR = 6291456

    REPORT_RX_INV_TYP = 6291457

    REPORT_RX_CRC = 6291458

    REPORT_RX_LFD = 6291459

    REPORT_RX_CSF = 6291460


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpReportEnum']


class GfpThresholdEnum(Enum):
    """
    GfpThresholdEnum

    Gfp threshold

    .. data:: THRESH_RX_BIT_ERR = 67108864

    	PM GFP rx bit err threshold

    .. data:: THRESH_RX_INV_TYP = 67108865

    	PM GFP rx inv type threshold

    .. data:: THRESH_RX_CRC = 67108866

    	PM GFP rx crc threshold

    .. data:: THRESH_RX_LFD = 67108867

    	PM GFP rx lfd threshold

    .. data:: THRESH_RX_CSF = 67108868

    	PM GFP rx csf threshold

    """

    THRESH_RX_BIT_ERR = 67108864

    THRESH_RX_INV_TYP = 67108865

    THRESH_RX_CRC = 67108866

    THRESH_RX_LFD = 67108867

    THRESH_RX_CSF = 67108868


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpThresholdEnum']


class HoVcReportEnum(Enum):
    """
    HoVcReportEnum

    Ho vc report

    .. data:: REPORT_EB = 33554432

    	PM EB report

    .. data:: REPORT_ES = 33554433

    	PM ES report

    .. data:: REPORT_ESR = 33554434

    	PM ESR report

    .. data:: REPORT_SES = 33554435

    	PM SES report

    .. data:: REPORT_SESR = 33554436

    	PM SESR report

    .. data:: REPORT_BBE = 33554437

    	PM BBE report

    .. data:: REPORT_BBER = 33554438

    	PM BBER report

    .. data:: REPORT_UASS = 33554439

    	PM UASS report

    """

    REPORT_EB = 33554432

    REPORT_ES = 33554433

    REPORT_ESR = 33554434

    REPORT_SES = 33554435

    REPORT_SESR = 33554436

    REPORT_BBE = 33554437

    REPORT_BBER = 33554438

    REPORT_UASS = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcReportEnum']


class HoVcThresholdEnum(Enum):
    """
    HoVcThresholdEnum

    Ho vc threshold

    .. data:: THRESH_EB = 33554432

    	PM EB threshold

    .. data:: THRESH_ES = 33554433

    	PM ES threshold

    .. data:: THRESH_ESR = 33554434

    	PM ESR threshold

    .. data:: THRESH_SES = 33554435

    	PM SES threshold

    .. data:: THRESH_SESR = 33554436

    	PM SESR threshold

    .. data:: THRESH_BBE = 33554437

    	PM BBE threshold

    .. data:: THRESH_BBER = 33554438

    	PM BBER threshold

    .. data:: THRESH_UASS = 33554439

    	PM UASS threshold

    """

    THRESH_EB = 33554432

    THRESH_ES = 33554433

    THRESH_ESR = 33554434

    THRESH_SES = 33554435

    THRESH_SESR = 33554436

    THRESH_BBE = 33554437

    THRESH_BBER = 33554438

    THRESH_UASS = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcThresholdEnum']


class OcnReportEnum(Enum):
    """
    OcnReportEnum

    Ocn report

    .. data:: REPORT_SEFSS = 3145728

    	PM SEFSS threshold

    .. data:: REPORT_CVS = 3145729

    	PM CVS threshold

    .. data:: REPORT_ESS = 3145730

    	PM ESS threshold

    .. data:: REPORT_SESS = 3145731

    	PM SESS threshold

    .. data:: REPORT_CVL_NE = 3145734

    	PM CVL-NE threshold

    .. data:: REPORT_ESL_NE = 3145735

    	PM ESL-NE threshold

    .. data:: REPORT_SESL_NE = 3145736

    	PM SESL-NE threshold

    .. data:: REPORT_UASL_NE = 3145738

    	PM UASL-NE threshold

    .. data:: REPORT_FCL_NE = 3145739

    	PM FCL-NE threshold

    .. data:: REPORT_FCL_FE = 3145751

    	PM FCL_FE threshold

    .. data:: REPORT_CVL_FE = 3145752

    	PM CVL-FE threshold

    .. data:: REPORT_ESL_FE = 3145753

    	PM ESL_FE threshold

    .. data:: REPORT_SESL_FE = 3145754

    	PM SESL_FE threshold

    .. data:: REPORT_UASL_FE = 3145756

    	PM UASL_FEthreshold

    """

    REPORT_SEFSS = 3145728

    REPORT_CVS = 3145729

    REPORT_ESS = 3145730

    REPORT_SESS = 3145731

    REPORT_CVL_NE = 3145734

    REPORT_ESL_NE = 3145735

    REPORT_SESL_NE = 3145736

    REPORT_UASL_NE = 3145738

    REPORT_FCL_NE = 3145739

    REPORT_FCL_FE = 3145751

    REPORT_CVL_FE = 3145752

    REPORT_ESL_FE = 3145753

    REPORT_SESL_FE = 3145754

    REPORT_UASL_FE = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnReportEnum']


class OcnThresholdEnum(Enum):
    """
    OcnThresholdEnum

    Ocn threshold

    .. data:: THRESH_SEFSS = 3145728

    	PM SEFSS threshold

    .. data:: THRESH_CVS = 3145729

    	PM CVS threshold

    .. data:: THRESH_ESS = 3145730

    	PM ESS threshold

    .. data:: THRESH_SESS = 3145731

    	PM SESS threshold

    .. data:: THRESH_CVL_NE = 3145734

    	PM CVL-NE threshold

    .. data:: THRESH_ESL_NE = 3145735

    	PM ESL-NE threshold

    .. data:: THRESH_SESL_NE = 3145736

    	PM SESL-NE threshold

    .. data:: THRESH_UASL_NE = 3145738

    	PM UASL-NE threshold

    .. data:: THRESH_FCL_NE = 3145739

    	PM FCL-NE threshold

    .. data:: THRESH_FCL_FE = 3145751

    	PM FCL_FE threshold

    .. data:: THRESH_CVL_FE = 3145752

    	PM CVL-FE threshold

    .. data:: THRESH_ESL_FE = 3145753

    	PM ESL_FE threshold

    .. data:: THRESH_SESL_FE = 3145754

    	PM SESL_FE threshold

    .. data:: THRESH_UASL_FE = 3145756

    	PM UASL_FEthreshold

    """

    THRESH_SEFSS = 3145728

    THRESH_CVS = 3145729

    THRESH_ESS = 3145730

    THRESH_SESS = 3145731

    THRESH_CVL_NE = 3145734

    THRESH_ESL_NE = 3145735

    THRESH_SESL_NE = 3145736

    THRESH_UASL_NE = 3145738

    THRESH_FCL_NE = 3145739

    THRESH_FCL_FE = 3145751

    THRESH_CVL_FE = 3145752

    THRESH_ESL_FE = 3145753

    THRESH_SESL_FE = 3145754

    THRESH_UASL_FE = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnThresholdEnum']


class OpticsReportEnum(Enum):
    """
    OpticsReportEnum

    Optics report

    .. data:: REPORT_OPT_MIN = 65550

    	PM Optics opt min report

    .. data:: REPORT_OPR_MIN = 65551

    	PM Optics opr min report

    .. data:: REPORT_LBC_MIN = 65552

    	PM Optics lbc min report

    .. data:: REPORT_LBC_PC_MIN = 65553

    	PM Optics lbcpc min report

    .. data:: REPORT_CD_MIN = 65557

    	PM Optics cd min report

    .. data:: REPORT_DGD_MIN = 65558

    	PM Optics dgd min report

    .. data:: REPORT_PMD_MIN = 65559

    	PM Optics sopmd min report

    .. data:: REPORT_OSNR_MIN = 65560

    	PM Optics osnr min report

    .. data:: REPORT_PDL_MIN = 65561

    	PM Optics pdl min report

    .. data:: REPORT_PCR_MIN = 65562

    	PM Optics pcr min report

    .. data:: REPORT_PN_MIN = 65563

    	PM Optics pn min report

    .. data:: REPORT_OPT_MAX = 65564

    	PM Optics opt max report

    .. data:: REPORT_OPR_MAX = 65565

    	PM Optics opr max report

    .. data:: REPORT_LBC_MAX = 65566

    	PM Optics lbc max report

    .. data:: REPORT_LBC_PC_MAX = 65567

    	PM Optics lbcpc max report

    .. data:: REPORT_CD_MAX = 65571

    	PM Optics cd max report

    .. data:: REPORT_DGD_MAX = 65572

    	PM Optics dgd max report

    .. data:: REPORT_PMD_MAX = 65573

    	PM Optics sopmd max report

    .. data:: REPORT_OSNR_MAX = 65574

    	PM Optics osnr max report

    .. data:: REPORT_PDL_MAX = 65575

    	PM Optics pdl max report

    .. data:: REPORT_PCR_MAX = 65576

    	PM Optics pcr max report

    .. data:: REPORT_PN_MAX = 65577

    	PM Optics pn max report

    """

    REPORT_OPT_MIN = 65550

    REPORT_OPR_MIN = 65551

    REPORT_LBC_MIN = 65552

    REPORT_LBC_PC_MIN = 65553

    REPORT_CD_MIN = 65557

    REPORT_DGD_MIN = 65558

    REPORT_PMD_MIN = 65559

    REPORT_OSNR_MIN = 65560

    REPORT_PDL_MIN = 65561

    REPORT_PCR_MIN = 65562

    REPORT_PN_MIN = 65563

    REPORT_OPT_MAX = 65564

    REPORT_OPR_MAX = 65565

    REPORT_LBC_MAX = 65566

    REPORT_LBC_PC_MAX = 65567

    REPORT_CD_MAX = 65571

    REPORT_DGD_MAX = 65572

    REPORT_PMD_MAX = 65573

    REPORT_OSNR_MAX = 65574

    REPORT_PDL_MAX = 65575

    REPORT_PCR_MAX = 65576

    REPORT_PN_MAX = 65577


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsReportEnum']


class OpticsThresholdEnum(Enum):
    """
    OpticsThresholdEnum

    Optics threshold

    .. data:: THRESH_OPT_MIN = 65550

    	PM Optics opt min threshold

    .. data:: THRESH_OPR_MIN = 65551

    	PM Optics opr min threshold

    .. data:: THRESH_LBC_MIN = 65552

    	PM Optics lbc min threshold

    .. data:: THRESH_LBC_PC_MIN = 65553

    	PM Optics lbcpc min threshold

    .. data:: THRESH_CD_MIN = 65557

    	PM Optics cd min threshold

    .. data:: THRESH_DGD_MIN = 65558

    	PM Optics dgd min threshold

    .. data:: THRESH_PMD_MIN = 65559

    	PM Optics sopmd min threshold

    .. data:: THRESH_OSNR_MIN = 65560

    	PM Optics osnr min threshold

    .. data:: THRESH_PDL_MIN = 65561

    	PM Optics pdl min threshold

    .. data:: THRESH_PCR_MIN = 65562

    	PM Optics pcr min threshold

    .. data:: THRESH_PN_MIN = 65563

    	PM Optics pn min threshold

    .. data:: THRESH_OPT_MAX = 65564

    	PM Optics opt max threshold

    .. data:: THRESH_OPR_MAX = 65565

    	PM Optics opr max threshold

    .. data:: THRESH_LBC_MAX = 65566

    	PM Optics lbc max threshold

    .. data:: THRESH_LBC_PC_MAX = 65567

    	PM Optics lbcpc max threshold

    .. data:: THRESH_CD_MAX = 65571

    	PM Optics cd max threshold

    .. data:: THRESH_DGD_MAX = 65572

    	PM Optics dgd max threshold

    .. data:: THRESH_PMD_MAX = 65573

    	PM Optics sopmd max threshold

    .. data:: THRESH_OSNR_MAX = 65574

    	PM Optics osnr max threshold

    .. data:: THRESH_PDL_MAX = 65575

    	PM Optics pdl max threshold

    .. data:: THRESH_PCR_MAX = 65576

    	PM Optics pcr max threshold

    .. data:: THRESH_PN_MAX = 65577

    	PM Optics pn max threshold

    """

    THRESH_OPT_MIN = 65550

    THRESH_OPR_MIN = 65551

    THRESH_LBC_MIN = 65552

    THRESH_LBC_PC_MIN = 65553

    THRESH_CD_MIN = 65557

    THRESH_DGD_MIN = 65558

    THRESH_PMD_MIN = 65559

    THRESH_OSNR_MIN = 65560

    THRESH_PDL_MIN = 65561

    THRESH_PCR_MIN = 65562

    THRESH_PN_MIN = 65563

    THRESH_OPT_MAX = 65564

    THRESH_OPR_MAX = 65565

    THRESH_LBC_MAX = 65566

    THRESH_LBC_PC_MAX = 65567

    THRESH_CD_MAX = 65571

    THRESH_DGD_MAX = 65572

    THRESH_PMD_MAX = 65573

    THRESH_OSNR_MAX = 65574

    THRESH_PDL_MAX = 65575

    THRESH_PCR_MAX = 65576

    THRESH_PN_MAX = 65577


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsThresholdEnum']


class OtnReportEnum(Enum):
    """
    OtnReportEnum

    Otn report

    .. data:: REPORT_ES_SM_NE = 262144

    	PM Otn es sm ne report

    .. data:: REPORT_SES_SM_NE = 262145

    	PM Otn ses sm ne report

    .. data:: REPORT_UAS_SM_NE = 262146

    	PM Otn uas sm ne report

    .. data:: REPORT_BBE_SM_NE = 262147

    	PM Otn bbe sm ne report

    .. data:: REPORT_FC_SM_NE = 262148

    	PM Otn fc sm ne report

    .. data:: REPORT_ESR_SM_NE = 262149

    	PM Otn esr sm ne report

    .. data:: REPORT_SESR_SM_NE = 262150

    	PM Otn sesr sm ne report

    .. data:: REPORT_BBER_SM_NE = 262151

    	PM Otn bber sm ne report

    .. data:: REPORT_ES_PM_NE = 524288

    	PM Otn es pm ne report

    .. data:: REPORT_SES_PM_NE = 524289

    	PM Otn ses pm ne report

    .. data:: REPORT_UAS_PM_NE = 524290

    	PM Otn uas pm ne report

    .. data:: REPORT_BBE_PM_NE = 524291

    	PM Otn bbe pm ne report

    .. data:: REPORT_FC_PM_NE = 524292

    	PM Otn fc pm ne report

    .. data:: REPORT_ESR_PM_NE = 524293

    	PM Otn esr pm ne report

    .. data:: REPORT_SESR_PM_NE = 524294

    	PM Otn sesr pm ne report

    .. data:: REPORT_BBER_PM_NE = 524295

    	PM Otn bber pm ne report

    .. data:: REPORT_ES_SM_FE = 1048584

    	PM Otn es sm fe report

    .. data:: REPORT_SES_SM_FE = 1048585

    	PM Otn ses sm fe report

    .. data:: REPORT_UAS_SM_FE = 1048586

    	PM Otn uas sm fe report

    .. data:: REPORT_BBE_SM_FE = 1048587

    	PM Otn bbe sm fe report

    .. data:: REPORT_FC_SM_FE = 1048588

    	PM Otn fc sm fe report

    .. data:: REPORT_ESR_SM_FE = 1048589

    	PM Otn esr sm fe report

    .. data:: REPORT_SESR_SM_FE = 1048590

    	PM Otn sesr sm fe report

    .. data:: REPORT_BBER_SM_FE = 1048591

    	PM Otn bber sm fe report

    .. data:: REPORT_ES_PM_FE = 2097160

    	PM Otn es pm fe report

    .. data:: REPORT_SES_PM_FE = 2097161

    	PM Otn ses pm fe report

    .. data:: REPORT_UAS_PM_FE = 2097162

    	PM Otn uas pm fe report

    .. data:: REPORT_BBE_PM_FE = 2097163

    	PM Otn bbe pm fe report

    .. data:: REPORT_FC_PM_FE = 2097164

    	PM Otn fc pm fe report

    .. data:: REPORT_ESR_PM_FE = 2097165

    	PM Otn esr pm fe report

    .. data:: REPORT_SESR_PM_FE = 2097166

    	PM Otn sesr pm fe report

    .. data:: REPORT_BBER_PM_FE = 2097167

    	PM Otn bber pm fe report

    """

    REPORT_ES_SM_NE = 262144

    REPORT_SES_SM_NE = 262145

    REPORT_UAS_SM_NE = 262146

    REPORT_BBE_SM_NE = 262147

    REPORT_FC_SM_NE = 262148

    REPORT_ESR_SM_NE = 262149

    REPORT_SESR_SM_NE = 262150

    REPORT_BBER_SM_NE = 262151

    REPORT_ES_PM_NE = 524288

    REPORT_SES_PM_NE = 524289

    REPORT_UAS_PM_NE = 524290

    REPORT_BBE_PM_NE = 524291

    REPORT_FC_PM_NE = 524292

    REPORT_ESR_PM_NE = 524293

    REPORT_SESR_PM_NE = 524294

    REPORT_BBER_PM_NE = 524295

    REPORT_ES_SM_FE = 1048584

    REPORT_SES_SM_FE = 1048585

    REPORT_UAS_SM_FE = 1048586

    REPORT_BBE_SM_FE = 1048587

    REPORT_FC_SM_FE = 1048588

    REPORT_ESR_SM_FE = 1048589

    REPORT_SESR_SM_FE = 1048590

    REPORT_BBER_SM_FE = 1048591

    REPORT_ES_PM_FE = 2097160

    REPORT_SES_PM_FE = 2097161

    REPORT_UAS_PM_FE = 2097162

    REPORT_BBE_PM_FE = 2097163

    REPORT_FC_PM_FE = 2097164

    REPORT_ESR_PM_FE = 2097165

    REPORT_SESR_PM_FE = 2097166

    REPORT_BBER_PM_FE = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnReportEnum']


class OtnTcmReportEnum(Enum):
    """
    OtnTcmReportEnum

    Otn tcm report

    .. data:: REPORT_ES_TCM_FE = 16777224

    	PM Otn es TCM fe report

    .. data:: REPORT_SES_TCM_FE = 16777225

    	PM Otn ses TCM fe report

    .. data:: REPORT_UAS_TCM_FE = 16777226

    	PM Otn uas TCM fe report

    .. data:: REPORT_BBE_TCM_FE = 16777227

    	PM Otn bbe TCM fe report

    .. data:: REPORT_FC_TCM_FE = 16777228

    	PM Otn fc TCM fe report

    .. data:: REPORT_ESR_TCM_FE = 16777229

    	PM Otn esr TCM fe report

    .. data:: REPORT_SESR_TCM_FE = 16777230

    	PM Otn sesr TCM fe report

    .. data:: REPORT_BBER_TCM_FE = 16777231

    	PM Otn bber TCM fe report

    .. data:: REPORT_ES_TCM_NE = 33554432

    	PM Otn es TCM ne report

    .. data:: REPORT_SES_TCM_NE = 33554433

    	PM Otn ses TCM ne report

    .. data:: REPORT_UAS_TCM_NE = 33554434

    	PM Otn uas TCM ne report

    .. data:: REPORT_BBE_TCM_NE = 33554435

    	PM Otn bbe TCM ne report

    .. data:: REPORT_FC_TCM_NE = 33554436

    	PM Otn fc TCM ne report

    .. data:: REPORT_ESR_TCM_NE = 33554437

    	PM Otn esr TCM ne report

    .. data:: REPORT_SESR_TCM_NE = 33554438

    	PM Otn sesr TCM ne report

    .. data:: REPORT_BBER_TCM_NE = 33554439

    	PM Otn bber TCM ne report

    """

    REPORT_ES_TCM_FE = 16777224

    REPORT_SES_TCM_FE = 16777225

    REPORT_UAS_TCM_FE = 16777226

    REPORT_BBE_TCM_FE = 16777227

    REPORT_FC_TCM_FE = 16777228

    REPORT_ESR_TCM_FE = 16777229

    REPORT_SESR_TCM_FE = 16777230

    REPORT_BBER_TCM_FE = 16777231

    REPORT_ES_TCM_NE = 33554432

    REPORT_SES_TCM_NE = 33554433

    REPORT_UAS_TCM_NE = 33554434

    REPORT_BBE_TCM_NE = 33554435

    REPORT_FC_TCM_NE = 33554436

    REPORT_ESR_TCM_NE = 33554437

    REPORT_SESR_TCM_NE = 33554438

    REPORT_BBER_TCM_NE = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmReportEnum']


class OtnTcmThresholdEnum(Enum):
    """
    OtnTcmThresholdEnum

    Otn tcm threshold

    .. data:: THRESH_ES_TCM_FE = 16777224

    	PM Otn es TCM fe threshold

    .. data:: THRESH_SES_TCM_FE = 16777225

    	PM Otn ses TCM fe threshold

    .. data:: THRESH_UAS_TCM_FE = 16777226

    	PM Otn uas TCM fe threshold

    .. data:: THRESH_BBE_TCM_FE = 16777227

    	PM Otn bbe TCM fe threshold

    .. data:: THRESH_FC_TCM_FE = 16777228

    	PM Otn fc TCM fe threshold

    .. data:: THRESH_ESR_TCM_FE = 16777229

    	PM Otn esr TCM fe threshold

    .. data:: THRESH_SESR_TCM_FE = 16777230

    	PM Otn sesr TCM fe threshold

    .. data:: THRESH_BBER_TCM_FE = 16777231

    	PM Otn bber TCM fe threshold

    .. data:: THRESH_ES_TCM_NE = 33554432

    	PM Otn es TCM ne threshold

    .. data:: THRESH_SES_TCM_NE = 33554433

    	PM Otn ses TCM ne threshold

    .. data:: THRESH_UAS_TCM_NE = 33554434

    	PM Otn uas TCM ne threshold

    .. data:: THRESH_BBE_TCM_NE = 33554435

    	PM Otn bbe TCM ne threshold

    .. data:: THRESH_FC_TCM_NE = 33554436

    	PM Otn fc TCM ne threshold

    .. data:: THRESH_ESR_TCM_NE = 33554437

    	PM Otn esr TCM ne threshold

    .. data:: THRESH_SESR_TCM_NE = 33554438

    	PM Otn sesr TCM ne threshold

    .. data:: THRESH_BBER_TCM_NE = 33554439

    	PM Otn bber TCM ne threshold

    """

    THRESH_ES_TCM_FE = 16777224

    THRESH_SES_TCM_FE = 16777225

    THRESH_UAS_TCM_FE = 16777226

    THRESH_BBE_TCM_FE = 16777227

    THRESH_FC_TCM_FE = 16777228

    THRESH_ESR_TCM_FE = 16777229

    THRESH_SESR_TCM_FE = 16777230

    THRESH_BBER_TCM_FE = 16777231

    THRESH_ES_TCM_NE = 33554432

    THRESH_SES_TCM_NE = 33554433

    THRESH_UAS_TCM_NE = 33554434

    THRESH_BBE_TCM_NE = 33554435

    THRESH_FC_TCM_NE = 33554436

    THRESH_ESR_TCM_NE = 33554437

    THRESH_SESR_TCM_NE = 33554438

    THRESH_BBER_TCM_NE = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmThresholdEnum']


class OtnThresholdEnum(Enum):
    """
    OtnThresholdEnum

    Otn threshold

    .. data:: THRESH_ES_SM_NE = 262144

    	PM Otn es sm ne threshold

    .. data:: THRESH_SES_SM_NE = 262145

    	PM Otn ses sm ne threshold

    .. data:: THRESH_UAS_SM_NE = 262146

    	PM Otn uas sm ne threshold

    .. data:: THRESH_BBE_SM_NE = 262147

    	PM Otn bbe sm ne threshold

    .. data:: THRESH_FC_SM_NE = 262148

    	PM Otn fc sm ne threshold

    .. data:: THRESH_ESR_SM_NE = 262149

    	PM Otn esr sm ne threshold

    .. data:: THRESH_SESR_SM_NE = 262150

    	PM Otn sesr sm ne threshold

    .. data:: THRESH_BBER_SM_NE = 262151

    	PM Otn bber sm ne threshold

    .. data:: THRESH_ES_PM_NE = 524288

    	PM Otn es pm ne threshold

    .. data:: THRESH_SES_PM_NE = 524289

    	PM Otn ses pm ne threshold

    .. data:: THRESH_UAS_PM_NE = 524290

    	PM Otn uas pm ne threshold

    .. data:: THRESH_BBE_PM_NE = 524291

    	PM Otn bbe pm ne threshold

    .. data:: THRESH_FC_PM_NE = 524292

    	PM Otn fc pm ne threshold

    .. data:: THRESH_ESR_PM_NE = 524293

    	PM Otn esr pm ne threshold

    .. data:: THRESH_SESR_PM_NE = 524294

    	PM Otn sesr pm ne threshold

    .. data:: THRESH_BBER_PM_NE = 524295

    	PM Otn bber pm ne threshold

    .. data:: THRESH_ES_SM_FE = 1048584

    	PM Otn es sm fe threshold

    .. data:: THRESH_SES_SM_FE = 1048585

    	PM Otn ses sm fe threshold

    .. data:: THRESH_UAS_SM_FE = 1048586

    	PM Otn uas sm fe threshold

    .. data:: THRESH_BBE_SM_FE = 1048587

    	PM Otn bbe sm fe threshold

    .. data:: THRESH_FC_SM_FE = 1048588

    	PM Otn fc sm fe threshold

    .. data:: THRESH_ESR_SM_FE = 1048589

    	PM Otn esr sm fe threshold

    .. data:: THRESH_SESR_SM_FE = 1048590

    	PM Otn sesr sm fe threshold

    .. data:: THRESH_BBER_SM_FE = 1048591

    	PM Otn bber sm fe threshold

    .. data:: THRESH_ES_PM_FE = 2097160

    	PM Otn es pm fe threshold

    .. data:: THRESH_SES_PM_FE = 2097161

    	PM Otn ses pm fe threshold

    .. data:: THRESH_UAS_PM_FE = 2097162

    	PM Otn uas pm fe threshold

    .. data:: THRESH_BBE_PM_FE = 2097163

    	PM Otn bbe pm fe threshold

    .. data:: THRESH_FC_PM_FE = 2097164

    	PM Otn fc pm fe threshold

    .. data:: THRESH_ESR_PM_FE = 2097165

    	PM Otn esr pm fe threshold

    .. data:: THRESH_SESR_PM_FE = 2097166

    	PM Otn sesr pm fe threshold

    .. data:: THRESH_BBER_PM_FE = 2097167

    	PM Otn bber pm fe threshold

    """

    THRESH_ES_SM_NE = 262144

    THRESH_SES_SM_NE = 262145

    THRESH_UAS_SM_NE = 262146

    THRESH_BBE_SM_NE = 262147

    THRESH_FC_SM_NE = 262148

    THRESH_ESR_SM_NE = 262149

    THRESH_SESR_SM_NE = 262150

    THRESH_BBER_SM_NE = 262151

    THRESH_ES_PM_NE = 524288

    THRESH_SES_PM_NE = 524289

    THRESH_UAS_PM_NE = 524290

    THRESH_BBE_PM_NE = 524291

    THRESH_FC_PM_NE = 524292

    THRESH_ESR_PM_NE = 524293

    THRESH_SESR_PM_NE = 524294

    THRESH_BBER_PM_NE = 524295

    THRESH_ES_SM_FE = 1048584

    THRESH_SES_SM_FE = 1048585

    THRESH_UAS_SM_FE = 1048586

    THRESH_BBE_SM_FE = 1048587

    THRESH_FC_SM_FE = 1048588

    THRESH_ESR_SM_FE = 1048589

    THRESH_SESR_SM_FE = 1048590

    THRESH_BBER_SM_FE = 1048591

    THRESH_ES_PM_FE = 2097160

    THRESH_SES_PM_FE = 2097161

    THRESH_UAS_PM_FE = 2097162

    THRESH_BBE_PM_FE = 2097163

    THRESH_FC_PM_FE = 2097164

    THRESH_ESR_PM_FE = 2097165

    THRESH_SESR_PM_FE = 2097166

    THRESH_BBER_PM_FE = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnThresholdEnum']


class PathReportEnum(Enum):
    """
    PathReportEnum

    Path report

    .. data:: REPORT_CV = 5242880

    	PM CV threshold

    .. data:: REPORT_ES = 5242881

    	PM ES threshold

    .. data:: REPORT_SES = 5242882

    	PM SES threshold

    .. data:: REPORT_UAS = 5242883

    	PM UAS threshold

    """

    REPORT_CV = 5242880

    REPORT_ES = 5242881

    REPORT_SES = 5242882

    REPORT_UAS = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathReportEnum']


class PathThresholdEnum(Enum):
    """
    PathThresholdEnum

    Path threshold

    .. data:: THRESH_CV = 5242880

    	PM CV threshold

    .. data:: THRESH_ES = 5242881

    	PM ES threshold

    .. data:: THRESH_SES = 5242882

    	PM SES threshold

    .. data:: THRESH_UAS = 5242883

    	PM UAS threshold

    """

    THRESH_CV = 5242880

    THRESH_ES = 5242881

    THRESH_SES = 5242882

    THRESH_UAS = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathThresholdEnum']


class ReportEnum(Enum):
    """
    ReportEnum

    Report

    .. data:: FALSE = 0

    	Performance Monitoring Disabled

    .. data:: TRUE = 1

    	Performance Monitoring Enabled

    """

    FALSE = 0

    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['ReportEnum']


class StmReportEnum(Enum):
    """
    StmReportEnum

    Stm report

    .. data:: REPORT_EBS = 16777217

    	PM EBS REPORT

    .. data:: REPORT_ESS = 16777218

    	PM ESS REPORT

    .. data:: REPORT_ESRS = 16777219

    	PM ESRS REPORT

    .. data:: REPORT_SESS = 16777220

    	PM SES REPORT

    .. data:: REPORT_SESRS = 16777221

    	PM SESR REPORT

    .. data:: REPORT_BBES = 16777222

    	PM BBES REPORT

    .. data:: REPORT_BBESR = 16777223

    	PM BBESR REPORT

    .. data:: REPORT_UASS = 16777224

    	PM UASS REPORT

    .. data:: REPORT_EBL_NE = 16777225

    	PM EBLNE REPORT

    .. data:: REPORT_ESL_NE = 16777226

    	PM ESLNE REPORT

    .. data:: REPORT_ESLR_NE = 16777227

    	PM ESLRNE REPORT

    .. data:: REPORT_SESL_NE = 16777228

    	PM SESL REPORT

    .. data:: REPORT_SESRL_NE = 16777229

    	PM SESRL REPORT

    .. data:: REPORT_BBEL_NE = 16777230

    	PM BBELNE REPORT

    .. data:: REPORT_BBERL_NE = 16777231

    	PM BBERLNE REPORT

    .. data:: REPORT_UASL_NE = 16777232

    	PM UASNE REPORT

    .. data:: REPORT_EBL_FE = 16777245

    	PM EBFE REPORT

    .. data:: REPORT_ESL_FE = 16777246

    	PM ESFE REPORT

    .. data:: REPORT_ESRL_FE = 16777247

    	PM EBFE REPORT

    .. data:: REPORT_SESL_FE = 16777248

    	PM SESFE REPORT

    .. data:: REPORT_SESRL_FE = 16777249

    	PM SESRLFE REPORT

    .. data:: REPORT_BBEL_FE = 16777250

    	PM BBELFE REPORT

    .. data:: REPORT_BBERL_FE = 16777251

    	PM ESFE REPORT

    .. data:: REPORT_UASL_FE = 16777252

    	PM UASLFE REPORT

    """

    REPORT_EBS = 16777217

    REPORT_ESS = 16777218

    REPORT_ESRS = 16777219

    REPORT_SESS = 16777220

    REPORT_SESRS = 16777221

    REPORT_BBES = 16777222

    REPORT_BBESR = 16777223

    REPORT_UASS = 16777224

    REPORT_EBL_NE = 16777225

    REPORT_ESL_NE = 16777226

    REPORT_ESLR_NE = 16777227

    REPORT_SESL_NE = 16777228

    REPORT_SESRL_NE = 16777229

    REPORT_BBEL_NE = 16777230

    REPORT_BBERL_NE = 16777231

    REPORT_UASL_NE = 16777232

    REPORT_EBL_FE = 16777245

    REPORT_ESL_FE = 16777246

    REPORT_ESRL_FE = 16777247

    REPORT_SESL_FE = 16777248

    REPORT_SESRL_FE = 16777249

    REPORT_BBEL_FE = 16777250

    REPORT_BBERL_FE = 16777251

    REPORT_UASL_FE = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmReportEnum']


class StmThresholdEnum(Enum):
    """
    StmThresholdEnum

    Stm threshold

    .. data:: THRESH_EBS = 16777217

    	PM EBS threshold

    .. data:: THRESH_ESS = 16777218

    	PM ESS threshold

    .. data:: THRESH_ESRS = 16777219

    	PM ESRS threshold

    .. data:: THRESH_SESS = 16777220

    	PM SES threshold

    .. data:: THRESH_SESRS = 16777221

    	PM SESR threshold

    .. data:: THRESH_BBES = 16777222

    	PM BBES threshold

    .. data:: THRESH_BBESR = 16777223

    	PM BBESR threshold

    .. data:: THRESH_UASS = 16777224

    	PM UASS threshold

    .. data:: THRESH_EBL_NE = 16777225

    	PM EBLNE threshold

    .. data:: THRESH_ESL_NE = 16777226

    	PM ESLNE threshold

    .. data:: THRESH_ESLR_NE = 16777227

    	PM ESLRNE threshold

    .. data:: THRESH_SESL_NE = 16777228

    	PM SESL threshold

    .. data:: THRESH_SESRL_NE = 16777229

    	PM SESRL threshold

    .. data:: THRESH_BBEL_NE = 16777230

    	PM BBERLNE threshold

    .. data:: THRESH_BBERL_NE = 16777231

    	PM BBERLNE threshold

    .. data:: THRESH_UASL_NE = 16777232

    	PM UASNE threshold

    .. data:: THRESH_EBL_FE = 16777245

    	PM EBFE threshold

    .. data:: THRESH_ESL_FE = 16777246

    	PM ESFE threshold

    .. data:: THRESH_ESRL_FE = 16777247

    	PM EBFE threshold

    .. data:: THRESH_SESL_FE = 16777248

    	PM SESFE threshold

    .. data:: THRESH_SESRL_FE = 16777249

    	PM SESRLFE threshold

    .. data:: THRESH_BBEL_FE = 16777250

    	PM BBEL threshold

    .. data:: THRESH_BBERL_FE = 16777251

    	PM BBELFE threshold

    .. data:: THRESH_UASL_FE = 16777252

    	PM UASLFE threshold

    """

    THRESH_EBS = 16777217

    THRESH_ESS = 16777218

    THRESH_ESRS = 16777219

    THRESH_SESS = 16777220

    THRESH_SESRS = 16777221

    THRESH_BBES = 16777222

    THRESH_BBESR = 16777223

    THRESH_UASS = 16777224

    THRESH_EBL_NE = 16777225

    THRESH_ESL_NE = 16777226

    THRESH_ESLR_NE = 16777227

    THRESH_SESL_NE = 16777228

    THRESH_SESRL_NE = 16777229

    THRESH_BBEL_NE = 16777230

    THRESH_BBERL_NE = 16777231

    THRESH_UASL_NE = 16777232

    THRESH_EBL_FE = 16777245

    THRESH_ESL_FE = 16777246

    THRESH_ESRL_FE = 16777247

    THRESH_SESL_FE = 16777248

    THRESH_SESRL_FE = 16777249

    THRESH_BBEL_FE = 16777250

    THRESH_BBERL_FE = 16777251

    THRESH_UASL_FE = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmThresholdEnum']


class StsReportEnum(Enum):
    """
    StsReportEnum

    Sts report

    .. data:: REPORT_CV = 4194304

    	PM CV threshold

    .. data:: REPORT_ES = 4194305

    	PM ES threshold

    .. data:: REPORT_SES = 4194306

    	PM SES threshold

    .. data:: REPORT_UAS = 4194307

    	PM UAS threshold

    """

    REPORT_CV = 4194304

    REPORT_ES = 4194305

    REPORT_SES = 4194306

    REPORT_UAS = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsReportEnum']


class StsThresholdEnum(Enum):
    """
    StsThresholdEnum

    Sts threshold

    .. data:: THRESH_CV = 4194304

    	PM CV threshold

    .. data:: THRESH_ES = 4194305

    	PM ES threshold

    .. data:: THRESH_SES = 4194306

    	PM SES threshold

    .. data:: THRESH_UAS = 4194307

    	PM UAS threshold

    """

    THRESH_CV = 4194304

    THRESH_ES = 4194305

    THRESH_SES = 4194306

    THRESH_UAS = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsThresholdEnum']




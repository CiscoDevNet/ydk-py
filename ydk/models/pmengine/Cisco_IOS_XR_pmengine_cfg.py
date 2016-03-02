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



class EtherReport_Enum(Enum):
    """
    EtherReport_Enum

    Ether report

    """

    """

    PM Ether rx pkt report

    """
    REPORT_RX_PKT = 524290

    """

    PM ether stat pkt threshold

    """
    REPORT_STAT_PKT = 524291

    """

    PM Ether octet stat report

    """
    REPORT_OCTET_STAT = 524292

    """

    PM Ether oversize pkt report

    """
    REPORT_OVER_SIZE_PKT = 524293

    """

    PM Ether fcs error report

    """
    REPORT_FCS_ERR = 524294

    """

    PM Ether long frames report

    """
    REPORT_LONG_FRAME_S = 524295

    """

    PM Ether jabber stats report

    """
    REPORT_JABBER_STATS = 524296

    """

    PM Ether 64 octet report

    """
    REPORT_64_OCTET = 524297

    """

    PM Ether 65 to 127 octet report

    """
    REPORT_65_127_OCTET = 524298

    """

    PM Ether 128 to 255 octet report

    """
    REPORT_128_255_OCTET = 524299

    """

    PM Ether 256 to 511 octet report

    """
    REPORT_256_511_OCTET = 524300

    """

    PM Ether 512 to 1023 octet report

    """
    REPORT_512_1023_OCTET = 524301

    """

    PM Ether 1024 to 1518 report

    """
    REPORT_1024_1518_OCTET = 524302

    """

    PM Ether rx ucast report

    """
    REPORT_IN_UCAST = 524303

    """

    PM Ether rx mcast report

    """
    REPORT_IN_MCAST = 524304

    """

    PM Ether rx bcast report

    """
    REPORT_IN_BCAST = 524305

    """

    PM Ether tx ucast report

    """
    REPORT_OUT_UCAST = 524306

    """

    PM Ether tx mcast report

    """
    REPORT_OUT_MCAST = 524307

    """

    PM Ether tx bcast report

    """
    REPORT_OUT_BCAST = 524308

    """

    PM Ether tx pkt threshold

    """
    REPORT_TX_PKT = 524309

    """

    PM ether ifIn errors threshold

    """
    REPORT_IFIN_ERROR_S = 524310

    """

    PM ether ifInOctets threshold

    """
    REPORT_IFIN_OCTETS = 524311

    """

    PM ether stat multicast pkt threshold

    """
    REPORT_ETHER_STAT_MULTICAST_PKT = 524312

    """

    PM ether stat broadcast pkt threshold

    """
    REPORT_ETHER_STAT_BROADCAST_PKT = 524313

    """

    PM ether stat undersized pkt threshold

    """
    REPORT_ETHER_STAT_UNDER_SIZE_D_PKT = 524314

    """

    PM ether out octets threshold

    """
    REPORT_OUT_OCTET = 524315

    """

    PM ether in pause frame report

    """
    REPORT_IN_PAUSE_FRAME = 524316

    """

    PM in good bytes report

    """
    REPORT_IN_GO_OD_BYTES = 524317

    """

    PM in 802\_1 Q report

    """
    REPORT_IN_802_1Q_FRAME_S = 524318

    """

    PM in pkts 1519 max octets report

    """
    REPORT_IN_PKTS_1519_MAX_OCTETS = 524319

    """

    PM in good pkts report

    """
    REPORT_IN_GO_OD_PKTS = 524320

    """

    PM in drop overrun report

    """
    REPORT_IN_DROP_OVERRUN = 524321

    """

    PM in drop abort report

    """
    REPORT_IN_DROP_ABORT = 524322

    """

    PM in drop invalid vlan report

    """
    REPORT_IN_DROP_INVALID_VLAN = 524323

    """

    PM in drop invalid DMAC report

    """
    REPORT_IN_DROP_INVALID_DMAC = 524324

    """

    PM in drop invalid encap report

    """
    REPORT_IN_DROP_INVALID_ENCAP = 524325

    """

    PM in drop other report

    """
    REPORT_IN_DROP_OTHER = 524326

    """

    PM in MIB giant report

    """
    REPORT_IN_MIB_GIANT = 524327

    """

    PM in MIB jabber report

    """
    REPORT_IN_MIB_JABBER = 524328

    """

    PM in MIB CRC report

    """
    REPORT_IN_MIB_CRC = 524329

    """

    PM in error collisions report

    """
    REPORT_IN_ERROR_COLLISION_S = 524330

    """

    PM in error symbol report

    """
    REPORT_IN_ERROR_SYMBOL = 524331

    """

    PM out good bytes report

    """
    REPORT_OUT_GO_OD_BYTES = 524332

    """

    PM out 802\_1 Q report

    """
    REPORT_OUT_802_1Q_FRAME_S = 524333

    """

    PM out pause frame report

    """
    REPORT_OUT_PAUSE_FRAME_S = 524334

    """

    PM out pkts 1519 max octets report

    """
    REPORT_OUT_PKTS_1519_MAX_OCTETS = 524335

    """

    PM out good pkts report

    """
    REPORT_OUT_GO_OD_PKTS = 524336

    """

    PM out drop underrun report

    """
    REPORT_OUT_DROP_UNDER_RUN = 524337

    """

    PM out drop abort report

    """
    REPORT_OUT_DROP_ABORT = 524338

    """

    PM out drop other report

    """
    REPORT_OUT_DROP_OTHER = 524339

    """

    PM out error other report

    """
    REPORT_OUT_ERROR_OTHER = 524340

    """

    PM in error giant report

    """
    REPORT_IN_ERROR_GIANT = 524341

    """

    PM in error runt report

    """
    REPORT_IN_ERROR_RUNT = 524342

    """

    PM in error jabber report

    """
    REPORT_IN_ERROR_JABBERS = 524343

    """

    PM in error fragments report

    """
    REPORT_IN_ERROR_FRAGMENTS = 524344

    """

    PM in error other report

    """
    REPORT_IN_ERROR_OTHER = 524345

    """

    PM in pkt 64 octet report

    """
    REPORT_IN_PKT_64_OCTET = 524346

    """

    PM in pkts 65\_127 octets report

    """
    REPORT_IN_PKTS_65_127OCTETS = 524347

    """

    PM in pkts 128\_255 octets report

    """
    REPORT_IN_PKTS_128_255_OCTETS = 524348

    """

    PM in pkts 256\_511 octets report

    """
    REPORT_IN_PKTS_256_511_OCTETS = 524349

    """

    PM in pkts 512\_1023 octets report

    """
    REPORT_IN_PKTS_512_1023_OCTETS = 524350

    """

    PM in pkts 1024\_1058 octets report

    """
    REPORT_IN_PKTS_1024_1518_OCTETS = 524351

    """

    PM out pkt 64 octet report

    """
    REPORT_OUT_PKT_64_OCTET = 524352

    """

    PM out pkts 65\_127 octets report

    """
    REPORT_OUT_PKTS_65_127OCTETS = 524353

    """

    PM out pkts 128\_255 octets report

    """
    REPORT_OUT_PKTS_128_255_OCTETS = 524354

    """

    PM out pkts 256\_511 octets report

    """
    REPORT_OUT_PKTS_256_511_OCTETS = 524355

    """

    PM out pkts 512\_1023 octets report

    """
    REPORT_OUT_PKTS_512_1023_OCTETS = 524356

    """

    PM out pkts 1024\_1058 octets report

    """
    REPORT_OUT_PKTS_1024_1518_OCTETS = 524357


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherReport_Enum']


class EtherThreshold_Enum(Enum):
    """
    EtherThreshold_Enum

    Ether threshold

    """

    """

    PM Ether rx pkt threshold

    """
    THRESH_RX_PKT = 8388610

    """

    PM ether stat pkt threshold

    """
    THRESH_STAT_PKT = 8388611

    """

    PM Ether octet stat threshold

    """
    THRESH_OCTET_STAT = 8388612

    """

    PM Ether oversize pkt threshold

    """
    THRESH_OVER_SIZE_PKT = 8388613

    """

    PMEther fcs error threshold

    """
    THRESH_FCS_ERR = 8388614

    """

    PM Ether long frames threshold

    """
    THRESH_LONG_FRAME_S = 8388615

    """

    PM Ether jabber stats threshold

    """
    THRESH_JABBER_STATS = 8388616

    """

    PM Ether 64 octet threshold

    """
    THRESH_64_OCTET = 8388617

    """

    PM Ether 65 to 127 octet threshold

    """
    THRESH_65_127_OCTET = 8388618

    """

    PM Ether 128 to 255 octet threshold

    """
    THRESH_128_255_OCTET = 8388619

    """

    PM Ether 256 to 511 octet threshold

    """
    THRESH_256_511_OCTET = 8388620

    """

    PM Ether 512 to 1023 octet threshold

    """
    THRESH_512_1023_OCTET = 8388621

    """

    PM Ether 1024 to 1518 threshold

    """
    THRESH_1024_1518_OCTET = 8388622

    """

    PM Ether rx ucast threshold

    """
    THRESH_IN_UCAST = 8388623

    """

    PM Ether rx mcast threshold

    """
    THRESH_IN_MCAST = 8388624

    """

    PM Ether rx bcast threshold

    """
    THRESH_IN_BCAST = 8388625

    """

    PM Ether tx ucast threshold

    """
    THRESH_OUT_UCAST = 8388626

    """

    PM Ether tx mcast threshold

    """
    THRESH_OUT_MCAST = 8388627

    """

    PM Ether tx bcast threshold

    """
    THRESH_OUT_BCAST = 8388628

    """

    PM Ether tx pkt threshold

    """
    THRESH_TX_PKT = 8388629

    """

    PM ether ifIn errors threshold

    """
    THRESH_IFIN_ERROR_S = 8388630

    """

    PM ether ifInOctets threshold

    """
    THRESH_IFIN_OCTETS = 8388631

    """

    PM ether stat multicast pkt threshold

    """
    THRESH_ETHER_STAT_MULTICAST_PKT = 8388632

    """

    PM ether stat broadcast pkt threshold

    """
    THRESH_ETHER_STAT_BROADCAST_PKT = 8388633

    """

    PM ether stat undersized pkt threshold

    """
    THRESH_ETHER_STAT_UNDER_SIZE_D_PKT = 8388634

    """

    PM ether out octets threshold

    """
    THRESH_OUT_OCTET = 8388635

    """

    PM in pause frame threshold

    """
    THRESH_IN_PAUSE_FRAME = 8388636

    """

    PM in good bytes threshold

    """
    THRESH_IN_GO_OD_BYTES = 8388637

    """

    PM in 802\_1 Q threshold

    """
    THRESH_IN_802_1Q_FRAME_S = 8388638

    """

    PM in pkts 1519 max octets threshold

    """
    THRESH_IN_PKTS_1519_MAX_OCTETS = 8388639

    """

    PM in good pkts threshold

    """
    THRESH_IN_GO_OD_PKTS = 8388640

    """

    PM in drop overrun threshold

    """
    THRESH_IN_DROP_OVERRUN = 8388641

    """

    PM in drop abort threshold

    """
    THRESH_IN_DROP_ABORT = 8388642

    """

    PM in drop invalid vlan threshold

    """
    THRESH_IN_DROP_INVALID_VLAN = 8388643

    """

    PM in drop invalid DMAC threshold

    """
    THRESH_IN_DROP_INVALID_DMAC = 8388644

    """

    PM in drop invalid encap threshold

    """
    THRESH_IN_DROP_INVALID_ENCAP = 8388645

    """

    PM in drop other threshold

    """
    THRESH_IN_DROP_OTHER = 8388646

    """

    PM in MIB giant threshold

    """
    THRESH_IN_MIB_GIANT = 8388647

    """

    PM in MIB jabber threshold

    """
    THRESH_IN_MIB_JABBER = 8388648

    """

    PM in MIB CRC threshold

    """
    THRESH_IN_MIB_CRC = 8388649

    """

    PM in error collisions threshold

    """
    THRESH_IN_ERROR_COLLISION_S = 8388650

    """

    PM in error symbol threshold

    """
    THRESH_IN_ERROR_SYMBOL = 8388651

    """

    PM out good bytes threshold

    """
    THRESH_OUT_GO_OD_BYTES = 8388652

    """

    PM out 802\_1 Q threshold

    """
    THRESH_OUT_802_1Q_FRAME_S = 8388653

    """

    PM out pause frame threshold

    """
    THRESH_OUT_PAUSE_FRAME_S = 8388654

    """

    PM out pkts 1519 max octets threshold

    """
    THRESH_OUT_PKTS_1519_MAX_OCTETS = 8388655

    """

    PM out good pkts threshold

    """
    THRESH_OUT_GO_OD_PKTS = 8388656

    """

    PM out drop underrun threshold

    """
    THRESH_OUT_DROP_UNDER_RUN = 8388657

    """

    PM out drop abort threshold

    """
    THRESH_OUT_DROP_ABORT = 8388658

    """

    PM out drop other threshold

    """
    THRESH_OUT_DROP_OTHER = 8388659

    """

    PM out error other threshold

    """
    THRESH_OUT_ERROR_OTHER = 8388660

    """

    PM in error giant threshold

    """
    THRESH_IN_ERROR_GIANT = 8388661

    """

    PM in error runt threshold

    """
    THRESH_IN_ERROR_RUNT = 8388662

    """

    PM in error jabber threshold

    """
    THRESH_IN_ERROR_JABBERS = 8388663

    """

    PM in error fragments threshold

    """
    THRESH_IN_ERROR_FRAGMENTS = 8388664

    """

    PM in error other threshold

    """
    THRESH_IN_ERROR_OTHER = 8388665

    """

    PM in pkt 64 octet threshold

    """
    THRESH_IN_PKT_64_OCTET = 8388666

    """

    PM in pkts 65\_127 octets threshold

    """
    THRESH_IN_PKTS_65_127OCTETS = 8388667

    """

    PM in pkts 128\_255 octets threshold

    """
    THRESH_IN_PKTS_128_255_OCTETS = 8388668

    """

    PM in pkts 256\_511 octets threshold

    """
    THRESH_IN_PKTS_256_511_OCTETS = 8388669

    """

    PM in pkts 512\_1023 octets threshold

    """
    THRESH_IN_PKTS_512_1023_OCTETS = 8388670

    """

    PM in pkts 1024\_1058 octets threshold

    """
    THRESH_IN_PKTS_1024_1518_OCTETS = 8388671

    """

    PM out pkt 64 octet threshold

    """
    THRESH_OUT_PKT_64_OCTET = 8388672

    """

    PM out pkts 65\_127 octets threshold

    """
    THRESH_OUT_PKTS_65_127OCTETS = 8388673

    """

    PM out pkts 128\_255 octets threshold

    """
    THRESH_OUT_PKTS_128_255_OCTETS = 8388674

    """

    PM out pkts 256\_511 octets threshold

    """
    THRESH_OUT_PKTS_256_511_OCTETS = 8388675

    """

    PM out pkts 512\_1023 octets threshold

    """
    THRESH_OUT_PKTS_512_1023_OCTETS = 8388676

    """

    PM out pkts 1024\_1058 octets threshold

    """
    THRESH_OUT_PKTS_1024_1518_OCTETS = 8388677


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['EtherThreshold_Enum']


class FecReport_Enum(Enum):
    """
    FecReport_Enum

    Fec report

    """

    """

    PM Fec ec bits report

    """
    REPORT_EC_BITS = 131072

    """

    PM Fec uc words report

    """
    REPORT_UC_WORDS = 131076


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecReport_Enum']


class FecThreshold_Enum(Enum):
    """
    FecThreshold_Enum

    Fec threshold

    """

    """

    PM Fec ec bits threshold

    """
    THRESH_EC_BITS = 131072

    """

    PM Fec uc words threshold

    """
    THRESH_UC_WORDS = 131076


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['FecThreshold_Enum']


class GfpReport_Enum(Enum):
    """
    GfpReport_Enum

    Gfp report

    """

    """

    PM GFP rx bit err report

    """
    REPORT_RX_BIT_ERR = 6291456

    """

    PM GFP rx inv type report

    """
    REPORT_RX_INV_TYP = 6291457

    """

    PM GFP rx crc report

    """
    REPORT_RX_CRC = 6291458

    """

    PM GFP rx lfd report

    """
    REPORT_RX_LFD = 6291459

    """

    PM GFP rx csf report

    """
    REPORT_RX_CSF = 6291460


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpReport_Enum']


class GfpThreshold_Enum(Enum):
    """
    GfpThreshold_Enum

    Gfp threshold

    """

    """

    PM GFP rx bit err threshold

    """
    THRESH_RX_BIT_ERR = 67108864

    """

    PM GFP rx inv type threshold

    """
    THRESH_RX_INV_TYP = 67108865

    """

    PM GFP rx crc threshold

    """
    THRESH_RX_CRC = 67108866

    """

    PM GFP rx lfd threshold

    """
    THRESH_RX_LFD = 67108867

    """

    PM GFP rx csf threshold

    """
    THRESH_RX_CSF = 67108868


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['GfpThreshold_Enum']


class HoVcReport_Enum(Enum):
    """
    HoVcReport_Enum

    Ho vc report

    """

    """

    PM EB report

    """
    REPORT_EB = 33554432

    """

    PM ES report

    """
    REPORT_ES = 33554433

    """

    PM ESR report

    """
    REPORT_ESR = 33554434

    """

    PM SES report

    """
    REPORT_SES = 33554435

    """

    PM SESR report

    """
    REPORT_SESR = 33554436

    """

    PM BBE report

    """
    REPORT_BBE = 33554437

    """

    PM BBER report

    """
    REPORT_BBER = 33554438

    """

    PM UASS report

    """
    REPORT_UASS = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcReport_Enum']


class HoVcThreshold_Enum(Enum):
    """
    HoVcThreshold_Enum

    Ho vc threshold

    """

    """

    PM EB threshold

    """
    THRESH_EB = 33554432

    """

    PM ES threshold

    """
    THRESH_ES = 33554433

    """

    PM ESR threshold

    """
    THRESH_ESR = 33554434

    """

    PM SES threshold

    """
    THRESH_SES = 33554435

    """

    PM SESR threshold

    """
    THRESH_SESR = 33554436

    """

    PM BBE threshold

    """
    THRESH_BBE = 33554437

    """

    PM BBER threshold

    """
    THRESH_BBER = 33554438

    """

    PM UASS threshold

    """
    THRESH_UASS = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['HoVcThreshold_Enum']


class OcnReport_Enum(Enum):
    """
    OcnReport_Enum

    Ocn report

    """

    """

    PM SEFSS threshold

    """
    REPORT_SEFSS = 3145728

    """

    PM CVS threshold

    """
    REPORT_CVS = 3145729

    """

    PM ESS threshold

    """
    REPORT_ESS = 3145730

    """

    PM SESS threshold

    """
    REPORT_SESS = 3145731

    """

    PM CVL\-NE threshold

    """
    REPORT_CVL_NE = 3145734

    """

    PM ESL\-NE threshold

    """
    REPORT_ESL_NE = 3145735

    """

    PM SESL\-NE threshold

    """
    REPORT_SESL_NE = 3145736

    """

    PM UASL\-NE threshold

    """
    REPORT_UASL_NE = 3145738

    """

    PM FCL\-NE threshold

    """
    REPORT_FCL_NE = 3145739

    """

    PM FCL\_FE threshold

    """
    REPORT_FCL_FE = 3145751

    """

    PM CVL\-FE threshold

    """
    REPORT_CVL_FE = 3145752

    """

    PM ESL\_FE threshold

    """
    REPORT_ESL_FE = 3145753

    """

    PM SESL\_FE threshold

    """
    REPORT_SESL_FE = 3145754

    """

    PM UASL\_FEthreshold

    """
    REPORT_UASL_FE = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnReport_Enum']


class OcnThreshold_Enum(Enum):
    """
    OcnThreshold_Enum

    Ocn threshold

    """

    """

    PM SEFSS threshold

    """
    THRESH_SEFSS = 3145728

    """

    PM CVS threshold

    """
    THRESH_CVS = 3145729

    """

    PM ESS threshold

    """
    THRESH_ESS = 3145730

    """

    PM SESS threshold

    """
    THRESH_SESS = 3145731

    """

    PM CVL\-NE threshold

    """
    THRESH_CVL_NE = 3145734

    """

    PM ESL\-NE threshold

    """
    THRESH_ESL_NE = 3145735

    """

    PM SESL\-NE threshold

    """
    THRESH_SESL_NE = 3145736

    """

    PM UASL\-NE threshold

    """
    THRESH_UASL_NE = 3145738

    """

    PM FCL\-NE threshold

    """
    THRESH_FCL_NE = 3145739

    """

    PM FCL\_FE threshold

    """
    THRESH_FCL_FE = 3145751

    """

    PM CVL\-FE threshold

    """
    THRESH_CVL_FE = 3145752

    """

    PM ESL\_FE threshold

    """
    THRESH_ESL_FE = 3145753

    """

    PM SESL\_FE threshold

    """
    THRESH_SESL_FE = 3145754

    """

    PM UASL\_FEthreshold

    """
    THRESH_UASL_FE = 3145756


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OcnThreshold_Enum']


class OpticsReport_Enum(Enum):
    """
    OpticsReport_Enum

    Optics report

    """

    """

    PM Optics opt min report

    """
    REPORT_OPT_MIN = 65550

    """

    PM Optics opr min report

    """
    REPORT_OPR_MIN = 65551

    """

    PM Optics lbc min report

    """
    REPORT_LBC_MIN = 65552

    """

    PM Optics lbcpc min report

    """
    REPORT_LBC_PC_MIN = 65553

    """

    PM Optics cd min report

    """
    REPORT_CD_MIN = 65557

    """

    PM Optics dgd min report

    """
    REPORT_DGD_MIN = 65558

    """

    PM Optics sopmd min report

    """
    REPORT_PMD_MIN = 65559

    """

    PM Optics osnr min report

    """
    REPORT_OSNR_MIN = 65560

    """

    PM Optics pdl min report

    """
    REPORT_PDL_MIN = 65561

    """

    PM Optics pcr min report

    """
    REPORT_PCR_MIN = 65562

    """

    PM Optics pn min report

    """
    REPORT_PN_MIN = 65563

    """

    PM Optics opt max report

    """
    REPORT_OPT_MAX = 65564

    """

    PM Optics opr max report

    """
    REPORT_OPR_MAX = 65565

    """

    PM Optics lbc max report

    """
    REPORT_LBC_MAX = 65566

    """

    PM Optics lbcpc max report

    """
    REPORT_LBC_PC_MAX = 65567

    """

    PM Optics cd max report

    """
    REPORT_CD_MAX = 65571

    """

    PM Optics dgd max report

    """
    REPORT_DGD_MAX = 65572

    """

    PM Optics sopmd max report

    """
    REPORT_PMD_MAX = 65573

    """

    PM Optics osnr max report

    """
    REPORT_OSNR_MAX = 65574

    """

    PM Optics pdl max report

    """
    REPORT_PDL_MAX = 65575

    """

    PM Optics pcr max report

    """
    REPORT_PCR_MAX = 65576

    """

    PM Optics pn max report

    """
    REPORT_PN_MAX = 65577


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsReport_Enum']


class OpticsThreshold_Enum(Enum):
    """
    OpticsThreshold_Enum

    Optics threshold

    """

    """

    PM Optics opt min threshold

    """
    THRESH_OPT_MIN = 65550

    """

    PM Optics opr min threshold

    """
    THRESH_OPR_MIN = 65551

    """

    PM Optics lbc min threshold

    """
    THRESH_LBC_MIN = 65552

    """

    PM Optics lbcpc min threshold

    """
    THRESH_LBC_PC_MIN = 65553

    """

    PM Optics cd min threshold

    """
    THRESH_CD_MIN = 65557

    """

    PM Optics dgd min threshold

    """
    THRESH_DGD_MIN = 65558

    """

    PM Optics sopmd min threshold

    """
    THRESH_PMD_MIN = 65559

    """

    PM Optics osnr min threshold

    """
    THRESH_OSNR_MIN = 65560

    """

    PM Optics pdl min threshold

    """
    THRESH_PDL_MIN = 65561

    """

    PM Optics pcr min threshold

    """
    THRESH_PCR_MIN = 65562

    """

    PM Optics pn min threshold

    """
    THRESH_PN_MIN = 65563

    """

    PM Optics opt max threshold

    """
    THRESH_OPT_MAX = 65564

    """

    PM Optics opr max threshold

    """
    THRESH_OPR_MAX = 65565

    """

    PM Optics lbc max threshold

    """
    THRESH_LBC_MAX = 65566

    """

    PM Optics lbcpc max threshold

    """
    THRESH_LBC_PC_MAX = 65567

    """

    PM Optics cd max threshold

    """
    THRESH_CD_MAX = 65571

    """

    PM Optics dgd max threshold

    """
    THRESH_DGD_MAX = 65572

    """

    PM Optics sopmd max threshold

    """
    THRESH_PMD_MAX = 65573

    """

    PM Optics osnr max threshold

    """
    THRESH_OSNR_MAX = 65574

    """

    PM Optics pdl max threshold

    """
    THRESH_PDL_MAX = 65575

    """

    PM Optics pcr max threshold

    """
    THRESH_PCR_MAX = 65576

    """

    PM Optics pn max threshold

    """
    THRESH_PN_MAX = 65577


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OpticsThreshold_Enum']


class OtnReport_Enum(Enum):
    """
    OtnReport_Enum

    Otn report

    """

    """

    PM Otn es sm ne report

    """
    REPORT_ES_SM_NE = 262144

    """

    PM Otn ses sm ne report

    """
    REPORT_SES_SM_NE = 262145

    """

    PM Otn uas sm ne report

    """
    REPORT_UAS_SM_NE = 262146

    """

    PM Otn bbe sm ne report

    """
    REPORT_BBE_SM_NE = 262147

    """

    PM Otn fc sm ne report

    """
    REPORT_FC_SM_NE = 262148

    """

    PM Otn esr sm ne report

    """
    REPORT_ESR_SM_NE = 262149

    """

    PM Otn sesr sm ne report

    """
    REPORT_SESR_SM_NE = 262150

    """

    PM Otn bber sm ne report

    """
    REPORT_BBER_SM_NE = 262151

    """

    PM Otn es pm ne report

    """
    REPORT_ES_PM_NE = 524288

    """

    PM Otn ses pm ne report

    """
    REPORT_SES_PM_NE = 524289

    """

    PM Otn uas pm ne report

    """
    REPORT_UAS_PM_NE = 524290

    """

    PM Otn bbe pm ne report

    """
    REPORT_BBE_PM_NE = 524291

    """

    PM Otn fc pm ne report

    """
    REPORT_FC_PM_NE = 524292

    """

    PM Otn esr pm ne report

    """
    REPORT_ESR_PM_NE = 524293

    """

    PM Otn sesr pm ne report

    """
    REPORT_SESR_PM_NE = 524294

    """

    PM Otn bber pm ne report

    """
    REPORT_BBER_PM_NE = 524295

    """

    PM Otn es sm fe report

    """
    REPORT_ES_SM_FE = 1048584

    """

    PM Otn ses sm fe report

    """
    REPORT_SES_SM_FE = 1048585

    """

    PM Otn uas sm fe report

    """
    REPORT_UAS_SM_FE = 1048586

    """

    PM Otn bbe sm fe report

    """
    REPORT_BBE_SM_FE = 1048587

    """

    PM Otn fc sm fe report

    """
    REPORT_FC_SM_FE = 1048588

    """

    PM Otn esr sm fe report

    """
    REPORT_ESR_SM_FE = 1048589

    """

    PM Otn sesr sm fe report

    """
    REPORT_SESR_SM_FE = 1048590

    """

    PM Otn bber sm fe report

    """
    REPORT_BBER_SM_FE = 1048591

    """

    PM Otn es pm fe report

    """
    REPORT_ES_PM_FE = 2097160

    """

    PM Otn ses pm fe report

    """
    REPORT_SES_PM_FE = 2097161

    """

    PM Otn uas pm fe report

    """
    REPORT_UAS_PM_FE = 2097162

    """

    PM Otn bbe pm fe report

    """
    REPORT_BBE_PM_FE = 2097163

    """

    PM Otn fc pm fe report

    """
    REPORT_FC_PM_FE = 2097164

    """

    PM Otn esr pm fe report

    """
    REPORT_ESR_PM_FE = 2097165

    """

    PM Otn sesr pm fe report

    """
    REPORT_SESR_PM_FE = 2097166

    """

    PM Otn bber pm fe report

    """
    REPORT_BBER_PM_FE = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnReport_Enum']


class OtnTcmReport_Enum(Enum):
    """
    OtnTcmReport_Enum

    Otn tcm report

    """

    """

    PM Otn es TCM fe report

    """
    REPORT_ES_TCM_FE = 16777224

    """

    PM Otn ses TCM fe report

    """
    REPORT_SES_TCM_FE = 16777225

    """

    PM Otn uas TCM fe report

    """
    REPORT_UAS_TCM_FE = 16777226

    """

    PM Otn bbe TCM fe report

    """
    REPORT_BBE_TCM_FE = 16777227

    """

    PM Otn fc TCM fe report

    """
    REPORT_FC_TCM_FE = 16777228

    """

    PM Otn esr TCM fe report

    """
    REPORT_ESR_TCM_FE = 16777229

    """

    PM Otn sesr TCM fe report

    """
    REPORT_SESR_TCM_FE = 16777230

    """

    PM Otn bber TCM fe report

    """
    REPORT_BBER_TCM_FE = 16777231

    """

    PM Otn es TCM ne report

    """
    REPORT_ES_TCM_NE = 33554432

    """

    PM Otn ses TCM ne report

    """
    REPORT_SES_TCM_NE = 33554433

    """

    PM Otn uas TCM ne report

    """
    REPORT_UAS_TCM_NE = 33554434

    """

    PM Otn bbe TCM ne report

    """
    REPORT_BBE_TCM_NE = 33554435

    """

    PM Otn fc TCM ne report

    """
    REPORT_FC_TCM_NE = 33554436

    """

    PM Otn esr TCM ne report

    """
    REPORT_ESR_TCM_NE = 33554437

    """

    PM Otn sesr TCM ne report

    """
    REPORT_SESR_TCM_NE = 33554438

    """

    PM Otn bber TCM ne report

    """
    REPORT_BBER_TCM_NE = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmReport_Enum']


class OtnTcmThreshold_Enum(Enum):
    """
    OtnTcmThreshold_Enum

    Otn tcm threshold

    """

    """

    PM Otn es TCM fe threshold

    """
    THRESH_ES_TCM_FE = 16777224

    """

    PM Otn ses TCM fe threshold

    """
    THRESH_SES_TCM_FE = 16777225

    """

    PM Otn uas TCM fe threshold

    """
    THRESH_UAS_TCM_FE = 16777226

    """

    PM Otn bbe TCM fe threshold

    """
    THRESH_BBE_TCM_FE = 16777227

    """

    PM Otn fc TCM fe threshold

    """
    THRESH_FC_TCM_FE = 16777228

    """

    PM Otn esr TCM fe threshold

    """
    THRESH_ESR_TCM_FE = 16777229

    """

    PM Otn sesr TCM fe threshold

    """
    THRESH_SESR_TCM_FE = 16777230

    """

    PM Otn bber TCM fe threshold

    """
    THRESH_BBER_TCM_FE = 16777231

    """

    PM Otn es TCM ne threshold

    """
    THRESH_ES_TCM_NE = 33554432

    """

    PM Otn ses TCM ne threshold

    """
    THRESH_SES_TCM_NE = 33554433

    """

    PM Otn uas TCM ne threshold

    """
    THRESH_UAS_TCM_NE = 33554434

    """

    PM Otn bbe TCM ne threshold

    """
    THRESH_BBE_TCM_NE = 33554435

    """

    PM Otn fc TCM ne threshold

    """
    THRESH_FC_TCM_NE = 33554436

    """

    PM Otn esr TCM ne threshold

    """
    THRESH_ESR_TCM_NE = 33554437

    """

    PM Otn sesr TCM ne threshold

    """
    THRESH_SESR_TCM_NE = 33554438

    """

    PM Otn bber TCM ne threshold

    """
    THRESH_BBER_TCM_NE = 33554439


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnTcmThreshold_Enum']


class OtnThreshold_Enum(Enum):
    """
    OtnThreshold_Enum

    Otn threshold

    """

    """

    PM Otn es sm ne threshold

    """
    THRESH_ES_SM_NE = 262144

    """

    PM Otn ses sm ne threshold

    """
    THRESH_SES_SM_NE = 262145

    """

    PM Otn uas sm ne threshold

    """
    THRESH_UAS_SM_NE = 262146

    """

    PM Otn bbe sm ne threshold

    """
    THRESH_BBE_SM_NE = 262147

    """

    PM Otn fc sm ne threshold

    """
    THRESH_FC_SM_NE = 262148

    """

    PM Otn esr sm ne threshold

    """
    THRESH_ESR_SM_NE = 262149

    """

    PM Otn sesr sm ne threshold

    """
    THRESH_SESR_SM_NE = 262150

    """

    PM Otn bber sm ne threshold

    """
    THRESH_BBER_SM_NE = 262151

    """

    PM Otn es pm ne threshold

    """
    THRESH_ES_PM_NE = 524288

    """

    PM Otn ses pm ne threshold

    """
    THRESH_SES_PM_NE = 524289

    """

    PM Otn uas pm ne threshold

    """
    THRESH_UAS_PM_NE = 524290

    """

    PM Otn bbe pm ne threshold

    """
    THRESH_BBE_PM_NE = 524291

    """

    PM Otn fc pm ne threshold

    """
    THRESH_FC_PM_NE = 524292

    """

    PM Otn esr pm ne threshold

    """
    THRESH_ESR_PM_NE = 524293

    """

    PM Otn sesr pm ne threshold

    """
    THRESH_SESR_PM_NE = 524294

    """

    PM Otn bber pm ne threshold

    """
    THRESH_BBER_PM_NE = 524295

    """

    PM Otn es sm fe threshold

    """
    THRESH_ES_SM_FE = 1048584

    """

    PM Otn ses sm fe threshold

    """
    THRESH_SES_SM_FE = 1048585

    """

    PM Otn uas sm fe threshold

    """
    THRESH_UAS_SM_FE = 1048586

    """

    PM Otn bbe sm fe threshold

    """
    THRESH_BBE_SM_FE = 1048587

    """

    PM Otn fc sm fe threshold

    """
    THRESH_FC_SM_FE = 1048588

    """

    PM Otn esr sm fe threshold

    """
    THRESH_ESR_SM_FE = 1048589

    """

    PM Otn sesr sm fe threshold

    """
    THRESH_SESR_SM_FE = 1048590

    """

    PM Otn bber sm fe threshold

    """
    THRESH_BBER_SM_FE = 1048591

    """

    PM Otn es pm fe threshold

    """
    THRESH_ES_PM_FE = 2097160

    """

    PM Otn ses pm fe threshold

    """
    THRESH_SES_PM_FE = 2097161

    """

    PM Otn uas pm fe threshold

    """
    THRESH_UAS_PM_FE = 2097162

    """

    PM Otn bbe pm fe threshold

    """
    THRESH_BBE_PM_FE = 2097163

    """

    PM Otn fc pm fe threshold

    """
    THRESH_FC_PM_FE = 2097164

    """

    PM Otn esr pm fe threshold

    """
    THRESH_ESR_PM_FE = 2097165

    """

    PM Otn sesr pm fe threshold

    """
    THRESH_SESR_PM_FE = 2097166

    """

    PM Otn bber pm fe threshold

    """
    THRESH_BBER_PM_FE = 2097167


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['OtnThreshold_Enum']


class PathReport_Enum(Enum):
    """
    PathReport_Enum

    Path report

    """

    """

    PM CV threshold

    """
    REPORT_CV = 5242880

    """

    PM ES threshold

    """
    REPORT_ES = 5242881

    """

    PM SES threshold

    """
    REPORT_SES = 5242882

    """

    PM UAS threshold

    """
    REPORT_UAS = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathReport_Enum']


class PathThreshold_Enum(Enum):
    """
    PathThreshold_Enum

    Path threshold

    """

    """

    PM CV threshold

    """
    THRESH_CV = 5242880

    """

    PM ES threshold

    """
    THRESH_ES = 5242881

    """

    PM SES threshold

    """
    THRESH_SES = 5242882

    """

    PM UAS threshold

    """
    THRESH_UAS = 5242883


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['PathThreshold_Enum']


class Report_Enum(Enum):
    """
    Report_Enum

    Report

    """

    """

    Performance Monitoring Disabled

    """
    FALSE = 0

    """

    Performance Monitoring Enabled

    """
    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['Report_Enum']


class StmReport_Enum(Enum):
    """
    StmReport_Enum

    Stm report

    """

    """

    PM EBS REPORT

    """
    REPORT_EBS = 16777217

    """

    PM ESS REPORT

    """
    REPORT_ESS = 16777218

    """

    PM ESRS REPORT

    """
    REPORT_ESRS = 16777219

    """

    PM SES REPORT

    """
    REPORT_SESS = 16777220

    """

    PM SESR REPORT

    """
    REPORT_SESRS = 16777221

    """

    PM BBES REPORT

    """
    REPORT_BBES = 16777222

    """

    PM BBESR REPORT

    """
    REPORT_BBESR = 16777223

    """

    PM UASS REPORT

    """
    REPORT_UASS = 16777224

    """

    PM EBLNE REPORT

    """
    REPORT_EBL_NE = 16777225

    """

    PM ESLNE REPORT

    """
    REPORT_ESL_NE = 16777226

    """

    PM ESLRNE REPORT

    """
    REPORT_ESLR_NE = 16777227

    """

    PM SESL REPORT

    """
    REPORT_SESL_NE = 16777228

    """

    PM SESRL REPORT

    """
    REPORT_SESRL_NE = 16777229

    """

    PM BBELNE REPORT

    """
    REPORT_BBEL_NE = 16777230

    """

    PM BBERLNE REPORT

    """
    REPORT_BBERL_NE = 16777231

    """

    PM UASNE REPORT

    """
    REPORT_UASL_NE = 16777232

    """

    PM EBFE REPORT

    """
    REPORT_EBL_FE = 16777245

    """

    PM ESFE REPORT

    """
    REPORT_ESL_FE = 16777246

    """

    PM EBFE REPORT

    """
    REPORT_ESRL_FE = 16777247

    """

    PM SESFE REPORT

    """
    REPORT_SESL_FE = 16777248

    """

    PM SESRLFE REPORT

    """
    REPORT_SESRL_FE = 16777249

    """

    PM BBELFE REPORT

    """
    REPORT_BBEL_FE = 16777250

    """

    PM ESFE REPORT

    """
    REPORT_BBERL_FE = 16777251

    """

    PM UASLFE REPORT

    """
    REPORT_UASL_FE = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmReport_Enum']


class StmThreshold_Enum(Enum):
    """
    StmThreshold_Enum

    Stm threshold

    """

    """

    PM EBS threshold

    """
    THRESH_EBS = 16777217

    """

    PM ESS threshold

    """
    THRESH_ESS = 16777218

    """

    PM ESRS threshold

    """
    THRESH_ESRS = 16777219

    """

    PM SES threshold

    """
    THRESH_SESS = 16777220

    """

    PM SESR threshold

    """
    THRESH_SESRS = 16777221

    """

    PM BBES threshold

    """
    THRESH_BBES = 16777222

    """

    PM BBESR threshold

    """
    THRESH_BBESR = 16777223

    """

    PM UASS threshold

    """
    THRESH_UASS = 16777224

    """

    PM EBLNE threshold

    """
    THRESH_EBL_NE = 16777225

    """

    PM ESLNE threshold

    """
    THRESH_ESL_NE = 16777226

    """

    PM ESLRNE threshold

    """
    THRESH_ESLR_NE = 16777227

    """

    PM SESL threshold

    """
    THRESH_SESL_NE = 16777228

    """

    PM SESRL threshold

    """
    THRESH_SESRL_NE = 16777229

    """

    PM BBERLNE threshold

    """
    THRESH_BBEL_NE = 16777230

    """

    PM BBERLNE threshold

    """
    THRESH_BBERL_NE = 16777231

    """

    PM UASNE threshold

    """
    THRESH_UASL_NE = 16777232

    """

    PM EBFE threshold

    """
    THRESH_EBL_FE = 16777245

    """

    PM ESFE threshold

    """
    THRESH_ESL_FE = 16777246

    """

    PM EBFE threshold

    """
    THRESH_ESRL_FE = 16777247

    """

    PM SESFE threshold

    """
    THRESH_SESL_FE = 16777248

    """

    PM SESRLFE threshold

    """
    THRESH_SESRL_FE = 16777249

    """

    PM BBEL threshold

    """
    THRESH_BBEL_FE = 16777250

    """

    PM BBELFE threshold

    """
    THRESH_BBERL_FE = 16777251

    """

    PM UASLFE threshold

    """
    THRESH_UASL_FE = 16777252


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StmThreshold_Enum']


class StsReport_Enum(Enum):
    """
    StsReport_Enum

    Sts report

    """

    """

    PM CV threshold

    """
    REPORT_CV = 4194304

    """

    PM ES threshold

    """
    REPORT_ES = 4194305

    """

    PM SES threshold

    """
    REPORT_SES = 4194306

    """

    PM UAS threshold

    """
    REPORT_UAS = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsReport_Enum']


class StsThreshold_Enum(Enum):
    """
    StsThreshold_Enum

    Sts threshold

    """

    """

    PM CV threshold

    """
    THRESH_CV = 4194304

    """

    PM ES threshold

    """
    THRESH_ES = 4194305

    """

    PM SES threshold

    """
    THRESH_SES = 4194306

    """

    PM UAS threshold

    """
    THRESH_UAS = 4194307


    @staticmethod
    def _meta_info():
        from ydk.models.pmengine._meta import _Cisco_IOS_XR_pmengine_cfg as meta
        return meta._meta_table['StsThreshold_Enum']




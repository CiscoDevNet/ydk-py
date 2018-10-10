""" Cisco_IOS_XR_freqsync_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsyncClock(Enum):
    """
    FsyncClock (Enum Class)

    Fsync clock

    .. data:: sync = 3

    	Synchronous clock

    .. data:: internal = 4

    	Internal clock

    .. data:: gnss = 8

    	GNSS receiver

    """

    sync = Enum.YLeaf(3, "sync")

    internal = Enum.YLeaf(4, "internal")

    gnss = Enum.YLeaf(8, "gnss")


class FsyncQlOption(Enum):
    """
    FsyncQlOption (Enum Class)

    Fsync ql option

    .. data:: option_1 = 1

    	ITU-T Option 1

    .. data:: option_2__COMMA___generation_1 = 2

    	ITU-T Option 2, Generation 1

    .. data:: option_2__COMMA___generation_2 = 3

    	ITU-T Option 2, Generation 2

    """

    option_1 = Enum.YLeaf(1, "option-1")

    option_2__COMMA___generation_1 = Enum.YLeaf(2, "option-2,-generation-1")

    option_2__COMMA___generation_2 = Enum.YLeaf(3, "option-2,-generation-2")


class FsyncQlValue(Enum):
    """
    FsyncQlValue (Enum Class)

    Fsync ql value

    .. data:: dnu = 1

    	This signal should not be used for

    	synchronization

    .. data:: o1_prc = 10

    	ITU-T Option 1: Primary reference clock

    .. data:: o1_ssu_a = 11

    	ITU-T Option 1: Type I or V slave clock

    .. data:: o1_ssu_b = 12

    	ITU-T Option 1: Type IV slave clock

    .. data:: o1_sec = 13

    	ITU-T Option 1: SONET equipment clock

    .. data:: o2_g1_prs = 20

    	ITU-T Option 2, Generation 1: Primary reference

    	source

    .. data:: o2_g1_stu = 21

    	ITU-T Option 2, Generation 1: Synchronized -

    	traceability unknown

    .. data:: o2_g1_st2 = 22

    	ITU-T Option 2, Generation 1: Stratum 2

    .. data:: o2_g1_st3 = 23

    	ITU-T Option 2, Generation 1: Stratum 3

    .. data:: o2_g1_smc = 24

    	ITU-T Option 2, Generation 1: SONET clock self

    	timed

    .. data:: o2_g1_st4 = 25

    	ITU-T Option 2, Generation 1: Stratum 4 freerun

    .. data:: o2_g2_prs = 30

    	ITU-T Option 2, Generation 2: Primary reference

    	source

    .. data:: o2_g2_stu = 31

    	ITU-T Option 2, Generation 2: Synchronized -

    	traceability unknown

    .. data:: o2_g2_st2 = 32

    	ITU-T Option 2, Generation 2: Stratum 2

    .. data:: o2_g2_st3 = 33

    	ITU-T Option 2, Generation 2: Stratum 3

    .. data:: o2_g2_tnc = 34

    	ITU-T Option 2, Generation 2: Transit node

    	clock

    .. data:: o2_g2_st3e = 35

    	ITU-T Option 2, Generation 2: Stratum 3E

    .. data:: o2_g2_smc = 36

    	ITU-T Option 2, Generation 2: SONET clock self

    	timed

    .. data:: o2_g2_st4 = 37

    	ITU-T Option 2, Generation 2: Stratum 4 freerun

    """

    dnu = Enum.YLeaf(1, "dnu")

    o1_prc = Enum.YLeaf(10, "o1-prc")

    o1_ssu_a = Enum.YLeaf(11, "o1-ssu-a")

    o1_ssu_b = Enum.YLeaf(12, "o1-ssu-b")

    o1_sec = Enum.YLeaf(13, "o1-sec")

    o2_g1_prs = Enum.YLeaf(20, "o2-g1-prs")

    o2_g1_stu = Enum.YLeaf(21, "o2-g1-stu")

    o2_g1_st2 = Enum.YLeaf(22, "o2-g1-st2")

    o2_g1_st3 = Enum.YLeaf(23, "o2-g1-st3")

    o2_g1_smc = Enum.YLeaf(24, "o2-g1-smc")

    o2_g1_st4 = Enum.YLeaf(25, "o2-g1-st4")

    o2_g2_prs = Enum.YLeaf(30, "o2-g2-prs")

    o2_g2_stu = Enum.YLeaf(31, "o2-g2-stu")

    o2_g2_st2 = Enum.YLeaf(32, "o2-g2-st2")

    o2_g2_st3 = Enum.YLeaf(33, "o2-g2-st3")

    o2_g2_tnc = Enum.YLeaf(34, "o2-g2-tnc")

    o2_g2_st3e = Enum.YLeaf(35, "o2-g2-st3e")

    o2_g2_smc = Enum.YLeaf(36, "o2-g2-smc")

    o2_g2_st4 = Enum.YLeaf(37, "o2-g2-st4")


class Gnss1ppsPolarity(Enum):
    """
    Gnss1ppsPolarity (Enum Class)

    Gnss1pps polarity

    .. data:: positive = 0

    	Positive 1PPS polarity

    .. data:: negative = 1

    	Negative 1PPS polarity

    """

    positive = Enum.YLeaf(0, "positive")

    negative = Enum.YLeaf(1, "negative")


class GnssConstellation(Enum):
    """
    GnssConstellation (Enum Class)

    Gnss constellation

    .. data:: auto = 0

    	Unicast communication

    .. data:: gps = 1

    	GPS constellation

    .. data:: galileo = 2

    	Galileo constellation

    .. data:: bei_dou = 3

    	BeiDou constellation

    .. data:: qzss = 4

    	QZSS constellation

    .. data:: glonass = 5

    	GLONASS constellation

    .. data:: sbas = 6

    	SBAS constellation

    .. data:: irnss = 7

    	IRNSS constellation

    """

    auto = Enum.YLeaf(0, "auto")

    gps = Enum.YLeaf(1, "gps")

    galileo = Enum.YLeaf(2, "galileo")

    bei_dou = Enum.YLeaf(3, "bei-dou")

    qzss = Enum.YLeaf(4, "qzss")

    glonass = Enum.YLeaf(5, "glonass")

    sbas = Enum.YLeaf(6, "sbas")

    irnss = Enum.YLeaf(7, "irnss")




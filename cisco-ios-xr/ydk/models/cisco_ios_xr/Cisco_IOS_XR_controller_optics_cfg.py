""" Cisco_IOS_XR_controller_optics_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package configuration.

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



class OpticsDwdmCarrierGrid(Enum):
    """
    OpticsDwdmCarrierGrid (Enum Class)

    Optics dwdm carrier grid

    .. data:: Y_50g_hz_grid = 0

    	50GHz Grid

    .. data:: Y_100mhz_grid = 1

    	100MHz Grid

    """

    Y_50g_hz_grid = Enum.YLeaf(0, "50g-hz-grid")

    Y_100mhz_grid = Enum.YLeaf(1, "100mhz-grid")


class OpticsDwdmCarrierParam(Enum):
    """
    OpticsDwdmCarrierParam (Enum Class)

    Optics dwdm carrier param

    .. data:: itu_ch = 0

    	ITU Wave Channel Number

    .. data:: wavelength = 1

    	Wavelength in nm

    .. data:: frequency = 2

    	Frequency in Hertz

    """

    itu_ch = Enum.YLeaf(0, "itu-ch")

    wavelength = Enum.YLeaf(1, "wavelength")

    frequency = Enum.YLeaf(2, "frequency")


class OpticsFec(Enum):
    """
    OpticsFec (Enum Class)

    Optics fec

    .. data:: fec_none = 0

    	No Fec

    .. data:: fec_h15 = 1

    	Enhanced H15

    .. data:: fec_h25 = 2

    	Enhanced H25

    .. data:: fec_h15_de = 4

    	Enhanced H15 DE

    .. data:: fec_h25_de = 8

    	Enhanced H25 DE

    """

    fec_none = Enum.YLeaf(0, "fec-none")

    fec_h15 = Enum.YLeaf(1, "fec-h15")

    fec_h25 = Enum.YLeaf(2, "fec-h25")

    fec_h15_de = Enum.YLeaf(4, "fec-h15-de")

    fec_h25_de = Enum.YLeaf(8, "fec-h25-de")


class OpticsLoopback(Enum):
    """
    OpticsLoopback (Enum Class)

    Optics loopback

    .. data:: none = 0

    	No Loopback

    .. data:: internal = 1

    	Internal Loopback

    .. data:: line = 2

    	Line Loopback

    """

    none = Enum.YLeaf(0, "none")

    internal = Enum.YLeaf(1, "internal")

    line = Enum.YLeaf(2, "line")


class OpticsOtsAmpliControlMode(Enum):
    """
    OpticsOtsAmpliControlMode (Enum Class)

    Optics ots ampli control mode

    .. data:: automatic = 1

    	Automatic Amplifier Mode

    .. data:: manual = 2

    	Manual Amplifier Mode

    """

    automatic = Enum.YLeaf(1, "automatic")

    manual = Enum.YLeaf(2, "manual")


class OpticsOtsAmpliGainRange(Enum):
    """
    OpticsOtsAmpliGainRange (Enum Class)

    Optics ots ampli gain range

    .. data:: normal = 1

    	Normal Amplifier Gain Range

    .. data:: extended = 2

    	Extended Amplifier Gain Range

    """

    normal = Enum.YLeaf(1, "normal")

    extended = Enum.YLeaf(2, "extended")


class OpticsOtsSafetyControlMode(Enum):
    """
    OpticsOtsSafetyControlMode (Enum Class)

    Optics ots safety control mode

    .. data:: auto = 1

    	Automatic Safety Control Mode

    .. data:: disabled = 2

    	Disable Safety Control Mode

    """

    auto = Enum.YLeaf(1, "auto")

    disabled = Enum.YLeaf(2, "disabled")


class Threshold(Enum):
    """
    Threshold (Enum Class)

    Threshold

    .. data:: low = 1

    	Low Threshold

    .. data:: high = 2

    	High Threshold

    """

    low = Enum.YLeaf(1, "low")

    high = Enum.YLeaf(2, "high")




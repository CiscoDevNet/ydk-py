""" ietf_transport_types 

This module defines transport types.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class TributarySlotGranularityIdentity(object):
    """
    Tributary slot granularity.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['TributarySlotGranularityIdentity']['meta_info']


class ClientSignalIdentity(object):
    """
    Base identity from which specific client signals for the
    tunnel are derived.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalIdentity']['meta_info']


class TributaryProtocolTypeIdentity(object):
    """
    Base identity for protocol framing used by
    tributary signals.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['TributaryProtocolTypeIdentity']['meta_info']


class Tsg1__Dot__25GIdentity(TributarySlotGranularityIdentity):
    """
    1.25G tributary slot granularity.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributarySlotGranularityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Tsg1__Dot__25GIdentity']['meta_info']


class Tsg2__Dot__5GIdentity(TributarySlotGranularityIdentity):
    """
    2.5G tributary slot granularity.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributarySlotGranularityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Tsg2__Dot__5GIdentity']['meta_info']


class ProtOtu2EIdentity(TributaryProtocolTypeIdentity):
    """
    OTU2e type (11.09G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtu2EIdentity']['meta_info']


class ClientSignalFicon4GIdentity(ClientSignalIdentity):
    """
    Client signal type of Fibre Connection 4G.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalFicon4GIdentity']['meta_info']


class ClientSignal10GbeLanIdentity(ClientSignalIdentity):
    """
    Client signal type of 10GbE LAN
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignal10GbeLanIdentity']['meta_info']


class ClientSignal1GbeIdentity(ClientSignalIdentity):
    """
    Client signal type of 1GbE
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignal1GbeIdentity']['meta_info']


class ClientSignalOduflexCbrIdentity(ClientSignalIdentity):
    """
    Client signal type of ODU Flex CBR
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOduflexCbrIdentity']['meta_info']


class ClientSignal40GbeIdentity(ClientSignalIdentity):
    """
    Client signal type of 40GbE
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignal40GbeIdentity']['meta_info']


class ClientSignalFc800Identity(ClientSignalIdentity):
    """
    Client signal type of Fibre Channel FC800.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalFc800Identity']['meta_info']


class Prot40GbeIdentity(TributaryProtocolTypeIdentity):
    """
    40G Ethernet protocol
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Prot40GbeIdentity']['meta_info']


class ClientSignalOduflexGfpIdentity(ClientSignalIdentity):
    """
    Client signal type of ODU Flex GFP
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOduflexGfpIdentity']['meta_info']


class ClientSignal10GbeWanIdentity(ClientSignalIdentity):
    """
    Client signal type of 10GbE WAN
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignal10GbeWanIdentity']['meta_info']


class Prot1GbeIdentity(TributaryProtocolTypeIdentity):
    """
    1G Ethernet protocol
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Prot1GbeIdentity']['meta_info']


class ClientSignalFc400Identity(ClientSignalIdentity):
    """
    Client signal type of Fibre Channel FC400.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalFc400Identity']['meta_info']


class ClientSignalOc3_Stm1Identity(ClientSignalIdentity):
    """
    Client signal type of OC3 & STM1
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOc3_Stm1Identity']['meta_info']


class ClientSignalOc192_Stm64Identity(ClientSignalIdentity):
    """
    Client signal type of OC192 & STM64
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOc192_Stm64Identity']['meta_info']


class ClientSignalOc768_Stm256Identity(ClientSignalIdentity):
    """
    Client signal type of OC768 & STM256
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOc768_Stm256Identity']['meta_info']


class ClientSignalOc48_Stm16Identity(ClientSignalIdentity):
    """
    Client signal type of OC48 & STM16
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOc48_Stm16Identity']['meta_info']


class ProtOdu3Identity(TributaryProtocolTypeIdentity):
    """
    ODU3 protocol (40.31G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu3Identity']['meta_info']


class ProtOdu2Identity(TributaryProtocolTypeIdentity):
    """
    ODU2 protocol (10.03G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu2Identity']['meta_info']


class ProtOdu1Identity(TributaryProtocolTypeIdentity):
    """
    ODU1 protocol (2.49G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu1Identity']['meta_info']


class ProtOdu0Identity(TributaryProtocolTypeIdentity):
    """
    ODU0 protocol (1.24G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu0Identity']['meta_info']


class ProtOdu4Identity(TributaryProtocolTypeIdentity):
    """
    ODU4 protocol (104.79G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu4Identity']['meta_info']


class ClientSignalFicon8GIdentity(ClientSignalIdentity):
    """
    Client signal type of Fibre Connection 8G.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalFicon8GIdentity']['meta_info']


class ClientSignal100GbeIdentity(ClientSignalIdentity):
    """
    Client signal type of 100GbE
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignal100GbeIdentity']['meta_info']


class ProtOducnIdentity(TributaryProtocolTypeIdentity):
    """
    ODUCn protocol (beyond 100G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOducnIdentity']['meta_info']


class ProtOtu3Identity(TributaryProtocolTypeIdentity):
    """
    OTU3 type (43.01G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtu3Identity']['meta_info']


class ProtOtu2Identity(TributaryProtocolTypeIdentity):
    """
    OTU2 type (10.70G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtu2Identity']['meta_info']


class ProtOtu1Identity(TributaryProtocolTypeIdentity):
    """
    OTU1 protocol (2.66G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtu1Identity']['meta_info']


class ProtOduflexCbrIdentity(TributaryProtocolTypeIdentity):
    """
    ODU Flex CBR protocol for transporting constant bit
    rate signal.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOduflexCbrIdentity']['meta_info']


class ClientSignalOdu3Identity(ClientSignalIdentity):
    """
    Client signal type of ODU3 (40.31G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu3Identity']['meta_info']


class ClientSignalOdu2Identity(ClientSignalIdentity):
    """
    Client signal type of ODU2 (10.03G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu2Identity']['meta_info']


class ClientSignalOdu1Identity(ClientSignalIdentity):
    """
    ODU1 protocol (2.49G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu1Identity']['meta_info']


class ProtOtu4Identity(TributaryProtocolTypeIdentity):
    """
    OTU4 type (111.80G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtu4Identity']['meta_info']


class ProtOdu2EIdentity(TributaryProtocolTypeIdentity):
    """
    ODU2e protocol (10.39G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOdu2EIdentity']['meta_info']


class ProtOtucnIdentity(TributaryProtocolTypeIdentity):
    """
    OTUCn type (beyond 100G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOtucnIdentity']['meta_info']


class ClientSignalOdu0Identity(ClientSignalIdentity):
    """
    Client signal type of ODU0 (1.24G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu0Identity']['meta_info']


class Prot10GbeLanIdentity(TributaryProtocolTypeIdentity):
    """
    10G Ethernet LAN protocol
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Prot10GbeLanIdentity']['meta_info']


class ClientSignalOdu2EIdentity(ClientSignalIdentity):
    """
    Client signal type of ODU2e (10.39G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu2EIdentity']['meta_info']


class ProtOduflexGfpIdentity(TributaryProtocolTypeIdentity):
    """
    ODU Flex GFP protocol for transporting stream of packets
    using Generic Framing Procedure.
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ProtOduflexGfpIdentity']['meta_info']


class ClientSignalOdu4Identity(ClientSignalIdentity):
    """
    Client signal type of ODU4 (104.79G)
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOdu4Identity']['meta_info']


class Prot100GbeIdentity(TributaryProtocolTypeIdentity):
    """
    100G Ethernet protocol
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        TributaryProtocolTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['Prot100GbeIdentity']['meta_info']


class ClientSignalOc12_Stm4Identity(ClientSignalIdentity):
    """
    Client signal type of OC12 & STM4
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOc12_Stm4Identity']['meta_info']


class ClientSignalOducnIdentity(ClientSignalIdentity):
    """
    Client signal type of ODUCn (beyond 100G).
    
    

    """

    _prefix = 'tran-types'
    _revision = '2016-10-25'

    def __init__(self):
        ClientSignalIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_transport_types as meta
        return meta._meta_table['ClientSignalOducnIdentity']['meta_info']



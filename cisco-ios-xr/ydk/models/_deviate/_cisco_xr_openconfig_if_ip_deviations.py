
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Interfaces.Interface.RoutedVlan.Ipv4.Address' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Config.mtu' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.Neighbor' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv4.State.mtu' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Address' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config.create_global_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config.create_temporary_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config.temporary_preferred_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config.temporary_valid_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State.create_global_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State.create_temporary_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State.temporary_preferred_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State.temporary_valid_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Config.dup_addr_detect_transmits' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Config.mtu' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.Neighbor' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.State.dup_addr_detect_transmits' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.RoutedVlan.Ipv6.State.mtu' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config.create_global_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config.create_temporary_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config.temporary_preferred_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config.temporary_valid_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State.create_global_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State.create_temporary_addresses' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State.temporary_preferred_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State.temporary_valid_lifetime' : {
        'deviation_typ' : 'not_supported',
    },
}

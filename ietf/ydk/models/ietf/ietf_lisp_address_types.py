""" ietf_lisp_address_types 

This YANG module defines the LISP Canonical Address Formats
(LCAF) for LISP. The module can be extended by vendors to
define vendor\-specific parameters.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6338; see
the RFC itself for full legal notices.



"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class LispAddressFamilyIdentity(object):
    """
    Base identity from which identities describing LISP address
    families are derived.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['LispAddressFamilyIdentity']['meta_info']


class Ipv6AfiIdentity(LispAddressFamilyIdentity):
    """
    IANA IPv6 address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['Ipv6AfiIdentity']['meta_info']


class AsNumberAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA AS Number address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['AsNumberAfiIdentity']['meta_info']


class LcafIdentity(LispAddressFamilyIdentity):
    """
    IANA LISP Canonical Address Format address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['LcafIdentity']['meta_info']


class NullAddressLcafIdentity(LcafIdentity):
    """
    Null body LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['NullAddressLcafIdentity']['meta_info']


class ReplicationListLcafIdentity(LcafIdentity):
    """
    Replication\-List LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['ReplicationListLcafIdentity']['meta_info']


class ExplicitLocatorPathLcafIdentity(LcafIdentity):
    """
    Explicit Locator Path LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['ExplicitLocatorPathLcafIdentity']['meta_info']


class NoAddressAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA Reserved.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['NoAddressAfiIdentity']['meta_info']


class EncapsulationFormatLcafIdentity(LcafIdentity):
    """
    Encapsulation Format LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['EncapsulationFormatLcafIdentity']['meta_info']


class NatTraversalLcafIdentity(LcafIdentity):
    """
    NAT\-Traversal LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['NatTraversalLcafIdentity']['meta_info']


class KeyValueAddressLcafIdentity(LcafIdentity):
    """
    Key/Value Address LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['KeyValueAddressLcafIdentity']['meta_info']


class Ipv4AfiIdentity(LispAddressFamilyIdentity):
    """
    IANA IPv4 address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['Ipv4AfiIdentity']['meta_info']


class MulticastInfoLcafIdentity(LcafIdentity):
    """
    Multicast Info LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['MulticastInfoLcafIdentity']['meta_info']


class SecurityKeyLcafIdentity(LcafIdentity):
    """
    Security Key LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['SecurityKeyLcafIdentity']['meta_info']


class Ipv4PrefixAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA IPv4 address family prefix.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['Ipv4PrefixAfiIdentity']['meta_info']


class Ipv6PrefixAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA IPv6 address family prefix.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['Ipv6PrefixAfiIdentity']['meta_info']


class AfiListLcafIdentity(LcafIdentity):
    """
    AFI\-List LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['AfiListLcafIdentity']['meta_info']


class DistinguishedNameAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA Distinguished Name address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['DistinguishedNameAfiIdentity']['meta_info']


class OpaqueKeyLcafIdentity(LcafIdentity):
    """
    Opaque Key LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['OpaqueKeyLcafIdentity']['meta_info']


class ApplicationDataLcafIdentity(LcafIdentity):
    """
    Application Data LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['ApplicationDataLcafIdentity']['meta_info']


class JsonDataModelLcafIdentity(LcafIdentity):
    """
    JSON Data Model LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['JsonDataModelLcafIdentity']['meta_info']


class SourceDestKeyLcafIdentity(LcafIdentity):
    """
    Source/Dest LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['SourceDestKeyLcafIdentity']['meta_info']


class MacAfiIdentity(LispAddressFamilyIdentity):
    """
    IANA MAC address family.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LispAddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['MacAfiIdentity']['meta_info']


class ServicePathLcafIdentity(LcafIdentity):
    """
    Service Path LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['ServicePathLcafIdentity']['meta_info']


class GeoCoordinatesLcafIdentity(LcafIdentity):
    """
    Geo\-coordinates LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['GeoCoordinatesLcafIdentity']['meta_info']


class InstanceIdLcafIdentity(LcafIdentity):
    """
    Instance\-ID LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['InstanceIdLcafIdentity']['meta_info']


class AsNumberLcafIdentity(LcafIdentity):
    """
    AS Number LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['AsNumberLcafIdentity']['meta_info']


class NonceLocatorLcafIdentity(LcafIdentity):
    """
    Nonce\-Locator LCAF type.
    
    

    """

    _prefix = 'laddr'
    _revision = '2015-11-05'

    def __init__(self):
        LcafIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_lisp_address_types as meta
        return meta._meta_table['NonceLocatorLcafIdentity']['meta_info']



""" ietf_savi_dhcpv4 


The Yang data module defined for SAVI DHCPv4.


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_savi import BindingStateIdentity


class SaviDhcpStateIdentity(BindingStateIdentity):
    """
    Base identity for the sates definition of SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        BindingStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['SaviDhcpStateIdentity']['meta_info']


class VerifyIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['VerifyIdentity']['meta_info']


class RecoveryIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['RecoveryIdentity']['meta_info']


class Init_BindIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['Init_BindIdentity']['meta_info']


class DetectionIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['DetectionIdentity']['meta_info']


class BindIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['BindIdentity']['meta_info']


class No_BindIdentity(SaviDhcpStateIdentity):
    """
    A state defined in SAVI DHCPv4.
    
    

    """

    _prefix = 'savi-dhcpv4'
    _revision = '2017-02-15'

    def __init__(self):
        SaviDhcpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_dhcpv4 as meta
        return meta._meta_table['No_BindIdentity']['meta_info']



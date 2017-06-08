""" ietf_savi_send 


The Yang data module defined for SAVI SEND.


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_savi import BindingStateIdentity


class SaviSendStateIdentity(BindingStateIdentity):
    """
    Base identity for the sates definition of SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        BindingStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['SaviSendStateIdentity']['meta_info']


class TentativeNudIdentity(SaviSendStateIdentity):
    """
    A state defined in SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        SaviSendStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['TentativeNudIdentity']['meta_info']


class Testing_Vp_1Identity(SaviSendStateIdentity):
    """
    A state defined in SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        SaviSendStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['Testing_Vp_1Identity']['meta_info']


class Testing_VpIdentity(SaviSendStateIdentity):
    """
    A state defined in SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        SaviSendStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['Testing_VpIdentity']['meta_info']


class ValidIdentity(SaviSendStateIdentity):
    """
    A state defined in SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        SaviSendStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['ValidIdentity']['meta_info']


class TentativeDadIdentity(SaviSendStateIdentity):
    """
    A state defined in SAVI SEND.
    
    

    """

    _prefix = 'savi-send'
    _revision = '2017-02-15'

    def __init__(self):
        SaviSendStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_send as meta
        return meta._meta_table['TentativeDadIdentity']['meta_info']



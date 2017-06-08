""" ietf_savi_fcfs 


The Yang data module defined for SAVI FCFS.


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError


from ydk.models.ietf.ietf_savi import BindingStateIdentity


class SaviFcfsStateIdentity(BindingStateIdentity):
    """
    Base identity for the sates definition of SAVI FCFS.
    
    

    """

    _prefix = 'savi-fcfs'
    _revision = '2017-02-15'

    def __init__(self):
        BindingStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_fcfs as meta
        return meta._meta_table['SaviFcfsStateIdentity']['meta_info']


class Testing_VpIdentity(SaviFcfsStateIdentity):
    """
    A state defined in SAVI FCFS.
    
    

    """

    _prefix = 'savi-fcfs'
    _revision = '2017-02-15'

    def __init__(self):
        SaviFcfsStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_fcfs as meta
        return meta._meta_table['Testing_VpIdentity']['meta_info']


class TentativeIdentity(SaviFcfsStateIdentity):
    """
    A state defined in SAVI FCFS.
    
    

    """

    _prefix = 'savi-fcfs'
    _revision = '2017-02-15'

    def __init__(self):
        SaviFcfsStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_fcfs as meta
        return meta._meta_table['TentativeIdentity']['meta_info']


class Testing_VpLtIdentity(SaviFcfsStateIdentity):
    """
    A state defined in SAVI FCFS.
    
    

    """

    _prefix = 'savi-fcfs'
    _revision = '2017-02-15'

    def __init__(self):
        SaviFcfsStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_fcfs as meta
        return meta._meta_table['Testing_VpLtIdentity']['meta_info']


class ValidIdentity(SaviFcfsStateIdentity):
    """
    A state defined in SAVI FCFS.
    
    

    """

    _prefix = 'savi-fcfs'
    _revision = '2017-02-15'

    def __init__(self):
        SaviFcfsStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_savi_fcfs as meta
        return meta._meta_table['ValidIdentity']['meta_info']



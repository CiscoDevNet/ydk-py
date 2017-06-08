""" ietf_dots_signal_config 

This module contains YANG definition for DOTS
signal channel session configuration

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SignalConfig(object):
    """
    top level container for DOTS signal channel session
    configuration
    
    .. attribute:: ack_random_factor
    
    	Random factor used to influence the timing of retransmissions
    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
    
    	**range:** \-92233720368547758.08..92233720368547758.07
    
    .. attribute:: ack_timeout
    
    	Initial retransmission timeout value
    	**type**\:  int
    
    	**range:** \-32768..32767
    
    .. attribute:: heartbeat_interval
    
    	heartbeat interval
    	**type**\:  int
    
    	**range:** \-32768..32767
    
    .. attribute:: max_retransmit
    
    	Maximum number of retransmissions
    	**type**\:  int
    
    	**range:** \-32768..32767
    
    .. attribute:: policy_id
    
    	Identifier for the DOTS signal channel session configuration data
    	**type**\:  int
    
    	**range:** \-2147483648..2147483647
    
    

    """

    _prefix = 'config'
    _revision = '2016-11-28'

    def __init__(self):
        self.ack_random_factor = None
        self.ack_timeout = None
        self.heartbeat_interval = None
        self.max_retransmit = None
        self.policy_id = None

    @property
    def _common_path(self):

        return '/ietf-dots-signal-config:signal-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.ack_random_factor is not None:
            return True

        if self.ack_timeout is not None:
            return True

        if self.heartbeat_interval is not None:
            return True

        if self.max_retransmit is not None:
            return True

        if self.policy_id is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dots_signal_config as meta
        return meta._meta_table['SignalConfig']['meta_info']



""" Cisco_IOS_XE_efp_oper 

This module contains a collection of YANG definitions for
service instance (efp) statsCopyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class EfpStats(object):
    """
    Service instance stats
    
    .. attribute:: efp_stat
    
    	
    	**type**\: list of    :py:class:`EfpStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper.EfpStats.EfpStat>`
    
    

    """

    _prefix = 'efp-stats-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.efp_stat = YList()
        self.efp_stat.parent = self
        self.efp_stat.name = 'efp_stat'


    class EfpStat(object):
        """
        
        
        .. attribute:: id  <key>
        
        	
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface  <key>
        
        	
        	**type**\:  str
        
        .. attribute:: in_bytes
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: in_pkts
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_bytes
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_pkts
        
        	
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'efp-stats-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.id = None
            self.interface = None
            self.in_bytes = None
            self.in_pkts = None
            self.out_bytes = None
            self.out_pkts = None

        @property
        def _common_path(self):
            if self.id is None:
                raise YPYModelError('Key property id is None')
            if self.interface is None:
                raise YPYModelError('Key property interface is None')

            return '/Cisco-IOS-XE-efp-oper:efp-stats/Cisco-IOS-XE-efp-oper:efp-stat[Cisco-IOS-XE-efp-oper:id = ' + str(self.id) + '][Cisco-IOS-XE-efp-oper:interface = ' + str(self.interface) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.id is not None:
                return True

            if self.interface is not None:
                return True

            if self.in_bytes is not None:
                return True

            if self.in_pkts is not None:
                return True

            if self.out_bytes is not None:
                return True

            if self.out_pkts is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_efp_oper as meta
            return meta._meta_table['EfpStats.EfpStat']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-efp-oper:efp-stats'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.efp_stat is not None:
            for child_ref in self.efp_stat:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_efp_oper as meta
        return meta._meta_table['EfpStats']['meta_info']



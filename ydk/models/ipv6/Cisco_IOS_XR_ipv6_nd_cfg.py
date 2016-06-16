""" Cisco_IOS_XR_ipv6_nd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-neighbor\: IPv6 neighbor or neighbor discovery
    configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Ipv6NdMonthEnum(Enum):
    """
    Ipv6NdMonthEnum

    Ipv6nd month

    .. data:: JANUARY = 0

    	January

    .. data:: FEBRUARY = 1

    	February

    .. data:: MARCH = 2

    	March

    .. data:: APRIL = 3

    	April

    .. data:: MAY = 4

    	May

    .. data:: JUNE = 5

    	June

    .. data:: JULY = 6

    	July

    .. data:: AUGUST = 7

    	August

    .. data:: SEPTEMBER = 8

    	September

    .. data:: OCTOBER = 9

    	October

    .. data:: NOVEMBER = 10

    	November

    .. data:: DECEMBER = 11

    	December

    """

    JANUARY = 0

    FEBRUARY = 1

    MARCH = 2

    APRIL = 3

    MAY = 4

    JUNE = 5

    JULY = 6

    AUGUST = 7

    SEPTEMBER = 8

    OCTOBER = 9

    NOVEMBER = 10

    DECEMBER = 11


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6NdMonthEnum']


class Ipv6NdRouterPrefEnum(Enum):
    """
    Ipv6NdRouterPrefEnum

    Ipv6 nd router pref

    .. data:: HIGH = 1

    	High preference

    .. data:: MEDIUM = 2

    	Medium preference

    .. data:: LOW = 3

    	Low preference

    """

    HIGH = 1

    MEDIUM = 2

    LOW = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6NdRouterPrefEnum']


class Ipv6SrpEncapsulationEnum(Enum):
    """
    Ipv6SrpEncapsulationEnum

    Ipv6srp encapsulation

    .. data:: SRPA = 5

    	Encapsulation type SRP, prefer side A

    .. data:: SRPB = 6

    	Encapsulation type SRP, prefer side B

    """

    SRPA = 5

    SRPB = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6SrpEncapsulationEnum']



class Ipv6Neighbor(object):
    """
    IPv6 neighbor or neighbor discovery configuration
    
    .. attribute:: neighbors
    
    	IPv6 neighbors
    	**type**\: :py:class:`Neighbors <ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors>`
    
    .. attribute:: scavenge_timeout
    
    	Set lifetime for stale neighbor
    	**type**\: int
    
    	**range:** 1..43200
    
    

    """

    _prefix = 'ipv6-nd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.neighbors = Ipv6Neighbor.Neighbors()
        self.neighbors.parent = self
        self.scavenge_timeout = None


    class Neighbors(object):
        """
        IPv6 neighbors
        
        .. attribute:: neighbor
        
        	IPv6 neighbor configuration
        	**type**\: list of :py:class:`Neighbor <ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ipv6-nd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.neighbor = YList()
            self.neighbor.parent = self
            self.neighbor.name = 'neighbor'


        class Neighbor(object):
            """
            IPv6 neighbor configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: neighbor_address  <key>
            
            	IPv6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: encapsulation
            
            	Encapsulation type only if interface type is SRP
            	**type**\: :py:class:`Ipv6SrpEncapsulationEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6SrpEncapsulationEnum>`
            
            .. attribute:: mac_address
            
            	48\-bit hardware address H.H.H
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: zone
            
            	IPv6 address zone
            	**type**\: str
            
            

            """

            _prefix = 'ipv6-nd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.neighbor_address = None
                self.encapsulation = None
                self.mac_address = None
                self.zone = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')
                if self.neighbor_address is None:
                    raise YPYModelError('Key property neighbor_address is None')

                return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/Cisco-IOS-XR-ipv6-nd-cfg:neighbors/Cisco-IOS-XR-ipv6-nd-cfg:neighbor[Cisco-IOS-XR-ipv6-nd-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv6-nd-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.neighbor_address is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.zone is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
                return meta._meta_table['Ipv6Neighbor.Neighbors.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/Cisco-IOS-XR-ipv6-nd-cfg:neighbors'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
            return meta._meta_table['Ipv6Neighbor.Neighbors']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.neighbors is not None and self.neighbors._has_data():
            return True

        if self.scavenge_timeout is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6Neighbor']['meta_info']



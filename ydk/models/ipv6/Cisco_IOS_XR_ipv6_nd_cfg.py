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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv6NdRouterPref_Enum(Enum):
    """
    Ipv6NdRouterPref_Enum

    Ipv6 nd router pref

    """

    """

    High preference

    """
    HIGH = 1

    """

    Medium preference

    """
    MEDIUM = 2

    """

    Low preference

    """
    LOW = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6NdRouterPref_Enum']


class Ipv6ndMonth_Enum(Enum):
    """
    Ipv6ndMonth_Enum

    Ipv6nd month

    """

    """

    January

    """
    JANUARY = 0

    """

    February

    """
    FEBRUARY = 1

    """

    March

    """
    MARCH = 2

    """

    April

    """
    APRIL = 3

    """

    May

    """
    MAY = 4

    """

    June

    """
    JUNE = 5

    """

    July

    """
    JULY = 6

    """

    August

    """
    AUGUST = 7

    """

    September

    """
    SEPTEMBER = 8

    """

    October

    """
    OCTOBER = 9

    """

    November

    """
    NOVEMBER = 10

    """

    December

    """
    DECEMBER = 11


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6ndMonth_Enum']


class Ipv6srpEncapsulation_Enum(Enum):
    """
    Ipv6srpEncapsulation_Enum

    Ipv6srp encapsulation

    """

    """

    Encapsulation type SRP, prefer side A

    """
    SRPA = 5

    """

    Encapsulation type SRP, prefer side B

    """
    SRPB = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6srpEncapsulation_Enum']



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
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: neighbor_address
            
            	IPv6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: encapsulation
            
            	Encapsulation type only if interface type is SRP
            	**type**\: :py:class:`Ipv6srpEncapsulation_Enum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6srpEncapsulation_Enum>`
            
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
                    raise YPYDataValidationError('Key property interface_name is None')
                if self.neighbor_address is None:
                    raise YPYDataValidationError('Key property neighbor_address is None')

                return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/Cisco-IOS-XR-ipv6-nd-cfg:neighbors/Cisco-IOS-XR-ipv6-nd-cfg:neighbor[Cisco-IOS-XR-ipv6-nd-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv6-nd-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
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
            if self.is_presence():
                return True
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
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
        if self.is_presence():
            return True
        if self.neighbors is not None and self.neighbors._has_data():
            return True

        if self.neighbors is not None and self.neighbors.is_presence():
            return True

        if self.scavenge_timeout is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6Neighbor']['meta_info']



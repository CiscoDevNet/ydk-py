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

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = 0

    february = 1

    march = 2

    april = 3

    may = 4

    june = 5

    july = 6

    august = 7

    september = 8

    october = 9

    november = 10

    december = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6NdMonthEnum']


class Ipv6NdRouterPrefEnum(Enum):
    """
    Ipv6NdRouterPrefEnum

    Ipv6 nd router pref

    .. data:: high = 1

    	High preference

    .. data:: medium = 2

    	Medium preference

    .. data:: low = 3

    	Low preference

    """

    high = 1

    medium = 2

    low = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6NdRouterPrefEnum']


class Ipv6SrpEncapsulationEnum(Enum):
    """
    Ipv6SrpEncapsulationEnum

    Ipv6srp encapsulation

    .. data:: srpa = 5

    	Encapsulation type SRP, prefer side A

    .. data:: srpb = 6

    	Encapsulation type SRP, prefer side B

    """

    srpa = 5

    srpb = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6SrpEncapsulationEnum']



class Ipv6Neighbor(object):
    """
    IPv6 neighbor or neighbor discovery configuration
    
    .. attribute:: neighbors
    
    	IPv6 neighbors
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors>`
    
    .. attribute:: scavenge_timeout
    
    	Set lifetime for stale neighbor
    	**type**\:  int
    
    	**range:** 1..43200
    
    	**units**\: second
    
    

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
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors.Neighbor>`
        
        

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
            
            .. attribute:: neighbor_address  <key>
            
            	IPv6 address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: encapsulation
            
            	Encapsulation type only if interface type is SRP
            	**type**\:   :py:class:`Ipv6SrpEncapsulationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6SrpEncapsulationEnum>`
            
            .. attribute:: mac_address
            
            	48\-bit hardware address H.H.H
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**mandatory**\: True
            
            .. attribute:: zone
            
            	IPv6 address zone
            	**type**\:  str
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv6-nd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.neighbor_address = None
                self.interface_name = None
                self.encapsulation = None
                self.mac_address = None
                self.zone = None

            @property
            def _common_path(self):
                if self.neighbor_address is None:
                    raise YPYModelError('Key property neighbor_address is None')
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/Cisco-IOS-XR-ipv6-nd-cfg:neighbors/Cisco-IOS-XR-ipv6-nd-cfg:neighbor[Cisco-IOS-XR-ipv6-nd-cfg:neighbor-address = ' + str(self.neighbor_address) + '][Cisco-IOS-XR-ipv6-nd-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.neighbor_address is not None:
                    return True

                if self.interface_name is not None:
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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
                return meta._meta_table['Ipv6Neighbor.Neighbors.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/Cisco-IOS-XR-ipv6-nd-cfg:neighbors'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
            return meta._meta_table['Ipv6Neighbor.Neighbors']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.neighbors is not None and self.neighbors._has_data():
            return True

        if self.scavenge_timeout is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_nd_cfg as meta
        return meta._meta_table['Ipv6Neighbor']['meta_info']



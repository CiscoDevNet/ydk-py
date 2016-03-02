""" Cisco_IOS_XR_ncs1k_mxp_lldp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp\-lldp package operational data.

This module contains definitions
for the following management objects\:
  lldp\-snoop\-data\: Information related to LLDP Snoop

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class LldpSnoopData(object):
    """
    Information related to LLDP Snoop
    
    .. attribute:: ethernet_controller_names
    
    	Ethernet controller snoop data
    	**type**\: :py:class:`EthernetControllerNames <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames>`
    
    

    """

    _prefix = 'ncs1k-mxp-lldp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.ethernet_controller_names = LldpSnoopData.EthernetControllerNames()
        self.ethernet_controller_names.parent = self


    class EthernetControllerNames(object):
        """
        Ethernet controller snoop data
        
        .. attribute:: ethernet_controller_name
        
        	port Name
        	**type**\: list of :py:class:`EthernetControllerName <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper.LldpSnoopData.EthernetControllerNames.EthernetControllerName>`
        
        

        """

        _prefix = 'ncs1k-mxp-lldp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ethernet_controller_name = YList()
            self.ethernet_controller_name.parent = self
            self.ethernet_controller_name.name = 'ethernet_controller_name'


        class EthernetControllerName(object):
            """
            port Name
            
            .. attribute:: name
            
            	Port name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: lldp_neighbor
            
            	LldpNeighbor
            	**type**\: str
            
            	**range:** 0..40
            
            

            """

            _prefix = 'ncs1k-mxp-lldp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.lldp_neighbor = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-names/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-name[Cisco-IOS-XR-ncs1k-mxp-lldp-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.name is not None:
                    return True

                if self.lldp_neighbor is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
                return meta._meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:ethernet-controller-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ethernet_controller_name is not None:
                for child_ref in self.ethernet_controller_name:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
            return meta._meta_table['LldpSnoopData.EthernetControllerNames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-lldp-oper:lldp-snoop-data'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ethernet_controller_names is not None and self.ethernet_controller_names._has_data():
            return True

        if self.ethernet_controller_names is not None and self.ethernet_controller_names.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_lldp_oper as meta
        return meta._meta_table['LldpSnoopData']['meta_info']



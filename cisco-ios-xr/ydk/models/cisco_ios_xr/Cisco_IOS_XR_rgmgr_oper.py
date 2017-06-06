""" Cisco_IOS_XR_rgmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package operational data.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy group manager operational
    data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class RedundancyGroupManager(object):
    """
    Redundancy group manager operational data
    
    .. attribute:: controllers
    
    	Redundancy group manager data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers>`
    
    

    """

    _prefix = 'rgmgr-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.controllers = RedundancyGroupManager.Controllers()
        self.controllers.parent = self


    class Controllers(object):
        """
        Redundancy group manager data
        
        .. attribute:: controller
        
        	Display redundancy group by controller name
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers.Controller>`
        
        

        """

        _prefix = 'rgmgr-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.controller = YList()
            self.controller.parent = self
            self.controller.name = 'controller'


        class Controller(object):
            """
            Display redundancy group by controller name
            
            .. attribute:: controller_name  <key>
            
            	Controller name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: backup_interface_handle
            
            	Backup interface handle
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: backup_interface_next_hop_ip_address
            
            	Backup interface next hop IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: controller_handle
            
            	Handle of controller being backed up
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: controller_name_xr
            
            	Name of controller being backed up
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: inter_chassis_group_state
            
            	Configured interchassis redundancy group state
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: multi_router_aps_group_number
            
            	Configured interchassis redundancy group number
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'rgmgr-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.controller_name = None
                self.backup_interface_handle = None
                self.backup_interface_name = None
                self.backup_interface_next_hop_ip_address = None
                self.controller_handle = None
                self.controller_name_xr = None
                self.inter_chassis_group_state = None
                self.multi_router_aps_group_number = None

            @property
            def _common_path(self):
                if self.controller_name is None:
                    raise YPYModelError('Key property controller_name is None')

                return '/Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/Cisco-IOS-XR-rgmgr-oper:controllers/Cisco-IOS-XR-rgmgr-oper:controller[Cisco-IOS-XR-rgmgr-oper:controller-name = ' + str(self.controller_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.controller_name is not None:
                    return True

                if self.backup_interface_handle is not None:
                    return True

                if self.backup_interface_name is not None:
                    return True

                if self.backup_interface_next_hop_ip_address is not None:
                    return True

                if self.controller_handle is not None:
                    return True

                if self.controller_name_xr is not None:
                    return True

                if self.inter_chassis_group_state is not None:
                    return True

                if self.multi_router_aps_group_number is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
                return meta._meta_table['RedundancyGroupManager.Controllers.Controller']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/Cisco-IOS-XR-rgmgr-oper:controllers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.controller is not None:
                for child_ref in self.controller:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
            return meta._meta_table['RedundancyGroupManager.Controllers']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.controllers is not None and self.controllers._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
        return meta._meta_table['RedundancyGroupManager']['meta_info']



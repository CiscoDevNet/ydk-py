""" Cisco_IOS_XR_group_cfg 

This module contains IOS\-XR group YANG data 
for flexible cli groups 
    
Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Groups(object):
    """
    config groups
    
    .. attribute:: group
    
    	Group config definition
    	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg.Groups.Group>`
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        self.group = YList()
        self.group.parent = self
        self.group.name = 'group'


    class Group(object):
        """
        Group config definition
        
        .. attribute:: group_name  <key>
        
        	Group name
        	**type**\:  str
        
        	**length:** 0..32
        
        

        """

        _prefix = 'group-cfg'
        _revision = '2016-04-29'

        def __init__(self):
            self.parent = None
            self.group_name = None

        @property
        def _common_path(self):
            if self.group_name is None:
                raise YPYModelError('Key property group_name is None')

            return '/Cisco-IOS-XR-group-cfg:groups/Cisco-IOS-XR-group-cfg:group[Cisco-IOS-XR-group-cfg:group-name = ' + str(self.group_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.group_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_group_cfg as meta
            return meta._meta_table['Groups.Group']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-group-cfg:groups'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.group is not None:
            for child_ref in self.group:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_group_cfg as meta
        return meta._meta_table['Groups']['meta_info']


class ApplyGroups(object):
    """
    apply groups
    
    .. attribute:: apply_group
    
    	apply\-group name
    	**type**\:  str
    
    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
    
    

    """

    _prefix = 'group-cfg'
    _revision = '2016-04-29'

    def __init__(self):
        self.apply_group = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-group-cfg:apply-groups'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.apply_group is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_group_cfg as meta
        return meta._meta_table['ApplyGroups']['meta_info']



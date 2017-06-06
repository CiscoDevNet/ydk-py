""" Cisco_IOS_XR_cfgmgr_rollback_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class RollBackConfigurationLastRpc(object):
    """
    Rollback last <n> commits made
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationLastRpc.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = RollBackConfigurationLastRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: count
        
        	Number of commits to rollback
        	**type**\:  int
        
        	**range:** 1..100
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.best_effort = None
            self.comment = None
            self.count = None
            self.force = None
            self.label = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last/Cisco-IOS-XR-cfgmgr-rollback-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.best_effort is not None:
                return True

            if self.comment is not None:
                return True

            if self.count is not None:
                return True

            if self.force is not None:
                return True

            if self.label is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
            return meta._meta_table['RollBackConfigurationLastRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
        return meta._meta_table['RollBackConfigurationLastRpc']['meta_info']


class RollBackConfigurationToRpc(object):
    """
    Rollback up to (and including) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationToRpc.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = RollBackConfigurationToRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.best_effort = None
            self.comment = None
            self.commit_id = None
            self.force = None
            self.label = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to/Cisco-IOS-XR-cfgmgr-rollback-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.best_effort is not None:
                return True

            if self.comment is not None:
                return True

            if self.commit_id is not None:
                return True

            if self.force is not None:
                return True

            if self.label is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
            return meta._meta_table['RollBackConfigurationToRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
        return meta._meta_table['RollBackConfigurationToRpc']['meta_info']


class RollBackConfigurationToExcludeRpc(object):
    """
    Rollback up to (and excluding) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationToExcludeRpc.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = RollBackConfigurationToExcludeRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.best_effort = None
            self.comment = None
            self.commit_id = None
            self.force = None
            self.label = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude/Cisco-IOS-XR-cfgmgr-rollback-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.best_effort is not None:
                return True

            if self.comment is not None:
                return True

            if self.commit_id is not None:
                return True

            if self.force is not None:
                return True

            if self.label is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
            return meta._meta_table['RollBackConfigurationToExcludeRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
        return meta._meta_table['RollBackConfigurationToExcludeRpc']['meta_info']


class RollBackConfigurationRpc(object):
    """
    Rollback a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationRpc.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = RollBackConfigurationRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.best_effort = None
            self.comment = None
            self.commit_id = None
            self.force = None
            self.label = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration/Cisco-IOS-XR-cfgmgr-rollback-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.best_effort is not None:
                return True

            if self.comment is not None:
                return True

            if self.commit_id is not None:
                return True

            if self.force is not None:
                return True

            if self.label is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
            return meta._meta_table['RollBackConfigurationRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cfgmgr_rollback_act as meta
        return meta._meta_table['RollBackConfigurationRpc']['meta_info']



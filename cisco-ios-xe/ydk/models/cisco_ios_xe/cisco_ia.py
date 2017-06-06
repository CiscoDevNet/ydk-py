""" cisco_ia 

DMI self\-management YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CiaLogLevelEnum(Enum):
    """
    CiaLogLevelEnum

    Logging levels for DMI

    .. data:: none = 0

    	No logging

    .. data:: error = 1

    	Log errors only

    .. data:: warning = 2

    	Log errors and warnings only

    .. data:: information = 3

    	Log errors, warnings, and information only

    .. data:: debug = 4

    	Log errors, warnings, information,

    	and debug messages

    """

    none = 0

    error = 1

    warning = 2

    information = 3

    debug = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['CiaLogLevelEnum']


class CiaSyncTypeEnum(Enum):
    """
    CiaSyncTypeEnum

    Controls the elements sent to the DMI 

    database from the Network Element

    .. data:: disabled = 0

    	Do no synchronize the DMI

    	database from the Network Element

    .. data:: without_defaults = 1

    	Collect "show running" from 

    	the Network Element

    .. data:: include_defaults = 2

    	Collect "show running all" from 

    	the Network Element

    """

    disabled = 0

    without_defaults = 1

    include_defaults = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['CiaSyncTypeEnum']


class OnepLogLevelEnum(Enum):
    """
    OnepLogLevelEnum

    Logging levels for Onep

    .. data:: none = 0

    	No logging

    .. data:: fatal = 1

    	Log fatal events only

    .. data:: error = 2

    	Log fatal events and errors only

    .. data:: warning = 3

    	Log fatal events, errors, and warnings only

    .. data:: information = 4

    	Log fatal events, errors, warnings, 

    	and information only

    .. data:: debug = 5

    	Log fatal events, errors, warnings, information,

    	and debug messages

    .. data:: trace = 6

    	Log all messages

    """

    none = 0

    fatal = 1

    error = 2

    warning = 3

    information = 4

    debug = 5

    trace = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['OnepLogLevelEnum']


class SyslogSeverityEnum(Enum):
    """
    SyslogSeverityEnum

    Standard Syslog logging levels)

    .. data:: none = 8

    	No logging

    .. data:: emergency = 0

    	Emergency Level Msg

    .. data:: alert = 1

    	Alert Level Msg

    .. data:: critical = 2

    	Critical Level Msg

    .. data:: error = 3

    	Error Level Msg

    .. data:: warning = 4

    	Warning Level Msg

    .. data:: notice = 5

    	Notification Level Msg

    .. data:: info = 6

    	Informational Level Msg

    .. data:: debug = 7

    	Debugging Level Msg

    """

    none = 8

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    info = 6

    debug = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['SyslogSeverityEnum']



class SyncFromRpc(object):
    """
    Synchronize the network element's 
    running\-configuration to ConfD.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.SyncFromRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SyncFromRpc.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = SyncFromRpc.Input()
        self.input.parent = self
        self.output = SyncFromRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: sync_defaults
        
        	Sends the output of  "show running all" line by line to Confd
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.sync_defaults = None

        @property
        def _common_path(self):

            return '/cisco-ia:sync-from/cisco-ia:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.sync_defaults is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['SyncFromRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/cisco-ia:sync-from/cisco-ia:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['SyncFromRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-ia:sync-from'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['SyncFromRpc']['meta_info']


class SaveConfigRpc(object):
    """
    Copy the running\-config to 
    startup\-config on the Network
    Element.
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SaveConfigRpc.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        self.output = SaveConfigRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/cisco-ia:save-config/cisco-ia:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['SaveConfigRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-ia:save-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['SaveConfigRpc']['meta_info']


class CheckpointRpc(object):
    """
    Create a configuration rollback checkpoint.
    Equivalent to the "archive config" CLI
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.CheckpointRpc.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        self.output = CheckpointRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/cisco-ia:checkpoint/cisco-ia:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['CheckpointRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-ia:checkpoint'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['CheckpointRpc']['meta_info']


class RevertRpc(object):
    """
    Cancel the timed rollback and trigger the
    rollback immediately, or to reset parameters 
    for the timed rollback
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.RevertRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.RevertRpc.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = RevertRpc.Input()
        self.input.parent = self
        self.output = RevertRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: idle
        
        	Maximum allowable time period of no activity before reverting to the saved configuration
        	**type**\:  int
        
        	**range:** 1..120
        
        .. attribute:: now
        
        	To cancel the timed rollback and  trigger the rollback immediately
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: timer
        
        	Reset parameters for the timed rollback
        	**type**\:  int
        
        	**range:** 1..120
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.idle = None
            self.now = None
            self.timer = None

        @property
        def _common_path(self):

            return '/cisco-ia:revert/cisco-ia:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.idle is not None:
                return True

            if self.now is not None:
                return True

            if self.timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['RevertRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/cisco-ia:revert/cisco-ia:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['RevertRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-ia:revert'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['RevertRpc']['meta_info']


class RollbackRpc(object):
    """
    Replaces the current running configuration 
    file with a saved Cisco IOS XE configuration file.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.RollbackRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.RollbackRpc.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2017-03-02'

    def __init__(self):
        self.input = RollbackRpc.Input()
        self.input.parent = self
        self.output = RollbackRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: nolock
        
        	Disables the locking of the running  configuration file that prevents other users from changing the running configuration  during a configuration replace operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: revert_on_error
        
        	Reverts to the original configuration upon error
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: revert_timer
        
        	Reverts to the original configuration if  specified time elapses
        	**type**\:  int
        
        	**range:** 1..120
        
        .. attribute:: target_url
        
        	Cisco IOS XE configuration file that is to  replace the current running configuration
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: verbose
        
        	Display a list of the command lines applied by  the Cisco IOS XE software parser during each pass  of the configuration replace operation. The total  number of passes performed is also displayed
        	**type**\:  bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.nolock = None
            self.revert_on_error = None
            self.revert_timer = None
            self.target_url = None
            self.verbose = None

        @property
        def _common_path(self):

            return '/cisco-ia:rollback/cisco-ia:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.nolock is not None:
                return True

            if self.revert_on_error is not None:
                return True

            if self.revert_timer is not None:
                return True

            if self.target_url is not None:
                return True

            if self.verbose is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['RollbackRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/cisco-ia:rollback/cisco-ia:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
            return meta._meta_table['RollbackRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-ia:rollback'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ia as meta
        return meta._meta_table['RollbackRpc']['meta_info']



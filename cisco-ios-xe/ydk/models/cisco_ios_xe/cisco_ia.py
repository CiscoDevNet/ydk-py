""" cisco_ia 

DMI self\-management YANG module for IOS
Copyright (c) 2016, 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiaLogLevel(Enum):
    """
    CiaLogLevel (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    error = Enum.YLeaf(1, "error")

    warning = Enum.YLeaf(2, "warning")

    information = Enum.YLeaf(3, "information")

    debug = Enum.YLeaf(4, "debug")


class CiaSyncType(Enum):
    """
    CiaSyncType (Enum Class)

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

    disabled = Enum.YLeaf(0, "disabled")

    without_defaults = Enum.YLeaf(1, "without-defaults")

    include_defaults = Enum.YLeaf(2, "include-defaults")


class OnepLogLevel(Enum):
    """
    OnepLogLevel (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    fatal = Enum.YLeaf(1, "fatal")

    error = Enum.YLeaf(2, "error")

    warning = Enum.YLeaf(3, "warning")

    information = Enum.YLeaf(4, "information")

    debug = Enum.YLeaf(5, "debug")

    trace = Enum.YLeaf(6, "trace")


class SyslogSeverity(Enum):
    """
    SyslogSeverity (Enum Class)

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

    none = Enum.YLeaf(8, "none")

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    info = Enum.YLeaf(6, "info")

    debug = Enum.YLeaf(7, "debug")



class SyncFrom(Entity):
    """
    Synchronize the network element's 
    running\-configuration to ConfD.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.SyncFrom.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SyncFrom.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(SyncFrom, self).__init__()
        self._top_entity = None

        self.yang_name = "sync-from"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = SyncFrom.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = SyncFrom.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:sync-from"


    class Input(Entity):
        """
        
        
        .. attribute:: sync_defaults
        
        	Sends the output of  "show running all" line by line to Confd
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ignore_presrv_paths
        
        	Sync everything under /native. Ignore any preserve paths
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(SyncFrom.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "sync-from"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sync_defaults', YLeaf(YType.empty, 'sync-defaults')),
                ('ignore_presrv_paths', YLeaf(YType.empty, 'ignore-presrv-paths')),
            ])
            self.sync_defaults = None
            self.ignore_presrv_paths = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-ia:sync-from/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SyncFrom.Input, ['sync_defaults', 'ignore_presrv_paths'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(SyncFrom.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "sync-from"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:sync-from/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SyncFrom.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = SyncFrom()
        return self._top_entity

class SaveConfig(Entity):
    """
    Copy the running\-config to 
    startup\-config on the Network
    Element.
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.SaveConfig.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(SaveConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "save-config"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = SaveConfig.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:save-config"


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(SaveConfig.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "save-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:save-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SaveConfig.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = SaveConfig()
        return self._top_entity

class IsSyncing(Entity):
    """
    Checks to see if sync from the
    network element to the running data store
    is in progress.
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.IsSyncing.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(IsSyncing, self).__init__()
        self._top_entity = None

        self.yang_name = "is-syncing"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = IsSyncing.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:is-syncing"


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(IsSyncing.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "is-syncing"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:is-syncing/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IsSyncing.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = IsSyncing()
        return self._top_entity

class Checkpoint(Entity):
    """
    Create a configuration rollback checkpoint.
    Equivalent to the "archive config" CLI
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Checkpoint.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(Checkpoint, self).__init__()
        self._top_entity = None

        self.yang_name = "checkpoint"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.output = Checkpoint.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:checkpoint"


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(Checkpoint.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "checkpoint"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:checkpoint/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Checkpoint.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Checkpoint()
        return self._top_entity

class Revert(Entity):
    """
    Cancel the timed rollback and trigger the
    rollback immediately, or to reset parameters 
    for the timed rollback
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.Revert.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Revert.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(Revert, self).__init__()
        self._top_entity = None

        self.yang_name = "revert"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Revert.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Revert.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:revert"


    class Input(Entity):
        """
        
        
        .. attribute:: now
        
        	To cancel the timed rollback and  trigger the rollback immediately
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: timer
        
        	Reset parameters for the timed rollback
        	**type**\: int
        
        	**range:** 1..120
        
        .. attribute:: idle
        
        	Maximum allowable time period of no activity before reverting to the saved configuration
        	**type**\: int
        
        	**range:** 1..120
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(Revert.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "revert"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('now', YLeaf(YType.empty, 'now')),
                ('timer', YLeaf(YType.int16, 'timer')),
                ('idle', YLeaf(YType.int16, 'idle')),
            ])
            self.now = None
            self.timer = None
            self.idle = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-ia:revert/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Revert.Input, ['now', 'timer', 'idle'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(Revert.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "revert"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:revert/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Revert.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Revert()
        return self._top_entity

class Rollback(Entity):
    """
    Replaces the current running configuration 
    file with a saved Cisco IOS XE configuration file.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_ia.Rollback.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_ia.Rollback.Output>`
    
    

    """

    _prefix = 'cisco-ia'
    _revision = '2018-01-22'

    def __init__(self):
        super(Rollback, self).__init__()
        self._top_entity = None

        self.yang_name = "rollback"
        self.yang_parent_name = "cisco-ia"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = Rollback.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Rollback.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-ia:rollback"


    class Input(Entity):
        """
        
        
        .. attribute:: target_url
        
        	Cisco IOS XE configuration file that is to  replace the current running configuration
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: verbose
        
        	Display a list of the command lines applied by  the Cisco IOS XE software parser during each pass  of the configuration replace operation. The total  number of passes performed is also displayed
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: nolock
        
        	Disables the locking of the running  configuration file that prevents other users from changing the running configuration  during a configuration replace operation
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: revert_on_error
        
        	Reverts to the original configuration upon error
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: revert_timer
        
        	Reverts to the original configuration if  specified time elapses
        	**type**\: int
        
        	**range:** 1..120
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(Rollback.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "rollback"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('target_url', YLeaf(YType.str, 'target-url')),
                ('verbose', YLeaf(YType.boolean, 'verbose')),
                ('nolock', YLeaf(YType.boolean, 'nolock')),
                ('revert_on_error', YLeaf(YType.empty, 'revert-on-error')),
                ('revert_timer', YLeaf(YType.int16, 'revert-timer')),
            ])
            self.target_url = None
            self.verbose = None
            self.nolock = None
            self.revert_on_error = None
            self.revert_timer = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-ia:rollback/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rollback.Input, ['target_url', 'verbose', 'nolock', 'revert_on_error', 'revert_timer'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\: str
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(Rollback.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "rollback"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('result', YLeaf(YType.str, 'result')),
            ])
            self.result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-ia:rollback/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rollback.Output, ['result'], name, value)

    def clone_ptr(self):
        self._top_entity = Rollback()
        return self._top_entity


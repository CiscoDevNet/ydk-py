""" Cisco_IOS_XR_sysadmin_pm 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

The Process Manager (PM).

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ProcessState(Enum):
    """
    ProcessState (Enum Class)

    .. data:: IDLE = 0

    .. data:: RUNNING = 1

    .. data:: STOPPING = 2

    .. data:: STOPPED = 3

    .. data:: DESELECTING = 4

    .. data:: DESELECTED = 5

    """

    IDLE = Enum.YLeaf(0, "IDLE")

    RUNNING = Enum.YLeaf(1, "RUNNING")

    STOPPING = Enum.YLeaf(2, "STOPPING")

    STOPPED = Enum.YLeaf(3, "STOPPED")

    DESELECTING = Enum.YLeaf(4, "DESELECTING")

    DESELECTED = Enum.YLeaf(5, "DESELECTED")


class ServiceRole(Enum):
    """
    ServiceRole (Enum Class)

    .. data:: NONE = 0

    .. data:: ACTIVE = 1

    .. data:: STANDBY = 2

    """

    NONE = Enum.YLeaf(0, "NONE")

    ACTIVE = Enum.YLeaf(1, "ACTIVE")

    STANDBY = Enum.YLeaf(2, "STANDBY")


class ServiceScope(Enum):
    """
    ServiceScope (Enum Class)

    .. data:: SYSTEM = 0

    .. data:: RACK = 1

    """

    SYSTEM = Enum.YLeaf(0, "SYSTEM")

    RACK = Enum.YLeaf(1, "RACK")


class ServiceState(Enum):
    """
    ServiceState (Enum Class)

    .. data:: SS_IDLE = 0

    .. data:: SS_RUNNING = 1

    .. data:: SS_ACK_PENDING = 2

    """

    SS_IDLE = Enum.YLeaf(0, "SS_IDLE")

    SS_RUNNING = Enum.YLeaf(1, "SS_RUNNING")

    SS_ACK_PENDING = Enum.YLeaf(2, "SS_ACK_PENDING")


class StartupMode(Enum):
    """
    StartupMode (Enum Class)

    .. data:: ON_BOOTUP = 0

    .. data:: ON_SELECTION = 1

    .. data:: ON_DEMAND = 2

    """

    ON_BOOTUP = Enum.YLeaf(0, "ON-BOOTUP")

    ON_SELECTION = Enum.YLeaf(1, "ON-SELECTION")

    ON_DEMAND = Enum.YLeaf(2, "ON-DEMAND")



class Processes(Entity):
    """
    Process Info
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Processes.AllLocations>`
    
    

    """

    _prefix = 'pmh'
    _revision = '2017-04-12'

    def __init__(self):
        super(Processes, self).__init__()
        self._top_entity = None

        self.yang_name = "processes"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-pm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-locations", ("all_locations", Processes.AllLocations))])
        self._leafs = OrderedDict()

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-pm:processes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Processes, [], name, value)


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        .. attribute:: ip_addr
        
        	IP address of the location
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: pcbs
        
        	Total number of process control blocks
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	
        	**type**\: list of  		 :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Processes.AllLocations.Name>`
        
        

        """

        _prefix = 'pmh'
        _revision = '2017-04-12'

        def __init__(self):
            super(Processes.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "processes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("name", ("name", Processes.AllLocations.Name))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str','str'])),
                ('pcbs', (YLeaf(YType.uint32, 'pcbs'), ['int'])),
            ])
            self.location = None
            self.ip_addr = None
            self.pcbs = None

            self.name = YList(self)
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-pm:processes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Processes.AllLocations, ['location', 'ip_addr', 'pcbs'], name, value)


        class Name(Entity):
            """
            
            
            .. attribute:: proc_name  (key)
            
            	Name of the process
            	**type**\: str
            
            .. attribute:: instance_id  (key)
            
            	Instance identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: path
            
            	Process path
            	**type**\: str
            
            .. attribute:: startup_file
            
            	Process startup file
            	**type**\: str
            
            .. attribute:: startup_mode
            
            	When is a process started
            	**type**\:  :py:class:`StartupMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.StartupMode>`
            
            .. attribute:: heart_beat_timeout
            
            	Heart beat timeout in sec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_heart_beat_time
            
            	How long ago last heart beat was detected
            	**type**\: str
            
            .. attribute:: max_restarts
            
            	Maximum num of restarts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: respawn_reset_timer
            
            	Respawn reset timer in min
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mandatory
            
            	Mandatory process
            	**type**\: bool
            
            .. attribute:: maint_mode
            
            	Should run during maintenance mode
            	**type**\: bool
            
            .. attribute:: args
            
            	Process arguments
            	**type**\: str
            
            .. attribute:: proc_state
            
            	State of the process
            	**type**\:  :py:class:`ProcessState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ProcessState>`
            
            .. attribute:: pid
            
            	Process ID
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: proc_aborted
            
            	Whether the processes ever aborted
            	**type**\: bool
            
            .. attribute:: exit_status
            
            	Last exit status/info of the process
            	**type**\: str
            
            .. attribute:: respawns
            
            	Total number of respawns of the process
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: start_time
            
            	Last start date and time
            	**type**\: str
            
            .. attribute:: ready_time
            
            	Time for ready from start\-time
            	**type**\: str
            
            .. attribute:: last_exit_time
            
            	Last exit date and time
            	**type**\: str
            
            .. attribute:: services
            
            	
            	**type**\: list of  		 :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Processes.AllLocations.Name.Services>`
            
            

            """

            _prefix = 'pmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(Processes.AllLocations.Name, self).__init__()

                self.yang_name = "name"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['proc_name','instance_id']
                self._child_classes = OrderedDict([("services", ("services", Processes.AllLocations.Name.Services))])
                self._leafs = OrderedDict([
                    ('proc_name', (YLeaf(YType.str, 'proc-name'), ['str'])),
                    ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                    ('startup_file', (YLeaf(YType.str, 'startup-file'), ['str'])),
                    ('startup_mode', (YLeaf(YType.enumeration, 'startup-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'StartupMode', '')])),
                    ('heart_beat_timeout', (YLeaf(YType.uint32, 'heart-beat-timeout'), ['int'])),
                    ('last_heart_beat_time', (YLeaf(YType.str, 'last-heart-beat-time'), ['str'])),
                    ('max_restarts', (YLeaf(YType.uint32, 'max-restarts'), ['int'])),
                    ('respawn_reset_timer', (YLeaf(YType.uint32, 'respawn-reset-timer'), ['int'])),
                    ('mandatory', (YLeaf(YType.boolean, 'mandatory'), ['bool'])),
                    ('maint_mode', (YLeaf(YType.boolean, 'maint-mode'), ['bool'])),
                    ('args', (YLeaf(YType.str, 'args'), ['str'])),
                    ('proc_state', (YLeaf(YType.enumeration, 'proc-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'ProcessState', '')])),
                    ('pid', (YLeaf(YType.int32, 'pid'), ['int'])),
                    ('proc_aborted', (YLeaf(YType.boolean, 'proc-aborted'), ['bool'])),
                    ('exit_status', (YLeaf(YType.str, 'exit-status'), ['str'])),
                    ('respawns', (YLeaf(YType.int32, 'respawns'), ['int'])),
                    ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                    ('ready_time', (YLeaf(YType.str, 'ready-time'), ['str'])),
                    ('last_exit_time', (YLeaf(YType.str, 'last-exit-time'), ['str'])),
                ])
                self.proc_name = None
                self.instance_id = None
                self.path = None
                self.startup_file = None
                self.startup_mode = None
                self.heart_beat_timeout = None
                self.last_heart_beat_time = None
                self.max_restarts = None
                self.respawn_reset_timer = None
                self.mandatory = None
                self.maint_mode = None
                self.args = None
                self.proc_state = None
                self.pid = None
                self.proc_aborted = None
                self.exit_status = None
                self.respawns = None
                self.start_time = None
                self.ready_time = None
                self.last_exit_time = None

                self.services = YList(self)
                self._segment_path = lambda: "name" + "[proc-name='" + str(self.proc_name) + "']" + "[instance-id='" + str(self.instance_id) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Processes.AllLocations.Name, ['proc_name', 'instance_id', 'path', 'startup_file', 'startup_mode', 'heart_beat_timeout', 'last_heart_beat_time', 'max_restarts', 'respawn_reset_timer', 'mandatory', 'maint_mode', 'args', 'proc_state', 'pid', 'proc_aborted', 'exit_status', 'respawns', 'start_time', 'ready_time', 'last_exit_time'], name, value)


            class Services(Entity):
                """
                
                
                .. attribute:: service_name  (key)
                
                	Name of the service
                	**type**\: str
                
                .. attribute:: scope
                
                	Scope of the service
                	**type**\:  :py:class:`ServiceScope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ServiceScope>`
                
                .. attribute:: redundancy
                
                	Service redundancy support
                	**type**\: bool
                
                .. attribute:: ha_ready
                
                	Standby ready for HA
                	**type**\: bool
                
                .. attribute:: service_state
                
                	State of the service
                	**type**\:  :py:class:`ServiceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ServiceState>`
                
                .. attribute:: ha_role
                
                	Service role
                	**type**\:  :py:class:`ServiceRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ServiceRole>`
                
                .. attribute:: new_ha_role
                
                	New service role, different if PM in process of assigning
                	**type**\:  :py:class:`ServiceRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ServiceRole>`
                
                .. attribute:: selected
                
                	Service seleted to run on the node
                	**type**\: bool
                
                .. attribute:: ip1
                
                	First IP address in the selection
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ip2
                
                	Second IP address in the selection
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: svc_start_time
                
                	Last start date and time
                	**type**\: str
                
                .. attribute:: svc_ready_time
                
                	Time it took to get ready since start time
                	**type**\: str
                
                .. attribute:: svc_haready_time
                
                	Time it took to get HA\-ready since start time
                	**type**\: str
                
                

                """

                _prefix = 'pmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Processes.AllLocations.Name.Services, self).__init__()

                    self.yang_name = "services"
                    self.yang_parent_name = "name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['service_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                        ('scope', (YLeaf(YType.enumeration, 'scope'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'ServiceScope', '')])),
                        ('redundancy', (YLeaf(YType.boolean, 'redundancy'), ['bool'])),
                        ('ha_ready', (YLeaf(YType.boolean, 'ha-ready'), ['bool'])),
                        ('service_state', (YLeaf(YType.enumeration, 'service-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'ServiceState', '')])),
                        ('ha_role', (YLeaf(YType.enumeration, 'ha-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'ServiceRole', '')])),
                        ('new_ha_role', (YLeaf(YType.enumeration, 'new-ha-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm', 'ServiceRole', '')])),
                        ('selected', (YLeaf(YType.boolean, 'selected'), ['bool'])),
                        ('ip1', (YLeaf(YType.str, 'ip1'), ['str','str'])),
                        ('ip2', (YLeaf(YType.str, 'ip2'), ['str','str'])),
                        ('svc_start_time', (YLeaf(YType.str, 'svc-start-time'), ['str'])),
                        ('svc_ready_time', (YLeaf(YType.str, 'svc-ready-time'), ['str'])),
                        ('svc_haready_time', (YLeaf(YType.str, 'svc-haready-time'), ['str'])),
                    ])
                    self.service_name = None
                    self.scope = None
                    self.redundancy = None
                    self.ha_ready = None
                    self.service_state = None
                    self.ha_role = None
                    self.new_ha_role = None
                    self.selected = None
                    self.ip1 = None
                    self.ip2 = None
                    self.svc_start_time = None
                    self.svc_ready_time = None
                    self.svc_haready_time = None
                    self._segment_path = lambda: "services" + "[service-name='" + str(self.service_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Processes.AllLocations.Name.Services, ['service_name', 'scope', 'redundancy', 'ha_ready', 'service_state', 'ha_role', 'new_ha_role', 'selected', 'ip1', 'ip2', 'svc_start_time', 'svc_ready_time', 'svc_haready_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Processes()
        return self._top_entity

class ProcessManager(Entity):
    """
    Process Manager Info
    
    .. attribute:: all_locations_info
    
    	
    	**type**\: list of  		 :py:class:`AllLocationsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.ProcessManager.AllLocationsInfo>`
    
    

    """

    _prefix = 'pmh'
    _revision = '2017-04-12'

    def __init__(self):
        super(ProcessManager, self).__init__()
        self._top_entity = None

        self.yang_name = "process-manager"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-pm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-locations-info", ("all_locations_info", ProcessManager.AllLocationsInfo))])
        self._leafs = OrderedDict()

        self.all_locations_info = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-pm:process-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ProcessManager, [], name, value)


    class AllLocationsInfo(Entity):
        """
        
        
        .. attribute:: location_info  (key)
        
        	
        	**type**\: str
        
        .. attribute:: ip_addr_info
        
        	IP address of the location
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: pm_start_time
        
        	Last start date and time for PM
        	**type**\: str
        
        .. attribute:: mand_proc_down
        
        	PM in mandatory process down state
        	**type**\: bool
        
        .. attribute:: vmm_capi_up
        
        	Status of CAPI with vm\-manager
        	**type**\: bool
        
        .. attribute:: wdmon_capi_up
        
        	Status of CAPI with wdmon
        	**type**\: bool
        
        .. attribute:: wdmon_capi_timestamp
        
        	Date and time of last wdmon CAPI connection establish
        	**type**\: str
        
        .. attribute:: wdmon_num_capi_connects
        
        	Number of times wdmon CAPI connection extablished
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'pmh'
        _revision = '2017-04-12'

        def __init__(self):
            super(ProcessManager.AllLocationsInfo, self).__init__()

            self.yang_name = "all-locations-info"
            self.yang_parent_name = "process-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location_info']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location_info', (YLeaf(YType.str, 'location-info'), ['str'])),
                ('ip_addr_info', (YLeaf(YType.str, 'ip-addr-info'), ['str','str'])),
                ('pm_start_time', (YLeaf(YType.str, 'pm-start-time'), ['str'])),
                ('mand_proc_down', (YLeaf(YType.boolean, 'mand-proc-down'), ['bool'])),
                ('vmm_capi_up', (YLeaf(YType.boolean, 'vmm-capi-up'), ['bool'])),
                ('wdmon_capi_up', (YLeaf(YType.boolean, 'wdmon-capi-up'), ['bool'])),
                ('wdmon_capi_timestamp', (YLeaf(YType.str, 'wdmon-capi-timestamp'), ['str'])),
                ('wdmon_num_capi_connects', (YLeaf(YType.uint32, 'wdmon-num-capi-connects'), ['int'])),
            ])
            self.location_info = None
            self.ip_addr_info = None
            self.pm_start_time = None
            self.mand_proc_down = None
            self.vmm_capi_up = None
            self.wdmon_capi_up = None
            self.wdmon_capi_timestamp = None
            self.wdmon_num_capi_connects = None
            self._segment_path = lambda: "all-locations-info" + "[location-info='" + str(self.location_info) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-pm:process-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessManager.AllLocationsInfo, ['location_info', 'ip_addr_info', 'pm_start_time', 'mand_proc_down', 'vmm_capi_up', 'wdmon_capi_up', 'wdmon_capi_timestamp', 'wdmon_num_capi_connects'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessManager()
        return self._top_entity

class Pm(Entity):
    """
    
    
    .. attribute:: pm
    
    	
    	**type**\:  :py:class:`Pm_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Pm.Pm_>`
    
    

    """

    _prefix = 'pmh'
    _revision = '2017-04-12'

    def __init__(self):
        super(Pm, self).__init__()
        self._top_entity = None

        self.yang_name = "pm"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-pm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("pm", ("pm", Pm.Pm_))])
        self._leafs = OrderedDict()

        self.pm = Pm.Pm_()
        self.pm.parent = self
        self._children_name_map["pm"] = "pm"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-pm:pm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pm, [], name, value)


    class Pm_(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Pm.Pm_.Trace>`
        
        

        """

        _prefix = 'pmh'
        _revision = '2017-04-12'

        def __init__(self):
            super(Pm.Pm_, self).__init__()

            self.yang_name = "pm"
            self.yang_parent_name = "pm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Pm.Pm_.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "pm"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-pm:pm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pm.Pm_, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Pm.Pm_.Trace.Location>`
            
            

            """

            _prefix = 'pmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(Pm.Pm_.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "pm"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Pm.Pm_.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-pm:pm/pm/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pm.Pm_.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Pm.Pm_.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'pmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Pm.Pm_.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Pm.Pm_.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pm.Pm_.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_pm.Pm.Pm_.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'pmh'
                    _revision = '2017-04-12'

                    def __init__(self):
                        super(Pm.Pm_.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Pm.Pm_.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pm.Pm_.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'pmh'
                        _revision = '2017-04-12'

                        def __init__(self):
                            super(Pm.Pm_.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pm.Pm_.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)

    def clone_ptr(self):
        self._top_entity = Pm()
        return self._top_entity


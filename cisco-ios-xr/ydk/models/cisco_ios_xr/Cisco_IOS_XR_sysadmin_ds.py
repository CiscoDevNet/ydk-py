""" Cisco_IOS_XR_sysadmin_ds 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

The Directory Services (DS).

Copyright(c) 2010\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ProcessIssuRole(Enum):
    """
    ProcessIssuRole (Enum Class)

    .. data:: Primary = 1

    .. data:: Secondary = 2

    .. data:: Tertiary = 3

    .. data:: Unknown = 254

    """

    Primary = Enum.YLeaf(1, "Primary")

    Secondary = Enum.YLeaf(2, "Secondary")

    Tertiary = Enum.YLeaf(3, "Tertiary")

    Unknown = Enum.YLeaf(254, "Unknown")


class ProcessRole(Enum):
    """
    ProcessRole (Enum Class)

    .. data:: NoRole = 0

    .. data:: Active = 1

    .. data:: Standby = 2

    .. data:: None_ = 3

    .. data:: Unknown = 254

    """

    NoRole = Enum.YLeaf(0, "NoRole")

    Active = Enum.YLeaf(1, "Active")

    Standby = Enum.YLeaf(2, "Standby")

    None_ = Enum.YLeaf(3, "None")

    Unknown = Enum.YLeaf(254, "Unknown")


class ServiceScope(Enum):
    """
    ServiceScope (Enum Class)

    .. data:: None_ = 0

    .. data:: Rack = 1

    .. data:: System = 2

    .. data:: Node = 3

    """

    None_ = Enum.YLeaf(0, "None")

    Rack = Enum.YLeaf(1, "Rack")

    System = Enum.YLeaf(2, "System")

    Node = Enum.YLeaf(3, "Node")



class Services(Entity):
    """
    Directory Services Entries
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.Services.AllLocations>`
    
    

    """

    _prefix = 'ds'
    _revision = '2017-04-12'

    def __init__(self):
        super(Services, self).__init__()
        self._top_entity = None

        self.yang_name = "services"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-ds"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-locations", ("all_locations", Services.AllLocations))])
        self._leafs = OrderedDict()

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Services, [], name, value)


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	Node Location
        	**type**\: str
        
        .. attribute:: services
        
        	
        	**type**\: list of  		 :py:class:`Services_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.Services.AllLocations.Services_>`
        
        

        """

        _prefix = 'ds'
        _revision = '2017-04-12'

        def __init__(self):
            super(Services.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "services"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("services", ("services", Services.AllLocations.Services_))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.services = YList(self)
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Services.AllLocations, ['location'], name, value)


        class Services_(Entity):
            """
            
            
            .. attribute:: name  (key)
            
            	Name of the service
            	**type**\: str
            
            .. attribute:: endpoint
            
            	endpoint info for a service in DS
            	**type**\: list of  		 :py:class:`Endpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.Services.AllLocations.Services_.Endpoint>`
            
            .. attribute:: registrations
            
            	clients registered for a service in DS
            	**type**\: list of  		 :py:class:`Registrations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.Services.AllLocations.Services_.Registrations>`
            
            

            """

            _prefix = 'ds'
            _revision = '2017-04-12'

            def __init__(self):
                super(Services.AllLocations.Services_, self).__init__()

                self.yang_name = "services"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("endpoint", ("endpoint", Services.AllLocations.Services_.Endpoint)), ("registrations", ("registrations", Services.AllLocations.Services_.Registrations))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.endpoint = YList(self)
                self.registrations = YList(self)
                self._segment_path = lambda: "services" + "[name='" + str(self.name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Services.AllLocations.Services_, ['name'], name, value)


            class Endpoint(Entity):
                """
                endpoint info for a service in DS
                
                .. attribute:: scope
                
                	
                	**type**\:  :py:class:`ServiceScope <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServiceScope>`
                
                .. attribute:: ip
                
                	
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: role
                
                	
                	**type**\:  :py:class:`ProcessRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ProcessRole>`
                
                .. attribute:: issu_role
                
                	
                	**type**\:  :py:class:`ProcessIssuRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ProcessIssuRole>`
                
                .. attribute:: node
                
                	Ethernet address of the node hosting the endpoint
                	**type**\: str
                
                

                """

                _prefix = 'ds'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Services.AllLocations.Services_.Endpoint, self).__init__()

                    self.yang_name = "endpoint"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('scope', (YLeaf(YType.enumeration, 'scope'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds', 'ServiceScope', '')])),
                        ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
                        ('role', (YLeaf(YType.enumeration, 'role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds', 'ProcessRole', '')])),
                        ('issu_role', (YLeaf(YType.enumeration, 'issu_role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds', 'ProcessIssuRole', '')])),
                        ('node', (YLeaf(YType.str, 'node'), ['str'])),
                    ])
                    self.scope = None
                    self.ip = None
                    self.port = None
                    self.role = None
                    self.issu_role = None
                    self.node = None
                    self._segment_path = lambda: "endpoint"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Services.AllLocations.Services_.Endpoint, ['scope', 'ip', 'port', 'role', 'issu_role', 'node'], name, value)


            class Registrations(Entity):
                """
                clients registered for a service in DS
                
                .. attribute:: client
                
                	
                	**type**\: str
                
                .. attribute:: pid
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ds'
                _revision = '2017-04-12'

                def __init__(self):
                    super(Services.AllLocations.Services_.Registrations, self).__init__()

                    self.yang_name = "registrations"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('client', (YLeaf(YType.str, 'client'), ['str'])),
                        ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                    ])
                    self.client = None
                    self.pid = None
                    self._segment_path = lambda: "registrations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Services.AllLocations.Services_.Registrations, ['client', 'pid'], name, value)

    def clone_ptr(self):
        self._top_entity = Services()
        return self._top_entity

class ServicesStats(Entity):
    """
    Directory Services Stats
    
    .. attribute:: ds
    
    	
    	**type**\:  :py:class:`Ds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.Ds>`
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.AllLocations>`
    
    

    """

    _prefix = 'ds'
    _revision = '2017-04-12'

    def __init__(self):
        super(ServicesStats, self).__init__()
        self._top_entity = None

        self.yang_name = "services-stats"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-ds"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ds", ("ds", ServicesStats.Ds)), ("all-locations", ("all_locations", ServicesStats.AllLocations))])
        self._leafs = OrderedDict()

        self.ds = ServicesStats.Ds()
        self.ds.parent = self
        self._children_name_map["ds"] = "ds"

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services-stats"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ServicesStats, [], name, value)


    class Ds(Entity):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.Ds.Trace>`
        
        

        """

        _prefix = 'ds'
        _revision = '2017-04-12'

        def __init__(self):
            super(ServicesStats.Ds, self).__init__()

            self.yang_name = "ds"
            self.yang_parent_name = "services-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", ServicesStats.Ds.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "ds"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services-stats/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ServicesStats.Ds, [], name, value)


        class Trace(Entity):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.Ds.Trace.Location>`
            
            

            """

            _prefix = 'ds'
            _revision = '2017-04-12'

            def __init__(self):
                super(ServicesStats.Ds.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "ds"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", ServicesStats.Ds.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services-stats/ds/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ServicesStats.Ds.Trace, [u'buffer'], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.Ds.Trace.Location.AllOptions>`
                
                

                """

                _prefix = 'ds'
                _revision = '2017-04-12'

                def __init__(self):
                    super(ServicesStats.Ds.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", ServicesStats.Ds.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ServicesStats.Ds.Trace.Location, [u'location_name'], name, value)


                class AllOptions(Entity):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.Ds.Trace.Location.AllOptions.TraceBlocks>`
                    
                    

                    """

                    _prefix = 'ds'
                    _revision = '2017-04-12'

                    def __init__(self):
                        super(ServicesStats.Ds.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", ServicesStats.Ds.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ServicesStats.Ds.Trace.Location.AllOptions, [u'option'], name, value)


                    class TraceBlocks(Entity):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ds'
                        _revision = '2017-04-12'

                        def __init__(self):
                            super(ServicesStats.Ds.Trace.Location.AllOptions.TraceBlocks, self).__init__()

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
                            self._perform_setattr(ServicesStats.Ds.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        .. attribute:: stats
        
        	
        	**type**\: list of  		 :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ds.ServicesStats.AllLocations.Stats>`
        
        

        """

        _prefix = 'ds'
        _revision = '2017-04-12'

        def __init__(self):
            super(ServicesStats.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "services-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("stats", ("stats", ServicesStats.AllLocations.Stats))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.stats = YList(self)
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-ds:services-stats/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ServicesStats.AllLocations, ['location'], name, value)


        class Stats(Entity):
            """
            
            
            .. attribute:: name  (key)
            
            	Name of the service
            	**type**\: str
            
            .. attribute:: published
            
            	number of endpoints published for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: deleted
            
            	number of endpoints deleted for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: modified
            
            	number of endpoints modified for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: registered
            
            	number of clients registered for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: unregistered
            
            	number of clients un\-registered for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: notifications
            
            	number of clients notified for this service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_sent
            
            	number of remote service updates sent to remote nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_recv
            
            	number of remote service received from remote nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ds'
            _revision = '2017-04-12'

            def __init__(self):
                super(ServicesStats.AllLocations.Stats, self).__init__()

                self.yang_name = "stats"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('published', (YLeaf(YType.uint32, 'published'), ['int'])),
                    ('deleted', (YLeaf(YType.uint32, 'deleted'), ['int'])),
                    ('modified', (YLeaf(YType.uint32, 'modified'), ['int'])),
                    ('registered', (YLeaf(YType.uint32, 'registered'), ['int'])),
                    ('unregistered', (YLeaf(YType.uint32, 'unregistered'), ['int'])),
                    ('notifications', (YLeaf(YType.uint32, 'notifications'), ['int'])),
                    ('remote_sent', (YLeaf(YType.uint32, 'remote_sent'), ['int'])),
                    ('remote_recv', (YLeaf(YType.uint32, 'remote_recv'), ['int'])),
                ])
                self.name = None
                self.published = None
                self.deleted = None
                self.modified = None
                self.registered = None
                self.unregistered = None
                self.notifications = None
                self.remote_sent = None
                self.remote_recv = None
                self._segment_path = lambda: "stats" + "[name='" + str(self.name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ServicesStats.AllLocations.Stats, ['name', 'published', 'deleted', 'modified', 'registered', 'unregistered', 'notifications', 'remote_sent', 'remote_recv'], name, value)

    def clone_ptr(self):
        self._top_entity = ServicesStats()
        return self._top_entity


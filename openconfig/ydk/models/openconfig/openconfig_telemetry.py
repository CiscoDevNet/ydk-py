""" openconfig_telemetry 

Data model which creates the configuration for the telemetry
systems and functions on the device.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TelemetryStreamProtocolEnum(Enum):
    """
    TelemetryStreamProtocolEnum

    Selectable protocols for transport

    of the telemetry stream

    .. data:: TCP = 0

    	TCP protocol transport for the stream

    .. data:: UDP = 1

    	UDP protocol transport for the stream

    """

    TCP = 0

    UDP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
        return meta._meta_table['TelemetryStreamProtocolEnum']



class TelemetrySystem(object):
    """
    Top level configuration and state for the
    device's telemetry system.
    
    .. attribute:: destination_groups
    
    	Top level container for destination group configuration and state
    	**type**\:   :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups>`
    
    .. attribute:: sensor_groups
    
    	Top level container for sensor\-groups
    	**type**\:   :py:class:`SensorGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	This container holds information for both persistent and dynamic telemetry subscriptions
    	**type**\:   :py:class:`Subscriptions <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions>`
    
    

    """

    _prefix = 'oc-telemetry'
    _revision = '2016-02-04'

    def __init__(self):
        self.destination_groups = TelemetrySystem.DestinationGroups()
        self.destination_groups.parent = self
        self.sensor_groups = TelemetrySystem.SensorGroups()
        self.sensor_groups.parent = self
        self.subscriptions = TelemetrySystem.Subscriptions()
        self.subscriptions.parent = self


    class SensorGroups(object):
        """
        Top level container for sensor\-groups.
        
        .. attribute:: sensor_group
        
        	List of telemetry sensory groups on the local system, where a sensor grouping represents a resuable grouping of multiple paths and exclude filters
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            self.parent = None
            self.sensor_group = YList()
            self.sensor_group.parent = self
            self.sensor_group.name = 'sensor_group'


        class SensorGroup(object):
            """
            List of telemetry sensory groups on the local
            system, where a sensor grouping represents a resuable
            grouping of multiple paths and exclude filters.
            
            .. attribute:: sensor_group_id  <key>
            
            	Reference to the name or identifier of the sensor grouping
            	**type**\:  str
            
            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: config
            
            	Configuration parameters relating to the telemetry sensor grouping
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: sensor_paths
            
            	Top level container to hold a set of sensor paths grouped together
            	**type**\:   :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths>`
            
            .. attribute:: state
            
            	State information relating to the telemetry sensor group
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.State>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                self.parent = None
                self.sensor_group_id = None
                self.config = TelemetrySystem.SensorGroups.SensorGroup.Config()
                self.config.parent = self
                self.sensor_paths = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self
                self.state = TelemetrySystem.SensorGroups.SensorGroup.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration parameters relating to the
                telemetry sensor grouping
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.sensor_group_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sensor_group_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.Config']['meta_info']


            class State(object):
                """
                State information relating to the telemetry
                sensor group
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.sensor_group_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.sensor_group_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.State']['meta_info']


            class SensorPaths(object):
                """
                Top level container to hold a set of sensor
                paths grouped together
                
                .. attribute:: sensor_path
                
                	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                	**type**\: list of    :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.sensor_path = YList()
                    self.sensor_path.parent = self
                    self.sensor_path.name = 'sensor_path'


                class SensorPath(object):
                    """
                    List of paths in the model which together
                    comprise a sensor grouping. Filters for each path
                    to exclude items are also provided.
                    
                    .. attribute:: path  <key>
                    
                    	Reference to the path of interest
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: state
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.path = None
                        self.config = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config()
                        self.config.parent = self
                        self.state = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\:  str
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.exclude_filter = None
                            self.path = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-telemetry:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.exclude_filter is not None:
                                return True

                            if self.path is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config']['meta_info']


                    class State(object):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\:  str
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.exclude_filter = None
                            self.path = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-telemetry:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.exclude_filter is not None:
                                return True

                            if self.path is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.path is None:
                            raise YPYModelError('Key property path is None')

                        return self.parent._common_path +'/openconfig-telemetry:sensor-path[openconfig-telemetry:path = ' + str(self.path) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.path is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:sensor-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sensor_path is not None:
                        for child_ref in self.sensor_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup.SensorPaths']['meta_info']

            @property
            def _common_path(self):
                if self.sensor_group_id is None:
                    raise YPYModelError('Key property sensor_group_id is None')

                return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:sensor-groups/openconfig-telemetry:sensor-group[openconfig-telemetry:sensor-group-id = ' + str(self.sensor_group_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.sensor_group_id is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.sensor_paths is not None and self.sensor_paths._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                return meta._meta_table['TelemetrySystem.SensorGroups.SensorGroup']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:sensor-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.sensor_group is not None:
                for child_ref in self.sensor_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
            return meta._meta_table['TelemetrySystem.SensorGroups']['meta_info']


    class DestinationGroups(object):
        """
        Top level container for destination group configuration
        and state.
        
        .. attribute:: destination_group
        
        	List of destination\-groups. Destination groups allow the reuse of common telemetry destinations across the telemetry configuration. An operator references a set of destinations via the configurable destination\-group\-identifier.  A destination group may contain one or more telemetry destinations
        	**type**\: list of    :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            self.parent = None
            self.destination_group = YList()
            self.destination_group.parent = self
            self.destination_group.name = 'destination_group'


        class DestinationGroup(object):
            """
            List of destination\-groups. Destination groups allow the
            reuse of common telemetry destinations across the
            telemetry configuration. An operator references a
            set of destinations via the configurable
            destination\-group\-identifier.
            
            A destination group may contain one or more telemetry
            destinations
            
            .. attribute:: group_id  <key>
            
            	Unique identifier for the destination group
            	**type**\:  str
            
            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: config
            
            	Top level config container for destination groups
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: destinations
            
            	The destination container lists the destination information such as IP address and port of the telemetry messages from the network element
            	**type**\:   :py:class:`Destinations <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations>`
            
            .. attribute:: state
            
            	Top level state container for destination groups
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.State>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                self.parent = None
                self.group_id = None
                self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Config()
                self.config.parent = self
                self.destinations = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations()
                self.destinations.parent = self
                self.state = TelemetrySystem.DestinationGroups.DestinationGroup.State()
                self.state.parent = self


            class Config(object):
                """
                Top level config container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for the destination group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.group_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Config']['meta_info']


            class State(object):
                """
                Top level state container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for destination group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.group_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.State']['meta_info']


            class Destinations(object):
                """
                The destination container lists the destination
                information such as IP address and port of the
                telemetry messages from the network element.
                
                .. attribute:: destination
                
                	List of telemetry stream destinations
                	**type**\: list of    :py:class:`Destination <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.destination = YList()
                    self.destination.parent = self
                    self.destination.name = 'destination'


                class Destination(object):
                    """
                    List of telemetry stream destinations
                    
                    .. attribute:: destination_address  <key>
                    
                    	Reference to the destination address of the telemetry stream
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: destination_port  <key>
                    
                    	Reference to the port number of the stream destination
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`destination_port <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to telemetry destinations
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with telemetry destinations
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.destination_address = None
                        self.destination_port = None
                        self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config()
                        self.config.parent = self
                        self.state = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:   :py:class:`TelemetryStreamProtocolEnum <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocolEnum>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.destination_address = None
                            self.destination_port = None
                            self.destination_protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-telemetry:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.destination_address is not None:
                                return True

                            if self.destination_port is not None:
                                return True

                            if self.destination_protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config']['meta_info']


                    class State(object):
                        """
                        State information associated with
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:   :py:class:`TelemetryStreamProtocolEnum <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocolEnum>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.destination_address = None
                            self.destination_port = None
                            self.destination_protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-telemetry:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.destination_address is not None:
                                return True

                            if self.destination_port is not None:
                                return True

                            if self.destination_protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.destination_address is None:
                            raise YPYModelError('Key property destination_address is None')
                        if self.destination_port is None:
                            raise YPYModelError('Key property destination_port is None')

                        return self.parent._common_path +'/openconfig-telemetry:destination[openconfig-telemetry:destination-address = ' + str(self.destination_address) + '][openconfig-telemetry:destination-port = ' + str(self.destination_port) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.destination_address is not None:
                            return True

                        if self.destination_port is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-telemetry:destinations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.destination is not None:
                        for child_ref in self.destination:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup.Destinations']['meta_info']

            @property
            def _common_path(self):
                if self.group_id is None:
                    raise YPYModelError('Key property group_id is None')

                return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:destination-groups/openconfig-telemetry:destination-group[openconfig-telemetry:group-id = ' + str(self.group_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.group_id is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.destinations is not None and self.destinations._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                return meta._meta_table['TelemetrySystem.DestinationGroups.DestinationGroup']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:destination-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.destination_group is not None:
                for child_ref in self.destination_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
            return meta._meta_table['TelemetrySystem.DestinationGroups']['meta_info']


    class Subscriptions(object):
        """
        This container holds information for both persistent
        and dynamic telemetry subscriptions.
        
        .. attribute:: dynamic
        
        	This container holds information relating to dynamic telemetry subscriptions. A dynamic subscription is typically configured through an RPC channel, and does not persist across device restarts, or if the RPC channel is reset or otherwise torn down
        	**type**\:   :py:class:`Dynamic <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic>`
        
        .. attribute:: persistent
        
        	This container holds information relating to persistent telemetry subscriptions. A persistent telemetry subscription is configued locally on the device through configuration, and is persistent across device restarts or other redundancy changes
        	**type**\:   :py:class:`Persistent <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            self.parent = None
            self.dynamic = TelemetrySystem.Subscriptions.Dynamic()
            self.dynamic.parent = self
            self.persistent = TelemetrySystem.Subscriptions.Persistent()
            self.persistent.parent = self


        class Persistent(object):
            """
            This container holds information relating to persistent
            telemetry subscriptions. A persistent telemetry
            subscription is configued locally on the device through
            configuration, and is persistent across device restarts or
            other redundancy changes.
            
            .. attribute:: subscription
            
            	List of telemetry subscriptions. A telemetry subscription consists of a set of collection destinations, stream attributes, and associated paths to state information in the model (sensor data)
            	**type**\: list of    :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                self.parent = None
                self.subscription = YList()
                self.subscription.parent = self
                self.subscription.name = 'subscription'


            class Subscription(object):
                """
                List of telemetry subscriptions. A telemetry
                subscription consists of a set of collection
                destinations, stream attributes, and associated paths to
                state information in the model (sensor data)
                
                .. attribute:: subscription_id  <key>
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: config
                
                	Config parameters relating to the telemetry subscriptions on the local device
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: destination_groups
                
                	A subscription may specify destination addresses. If the subscription supplies destination addresses, the network element will be the initiator of the telemetry streaming, sending it to the destination(s) specified.  If the destination set is omitted, the subscription preconfigures certain elements such as paths and sample intervals under a specified subscription ID. In this case, the network element will NOT initiate an outbound connection for telemetry, but will wait for an inbound connection from a network management system.  It is expected that the network management system connecting to the network element will reference the preconfigured subscription ID when initiating a subscription
                	**type**\:   :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups>`
                
                .. attribute:: sensor_profiles
                
                	A sensor profile is a set of sensor groups or individual sensor paths which are associated with a telemetry subscription. This is the source of the telemetry data for the subscription to send to the defined collectors
                	**type**\:   :py:class:`SensorProfiles <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles>`
                
                .. attribute:: state
                
                	State parameters relating to the telemetry subscriptions on the local device
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.State>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.subscription_id = None
                    self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.Config()
                    self.config.parent = self
                    self.destination_groups = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups()
                    self.destination_groups.parent = self
                    self.sensor_profiles = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles()
                    self.sensor_profiles.parent = self
                    self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Config parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.local_source_address = None
                        self.originated_qos_marking = None
                        self.subscription_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.local_source_address is not None:
                            return True

                        if self.originated_qos_marking is not None:
                            return True

                        if self.subscription_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.Config']['meta_info']


                class State(object):
                    """
                    State parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.local_source_address = None
                        self.originated_qos_marking = None
                        self.subscription_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.local_source_address is not None:
                            return True

                        if self.originated_qos_marking is not None:
                            return True

                        if self.subscription_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.State']['meta_info']


                class SensorProfiles(object):
                    """
                    A sensor profile is a set of sensor groups or
                    individual sensor paths which are associated with a
                    telemetry subscription. This is the source of the
                    telemetry data for the subscription to send to the
                    defined collectors.
                    
                    .. attribute:: sensor_profile
                    
                    	List of telemetry sensor groups used in the subscription
                    	**type**\: list of    :py:class:`SensorProfile <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.sensor_profile = YList()
                        self.sensor_profile.parent = self
                        self.sensor_profile.name = 'sensor_profile'


                    class SensorProfile(object):
                        """
                        List of telemetry sensor groups used
                        in the subscription
                        
                        .. attribute:: sensor_group  <key>
                        
                        	Reference to the telemetry sensor group name
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`sensor_group <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to the sensor profile for a subscription
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the sensor profile for a subscription
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.sensor_group = None
                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config()
                            self.config.parent = self
                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters related to the sensor
                            profile for a subscription
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                self.parent = None
                                self.heartbeat_interval = None
                                self.sample_interval = None
                                self.sensor_group = None
                                self.suppress_redundant = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-telemetry:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.heartbeat_interval is not None:
                                    return True

                                if self.sample_interval is not None:
                                    return True

                                if self.sensor_group is not None:
                                    return True

                                if self.suppress_redundant is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                                return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config']['meta_info']


                        class State(object):
                            """
                            State information relating to the sensor profile
                            for a subscription
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                self.parent = None
                                self.heartbeat_interval = None
                                self.sample_interval = None
                                self.sensor_group = None
                                self.suppress_redundant = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-telemetry:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.heartbeat_interval is not None:
                                    return True

                                if self.sample_interval is not None:
                                    return True

                                if self.sensor_group is not None:
                                    return True

                                if self.suppress_redundant is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                                return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sensor_group is None:
                                raise YPYModelError('Key property sensor_group is None')

                            return self.parent._common_path +'/openconfig-telemetry:sensor-profile[openconfig-telemetry:sensor-group = ' + str(self.sensor_group) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.sensor_group is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:sensor-profiles'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sensor_profile is not None:
                            for child_ref in self.sensor_profile:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles']['meta_info']


                class DestinationGroups(object):
                    """
                    A subscription may specify destination addresses.
                    If the subscription supplies destination addresses,
                    the network element will be the initiator of the
                    telemetry streaming, sending it to the destination(s)
                    specified.
                    
                    If the destination set is omitted, the subscription
                    preconfigures certain elements such as paths and
                    sample intervals under a specified subscription ID.
                    In this case, the network element will NOT initiate an
                    outbound connection for telemetry, but will wait for
                    an inbound connection from a network management
                    system.
                    
                    It is expected that the network management system
                    connecting to the network element will reference
                    the preconfigured subscription ID when initiating
                    a subscription.
                    
                    .. attribute:: destination_group
                    
                    	Identifier of the previously defined destination group
                    	**type**\: list of    :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.destination_group = YList()
                        self.destination_group.parent = self
                        self.destination_group.name = 'destination_group'


                    class DestinationGroup(object):
                        """
                        Identifier of the previously defined destination
                        group
                        
                        .. attribute:: group_id  <key>
                        
                        	The destination group id references a configured group of destinations for the telemetry stream
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to telemetry destinations
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: state
                        
                        	State information related to telemetry destinations
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.group_id = None
                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config()
                            self.config.parent = self
                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters related to telemetry
                            destinations.
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                self.parent = None
                                self.group_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-telemetry:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                                return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config']['meta_info']


                        class State(object):
                            """
                            State information related to telemetry
                            destinations
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                self.parent = None
                                self.group_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-telemetry:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                                return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_id is None:
                                raise YPYModelError('Key property group_id is None')

                            return self.parent._common_path +'/openconfig-telemetry:destination-group[openconfig-telemetry:group-id = ' + str(self.group_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_id is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:destination-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.destination_group is not None:
                            for child_ref in self.destination_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups']['meta_info']

                @property
                def _common_path(self):
                    if self.subscription_id is None:
                        raise YPYModelError('Key property subscription_id is None')

                    return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:subscriptions/openconfig-telemetry:persistent/openconfig-telemetry:subscription[openconfig-telemetry:subscription-id = ' + str(self.subscription_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.subscription_id is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.destination_groups is not None and self.destination_groups._has_data():
                        return True

                    if self.sensor_profiles is not None and self.sensor_profiles._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.Subscriptions.Persistent.Subscription']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:subscriptions/openconfig-telemetry:persistent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subscription is not None:
                    for child_ref in self.subscription:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                return meta._meta_table['TelemetrySystem.Subscriptions.Persistent']['meta_info']


        class Dynamic(object):
            """
            This container holds information relating to dynamic
            telemetry subscriptions. A dynamic subscription is
            typically configured through an RPC channel, and does not
            persist across device restarts, or if the RPC channel is
            reset or otherwise torn down.
            
            .. attribute:: subscription
            
            	List representation of telemetry subscriptions that are configured via an inline RPC, otherwise known as dynamic telemetry subscriptions
            	**type**\: list of    :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                self.parent = None
                self.subscription = YList()
                self.subscription.parent = self
                self.subscription.name = 'subscription'


            class Subscription(object):
                """
                List representation of telemetry subscriptions that
                are configured via an inline RPC, otherwise known
                as dynamic telemetry subscriptions.
                
                .. attribute:: subscription_id  <key>
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                .. attribute:: sensor_paths
                
                	Top level container to hold a set of sensor paths grouped together
                	**type**\:   :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths>`
                
                .. attribute:: state
                
                	State information relating to dynamic telemetry subscriptions
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    self.parent = None
                    self.subscription_id = None
                    self.sensor_paths = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths()
                    self.sensor_paths.parent = self
                    self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.State()
                    self.state.parent = self


                class State(object):
                    """
                    State information relating to dynamic telemetry
                    subscriptions.
                    
                    .. attribute:: destination_address
                    
                    	IP address of the telemetry stream destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: destination_port
                    
                    	Protocol (udp or tcp) port number for the telemetry stream destination
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_protocol
                    
                    	Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`TelemetryStreamProtocolEnum <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocolEnum>`
                    
                    .. attribute:: heartbeat_interval
                    
                    	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: sample_interval
                    
                    	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: suppress_redundant
                    
                    	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.destination_address = None
                        self.destination_port = None
                        self.destination_protocol = None
                        self.heartbeat_interval = None
                        self.originated_qos_marking = None
                        self.sample_interval = None
                        self.subscription_id = None
                        self.suppress_redundant = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.destination_address is not None:
                            return True

                        if self.destination_port is not None:
                            return True

                        if self.destination_protocol is not None:
                            return True

                        if self.heartbeat_interval is not None:
                            return True

                        if self.originated_qos_marking is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.subscription_id is not None:
                            return True

                        if self.suppress_redundant is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.State']['meta_info']


                class SensorPaths(object):
                    """
                    Top level container to hold a set of sensor
                    paths grouped together
                    
                    .. attribute:: sensor_path
                    
                    	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                    	**type**\: list of    :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        self.parent = None
                        self.sensor_path = YList()
                        self.sensor_path.parent = self
                        self.sensor_path.name = 'sensor_path'


                    class SensorPath(object):
                        """
                        List of paths in the model which together
                        comprise a sensor grouping. Filters for each path
                        to exclude items are also provided.
                        
                        .. attribute:: path  <key>
                        
                        	Reference to the path of interest
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        .. attribute:: state
                        
                        	State information for a dynamic subscription's paths of interest
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            self.parent = None
                            self.path = None
                            self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State()
                            self.state.parent = self


                        class State(object):
                            """
                            State information for a dynamic subscription's
                            paths of interest
                            
                            .. attribute:: exclude_filter
                            
                            	Filter to exclude certain values out of the state values
                            	**type**\:  str
                            
                            .. attribute:: path
                            
                            	Path to a section of operational state of interest (the sensor)
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                self.parent = None
                                self.exclude_filter = None
                                self.path = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-telemetry:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.exclude_filter is not None:
                                    return True

                                if self.path is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                                return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.path is None:
                                raise YPYModelError('Key property path is None')

                            return self.parent._common_path +'/openconfig-telemetry:sensor-path[openconfig-telemetry:path = ' + str(self.path) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.path is not None:
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                            return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-telemetry:sensor-paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sensor_path is not None:
                            for child_ref in self.sensor_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                        return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths']['meta_info']

                @property
                def _common_path(self):
                    if self.subscription_id is None:
                        raise YPYModelError('Key property subscription_id is None')

                    return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:subscriptions/openconfig-telemetry:dynamic/openconfig-telemetry:subscription[openconfig-telemetry:subscription-id = ' + str(self.subscription_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.subscription_id is not None:
                        return True

                    if self.sensor_paths is not None and self.sensor_paths._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                    return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic.Subscription']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:subscriptions/openconfig-telemetry:dynamic'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subscription is not None:
                    for child_ref in self.subscription:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_telemetry as meta
                return meta._meta_table['TelemetrySystem.Subscriptions.Dynamic']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-telemetry:telemetry-system/openconfig-telemetry:subscriptions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.dynamic is not None and self.dynamic._has_data():
                return True

            if self.persistent is not None and self.persistent._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_telemetry as meta
            return meta._meta_table['TelemetrySystem.Subscriptions']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-telemetry:telemetry-system'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.destination_groups is not None and self.destination_groups._has_data():
            return True

        if self.sensor_groups is not None and self.sensor_groups._has_data():
            return True

        if self.subscriptions is not None and self.subscriptions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_telemetry as meta
        return meta._meta_table['TelemetrySystem']['meta_info']



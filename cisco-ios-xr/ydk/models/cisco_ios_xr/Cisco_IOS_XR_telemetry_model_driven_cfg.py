""" Cisco_IOS_XR_telemetry_model_driven_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package configuration.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Model Driven Telemetry configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EncodeTypeEnum(Enum):
    """
    EncodeTypeEnum

    Encode type

    .. data:: gpb = 2

    	GPB

    .. data:: self_describing_gpb = 3

    	SELF DESCRIBING GPB

    """

    gpb = 2

    self_describing_gpb = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
        return meta._meta_table['EncodeTypeEnum']


class ProtoTypeEnum(Enum):
    """
    ProtoTypeEnum

    Proto type

    .. data:: grpc = 1

    	GRPC

    .. data:: tcp = 2

    	tcp

    """

    grpc = 1

    tcp = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
        return meta._meta_table['ProtoTypeEnum']



class TelemetryModelDriven(object):
    """
    Model Driven Telemetry configuration
    
    .. attribute:: destination_groups
    
    	Destination Group configuration
    	**type**\:   :py:class:`DestinationGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups>`
    
    .. attribute:: enable
    
    	Enable Model Driven Telemetry
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: sensor_groups
    
    	Sensor group configuration
    	**type**\:   :py:class:`SensorGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	Streaming Telemetry Subscription
    	**type**\:   :py:class:`Subscriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions>`
    
    

    """

    _prefix = 'telemetry-model-driven-cfg'
    _revision = '2016-10-20'

    def __init__(self):
        self.destination_groups = TelemetryModelDriven.DestinationGroups()
        self.destination_groups.parent = self
        self.enable = None
        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self


    class SensorGroups(object):
        """
        Sensor group configuration
        
        .. attribute:: sensor_group
        
        	Sensor group configuration
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2016-10-20'

        def __init__(self):
            self.parent = None
            self.sensor_group = YList()
            self.sensor_group.parent = self
            self.sensor_group.name = 'sensor_group'


        class SensorGroup(object):
            """
            Sensor group configuration
            
            .. attribute:: sensor_group_identifier  <key>
            
            	The identifier for this group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: sensor_paths
            
            	Sensor path configuration
            	**type**\:   :py:class:`SensorPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2016-10-20'

            def __init__(self):
                self.parent = None
                self.sensor_group_identifier = None
                self.sensor_paths = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self


            class SensorPaths(object):
                """
                Sensor path configuration
                
                .. attribute:: sensor_path
                
                	Sensor path configuration
                	**type**\: list of    :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2016-10-20'

                def __init__(self):
                    self.parent = None
                    self.sensor_path = YList()
                    self.sensor_path.parent = self
                    self.sensor_path.name = 'sensor_path'


                class SensorPath(object):
                    """
                    Sensor path configuration
                    
                    .. attribute:: telemetry_sensor_path  <key>
                    
                    	Sensor Path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2016-10-20'

                    def __init__(self):
                        self.parent = None
                        self.telemetry_sensor_path = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.telemetry_sensor_path is None:
                            raise YPYModelError('Key property telemetry_sensor_path is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-path[Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-sensor-path = ' + str(self.telemetry_sensor_path) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.telemetry_sensor_path is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                        return meta._meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-paths'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                    return meta._meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths']['meta_info']

            @property
            def _common_path(self):
                if self.sensor_group_identifier is None:
                    raise YPYModelError('Key property sensor_group_identifier is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-groups/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-group[Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-group-identifier = ' + str(self.sensor_group_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.sensor_group_identifier is not None:
                    return True

                if self.sensor_paths is not None and self.sensor_paths._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                return meta._meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-groups'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
            return meta._meta_table['TelemetryModelDriven.SensorGroups']['meta_info']


    class Subscriptions(object):
        """
        Streaming Telemetry Subscription
        
        .. attribute:: subscription
        
        	Streaming Telemetry Subscription
        	**type**\: list of    :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2016-10-20'

        def __init__(self):
            self.parent = None
            self.subscription = YList()
            self.subscription.parent = self
            self.subscription.name = 'subscription'


        class Subscription(object):
            """
            Streaming Telemetry Subscription
            
            .. attribute:: subscription_identifier  <key>
            
            	Subscription identifier string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: destination_profiles
            
            	Associate Destination Groups with Subscription
            	**type**\:   :py:class:`DestinationProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles>`
            
            .. attribute:: sensor_profiles
            
            	Associate Sensor Groups with Subscription
            	**type**\:   :py:class:`SensorProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2016-10-20'

            def __init__(self):
                self.parent = None
                self.subscription_identifier = None
                self.destination_profiles = TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles()
                self.destination_profiles.parent = self
                self.sensor_profiles = TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles()
                self.sensor_profiles.parent = self


            class SensorProfiles(object):
                """
                Associate Sensor Groups with Subscription
                
                .. attribute:: sensor_profile
                
                	Associate Sensor Group with Subscription
                	**type**\: list of    :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2016-10-20'

                def __init__(self):
                    self.parent = None
                    self.sensor_profile = YList()
                    self.sensor_profile.parent = self
                    self.sensor_profile.name = 'sensor_profile'


                class SensorProfile(object):
                    """
                    Associate Sensor Group with Subscription
                    
                    .. attribute:: sensorgroupid  <key>
                    
                    	Reference to the telemetry sensor group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: sample_interval
                    
                    	Sample interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2016-10-20'

                    def __init__(self):
                        self.parent = None
                        self.sensorgroupid = None
                        self.sample_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.sensorgroupid is None:
                            raise YPYModelError('Key property sensorgroupid is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-profile[Cisco-IOS-XR-telemetry-model-driven-cfg:sensorgroupid = ' + str(self.sensorgroupid) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sensorgroupid is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:sensor-profiles'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                    return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles']['meta_info']


            class DestinationProfiles(object):
                """
                Associate Destination Groups with Subscription
                
                .. attribute:: destination_profile
                
                	Associate Destination Group with Subscription
                	**type**\: list of    :py:class:`DestinationProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2016-10-20'

                def __init__(self):
                    self.parent = None
                    self.destination_profile = YList()
                    self.destination_profile.parent = self
                    self.destination_profile.name = 'destination_profile'


                class DestinationProfile(object):
                    """
                    Associate Destination Group with Subscription
                    
                    .. attribute:: destination_id  <key>
                    
                    	Destination Id to associate with Subscription
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2016-10-20'

                    def __init__(self):
                        self.parent = None
                        self.destination_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.destination_id is None:
                            raise YPYModelError('Key property destination_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:destination-profile[Cisco-IOS-XR-telemetry-model-driven-cfg:destination-id = ' + str(self.destination_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.destination_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:destination-profiles'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.destination_profile is not None:
                        for child_ref in self.destination_profile:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                    return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles']['meta_info']

            @property
            def _common_path(self):
                if self.subscription_identifier is None:
                    raise YPYModelError('Key property subscription_identifier is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:subscriptions/Cisco-IOS-XR-telemetry-model-driven-cfg:subscription[Cisco-IOS-XR-telemetry-model-driven-cfg:subscription-identifier = ' + str(self.subscription_identifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subscription_identifier is not None:
                    return True

                if self.destination_profiles is not None and self.destination_profiles._has_data():
                    return True

                if self.sensor_profiles is not None and self.sensor_profiles._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:subscriptions'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
            return meta._meta_table['TelemetryModelDriven.Subscriptions']['meta_info']


    class DestinationGroups(object):
        """
        Destination Group configuration
        
        .. attribute:: destination_group
        
        	Destination Group
        	**type**\: list of    :py:class:`DestinationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2016-10-20'

        def __init__(self):
            self.parent = None
            self.destination_group = YList()
            self.destination_group.parent = self
            self.destination_group.name = 'destination_group'


        class DestinationGroup(object):
            """
            Destination Group
            
            .. attribute:: destination_id  <key>
            
            	destination group id string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_destinations
            
            	Destination address configuration
            	**type**\:   :py:class:`Ipv4Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations>`
            
            .. attribute:: ipv6_destinations
            
            	Destination address configuration
            	**type**\:   :py:class:`Ipv6Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2016-10-20'

            def __init__(self):
                self.parent = None
                self.destination_id = None
                self.ipv4_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations()
                self.ipv4_destinations.parent = self
                self.ipv6_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations()
                self.ipv6_destinations.parent = self


            class Ipv6Destinations(object):
                """
                Destination address configuration
                
                .. attribute:: ipv6_destination
                
                	destination IP address
                	**type**\: list of    :py:class:`Ipv6Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2016-10-20'

                def __init__(self):
                    self.parent = None
                    self.ipv6_destination = YList()
                    self.ipv6_destination.parent = self
                    self.ipv6_destination.name = 'ipv6_destination'


                class Ipv6Destination(object):
                    """
                    destination IP address
                    
                    .. attribute:: ipv6_address  <key>
                    
                    	Destination IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  <key>
                    
                    	destination port
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`EncodeTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeTypeEnum>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2016-10-20'

                    def __init__(self):
                        self.parent = None
                        self.ipv6_address = None
                        self.destination_port = None
                        self.encoding = None
                        self.protocol = None


                    class Protocol(object):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:   :py:class:`ProtoTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoTypeEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\:  str
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2016-10-20'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.no_tls = None
                            self.protocol = None
                            self.tls_hostname = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:protocol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.no_tls is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            if self.tls_hostname is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                            return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ipv6_address is None:
                            raise YPYModelError('Key property ipv6_address is None')
                        if self.destination_port is None:
                            raise YPYModelError('Key property destination_port is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:ipv6-destination[Cisco-IOS-XR-telemetry-model-driven-cfg:ipv6-address = ' + str(self.ipv6_address) + '][Cisco-IOS-XR-telemetry-model-driven-cfg:destination-port = ' + str(self.destination_port) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv6_address is not None:
                            return True

                        if self.destination_port is not None:
                            return True

                        if self.encoding is not None:
                            return True

                        if self.protocol is not None and self.protocol._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                        return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:ipv6-destinations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv6_destination is not None:
                        for child_ref in self.ipv6_destination:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                    return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations']['meta_info']


            class Ipv4Destinations(object):
                """
                Destination address configuration
                
                .. attribute:: ipv4_destination
                
                	destination IP address
                	**type**\: list of    :py:class:`Ipv4Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2016-10-20'

                def __init__(self):
                    self.parent = None
                    self.ipv4_destination = YList()
                    self.ipv4_destination.parent = self
                    self.ipv4_destination.name = 'ipv4_destination'


                class Ipv4Destination(object):
                    """
                    destination IP address
                    
                    .. attribute:: ipv4_address  <key>
                    
                    	Destination IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  <key>
                    
                    	destination port
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`EncodeTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeTypeEnum>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2016-10-20'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_address = None
                        self.destination_port = None
                        self.encoding = None
                        self.protocol = None


                    class Protocol(object):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:   :py:class:`ProtoTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoTypeEnum>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\:  str
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2016-10-20'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.no_tls = None
                            self.protocol = None
                            self.tls_hostname = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:protocol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.no_tls is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            if self.tls_hostname is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                            return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ipv4_address is None:
                            raise YPYModelError('Key property ipv4_address is None')
                        if self.destination_port is None:
                            raise YPYModelError('Key property destination_port is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:ipv4-destination[Cisco-IOS-XR-telemetry-model-driven-cfg:ipv4-address = ' + str(self.ipv4_address) + '][Cisco-IOS-XR-telemetry-model-driven-cfg:destination-port = ' + str(self.destination_port) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4_address is not None:
                            return True

                        if self.destination_port is not None:
                            return True

                        if self.encoding is not None:
                            return True

                        if self.protocol is not None and self.protocol._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                        return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-cfg:ipv4-destinations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipv4_destination is not None:
                        for child_ref in self.ipv4_destination:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                    return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations']['meta_info']

            @property
            def _common_path(self):
                if self.destination_id is None:
                    raise YPYModelError('Key property destination_id is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:destination-groups/Cisco-IOS-XR-telemetry-model-driven-cfg:destination-group[Cisco-IOS-XR-telemetry-model-driven-cfg:destination-id = ' + str(self.destination_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.destination_id is not None:
                    return True

                if self.ipv4_destinations is not None and self.ipv4_destinations._has_data():
                    return True

                if self.ipv6_destinations is not None and self.ipv6_destinations._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
                return meta._meta_table['TelemetryModelDriven.DestinationGroups.DestinationGroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-cfg:destination-groups'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
            return meta._meta_table['TelemetryModelDriven.DestinationGroups']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.destination_groups is not None and self.destination_groups._has_data():
            return True

        if self.enable is not None:
            return True

        if self.sensor_groups is not None and self.sensor_groups._has_data():
            return True

        if self.subscriptions is not None and self.subscriptions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_cfg as meta
        return meta._meta_table['TelemetryModelDriven']['meta_info']



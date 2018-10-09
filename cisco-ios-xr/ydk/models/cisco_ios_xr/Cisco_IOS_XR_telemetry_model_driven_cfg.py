""" Cisco_IOS_XR_telemetry_model_driven_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package configuration.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Model Driven Telemetry configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EncodeType(Enum):
    """
    EncodeType (Enum Class)

    Encode type

    .. data:: gpb = 2

    	GPB

    .. data:: self_describing_gpb = 3

    	SELF DESCRIBING GPB

    .. data:: json = 4

    	JSON

    """

    gpb = Enum.YLeaf(2, "gpb")

    self_describing_gpb = Enum.YLeaf(3, "self-describing-gpb")

    json = Enum.YLeaf(4, "json")


class MdtDscpValue(Enum):
    """
    MdtDscpValue (Enum Class)

    Mdt dscp value

    .. data:: default = 0

    	Applicable to DSCP: bits 000000

    .. data:: cs1 = 8

    	Applicable to DSCP: bits 001000

    .. data:: af11 = 10

    	Applicable to DSCP: bits 001010

    .. data:: af12 = 12

    	Applicable to DSCP: bits 001100

    .. data:: af13 = 14

    	Applicable to DSCP: bits 001110

    .. data:: cs2 = 16

    	Applicable to DSCP: bits 010000

    .. data:: af21 = 18

    	Applicable to DSCP: bits 010010

    .. data:: af22 = 20

    	Applicable to DSCP: bits 010100

    .. data:: af23 = 22

    	Applicable to DSCP: bits 010110

    .. data:: cs3 = 24

    	Applicable to DSCP: bits 011000

    .. data:: af31 = 26

    	Applicable to DSCP: bits 011010

    .. data:: af32 = 28

    	Applicable to DSCP: bits 011100

    .. data:: af33 = 30

    	Applicable to DSCP: bits 011110

    .. data:: cs4 = 32

    	Applicable to DSCP: bits 100000

    .. data:: af41 = 34

    	Applicable to DSCP: bits 100010

    .. data:: af42 = 36

    	Applicable to DSCP: bits 100100

    .. data:: af43 = 38

    	Applicable to DSCP: bits 100110

    .. data:: cs5 = 40

    	Applicable to DSCP: bits 101000

    .. data:: ef = 46

    	Applicable to DSCP: bits 101110

    .. data:: cs6 = 48

    	Applicable to DSCP: bits 110000

    .. data:: cs7 = 56

    	Applicable to DSCP: bits 111000

    """

    default = Enum.YLeaf(0, "default")

    cs1 = Enum.YLeaf(8, "cs1")

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    cs2 = Enum.YLeaf(16, "cs2")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    cs3 = Enum.YLeaf(24, "cs3")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    cs4 = Enum.YLeaf(32, "cs4")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    cs5 = Enum.YLeaf(40, "cs5")

    ef = Enum.YLeaf(46, "ef")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")


class ProtoType(Enum):
    """
    ProtoType (Enum Class)

    Proto type

    .. data:: grpc = 1

    	GRPC

    .. data:: tcp = 2

    	tcp

    .. data:: udp = 3

    	udp

    """

    grpc = Enum.YLeaf(1, "grpc")

    tcp = Enum.YLeaf(2, "tcp")

    udp = Enum.YLeaf(3, "udp")



class TelemetryModelDriven(Entity):
    """
    Model Driven Telemetry configuration
    
    .. attribute:: sensor_groups
    
    	Sensor group configuration
    	**type**\:  :py:class:`SensorGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	Streaming Telemetry Subscription
    	**type**\:  :py:class:`Subscriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions>`
    
    .. attribute:: include
    
    	Include fields with empty values in output
    	**type**\:  :py:class:`Include <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Include>`
    
    .. attribute:: destination_groups
    
    	Destination Group configuration
    	**type**\:  :py:class:`DestinationGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups>`
    
    .. attribute:: strict_timer
    
    	enable strict\-timer for all subscriptions, default is relative timer
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable Model Driven Telemetry
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: max_sensor_paths
    
    	Maximum allowed sensor paths, default\: 1000
    	**type**\: int
    
    	**range:** 0..4000
    
    .. attribute:: max_containers_per_path
    
    	Maximum containers allowed per path, 0 disables the check
    	**type**\: int
    
    	**range:** 0..1024
    
    .. attribute:: tcp_send_timeout
    
    	TCP send timeout value, default\:30 sec,0 will disable the timeout
    	**type**\: int
    
    	**range:** 0..30
    
    

    """

    _prefix = 'telemetry-model-driven-cfg'
    _revision = '2018-05-29'

    def __init__(self):
        super(TelemetryModelDriven, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-model-driven"
        self.yang_parent_name = "Cisco-IOS-XR-telemetry-model-driven-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sensor-groups", ("sensor_groups", TelemetryModelDriven.SensorGroups)), ("subscriptions", ("subscriptions", TelemetryModelDriven.Subscriptions)), ("include", ("include", TelemetryModelDriven.Include)), ("destination-groups", ("destination_groups", TelemetryModelDriven.DestinationGroups))])
        self._leafs = OrderedDict([
            ('strict_timer', (YLeaf(YType.empty, 'strict-timer'), ['Empty'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('max_sensor_paths', (YLeaf(YType.uint32, 'max-sensor-paths'), ['int'])),
            ('max_containers_per_path', (YLeaf(YType.uint32, 'max-containers-per-path'), ['int'])),
            ('tcp_send_timeout', (YLeaf(YType.uint32, 'tcp-send-timeout'), ['int'])),
        ])
        self.strict_timer = None
        self.enable = None
        self.max_sensor_paths = None
        self.max_containers_per_path = None
        self.tcp_send_timeout = None

        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"

        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"

        self.include = TelemetryModelDriven.Include()
        self.include.parent = self
        self._children_name_map["include"] = "include"

        self.destination_groups = TelemetryModelDriven.DestinationGroups()
        self.destination_groups.parent = self
        self._children_name_map["destination_groups"] = "destination-groups"
        self._segment_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TelemetryModelDriven, ['strict_timer', 'enable', 'max_sensor_paths', 'max_containers_per_path', 'tcp_send_timeout'], name, value)


    class SensorGroups(Entity):
        """
        Sensor group configuration
        
        .. attribute:: sensor_group
        
        	Sensor group configuration
        	**type**\: list of  		 :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2018-05-29'

        def __init__(self):
            super(TelemetryModelDriven.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sensor-group", ("sensor_group", TelemetryModelDriven.SensorGroups.SensorGroup))])
            self._leafs = OrderedDict()

            self.sensor_group = YList(self)
            self._segment_path = lambda: "sensor-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.SensorGroups, [], name, value)


        class SensorGroup(Entity):
            """
            Sensor group configuration
            
            .. attribute:: sensor_group_identifier  (key)
            
            	The identifier for this group
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: sensor_paths
            
            	Sensor path configuration
            	**type**\:  :py:class:`SensorPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2018-05-29'

            def __init__(self):
                super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sensor_group_identifier']
                self._child_classes = OrderedDict([("sensor-paths", ("sensor_paths", TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths))])
                self._leafs = OrderedDict([
                    ('sensor_group_identifier', (YLeaf(YType.str, 'sensor-group-identifier'), ['str'])),
                ])
                self.sensor_group_identifier = None

                self.sensor_paths = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self
                self._children_name_map["sensor_paths"] = "sensor-paths"
                self._segment_path = lambda: "sensor-group" + "[sensor-group-identifier='" + str(self.sensor_group_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/sensor-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup, ['sensor_group_identifier'], name, value)


            class SensorPaths(Entity):
                """
                Sensor path configuration
                
                .. attribute:: sensor_path
                
                	Sensor path configuration
                	**type**\: list of  		 :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2018-05-29'

                def __init__(self):
                    super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths, self).__init__()

                    self.yang_name = "sensor-paths"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sensor-path", ("sensor_path", TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath))])
                    self._leafs = OrderedDict()

                    self.sensor_path = YList(self)
                    self._segment_path = lambda: "sensor-paths"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths, [], name, value)


                class SensorPath(Entity):
                    """
                    Sensor path configuration
                    
                    .. attribute:: telemetry_sensor_path  (key)
                    
                    	Sensor Path
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2018-05-29'

                    def __init__(self):
                        super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__init__()

                        self.yang_name = "sensor-path"
                        self.yang_parent_name = "sensor-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['telemetry_sensor_path']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('telemetry_sensor_path', (YLeaf(YType.str, 'telemetry-sensor-path'), ['str'])),
                        ])
                        self.telemetry_sensor_path = None
                        self._segment_path = lambda: "sensor-path" + "[telemetry-sensor-path='" + str(self.telemetry_sensor_path) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath, ['telemetry_sensor_path'], name, value)


    class Subscriptions(Entity):
        """
        Streaming Telemetry Subscription
        
        .. attribute:: subscription
        
        	Streaming Telemetry Subscription
        	**type**\: list of  		 :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2018-05-29'

        def __init__(self):
            super(TelemetryModelDriven.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("subscription", ("subscription", TelemetryModelDriven.Subscriptions.Subscription))])
            self._leafs = OrderedDict()

            self.subscription = YList(self)
            self._segment_path = lambda: "subscriptions"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Subscriptions, [], name, value)


        class Subscription(Entity):
            """
            Streaming Telemetry Subscription
            
            .. attribute:: subscription_identifier  (key)
            
            	Subscription identifier string
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: sensor_profiles
            
            	Associate Sensor Groups with Subscription
            	**type**\:  :py:class:`SensorProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles>`
            
            .. attribute:: destination_profiles
            
            	Associate Destination Groups with Subscription
            	**type**\:  :py:class:`DestinationProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles>`
            
            .. attribute:: source_qos_marking
            
            	Outgoing DSCP value
            	**type**\:  :py:class:`MdtDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.MdtDscpValue>`
            
            .. attribute:: source_interface
            
            	Source address to use for streaming telemetry information
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2018-05-29'

            def __init__(self):
                super(TelemetryModelDriven.Subscriptions.Subscription, self).__init__()

                self.yang_name = "subscription"
                self.yang_parent_name = "subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['subscription_identifier']
                self._child_classes = OrderedDict([("sensor-profiles", ("sensor_profiles", TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles)), ("destination-profiles", ("destination_profiles", TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles))])
                self._leafs = OrderedDict([
                    ('subscription_identifier', (YLeaf(YType.str, 'subscription-identifier'), ['str'])),
                    ('source_qos_marking', (YLeaf(YType.enumeration, 'source-qos-marking'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'MdtDscpValue', '')])),
                    ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                ])
                self.subscription_identifier = None
                self.source_qos_marking = None
                self.source_interface = None

                self.sensor_profiles = TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles()
                self.sensor_profiles.parent = self
                self._children_name_map["sensor_profiles"] = "sensor-profiles"

                self.destination_profiles = TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles()
                self.destination_profiles.parent = self
                self._children_name_map["destination_profiles"] = "destination-profiles"
                self._segment_path = lambda: "subscription" + "[subscription-identifier='" + str(self.subscription_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/subscriptions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription, ['subscription_identifier', 'source_qos_marking', 'source_interface'], name, value)


            class SensorProfiles(Entity):
                """
                Associate Sensor Groups with Subscription
                
                .. attribute:: sensor_profile
                
                	Associate Sensor Group with Subscription
                	**type**\: list of  		 :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2018-05-29'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles, self).__init__()

                    self.yang_name = "sensor-profiles"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sensor-profile", ("sensor_profile", TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile))])
                    self._leafs = OrderedDict()

                    self.sensor_profile = YList(self)
                    self._segment_path = lambda: "sensor-profiles"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles, [], name, value)


                class SensorProfile(Entity):
                    """
                    Associate Sensor Group with Subscription
                    
                    .. attribute:: sensorgroupid  (key)
                    
                    	Reference to the telemetry sensor group name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: strict_timer
                    
                    	use strict timer
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: sample_interval
                    
                    	Sample interval in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2018-05-29'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile, self).__init__()

                        self.yang_name = "sensor-profile"
                        self.yang_parent_name = "sensor-profiles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensorgroupid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensorgroupid', (YLeaf(YType.str, 'sensorgroupid'), ['str'])),
                            ('strict_timer', (YLeaf(YType.empty, 'strict-timer'), ['Empty'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.sensorgroupid = None
                        self.strict_timer = None
                        self.sample_interval = None
                        self._segment_path = lambda: "sensor-profile" + "[sensorgroupid='" + str(self.sensorgroupid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile, ['sensorgroupid', 'strict_timer', 'sample_interval'], name, value)


            class DestinationProfiles(Entity):
                """
                Associate Destination Groups with Subscription
                
                .. attribute:: destination_profile
                
                	Associate Destination Group with Subscription
                	**type**\: list of  		 :py:class:`DestinationProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2018-05-29'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles, self).__init__()

                    self.yang_name = "destination-profiles"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("destination-profile", ("destination_profile", TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile))])
                    self._leafs = OrderedDict()

                    self.destination_profile = YList(self)
                    self._segment_path = lambda: "destination-profiles"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles, [], name, value)


                class DestinationProfile(Entity):
                    """
                    Associate Destination Group with Subscription
                    
                    .. attribute:: destination_id  (key)
                    
                    	Destination Id to associate with Subscription
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2018-05-29'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile, self).__init__()

                        self.yang_name = "destination-profile"
                        self.yang_parent_name = "destination-profiles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['destination_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('destination_id', (YLeaf(YType.str, 'destination-id'), ['str'])),
                        ])
                        self.destination_id = None
                        self._segment_path = lambda: "destination-profile" + "[destination-id='" + str(self.destination_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile, ['destination_id'], name, value)


    class Include(Entity):
        """
        Include fields with empty values in output.
        
        .. attribute:: empty
        
        	Include fields with empty values in output
        	**type**\:  :py:class:`Empty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Include.Empty>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2018-05-29'

        def __init__(self):
            super(TelemetryModelDriven.Include, self).__init__()

            self.yang_name = "include"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("empty", ("empty", TelemetryModelDriven.Include.Empty))])
            self._leafs = OrderedDict()

            self.empty = TelemetryModelDriven.Include.Empty()
            self.empty.parent = self
            self._children_name_map["empty"] = "empty"
            self._segment_path = lambda: "include"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Include, [], name, value)


        class Empty(Entity):
            """
            Include fields with empty values in output.
            
            .. attribute:: values
            
            	String type fields with empty string value, for example, are omitted by default. This provides an option to override this behavior and include them in the output
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2018-05-29'

            def __init__(self):
                super(TelemetryModelDriven.Include.Empty, self).__init__()

                self.yang_name = "empty"
                self.yang_parent_name = "include"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('values', (YLeaf(YType.empty, 'values'), ['Empty'])),
                ])
                self.values = None
                self._segment_path = lambda: "empty"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/include/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Include.Empty, ['values'], name, value)


    class DestinationGroups(Entity):
        """
        Destination Group configuration
        
        .. attribute:: destination_group
        
        	Destination Group
        	**type**\: list of  		 :py:class:`DestinationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2018-05-29'

        def __init__(self):
            super(TelemetryModelDriven.DestinationGroups, self).__init__()

            self.yang_name = "destination-groups"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination-group", ("destination_group", TelemetryModelDriven.DestinationGroups.DestinationGroup))])
            self._leafs = OrderedDict()

            self.destination_group = YList(self)
            self._segment_path = lambda: "destination-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.DestinationGroups, [], name, value)


        class DestinationGroup(Entity):
            """
            Destination Group
            
            .. attribute:: destination_id  (key)
            
            	destination group id string
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv6_destinations
            
            	Destination address configuration
            	**type**\:  :py:class:`Ipv6Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations>`
            
            .. attribute:: ipv4_destinations
            
            	Destination address configuration
            	**type**\:  :py:class:`Ipv4Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations>`
            
            .. attribute:: vrf
            
            	Vrf for the destination group
            	**type**\: str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2018-05-29'

            def __init__(self):
                super(TelemetryModelDriven.DestinationGroups.DestinationGroup, self).__init__()

                self.yang_name = "destination-group"
                self.yang_parent_name = "destination-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['destination_id']
                self._child_classes = OrderedDict([("ipv6-destinations", ("ipv6_destinations", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations)), ("ipv4-destinations", ("ipv4_destinations", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations))])
                self._leafs = OrderedDict([
                    ('destination_id', (YLeaf(YType.str, 'destination-id'), ['str'])),
                    ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                ])
                self.destination_id = None
                self.vrf = None

                self.ipv6_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations()
                self.ipv6_destinations.parent = self
                self._children_name_map["ipv6_destinations"] = "ipv6-destinations"

                self.ipv4_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations()
                self.ipv4_destinations.parent = self
                self._children_name_map["ipv4_destinations"] = "ipv4-destinations"
                self._segment_path = lambda: "destination-group" + "[destination-id='" + str(self.destination_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/destination-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup, ['destination_id', 'vrf'], name, value)


            class Ipv6Destinations(Entity):
                """
                Destination address configuration
                
                .. attribute:: ipv6_destination
                
                	destination IP address
                	**type**\: list of  		 :py:class:`Ipv6Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2018-05-29'

                def __init__(self):
                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations, self).__init__()

                    self.yang_name = "ipv6-destinations"
                    self.yang_parent_name = "destination-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv6-destination", ("ipv6_destination", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination))])
                    self._leafs = OrderedDict()

                    self.ipv6_destination = YList(self)
                    self._segment_path = lambda: "ipv6-destinations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations, [], name, value)


                class Ipv6Destination(Entity):
                    """
                    destination IP address
                    
                    .. attribute:: ipv6_address  (key)
                    
                    	Destination IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  (key)
                    
                    	destination port
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:  :py:class:`EncodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeType>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:  :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2018-05-29'

                    def __init__(self):
                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination, self).__init__()

                        self.yang_name = "ipv6-destination"
                        self.yang_parent_name = "ipv6-destinations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ipv6_address','destination_port']
                        self._child_classes = OrderedDict([("protocol", ("protocol", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol))])
                        self._leafs = OrderedDict([
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ('destination_port', (YLeaf(YType.uint16, 'destination-port'), ['int'])),
                            ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeType', '')])),
                        ])
                        self.ipv6_address = None
                        self.destination_port = None
                        self.encoding = None

                        self.protocol = None
                        self._children_name_map["protocol"] = "protocol"
                        self._segment_path = lambda: "ipv6-destination" + "[ipv6-address='" + str(self.ipv6_address) + "']" + "[destination-port='" + str(self.destination_port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination, ['ipv6_address', 'destination_port', 'encoding'], name, value)


                    class Protocol(Entity):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:  :py:class:`ProtoType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoType>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\: str
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: packetsize
                        
                        	udp packetsize
                        	**type**\: int
                        
                        	**range:** 484..65507
                        
                        	**default value**\: 1472
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2018-05-29'

                        def __init__(self):
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "ipv6-destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('protocol', (YLeaf(YType.enumeration, 'protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoType', '')])),
                                ('tls_hostname', (YLeaf(YType.str, 'tls-hostname'), ['str'])),
                                ('no_tls', (YLeaf(YType.uint32, 'no-tls'), ['int'])),
                                ('packetsize', (YLeaf(YType.uint32, 'packetsize'), ['int'])),
                            ])
                            self.protocol = None
                            self.tls_hostname = None
                            self.no_tls = None
                            self.packetsize = None
                            self._segment_path = lambda: "protocol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol, ['protocol', 'tls_hostname', 'no_tls', 'packetsize'], name, value)


            class Ipv4Destinations(Entity):
                """
                Destination address configuration
                
                .. attribute:: ipv4_destination
                
                	destination IP address
                	**type**\: list of  		 :py:class:`Ipv4Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2018-05-29'

                def __init__(self):
                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations, self).__init__()

                    self.yang_name = "ipv4-destinations"
                    self.yang_parent_name = "destination-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv4-destination", ("ipv4_destination", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination))])
                    self._leafs = OrderedDict()

                    self.ipv4_destination = YList(self)
                    self._segment_path = lambda: "ipv4-destinations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations, [], name, value)


                class Ipv4Destination(Entity):
                    """
                    destination IP address
                    
                    .. attribute:: ipv4_address  (key)
                    
                    	Destination IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  (key)
                    
                    	destination port
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:  :py:class:`EncodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeType>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:  :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2018-05-29'

                    def __init__(self):
                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination, self).__init__()

                        self.yang_name = "ipv4-destination"
                        self.yang_parent_name = "ipv4-destinations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ipv4_address','destination_port']
                        self._child_classes = OrderedDict([("protocol", ("protocol", TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol))])
                        self._leafs = OrderedDict([
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('destination_port', (YLeaf(YType.uint16, 'destination-port'), ['int'])),
                            ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'EncodeType', '')])),
                        ])
                        self.ipv4_address = None
                        self.destination_port = None
                        self.encoding = None

                        self.protocol = None
                        self._children_name_map["protocol"] = "protocol"
                        self._segment_path = lambda: "ipv4-destination" + "[ipv4-address='" + str(self.ipv4_address) + "']" + "[destination-port='" + str(self.destination_port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination, ['ipv4_address', 'destination_port', 'encoding'], name, value)


                    class Protocol(Entity):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:  :py:class:`ProtoType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoType>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\: str
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: packetsize
                        
                        	udp packetsize
                        	**type**\: int
                        
                        	**range:** 484..65507
                        
                        	**default value**\: 1472
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2018-05-29'

                        def __init__(self):
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "ipv4-destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('protocol', (YLeaf(YType.enumeration, 'protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg', 'ProtoType', '')])),
                                ('tls_hostname', (YLeaf(YType.str, 'tls-hostname'), ['str'])),
                                ('no_tls', (YLeaf(YType.uint32, 'no-tls'), ['int'])),
                                ('packetsize', (YLeaf(YType.uint32, 'packetsize'), ['int'])),
                            ])
                            self.protocol = None
                            self.tls_hostname = None
                            self.no_tls = None
                            self.packetsize = None
                            self._segment_path = lambda: "protocol"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol, ['protocol', 'tls_hostname', 'no_tls', 'packetsize'], name, value)

    def clone_ptr(self):
        self._top_entity = TelemetryModelDriven()
        return self._top_entity


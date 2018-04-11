""" openconfig_channel_monitor 

This model describes operational state data for an optical
channel monitor (OCM) for optical transport line system
elements such as wavelength routers (ROADMs) and amplifiers.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ChannelMonitors(Entity):
    """
    Top\-level container for optical channel monitors
    
    .. attribute:: channel_monitor
    
    	List of channel monitors, keyed by channel monitor name
    	**type**\: list of  		 :py:class:`ChannelMonitor <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor>`
    
    

    """

    _prefix = 'oc-chan-monitor'
    _revision = '2017-07-08'

    def __init__(self):
        super(ChannelMonitors, self).__init__()
        self._top_entity = None

        self.yang_name = "channel-monitors"
        self.yang_parent_name = "openconfig-channel-monitor"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("channel-monitor", ("channel_monitor", ChannelMonitors.ChannelMonitor))])
        self._leafs = OrderedDict()

        self.channel_monitor = YList(self)
        self._segment_path = lambda: "openconfig-channel-monitor:channel-monitors"

    def __setattr__(self, name, value):
        self._perform_setattr(ChannelMonitors, [], name, value)


    class ChannelMonitor(Entity):
        """
        List of channel monitors, keyed by channel monitor name.
        
        .. attribute:: name  (key)
        
        	References the optical channel monitor name
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Config>`
        
        .. attribute:: config
        
        	Configuration data 
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Config>`
        
        .. attribute:: state
        
        	Operational state data 
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.State>`
        
        .. attribute:: channels
        
        	Enclosing container for the list of values describing the power spectral density distribution
        	**type**\:  :py:class:`Channels <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Channels>`
        
        

        """

        _prefix = 'oc-chan-monitor'
        _revision = '2017-07-08'

        def __init__(self):
            super(ChannelMonitors.ChannelMonitor, self).__init__()

            self.yang_name = "channel-monitor"
            self.yang_parent_name = "channel-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([("config", ("config", ChannelMonitors.ChannelMonitor.Config)), ("state", ("state", ChannelMonitors.ChannelMonitor.State)), ("channels", ("channels", ChannelMonitors.ChannelMonitor.Channels))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
            ])
            self.name = None

            self.config = ChannelMonitors.ChannelMonitor.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.state = ChannelMonitors.ChannelMonitor.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")

            self.channels = ChannelMonitors.ChannelMonitor.Channels()
            self.channels.parent = self
            self._children_name_map["channels"] = "channels"
            self._children_yang_names.add("channels")
            self._segment_path = lambda: "channel-monitor" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "openconfig-channel-monitor:channel-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ChannelMonitors.ChannelMonitor, ['name'], name, value)


        class Config(Entity):
            """
            Configuration data 
            
            .. attribute:: name
            
            	Reference to system\-supplied name of the port on the optical channel monitor (OCM). If this port is embedded in another card (i.e. an amplifier card) the device should still define a port representing the OCM even if it is internal and not physically present on the faceplate of the card
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            .. attribute:: monitor_port
            
            	Reference to system\-supplied name of the port that the channel monitor is physically connected to. This port will be of type MONITOR. This port is a tap off of the monitored\-port and would be in the same card as the monitored port. If this port is embedded in another card (i.e. an amplifier card) the device should still define a port representing the monitor port if it is internal and not physically present on the faceplate of the card
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            

            """

            _prefix = 'oc-chan-monitor'
            _revision = '2017-07-08'

            def __init__(self):
                super(ChannelMonitors.ChannelMonitor.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "channel-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('monitor_port', YLeaf(YType.str, 'monitor-port')),
                ])
                self.name = None
                self.monitor_port = None
                self._segment_path = lambda: "config"

            def __setattr__(self, name, value):
                self._perform_setattr(ChannelMonitors.ChannelMonitor.Config, ['name', 'monitor_port'], name, value)


        class State(Entity):
            """
            Operational state data 
            
            .. attribute:: name
            
            	Reference to system\-supplied name of the port on the optical channel monitor (OCM). If this port is embedded in another card (i.e. an amplifier card) the device should still define a port representing the OCM even if it is internal and not physically present on the faceplate of the card
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            .. attribute:: monitor_port
            
            	Reference to system\-supplied name of the port that the channel monitor is physically connected to. This port will be of type MONITOR. This port is a tap off of the monitored\-port and would be in the same card as the monitored port. If this port is embedded in another card (i.e. an amplifier card) the device should still define a port representing the monitor port if it is internal and not physically present on the faceplate of the card
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            

            """

            _prefix = 'oc-chan-monitor'
            _revision = '2017-07-08'

            def __init__(self):
                super(ChannelMonitors.ChannelMonitor.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "channel-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('monitor_port', YLeaf(YType.str, 'monitor-port')),
                ])
                self.name = None
                self.monitor_port = None
                self._segment_path = lambda: "state"

            def __setattr__(self, name, value):
                self._perform_setattr(ChannelMonitors.ChannelMonitor.State, ['name', 'monitor_port'], name, value)


        class Channels(Entity):
            """
            Enclosing container for the list of values describing
            the power spectral density distribution
            
            .. attribute:: channel
            
            	List of tuples describing the PSD distribution
            	**type**\: list of  		 :py:class:`Channel <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Channels.Channel>`
            
            

            """

            _prefix = 'oc-chan-monitor'
            _revision = '2017-07-08'

            def __init__(self):
                super(ChannelMonitors.ChannelMonitor.Channels, self).__init__()

                self.yang_name = "channels"
                self.yang_parent_name = "channel-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("channel", ("channel", ChannelMonitors.ChannelMonitor.Channels.Channel))])
                self._leafs = OrderedDict()

                self.channel = YList(self)
                self._segment_path = lambda: "channels"

            def __setattr__(self, name, value):
                self._perform_setattr(ChannelMonitors.ChannelMonitor.Channels, [], name, value)


            class Channel(Entity):
                """
                List of tuples describing the PSD distribution
                
                .. attribute:: lower_frequency  (key)
                
                	Reference to the list key
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`lower_frequency <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Channels.Channel.State>`
                
                .. attribute:: upper_frequency  (key)
                
                	Reference to the list key
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`upper_frequency <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Channels.Channel.State>`
                
                .. attribute:: state
                
                	Operational state data for PSD
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_channel_monitor.ChannelMonitors.ChannelMonitor.Channels.Channel.State>`
                
                

                """

                _prefix = 'oc-chan-monitor'
                _revision = '2017-07-08'

                def __init__(self):
                    super(ChannelMonitors.ChannelMonitor.Channels.Channel, self).__init__()

                    self.yang_name = "channel"
                    self.yang_parent_name = "channels"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['lower_frequency','upper_frequency']
                    self._child_container_classes = OrderedDict([("state", ("state", ChannelMonitors.ChannelMonitor.Channels.Channel.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lower_frequency', YLeaf(YType.str, 'lower-frequency')),
                        ('upper_frequency', YLeaf(YType.str, 'upper-frequency')),
                    ])
                    self.lower_frequency = None
                    self.upper_frequency = None

                    self.state = ChannelMonitors.ChannelMonitor.Channels.Channel.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "channel" + "[lower-frequency='" + str(self.lower_frequency) + "']" + "[upper-frequency='" + str(self.upper_frequency) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(ChannelMonitors.ChannelMonitor.Channels.Channel, ['lower_frequency', 'upper_frequency'], name, value)


                class State(Entity):
                    """
                    Operational state data for PSD
                    
                    .. attribute:: lower_frequency
                    
                    	Lower frequency of the specified PSD
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: upper_frequency
                    
                    	Upper frequency of the specified PSD
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: psd
                    
                    	Power spectral density expressed in nanowatts per megahertz, nW/MHz.  These units allow the value to often be greater than 1.0.  It also avoids dealing with zero values for 0dBm.  For example, a 40GHz wide channel with 0dBm power would be\:  0dBm = 1mW = 10^6nW  40GHz = 40,000MHz  0dBm/40GHz = 10^6nW/40,000MHz = 1000/40 = 25
                    	**type**\: str
                    
                    	**length:** 32
                    
                    	**units**\: nW/MHz
                    
                    

                    """

                    _prefix = 'oc-chan-monitor'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(ChannelMonitors.ChannelMonitor.Channels.Channel.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "channel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lower_frequency', YLeaf(YType.uint64, 'lower-frequency')),
                            ('upper_frequency', YLeaf(YType.uint64, 'upper-frequency')),
                            ('psd', YLeaf(YType.str, 'psd')),
                        ])
                        self.lower_frequency = None
                        self.upper_frequency = None
                        self.psd = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ChannelMonitors.ChannelMonitor.Channels.Channel.State, ['lower_frequency', 'upper_frequency', 'psd'], name, value)

    def clone_ptr(self):
        self._top_entity = ChannelMonitors()
        return self._top_entity


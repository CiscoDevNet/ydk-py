""" openconfig_optical_amplifier 

This model describes configuration and operational state data
for optical amplifiers, deployed as part of a transport
line system.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OPTICALAMPLIFIERTYPE(Identity):
    """
    Type definition for different types of optical amplifiers
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:OPTICAL_AMPLIFIER_TYPE"):
        super(OPTICALAMPLIFIERTYPE, self).__init__(ns, pref, tag)


class OPTICALAMPLIFIERMODE(Identity):
    """
    Type definition for different types of optical amplifier
    operating modes
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:OPTICAL_AMPLIFIER_MODE"):
        super(OPTICALAMPLIFIERMODE, self).__init__(ns, pref, tag)


class GAINRANGE(Identity):
    """
    Base type for expressing the gain range for a switched gain
    amplifier.  The gain range is expressed as a generic setting,
    e.g., LOW/MID/HIGH. The actual db range will be determined
    by the implementation.
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:GAIN_RANGE"):
        super(GAINRANGE, self).__init__(ns, pref, tag)


class OpticalAmplifier(Entity):
    """
    Enclosing container for amplifiers and supervisory channels
    
    .. attribute:: amplifiers
    
    	Enclosing container for list of amplifiers
    	**type**\:  :py:class:`Amplifiers <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers>`
    
    .. attribute:: supervisory_channels
    
    	Enclosing container for list of supervisory channels
    	**type**\:  :py:class:`SupervisoryChannels <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels>`
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self):
        super(OpticalAmplifier, self).__init__()
        self._top_entity = None

        self.yang_name = "optical-amplifier"
        self.yang_parent_name = "openconfig-optical-amplifier"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("amplifiers", ("amplifiers", OpticalAmplifier.Amplifiers)), ("supervisory-channels", ("supervisory_channels", OpticalAmplifier.SupervisoryChannels))])
        self._leafs = OrderedDict()

        self.amplifiers = OpticalAmplifier.Amplifiers()
        self.amplifiers.parent = self
        self._children_name_map["amplifiers"] = "amplifiers"

        self.supervisory_channels = OpticalAmplifier.SupervisoryChannels()
        self.supervisory_channels.parent = self
        self._children_name_map["supervisory_channels"] = "supervisory-channels"
        self._segment_path = lambda: "openconfig-optical-amplifier:optical-amplifier"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OpticalAmplifier, [], name, value)


    class Amplifiers(Entity):
        """
        Enclosing container for list of amplifiers
        
        .. attribute:: amplifier
        
        	List of optical amplifiers present in the device
        	**type**\: list of  		 :py:class:`Amplifier <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier>`
        
        

        """

        _prefix = 'oc-opt-amp'
        _revision = '2017-07-08'

        def __init__(self):
            super(OpticalAmplifier.Amplifiers, self).__init__()

            self.yang_name = "amplifiers"
            self.yang_parent_name = "optical-amplifier"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("amplifier", ("amplifier", OpticalAmplifier.Amplifiers.Amplifier))])
            self._leafs = OrderedDict()

            self.amplifier = YList(self)
            self._segment_path = lambda: "amplifiers"
            self._absolute_path = lambda: "openconfig-optical-amplifier:optical-amplifier/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalAmplifier.Amplifiers, [], name, value)


        class Amplifier(Entity):
            """
            List of optical amplifiers present in the device
            
            .. attribute:: name  (key)
            
            	Reference to the name of the amplifier
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.Config>`
            
            .. attribute:: config
            
            	Configuration data for the amplifier
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.Config>`
            
            .. attribute:: state
            
            	Operational state data for the amplifier
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State>`
            
            

            """

            _prefix = 'oc-opt-amp'
            _revision = '2017-07-08'

            def __init__(self):
                super(OpticalAmplifier.Amplifiers.Amplifier, self).__init__()

                self.yang_name = "amplifier"
                self.yang_parent_name = "amplifiers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("config", ("config", OpticalAmplifier.Amplifiers.Amplifier.Config)), ("state", ("state", OpticalAmplifier.Amplifiers.Amplifier.State))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.config = OpticalAmplifier.Amplifiers.Amplifier.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = OpticalAmplifier.Amplifiers.Amplifier.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "amplifier" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-optical-amplifier:optical-amplifier/amplifiers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier, ['name'], name, value)


            class Config(Entity):
                """
                Configuration data for the amplifier
                
                .. attribute:: name
                
                	User\-defined name assigned to identify a specific amplifier in the device
                	**type**\: str
                
                .. attribute:: type
                
                	Type of the amplifier
                	**type**\:  :py:class:`OPTICALAMPLIFIERTYPE <ydk.models.openconfig.openconfig_optical_amplifier.OPTICALAMPLIFIERTYPE>`
                
                .. attribute:: target_gain
                
                	Positive gain applied by the amplifier
                	**type**\: Decimal64
                
                	**range:** 0..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: target_gain_tilt
                
                	Gain tilt control
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: gain_range
                
                	Selected gain range.  The gain range is a platform\-defined value indicating the switched gain amplifier setting
                	**type**\:  :py:class:`GAINRANGE <ydk.models.openconfig.openconfig_optical_amplifier.GAINRANGE>`
                
                .. attribute:: amp_mode
                
                	The operating mode of the amplifier
                	**type**\:  :py:class:`OPTICALAMPLIFIERMODE <ydk.models.openconfig.openconfig_optical_amplifier.OPTICALAMPLIFIERMODE>`
                
                .. attribute:: target_output_power
                
                	Output optical power of the amplifier
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: enabled
                
                	Turns power on / off to the amplifiers gain module
                	**type**\: bool
                
                

                """

                _prefix = 'oc-opt-amp'
                _revision = '2017-07-08'

                def __init__(self):
                    super(OpticalAmplifier.Amplifiers.Amplifier.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "amplifier"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'OPTICALAMPLIFIERTYPE')])),
                        ('target_gain', (YLeaf(YType.str, 'target-gain'), ['Decimal64'])),
                        ('target_gain_tilt', (YLeaf(YType.str, 'target-gain-tilt'), ['Decimal64'])),
                        ('gain_range', (YLeaf(YType.identityref, 'gain-range'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'GAINRANGE')])),
                        ('amp_mode', (YLeaf(YType.identityref, 'amp-mode'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'OPTICALAMPLIFIERMODE')])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                    ])
                    self.name = None
                    self.type = None
                    self.target_gain = None
                    self.target_gain_tilt = None
                    self.gain_range = None
                    self.amp_mode = None
                    self.target_output_power = None
                    self.enabled = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.Config, ['name', 'type', 'target_gain', 'target_gain_tilt', 'gain_range', 'amp_mode', 'target_output_power', 'enabled'], name, value)


            class State(Entity):
                """
                Operational state data for the amplifier
                
                .. attribute:: name
                
                	User\-defined name assigned to identify a specific amplifier in the device
                	**type**\: str
                
                .. attribute:: type
                
                	Type of the amplifier
                	**type**\:  :py:class:`OPTICALAMPLIFIERTYPE <ydk.models.openconfig.openconfig_optical_amplifier.OPTICALAMPLIFIERTYPE>`
                
                .. attribute:: target_gain
                
                	Positive gain applied by the amplifier
                	**type**\: Decimal64
                
                	**range:** 0..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: target_gain_tilt
                
                	Gain tilt control
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: gain_range
                
                	Selected gain range.  The gain range is a platform\-defined value indicating the switched gain amplifier setting
                	**type**\:  :py:class:`GAINRANGE <ydk.models.openconfig.openconfig_optical_amplifier.GAINRANGE>`
                
                .. attribute:: amp_mode
                
                	The operating mode of the amplifier
                	**type**\:  :py:class:`OPTICALAMPLIFIERMODE <ydk.models.openconfig.openconfig_optical_amplifier.OPTICALAMPLIFIERMODE>`
                
                .. attribute:: target_output_power
                
                	Output optical power of the amplifier
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: enabled
                
                	Turns power on / off to the amplifiers gain module
                	**type**\: bool
                
                .. attribute:: ingress_port
                
                	Reference to system\-supplied name of the amplifier ingress port. This leaf is only valid for ports of type INGRESS
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: egress_port
                
                	Reference to system\-supplied name of the amplifier egress port. This leaf is only valid for ports of type EGRESS
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: actual_gain
                
                	The actual gain applied by the amplifier in units of 0.01dB. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`ActualGain <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.ActualGain>`
                
                .. attribute:: actual_gain_tilt
                
                	The actual tilt applied by the amplifier in units of 0.01dB. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`ActualGainTilt <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.ActualGainTilt>`
                
                .. attribute:: input_power_total
                
                	The total input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`InputPowerTotal <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerTotal>`
                
                .. attribute:: input_power_c_band
                
                	The C band (consisting of approximately 191 to 195 THz or 1530nm to 1565 nm) input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`InputPowerCBand <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerCBand>`
                
                .. attribute:: input_power_l_band
                
                	The L band (consisting of approximately 184 to 191 THz or 1565 to 1625 nm) input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`InputPowerLBand <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerLBand>`
                
                .. attribute:: output_power_total
                
                	The total output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OutputPowerTotal <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerTotal>`
                
                .. attribute:: output_power_c_band
                
                	The C band (consisting of approximately 191 to 195 THz or 1530nm to 1565 nm)output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OutputPowerCBand <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerCBand>`
                
                .. attribute:: output_power_l_band
                
                	The L band (consisting of approximately 184 to 191 THz or 1565 to 1625 nm)output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OutputPowerLBand <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerLBand>`
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.LaserBiasCurrent>`
                
                .. attribute:: optical_return_loss
                
                	The optical return loss (ORL) is the ratio of the light reflected back into the port to the light launched out of the port. ORL is in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OpticalReturnLoss <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.Amplifiers.Amplifier.State.OpticalReturnLoss>`
                
                

                """

                _prefix = 'oc-opt-amp'
                _revision = '2017-07-08'

                def __init__(self):
                    super(OpticalAmplifier.Amplifiers.Amplifier.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "amplifier"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("actual-gain", ("actual_gain", OpticalAmplifier.Amplifiers.Amplifier.State.ActualGain)), ("actual-gain-tilt", ("actual_gain_tilt", OpticalAmplifier.Amplifiers.Amplifier.State.ActualGainTilt)), ("input-power-total", ("input_power_total", OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerTotal)), ("input-power-c-band", ("input_power_c_band", OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerCBand)), ("input-power-l-band", ("input_power_l_band", OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerLBand)), ("output-power-total", ("output_power_total", OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerTotal)), ("output-power-c-band", ("output_power_c_band", OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerCBand)), ("output-power-l-band", ("output_power_l_band", OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerLBand)), ("laser-bias-current", ("laser_bias_current", OpticalAmplifier.Amplifiers.Amplifier.State.LaserBiasCurrent)), ("optical-return-loss", ("optical_return_loss", OpticalAmplifier.Amplifiers.Amplifier.State.OpticalReturnLoss))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'OPTICALAMPLIFIERTYPE')])),
                        ('target_gain', (YLeaf(YType.str, 'target-gain'), ['Decimal64'])),
                        ('target_gain_tilt', (YLeaf(YType.str, 'target-gain-tilt'), ['Decimal64'])),
                        ('gain_range', (YLeaf(YType.identityref, 'gain-range'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'GAINRANGE')])),
                        ('amp_mode', (YLeaf(YType.identityref, 'amp-mode'), [('ydk.models.openconfig.openconfig_optical_amplifier', 'OPTICALAMPLIFIERMODE')])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('ingress_port', (YLeaf(YType.str, 'ingress-port'), ['str'])),
                        ('egress_port', (YLeaf(YType.str, 'egress-port'), ['str'])),
                    ])
                    self.name = None
                    self.type = None
                    self.target_gain = None
                    self.target_gain_tilt = None
                    self.gain_range = None
                    self.amp_mode = None
                    self.target_output_power = None
                    self.enabled = None
                    self.ingress_port = None
                    self.egress_port = None

                    self.actual_gain = OpticalAmplifier.Amplifiers.Amplifier.State.ActualGain()
                    self.actual_gain.parent = self
                    self._children_name_map["actual_gain"] = "actual-gain"

                    self.actual_gain_tilt = OpticalAmplifier.Amplifiers.Amplifier.State.ActualGainTilt()
                    self.actual_gain_tilt.parent = self
                    self._children_name_map["actual_gain_tilt"] = "actual-gain-tilt"

                    self.input_power_total = OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerTotal()
                    self.input_power_total.parent = self
                    self._children_name_map["input_power_total"] = "input-power-total"

                    self.input_power_c_band = OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerCBand()
                    self.input_power_c_band.parent = self
                    self._children_name_map["input_power_c_band"] = "input-power-c-band"

                    self.input_power_l_band = OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerLBand()
                    self.input_power_l_band.parent = self
                    self._children_name_map["input_power_l_band"] = "input-power-l-band"

                    self.output_power_total = OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerTotal()
                    self.output_power_total.parent = self
                    self._children_name_map["output_power_total"] = "output-power-total"

                    self.output_power_c_band = OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerCBand()
                    self.output_power_c_band.parent = self
                    self._children_name_map["output_power_c_band"] = "output-power-c-band"

                    self.output_power_l_band = OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerLBand()
                    self.output_power_l_band.parent = self
                    self._children_name_map["output_power_l_band"] = "output-power-l-band"

                    self.laser_bias_current = OpticalAmplifier.Amplifiers.Amplifier.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"

                    self.optical_return_loss = OpticalAmplifier.Amplifiers.Amplifier.State.OpticalReturnLoss()
                    self.optical_return_loss.parent = self
                    self._children_name_map["optical_return_loss"] = "optical-return-loss"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State, ['name', 'type', 'target_gain', 'target_gain_tilt', 'gain_range', 'amp_mode', 'target_output_power', 'enabled', 'ingress_port', 'egress_port'], name, value)


                class ActualGain(Entity):
                    """
                    The actual gain applied by the amplifier in units of
                    0.01dB. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.ActualGain, self).__init__()

                        self.yang_name = "actual-gain"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "actual-gain"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.ActualGain, ['instant', 'avg', 'min', 'max'], name, value)


                class ActualGainTilt(Entity):
                    """
                    The actual tilt applied by the amplifier in units of
                    0.01dB. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dB
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.ActualGainTilt, self).__init__()

                        self.yang_name = "actual-gain-tilt"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "actual-gain-tilt"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.ActualGainTilt, ['instant', 'avg', 'min', 'max'], name, value)


                class InputPowerTotal(Entity):
                    """
                    The total input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerTotal, self).__init__()

                        self.yang_name = "input-power-total"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power-total"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerTotal, ['instant', 'avg', 'min', 'max'], name, value)


                class InputPowerCBand(Entity):
                    """
                    The C band (consisting of approximately 191 to 195 THz or
                    1530nm to 1565 nm) input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerCBand, self).__init__()

                        self.yang_name = "input-power-c-band"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power-c-band"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerCBand, ['instant', 'avg', 'min', 'max'], name, value)


                class InputPowerLBand(Entity):
                    """
                    The L band (consisting of approximately 184 to 191 THz or
                    1565 to 1625 nm) input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerLBand, self).__init__()

                        self.yang_name = "input-power-l-band"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power-l-band"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.InputPowerLBand, ['instant', 'avg', 'min', 'max'], name, value)


                class OutputPowerTotal(Entity):
                    """
                    The total output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerTotal, self).__init__()

                        self.yang_name = "output-power-total"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power-total"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerTotal, ['instant', 'avg', 'min', 'max'], name, value)


                class OutputPowerCBand(Entity):
                    """
                    The C band (consisting of approximately 191 to 195 THz or
                    1530nm to 1565 nm)output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerCBand, self).__init__()

                        self.yang_name = "output-power-c-band"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power-c-band"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerCBand, ['instant', 'avg', 'min', 'max'], name, value)


                class OutputPowerLBand(Entity):
                    """
                    The L band (consisting of approximately 184 to 191 THz or
                    1565 to 1625 nm)output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerLBand, self).__init__()

                        self.yang_name = "output-power-l-band"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power-l-band"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.OutputPowerLBand, ['instant', 'avg', 'min', 'max'], name, value)


                class LaserBiasCurrent(Entity):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power. The current is expressed in mA
                    with up to two decimal precision. If avg/min/max statistics
                    are not supported, just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "laser-bias-current"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max'], name, value)


                class OpticalReturnLoss(Entity):
                    """
                    The optical return loss (ORL) is the ratio of the light
                    reflected back into the port to the light launched out of
                    the port. ORL is in units of 0.01dBm. If avg/min/max
                    statistics are not supported, just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.Amplifiers.Amplifier.State.OpticalReturnLoss, self).__init__()

                        self.yang_name = "optical-return-loss"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "optical-return-loss"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.Amplifiers.Amplifier.State.OpticalReturnLoss, ['instant', 'avg', 'min', 'max'], name, value)


    class SupervisoryChannels(Entity):
        """
        Enclosing container for list of supervisory channels
        
        .. attribute:: supervisory_channel
        
        	List of supervisory channels
        	**type**\: list of  		 :py:class:`SupervisoryChannel <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel>`
        
        

        """

        _prefix = 'oc-opt-amp'
        _revision = '2017-07-08'

        def __init__(self):
            super(OpticalAmplifier.SupervisoryChannels, self).__init__()

            self.yang_name = "supervisory-channels"
            self.yang_parent_name = "optical-amplifier"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("supervisory-channel", ("supervisory_channel", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel))])
            self._leafs = OrderedDict()

            self.supervisory_channel = YList(self)
            self._segment_path = lambda: "supervisory-channels"
            self._absolute_path = lambda: "openconfig-optical-amplifier:optical-amplifier/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OpticalAmplifier.SupervisoryChannels, [], name, value)


        class SupervisoryChannel(Entity):
            """
            List of supervisory channels
            
            .. attribute:: interface  (key)
            
            	Reference to the interface of the supervisory channel
            	**type**\: str
            
            	**refers to**\:  :py:class:`interface <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config>`
            
            .. attribute:: config
            
            	Configuration data for OSCs
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config>`
            
            .. attribute:: state
            
            	Operational state data for OSCs
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State>`
            
            

            """

            _prefix = 'oc-opt-amp'
            _revision = '2017-07-08'

            def __init__(self):
                super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel, self).__init__()

                self.yang_name = "supervisory-channel"
                self.yang_parent_name = "supervisory-channels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface']
                self._child_classes = OrderedDict([("config", ("config", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config)), ("state", ("state", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State))])
                self._leafs = OrderedDict([
                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                ])
                self.interface = None

                self.config = OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "supervisory-channel" + "[interface='" + str(self.interface) + "']"
                self._absolute_path = lambda: "openconfig-optical-amplifier:optical-amplifier/supervisory-channels/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel, ['interface'], name, value)


            class Config(Entity):
                """
                Configuration data for OSCs
                
                .. attribute:: interface
                
                	List of references to OSC interfaces
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                

                """

                _prefix = 'oc-opt-amp'
                _revision = '2017-07-08'

                def __init__(self):
                    super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "supervisory-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', (YLeafList(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = []
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.Config, [u'interface'], name, value)


            class State(Entity):
                """
                Operational state data for OSCs
                
                .. attribute:: interface
                
                	List of references to OSC interfaces
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: input_power
                
                	The input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.InputPower>`
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.OutputPower>`
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to one decimal precision. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_optical_amplifier.OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.LaserBiasCurrent>`
                
                

                """

                _prefix = 'oc-opt-amp'
                _revision = '2017-07-08'

                def __init__(self):
                    super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "supervisory-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("input-power", ("input_power", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.InputPower)), ("output-power", ("output_power", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.OutputPower)), ("laser-bias-current", ("laser_bias_current", OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.LaserBiasCurrent))])
                    self._leafs = OrderedDict([
                        ('interface', (YLeafList(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = []

                    self.input_power = OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.output_power = OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"

                    self.laser_bias_current = OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State, [u'interface'], name, value)


                class InputPower(Entity):
                    """
                    The input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    the target is expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.InputPower, ['instant', 'avg', 'min', 'max'], name, value)


                class OutputPower(Entity):
                    """
                    The output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    the target is expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.OutputPower, ['instant', 'avg', 'min', 'max'], name, value)


                class LaserBiasCurrent(Entity):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power. The current is expressed in mA
                    with up to one decimal precision. If avg/min/max statistics
                    are not supported, the target is expected to just supply
                    the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**units**\: mA
                    
                    

                    """

                    _prefix = 'oc-opt-amp'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "laser-bias-current"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OpticalAmplifier.SupervisoryChannels.SupervisoryChannel.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max'], name, value)

    def clone_ptr(self):
        self._top_entity = OpticalAmplifier()
        return self._top_entity

class LOWGAINRANGE(GAINRANGE):
    """
    LOW gain range setting
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:LOW_GAIN_RANGE"):
        super(LOWGAINRANGE, self).__init__(ns, pref, tag)


class BACKWARDRAMAN(OPTICALAMPLIFIERTYPE):
    """
    Backward pumping Raman amplifier
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:BACKWARD_RAMAN"):
        super(BACKWARDRAMAN, self).__init__(ns, pref, tag)


class CONSTANTGAIN(OPTICALAMPLIFIERMODE):
    """
    Constant gain mode
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:CONSTANT_GAIN"):
        super(CONSTANTGAIN, self).__init__(ns, pref, tag)


class FIXEDGAINRANGE(GAINRANGE):
    """
    Fixed or non\-switched gain amplfier
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:FIXED_GAIN_RANGE"):
        super(FIXEDGAINRANGE, self).__init__(ns, pref, tag)


class MIDGAINRANGE(GAINRANGE):
    """
    MID gain range setting
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:MID_GAIN_RANGE"):
        super(MIDGAINRANGE, self).__init__(ns, pref, tag)


class HIGHGAINRANGE(GAINRANGE):
    """
    HIGH gain range setting
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:HIGH_GAIN_RANGE"):
        super(HIGHGAINRANGE, self).__init__(ns, pref, tag)


class HYBRID(OPTICALAMPLIFIERTYPE):
    """
    Hybrid backward pumping Raman + EDFA amplifier
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:HYBRID"):
        super(HYBRID, self).__init__(ns, pref, tag)


class FORWARDRAMAN(OPTICALAMPLIFIERTYPE):
    """
    Forward pumping Raman amplifier
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:FORWARD_RAMAN"):
        super(FORWARDRAMAN, self).__init__(ns, pref, tag)


class EDFA(OPTICALAMPLIFIERTYPE):
    """
    Erbium doped fiber amplifer (EDFA)
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:EDFA"):
        super(EDFA, self).__init__(ns, pref, tag)


class CONSTANTPOWER(OPTICALAMPLIFIERMODE):
    """
    Constant power mode
    
    

    """

    _prefix = 'oc-opt-amp'
    _revision = '2017-07-08'

    def __init__(self, ns="http://openconfig.net/yang/optical-amplfier", pref="openconfig-optical-amplifier", tag="openconfig-optical-amplifier:CONSTANT_POWER"):
        super(CONSTANTPOWER, self).__init__(ns, pref, tag)



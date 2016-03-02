""" Cisco_IOS_XR_controller_optics_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package operational data.

This module contains definitions
for the following management objects\:
  optics\-oper\: Optics operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class OpticsControllerState_Enum(Enum):
    """
    OpticsControllerState_Enum

    Optics controller state

    """

    """

    Up

    """
    OPTICS_STATE_UP = 0

    """

    Down

    """
    OPTICS_STATE_DOWN = 1

    """

    Administratively Down

    """
    OPTICS_STATE_ADMIN_DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsControllerState_Enum']


class OpticsFormFactor_Enum(Enum):
    """
    OpticsFormFactor_Enum

    Optics form factor

    """

    """

    Not set

    """
    NOT_SET = 0

    """

    Invalid

    """
    INVALID = 1

    """

    CPAK

    """
    CPAK = 2

    """

    CXP

    """
    CXP = 3

    """

    SFP+

    """
    SFP_PLUS = 4

    """

    QSFP

    """
    QSFP = 5

    """

    QSFP+

    """
    QSFP_PLUS = 6

    """

    QSFP28

    """
    QSFP28 = 7


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsFormFactor_Enum']


class OpticsLaserState_Enum(Enum):
    """
    OpticsLaserState_Enum

    Optics laser state

    """

    """

    On

    """
    ON = 0

    """

    Off

    """
    OFF = 1

    """

    Unknown

    """
    UNKNOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLaserState_Enum']


class OpticsLedState_Enum(Enum):
    """
    OpticsLedState_Enum

    Optics led state

    """

    """

    Off

    """
    OFF = 0

    """

    Green

    """
    GREEN_ON = 1

    """

    Green Flashing

    """
    GREEN_FLASHING = 2

    """

    Yellow

    """
    YELLOW_ON = 3

    """

    Yellow Flashing

    """
    YELLOW_FLASHING = 4

    """

    Red

    """
    RED_ON = 5

    """

    Red Flashing

    """
    RED_FLASHING = 6


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLedState_Enum']


class OpticsPhy_Enum(Enum):
    """
    OpticsPhy_Enum

    Optics phy type

    """

    """

    Not set

    """
    NOT_SET = 0

    """

    Invalid

    """
    INVALID = 1

    """

    Long reach 4 lanes

    """
    LONG_REACH_FOUR_LANES = 2

    """

    Short reach 10 lanes

    """
    SHORT_REACH_TEN_LANES = 3

    """

    Short reach 1 lane

    """
    SHORT_REACH_ONE_LANE = 4

    """

    Long reach 1 lane

    """
    LONG_REACH_ONE_LANE = 5

    """

    Short reach 4 lanes

    """
    SHORT_REACH_FOUR_LANES = 6

    """

    Copper 4 lanes

    """
    COPPER_FOUR_LANES = 7

    """

    Active optical cable

    """
    ACTIVE_OPTICAL_CABLE = 8

    """

    Long reach 4 lanes

    """
    FOURTY_GIG_E_LONG_REACH_FOUR_LANES = 9

    """

    Short reach 4 lanes

    """
    FOURTY_GIG_E_SHORT_REACH_FOUR_LANES = 10

    """

    CWDM 4 lanes

    """
    CWDM_FOUR_LANES = 11


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsPhy_Enum']


class OpticsTas_Enum(Enum):
    """
    OpticsTas_Enum

    Optics tas

    """

    """

    Out Of Service

    """
    TAS_UI_OOS = 0

    """

    Maintenance

    """
    TAS_UI_MAIN = 1

    """

    In Service

    """
    TAS_UI_IS = 2

    """

    Automatic In Service

    """
    TAS_UI_AINS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsTas_Enum']


class Optics_Enum(Enum):
    """
    Optics_Enum

    Optics

    """

    """

    Unknow Optics Type

    """
    OPTICS_UNKNOWN = 0

    """

    Grey Optics

    """
    OPTICS_GREY = 1

    """

    DWDM Optics

    """
    OPTICS_DWDM = 2

    """

    CWDM Optics

    """
    OPTICS_CWDM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['Optics_Enum']



class OpticsOper(object):
    """
    Optics operational data
    
    .. attribute:: optics_ports
    
    	All Optics Port operational data
    	**type**\: :py:class:`OpticsPorts <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts>`
    
    

    """

    _prefix = 'controller-optics-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.optics_ports = OpticsOper.OpticsPorts()
        self.optics_ports.parent = self


    class OpticsPorts(object):
        """
        All Optics Port operational data
        
        .. attribute:: optics_port
        
        	Optics operational data
        	**type**\: list of :py:class:`OpticsPort <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort>`
        
        

        """

        _prefix = 'controller-optics-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.optics_port = YList()
            self.optics_port.parent = self
            self.optics_port.name = 'optics_port'


        class OpticsPort(object):
            """
            Optics operational data
            
            .. attribute:: name
            
            	Port name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: optics_dwdm_carrrier_channel_map
            
            	Optics operational data
            	**type**\: :py:class:`OpticsDwdmCarrrierChannelMap <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap>`
            
            .. attribute:: optics_info
            
            	Optics operational data
            	**type**\: :py:class:`OpticsInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo>`
            
            

            """

            _prefix = 'controller-optics-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.optics_dwdm_carrrier_channel_map = OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap()
                self.optics_dwdm_carrrier_channel_map.parent = self
                self.optics_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo()
                self.optics_info.parent = self


            class OpticsDwdmCarrrierChannelMap(object):
                """
                Optics operational data
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM carrier band
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: dwdm_carrier_map_info
                
                	DWDM carrier mapping info
                	**type**\: list of :py:class:`DwdmCarrierMapInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo>`
                
                .. attribute:: dwdm_carrier_max
                
                	Highest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_min
                
                	Lowest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_map_info = YList()
                    self.dwdm_carrier_map_info.parent = self
                    self.dwdm_carrier_map_info.name = 'dwdm_carrier_map_info'
                    self.dwdm_carrier_max = None
                    self.dwdm_carrier_min = None


                class DwdmCarrierMapInfo(object):
                    """
                    DWDM carrier mapping info
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: g694_chan_num
                    
                    	G694 channel number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: itu_chan_num
                    
                    	ITU channel number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.frequency = None
                        self.g694_chan_num = None
                        self.itu_chan_num = None
                        self.wavelength = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:dwdm-carrier-map-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.frequency is not None:
                            return True

                        if self.g694_chan_num is not None:
                            return True

                        if self.itu_chan_num is not None:
                            return True

                        if self.wavelength is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-dwdm-carrrier-channel-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_map_info is not None:
                        for child_ref in self.dwdm_carrier_map_info:
                            if child_ref._has_data():
                                return True

                    if self.dwdm_carrier_max is not None:
                        return True

                    if self.dwdm_carrier_min is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info']


            class OpticsInfo(object):
                """
                Optics operational data
                
                .. attribute:: cd
                
                	Chromatic Dispersion ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_high_threshold
                
                	Chromatic Dispersion high threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_low_threshold
                
                	Chromatic Dispersion low threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_max
                
                	Chromatic Dispersion Max ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_min
                
                	Chromatic Dispersion Min ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cfg_tx_power
                
                	Configured Tx power value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\: :py:class:`OpticsControllerState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsControllerState_Enum>`
                
                .. attribute:: dgd_high_threshold
                
                	DGD high threshold in 0.1 ps
                	**type**\: str
                
                .. attribute:: differential_group_delay
                
                	Differential Group Delay ps
                	**type**\: str
                
                .. attribute:: display_volt_temp
                
                	Display Volt/Temp ?
                	**type**\: bool
                
                .. attribute:: dwdm_carrier_band
                
                	DWDM Carrier Band information
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_channel
                
                	Current ITU DWDM Carrier channel number
                	**type**\: str
                
                .. attribute:: dwdm_carrier_frequency
                
                	DWDM Carrier frequency read from hw in the unit 0.01THz
                	**type**\: str
                
                .. attribute:: dwdm_carrier_wavelength
                
                	Wavelength of color optics 0.001nm
                	**type**\: str
                
                .. attribute:: form_factor
                
                	Optics form factor
                	**type**\: :py:class:`OpticsFormFactor_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsFormFactor_Enum>`
                
                .. attribute:: grey_wavelength
                
                	Wavelength of grey optics 0.01nm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lane_data
                
                	Lane information
                	**type**\: list of :py:class:`LaneData <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData>`
                
                .. attribute:: laser_state
                
                	Showing laser state.Either ON or OFF or unknown
                	**type**\: :py:class:`OpticsLaserState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsLaserState_Enum>`
                
                .. attribute:: lbc_high_threshold
                
                	LBC High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: led_state
                
                	Showing Current Colour of led state
                	**type**\: :py:class:`OpticsLedState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsLedState_Enum>`
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\: :py:class:`NetworkSrlgInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo>`
                
                .. attribute:: optical_signal_to_noise_ratio
                
                	Optical Signal to Noise Ratio dB
                	**type**\: str
                
                .. attribute:: optics_alarm_info
                
                	Optics Alarm Information
                	**type**\: :py:class:`OpticsAlarmInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo>`
                
                .. attribute:: optics_module
                
                	Optics module name
                	**type**\: str
                
                .. attribute:: optics_present
                
                	Is Optics Present?
                	**type**\: bool
                
                .. attribute:: optics_type
                
                	Optics type name
                	**type**\: :py:class:`Optics_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.Optics_Enum>`
                
                .. attribute:: osnr_low_threshold
                
                	OSNR low threshold in 0.01 dB
                	**type**\: str
                
                .. attribute:: phase_noise
                
                	Phase Noise dB
                	**type**\: str
                
                .. attribute:: phy_type
                
                	Optics physical type
                	**type**\: :py:class:`OpticsPhy_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsPhy_Enum>`
                
                .. attribute:: pm_enable
                
                	PmEable or Disable
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: polarization_change_rate
                
                	Polarization Change Rate rad/s
                	**type**\: str
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss dB
                	**type**\: str
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion 0.1ps
                	**type**\: str
                
                .. attribute:: rx_high_threshold
                
                	Rx High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_low_threshold
                
                	Rx Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion 0 .1ps^2
                	**type**\: str
                
                .. attribute:: temp_high_threshold
                
                	Temp High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_threshold
                
                	Temp Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\: :py:class:`OpticsTas_Enum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsTas_Enum>`
                
                .. attribute:: tx_high_threshold
                
                	Tx High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_low_threshold
                
                	Tx Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: vendor_info
                
                	Vendor Information
                	**type**\: str
                
                .. attribute:: volt_high_threshold
                
                	Volt High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_threshold
                
                	Volt Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cd = None
                    self.cd_high_threshold = None
                    self.cd_low_threshold = None
                    self.cd_max = None
                    self.cd_min = None
                    self.cfg_tx_power = None
                    self.controller_state = None
                    self.dgd_high_threshold = None
                    self.differential_group_delay = None
                    self.display_volt_temp = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_channel = None
                    self.dwdm_carrier_frequency = None
                    self.dwdm_carrier_wavelength = None
                    self.form_factor = None
                    self.grey_wavelength = None
                    self.lane_data = YList()
                    self.lane_data.parent = self
                    self.lane_data.name = 'lane_data'
                    self.laser_state = None
                    self.lbc_high_threshold = None
                    self.led_state = None
                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self.optical_signal_to_noise_ratio = None
                    self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                    self.optics_alarm_info.parent = self
                    self.optics_module = None
                    self.optics_present = None
                    self.optics_type = None
                    self.osnr_low_threshold = None
                    self.phase_noise = None
                    self.phy_type = None
                    self.pm_enable = None
                    self.polarization_change_rate = None
                    self.polarization_dependent_loss = None
                    self.polarization_mode_dispersion = None
                    self.rx_high_threshold = None
                    self.rx_low_threshold = None
                    self.second_order_polarization_mode_dispersion = None
                    self.temp_high_threshold = None
                    self.temp_low_threshold = None
                    self.transport_admin_state = None
                    self.tx_high_threshold = None
                    self.tx_low_threshold = None
                    self.vendor_info = None
                    self.volt_high_threshold = None
                    self.volt_low_threshold = None


                class LaneData(object):
                    """
                    Lane information
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01%
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the unit of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lane_index = None
                        self.laser_bias_current_milli_amps = None
                        self.laser_bias_current_percent = None
                        self.receive_power = None
                        self.transmit_power = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:lane-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.lane_index is not None:
                            return True

                        if self.laser_bias_current_milli_amps is not None:
                            return True

                        if self.laser_bias_current_percent is not None:
                            return True

                        if self.receive_power is not None:
                            return True

                        if self.transmit_power is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info']


                class NetworkSrlgInfo(object):
                    """
                    Network SRLG information
                    
                    .. attribute:: network_srlg
                    
                    	Network Srlg
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.network_srlg = []

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:network-srlg-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.network_srlg is not None:
                            for child in self.network_srlg:
                                if child is not None:
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info']


                class OpticsAlarmInfo(object):
                    """
                    Optics Alarm Information
                    
                    .. attribute:: hidgd
                    
                    	HI DGD
                    	**type**\: :py:class:`Hidgd <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd>`
                    
                    .. attribute:: high_lbc
                    
                    	High laser bias current
                    	**type**\: :py:class:`HighLbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc>`
                    
                    .. attribute:: high_rx1_power
                    
                    	High Rx1 Power
                    	**type**\: :py:class:`HighRx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power>`
                    
                    .. attribute:: high_rx2_power
                    
                    	High Rx2 Power
                    	**type**\: :py:class:`HighRx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power>`
                    
                    .. attribute:: high_rx3_power
                    
                    	High Rx3 Power
                    	**type**\: :py:class:`HighRx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power>`
                    
                    .. attribute:: high_rx4_power
                    
                    	High Rx4 Power
                    	**type**\: :py:class:`HighRx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power>`
                    
                    .. attribute:: high_rx_power
                    
                    	High Rx Power
                    	**type**\: :py:class:`HighRxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower>`
                    
                    .. attribute:: high_tx1_power
                    
                    	High Tx1 Power
                    	**type**\: :py:class:`HighTx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power>`
                    
                    .. attribute:: high_tx1lbc
                    
                    	High Tx1 laser bias current
                    	**type**\: :py:class:`HighTx1lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc>`
                    
                    .. attribute:: high_tx2_power
                    
                    	High Tx2 Power
                    	**type**\: :py:class:`HighTx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power>`
                    
                    .. attribute:: high_tx2lbc
                    
                    	High Tx2 laser bias current
                    	**type**\: :py:class:`HighTx2lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc>`
                    
                    .. attribute:: high_tx3_power
                    
                    	High Tx3 Power
                    	**type**\: :py:class:`HighTx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power>`
                    
                    .. attribute:: high_tx3lbc
                    
                    	High Tx3 laser bias current
                    	**type**\: :py:class:`HighTx3lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc>`
                    
                    .. attribute:: high_tx4_power
                    
                    	High Tx4 Power
                    	**type**\: :py:class:`HighTx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power>`
                    
                    .. attribute:: high_tx4lbc
                    
                    	High Tx4 laser bias current
                    	**type**\: :py:class:`HighTx4lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc>`
                    
                    .. attribute:: high_tx_power
                    
                    	High Tx Power
                    	**type**\: :py:class:`HighTxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower>`
                    
                    .. attribute:: imp_removal
                    
                    	IMPROPER REM
                    	**type**\: :py:class:`ImpRemoval <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval>`
                    
                    .. attribute:: low_rx1_power
                    
                    	Low Rx1 Power
                    	**type**\: :py:class:`LowRx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power>`
                    
                    .. attribute:: low_rx2_power
                    
                    	Low Rx2 Power
                    	**type**\: :py:class:`LowRx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power>`
                    
                    .. attribute:: low_rx3_power
                    
                    	Low Rx3 Power
                    	**type**\: :py:class:`LowRx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power>`
                    
                    .. attribute:: low_rx4_power
                    
                    	Low Rx4 Power
                    	**type**\: :py:class:`LowRx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power
                    	**type**\: :py:class:`LowRxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: low_tx1_power
                    
                    	Low Tx1 Power
                    	**type**\: :py:class:`LowTx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power>`
                    
                    .. attribute:: low_tx1lbc
                    
                    	Low Tx1 laser bias current
                    	**type**\: :py:class:`LowTx1lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc>`
                    
                    .. attribute:: low_tx2_power
                    
                    	Low Tx2 Power
                    	**type**\: :py:class:`LowTx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power>`
                    
                    .. attribute:: low_tx2lbc
                    
                    	Low Tx2 laser bias current
                    	**type**\: :py:class:`LowTx2lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc>`
                    
                    .. attribute:: low_tx3_power
                    
                    	Low Tx3 Power
                    	**type**\: :py:class:`LowTx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power>`
                    
                    .. attribute:: low_tx3lbc
                    
                    	Low Tx3 laser bias current
                    	**type**\: :py:class:`LowTx3lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc>`
                    
                    .. attribute:: low_tx4_power
                    
                    	Low Tx4 Power
                    	**type**\: :py:class:`LowTx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power>`
                    
                    .. attribute:: low_tx4lbc
                    
                    	Low Tx4 laser bias current
                    	**type**\: :py:class:`LowTx4lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc>`
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power
                    	**type**\: :py:class:`LowTxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower>`
                    
                    .. attribute:: mea
                    
                    	MEA
                    	**type**\: :py:class:`Mea <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea>`
                    
                    .. attribute:: oorcd
                    
                    	OOR CD
                    	**type**\: :py:class:`Oorcd <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd>`
                    
                    .. attribute:: osnr
                    
                    	OSNR
                    	**type**\: :py:class:`Osnr <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr>`
                    
                    .. attribute:: rx_lol
                    
                    	RX LOL
                    	**type**\: :py:class:`RxLol <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol>`
                    
                    .. attribute:: rx_los
                    
                    	RX LOS
                    	**type**\: :py:class:`RxLos <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos>`
                    
                    .. attribute:: tx_fault
                    
                    	TX Fault
                    	**type**\: :py:class:`TxFault <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault>`
                    
                    .. attribute:: tx_lol
                    
                    	TX LOL
                    	**type**\: :py:class:`TxLol <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol>`
                    
                    .. attribute:: tx_los
                    
                    	TX LOS
                    	**type**\: :py:class:`TxLos <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos>`
                    
                    .. attribute:: wvlool
                    
                    	WVL OOL
                    	**type**\: :py:class:`Wvlool <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                        self.hidgd.parent = self
                        self.high_lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc()
                        self.high_lbc.parent = self
                        self.high_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power()
                        self.high_rx1_power.parent = self
                        self.high_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power()
                        self.high_rx2_power.parent = self
                        self.high_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power()
                        self.high_rx3_power.parent = self
                        self.high_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power()
                        self.high_rx4_power.parent = self
                        self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                        self.high_rx_power.parent = self
                        self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                        self.high_tx1_power.parent = self
                        self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc()
                        self.high_tx1lbc.parent = self
                        self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                        self.high_tx2_power.parent = self
                        self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc()
                        self.high_tx2lbc.parent = self
                        self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                        self.high_tx3_power.parent = self
                        self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc()
                        self.high_tx3lbc.parent = self
                        self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                        self.high_tx4_power.parent = self
                        self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc()
                        self.high_tx4lbc.parent = self
                        self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                        self.high_tx_power.parent = self
                        self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                        self.imp_removal.parent = self
                        self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                        self.low_rx1_power.parent = self
                        self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                        self.low_rx2_power.parent = self
                        self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                        self.low_rx3_power.parent = self
                        self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                        self.low_rx4_power.parent = self
                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                        self.low_tx1_power.parent = self
                        self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc()
                        self.low_tx1lbc.parent = self
                        self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                        self.low_tx2_power.parent = self
                        self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc()
                        self.low_tx2lbc.parent = self
                        self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                        self.low_tx3_power.parent = self
                        self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc()
                        self.low_tx3lbc.parent = self
                        self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                        self.low_tx4_power.parent = self
                        self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc()
                        self.low_tx4lbc.parent = self
                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
                        self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                        self.mea.parent = self
                        self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                        self.oorcd.parent = self
                        self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                        self.osnr.parent = self
                        self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                        self.rx_lol.parent = self
                        self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                        self.rx_los.parent = self
                        self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                        self.tx_fault.parent = self
                        self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                        self.tx_lol.parent = self
                        self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                        self.tx_los.parent = self
                        self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                        self.wvlool.parent = self


                    class Hidgd(object):
                        """
                        HI DGD
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:hidgd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd']['meta_info']


                    class HighLbc(object):
                        """
                        High laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc']['meta_info']


                    class HighRx1Power(object):
                        """
                        High Rx1 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power']['meta_info']


                    class HighRx2Power(object):
                        """
                        High Rx2 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power']['meta_info']


                    class HighRx3Power(object):
                        """
                        High Rx3 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power']['meta_info']


                    class HighRx4Power(object):
                        """
                        High Rx4 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power']['meta_info']


                    class HighRxPower(object):
                        """
                        High Rx Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-rx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower']['meta_info']


                    class HighTx1Power(object):
                        """
                        High Tx1 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power']['meta_info']


                    class HighTx1lbc(object):
                        """
                        High Tx1 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx1lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc']['meta_info']


                    class HighTx2Power(object):
                        """
                        High Tx2 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power']['meta_info']


                    class HighTx2lbc(object):
                        """
                        High Tx2 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx2lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc']['meta_info']


                    class HighTx3Power(object):
                        """
                        High Tx3 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power']['meta_info']


                    class HighTx3lbc(object):
                        """
                        High Tx3 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx3lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc']['meta_info']


                    class HighTx4Power(object):
                        """
                        High Tx4 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power']['meta_info']


                    class HighTx4lbc(object):
                        """
                        High Tx4 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx4lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc']['meta_info']


                    class HighTxPower(object):
                        """
                        High Tx Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:high-tx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower']['meta_info']


                    class ImpRemoval(object):
                        """
                        IMPROPER REM
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:imp-removal'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval']['meta_info']


                    class LowRx1Power(object):
                        """
                        Low Rx1 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power']['meta_info']


                    class LowRx2Power(object):
                        """
                        Low Rx2 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power']['meta_info']


                    class LowRx3Power(object):
                        """
                        Low Rx3 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power']['meta_info']


                    class LowRx4Power(object):
                        """
                        Low Rx4 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power']['meta_info']


                    class LowRxPower(object):
                        """
                        Low Rx Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-rx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower']['meta_info']


                    class LowTx1Power(object):
                        """
                        Low Tx1 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx1-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power']['meta_info']


                    class LowTx1lbc(object):
                        """
                        Low Tx1 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx1lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc']['meta_info']


                    class LowTx2Power(object):
                        """
                        Low Tx2 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx2-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power']['meta_info']


                    class LowTx2lbc(object):
                        """
                        Low Tx2 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx2lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc']['meta_info']


                    class LowTx3Power(object):
                        """
                        Low Tx3 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx3-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power']['meta_info']


                    class LowTx3lbc(object):
                        """
                        Low Tx3 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx3lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc']['meta_info']


                    class LowTx4Power(object):
                        """
                        Low Tx4 Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx4-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power']['meta_info']


                    class LowTx4lbc(object):
                        """
                        Low Tx4 laser bias current
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx4lbc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc']['meta_info']


                    class LowTxPower(object):
                        """
                        Low Tx Power
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:low-tx-power'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower']['meta_info']


                    class Mea(object):
                        """
                        MEA
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:mea'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea']['meta_info']


                    class Oorcd(object):
                        """
                        OOR CD
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:oorcd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd']['meta_info']


                    class Osnr(object):
                        """
                        OSNR
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:osnr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr']['meta_info']


                    class RxLol(object):
                        """
                        RX LOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-lol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol']['meta_info']


                    class RxLos(object):
                        """
                        RX LOS
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:rx-los'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos']['meta_info']


                    class TxFault(object):
                        """
                        TX Fault
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-fault'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault']['meta_info']


                    class TxLol(object):
                        """
                        TX LOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-lol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol']['meta_info']


                    class TxLos(object):
                        """
                        TX LOS
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:tx-los'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos']['meta_info']


                    class Wvlool(object):
                        """
                        WVL OOL
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_detected = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:wvlool'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.counter is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.hidgd is not None and self.hidgd._has_data():
                            return True

                        if self.hidgd is not None and self.hidgd.is_presence():
                            return True

                        if self.high_lbc is not None and self.high_lbc._has_data():
                            return True

                        if self.high_lbc is not None and self.high_lbc.is_presence():
                            return True

                        if self.high_rx1_power is not None and self.high_rx1_power._has_data():
                            return True

                        if self.high_rx1_power is not None and self.high_rx1_power.is_presence():
                            return True

                        if self.high_rx2_power is not None and self.high_rx2_power._has_data():
                            return True

                        if self.high_rx2_power is not None and self.high_rx2_power.is_presence():
                            return True

                        if self.high_rx3_power is not None and self.high_rx3_power._has_data():
                            return True

                        if self.high_rx3_power is not None and self.high_rx3_power.is_presence():
                            return True

                        if self.high_rx4_power is not None and self.high_rx4_power._has_data():
                            return True

                        if self.high_rx4_power is not None and self.high_rx4_power.is_presence():
                            return True

                        if self.high_rx_power is not None and self.high_rx_power._has_data():
                            return True

                        if self.high_rx_power is not None and self.high_rx_power.is_presence():
                            return True

                        if self.high_tx1_power is not None and self.high_tx1_power._has_data():
                            return True

                        if self.high_tx1_power is not None and self.high_tx1_power.is_presence():
                            return True

                        if self.high_tx1lbc is not None and self.high_tx1lbc._has_data():
                            return True

                        if self.high_tx1lbc is not None and self.high_tx1lbc.is_presence():
                            return True

                        if self.high_tx2_power is not None and self.high_tx2_power._has_data():
                            return True

                        if self.high_tx2_power is not None and self.high_tx2_power.is_presence():
                            return True

                        if self.high_tx2lbc is not None and self.high_tx2lbc._has_data():
                            return True

                        if self.high_tx2lbc is not None and self.high_tx2lbc.is_presence():
                            return True

                        if self.high_tx3_power is not None and self.high_tx3_power._has_data():
                            return True

                        if self.high_tx3_power is not None and self.high_tx3_power.is_presence():
                            return True

                        if self.high_tx3lbc is not None and self.high_tx3lbc._has_data():
                            return True

                        if self.high_tx3lbc is not None and self.high_tx3lbc.is_presence():
                            return True

                        if self.high_tx4_power is not None and self.high_tx4_power._has_data():
                            return True

                        if self.high_tx4_power is not None and self.high_tx4_power.is_presence():
                            return True

                        if self.high_tx4lbc is not None and self.high_tx4lbc._has_data():
                            return True

                        if self.high_tx4lbc is not None and self.high_tx4lbc.is_presence():
                            return True

                        if self.high_tx_power is not None and self.high_tx_power._has_data():
                            return True

                        if self.high_tx_power is not None and self.high_tx_power.is_presence():
                            return True

                        if self.imp_removal is not None and self.imp_removal._has_data():
                            return True

                        if self.imp_removal is not None and self.imp_removal.is_presence():
                            return True

                        if self.low_rx1_power is not None and self.low_rx1_power._has_data():
                            return True

                        if self.low_rx1_power is not None and self.low_rx1_power.is_presence():
                            return True

                        if self.low_rx2_power is not None and self.low_rx2_power._has_data():
                            return True

                        if self.low_rx2_power is not None and self.low_rx2_power.is_presence():
                            return True

                        if self.low_rx3_power is not None and self.low_rx3_power._has_data():
                            return True

                        if self.low_rx3_power is not None and self.low_rx3_power.is_presence():
                            return True

                        if self.low_rx4_power is not None and self.low_rx4_power._has_data():
                            return True

                        if self.low_rx4_power is not None and self.low_rx4_power.is_presence():
                            return True

                        if self.low_rx_power is not None and self.low_rx_power._has_data():
                            return True

                        if self.low_rx_power is not None and self.low_rx_power.is_presence():
                            return True

                        if self.low_tx1_power is not None and self.low_tx1_power._has_data():
                            return True

                        if self.low_tx1_power is not None and self.low_tx1_power.is_presence():
                            return True

                        if self.low_tx1lbc is not None and self.low_tx1lbc._has_data():
                            return True

                        if self.low_tx1lbc is not None and self.low_tx1lbc.is_presence():
                            return True

                        if self.low_tx2_power is not None and self.low_tx2_power._has_data():
                            return True

                        if self.low_tx2_power is not None and self.low_tx2_power.is_presence():
                            return True

                        if self.low_tx2lbc is not None and self.low_tx2lbc._has_data():
                            return True

                        if self.low_tx2lbc is not None and self.low_tx2lbc.is_presence():
                            return True

                        if self.low_tx3_power is not None and self.low_tx3_power._has_data():
                            return True

                        if self.low_tx3_power is not None and self.low_tx3_power.is_presence():
                            return True

                        if self.low_tx3lbc is not None and self.low_tx3lbc._has_data():
                            return True

                        if self.low_tx3lbc is not None and self.low_tx3lbc.is_presence():
                            return True

                        if self.low_tx4_power is not None and self.low_tx4_power._has_data():
                            return True

                        if self.low_tx4_power is not None and self.low_tx4_power.is_presence():
                            return True

                        if self.low_tx4lbc is not None and self.low_tx4lbc._has_data():
                            return True

                        if self.low_tx4lbc is not None and self.low_tx4lbc.is_presence():
                            return True

                        if self.low_tx_power is not None and self.low_tx_power._has_data():
                            return True

                        if self.low_tx_power is not None and self.low_tx_power.is_presence():
                            return True

                        if self.mea is not None and self.mea._has_data():
                            return True

                        if self.mea is not None and self.mea.is_presence():
                            return True

                        if self.oorcd is not None and self.oorcd._has_data():
                            return True

                        if self.oorcd is not None and self.oorcd.is_presence():
                            return True

                        if self.osnr is not None and self.osnr._has_data():
                            return True

                        if self.osnr is not None and self.osnr.is_presence():
                            return True

                        if self.rx_lol is not None and self.rx_lol._has_data():
                            return True

                        if self.rx_lol is not None and self.rx_lol.is_presence():
                            return True

                        if self.rx_los is not None and self.rx_los._has_data():
                            return True

                        if self.rx_los is not None and self.rx_los.is_presence():
                            return True

                        if self.tx_fault is not None and self.tx_fault._has_data():
                            return True

                        if self.tx_fault is not None and self.tx_fault.is_presence():
                            return True

                        if self.tx_lol is not None and self.tx_lol._has_data():
                            return True

                        if self.tx_lol is not None and self.tx_lol.is_presence():
                            return True

                        if self.tx_los is not None and self.tx_los._has_data():
                            return True

                        if self.tx_los is not None and self.tx_los.is_presence():
                            return True

                        if self.wvlool is not None and self.wvlool._has_data():
                            return True

                        if self.wvlool is not None and self.wvlool.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-optics-oper:optics-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.cd is not None:
                        return True

                    if self.cd_high_threshold is not None:
                        return True

                    if self.cd_low_threshold is not None:
                        return True

                    if self.cd_max is not None:
                        return True

                    if self.cd_min is not None:
                        return True

                    if self.cfg_tx_power is not None:
                        return True

                    if self.controller_state is not None:
                        return True

                    if self.dgd_high_threshold is not None:
                        return True

                    if self.differential_group_delay is not None:
                        return True

                    if self.display_volt_temp is not None:
                        return True

                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_channel is not None:
                        return True

                    if self.dwdm_carrier_frequency is not None:
                        return True

                    if self.dwdm_carrier_wavelength is not None:
                        return True

                    if self.form_factor is not None:
                        return True

                    if self.grey_wavelength is not None:
                        return True

                    if self.lane_data is not None:
                        for child_ref in self.lane_data:
                            if child_ref._has_data():
                                return True

                    if self.laser_state is not None:
                        return True

                    if self.lbc_high_threshold is not None:
                        return True

                    if self.led_state is not None:
                        return True

                    if self.network_srlg_info is not None and self.network_srlg_info._has_data():
                        return True

                    if self.network_srlg_info is not None and self.network_srlg_info.is_presence():
                        return True

                    if self.optical_signal_to_noise_ratio is not None:
                        return True

                    if self.optics_alarm_info is not None and self.optics_alarm_info._has_data():
                        return True

                    if self.optics_alarm_info is not None and self.optics_alarm_info.is_presence():
                        return True

                    if self.optics_module is not None:
                        return True

                    if self.optics_present is not None:
                        return True

                    if self.optics_type is not None:
                        return True

                    if self.osnr_low_threshold is not None:
                        return True

                    if self.phase_noise is not None:
                        return True

                    if self.phy_type is not None:
                        return True

                    if self.pm_enable is not None:
                        return True

                    if self.polarization_change_rate is not None:
                        return True

                    if self.polarization_dependent_loss is not None:
                        return True

                    if self.polarization_mode_dispersion is not None:
                        return True

                    if self.rx_high_threshold is not None:
                        return True

                    if self.rx_low_threshold is not None:
                        return True

                    if self.second_order_polarization_mode_dispersion is not None:
                        return True

                    if self.temp_high_threshold is not None:
                        return True

                    if self.temp_low_threshold is not None:
                        return True

                    if self.transport_admin_state is not None:
                        return True

                    if self.tx_high_threshold is not None:
                        return True

                    if self.tx_low_threshold is not None:
                        return True

                    if self.vendor_info is not None:
                        return True

                    if self.volt_high_threshold is not None:
                        return True

                    if self.volt_low_threshold is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-controller-optics-oper:optics-oper/Cisco-IOS-XR-controller-optics-oper:optics-ports/Cisco-IOS-XR-controller-optics-oper:optics-port[Cisco-IOS-XR-controller-optics-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.name is not None:
                    return True

                if self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map._has_data():
                    return True

                if self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map.is_presence():
                    return True

                if self.optics_info is not None and self.optics_info._has_data():
                    return True

                if self.optics_info is not None and self.optics_info.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-controller-optics-oper:optics-oper/Cisco-IOS-XR-controller-optics-oper:optics-ports'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.optics_port is not None:
                for child_ref in self.optics_port:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
            return meta._meta_table['OpticsOper.OpticsPorts']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-controller-optics-oper:optics-oper'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.optics_ports is not None and self.optics_ports._has_data():
            return True

        if self.optics_ports is not None and self.optics_ports.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsOper']['meta_info']



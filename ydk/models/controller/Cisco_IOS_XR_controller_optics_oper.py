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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class OpticsControllerStateEnum(Enum):
    """
    OpticsControllerStateEnum

    Optics controller state

    .. data:: OPTICS_STATE_UP = 0

    	Up

    .. data:: OPTICS_STATE_DOWN = 1

    	Down

    .. data:: OPTICS_STATE_ADMIN_DOWN = 2

    	Administratively Down

    """

    OPTICS_STATE_UP = 0

    OPTICS_STATE_DOWN = 1

    OPTICS_STATE_ADMIN_DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsControllerStateEnum']


class OpticsEnum(Enum):
    """
    OpticsEnum

    Optics

    .. data:: OPTICS_UNKNOWN = 0

    	Unknow Optics Type

    .. data:: OPTICS_GREY = 1

    	Grey Optics

    .. data:: OPTICS_DWDM = 2

    	DWDM Optics

    .. data:: OPTICS_CWDM = 3

    	CWDM Optics

    """

    OPTICS_UNKNOWN = 0

    OPTICS_GREY = 1

    OPTICS_DWDM = 2

    OPTICS_CWDM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsEnum']


class OpticsFormFactorEnum(Enum):
    """
    OpticsFormFactorEnum

    Optics form factor

    .. data:: NOT_SET = 0

    	Not set

    .. data:: INVALID = 1

    	Invalid

    .. data:: CPAK = 2

    	CPAK

    .. data:: CXP = 3

    	CXP

    .. data:: SFP_PLUS = 4

    	SFP+

    .. data:: QSFP = 5

    	QSFP

    .. data:: QSFP_PLUS = 6

    	QSFP+

    .. data:: QSFP28 = 7

    	QSFP28

    """

    NOT_SET = 0

    INVALID = 1

    CPAK = 2

    CXP = 3

    SFP_PLUS = 4

    QSFP = 5

    QSFP_PLUS = 6

    QSFP28 = 7


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsFormFactorEnum']


class OpticsLaserStateEnum(Enum):
    """
    OpticsLaserStateEnum

    Optics laser state

    .. data:: ON = 0

    	On

    .. data:: OFF = 1

    	Off

    .. data:: UNKNOWN = 2

    	Unknown

    """

    ON = 0

    OFF = 1

    UNKNOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLaserStateEnum']


class OpticsLedStateEnum(Enum):
    """
    OpticsLedStateEnum

    Optics led state

    .. data:: OFF = 0

    	Off

    .. data:: GREEN_ON = 1

    	Green

    .. data:: GREEN_FLASHING = 2

    	Green Flashing

    .. data:: YELLOW_ON = 3

    	Yellow

    .. data:: YELLOW_FLASHING = 4

    	Yellow Flashing

    .. data:: RED_ON = 5

    	Red

    .. data:: RED_FLASHING = 6

    	Red Flashing

    """

    OFF = 0

    GREEN_ON = 1

    GREEN_FLASHING = 2

    YELLOW_ON = 3

    YELLOW_FLASHING = 4

    RED_ON = 5

    RED_FLASHING = 6


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsLedStateEnum']


class OpticsPhyEnum(Enum):
    """
    OpticsPhyEnum

    Optics phy type

    .. data:: NOT_SET = 0

    	Not set

    .. data:: INVALID = 1

    	Invalid

    .. data:: LONG_REACH_FOUR_LANES = 2

    	Long reach 4 lanes

    .. data:: SHORT_REACH_TEN_LANES = 3

    	Short reach 10 lanes

    .. data:: SHORT_REACH_ONE_LANE = 4

    	Short reach 1 lane

    .. data:: LONG_REACH_ONE_LANE = 5

    	Long reach 1 lane

    .. data:: SHORT_REACH_FOUR_LANES = 6

    	Short reach 4 lanes

    .. data:: COPPER_FOUR_LANES = 7

    	Copper 4 lanes

    .. data:: ACTIVE_OPTICAL_CABLE = 8

    	Active optical cable

    .. data:: FOURTY_GIG_E_LONG_REACH_FOUR_LANES = 9

    	Long reach 4 lanes

    .. data:: FOURTY_GIG_E_SHORT_REACH_FOUR_LANES = 10

    	Short reach 4 lanes

    .. data:: CWDM_FOUR_LANES = 11

    	CWDM 4 lanes

    """

    NOT_SET = 0

    INVALID = 1

    LONG_REACH_FOUR_LANES = 2

    SHORT_REACH_TEN_LANES = 3

    SHORT_REACH_ONE_LANE = 4

    LONG_REACH_ONE_LANE = 5

    SHORT_REACH_FOUR_LANES = 6

    COPPER_FOUR_LANES = 7

    ACTIVE_OPTICAL_CABLE = 8

    FOURTY_GIG_E_LONG_REACH_FOUR_LANES = 9

    FOURTY_GIG_E_SHORT_REACH_FOUR_LANES = 10

    CWDM_FOUR_LANES = 11


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsPhyEnum']


class OpticsTasEnum(Enum):
    """
    OpticsTasEnum

    Optics tas

    .. data:: TAS_UI_OOS = 0

    	Out Of Service

    .. data:: TAS_UI_MAIN = 1

    	Maintenance

    .. data:: TAS_UI_IS = 2

    	In Service

    .. data:: TAS_UI_AINS = 3

    	Automatic In Service

    """

    TAS_UI_OOS = 0

    TAS_UI_MAIN = 1

    TAS_UI_IS = 2

    TAS_UI_AINS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsTasEnum']



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
            
            .. attribute:: name  <key>
            
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
                
                .. attribute:: dwdm_carrier_min
                
                	Lowest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_max
                
                	Highest DWDM carrier supported
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dwdm_carrier_map_info
                
                	DWDM carrier mapping info
                	**type**\: list of :py:class:`DwdmCarrierMapInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_min = None
                    self.dwdm_carrier_max = None
                    self.dwdm_carrier_map_info = YList()
                    self.dwdm_carrier_map_info.parent = self
                    self.dwdm_carrier_map_info.name = 'dwdm_carrier_map_info'


                class DwdmCarrierMapInfo(object):
                    """
                    DWDM carrier mapping info
                    
                    .. attribute:: itu_chan_num
                    
                    	ITU channel number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: g694_chan_num
                    
                    	G694 channel number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: frequency
                    
                    	Frequency
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: wavelength
                    
                    	Wavelength
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.itu_chan_num = None
                        self.g694_chan_num = None
                        self.frequency = None
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
                        if self.itu_chan_num is not None:
                            return True

                        if self.g694_chan_num is not None:
                            return True

                        if self.frequency is not None:
                            return True

                        if self.wavelength is not None:
                            return True

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
                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_min is not None:
                        return True

                    if self.dwdm_carrier_max is not None:
                        return True

                    if self.dwdm_carrier_map_info is not None:
                        for child_ref in self.dwdm_carrier_map_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                    return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info']


            class OpticsInfo(object):
                """
                Optics operational data
                
                .. attribute:: network_srlg_info
                
                	Network SRLG information
                	**type**\: :py:class:`NetworkSrlgInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo>`
                
                .. attribute:: optics_alarm_info
                
                	Optics Alarm Information
                	**type**\: :py:class:`OpticsAlarmInfo <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo>`
                
                .. attribute:: transport_admin_state
                
                	Transport Admin State
                	**type**\: :py:class:`OpticsTasEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsTasEnum>`
                
                .. attribute:: optics_present
                
                	Is Optics Present?
                	**type**\: bool
                
                .. attribute:: optics_type
                
                	Optics type name
                	**type**\: :py:class:`OpticsEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsEnum>`
                
                .. attribute:: optics_module
                
                	Optics module name
                	**type**\: str
                
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
                
                .. attribute:: grey_wavelength
                
                	Wavelength of grey optics 0.01nm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rx_low_threshold
                
                	Rx Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: rx_high_threshold
                
                	Rx High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: lbc_high_threshold
                
                	LBC High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_low_threshold
                
                	Tx Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tx_high_threshold
                
                	Tx High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_low_threshold
                
                	Temp Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: temp_high_threshold
                
                	Temp High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_low_threshold
                
                	Volt Low threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: volt_high_threshold
                
                	Volt High threshold value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd
                
                	Chromatic Dispersion ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_min
                
                	Chromatic Dispersion Min ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_max
                
                	Chromatic Dispersion Max ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_low_threshold
                
                	Chromatic Dispersion low threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cd_high_threshold
                
                	Chromatic Dispersion high threshold ps/nm
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: osnr_low_threshold
                
                	OSNR low threshold in 0.01 dB
                	**type**\: str
                
                .. attribute:: dgd_high_threshold
                
                	DGD high threshold in 0.1 ps
                	**type**\: str
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion 0.1ps
                	**type**\: str
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion 0 .1ps^2
                	**type**\: str
                
                .. attribute:: optical_signal_to_noise_ratio
                
                	Optical Signal to Noise Ratio dB
                	**type**\: str
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss dB
                	**type**\: str
                
                .. attribute:: polarization_change_rate
                
                	Polarization Change Rate rad/s
                	**type**\: str
                
                .. attribute:: differential_group_delay
                
                	Differential Group Delay ps
                	**type**\: str
                
                .. attribute:: phase_noise
                
                	Phase Noise dB
                	**type**\: str
                
                .. attribute:: pm_enable
                
                	PmEable or Disable
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: laser_state
                
                	Showing laser state.Either ON or OFF or unknown
                	**type**\: :py:class:`OpticsLaserStateEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsLaserStateEnum>`
                
                .. attribute:: led_state
                
                	Showing Current Colour of led state
                	**type**\: :py:class:`OpticsLedStateEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsLedStateEnum>`
                
                .. attribute:: controller_state
                
                	Optics controller state\: Up, Down or Administratively Down
                	**type**\: :py:class:`OpticsControllerStateEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsControllerStateEnum>`
                
                .. attribute:: form_factor
                
                	Optics form factor
                	**type**\: :py:class:`OpticsFormFactorEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsFormFactorEnum>`
                
                .. attribute:: phy_type
                
                	Optics physical type
                	**type**\: :py:class:`OpticsPhyEnum <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsPhyEnum>`
                
                .. attribute:: cfg_tx_power
                
                	Configured Tx power value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: vendor_info
                
                	Vendor Information
                	**type**\: str
                
                .. attribute:: display_volt_temp
                
                	Display Volt/Temp ?
                	**type**\: bool
                
                .. attribute:: lane_data
                
                	Lane information
                	**type**\: list of :py:class:`LaneData <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData>`
                
                

                """

                _prefix = 'controller-optics-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.network_srlg_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo()
                    self.network_srlg_info.parent = self
                    self.optics_alarm_info = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo()
                    self.optics_alarm_info.parent = self
                    self.transport_admin_state = None
                    self.optics_present = None
                    self.optics_type = None
                    self.optics_module = None
                    self.dwdm_carrier_band = None
                    self.dwdm_carrier_channel = None
                    self.dwdm_carrier_frequency = None
                    self.dwdm_carrier_wavelength = None
                    self.grey_wavelength = None
                    self.rx_low_threshold = None
                    self.rx_high_threshold = None
                    self.lbc_high_threshold = None
                    self.tx_low_threshold = None
                    self.tx_high_threshold = None
                    self.temp_low_threshold = None
                    self.temp_high_threshold = None
                    self.volt_low_threshold = None
                    self.volt_high_threshold = None
                    self.cd = None
                    self.cd_min = None
                    self.cd_max = None
                    self.cd_low_threshold = None
                    self.cd_high_threshold = None
                    self.osnr_low_threshold = None
                    self.dgd_high_threshold = None
                    self.polarization_mode_dispersion = None
                    self.second_order_polarization_mode_dispersion = None
                    self.optical_signal_to_noise_ratio = None
                    self.polarization_dependent_loss = None
                    self.polarization_change_rate = None
                    self.differential_group_delay = None
                    self.phase_noise = None
                    self.pm_enable = None
                    self.laser_state = None
                    self.led_state = None
                    self.controller_state = None
                    self.form_factor = None
                    self.phy_type = None
                    self.cfg_tx_power = None
                    self.vendor_info = None
                    self.display_volt_temp = None
                    self.lane_data = YList()
                    self.lane_data.parent = self
                    self.lane_data.name = 'lane_data'


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
                        self.network_srlg = YLeafList()
                        self.network_srlg.parent = self
                        self.network_srlg.name = 'network_srlg'

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
                        if self.network_srlg is not None:
                            for child in self.network_srlg:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info']


                class OpticsAlarmInfo(object):
                    """
                    Optics Alarm Information
                    
                    .. attribute:: high_rx_power
                    
                    	High Rx Power
                    	**type**\: :py:class:`HighRxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower>`
                    
                    .. attribute:: low_rx_power
                    
                    	Low Rx Power
                    	**type**\: :py:class:`LowRxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower>`
                    
                    .. attribute:: high_tx_power
                    
                    	High Tx Power
                    	**type**\: :py:class:`HighTxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower>`
                    
                    .. attribute:: low_tx_power
                    
                    	Low Tx Power
                    	**type**\: :py:class:`LowTxPower <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower>`
                    
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
                    
                    .. attribute:: high_tx1_power
                    
                    	High Tx1 Power
                    	**type**\: :py:class:`HighTx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power>`
                    
                    .. attribute:: high_tx2_power
                    
                    	High Tx2 Power
                    	**type**\: :py:class:`HighTx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power>`
                    
                    .. attribute:: high_tx3_power
                    
                    	High Tx3 Power
                    	**type**\: :py:class:`HighTx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power>`
                    
                    .. attribute:: high_tx4_power
                    
                    	High Tx4 Power
                    	**type**\: :py:class:`HighTx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power>`
                    
                    .. attribute:: low_tx1_power
                    
                    	Low Tx1 Power
                    	**type**\: :py:class:`LowTx1Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power>`
                    
                    .. attribute:: low_tx2_power
                    
                    	Low Tx2 Power
                    	**type**\: :py:class:`LowTx2Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power>`
                    
                    .. attribute:: low_tx3_power
                    
                    	Low Tx3 Power
                    	**type**\: :py:class:`LowTx3Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power>`
                    
                    .. attribute:: low_tx4_power
                    
                    	Low Tx4 Power
                    	**type**\: :py:class:`LowTx4Power <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power>`
                    
                    .. attribute:: high_tx1lbc
                    
                    	High Tx1 laser bias current
                    	**type**\: :py:class:`HighTx1Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc>`
                    
                    .. attribute:: high_tx2lbc
                    
                    	High Tx2 laser bias current
                    	**type**\: :py:class:`HighTx2Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc>`
                    
                    .. attribute:: high_tx3lbc
                    
                    	High Tx3 laser bias current
                    	**type**\: :py:class:`HighTx3Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc>`
                    
                    .. attribute:: high_tx4lbc
                    
                    	High Tx4 laser bias current
                    	**type**\: :py:class:`HighTx4Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc>`
                    
                    .. attribute:: low_tx1lbc
                    
                    	Low Tx1 laser bias current
                    	**type**\: :py:class:`LowTx1Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc>`
                    
                    .. attribute:: low_tx2lbc
                    
                    	Low Tx2 laser bias current
                    	**type**\: :py:class:`LowTx2Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc>`
                    
                    .. attribute:: low_tx3lbc
                    
                    	Low Tx3 laser bias current
                    	**type**\: :py:class:`LowTx3Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc>`
                    
                    .. attribute:: low_tx4lbc
                    
                    	Low Tx4 laser bias current
                    	**type**\: :py:class:`LowTx4Lbc <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc>`
                    
                    .. attribute:: rx_los
                    
                    	RX LOS
                    	**type**\: :py:class:`RxLos <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos>`
                    
                    .. attribute:: tx_los
                    
                    	TX LOS
                    	**type**\: :py:class:`TxLos <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos>`
                    
                    .. attribute:: rx_lol
                    
                    	RX LOL
                    	**type**\: :py:class:`RxLol <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol>`
                    
                    .. attribute:: tx_lol
                    
                    	TX LOL
                    	**type**\: :py:class:`TxLol <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol>`
                    
                    .. attribute:: tx_fault
                    
                    	TX Fault
                    	**type**\: :py:class:`TxFault <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault>`
                    
                    .. attribute:: hidgd
                    
                    	HI DGD
                    	**type**\: :py:class:`Hidgd <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd>`
                    
                    .. attribute:: oorcd
                    
                    	OOR CD
                    	**type**\: :py:class:`Oorcd <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd>`
                    
                    .. attribute:: osnr
                    
                    	OSNR
                    	**type**\: :py:class:`Osnr <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr>`
                    
                    .. attribute:: wvlool
                    
                    	WVL OOL
                    	**type**\: :py:class:`Wvlool <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool>`
                    
                    .. attribute:: mea
                    
                    	MEA
                    	**type**\: :py:class:`Mea <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea>`
                    
                    .. attribute:: imp_removal
                    
                    	IMPROPER REM
                    	**type**\: :py:class:`ImpRemoval <ydk.models.controller.Cisco_IOS_XR_controller_optics_oper.OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval>`
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.high_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower()
                        self.high_rx_power.parent = self
                        self.low_rx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower()
                        self.low_rx_power.parent = self
                        self.high_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower()
                        self.high_tx_power.parent = self
                        self.low_tx_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower()
                        self.low_tx_power.parent = self
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
                        self.low_rx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power()
                        self.low_rx1_power.parent = self
                        self.low_rx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power()
                        self.low_rx2_power.parent = self
                        self.low_rx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power()
                        self.low_rx3_power.parent = self
                        self.low_rx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power()
                        self.low_rx4_power.parent = self
                        self.high_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power()
                        self.high_tx1_power.parent = self
                        self.high_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power()
                        self.high_tx2_power.parent = self
                        self.high_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power()
                        self.high_tx3_power.parent = self
                        self.high_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power()
                        self.high_tx4_power.parent = self
                        self.low_tx1_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power()
                        self.low_tx1_power.parent = self
                        self.low_tx2_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power()
                        self.low_tx2_power.parent = self
                        self.low_tx3_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power()
                        self.low_tx3_power.parent = self
                        self.low_tx4_power = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power()
                        self.low_tx4_power.parent = self
                        self.high_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc()
                        self.high_tx1lbc.parent = self
                        self.high_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc()
                        self.high_tx2lbc.parent = self
                        self.high_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc()
                        self.high_tx3lbc.parent = self
                        self.high_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc()
                        self.high_tx4lbc.parent = self
                        self.low_tx1lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc()
                        self.low_tx1lbc.parent = self
                        self.low_tx2lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc()
                        self.low_tx2lbc.parent = self
                        self.low_tx3lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc()
                        self.low_tx3lbc.parent = self
                        self.low_tx4lbc = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc()
                        self.low_tx4lbc.parent = self
                        self.rx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos()
                        self.rx_los.parent = self
                        self.tx_los = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos()
                        self.tx_los.parent = self
                        self.rx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol()
                        self.rx_lol.parent = self
                        self.tx_lol = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol()
                        self.tx_lol.parent = self
                        self.tx_fault = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault()
                        self.tx_fault.parent = self
                        self.hidgd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd()
                        self.hidgd.parent = self
                        self.oorcd = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd()
                        self.oorcd.parent = self
                        self.osnr = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr()
                        self.osnr.parent = self
                        self.wvlool = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool()
                        self.wvlool.parent = self
                        self.mea = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea()
                        self.mea.parent = self
                        self.imp_removal = OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval()
                        self.imp_removal.parent = self


                    class HighRxPower(object):
                        """
                        High Rx Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower']['meta_info']


                    class LowRxPower(object):
                        """
                        Low Rx Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower']['meta_info']


                    class HighTxPower(object):
                        """
                        High Tx Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower']['meta_info']


                    class LowTxPower(object):
                        """
                        Low Tx Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower']['meta_info']


                    class HighLbc(object):
                        """
                        High laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc']['meta_info']


                    class HighRx1Power(object):
                        """
                        High Rx1 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power']['meta_info']


                    class HighRx2Power(object):
                        """
                        High Rx2 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power']['meta_info']


                    class HighRx3Power(object):
                        """
                        High Rx3 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power']['meta_info']


                    class HighRx4Power(object):
                        """
                        High Rx4 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power']['meta_info']


                    class LowRx1Power(object):
                        """
                        Low Rx1 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power']['meta_info']


                    class LowRx2Power(object):
                        """
                        Low Rx2 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power']['meta_info']


                    class LowRx3Power(object):
                        """
                        Low Rx3 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power']['meta_info']


                    class LowRx4Power(object):
                        """
                        Low Rx4 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power']['meta_info']


                    class HighTx1Power(object):
                        """
                        High Tx1 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power']['meta_info']


                    class HighTx2Power(object):
                        """
                        High Tx2 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power']['meta_info']


                    class HighTx3Power(object):
                        """
                        High Tx3 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power']['meta_info']


                    class HighTx4Power(object):
                        """
                        High Tx4 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power']['meta_info']


                    class LowTx1Power(object):
                        """
                        Low Tx1 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power']['meta_info']


                    class LowTx2Power(object):
                        """
                        Low Tx2 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power']['meta_info']


                    class LowTx3Power(object):
                        """
                        Low Tx3 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power']['meta_info']


                    class LowTx4Power(object):
                        """
                        Low Tx4 Power
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power']['meta_info']


                    class HighTx1Lbc(object):
                        """
                        High Tx1 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc']['meta_info']


                    class HighTx2Lbc(object):
                        """
                        High Tx2 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc']['meta_info']


                    class HighTx3Lbc(object):
                        """
                        High Tx3 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc']['meta_info']


                    class HighTx4Lbc(object):
                        """
                        High Tx4 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc']['meta_info']


                    class LowTx1Lbc(object):
                        """
                        Low Tx1 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc']['meta_info']


                    class LowTx2Lbc(object):
                        """
                        Low Tx2 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc']['meta_info']


                    class LowTx3Lbc(object):
                        """
                        Low Tx3 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc']['meta_info']


                    class LowTx4Lbc(object):
                        """
                        Low Tx4 laser bias current
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc']['meta_info']


                    class RxLos(object):
                        """
                        RX LOS
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos']['meta_info']


                    class TxLos(object):
                        """
                        TX LOS
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos']['meta_info']


                    class RxLol(object):
                        """
                        RX LOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol']['meta_info']


                    class TxLol(object):
                        """
                        TX LOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol']['meta_info']


                    class TxFault(object):
                        """
                        TX Fault
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault']['meta_info']


                    class Hidgd(object):
                        """
                        HI DGD
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd']['meta_info']


                    class Oorcd(object):
                        """
                        OOR CD
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd']['meta_info']


                    class Osnr(object):
                        """
                        OSNR
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr']['meta_info']


                    class Wvlool(object):
                        """
                        WVL OOL
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool']['meta_info']


                    class Mea(object):
                        """
                        MEA
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea']['meta_info']


                    class ImpRemoval(object):
                        """
                        IMPROPER REM
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-optics-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.is_detected = None
                            self.counter = None

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
                            if self.is_detected is not None:
                                return True

                            if self.counter is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                            return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval']['meta_info']

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
                        if self.high_rx_power is not None and self.high_rx_power._has_data():
                            return True

                        if self.low_rx_power is not None and self.low_rx_power._has_data():
                            return True

                        if self.high_tx_power is not None and self.high_tx_power._has_data():
                            return True

                        if self.low_tx_power is not None and self.low_tx_power._has_data():
                            return True

                        if self.high_lbc is not None and self.high_lbc._has_data():
                            return True

                        if self.high_rx1_power is not None and self.high_rx1_power._has_data():
                            return True

                        if self.high_rx2_power is not None and self.high_rx2_power._has_data():
                            return True

                        if self.high_rx3_power is not None and self.high_rx3_power._has_data():
                            return True

                        if self.high_rx4_power is not None and self.high_rx4_power._has_data():
                            return True

                        if self.low_rx1_power is not None and self.low_rx1_power._has_data():
                            return True

                        if self.low_rx2_power is not None and self.low_rx2_power._has_data():
                            return True

                        if self.low_rx3_power is not None and self.low_rx3_power._has_data():
                            return True

                        if self.low_rx4_power is not None and self.low_rx4_power._has_data():
                            return True

                        if self.high_tx1_power is not None and self.high_tx1_power._has_data():
                            return True

                        if self.high_tx2_power is not None and self.high_tx2_power._has_data():
                            return True

                        if self.high_tx3_power is not None and self.high_tx3_power._has_data():
                            return True

                        if self.high_tx4_power is not None and self.high_tx4_power._has_data():
                            return True

                        if self.low_tx1_power is not None and self.low_tx1_power._has_data():
                            return True

                        if self.low_tx2_power is not None and self.low_tx2_power._has_data():
                            return True

                        if self.low_tx3_power is not None and self.low_tx3_power._has_data():
                            return True

                        if self.low_tx4_power is not None and self.low_tx4_power._has_data():
                            return True

                        if self.high_tx1lbc is not None and self.high_tx1lbc._has_data():
                            return True

                        if self.high_tx2lbc is not None and self.high_tx2lbc._has_data():
                            return True

                        if self.high_tx3lbc is not None and self.high_tx3lbc._has_data():
                            return True

                        if self.high_tx4lbc is not None and self.high_tx4lbc._has_data():
                            return True

                        if self.low_tx1lbc is not None and self.low_tx1lbc._has_data():
                            return True

                        if self.low_tx2lbc is not None and self.low_tx2lbc._has_data():
                            return True

                        if self.low_tx3lbc is not None and self.low_tx3lbc._has_data():
                            return True

                        if self.low_tx4lbc is not None and self.low_tx4lbc._has_data():
                            return True

                        if self.rx_los is not None and self.rx_los._has_data():
                            return True

                        if self.tx_los is not None and self.tx_los._has_data():
                            return True

                        if self.rx_lol is not None and self.rx_lol._has_data():
                            return True

                        if self.tx_lol is not None and self.tx_lol._has_data():
                            return True

                        if self.tx_fault is not None and self.tx_fault._has_data():
                            return True

                        if self.hidgd is not None and self.hidgd._has_data():
                            return True

                        if self.oorcd is not None and self.oorcd._has_data():
                            return True

                        if self.osnr is not None and self.osnr._has_data():
                            return True

                        if self.wvlool is not None and self.wvlool._has_data():
                            return True

                        if self.mea is not None and self.mea._has_data():
                            return True

                        if self.imp_removal is not None and self.imp_removal._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']


                class LaneData(object):
                    """
                    Lane information
                    
                    .. attribute:: lane_index
                    
                    	The index number of the lane
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_percent
                    
                    	Laser Bias Current in units of 0.01%
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: laser_bias_current_milli_amps
                    
                    	Laser Bias Current in units of 0.01mA
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transmit_power
                    
                    	Transmit power in the unit of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: receive_power
                    
                    	Transponder receive power in the unit of 0.01dBm
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'controller-optics-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.lane_index = None
                        self.laser_bias_current_percent = None
                        self.laser_bias_current_milli_amps = None
                        self.transmit_power = None
                        self.receive_power = None

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
                        if self.lane_index is not None:
                            return True

                        if self.laser_bias_current_percent is not None:
                            return True

                        if self.laser_bias_current_milli_amps is not None:
                            return True

                        if self.transmit_power is not None:
                            return True

                        if self.receive_power is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
                        return meta._meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info']

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
                    if self.network_srlg_info is not None and self.network_srlg_info._has_data():
                        return True

                    if self.optics_alarm_info is not None and self.optics_alarm_info._has_data():
                        return True

                    if self.transport_admin_state is not None:
                        return True

                    if self.optics_present is not None:
                        return True

                    if self.optics_type is not None:
                        return True

                    if self.optics_module is not None:
                        return True

                    if self.dwdm_carrier_band is not None:
                        return True

                    if self.dwdm_carrier_channel is not None:
                        return True

                    if self.dwdm_carrier_frequency is not None:
                        return True

                    if self.dwdm_carrier_wavelength is not None:
                        return True

                    if self.grey_wavelength is not None:
                        return True

                    if self.rx_low_threshold is not None:
                        return True

                    if self.rx_high_threshold is not None:
                        return True

                    if self.lbc_high_threshold is not None:
                        return True

                    if self.tx_low_threshold is not None:
                        return True

                    if self.tx_high_threshold is not None:
                        return True

                    if self.temp_low_threshold is not None:
                        return True

                    if self.temp_high_threshold is not None:
                        return True

                    if self.volt_low_threshold is not None:
                        return True

                    if self.volt_high_threshold is not None:
                        return True

                    if self.cd is not None:
                        return True

                    if self.cd_min is not None:
                        return True

                    if self.cd_max is not None:
                        return True

                    if self.cd_low_threshold is not None:
                        return True

                    if self.cd_high_threshold is not None:
                        return True

                    if self.osnr_low_threshold is not None:
                        return True

                    if self.dgd_high_threshold is not None:
                        return True

                    if self.polarization_mode_dispersion is not None:
                        return True

                    if self.second_order_polarization_mode_dispersion is not None:
                        return True

                    if self.optical_signal_to_noise_ratio is not None:
                        return True

                    if self.polarization_dependent_loss is not None:
                        return True

                    if self.polarization_change_rate is not None:
                        return True

                    if self.differential_group_delay is not None:
                        return True

                    if self.phase_noise is not None:
                        return True

                    if self.pm_enable is not None:
                        return True

                    if self.laser_state is not None:
                        return True

                    if self.led_state is not None:
                        return True

                    if self.controller_state is not None:
                        return True

                    if self.form_factor is not None:
                        return True

                    if self.phy_type is not None:
                        return True

                    if self.cfg_tx_power is not None:
                        return True

                    if self.vendor_info is not None:
                        return True

                    if self.display_volt_temp is not None:
                        return True

                    if self.lane_data is not None:
                        for child_ref in self.lane_data:
                            if child_ref._has_data():
                                return True

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
                if self.name is not None:
                    return True

                if self.optics_dwdm_carrrier_channel_map is not None and self.optics_dwdm_carrrier_channel_map._has_data():
                    return True

                if self.optics_info is not None and self.optics_info._has_data():
                    return True

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
            if self.optics_port is not None:
                for child_ref in self.optics_port:
                    if child_ref._has_data():
                        return True

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
        if self.optics_ports is not None and self.optics_ports._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_oper as meta
        return meta._meta_table['OpticsOper']['meta_info']



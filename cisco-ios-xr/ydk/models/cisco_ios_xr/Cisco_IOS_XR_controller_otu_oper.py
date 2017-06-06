""" Cisco_IOS_XR_controller_otu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package operational data.

This module contains definitions
for the following management objects\:
  otu\: OTU operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class GmplsOtuTtiModeEnum(Enum):
    """
    GmplsOtuTtiModeEnum

    Gmpls otu tti mode

    .. data:: gmpls_otu_tti_mode_none = 0

    	Not Set

    .. data:: gmpls_otu_tti_mode_sm = 1

    	Section Monitoring

    .. data:: gmpls_otu_tti_mode_pm = 2

    	Path Monitoring

    .. data:: gmpls_otu_tti_mode_tcm = 3

    	Tandem Connection Monitoring

    """

    gmpls_otu_tti_mode_none = 0

    gmpls_otu_tti_mode_sm = 1

    gmpls_otu_tti_mode_pm = 2

    gmpls_otu_tti_mode_tcm = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['GmplsOtuTtiModeEnum']


class OtuDerStateEnum(Enum):
    """
    OtuDerStateEnum

    Otu der state

    .. data:: out_of_service = 0

    	Out Of Service

    .. data:: in_service = 1

    	In Service

    .. data:: maintenance = 2

    	Maintenance

    .. data:: ais = 3

    	Automatic In Service

    """

    out_of_service = 0

    in_service = 1

    maintenance = 2

    ais = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuDerStateEnum']


class OtuG709FecModeEnum(Enum):
    """
    OtuG709FecModeEnum

    Otu g709fec mode

    .. data:: otu_bag_none_fec = 1

    	NONE

    .. data:: otu_bag_standard_fec = 2

    	STANDARD

    .. data:: otu_bag_1_i_7_fec = 4

    	ENHANCEDI.7

    .. data:: otu_bag_1_i_4_fec = 8

    	ENHANCEDI.4

    .. data:: otu_bag_swizzle_fec = 16

    	SWIZZLE

    .. data:: otu_bag_hg20_fec = 32

    	HIGH GAIN20

    .. data:: otu_bag_enhanced_hg7_fec = 64

    	Enhanced High Gain 7

    .. data:: otu_bag_sd20_fec = 128

    	Soft-Decision 20

    .. data:: otu_bag_sd7_fec = 256

    	Soft-Decision 7

    .. data:: otu_bag_all_fec = 512

    	ALL

    """

    otu_bag_none_fec = 1

    otu_bag_standard_fec = 2

    otu_bag_1_i_7_fec = 4

    otu_bag_1_i_4_fec = 8

    otu_bag_swizzle_fec = 16

    otu_bag_hg20_fec = 32

    otu_bag_enhanced_hg7_fec = 64

    otu_bag_sd20_fec = 128

    otu_bag_sd7_fec = 256

    otu_bag_all_fec = 512


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuG709FecModeEnum']


class OtuLoopBackModeEnum(Enum):
    """
    OtuLoopBackModeEnum

    Otu loop back mode

    .. data:: none = 1

    	None

    .. data:: line = 2

    	Line

    .. data:: internal = 4

    	Internal

    """

    none = 1

    line = 2

    internal = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuLoopBackModeEnum']


class OtuPerMonEnum(Enum):
    """
    OtuPerMonEnum

    Otu per mon

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPerMonEnum']


class OtuPpFsmStateEnum(Enum):
    """
    OtuPpFsmStateEnum

    Otu pp fsm state

    .. data:: otu_in_active = 0

    	In Active

    .. data:: otu_disabled = 1

    	Disabled

    .. data:: otu_normal_state = 2

    	Normal

    .. data:: otu_local_failing = 3

    	Local Failing

    .. data:: otu_remote_failing = 4

    	Remote Failing

    .. data:: otu_main_t_failing = 5

    	Maintance Failing

    .. data:: otu_regen_failing = 6

    	Regenerator Failing

    .. data:: otu_local_failed = 7

    	Local Failed

    .. data:: otu_remote_failed = 8

    	Remote Failed

    .. data:: otu_main_t_failed = 9

    	Maintance Failed

    .. data:: otu_regen_failed = 10

    	Regenerator Failed

    """

    otu_in_active = 0

    otu_disabled = 1

    otu_normal_state = 2

    otu_local_failing = 3

    otu_remote_failing = 4

    otu_main_t_failing = 5

    otu_regen_failing = 6

    otu_local_failed = 7

    otu_remote_failed = 8

    otu_main_t_failed = 9

    otu_regen_failed = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpFsmStateEnum']


class OtuPpIntfStateEnum(Enum):
    """
    OtuPpIntfStateEnum

    Otu pp intf state

    .. data:: otu_pp_intf_up = 0

    	Interface is Up

    .. data:: otu_pp_intf_failing = 1

    	Interface is Going Down

    .. data:: otu_pp_intf_down = 2

    	Interface Down

    """

    otu_pp_intf_up = 0

    otu_pp_intf_failing = 1

    otu_pp_intf_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpIntfStateEnum']


class OtuSecStateEnum(Enum):
    """
    OtuSecStateEnum

    Otu sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintenance = 1

    	Maintenance

    .. data:: ais = 2

    	Automatic In Service

    """

    normal = 0

    maintenance = 1

    ais = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuSecStateEnum']


class OtuStateEtEnum(Enum):
    """
    OtuStateEtEnum

    Otu state et

    .. data:: not_ready = 0

    	Not Ready

    .. data:: admin_down = 1

    	Admin Down

    .. data:: down = 2

    	Down

    .. data:: up = 3

    	Up

    .. data:: shutdown = 4

    	Shutdown

    .. data:: error_disable = 5

    	Error Disable

    .. data:: down_immediate = 6

    	Down Immediate

    .. data:: down_immediate_admin = 7

    	Down Immediate Admin

    .. data:: down_graceful = 8

    	Down Graceful

    .. data:: begin_shutdown = 9

    	Begin Shutdown

    .. data:: end_shutdown = 10

    	End Shutdown

    .. data:: begin_error_disable = 11

    	Begin Error Disable

    .. data:: end_error_disable = 12

    	End Error Disable

    .. data:: begin_down_graceful = 13

    	Begin Down Graceful

    .. data:: reset = 14

    	Reset

    .. data:: operational = 15

    	Operational

    .. data:: not_operational = 16

    	Not Operational

    .. data:: unknown = 17

    	Unknown

    .. data:: last = 18

    	Last

    """

    not_ready = 0

    admin_down = 1

    down = 2

    up = 3

    shutdown = 4

    error_disable = 5

    down_immediate = 6

    down_immediate_admin = 7

    down_graceful = 8

    begin_shutdown = 9

    end_shutdown = 10

    begin_error_disable = 11

    end_error_disable = 12

    begin_down_graceful = 13

    reset = 14

    operational = 15

    not_operational = 16

    unknown = 17

    last = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuStateEtEnum']


class OtuTtiEtEnum(Enum):
    """
    OtuTtiEtEnum

    Otu tti et

    .. data:: ascii = 0

    	ASCII

    .. data:: hex = 1

    	HEX

    .. data:: full_ascii = 2

    	FULL ASCII

    .. data:: full_hex = 3

    	FULL HEX

    """

    ascii = 0

    hex = 1

    full_ascii = 2

    full_hex = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuTtiEtEnum']



class Otu(object):
    """
    OTU operational data
    
    .. attribute:: controllers
    
    	All OTU Port operational data
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers>`
    
    

    """

    _prefix = 'controller-otu-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.controllers = Otu.Controllers()
        self.controllers.parent = self


    class Controllers(object):
        """
        All OTU Port operational data
        
        .. attribute:: controller
        
        	OTU Port operational data
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller>`
        
        

        """

        _prefix = 'controller-otu-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.controller = YList()
            self.controller.parent = self
            self.controller.name = 'controller'


        class Controller(object):
            """
            OTU Port operational data
            
            .. attribute:: controller_name  <key>
            
            	Port name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: info
            
            	OTU port operational data
            	**type**\:   :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info>`
            
            

            """

            _prefix = 'controller-otu-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.controller_name = None
                self.info = Otu.Controllers.Controller.Info()
                self.info.parent = self


            class Info(object):
                """
                OTU port operational data
                
                .. attribute:: auto_tti_flag
                
                	Auto tti flag
                	**type**\:  bool
                
                .. attribute:: config_sec_state
                
                	Sec State
                	**type**\:   :py:class:`OtuSecStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecStateEnum>`
                
                .. attribute:: derivedstate_mode
                
                	Derived State
                	**type**\:   :py:class:`OtuDerStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuDerStateEnum>`
                
                .. attribute:: ec
                
                	Average bit errors corrected
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ec_value
                
                	EC value present
                	**type**\:  bool
                
                .. attribute:: fec_mode
                
                	FEC
                	**type**\:   :py:class:`OtuG709FecModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuG709FecModeEnum>`
                
                .. attribute:: gcc_mode
                
                	OTU GCC
                	**type**\:  bool
                
                .. attribute:: gmpls_tti_mode
                
                	GMPLS TTI MODE
                	**type**\:   :py:class:`GmplsOtuTtiModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.GmplsOtuTtiModeEnum>`
                
                .. attribute:: gmpls_tvm_id
                
                	GMPLS TCM ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: inherit_sec_state
                
                	Sec State
                	**type**\:   :py:class:`OtuSecStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecStateEnum>`
                
                .. attribute:: local
                
                	TTI
                	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Local>`
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\:   :py:class:`OtuLoopBackModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuLoopBackModeEnum>`
                
                .. attribute:: name
                
                	Interface Name
                	**type**\:  str
                
                .. attribute:: network_srlg
                
                	Network Shared Risk Link Group information
                	**type**\:   :py:class:`NetworkSrlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg>`
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\:  bool
                
                .. attribute:: otu_alarm_info
                
                	OTU layer alarm Information
                	**type**\:   :py:class:`OtuAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo>`
                
                .. attribute:: otu_fec_satistics
                
                	OTU FEC Statistics
                	**type**\:   :py:class:`OtuFecSatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuFecSatistics>`
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\:   :py:class:`OtuPerMonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPerMonEnum>`
                
                .. attribute:: pre_fec_ber_mantissa
                
                	Pre fec val mantissa
                	**type**\:  bool
                
                .. attribute:: pre_fec_ber_value
                
                	Pre fec val present 
                	**type**\:  bool
                
                .. attribute:: pre_fec_mantissa
                
                	Pre FEC BER Mantissa in form E\-<mantisaa>
                	**type**\:  int
                
                	**range:** \-128..127
                
                .. attribute:: pre_fec_val
                
                	Pre FEC BER Value in form 0.00
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: proactive
                
                	Proactive Protection
                	**type**\:   :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Proactive>`
                
                .. attribute:: q
                
                	q value calculated
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: q_margin
                
                	q margin calculated
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote
                
                	Remote
                	**type**\:   :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Remote>`
                
                .. attribute:: sd
                
                	SD in the form of 1.0E \- <SD>
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: sf
                
                	SF in the form of 1.0E \- <SF>
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: state
                
                	Admin State
                	**type**\:   :py:class:`OtuStateEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuStateEtEnum>`
                
                .. attribute:: tti_mode
                
                	OTU TTI
                	**type**\:   :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode>`
                
                .. attribute:: uc
                
                	Uncorrected word count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: uc_value
                
                	Uc value present
                	**type**\:  bool
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.auto_tti_flag = None
                    self.config_sec_state = None
                    self.derivedstate_mode = None
                    self.ec = None
                    self.ec_value = None
                    self.fec_mode = None
                    self.gcc_mode = None
                    self.gmpls_tti_mode = None
                    self.gmpls_tvm_id = None
                    self.inherit_sec_state = None
                    self.local = Otu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self.loopback_mode = None
                    self.name = None
                    self.network_srlg = Otu.Controllers.Controller.Info.NetworkSrlg()
                    self.network_srlg.parent = self
                    self.nv_optical_support = None
                    self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                    self.otu_alarm_info.parent = self
                    self.otu_fec_satistics = Otu.Controllers.Controller.Info.OtuFecSatistics()
                    self.otu_fec_satistics.parent = self
                    self.performance_monitoring = None
                    self.pre_fec_ber_mantissa = None
                    self.pre_fec_ber_value = None
                    self.pre_fec_mantissa = None
                    self.pre_fec_val = None
                    self.proactive = Otu.Controllers.Controller.Info.Proactive()
                    self.proactive.parent = self
                    self.q = None
                    self.q_margin = None
                    self.remote = Otu.Controllers.Controller.Info.Remote()
                    self.remote.parent = self
                    self.sd = None
                    self.sf = None
                    self.state = None
                    self.tti_mode = Otu.Controllers.Controller.Info.TtiMode()
                    self.tti_mode.parent = self
                    self.uc = None
                    self.uc_value = None


                class Local(object):
                    """
                    TTI
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.if_index = None
                        self.router_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:local'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.if_index is not None:
                            return True

                        if self.router_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Local']['meta_info']


                class Remote(object):
                    """
                    Remote
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.if_index = None
                        self.router_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:remote'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.if_index is not None:
                            return True

                        if self.router_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Remote']['meta_info']


                class TtiMode(object):
                    """
                    OTU TTI
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\:   :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\:   :py:class:`OtuTtiEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEtEnum>`
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\:   :py:class:`OtuTtiEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEtEnum>`
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI sent
                    	**type**\:   :py:class:`OtuTtiEtEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEtEnum>`
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\:   :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    .. attribute:: remote_host_name
                    
                    	Remote host name
                    	**type**\:  str
                    
                    .. attribute:: remote_interface
                    
                    	Remote Interface Name
                    	**type**\:  str
                    
                    .. attribute:: remote_ip_addr
                    
                    	Remote host ip
                    	**type**\:  str
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\:   :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.exp = Otu.Controllers.Controller.Info.TtiMode.Exp()
                        self.exp.parent = self
                        self.g709tti_exp_mode = None
                        self.g709tti_rec_mode = None
                        self.g709tti_sent_mode = None
                        self.rec = Otu.Controllers.Controller.Info.TtiMode.Rec()
                        self.rec.parent = self
                        self.remote_host_name = None
                        self.remote_interface = None
                        self.remote_ip_addr = None
                        self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self


                    class Tx(object):
                        """
                        String Sent
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = YLeafList()
                            self.dapi.parent = self
                            self.dapi.name = 'dapi'
                            self.full_tti_ascii_string = None
                            self.operator_specific = YLeafList()
                            self.operator_specific.parent = self
                            self.operator_specific.name = 'operator_specific'
                            self.sapi = YLeafList()
                            self.sapi.parent = self
                            self.sapi.name = 'sapi'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tx'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
                                        return True

                            if self.full_tti_ascii_string is not None:
                                return True

                            if self.operator_specific is not None:
                                for child in self.operator_specific:
                                    if child is not None:
                                        return True

                            if self.sapi is not None:
                                for child in self.sapi:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx']['meta_info']


                    class Exp(object):
                        """
                        String Expected
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = YLeafList()
                            self.dapi.parent = self
                            self.dapi.name = 'dapi'
                            self.full_tti_ascii_string = None
                            self.operator_specific = YLeafList()
                            self.operator_specific.parent = self
                            self.operator_specific.name = 'operator_specific'
                            self.sapi = YLeafList()
                            self.sapi.parent = self
                            self.sapi.name = 'sapi'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:exp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
                                        return True

                            if self.full_tti_ascii_string is not None:
                                return True

                            if self.operator_specific is not None:
                                for child in self.operator_specific:
                                    if child is not None:
                                        return True

                            if self.sapi is not None:
                                for child in self.sapi:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp']['meta_info']


                    class Rec(object):
                        """
                        String Received
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\:  str
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\:  list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = YLeafList()
                            self.dapi.parent = self
                            self.dapi.name = 'dapi'
                            self.full_tti_ascii_string = None
                            self.operator_specific = YLeafList()
                            self.operator_specific.parent = self
                            self.operator_specific.name = 'operator_specific'
                            self.sapi = YLeafList()
                            self.sapi.parent = self
                            self.sapi.name = 'sapi'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:rec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
                                        return True

                            if self.full_tti_ascii_string is not None:
                                return True

                            if self.operator_specific is not None:
                                for child in self.operator_specific:
                                    if child is not None:
                                        return True

                            if self.sapi is not None:
                                for child in self.sapi:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tti-mode'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.exp is not None and self.exp._has_data():
                            return True

                        if self.g709tti_exp_mode is not None:
                            return True

                        if self.g709tti_rec_mode is not None:
                            return True

                        if self.g709tti_sent_mode is not None:
                            return True

                        if self.rec is not None and self.rec._has_data():
                            return True

                        if self.remote_host_name is not None:
                            return True

                        if self.remote_interface is not None:
                            return True

                        if self.remote_ip_addr is not None:
                            return True

                        if self.tx is not None and self.tx._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']


                class NetworkSrlg(object):
                    """
                    Network Shared Risk Link Group information
                    
                    .. attribute:: srlg_info
                    
                    	Array of Network Shared Risk Link Group information
                    	**type**\: list of    :py:class:`SrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srlg_info = YList()
                        self.srlg_info.parent = self
                        self.srlg_info.name = 'srlg_info'


                    class SrlgInfo(object):
                        """
                        Array of Network Shared Risk Link Group
                        information
                        
                        .. attribute:: set_id
                        
                        	Array to maintain set id number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srlg
                        
                        	Shared Risk Link Group information expressed in integer format
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.set_id = None
                            self.srlg = YLeafList()
                            self.srlg.parent = self
                            self.srlg.name = 'srlg'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:srlg-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.set_id is not None:
                                return True

                            if self.srlg is not None:
                                for child in self.srlg:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:network-srlg'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.srlg_info is not None:
                            for child_ref in self.srlg_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.NetworkSrlg']['meta_info']


                class OtuAlarmInfo(object):
                    """
                    OTU layer alarm Information
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\:   :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais>`
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\:   :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi>`
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\:   :py:class:`Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae>`
                    
                    .. attribute:: ec
                    
                    	EC alarm
                    	**type**\:   :py:class:`Ec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec>`
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\:   :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc>`
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:   :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch>`
                    
                    .. attribute:: fecunc
                    
                    	FEC UnCorrected Word
                    	**type**\:   :py:class:`Fecunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc>`
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\:   :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae>`
                    
                    .. attribute:: lof
                    
                    	Loss of Frame
                    	**type**\:   :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof>`
                    
                    .. attribute:: lom
                    
                    	Loss of MultiFrame
                    	**type**\:   :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom>`
                    
                    .. attribute:: los
                    
                    	Loss of Signal
                    	**type**\:   :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Los>`
                    
                    .. attribute:: oof
                    
                    	Out of Frame
                    	**type**\:   :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof>`
                    
                    .. attribute:: oom
                    
                    	Out of MultiFrame
                    	**type**\:   :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom>`
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\:   :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer>`
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\:   :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer>`
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch
                    	**type**\:   :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim>`
                    
                    .. attribute:: uc
                    
                    	UC alarm
                    	**type**\:   :py:class:`Uc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc>`
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ais = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais()
                        self.ais.parent = self
                        self.bdi = Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi()
                        self.bdi.parent = self
                        self.biae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae()
                        self.biae.parent = self
                        self.ec = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec()
                        self.ec.parent = self
                        self.eoc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc()
                        self.eoc.parent = self
                        self.fec_mismatch = Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch()
                        self.fec_mismatch.parent = self
                        self.fecunc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc()
                        self.fecunc.parent = self
                        self.iae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae()
                        self.iae.parent = self
                        self.lof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof()
                        self.lof.parent = self
                        self.lom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom()
                        self.lom.parent = self
                        self.los = Otu.Controllers.Controller.Info.OtuAlarmInfo.Los()
                        self.los.parent = self
                        self.oof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof()
                        self.oof.parent = self
                        self.oom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom()
                        self.oom.parent = self
                        self.sd_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer()
                        self.sd_ber.parent = self
                        self.sf_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer()
                        self.sf_ber.parent = self
                        self.tim = Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim()
                        self.tim.parent = self
                        self.uc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc()
                        self.uc.parent = self


                    class Los(object):
                        """
                        Loss of Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:los'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Los']['meta_info']


                    class Lof(object):
                        """
                        Loss of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:lof'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof']['meta_info']


                    class Lom(object):
                        """
                        Loss of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:lom'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom']['meta_info']


                    class Oof(object):
                        """
                        Out of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:oof'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof']['meta_info']


                    class Oom(object):
                        """
                        Out of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:oom'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom']['meta_info']


                    class Ais(object):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:ais'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais']['meta_info']


                    class Iae(object):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:iae'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae']['meta_info']


                    class Biae(object):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:biae'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae']['meta_info']


                    class Bdi(object):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:bdi'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi']['meta_info']


                    class Tim(object):
                        """
                        Trace Identifier Mismatch
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tim'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim']['meta_info']


                    class Eoc(object):
                        """
                        GCC End of Channel
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:eoc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc']['meta_info']


                    class FecMismatch(object):
                        """
                        FEC mismatch alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:fec-mismatch'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch']['meta_info']


                    class SfBer(object):
                        """
                        SF BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:sf-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer']['meta_info']


                    class SdBer(object):
                        """
                        SD BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:sd-ber'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer']['meta_info']


                    class Ec(object):
                        """
                        EC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:ec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec']['meta_info']


                    class Uc(object):
                        """
                        UC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:uc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc']['meta_info']


                    class Fecunc(object):
                        """
                        FEC UnCorrected Word
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\:  bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\:  bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.counter = None
                            self.is_asserted = None
                            self.is_detected = None
                            self.reporting_enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:fecunc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.counter is not None:
                                return True

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:otu-alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ais is not None and self.ais._has_data():
                            return True

                        if self.bdi is not None and self.bdi._has_data():
                            return True

                        if self.biae is not None and self.biae._has_data():
                            return True

                        if self.ec is not None and self.ec._has_data():
                            return True

                        if self.eoc is not None and self.eoc._has_data():
                            return True

                        if self.fec_mismatch is not None and self.fec_mismatch._has_data():
                            return True

                        if self.fecunc is not None and self.fecunc._has_data():
                            return True

                        if self.iae is not None and self.iae._has_data():
                            return True

                        if self.lof is not None and self.lof._has_data():
                            return True

                        if self.lom is not None and self.lom._has_data():
                            return True

                        if self.los is not None and self.los._has_data():
                            return True

                        if self.oof is not None and self.oof._has_data():
                            return True

                        if self.oom is not None and self.oom._has_data():
                            return True

                        if self.sd_ber is not None and self.sd_ber._has_data():
                            return True

                        if self.sf_ber is not None and self.sf_ber._has_data():
                            return True

                        if self.tim is not None and self.tim._has_data():
                            return True

                        if self.uc is not None and self.uc._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']


                class Proactive(object):
                    """
                    Proactive Protection
                    
                    .. attribute:: config_sec_state
                    
                    	Sec State
                    	**type**\:   :py:class:`OtuSecStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecStateEnum>`
                    
                    .. attribute:: inherit_sec_state
                    
                    	Secondary Admin State
                    	**type**\:   :py:class:`OtuSecStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecStateEnum>`
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:   :py:class:`OtuPpIntfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpIntfStateEnum>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:   :py:class:`OtuPpFsmStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpFsmStateEnum>`
                    
                    .. attribute:: proactive_status
                    
                    	Proactive Status
                    	**type**\:  bool
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_coeff
                    
                    	Trigger threshold coefficient
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_power
                    
                    	Trigger threshold power
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trigger_window
                    
                    	Trigger Integration window
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.config_sec_state = None
                        self.inherit_sec_state = None
                        self.proactive_fsm_if_state = None
                        self.proactive_fsm_state = None
                        self.proactive_status = None
                        self.revert_window = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.trigger_window = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:proactive'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.config_sec_state is not None:
                            return True

                        if self.inherit_sec_state is not None:
                            return True

                        if self.proactive_fsm_if_state is not None:
                            return True

                        if self.proactive_fsm_state is not None:
                            return True

                        if self.proactive_status is not None:
                            return True

                        if self.revert_window is not None:
                            return True

                        if self.rvrt_thresh_coeff is not None:
                            return True

                        if self.rvrt_thresh_power is not None:
                            return True

                        if self.trig_thresh_coeff is not None:
                            return True

                        if self.trig_thresh_power is not None:
                            return True

                        if self.trigger_window is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Proactive']['meta_info']


                class OtuFecSatistics(object):
                    """
                    OTU FEC Statistics
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit Error Rate After Forward Error Correction
                    	**type**\:  str
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit Error Rate Before Forward Error Correction
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.post_fec_ber = None
                        self.pre_fec_ber = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:otu-fec-satistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.post_fec_ber is not None:
                            return True

                        if self.pre_fec_ber is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.OtuFecSatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.auto_tti_flag is not None:
                        return True

                    if self.config_sec_state is not None:
                        return True

                    if self.derivedstate_mode is not None:
                        return True

                    if self.ec is not None:
                        return True

                    if self.ec_value is not None:
                        return True

                    if self.fec_mode is not None:
                        return True

                    if self.gcc_mode is not None:
                        return True

                    if self.gmpls_tti_mode is not None:
                        return True

                    if self.gmpls_tvm_id is not None:
                        return True

                    if self.inherit_sec_state is not None:
                        return True

                    if self.local is not None and self.local._has_data():
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.network_srlg is not None and self.network_srlg._has_data():
                        return True

                    if self.nv_optical_support is not None:
                        return True

                    if self.otu_alarm_info is not None and self.otu_alarm_info._has_data():
                        return True

                    if self.otu_fec_satistics is not None and self.otu_fec_satistics._has_data():
                        return True

                    if self.performance_monitoring is not None:
                        return True

                    if self.pre_fec_ber_mantissa is not None:
                        return True

                    if self.pre_fec_ber_value is not None:
                        return True

                    if self.pre_fec_mantissa is not None:
                        return True

                    if self.pre_fec_val is not None:
                        return True

                    if self.proactive is not None and self.proactive._has_data():
                        return True

                    if self.q is not None:
                        return True

                    if self.q_margin is not None:
                        return True

                    if self.remote is not None and self.remote._has_data():
                        return True

                    if self.sd is not None:
                        return True

                    if self.sf is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.tti_mode is not None and self.tti_mode._has_data():
                        return True

                    if self.uc is not None:
                        return True

                    if self.uc_value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                    return meta._meta_table['Otu.Controllers.Controller.Info']['meta_info']

            @property
            def _common_path(self):
                if self.controller_name is None:
                    raise YPYModelError('Key property controller_name is None')

                return '/Cisco-IOS-XR-controller-otu-oper:otu/Cisco-IOS-XR-controller-otu-oper:controllers/Cisco-IOS-XR-controller-otu-oper:controller[Cisco-IOS-XR-controller-otu-oper:controller-name = ' + str(self.controller_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.controller_name is not None:
                    return True

                if self.info is not None and self.info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                return meta._meta_table['Otu.Controllers.Controller']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-controller-otu-oper:otu/Cisco-IOS-XR-controller-otu-oper:controllers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.controller is not None:
                for child_ref in self.controller:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
            return meta._meta_table['Otu.Controllers']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-controller-otu-oper:otu'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.controllers is not None and self.controllers._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['Otu']['meta_info']



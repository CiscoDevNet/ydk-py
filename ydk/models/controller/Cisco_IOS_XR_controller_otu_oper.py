""" Cisco_IOS_XR_controller_otu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package operational data.

This module contains definitions
for the following management objects\:
  otu\: OTU operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class GmplsOtuTtiMode_Enum(Enum):
    """
    GmplsOtuTtiMode_Enum

    Gmpls otu tti mode

    """

    """

    Not Set

    """
    GMPLS_OTU_TTI_MODE_NONE = 0

    """

    Section Monitoring

    """
    GMPLS_OTU_TTI_MODE_SM = 1

    """

    Path Monitoring

    """
    GMPLS_OTU_TTI_MODE_PM = 2

    """

    Tandem Connection Monitoring

    """
    GMPLS_OTU_TTI_MODE_TCM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['GmplsOtuTtiMode_Enum']


class OtuDerState_Enum(Enum):
    """
    OtuDerState_Enum

    Otu der state

    """

    """

    Out Of Service

    """
    OUT_OF_SERVICE = 0

    """

    In Service

    """
    IN_SERVICE = 1

    """

    Maintenance

    """
    MAINTENANCE = 2

    """

    Automatic In Service

    """
    AIS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuDerState_Enum']


class OtuG709fecMode_Enum(Enum):
    """
    OtuG709fecMode_Enum

    Otu g709fec mode

    """

    """

    NONE

    """
    OTU_BAG_NONE_FEC = 1

    """

    STANDARD

    """
    OTU_BAG_STANDARD_FEC = 2

    """

    ENHANCEDI.7

    """
    OTU_BAG_1_I_7_FEC = 4

    """

    ENHANCEDI.4

    """
    OTU_BAG_1_I_4_FEC = 8

    """

    SWIZZLE

    """
    OTU_BAG_SWIZZLE_FEC = 16

    """

    HIGH GAIN20

    """
    OTU_BAG_HG20_FEC = 32

    """

    Enhanced High Gain 7

    """
    OTU_BAG_ENHANCED_HG7_FEC = 64

    """

    Soft\-Decision 20

    """
    OTU_BAG_SD20_FEC = 128

    """

    Soft\-Decision 7

    """
    OTU_BAG_SD7_FEC = 256

    """

    ALL

    """
    OTU_BAG_ALL_FEC = 512


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuG709fecMode_Enum']


class OtuLoopBackMode_Enum(Enum):
    """
    OtuLoopBackMode_Enum

    Otu loop back mode

    """

    """

    None

    """
    NONE = 1

    """

    Line

    """
    LINE = 2

    """

    Internal

    """
    INTERNAL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuLoopBackMode_Enum']


class OtuPerMon_Enum(Enum):
    """
    OtuPerMon_Enum

    Otu per mon

    """

    """

    Disable

    """
    DISABLE = 0

    """

    Enable

    """
    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPerMon_Enum']


class OtuPpFsmState_Enum(Enum):
    """
    OtuPpFsmState_Enum

    Otu pp fsm state

    """

    """

    In Active

    """
    OTU_IN_ACTIVE = 0

    """

    Disabled

    """
    OTU_DISABLED = 1

    """

    Normal

    """
    OTU_NORMAL_STATE = 2

    """

    Local Failing

    """
    OTU_LOCAL_FAILING = 3

    """

    Remote Failing

    """
    OTU_REMOTE_FAILING = 4

    """

    Maintance Failing

    """
    OTU_MAIN_T_FAILING = 5

    """

    Regenerator Failing

    """
    OTU_REGEN_FAILING = 6

    """

    Local Failed

    """
    OTU_LOCAL_FAILED = 7

    """

    Remote Failed

    """
    OTU_REMOTE_FAILED = 8

    """

    Maintance Failed

    """
    OTU_MAIN_T_FAILED = 9

    """

    Regenerator Failed

    """
    OTU_REGEN_FAILED = 10


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpFsmState_Enum']


class OtuPpIntfState_Enum(Enum):
    """
    OtuPpIntfState_Enum

    Otu pp intf state

    """

    """

    Interface is Up

    """
    OTU_PP_INTF_UP = 0

    """

    Interface is Going Down

    """
    OTU_PP_INTF_FAILING = 1

    """

    Interface Down

    """
    OTU_PP_INTF_DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpIntfState_Enum']


class OtuSecState_Enum(Enum):
    """
    OtuSecState_Enum

    Otu sec state

    """

    """

    Normal

    """
    NORMAL = 0

    """

    Maintenance

    """
    MAINTENANCE = 1

    """

    Automatic In Service

    """
    AIS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuSecState_Enum']


class OtuStateEt_Enum(Enum):
    """
    OtuStateEt_Enum

    Otu state et

    """

    """

    Not Ready

    """
    NOT_READY = 0

    """

    Admin Down

    """
    ADMIN_DOWN = 1

    """

    Down

    """
    DOWN = 2

    """

    Up

    """
    UP = 3

    """

    Shutdown

    """
    SHUTDOWN = 4

    """

    Error Disable

    """
    ERROR_DISABLE = 5

    """

    Down Immediate

    """
    DOWN_IMMEDIATE = 6

    """

    Down Immediate Admin

    """
    DOWN_IMMEDIATE_ADMIN = 7

    """

    Down Graceful

    """
    DOWN_GRACEFUL = 8

    """

    Begin Shutdown

    """
    BEGIN_SHUTDOWN = 9

    """

    End Shutdown

    """
    END_SHUTDOWN = 10

    """

    Begin Error Disable

    """
    BEGIN_ERROR_DISABLE = 11

    """

    End Error Disable

    """
    END_ERROR_DISABLE = 12

    """

    Begin Down Graceful

    """
    BEGIN_DOWN_GRACEFUL = 13

    """

    Reset

    """
    RESET = 14

    """

    Operational

    """
    OPERATIONAL = 15

    """

    Not Operational

    """
    NOT_OPERATIONAL = 16

    """

    Unknown

    """
    UNKNOWN = 17

    """

    Last

    """
    LAST = 18


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuStateEt_Enum']


class OtuTtiEt_Enum(Enum):
    """
    OtuTtiEt_Enum

    Otu tti et

    """

    """

    ASCII

    """
    ASCII = 0

    """

    HEX

    """
    HEX = 1

    """

    FULL ASCII

    """
    FULL_ASCII = 2

    """

    FULL HEX

    """
    FULL_HEX = 3


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuTtiEt_Enum']



class Otu(object):
    """
    OTU operational data
    
    .. attribute:: controllers
    
    	All OTU Port operational data
    	**type**\: :py:class:`Controllers <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers>`
    
    

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
        	**type**\: list of :py:class:`Controller <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller>`
        
        

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
            
            .. attribute:: controller_name
            
            	Port name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: info
            
            	OTU port operational data
            	**type**\: :py:class:`Info <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info>`
            
            

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
                
                .. attribute:: derivedstate_mode
                
                	Derived State
                	**type**\: :py:class:`OtuDerState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuDerState_Enum>`
                
                .. attribute:: ec
                
                	Average bit errors corrected
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ec_value
                
                	EC value present
                	**type**\: bool
                
                .. attribute:: fec_mode
                
                	FEC
                	**type**\: :py:class:`OtuG709fecMode_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuG709fecMode_Enum>`
                
                .. attribute:: gcc_mode
                
                	OTU GCC
                	**type**\: bool
                
                .. attribute:: gmpls_tti_mode
                
                	GMPLS TTI MODE
                	**type**\: :py:class:`GmplsOtuTtiMode_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.GmplsOtuTtiMode_Enum>`
                
                .. attribute:: gmpls_tvm_id
                
                	GMPLS TCM ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: local
                
                	TTI
                	**type**\: :py:class:`Local <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Local>`
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\: :py:class:`OtuLoopBackMode_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuLoopBackMode_Enum>`
                
                .. attribute:: name
                
                	Interface Name
                	**type**\: str
                
                .. attribute:: network_srlg
                
                	Network SRLG
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\: bool
                
                .. attribute:: otu_alarm_info
                
                	OTU layer alarm Information
                	**type**\: :py:class:`OtuAlarmInfo <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo>`
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\: :py:class:`OtuPerMon_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuPerMon_Enum>`
                
                .. attribute:: pre_fec_ber_mantissa
                
                	Pre fec val mantissa
                	**type**\: bool
                
                .. attribute:: pre_fec_ber_value
                
                	Pre fec val present 
                	**type**\: bool
                
                .. attribute:: pre_fec_mantissa
                
                	Pre FEC BER Mantissa in form E\-<mantisaa>
                	**type**\: int
                
                	**range:** \-128..127
                
                .. attribute:: pre_fec_val
                
                	Pre FEC BER Value in form 0.00
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: proactive
                
                	Proactive Protection
                	**type**\: :py:class:`Proactive <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Proactive>`
                
                .. attribute:: q
                
                	q value calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: q_margin
                
                	q margin calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote
                
                	Remote
                	**type**\: :py:class:`Remote <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Remote>`
                
                .. attribute:: sd
                
                	SD
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: sec_state
                
                	Sec State
                	**type**\: :py:class:`OtuSecState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuSecState_Enum>`
                
                .. attribute:: sf
                
                	SF
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: state
                
                	Admin State
                	**type**\: :py:class:`OtuStateEt_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuStateEt_Enum>`
                
                .. attribute:: tti_mode
                
                	OTU TTI
                	**type**\: :py:class:`TtiMode <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode>`
                
                .. attribute:: uc
                
                	Uncorrected word count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: uc_value
                
                	Uc value present
                	**type**\: bool
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.derivedstate_mode = None
                    self.ec = None
                    self.ec_value = None
                    self.fec_mode = None
                    self.gcc_mode = None
                    self.gmpls_tti_mode = None
                    self.gmpls_tvm_id = None
                    self.local = Otu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self.loopback_mode = None
                    self.name = None
                    self.network_srlg = []
                    self.nv_optical_support = None
                    self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                    self.otu_alarm_info.parent = self
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
                    self.sec_state = None
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
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:local'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.if_index is not None:
                            return True

                        if self.router_id is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Local']['meta_info']


                class OtuAlarmInfo(object):
                    """
                    OTU layer alarm Information
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\: :py:class:`Ais <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais>`
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\: :py:class:`Bdi <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi>`
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\: :py:class:`Biae <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae>`
                    
                    .. attribute:: ec
                    
                    	EC alarm
                    	**type**\: :py:class:`Ec <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec>`
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\: :py:class:`Eoc <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc>`
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\: :py:class:`FecMismatch <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch>`
                    
                    .. attribute:: fecunc
                    
                    	FEC UnCorrected Word
                    	**type**\: :py:class:`Fecunc <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc>`
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\: :py:class:`Iae <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae>`
                    
                    .. attribute:: lof
                    
                    	Loss of Frame
                    	**type**\: :py:class:`Lof <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof>`
                    
                    .. attribute:: lom
                    
                    	Loss of MultiFrame
                    	**type**\: :py:class:`Lom <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom>`
                    
                    .. attribute:: los
                    
                    	Loss of Signal
                    	**type**\: :py:class:`Los <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Los>`
                    
                    .. attribute:: oof
                    
                    	Out of Frame
                    	**type**\: :py:class:`Oof <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof>`
                    
                    .. attribute:: oom
                    
                    	Out of MultiFrame
                    	**type**\: :py:class:`Oom <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom>`
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\: :py:class:`SdBer <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer>`
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\: :py:class:`SfBer <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer>`
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch
                    	**type**\: :py:class:`Tim <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim>`
                    
                    .. attribute:: uc
                    
                    	UC alarm
                    	**type**\: :py:class:`Uc <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc>`
                    
                    

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


                    class Ais(object):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:ais'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais']['meta_info']


                    class Bdi(object):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:bdi'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi']['meta_info']


                    class Biae(object):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:biae'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae']['meta_info']


                    class Ec(object):
                        """
                        EC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:ec'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec']['meta_info']


                    class Eoc(object):
                        """
                        GCC End of Channel
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:eoc'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc']['meta_info']


                    class FecMismatch(object):
                        """
                        FEC mismatch alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:fec-mismatch'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch']['meta_info']


                    class Fecunc(object):
                        """
                        FEC UnCorrected Word
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:fecunc'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc']['meta_info']


                    class Iae(object):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:iae'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae']['meta_info']


                    class Lof(object):
                        """
                        Loss of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:lof'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof']['meta_info']


                    class Lom(object):
                        """
                        Loss of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:lom'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom']['meta_info']


                    class Los(object):
                        """
                        Loss of Signal
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:los'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Los']['meta_info']


                    class Oof(object):
                        """
                        Out of Frame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:oof'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof']['meta_info']


                    class Oom(object):
                        """
                        Out of MultiFrame
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:oom'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom']['meta_info']


                    class SdBer(object):
                        """
                        SD BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:sd-ber'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer']['meta_info']


                    class SfBer(object):
                        """
                        SF BER alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:sf-ber'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer']['meta_info']


                    class Tim(object):
                        """
                        Trace Identifier Mismatch
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tim'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim']['meta_info']


                    class Uc(object):
                        """
                        UC alarm
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        

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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:uc'

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

                            if self.is_asserted is not None:
                                return True

                            if self.is_detected is not None:
                                return True

                            if self.reporting_enabled is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:otu-alarm-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.ais is not None and self.ais._has_data():
                            return True

                        if self.ais is not None and self.ais.is_presence():
                            return True

                        if self.bdi is not None and self.bdi._has_data():
                            return True

                        if self.bdi is not None and self.bdi.is_presence():
                            return True

                        if self.biae is not None and self.biae._has_data():
                            return True

                        if self.biae is not None and self.biae.is_presence():
                            return True

                        if self.ec is not None and self.ec._has_data():
                            return True

                        if self.ec is not None and self.ec.is_presence():
                            return True

                        if self.eoc is not None and self.eoc._has_data():
                            return True

                        if self.eoc is not None and self.eoc.is_presence():
                            return True

                        if self.fec_mismatch is not None and self.fec_mismatch._has_data():
                            return True

                        if self.fec_mismatch is not None and self.fec_mismatch.is_presence():
                            return True

                        if self.fecunc is not None and self.fecunc._has_data():
                            return True

                        if self.fecunc is not None and self.fecunc.is_presence():
                            return True

                        if self.iae is not None and self.iae._has_data():
                            return True

                        if self.iae is not None and self.iae.is_presence():
                            return True

                        if self.lof is not None and self.lof._has_data():
                            return True

                        if self.lof is not None and self.lof.is_presence():
                            return True

                        if self.lom is not None and self.lom._has_data():
                            return True

                        if self.lom is not None and self.lom.is_presence():
                            return True

                        if self.los is not None and self.los._has_data():
                            return True

                        if self.los is not None and self.los.is_presence():
                            return True

                        if self.oof is not None and self.oof._has_data():
                            return True

                        if self.oof is not None and self.oof.is_presence():
                            return True

                        if self.oom is not None and self.oom._has_data():
                            return True

                        if self.oom is not None and self.oom.is_presence():
                            return True

                        if self.sd_ber is not None and self.sd_ber._has_data():
                            return True

                        if self.sd_ber is not None and self.sd_ber.is_presence():
                            return True

                        if self.sf_ber is not None and self.sf_ber._has_data():
                            return True

                        if self.sf_ber is not None and self.sf_ber.is_presence():
                            return True

                        if self.tim is not None and self.tim._has_data():
                            return True

                        if self.tim is not None and self.tim.is_presence():
                            return True

                        if self.uc is not None and self.uc._has_data():
                            return True

                        if self.uc is not None and self.uc.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']


                class Proactive(object):
                    """
                    Proactive Protection
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\: :py:class:`OtuPpIntfState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuPpIntfState_Enum>`
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\: :py:class:`OtuPpFsmState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuPpFsmState_Enum>`
                    
                    .. attribute:: proactive_status
                    
                    	Proactive Status
                    	**type**\: bool
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: sec_state
                    
                    	Secondary Admin State
                    	**type**\: :py:class:`OtuSecState_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuSecState_Enum>`
                    
                    .. attribute:: trig_thresh_coeff
                    
                    	Trigger threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trig_thresh_power
                    
                    	Trigger threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: trigger_window
                    
                    	Trigger Integration window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.proactive_fsm_if_state = None
                        self.proactive_fsm_state = None
                        self.proactive_status = None
                        self.revert_window = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.sec_state = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.trigger_window = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:proactive'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
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

                        if self.sec_state is not None:
                            return True

                        if self.trig_thresh_coeff is not None:
                            return True

                        if self.trig_thresh_power is not None:
                            return True

                        if self.trigger_window is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Proactive']['meta_info']


                class Remote(object):
                    """
                    Remote
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
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
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:remote'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.if_index is not None:
                            return True

                        if self.router_id is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Remote']['meta_info']


                class TtiMode(object):
                    """
                    OTU TTI
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\: :py:class:`Exp <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\: :py:class:`OtuTtiEt_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt_Enum>`
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\: :py:class:`OtuTtiEt_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt_Enum>`
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI sent
                    	**type**\: :py:class:`OtuTtiEt_Enum <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt_Enum>`
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\: :py:class:`Rec <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\: :py:class:`Tx <ydk.models.controller.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    

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
                        self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self


                    class Exp(object):
                        """
                        String Expected
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = []
                            self.operator_specific = []
                            self.sapi = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:exp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
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

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp']['meta_info']


                    class Rec(object):
                        """
                        String Received
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = []
                            self.operator_specific = []
                            self.sapi = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:rec'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
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

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec']['meta_info']


                    class Tx(object):
                        """
                        String Sent
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dapi = []
                            self.operator_specific = []
                            self.sapi = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tx'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.dapi is not None:
                                for child in self.dapi:
                                    if child is not None:
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

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:tti-mode'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.exp is not None and self.exp._has_data():
                            return True

                        if self.exp is not None and self.exp.is_presence():
                            return True

                        if self.g709tti_exp_mode is not None:
                            return True

                        if self.g709tti_rec_mode is not None:
                            return True

                        if self.g709tti_sent_mode is not None:
                            return True

                        if self.rec is not None and self.rec._has_data():
                            return True

                        if self.rec is not None and self.rec.is_presence():
                            return True

                        if self.tx is not None and self.tx._has_data():
                            return True

                        if self.tx is not None and self.tx.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-controller-otu-oper:info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
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

                    if self.local is not None and self.local._has_data():
                        return True

                    if self.local is not None and self.local.is_presence():
                        return True

                    if self.loopback_mode is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.network_srlg is not None:
                        for child in self.network_srlg:
                            if child is not None:
                                return True

                    if self.nv_optical_support is not None:
                        return True

                    if self.otu_alarm_info is not None and self.otu_alarm_info._has_data():
                        return True

                    if self.otu_alarm_info is not None and self.otu_alarm_info.is_presence():
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

                    if self.proactive is not None and self.proactive.is_presence():
                        return True

                    if self.q is not None:
                        return True

                    if self.q_margin is not None:
                        return True

                    if self.remote is not None and self.remote._has_data():
                        return True

                    if self.remote is not None and self.remote.is_presence():
                        return True

                    if self.sd is not None:
                        return True

                    if self.sec_state is not None:
                        return True

                    if self.sf is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.tti_mode is not None and self.tti_mode._has_data():
                        return True

                    if self.tti_mode is not None and self.tti_mode.is_presence():
                        return True

                    if self.uc is not None:
                        return True

                    if self.uc_value is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                    return meta._meta_table['Otu.Controllers.Controller.Info']['meta_info']

            @property
            def _common_path(self):
                if self.controller_name is None:
                    raise YPYDataValidationError('Key property controller_name is None')

                return '/Cisco-IOS-XR-controller-otu-oper:otu/Cisco-IOS-XR-controller-otu-oper:controllers/Cisco-IOS-XR-controller-otu-oper:controller[Cisco-IOS-XR-controller-otu-oper:controller-name = ' + str(self.controller_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.controller_name is not None:
                    return True

                if self.info is not None and self.info._has_data():
                    return True

                if self.info is not None and self.info.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                return meta._meta_table['Otu.Controllers.Controller']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-controller-otu-oper:otu/Cisco-IOS-XR-controller-otu-oper:controllers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.controller is not None:
                for child_ref in self.controller:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
            return meta._meta_table['Otu.Controllers']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-controller-otu-oper:otu'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.controllers is not None and self.controllers._has_data():
            return True

        if self.controllers is not None and self.controllers.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['Otu']['meta_info']



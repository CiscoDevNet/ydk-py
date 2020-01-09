""" Cisco_IOS_XR_controller_otu_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package operational data.

This module contains definitions
for the following management objects\:
  otu\: OTU operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class GmplsOtuTtiMode(Enum):
    """
    GmplsOtuTtiMode (Enum Class)

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

    gmpls_otu_tti_mode_none = Enum.YLeaf(0, "gmpls-otu-tti-mode-none")

    gmpls_otu_tti_mode_sm = Enum.YLeaf(1, "gmpls-otu-tti-mode-sm")

    gmpls_otu_tti_mode_pm = Enum.YLeaf(2, "gmpls-otu-tti-mode-pm")

    gmpls_otu_tti_mode_tcm = Enum.YLeaf(3, "gmpls-otu-tti-mode-tcm")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['GmplsOtuTtiMode']


class OtuAinsStateEt(Enum):
    """
    OtuAinsStateEt (Enum Class)

    Otu ains state et

    .. data:: none = 0

    	None

    .. data:: active_running = 1

    	Running

    .. data:: active_pending = 2

    	Pending

    """

    none = Enum.YLeaf(0, "none")

    active_running = Enum.YLeaf(1, "active-running")

    active_pending = Enum.YLeaf(2, "active-pending")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuAinsStateEt']


class OtuDerState(Enum):
    """
    OtuDerState (Enum Class)

    Otu der state

    .. data:: out_of_service = 0

    	Out Of Service

    .. data:: in_service = 1

    	In Service

    .. data:: maintenance = 2

    	Maintenance

    .. data:: ains = 3

    	Automatic In Service

    """

    out_of_service = Enum.YLeaf(0, "out-of-service")

    in_service = Enum.YLeaf(1, "in-service")

    maintenance = Enum.YLeaf(2, "maintenance")

    ains = Enum.YLeaf(3, "ains")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuDerState']


class OtuG709fecMode(Enum):
    """
    OtuG709fecMode (Enum Class)

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

    .. data:: otu_bag_sd15_fec = 512

    	Soft-Decision 15

    .. data:: otu_bag_sd27_fec = 1024

    	Soft-Decision 27

    .. data:: otu_bag_all_fec = 2048

    	ALL

    """

    otu_bag_none_fec = Enum.YLeaf(1, "otu-bag-none-fec")

    otu_bag_standard_fec = Enum.YLeaf(2, "otu-bag-standard-fec")

    otu_bag_1_i_7_fec = Enum.YLeaf(4, "otu-bag-1-i-7-fec")

    otu_bag_1_i_4_fec = Enum.YLeaf(8, "otu-bag-1-i-4-fec")

    otu_bag_swizzle_fec = Enum.YLeaf(16, "otu-bag-swizzle-fec")

    otu_bag_hg20_fec = Enum.YLeaf(32, "otu-bag-hg20-fec")

    otu_bag_enhanced_hg7_fec = Enum.YLeaf(64, "otu-bag-enhanced-hg7-fec")

    otu_bag_sd20_fec = Enum.YLeaf(128, "otu-bag-sd20-fec")

    otu_bag_sd7_fec = Enum.YLeaf(256, "otu-bag-sd7-fec")

    otu_bag_sd15_fec = Enum.YLeaf(512, "otu-bag-sd15-fec")

    otu_bag_sd27_fec = Enum.YLeaf(1024, "otu-bag-sd27-fec")

    otu_bag_all_fec = Enum.YLeaf(2048, "otu-bag-all-fec")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuG709fecMode']


class OtuLoopBackMode(Enum):
    """
    OtuLoopBackMode (Enum Class)

    Otu loop back mode

    .. data:: none = 1

    	None

    .. data:: line = 2

    	Line

    .. data:: internal = 4

    	Internal

    """

    none = Enum.YLeaf(1, "none")

    line = Enum.YLeaf(2, "line")

    internal = Enum.YLeaf(4, "internal")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuLoopBackMode']


class OtuPerMon(Enum):
    """
    OtuPerMon (Enum Class)

    Otu per mon

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPerMon']


class OtuPpFsmState(Enum):
    """
    OtuPpFsmState (Enum Class)

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

    otu_in_active = Enum.YLeaf(0, "otu-in-active")

    otu_disabled = Enum.YLeaf(1, "otu-disabled")

    otu_normal_state = Enum.YLeaf(2, "otu-normal-state")

    otu_local_failing = Enum.YLeaf(3, "otu-local-failing")

    otu_remote_failing = Enum.YLeaf(4, "otu-remote-failing")

    otu_main_t_failing = Enum.YLeaf(5, "otu-main-t-failing")

    otu_regen_failing = Enum.YLeaf(6, "otu-regen-failing")

    otu_local_failed = Enum.YLeaf(7, "otu-local-failed")

    otu_remote_failed = Enum.YLeaf(8, "otu-remote-failed")

    otu_main_t_failed = Enum.YLeaf(9, "otu-main-t-failed")

    otu_regen_failed = Enum.YLeaf(10, "otu-regen-failed")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpFsmState']


class OtuPpIntfState(Enum):
    """
    OtuPpIntfState (Enum Class)

    Otu pp intf state

    .. data:: otu_pp_intf_up = 0

    	Interface is Up

    .. data:: otu_pp_intf_failing = 1

    	Interface is Going Down

    .. data:: otu_pp_intf_down = 2

    	Interface Down

    """

    otu_pp_intf_up = Enum.YLeaf(0, "otu-pp-intf-up")

    otu_pp_intf_failing = Enum.YLeaf(1, "otu-pp-intf-failing")

    otu_pp_intf_down = Enum.YLeaf(2, "otu-pp-intf-down")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPpIntfState']


class OtuPrbsMode(Enum):
    """
    OtuPrbsMode (Enum Class)

    Otu prbs mode

    .. data:: not_applicable = 0

    	OTU PRBS mode not applicable

    .. data:: source = 1

    	Source

    .. data:: sink = 2

    	Sink

    .. data:: source_sink = 3

    	Source Sink

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    source = Enum.YLeaf(1, "source")

    sink = Enum.YLeaf(2, "sink")

    source_sink = Enum.YLeaf(3, "source-sink")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPrbsMode']


class OtuPrbsPattern(Enum):
    """
    OtuPrbsPattern (Enum Class)

    Otu prbs pattern

    .. data:: not_applicable = 0

    	OTU PRBS pattern not applicable

    .. data:: pn31 = 1

    	PN31

    .. data:: pn23 = 2

    	PN23

    .. data:: pn11 = 4

    	PN11

    .. data:: inverted_pn31 = 8

    	INVERTED PN31

    .. data:: inverted_pn11 = 16

    	INVERTED PN11

    .. data:: pn15 = 32

    	PN15

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    pn31 = Enum.YLeaf(1, "pn31")

    pn23 = Enum.YLeaf(2, "pn23")

    pn11 = Enum.YLeaf(4, "pn11")

    inverted_pn31 = Enum.YLeaf(8, "inverted-pn31")

    inverted_pn11 = Enum.YLeaf(16, "inverted-pn11")

    pn15 = Enum.YLeaf(32, "pn15")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPrbsPattern']


class OtuPrbsStatus(Enum):
    """
    OtuPrbsStatus (Enum Class)

    Otu prbs status

    .. data:: locked = 0

    	Locked

    .. data:: unlocked = 1

    	Unlocked

    .. data:: not_applicable = 2

    	Not Applicable

    """

    locked = Enum.YLeaf(0, "locked")

    unlocked = Enum.YLeaf(1, "unlocked")

    not_applicable = Enum.YLeaf(2, "not-applicable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPrbsStatus']


class OtuPrbsTest(Enum):
    """
    OtuPrbsTest (Enum Class)

    Otu prbs test

    .. data:: disable = 0

    	Disable

    .. data:: enable = 1

    	Enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuPrbsTest']


class OtuSecState(Enum):
    """
    OtuSecState (Enum Class)

    Otu sec state

    .. data:: normal = 0

    	Normal

    .. data:: maintenance = 1

    	Maintenance

    .. data:: ains = 2

    	Automatic In Service

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")

    ains = Enum.YLeaf(2, "ains")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuSecState']


class OtuStateEt(Enum):
    """
    OtuStateEt (Enum Class)

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

    not_ready = Enum.YLeaf(0, "not-ready")

    admin_down = Enum.YLeaf(1, "admin-down")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    shutdown = Enum.YLeaf(4, "shutdown")

    error_disable = Enum.YLeaf(5, "error-disable")

    down_immediate = Enum.YLeaf(6, "down-immediate")

    down_immediate_admin = Enum.YLeaf(7, "down-immediate-admin")

    down_graceful = Enum.YLeaf(8, "down-graceful")

    begin_shutdown = Enum.YLeaf(9, "begin-shutdown")

    end_shutdown = Enum.YLeaf(10, "end-shutdown")

    begin_error_disable = Enum.YLeaf(11, "begin-error-disable")

    end_error_disable = Enum.YLeaf(12, "end-error-disable")

    begin_down_graceful = Enum.YLeaf(13, "begin-down-graceful")

    reset = Enum.YLeaf(14, "reset")

    operational = Enum.YLeaf(15, "operational")

    not_operational = Enum.YLeaf(16, "not-operational")

    unknown = Enum.YLeaf(17, "unknown")

    last = Enum.YLeaf(18, "last")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuStateEt']


class OtuTtiEt(Enum):
    """
    OtuTtiEt (Enum Class)

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

    ascii = Enum.YLeaf(0, "ascii")

    hex = Enum.YLeaf(1, "hex")

    full_ascii = Enum.YLeaf(2, "full-ascii")

    full_hex = Enum.YLeaf(3, "full-hex")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['OtuTtiEt']



class Otu(_Entity_):
    """
    OTU operational data
    
    .. attribute:: controllers
    
    	All OTU Port operational data
    	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers>`
    
    	**config**\: False
    
    

    """

    _prefix = 'controller-otu-oper'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Otu, self).__init__()
        self._top_entity = None

        self.yang_name = "otu"
        self.yang_parent_name = "Cisco-IOS-XR-controller-otu-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controllers", ("controllers", Otu.Controllers))])
        self._leafs = OrderedDict()

        self.controllers = Otu.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._segment_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Otu, [], name, value)


    class Controllers(_Entity_):
        """
        All OTU Port operational data
        
        .. attribute:: controller
        
        	OTU Port operational data
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller>`
        
        	**config**\: False
        
        

        """

        _prefix = 'controller-otu-oper'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Otu.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "otu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("controller", ("controller", Otu.Controllers.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Otu.Controllers, [], name, value)


        class Controller(_Entity_):
            """
            OTU Port operational data
            
            .. attribute:: controller_name  (key)
            
            	Port name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: prbs
            
            	OTU port PRBS operational data
            	**type**\:  :py:class:`Prbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Prbs>`
            
            	**config**\: False
            
            .. attribute:: info
            
            	OTU port operational data
            	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info>`
            
            	**config**\: False
            
            

            """

            _prefix = 'controller-otu-oper'
            _revision = '2017-05-01'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Otu.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_classes = OrderedDict([("prbs", ("prbs", Otu.Controllers.Controller.Prbs)), ("info", ("info", Otu.Controllers.Controller.Info))])
                self._leafs = OrderedDict([
                    ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                ])
                self.controller_name = None

                self.prbs = Otu.Controllers.Controller.Prbs()
                self.prbs.parent = self
                self._children_name_map["prbs"] = "prbs"

                self.info = Otu.Controllers.Controller.Info()
                self.info.parent = self
                self._children_name_map["info"] = "info"
                self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-controller-otu-oper:otu/controllers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Otu.Controllers.Controller, ['controller_name'], name, value)


            class Prbs(_Entity_):
                """
                OTU port PRBS operational data
                
                .. attribute:: otu_prbs_test
                
                	otu prbs test
                	**type**\:  :py:class:`OtuPrbsTest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsTest>`
                
                	**config**\: False
                
                .. attribute:: otu_prbs_mode
                
                	otu prbs mode
                	**type**\:  :py:class:`OtuPrbsMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsMode>`
                
                	**config**\: False
                
                .. attribute:: otu_prbs_pattern
                
                	otu prbs pattern
                	**type**\:  :py:class:`OtuPrbsPattern <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsPattern>`
                
                	**config**\: False
                
                .. attribute:: otu_prbs_status
                
                	otu prbs status
                	**type**\:  :py:class:`OtuPrbsStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPrbsStatus>`
                
                	**config**\: False
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Otu.Controllers.Controller.Prbs, self).__init__()

                    self.yang_name = "prbs"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('otu_prbs_test', (YLeaf(YType.enumeration, 'otu-prbs-test'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPrbsTest', '')])),
                        ('otu_prbs_mode', (YLeaf(YType.enumeration, 'otu-prbs-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPrbsMode', '')])),
                        ('otu_prbs_pattern', (YLeaf(YType.enumeration, 'otu-prbs-pattern'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPrbsPattern', '')])),
                        ('otu_prbs_status', (YLeaf(YType.enumeration, 'otu-prbs-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPrbsStatus', '')])),
                    ])
                    self.otu_prbs_test = None
                    self.otu_prbs_mode = None
                    self.otu_prbs_pattern = None
                    self.otu_prbs_status = None
                    self._segment_path = lambda: "prbs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Otu.Controllers.Controller.Prbs, ['otu_prbs_test', 'otu_prbs_mode', 'otu_prbs_pattern', 'otu_prbs_status'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                    return meta._meta_table['Otu.Controllers.Controller.Prbs']['meta_info']


            class Info(_Entity_):
                """
                OTU port operational data
                
                .. attribute:: local
                
                	TTI
                	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Local>`
                
                	**config**\: False
                
                .. attribute:: remote
                
                	Remote
                	**type**\:  :py:class:`Remote <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Remote>`
                
                	**config**\: False
                
                .. attribute:: tti_mode
                
                	OTU TTI
                	**type**\:  :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode>`
                
                	**config**\: False
                
                .. attribute:: network_srlg
                
                	Network Shared Risk Link Group information
                	**type**\:  :py:class:`NetworkSrlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg>`
                
                	**config**\: False
                
                .. attribute:: otu_alarm_info
                
                	OTU layer alarm Information
                	**type**\:  :py:class:`OtuAlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo>`
                
                	**config**\: False
                
                .. attribute:: proactive
                
                	Proactive Protection
                	**type**\:  :py:class:`Proactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.Proactive>`
                
                	**config**\: False
                
                .. attribute:: otu_fec_satistics
                
                	OTU FEC Statistics
                	**type**\:  :py:class:`OtuFecSatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuFecSatistics>`
                
                	**config**\: False
                
                .. attribute:: ains_info
                
                	AINS information
                	**type**\:  :py:class:`AinsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.AinsInfo>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	Admin State
                	**type**\:  :py:class:`OtuStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuStateEt>`
                
                	**config**\: False
                
                .. attribute:: name
                
                	Interface Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sf
                
                	SF in the form of 1.0E \- <SF>
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sd
                
                	SD in the form of 1.0E \- <SD>
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: loopback_mode
                
                	Loopback
                	**type**\:  :py:class:`OtuLoopBackMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuLoopBackMode>`
                
                	**config**\: False
                
                .. attribute:: fec_mode
                
                	FEC
                	**type**\:  :py:class:`OtuG709fecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuG709fecMode>`
                
                	**config**\: False
                
                .. attribute:: derivedstate_mode
                
                	Derived State
                	**type**\:  :py:class:`OtuDerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuDerState>`
                
                	**config**\: False
                
                .. attribute:: inherit_sec_state
                
                	Sec State
                	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                	**config**\: False
                
                .. attribute:: config_sec_state
                
                	Sec State
                	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                
                	**config**\: False
                
                .. attribute:: gcc_mode
                
                	OTU GCC
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: q
                
                	q value calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: q_margin
                
                	q margin calculated
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: performance_monitoring
                
                	Performance Monitoring
                	**type**\:  :py:class:`OtuPerMon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPerMon>`
                
                	**config**\: False
                
                .. attribute:: ec
                
                	Average bit errors corrected
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: uc
                
                	Uncorrected word count
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pre_fec_val
                
                	Pre FEC BER Value in form 0.00
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**config**\: False
                
                .. attribute:: pre_fec_mantissa
                
                	Pre FEC BER Mantissa in form E\-<mantisaa>
                	**type**\: int
                
                	**range:** \-128..127
                
                	**config**\: False
                
                .. attribute:: ec_value
                
                	EC value present
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: uc_value
                
                	Uc value present
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pre_fec_ber_value
                
                	Pre fec val present 
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pre_fec_ber_mantissa
                
                	Pre fec val mantissa
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: nv_optical_support
                
                	NV Optical support
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: gmpls_tti_mode
                
                	GMPLS TTI MODE
                	**type**\:  :py:class:`GmplsOtuTtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.GmplsOtuTtiMode>`
                
                	**config**\: False
                
                .. attribute:: gmpls_tvm_id
                
                	GMPLS TCM ID
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: auto_tti_flag
                
                	Auto tti flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: description
                
                	Controller description string
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'controller-otu-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Otu.Controllers.Controller.Info, self).__init__()

                    self.yang_name = "info"
                    self.yang_parent_name = "controller"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local", ("local", Otu.Controllers.Controller.Info.Local)), ("remote", ("remote", Otu.Controllers.Controller.Info.Remote)), ("tti-mode", ("tti_mode", Otu.Controllers.Controller.Info.TtiMode)), ("network-srlg", ("network_srlg", Otu.Controllers.Controller.Info.NetworkSrlg)), ("otu-alarm-info", ("otu_alarm_info", Otu.Controllers.Controller.Info.OtuAlarmInfo)), ("proactive", ("proactive", Otu.Controllers.Controller.Info.Proactive)), ("otu-fec-satistics", ("otu_fec_satistics", Otu.Controllers.Controller.Info.OtuFecSatistics)), ("ains-info", ("ains_info", Otu.Controllers.Controller.Info.AinsInfo))])
                    self._leafs = OrderedDict([
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuStateEt', '')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('sf', (YLeaf(YType.uint8, 'sf'), ['int'])),
                        ('sd', (YLeaf(YType.uint8, 'sd'), ['int'])),
                        ('loopback_mode', (YLeaf(YType.enumeration, 'loopback-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuLoopBackMode', '')])),
                        ('fec_mode', (YLeaf(YType.enumeration, 'fec-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuG709fecMode', '')])),
                        ('derivedstate_mode', (YLeaf(YType.enumeration, 'derivedstate-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuDerState', '')])),
                        ('inherit_sec_state', (YLeaf(YType.enumeration, 'inherit-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecState', '')])),
                        ('config_sec_state', (YLeaf(YType.enumeration, 'config-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecState', '')])),
                        ('gcc_mode', (YLeaf(YType.boolean, 'gcc-mode'), ['bool'])),
                        ('q', (YLeaf(YType.uint64, 'q'), ['int'])),
                        ('q_margin', (YLeaf(YType.uint64, 'q-margin'), ['int'])),
                        ('performance_monitoring', (YLeaf(YType.enumeration, 'performance-monitoring'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPerMon', '')])),
                        ('ec', (YLeaf(YType.uint64, 'ec'), ['int'])),
                        ('uc', (YLeaf(YType.uint64, 'uc'), ['int'])),
                        ('pre_fec_val', (YLeaf(YType.int32, 'pre-fec-val'), ['int'])),
                        ('pre_fec_mantissa', (YLeaf(YType.int8, 'pre-fec-mantissa'), ['int'])),
                        ('ec_value', (YLeaf(YType.boolean, 'ec-value'), ['bool'])),
                        ('uc_value', (YLeaf(YType.boolean, 'uc-value'), ['bool'])),
                        ('pre_fec_ber_value', (YLeaf(YType.boolean, 'pre-fec-ber-value'), ['bool'])),
                        ('pre_fec_ber_mantissa', (YLeaf(YType.boolean, 'pre-fec-ber-mantissa'), ['bool'])),
                        ('nv_optical_support', (YLeaf(YType.boolean, 'nv-optical-support'), ['bool'])),
                        ('gmpls_tti_mode', (YLeaf(YType.enumeration, 'gmpls-tti-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'GmplsOtuTtiMode', '')])),
                        ('gmpls_tvm_id', (YLeaf(YType.uint8, 'gmpls-tvm-id'), ['int'])),
                        ('auto_tti_flag', (YLeaf(YType.boolean, 'auto-tti-flag'), ['bool'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.state = None
                    self.name = None
                    self.sf = None
                    self.sd = None
                    self.loopback_mode = None
                    self.fec_mode = None
                    self.derivedstate_mode = None
                    self.inherit_sec_state = None
                    self.config_sec_state = None
                    self.gcc_mode = None
                    self.q = None
                    self.q_margin = None
                    self.performance_monitoring = None
                    self.ec = None
                    self.uc = None
                    self.pre_fec_val = None
                    self.pre_fec_mantissa = None
                    self.ec_value = None
                    self.uc_value = None
                    self.pre_fec_ber_value = None
                    self.pre_fec_ber_mantissa = None
                    self.nv_optical_support = None
                    self.gmpls_tti_mode = None
                    self.gmpls_tvm_id = None
                    self.auto_tti_flag = None
                    self.description = None

                    self.local = Otu.Controllers.Controller.Info.Local()
                    self.local.parent = self
                    self._children_name_map["local"] = "local"

                    self.remote = Otu.Controllers.Controller.Info.Remote()
                    self.remote.parent = self
                    self._children_name_map["remote"] = "remote"

                    self.tti_mode = Otu.Controllers.Controller.Info.TtiMode()
                    self.tti_mode.parent = self
                    self._children_name_map["tti_mode"] = "tti-mode"

                    self.network_srlg = Otu.Controllers.Controller.Info.NetworkSrlg()
                    self.network_srlg.parent = self
                    self._children_name_map["network_srlg"] = "network-srlg"

                    self.otu_alarm_info = Otu.Controllers.Controller.Info.OtuAlarmInfo()
                    self.otu_alarm_info.parent = self
                    self._children_name_map["otu_alarm_info"] = "otu-alarm-info"

                    self.proactive = Otu.Controllers.Controller.Info.Proactive()
                    self.proactive.parent = self
                    self._children_name_map["proactive"] = "proactive"

                    self.otu_fec_satistics = Otu.Controllers.Controller.Info.OtuFecSatistics()
                    self.otu_fec_satistics.parent = self
                    self._children_name_map["otu_fec_satistics"] = "otu-fec-satistics"

                    self.ains_info = Otu.Controllers.Controller.Info.AinsInfo()
                    self.ains_info.parent = self
                    self._children_name_map["ains_info"] = "ains-info"
                    self._segment_path = lambda: "info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Otu.Controllers.Controller.Info, ['state', 'name', 'sf', 'sd', 'loopback_mode', 'fec_mode', 'derivedstate_mode', 'inherit_sec_state', 'config_sec_state', 'gcc_mode', 'q', 'q_margin', 'performance_monitoring', 'ec', 'uc', 'pre_fec_val', 'pre_fec_mantissa', 'ec_value', 'uc_value', 'pre_fec_ber_value', 'pre_fec_ber_mantissa', 'nv_optical_support', 'gmpls_tti_mode', 'gmpls_tvm_id', 'auto_tti_flag', 'description'], name, value)


                class Local(_Entity_):
                    """
                    TTI
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.Local, self).__init__()

                        self.yang_name = "local"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "local"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Local, ['router_id', 'if_index'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Local']['meta_info']


                class Remote(_Entity_):
                    """
                    Remote
                    
                    .. attribute:: router_id
                    
                    	Router ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.Remote, self).__init__()

                        self.yang_name = "remote"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                        ])
                        self.router_id = None
                        self.if_index = None
                        self._segment_path = lambda: "remote"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Remote, ['router_id', 'if_index'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Remote']['meta_info']


                class TtiMode(_Entity_):
                    """
                    OTU TTI
                    
                    .. attribute:: tx
                    
                    	String Sent
                    	**type**\:  :py:class:`Tx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx>`
                    
                    	**config**\: False
                    
                    .. attribute:: exp
                    
                    	String Expected
                    	**type**\:  :py:class:`Exp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp>`
                    
                    	**config**\: False
                    
                    .. attribute:: rec
                    
                    	String Received
                    	**type**\:  :py:class:`Rec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_sent_mode
                    
                    	G709TTI sent
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_exp_mode
                    
                    	G709TTI Expected
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: g709tti_rec_mode
                    
                    	G709TTI Recieved
                    	**type**\:  :py:class:`OtuTtiEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuTtiEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: remote_interface
                    
                    	Remote Interface Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_host_name
                    
                    	Remote host name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_ip_addr
                    
                    	Remote host ip
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.TtiMode, self).__init__()

                        self.yang_name = "tti-mode"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tx", ("tx", Otu.Controllers.Controller.Info.TtiMode.Tx)), ("exp", ("exp", Otu.Controllers.Controller.Info.TtiMode.Exp)), ("rec", ("rec", Otu.Controllers.Controller.Info.TtiMode.Rec))])
                        self._leafs = OrderedDict([
                            ('g709tti_sent_mode', (YLeaf(YType.enumeration, 'g709tti-sent-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEt', '')])),
                            ('g709tti_exp_mode', (YLeaf(YType.enumeration, 'g709tti-exp-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEt', '')])),
                            ('g709tti_rec_mode', (YLeaf(YType.enumeration, 'g709tti-rec-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEt', '')])),
                            ('remote_interface', (YLeaf(YType.str, 'remote-interface'), ['str'])),
                            ('remote_host_name', (YLeaf(YType.str, 'remote-host-name'), ['str'])),
                            ('remote_ip_addr', (YLeaf(YType.str, 'remote-ip-addr'), ['str'])),
                        ])
                        self.g709tti_sent_mode = None
                        self.g709tti_exp_mode = None
                        self.g709tti_rec_mode = None
                        self.remote_interface = None
                        self.remote_host_name = None
                        self.remote_ip_addr = None

                        self.tx = Otu.Controllers.Controller.Info.TtiMode.Tx()
                        self.tx.parent = self
                        self._children_name_map["tx"] = "tx"

                        self.exp = Otu.Controllers.Controller.Info.TtiMode.Exp()
                        self.exp.parent = self
                        self._children_name_map["exp"] = "exp"

                        self.rec = Otu.Controllers.Controller.Info.TtiMode.Rec()
                        self.rec.parent = self
                        self._children_name_map["rec"] = "rec"
                        self._segment_path = lambda: "tti-mode"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode, ['g709tti_sent_mode', 'g709tti_exp_mode', 'g709tti_rec_mode', 'remote_interface', 'remote_host_name', 'remote_ip_addr'], name, value)


                    class Tx(_Entity_):
                        """
                        String Sent
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of  		 :py:class:`Sapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx.Sapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of  		 :py:class:`Dapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx.Dapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of  		 :py:class:`OperatorSpecific <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Tx.OperatorSpecific>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.TtiMode.Tx, self).__init__()

                            self.yang_name = "tx"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sapi", ("sapi", Otu.Controllers.Controller.Info.TtiMode.Tx.Sapi)), ("dapi", ("dapi", Otu.Controllers.Controller.Info.TtiMode.Tx.Dapi)), ("operator-specific", ("operator_specific", Otu.Controllers.Controller.Info.TtiMode.Tx.OperatorSpecific))])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', (YLeaf(YType.str, 'full-tti-ascii-string'), ['str'])),
                            ])
                            self.full_tti_ascii_string = None

                            self.sapi = YList(self)
                            self.dapi = YList(self)
                            self.operator_specific = YList(self)
                            self._segment_path = lambda: "tx"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Tx, ['full_tti_ascii_string'], name, value)


                        class Sapi(_Entity_):
                            """
                            tx String 
                            
                            .. attribute:: entry
                            
                            	tx String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Tx.Sapi, self).__init__()

                                self.yang_name = "sapi"
                                self.yang_parent_name = "tx"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "sapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Tx.Sapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx.Sapi']['meta_info']


                        class Dapi(_Entity_):
                            """
                            exp String 
                            
                            .. attribute:: entry
                            
                            	exp String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Tx.Dapi, self).__init__()

                                self.yang_name = "dapi"
                                self.yang_parent_name = "tx"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "dapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Tx.Dapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx.Dapi']['meta_info']


                        class OperatorSpecific(_Entity_):
                            """
                            rec String 
                            
                            .. attribute:: entry
                            
                            	rec String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Tx.OperatorSpecific, self).__init__()

                                self.yang_name = "operator-specific"
                                self.yang_parent_name = "tx"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "operator-specific"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Tx.OperatorSpecific, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx.OperatorSpecific']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx']['meta_info']


                    class Exp(_Entity_):
                        """
                        String Expected
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of  		 :py:class:`Sapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp.Sapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of  		 :py:class:`Dapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp.Dapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of  		 :py:class:`OperatorSpecific <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Exp.OperatorSpecific>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.TtiMode.Exp, self).__init__()

                            self.yang_name = "exp"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sapi", ("sapi", Otu.Controllers.Controller.Info.TtiMode.Exp.Sapi)), ("dapi", ("dapi", Otu.Controllers.Controller.Info.TtiMode.Exp.Dapi)), ("operator-specific", ("operator_specific", Otu.Controllers.Controller.Info.TtiMode.Exp.OperatorSpecific))])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', (YLeaf(YType.str, 'full-tti-ascii-string'), ['str'])),
                            ])
                            self.full_tti_ascii_string = None

                            self.sapi = YList(self)
                            self.dapi = YList(self)
                            self.operator_specific = YList(self)
                            self._segment_path = lambda: "exp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Exp, ['full_tti_ascii_string'], name, value)


                        class Sapi(_Entity_):
                            """
                            tx String 
                            
                            .. attribute:: entry
                            
                            	tx String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Exp.Sapi, self).__init__()

                                self.yang_name = "sapi"
                                self.yang_parent_name = "exp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "sapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Exp.Sapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp.Sapi']['meta_info']


                        class Dapi(_Entity_):
                            """
                            exp String 
                            
                            .. attribute:: entry
                            
                            	exp String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Exp.Dapi, self).__init__()

                                self.yang_name = "dapi"
                                self.yang_parent_name = "exp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "dapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Exp.Dapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp.Dapi']['meta_info']


                        class OperatorSpecific(_Entity_):
                            """
                            rec String 
                            
                            .. attribute:: entry
                            
                            	rec String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Exp.OperatorSpecific, self).__init__()

                                self.yang_name = "operator-specific"
                                self.yang_parent_name = "exp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "operator-specific"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Exp.OperatorSpecific, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp.OperatorSpecific']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp']['meta_info']


                    class Rec(_Entity_):
                        """
                        String Received
                        
                        .. attribute:: full_tti_ascii_string
                        
                        	full tti ascii String 
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sapi
                        
                        	tx String 
                        	**type**\: list of  		 :py:class:`Sapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec.Sapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: dapi
                        
                        	exp String 
                        	**type**\: list of  		 :py:class:`Dapi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec.Dapi>`
                        
                        	**config**\: False
                        
                        .. attribute:: operator_specific
                        
                        	rec String 
                        	**type**\: list of  		 :py:class:`OperatorSpecific <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.TtiMode.Rec.OperatorSpecific>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.TtiMode.Rec, self).__init__()

                            self.yang_name = "rec"
                            self.yang_parent_name = "tti-mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sapi", ("sapi", Otu.Controllers.Controller.Info.TtiMode.Rec.Sapi)), ("dapi", ("dapi", Otu.Controllers.Controller.Info.TtiMode.Rec.Dapi)), ("operator-specific", ("operator_specific", Otu.Controllers.Controller.Info.TtiMode.Rec.OperatorSpecific))])
                            self._leafs = OrderedDict([
                                ('full_tti_ascii_string', (YLeaf(YType.str, 'full-tti-ascii-string'), ['str'])),
                            ])
                            self.full_tti_ascii_string = None

                            self.sapi = YList(self)
                            self.dapi = YList(self)
                            self.operator_specific = YList(self)
                            self._segment_path = lambda: "rec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Rec, ['full_tti_ascii_string'], name, value)


                        class Sapi(_Entity_):
                            """
                            tx String 
                            
                            .. attribute:: entry
                            
                            	tx String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Rec.Sapi, self).__init__()

                                self.yang_name = "sapi"
                                self.yang_parent_name = "rec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "sapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Rec.Sapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec.Sapi']['meta_info']


                        class Dapi(_Entity_):
                            """
                            exp String 
                            
                            .. attribute:: entry
                            
                            	exp String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Rec.Dapi, self).__init__()

                                self.yang_name = "dapi"
                                self.yang_parent_name = "rec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "dapi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Rec.Dapi, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec.Dapi']['meta_info']


                        class OperatorSpecific(_Entity_):
                            """
                            rec String 
                            
                            .. attribute:: entry
                            
                            	rec String 
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.TtiMode.Rec.OperatorSpecific, self).__init__()

                                self.yang_name = "operator-specific"
                                self.yang_parent_name = "rec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint8, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "operator-specific"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.TtiMode.Rec.OperatorSpecific, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec.OperatorSpecific']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']


                class NetworkSrlg(_Entity_):
                    """
                    Network Shared Risk Link Group information
                    
                    .. attribute:: srlg_info
                    
                    	Array of Network Shared Risk Link Group information
                    	**type**\: list of  		 :py:class:`SrlgInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.NetworkSrlg, self).__init__()

                        self.yang_name = "network-srlg"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("srlg-info", ("srlg_info", Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo))])
                        self._leafs = OrderedDict()

                        self.srlg_info = YList(self)
                        self._segment_path = lambda: "network-srlg"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.NetworkSrlg, [], name, value)


                    class SrlgInfo(_Entity_):
                        """
                        Array of Network Shared Risk Link Group
                        information
                        
                        .. attribute:: set_id
                        
                        	Array to maintain set id number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: srlg
                        
                        	Shared Risk Link Group information expressed in  integer format
                        	**type**\: list of  		 :py:class:`Srlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo.Srlg>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, self).__init__()

                            self.yang_name = "srlg-info"
                            self.yang_parent_name = "network-srlg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("srlg", ("srlg", Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo.Srlg))])
                            self._leafs = OrderedDict([
                                ('set_id', (YLeaf(YType.uint32, 'set-id'), ['int'])),
                            ])
                            self.set_id = None

                            self.srlg = YList(self)
                            self._segment_path = lambda: "srlg-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo, ['set_id'], name, value)


                        class Srlg(_Entity_):
                            """
                            Shared Risk Link Group information expressed in
                            
                            integer format
                            
                            .. attribute:: entry
                            
                            	Shared Risk Link Group information expressed in  integer format
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'controller-otu-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo.Srlg, self).__init__()

                                self.yang_name = "srlg"
                                self.yang_parent_name = "srlg-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', (YLeaf(YType.uint32, 'entry'), ['int'])),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "srlg"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo.Srlg, ['entry'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                                return meta._meta_table['Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo.Srlg']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.NetworkSrlg.SrlgInfo']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.NetworkSrlg']['meta_info']


                class OtuAlarmInfo(_Entity_):
                    """
                    OTU layer alarm Information
                    
                    .. attribute:: los
                    
                    	Loss of Signal
                    	**type**\:  :py:class:`Los <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Los>`
                    
                    	**config**\: False
                    
                    .. attribute:: lof
                    
                    	Loss of Frame
                    	**type**\:  :py:class:`Lof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof>`
                    
                    	**config**\: False
                    
                    .. attribute:: lom
                    
                    	Loss of MultiFrame
                    	**type**\:  :py:class:`Lom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom>`
                    
                    	**config**\: False
                    
                    .. attribute:: oof
                    
                    	Out of Frame
                    	**type**\:  :py:class:`Oof <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof>`
                    
                    	**config**\: False
                    
                    .. attribute:: oom
                    
                    	Out of MultiFrame
                    	**type**\:  :py:class:`Oom <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom>`
                    
                    	**config**\: False
                    
                    .. attribute:: ais
                    
                    	Alarm Indication Signal
                    	**type**\:  :py:class:`Ais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais>`
                    
                    	**config**\: False
                    
                    .. attribute:: iae
                    
                    	Incoming Alignment Error
                    	**type**\:  :py:class:`Iae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae>`
                    
                    	**config**\: False
                    
                    .. attribute:: biae
                    
                    	Backward Incoming Alignment Error
                    	**type**\:  :py:class:`Biae <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae>`
                    
                    	**config**\: False
                    
                    .. attribute:: bdi
                    
                    	Backward Defect Indication
                    	**type**\:  :py:class:`Bdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi>`
                    
                    	**config**\: False
                    
                    .. attribute:: tim
                    
                    	Trace Identifier Mismatch
                    	**type**\:  :py:class:`Tim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim>`
                    
                    	**config**\: False
                    
                    .. attribute:: eoc
                    
                    	GCC End of Channel
                    	**type**\:  :py:class:`Eoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc>`
                    
                    	**config**\: False
                    
                    .. attribute:: fec_mismatch
                    
                    	FEC mismatch alarm
                    	**type**\:  :py:class:`FecMismatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch>`
                    
                    	**config**\: False
                    
                    .. attribute:: sf_ber
                    
                    	SF BER alarm
                    	**type**\:  :py:class:`SfBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: sd_ber
                    
                    	SD BER alarm
                    	**type**\:  :py:class:`SdBer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer>`
                    
                    	**config**\: False
                    
                    .. attribute:: ec
                    
                    	EC alarm
                    	**type**\:  :py:class:`Ec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec>`
                    
                    	**config**\: False
                    
                    .. attribute:: uc
                    
                    	UC alarm
                    	**type**\:  :py:class:`Uc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc>`
                    
                    	**config**\: False
                    
                    .. attribute:: fecunc
                    
                    	FEC UnCorrected Word
                    	**type**\:  :py:class:`Fecunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.OtuAlarmInfo, self).__init__()

                        self.yang_name = "otu-alarm-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("los", ("los", Otu.Controllers.Controller.Info.OtuAlarmInfo.Los)), ("lof", ("lof", Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof)), ("lom", ("lom", Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom)), ("oof", ("oof", Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof)), ("oom", ("oom", Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom)), ("ais", ("ais", Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais)), ("iae", ("iae", Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae)), ("biae", ("biae", Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae)), ("bdi", ("bdi", Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi)), ("tim", ("tim", Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim)), ("eoc", ("eoc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc)), ("fec-mismatch", ("fec_mismatch", Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch)), ("sf-ber", ("sf_ber", Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer)), ("sd-ber", ("sd_ber", Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer)), ("ec", ("ec", Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec)), ("uc", ("uc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc)), ("fecunc", ("fecunc", Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc))])
                        self._leafs = OrderedDict()

                        self.los = Otu.Controllers.Controller.Info.OtuAlarmInfo.Los()
                        self.los.parent = self
                        self._children_name_map["los"] = "los"

                        self.lof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof()
                        self.lof.parent = self
                        self._children_name_map["lof"] = "lof"

                        self.lom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom()
                        self.lom.parent = self
                        self._children_name_map["lom"] = "lom"

                        self.oof = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof()
                        self.oof.parent = self
                        self._children_name_map["oof"] = "oof"

                        self.oom = Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom()
                        self.oom.parent = self
                        self._children_name_map["oom"] = "oom"

                        self.ais = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais()
                        self.ais.parent = self
                        self._children_name_map["ais"] = "ais"

                        self.iae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae()
                        self.iae.parent = self
                        self._children_name_map["iae"] = "iae"

                        self.biae = Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae()
                        self.biae.parent = self
                        self._children_name_map["biae"] = "biae"

                        self.bdi = Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi()
                        self.bdi.parent = self
                        self._children_name_map["bdi"] = "bdi"

                        self.tim = Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim()
                        self.tim.parent = self
                        self._children_name_map["tim"] = "tim"

                        self.eoc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc()
                        self.eoc.parent = self
                        self._children_name_map["eoc"] = "eoc"

                        self.fec_mismatch = Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch()
                        self.fec_mismatch.parent = self
                        self._children_name_map["fec_mismatch"] = "fec-mismatch"

                        self.sf_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer()
                        self.sf_ber.parent = self
                        self._children_name_map["sf_ber"] = "sf-ber"

                        self.sd_ber = Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer()
                        self.sd_ber.parent = self
                        self._children_name_map["sd_ber"] = "sd-ber"

                        self.ec = Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec()
                        self.ec.parent = self
                        self._children_name_map["ec"] = "ec"

                        self.uc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc()
                        self.uc.parent = self
                        self._children_name_map["uc"] = "uc"

                        self.fecunc = Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc()
                        self.fecunc.parent = self
                        self._children_name_map["fecunc"] = "fecunc"
                        self._segment_path = lambda: "otu-alarm-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo, [], name, value)


                    class Los(_Entity_):
                        """
                        Loss of Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, self).__init__()

                            self.yang_name = "los"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "los"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Los, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Los']['meta_info']


                    class Lof(_Entity_):
                        """
                        Loss of Frame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, self).__init__()

                            self.yang_name = "lof"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "lof"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof']['meta_info']


                    class Lom(_Entity_):
                        """
                        Loss of MultiFrame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, self).__init__()

                            self.yang_name = "lom"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "lom"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom']['meta_info']


                    class Oof(_Entity_):
                        """
                        Out of Frame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, self).__init__()

                            self.yang_name = "oof"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "oof"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof']['meta_info']


                    class Oom(_Entity_):
                        """
                        Out of MultiFrame
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, self).__init__()

                            self.yang_name = "oom"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "oom"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom']['meta_info']


                    class Ais(_Entity_):
                        """
                        Alarm Indication Signal
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, self).__init__()

                            self.yang_name = "ais"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ais"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais']['meta_info']


                    class Iae(_Entity_):
                        """
                        Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, self).__init__()

                            self.yang_name = "iae"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "iae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae']['meta_info']


                    class Biae(_Entity_):
                        """
                        Backward Incoming Alignment Error
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, self).__init__()

                            self.yang_name = "biae"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "biae"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae']['meta_info']


                    class Bdi(_Entity_):
                        """
                        Backward Defect Indication
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, self).__init__()

                            self.yang_name = "bdi"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "bdi"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi']['meta_info']


                    class Tim(_Entity_):
                        """
                        Trace Identifier Mismatch
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, self).__init__()

                            self.yang_name = "tim"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "tim"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim']['meta_info']


                    class Eoc(_Entity_):
                        """
                        GCC End of Channel
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, self).__init__()

                            self.yang_name = "eoc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "eoc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc']['meta_info']


                    class FecMismatch(_Entity_):
                        """
                        FEC mismatch alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, self).__init__()

                            self.yang_name = "fec-mismatch"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "fec-mismatch"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch']['meta_info']


                    class SfBer(_Entity_):
                        """
                        SF BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, self).__init__()

                            self.yang_name = "sf-ber"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sf-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer']['meta_info']


                    class SdBer(_Entity_):
                        """
                        SD BER alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, self).__init__()

                            self.yang_name = "sd-ber"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "sd-ber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer']['meta_info']


                    class Ec(_Entity_):
                        """
                        EC alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, self).__init__()

                            self.yang_name = "ec"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "ec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec']['meta_info']


                    class Uc(_Entity_):
                        """
                        UC alarm
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, self).__init__()

                            self.yang_name = "uc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "uc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc']['meta_info']


                    class Fecunc(_Entity_):
                        """
                        FEC UnCorrected Word
                        
                        .. attribute:: reporting_enabled
                        
                        	Is reporting enabled?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_detected
                        
                        	Is defect detected?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_asserted
                        
                        	Is defect delared?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: counter
                        
                        	Alarm counter
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'controller-otu-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, self).__init__()

                            self.yang_name = "fecunc"
                            self.yang_parent_name = "otu-alarm-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reporting_enabled', (YLeaf(YType.boolean, 'reporting-enabled'), ['bool'])),
                                ('is_detected', (YLeaf(YType.boolean, 'is-detected'), ['bool'])),
                                ('is_asserted', (YLeaf(YType.boolean, 'is-asserted'), ['bool'])),
                                ('counter', (YLeaf(YType.uint64, 'counter'), ['int'])),
                            ])
                            self.reporting_enabled = None
                            self.is_detected = None
                            self.is_asserted = None
                            self.counter = None
                            self._segment_path = lambda: "fecunc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc, ['reporting_enabled', 'is_detected', 'is_asserted', 'counter'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                            return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']


                class Proactive(_Entity_):
                    """
                    Proactive Protection
                    
                    .. attribute:: proactive_status
                    
                    	Proactive Status
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: inherit_sec_state
                    
                    	Secondary Admin State
                    	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    	**config**\: False
                    
                    .. attribute:: config_sec_state
                    
                    	Sec State
                    	**type**\:  :py:class:`OtuSecState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuSecState>`
                    
                    	**config**\: False
                    
                    .. attribute:: proactive_fsm_state
                    
                    	Proactive FSM State
                    	**type**\:  :py:class:`OtuPpFsmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpFsmState>`
                    
                    	**config**\: False
                    
                    .. attribute:: proactive_fsm_if_state
                    
                    	Proactive FSM IF State
                    	**type**\:  :py:class:`OtuPpIntfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuPpIntfState>`
                    
                    	**config**\: False
                    
                    .. attribute:: trig_thresh_coeff
                    
                    	Trigger threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: trig_thresh_power
                    
                    	Trigger threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: rvrt_thresh_coeff
                    
                    	Revert threshold coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: rvrt_thresh_power
                    
                    	Revert threshold power
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: trigger_window
                    
                    	Trigger Integration window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: revert_window
                    
                    	Revert Integration Window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.Proactive, self).__init__()

                        self.yang_name = "proactive"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('proactive_status', (YLeaf(YType.boolean, 'proactive-status'), ['bool'])),
                            ('inherit_sec_state', (YLeaf(YType.enumeration, 'inherit-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecState', '')])),
                            ('config_sec_state', (YLeaf(YType.enumeration, 'config-sec-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecState', '')])),
                            ('proactive_fsm_state', (YLeaf(YType.enumeration, 'proactive-fsm-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPpFsmState', '')])),
                            ('proactive_fsm_if_state', (YLeaf(YType.enumeration, 'proactive-fsm-if-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPpIntfState', '')])),
                            ('trig_thresh_coeff', (YLeaf(YType.uint8, 'trig-thresh-coeff'), ['int'])),
                            ('trig_thresh_power', (YLeaf(YType.uint8, 'trig-thresh-power'), ['int'])),
                            ('rvrt_thresh_coeff', (YLeaf(YType.uint8, 'rvrt-thresh-coeff'), ['int'])),
                            ('rvrt_thresh_power', (YLeaf(YType.uint8, 'rvrt-thresh-power'), ['int'])),
                            ('trigger_window', (YLeaf(YType.uint32, 'trigger-window'), ['int'])),
                            ('revert_window', (YLeaf(YType.uint32, 'revert-window'), ['int'])),
                        ])
                        self.proactive_status = None
                        self.inherit_sec_state = None
                        self.config_sec_state = None
                        self.proactive_fsm_state = None
                        self.proactive_fsm_if_state = None
                        self.trig_thresh_coeff = None
                        self.trig_thresh_power = None
                        self.rvrt_thresh_coeff = None
                        self.rvrt_thresh_power = None
                        self.trigger_window = None
                        self.revert_window = None
                        self._segment_path = lambda: "proactive"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.Proactive, ['proactive_status', 'inherit_sec_state', 'config_sec_state', 'proactive_fsm_state', 'proactive_fsm_if_state', 'trig_thresh_coeff', 'trig_thresh_power', 'rvrt_thresh_coeff', 'rvrt_thresh_power', 'trigger_window', 'revert_window'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.Proactive']['meta_info']


                class OtuFecSatistics(_Entity_):
                    """
                    OTU FEC Statistics
                    
                    .. attribute:: post_fec_ber
                    
                    	Bit Error Rate After Forward Error Correction
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: pre_fec_ber
                    
                    	Bit Error Rate Before Forward Error Correction
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.OtuFecSatistics, self).__init__()

                        self.yang_name = "otu-fec-satistics"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('post_fec_ber', (YLeaf(YType.str, 'post-fec-ber'), ['str'])),
                            ('pre_fec_ber', (YLeaf(YType.str, 'pre-fec-ber'), ['str'])),
                        ])
                        self.post_fec_ber = None
                        self.pre_fec_ber = None
                        self._segment_path = lambda: "otu-fec-satistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.OtuFecSatistics, ['post_fec_ber', 'pre_fec_ber'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.OtuFecSatistics']['meta_info']


                class AinsInfo(_Entity_):
                    """
                    AINS information
                    
                    .. attribute:: ains_state
                    
                    	AINS State
                    	**type**\:  :py:class:`OtuAinsStateEt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper.OtuAinsStateEt>`
                    
                    	**config**\: False
                    
                    .. attribute:: ains_timer_minutes
                    
                    	AINS Timer in Minutes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: minute
                    
                    .. attribute:: ains_remaining_secs
                    
                    	AINS Remaining Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'controller-otu-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Otu.Controllers.Controller.Info.AinsInfo, self).__init__()

                        self.yang_name = "ains-info"
                        self.yang_parent_name = "info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ains_state', (YLeaf(YType.enumeration, 'ains-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuAinsStateEt', '')])),
                            ('ains_timer_minutes', (YLeaf(YType.uint32, 'ains-timer-minutes'), ['int'])),
                            ('ains_remaining_secs', (YLeaf(YType.uint32, 'ains-remaining-secs'), ['int'])),
                        ])
                        self.ains_state = None
                        self.ains_timer_minutes = None
                        self.ains_remaining_secs = None
                        self._segment_path = lambda: "ains-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Otu.Controllers.Controller.Info.AinsInfo, ['ains_state', 'ains_timer_minutes', 'ains_remaining_secs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                        return meta._meta_table['Otu.Controllers.Controller.Info.AinsInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                    return meta._meta_table['Otu.Controllers.Controller.Info']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
                return meta._meta_table['Otu.Controllers.Controller']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
            return meta._meta_table['Otu.Controllers']['meta_info']

    def clone_ptr(self):
        self._top_entity = Otu()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_oper as meta
        return meta._meta_table['Otu']['meta_info']



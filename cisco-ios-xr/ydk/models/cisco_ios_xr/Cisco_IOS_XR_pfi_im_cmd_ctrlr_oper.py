""" Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfi\-im\-cmd\-ctrlr package operational data.

This module contains definitions
for the following management objects\:
  controllers\: Controller operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ImStateEnum(Enum):
    """
    ImStateEnum (Enum Class)

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")



class Controllers(Entity):
    """
    Controller operational data
    
    .. attribute:: controllers
    
    	Descriptions for controllers
    	**type**\:  :py:class:`Controllers_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper.Controllers.Controllers_>`
    
    

    """

    _prefix = 'pfi-im-cmd-ctrlr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Controllers, self).__init__()
        self._top_entity = None

        self.yang_name = "controllers"
        self.yang_parent_name = "Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controllers", ("controllers", Controllers.Controllers_))])
        self._leafs = OrderedDict()

        self.controllers = Controllers.Controllers_()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._segment_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper:controllers"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Controllers, [], name, value)


    class Controllers_(Entity):
        """
        Descriptions for controllers
        
        .. attribute:: controller
        
        	Description for a particular controller
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper.Controllers.Controllers_.Controller>`
        
        

        """

        _prefix = 'pfi-im-cmd-ctrlr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Controllers.Controllers_, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "controllers"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("controller", ("controller", Controllers.Controllers_.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper:controllers/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Controllers.Controllers_, [], name, value)


        class Controller(Entity):
            """
            Description for a particular controller
            
            .. attribute:: interafce_name  (key)
            
            	The name of the controller
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: controller
            
            	Controller
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper.ImStateEnum>`
            
            .. attribute:: description
            
            	Controller description string
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-ctrlr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Controllers.Controllers_.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interafce_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interafce_name', (YLeaf(YType.str, 'interafce-name'), ['str'])),
                    ('controller', (YLeaf(YType.str, 'controller'), ['str'])),
                    ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_pfi_im_cmd_ctrlr_oper', 'ImStateEnum', '')])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.interafce_name = None
                self.controller = None
                self.state = None
                self.description = None
                self._segment_path = lambda: "controller" + "[interafce-name='" + str(self.interafce_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pfi-im-cmd-ctrlr-oper:controllers/controllers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Controllers.Controllers_.Controller, ['interafce_name', u'controller', u'state', u'description'], name, value)

    def clone_ptr(self):
        self._top_entity = Controllers()
        return self._top_entity


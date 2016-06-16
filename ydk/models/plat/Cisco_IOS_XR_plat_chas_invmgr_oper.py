""" Cisco_IOS_XR_plat_chas_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR plat\-chas\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  platform\: Platform information
  platform\-inventory\: platform inventory

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CardRedundancyStateEnum(Enum):
    """
    CardRedundancyStateEnum

    Redundancy state detail

    .. data:: ACTIVE = 1

    	Active

    .. data:: STANDBY = 2

    	Standby

    """

    ACTIVE = 1

    STANDBY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['CardRedundancyStateEnum']


class InvAdminStateEnum(Enum):
    """
    InvAdminStateEnum

    Inv admin state

    .. data:: ADMIN_STATE_INVALID = 0

    	admin state invalid

    .. data:: ADMIN_UP = 1

    	admin up

    .. data:: ADMIN_DOWN = 2

    	admin down

    """

    ADMIN_STATE_INVALID = 0

    ADMIN_UP = 1

    ADMIN_DOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['InvAdminStateEnum']


class InvCardStateEnum(Enum):
    """
    InvCardStateEnum

    Inv card state

    .. data:: INV_CARD_NOT_PRESENT = 0

    	inv card not present

    .. data:: INV_CARD_PRESENT = 1

    	inv card present

    .. data:: INV_CARD_RESET = 2

    	inv card reset

    .. data:: INV_CARD_BOOTING = 3

    	inv card booting

    .. data:: INV_CARD_MBI_BOOTING = 4

    	inv card mbi booting

    .. data:: INV_CARD_RUNNING_MBI = 5

    	inv card running mbi

    .. data:: INV_CARD_RUNNING_ENA = 6

    	inv card running ena

    .. data:: INV_CARD_BRING_DOWN = 7

    	inv card bring down

    .. data:: INV_CARD_ENA_FAILURE = 8

    	inv card ena failure

    .. data:: INV_CARD_F_DIAG_RUN = 9

    	inv card f diag run

    .. data:: INV_CARD_F_DIAG_FAILURE = 10

    	inv card f diag failure

    .. data:: INV_CARD_POWERED = 11

    	inv card powered

    .. data:: INV_CARD_UNPOWERED = 12

    	inv card unpowered

    .. data:: INV_CARD_MDR = 13

    	inv card mdr

    .. data:: INV_CARD_MDR_RUNNING_MBI = 14

    	inv card mdr running mbi

    .. data:: INV_CARD_MAIN_T_MODE = 15

    	inv card main t mode

    .. data:: INV_CARD_ADMIN_DOWN = 16

    	inv card admin down

    .. data:: INV_CARD_NO_MON = 17

    	inv card no mon

    .. data:: INV_CARD_UNKNOWN = 18

    	inv card unknown

    .. data:: INV_CARD_FAILED = 19

    	inv card failed

    .. data:: INV_CARD_OK = 20

    	inv card ok

    .. data:: INV_CARD_MISSING = 21

    	inv card missing

    .. data:: INV_CARD_FIELD_DIAG_DOWNLOADING = 22

    	inv card field diag downloading

    .. data:: INV_CARD_FIELD_DIAG_UNMONITOR = 23

    	inv card field diag unmonitor

    .. data:: INV_CARD_FABRIC_FIELD_DIAG_UNMONITOR = 24

    	inv card fabric field diag unmonitor

    .. data:: INV_CARD_FIELD_DIAG_RP_LAUNCHING = 25

    	inv card field diag rp launching

    .. data:: INV_CARD_FIELD_DIAG_RUNNING = 26

    	inv card field diag running

    .. data:: INV_CARD_FIELD_DIAG_PASS = 27

    	inv card field diag pass

    .. data:: INV_CARD_FIELD_DIAG_FAIL = 28

    	inv card field diag fail

    .. data:: INV_CARD_FIELD_DIAG_TIMEOUT = 29

    	inv card field diag timeout

    .. data:: INV_CARD_DISABLED = 30

    	inv card disabled

    .. data:: INV_CARD_SPA_BOOTING = 31

    	inv card spa booting

    .. data:: INV_CARD_NOT_ALLOWED_ONLINE = 32

    	inv card not allowed online

    .. data:: INV_CARD_STOPPED = 33

    	inv card stopped

    .. data:: INV_CARD_INCOMPATIBLE_FW_VER = 34

    	inv card incompatible fw ver

    .. data:: INV_CARD_FPD_HOLD = 35

    	inv card fpd hold

    .. data:: INV_CARD_NODE_PREP = 36

    	inv card node prep

    .. data:: INV_CARD_UPDATING_FPD = 37

    	inv card updating fpd

    .. data:: INV_CARD_NUM_STATES = 38

    	inv card num states

    """

    INV_CARD_NOT_PRESENT = 0

    INV_CARD_PRESENT = 1

    INV_CARD_RESET = 2

    INV_CARD_BOOTING = 3

    INV_CARD_MBI_BOOTING = 4

    INV_CARD_RUNNING_MBI = 5

    INV_CARD_RUNNING_ENA = 6

    INV_CARD_BRING_DOWN = 7

    INV_CARD_ENA_FAILURE = 8

    INV_CARD_F_DIAG_RUN = 9

    INV_CARD_F_DIAG_FAILURE = 10

    INV_CARD_POWERED = 11

    INV_CARD_UNPOWERED = 12

    INV_CARD_MDR = 13

    INV_CARD_MDR_RUNNING_MBI = 14

    INV_CARD_MAIN_T_MODE = 15

    INV_CARD_ADMIN_DOWN = 16

    INV_CARD_NO_MON = 17

    INV_CARD_UNKNOWN = 18

    INV_CARD_FAILED = 19

    INV_CARD_OK = 20

    INV_CARD_MISSING = 21

    INV_CARD_FIELD_DIAG_DOWNLOADING = 22

    INV_CARD_FIELD_DIAG_UNMONITOR = 23

    INV_CARD_FABRIC_FIELD_DIAG_UNMONITOR = 24

    INV_CARD_FIELD_DIAG_RP_LAUNCHING = 25

    INV_CARD_FIELD_DIAG_RUNNING = 26

    INV_CARD_FIELD_DIAG_PASS = 27

    INV_CARD_FIELD_DIAG_FAIL = 28

    INV_CARD_FIELD_DIAG_TIMEOUT = 29

    INV_CARD_DISABLED = 30

    INV_CARD_SPA_BOOTING = 31

    INV_CARD_NOT_ALLOWED_ONLINE = 32

    INV_CARD_STOPPED = 33

    INV_CARD_INCOMPATIBLE_FW_VER = 34

    INV_CARD_FPD_HOLD = 35

    INV_CARD_NODE_PREP = 36

    INV_CARD_UPDATING_FPD = 37

    INV_CARD_NUM_STATES = 38


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['InvCardStateEnum']


class InvMonitorStateEnum(Enum):
    """
    InvMonitorStateEnum

    Inv monitor state

    .. data:: UNMONITORED = 0

    	unmonitored

    .. data:: MONITORED = 1

    	monitored

    """

    UNMONITORED = 0

    MONITORED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['InvMonitorStateEnum']


class InvPowerAdminStateEnum(Enum):
    """
    InvPowerAdminStateEnum

    Inv power admin state

    .. data:: ADMIN_POWER_INVALID = 0

    	admin power invalid

    .. data:: ADMIN_ON = 2

    	admin on

    .. data:: ADMIN_OFF = 3

    	admin off

    """

    ADMIN_POWER_INVALID = 0

    ADMIN_ON = 2

    ADMIN_OFF = 3


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['InvPowerAdminStateEnum']


class InvResetReasonEnum(Enum):
    """
    InvResetReasonEnum

    Inv reset reason

    .. data:: MODULE_RESET_REASON_UNKNOWN = 0

    	module reset reason unknown

    .. data:: MODULE_RESET_REASON_POWERUP = 1

    	module reset reason powerup

    .. data:: MODULE_RESET_REASON_USER_SHUTDOWN = 2

    	module reset reason user shutdown

    .. data:: MODULE_RESET_REASON_USER_RELOAD = 3

    	module reset reason user reload

    .. data:: MODULE_RESET_REASON_AUTO_RELOAD = 4

    	module reset reason auto reload

    .. data:: MODULE_RESET_REASON_ENVIRONMENT = 5

    	module reset reason environment

    .. data:: MODULE_RESET_REASON_USER_UNPOWER = 6

    	module reset reason user unpower

    """

    MODULE_RESET_REASON_UNKNOWN = 0

    MODULE_RESET_REASON_POWERUP = 1

    MODULE_RESET_REASON_USER_SHUTDOWN = 2

    MODULE_RESET_REASON_USER_RELOAD = 3

    MODULE_RESET_REASON_AUTO_RELOAD = 4

    MODULE_RESET_REASON_ENVIRONMENT = 5

    MODULE_RESET_REASON_USER_UNPOWER = 6


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['InvResetReasonEnum']


class NodeStateEnum(Enum):
    """
    NodeStateEnum

    Node state detail

    .. data:: NOT_PRESENT = 0

    	Not present

    .. data:: PRESENT = 1

    	Present

    .. data:: RESET = 2

    	Reset

    .. data:: ROMMON = 3

    	Card booting or rommon

    .. data:: MBI_BOOT = 4

    	MBI booting

    .. data:: MBI_RUN = 5

    	Running MBI

    .. data:: XR_RUN = 6

    	Running ENA

    .. data:: BRING_DOWN = 7

    	Bringdown

    .. data:: XR_FAIL = 8

    	ENA failure

    .. data:: FDIAG_RUN = 9

    	Running FDIAG

    .. data:: FDIAG_FAIL = 10

    	FDIAG failure

    .. data:: POWER = 11

    	Powered

    .. data:: UNPOWER = 12

    	Unpowered

    .. data:: MDR_WARM_RELOAD = 13

    	MDR warm reload

    .. data:: MDR_MBI_RUN = 14

    	MDR running MBI

    .. data:: MAINTENANCE_MODE = 15

    	Maintenance mode

    .. data:: ADMIN_DOWN = 16

    	Admin down

    .. data:: NOT_MONITOR = 17

    	No MON

    .. data:: UNKNOWN_CARD = 18

    	Unknown

    .. data:: FAILED = 19

    	Failed

    .. data:: OK = 20

    	OK

    .. data:: MISSING = 21

    	Missing

    .. data:: DIAG_DOWNLOAD = 22

    	Field diag downloading

    .. data:: DIAG_NOT_MONITOR = 23

    	Field diag unmonitor

    .. data:: FABRIC_DIAG_NOT_MONITOR = 24

    	Fabric field diag unmonitor

    .. data:: DIAG_RP_LAUNCH = 25

    	Field diag RP launching

    .. data:: DIAG_RUN = 26

    	Field diag running

    .. data:: DIAG_PASS = 27

    	Field diag pass

    .. data:: DIAG_FAIL = 28

    	Field diag fail

    .. data:: DIAG_TIMEOUT = 29

    	Field diag timeout

    .. data:: DISABLE = 30

    	Disable

    .. data:: SPA_BOOT = 31

    	SPA booting

    .. data:: NOT_ALLOWED_ONLINE = 32

    	Not allowed online

    .. data:: STOP = 33

    	Stopped

    .. data:: INCOMP_VERSION = 34

    	Incompatible FW version

    .. data:: FPD_HOLD = 35

    	FPD hold

    .. data:: XR_PREPARATION = 36

    	XR preparation

    .. data:: SYNC_READY = 37

    	Sync ready state

    .. data:: XR_ISOLATE = 38

    	Node isolate state

    .. data:: READY = 39

    	Ready

    .. data:: INVALID = 40

    	Invalid

    .. data:: OPERATIONAL = 41

    	Operational

    .. data:: OPERATIONAL_LOCK = 42

    	Operational lock

    .. data:: GOING_DOWN = 43

    	Going down

    .. data:: GOING_OFFLINE = 44

    	Going offline

    .. data:: GOING_ONLINE = 45

    	Going online

    .. data:: OFFLINE = 46

    	Offline

    .. data:: UP = 47

    	Up

    .. data:: DOWN = 48

    	Down

    .. data:: MAX = 49

    	Max

    .. data:: UNKNOWN = 50

    	Unknown

    """

    NOT_PRESENT = 0

    PRESENT = 1

    RESET = 2

    ROMMON = 3

    MBI_BOOT = 4

    MBI_RUN = 5

    XR_RUN = 6

    BRING_DOWN = 7

    XR_FAIL = 8

    FDIAG_RUN = 9

    FDIAG_FAIL = 10

    POWER = 11

    UNPOWER = 12

    MDR_WARM_RELOAD = 13

    MDR_MBI_RUN = 14

    MAINTENANCE_MODE = 15

    ADMIN_DOWN = 16

    NOT_MONITOR = 17

    UNKNOWN_CARD = 18

    FAILED = 19

    OK = 20

    MISSING = 21

    DIAG_DOWNLOAD = 22

    DIAG_NOT_MONITOR = 23

    FABRIC_DIAG_NOT_MONITOR = 24

    DIAG_RP_LAUNCH = 25

    DIAG_RUN = 26

    DIAG_PASS = 27

    DIAG_FAIL = 28

    DIAG_TIMEOUT = 29

    DISABLE = 30

    SPA_BOOT = 31

    NOT_ALLOWED_ONLINE = 32

    STOP = 33

    INCOMP_VERSION = 34

    FPD_HOLD = 35

    XR_PREPARATION = 36

    SYNC_READY = 37

    XR_ISOLATE = 38

    READY = 39

    INVALID = 40

    OPERATIONAL = 41

    OPERATIONAL_LOCK = 42

    GOING_DOWN = 43

    GOING_OFFLINE = 44

    GOING_ONLINE = 45

    OFFLINE = 46

    UP = 47

    DOWN = 48

    MAX = 49

    UNKNOWN = 50


    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['NodeStateEnum']



class Platform(object):
    """
    Platform information
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\: :py:class:`Racks <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks>`
    
    

    """

    _prefix = 'plat-chas-invmgr-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.racks = Platform.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of :py:class:`Rack <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack>`
        
        

        """

        _prefix = 'plat-chas-invmgr-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
            """
            Rack name
            
            .. attribute:: rack_name  <key>
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\: :py:class:`Slots <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'plat-chas-invmgr-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.rack_name = None
                self.slots = Platform.Racks.Rack.Slots()
                self.slots.parent = self


            class Slots(object):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of :py:class:`Slot <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'plat-chas-invmgr-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.slot = YList()
                    self.slot.parent = self
                    self.slot.name = 'slot'


                class Slot(object):
                    """
                    Slot name
                    
                    .. attribute:: slot_name  <key>
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: instances
                    
                    	Table of Instances
                    	**type**\: :py:class:`Instances <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot.Instances>`
                    
                    .. attribute:: state
                    
                    	State information
                    	**type**\: :py:class:`State <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot.State>`
                    
                    .. attribute:: vm
                    
                    	VM information
                    	**type**\: :py:class:`Vm <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot.Vm>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.slot_name = None
                        self.instances = Platform.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self.state = Platform.Racks.Rack.Slots.Slot.State()
                        self.state.parent = self
                        self.vm = Platform.Racks.Rack.Slots.Slot.Vm()
                        self.vm.parent = self


                    class Instances(object):
                        """
                        Table of Instances
                        
                        .. attribute:: instance
                        
                        	Instance name
                        	**type**\: list of :py:class:`Instance <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.instance = YList()
                            self.instance.parent = self
                            self.instance.name = 'instance'


                        class Instance(object):
                            """
                            Instance name
                            
                            .. attribute:: instance_name  <key>
                            
                            	Instance name
                            	**type**\: str
                            
                            .. attribute:: state
                            
                            	State information
                            	**type**\: :py:class:`State <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.Platform.Racks.Rack.Slots.Slot.Instances.Instance.State>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-oper'
                            _revision = '2015-01-07'

                            def __init__(self):
                                self.parent = None
                                self.instance_name = None
                                self.state = Platform.Racks.Rack.Slots.Slot.Instances.Instance.State()
                                self.state.parent = self


                            class State(object):
                                """
                                State information
                                
                                .. attribute:: admin_state
                                
                                	Admin state
                                	**type**\: str
                                
                                .. attribute:: card_redundancy_state
                                
                                	Redundancy state
                                	**type**\: :py:class:`CardRedundancyStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.CardRedundancyStateEnum>`
                                
                                .. attribute:: card_type
                                
                                	Card type
                                	**type**\: str
                                
                                .. attribute:: is_monitored
                                
                                	True if power state is active
                                	**type**\: bool
                                
                                .. attribute:: is_powered
                                
                                	True if monitor state is active
                                	**type**\: bool
                                
                                .. attribute:: is_shutdown
                                
                                	True if shutdown state is active
                                	**type**\: bool
                                
                                .. attribute:: plim
                                
                                	PLIM
                                	**type**\: str
                                
                                .. attribute:: state
                                
                                	State
                                	**type**\: :py:class:`NodeStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.NodeStateEnum>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.admin_state = None
                                    self.card_redundancy_state = None
                                    self.card_type = None
                                    self.is_monitored = None
                                    self.is_powered = None
                                    self.is_shutdown = None
                                    self.plim = None
                                    self.state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.admin_state is not None:
                                        return True

                                    if self.card_redundancy_state is not None:
                                        return True

                                    if self.card_type is not None:
                                        return True

                                    if self.is_monitored is not None:
                                        return True

                                    if self.is_powered is not None:
                                        return True

                                    if self.is_shutdown is not None:
                                        return True

                                    if self.plim is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.instance_name is None:
                                    raise YPYModelError('Key property instance_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:instance[Cisco-IOS-XR-plat-chas-invmgr-oper:instance-name = ' + str(self.instance_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.instance_name is not None:
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                return meta._meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:instances'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.instance is not None:
                                for child_ref in self.instance:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['Platform.Racks.Rack.Slots.Slot.Instances']['meta_info']


                    class Vm(object):
                        """
                        VM information
                        
                        .. attribute:: node_descriptiton
                        
                        	Node Type
                        	**type**\: str
                        
                        .. attribute:: node_ip
                        
                        	Node IP Address
                        	**type**\: str
                        
                        .. attribute:: partner_name
                        
                        	Partner Name
                        	**type**\: str
                        
                        .. attribute:: red_role
                        
                        	Node Redundency Role
                        	**type**\: str
                        
                        .. attribute:: software_status
                        
                        	SW status
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.node_descriptiton = None
                            self.node_ip = None
                            self.partner_name = None
                            self.red_role = None
                            self.software_status = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:vm'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.node_descriptiton is not None:
                                return True

                            if self.node_ip is not None:
                                return True

                            if self.partner_name is not None:
                                return True

                            if self.red_role is not None:
                                return True

                            if self.software_status is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['Platform.Racks.Rack.Slots.Slot.Vm']['meta_info']


                    class State(object):
                        """
                        State information
                        
                        .. attribute:: admin_state
                        
                        	Admin state
                        	**type**\: str
                        
                        .. attribute:: card_redundancy_state
                        
                        	Redundancy state
                        	**type**\: :py:class:`CardRedundancyStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.CardRedundancyStateEnum>`
                        
                        .. attribute:: card_type
                        
                        	Card type
                        	**type**\: str
                        
                        .. attribute:: is_monitored
                        
                        	True if power state is active
                        	**type**\: bool
                        
                        .. attribute:: is_powered
                        
                        	True if monitor state is active
                        	**type**\: bool
                        
                        .. attribute:: is_shutdown
                        
                        	True if shutdown state is active
                        	**type**\: bool
                        
                        .. attribute:: plim
                        
                        	PLIM
                        	**type**\: str
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\: :py:class:`NodeStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.NodeStateEnum>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.admin_state = None
                            self.card_redundancy_state = None
                            self.card_type = None
                            self.is_monitored = None
                            self.is_powered = None
                            self.is_shutdown = None
                            self.plim = None
                            self.state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.admin_state is not None:
                                return True

                            if self.card_redundancy_state is not None:
                                return True

                            if self.card_type is not None:
                                return True

                            if self.is_monitored is not None:
                                return True

                            if self.is_powered is not None:
                                return True

                            if self.is_shutdown is not None:
                                return True

                            if self.plim is not None:
                                return True

                            if self.state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['Platform.Racks.Rack.Slots.Slot.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.slot_name is None:
                            raise YPYModelError('Key property slot_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:slot[Cisco-IOS-XR-plat-chas-invmgr-oper:slot-name = ' + str(self.slot_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.slot_name is not None:
                            return True

                        if self.instances is not None and self.instances._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.vm is not None and self.vm._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                        return meta._meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:slots'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.slot is not None:
                        for child_ref in self.slot:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                    return meta._meta_table['Platform.Racks.Rack.Slots']['meta_info']

            @property
            def _common_path(self):
                if self.rack_name is None:
                    raise YPYModelError('Key property rack_name is None')

                return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform/Cisco-IOS-XR-plat-chas-invmgr-oper:racks/Cisco-IOS-XR-plat-chas-invmgr-oper:rack[Cisco-IOS-XR-plat-chas-invmgr-oper:rack-name = ' + str(self.rack_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.rack_name is not None:
                    return True

                if self.slots is not None and self.slots._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                return meta._meta_table['Platform.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform/Cisco-IOS-XR-plat-chas-invmgr-oper:racks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.rack is not None:
                for child_ref in self.rack:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
            return meta._meta_table['Platform.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['Platform']['meta_info']


class PlatformInventory(object):
    """
    platform inventory
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\: :py:class:`Racks <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks>`
    
    

    """

    _prefix = 'plat-chas-invmgr-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.racks = PlatformInventory.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of :py:class:`Rack <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack>`
        
        

        """

        _prefix = 'plat-chas-invmgr-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
            """
            Rack name
            
            .. attribute:: name  <key>
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: attributes
            
            	Attributes
            	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Attributes>`
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\: :py:class:`Slots <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'plat-chas-invmgr-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.name = None
                self.attributes = PlatformInventory.Racks.Rack.Attributes()
                self.attributes.parent = self
                self.slots = PlatformInventory.Racks.Rack.Slots()
                self.slots.parent = self


            class Slots(object):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of :py:class:`Slot <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'plat-chas-invmgr-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.slot = YList()
                    self.slot.parent = self
                    self.slot.name = 'slot'


                class Slot(object):
                    """
                    Slot name
                    
                    .. attribute:: name  <key>
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes>`
                    
                    .. attribute:: cards
                    
                    	Table of cards
                    	**type**\: :py:class:`Cards <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Attributes()
                        self.attributes.parent = self
                        self.cards = PlatformInventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self


                    class Cards(object):
                        """
                        Table of cards
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of :py:class:`Card <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.card = YList()
                            self.card.parent = self
                            self.card.name = 'card'


                        class Card(object):
                            """
                            Card number
                            
                            .. attribute:: name  <key>
                            
                            	Card name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: attributes
                            
                            	Attributes
                            	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes>`
                            
                            .. attribute:: hardware_information
                            
                            	HardwareInformationDir
                            	**type**\: :py:class:`HardwareInformation <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation>`
                            
                            .. attribute:: hw_components
                            
                            	Table of  HW components 
                            	**type**\: :py:class:`HwComponents <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents>`
                            
                            .. attribute:: port_slots
                            
                            	Table of port slots
                            	**type**\: :py:class:`PortSlots <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots>`
                            
                            .. attribute:: portses
                            
                            	Table of spirit port slots
                            	**type**\: :py:class:`Portses <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses>`
                            
                            .. attribute:: sensors
                            
                            	Table of sensors
                            	**type**\: :py:class:`Sensors <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors>`
                            
                            .. attribute:: sub_slots
                            
                            	Table of subslots
                            	**type**\: :py:class:`SubSlots <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-oper'
                            _revision = '2015-01-07'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes()
                                self.attributes.parent = self
                                self.hardware_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation()
                                self.hardware_information.parent = self
                                self.hw_components = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self.port_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self.portses = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses()
                                self.portses.parent = self
                                self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self.sub_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self


                            class Portses(object):
                                """
                                Table of spirit port slots
                                
                                .. attribute:: ports
                                
                                	Port number
                                	**type**\: list of :py:class:`Ports <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.ports = YList()
                                    self.ports.parent = self
                                    self.ports.name = 'ports'


                                class Ports(object):
                                    """
                                    Port number
                                    
                                    .. attribute:: name  <key>
                                    
                                    	Port name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.name = None
                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes()
                                        self.attributes.parent = self


                                    class Attributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo()
                                            self.fru_info.parent = self


                                        class BasicInfo(object):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.description = None
                                                self.firmware_revision = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.model_name = None
                                                self.name = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.vendor_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.description is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo']['meta_info']


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.module_administrative_state = None
                                                self.module_monitor_state = None
                                                self.module_operational_state = None
                                                self.module_power_administrative_state = None
                                                self.module_reset_reason = None
                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self


                                            class LastOperationalStateChange(object):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class ModuleUpTime(object):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.module_administrative_state is not None:
                                                    return True

                                                if self.module_monitor_state is not None:
                                                    return True

                                                if self.module_operational_state is not None:
                                                    return True

                                                if self.module_power_administrative_state is not None:
                                                    return True

                                                if self.module_reset_reason is not None:
                                                    return True

                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:ports[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.name is not None:
                                            return True

                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:portses'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.ports is not None:
                                        for child_ref in self.ports:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses']['meta_info']


                            class HardwareInformation(object):
                                """
                                HardwareInformationDir
                                
                                .. attribute:: bootflash_information
                                
                                	BootflashInformation
                                	**type**\: :py:class:`BootflashInformation <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation>`
                                
                                .. attribute:: disk_information
                                
                                	DiskInformation
                                	**type**\: :py:class:`DiskInformation <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation>`
                                
                                .. attribute:: motherboard_information
                                
                                	MotherboardInformation
                                	**type**\: :py:class:`MotherboardInformation <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation>`
                                
                                .. attribute:: processor_information
                                
                                	ProcesorInformation
                                	**type**\: :py:class:`ProcessorInformation <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.bootflash_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation()
                                    self.bootflash_information.parent = self
                                    self.disk_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation()
                                    self.disk_information.parent = self
                                    self.motherboard_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation()
                                    self.motherboard_information.parent = self
                                    self.processor_information = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation()
                                    self.processor_information.parent = self


                                class ProcessorInformation(object):
                                    """
                                    ProcesorInformation
                                    
                                    .. attribute:: processor_type
                                    
                                    	Type e.g. 7457
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: revision
                                    
                                    	Revision. e.g 1.1
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: speed
                                    
                                    	Speed e.g. 1197Mhz
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.processor_type = None
                                        self.revision = None
                                        self.speed = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:processor-information'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.processor_type is not None:
                                            return True

                                        if self.revision is not None:
                                            return True

                                        if self.speed is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation']['meta_info']


                                class MotherboardInformation(object):
                                    """
                                    MotherboardInformation
                                    
                                    .. attribute:: bootflash
                                    
                                    	Bootflash information
                                    	**type**\: :py:class:`Bootflash <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash>`
                                    
                                    .. attribute:: main_memory_size
                                    
                                    	Memory size in bytes
                                    	**type**\: long
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: nvram_size
                                    
                                    	NVRAM size in bytes
                                    	**type**\: long
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processor
                                    
                                    	Processor information
                                    	**type**\: :py:class:`Processor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor>`
                                    
                                    .. attribute:: rom
                                    
                                    	ROM information
                                    	**type**\: :py:class:`Rom <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.bootflash = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash()
                                        self.bootflash.parent = self
                                        self.main_memory_size = None
                                        self.nvram_size = None
                                        self.processor = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor()
                                        self.processor.parent = self
                                        self.rom = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom()
                                        self.rom.parent = self


                                    class Rom(object):
                                        """
                                        ROM information
                                        
                                        .. attribute:: image_name
                                        
                                        	Image name
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: major_version
                                        
                                        	Major version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: micro_image_version
                                        
                                        	Micro image version
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: minor_version
                                        
                                        	Minor version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: platform_specific
                                        
                                        	Platform specific text
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: release_type
                                        
                                        	Release type
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.image_name = None
                                            self.major_version = None
                                            self.micro_image_version = None
                                            self.minor_version = None
                                            self.platform_specific = None
                                            self.release_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:rom'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.image_name is not None:
                                                return True

                                            if self.major_version is not None:
                                                return True

                                            if self.micro_image_version is not None:
                                                return True

                                            if self.minor_version is not None:
                                                return True

                                            if self.platform_specific is not None:
                                                return True

                                            if self.release_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom']['meta_info']


                                    class Bootflash(object):
                                        """
                                        Bootflash information
                                        
                                        .. attribute:: bootflash_size
                                        
                                        	Bootflash size in kilo\-bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: bootflash_type
                                        
                                        	Bootflash type e.g. SIMM
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: image_name
                                        
                                        	Image name
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: major_version
                                        
                                        	Major version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: micro_image_version
                                        
                                        	Micro image version
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: minor_version
                                        
                                        	Minor version
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: platform_specific
                                        
                                        	Platform specific text
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: platform_type
                                        
                                        	Platform Type
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: release_type
                                        
                                        	Release type
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: sector_size
                                        
                                        	Sector size in bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.bootflash_size = None
                                            self.bootflash_type = None
                                            self.image_name = None
                                            self.major_version = None
                                            self.micro_image_version = None
                                            self.minor_version = None
                                            self.platform_specific = None
                                            self.platform_type = None
                                            self.release_type = None
                                            self.sector_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:bootflash'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.bootflash_size is not None:
                                                return True

                                            if self.bootflash_type is not None:
                                                return True

                                            if self.image_name is not None:
                                                return True

                                            if self.major_version is not None:
                                                return True

                                            if self.micro_image_version is not None:
                                                return True

                                            if self.minor_version is not None:
                                                return True

                                            if self.platform_specific is not None:
                                                return True

                                            if self.platform_type is not None:
                                                return True

                                            if self.release_type is not None:
                                                return True

                                            if self.sector_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash']['meta_info']


                                    class Processor(object):
                                        """
                                        Processor information
                                        
                                        .. attribute:: processor_type
                                        
                                        	Type e.g. 7457
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: revision
                                        
                                        	Revision. e.g 1.1
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: speed
                                        
                                        	Speed e.g. 1197Mhz
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.processor_type = None
                                            self.revision = None
                                            self.speed = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:processor'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.processor_type is not None:
                                                return True

                                            if self.revision is not None:
                                                return True

                                            if self.speed is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:motherboard-information'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.bootflash is not None and self.bootflash._has_data():
                                            return True

                                        if self.main_memory_size is not None:
                                            return True

                                        if self.nvram_size is not None:
                                            return True

                                        if self.processor is not None and self.processor._has_data():
                                            return True

                                        if self.rom is not None and self.rom._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']


                                class BootflashInformation(object):
                                    """
                                    BootflashInformation
                                    
                                    .. attribute:: bootflash_size
                                    
                                    	Bootflash size in kilo\-bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: bootflash_type
                                    
                                    	Bootflash type e.g. SIMM
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: image_name
                                    
                                    	Image name
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: major_version
                                    
                                    	Major version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: micro_image_version
                                    
                                    	Micro image version
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: minor_version
                                    
                                    	Minor version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: platform_specific
                                    
                                    	Platform specific text
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: platform_type
                                    
                                    	Platform Type
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: release_type
                                    
                                    	Release type
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: sector_size
                                    
                                    	Sector size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.bootflash_size = None
                                        self.bootflash_type = None
                                        self.image_name = None
                                        self.major_version = None
                                        self.micro_image_version = None
                                        self.minor_version = None
                                        self.platform_specific = None
                                        self.platform_type = None
                                        self.release_type = None
                                        self.sector_size = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:bootflash-information'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.bootflash_size is not None:
                                            return True

                                        if self.bootflash_type is not None:
                                            return True

                                        if self.image_name is not None:
                                            return True

                                        if self.major_version is not None:
                                            return True

                                        if self.micro_image_version is not None:
                                            return True

                                        if self.minor_version is not None:
                                            return True

                                        if self.platform_specific is not None:
                                            return True

                                        if self.platform_type is not None:
                                            return True

                                        if self.release_type is not None:
                                            return True

                                        if self.sector_size is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation']['meta_info']


                                class DiskInformation(object):
                                    """
                                    DiskInformation
                                    
                                    .. attribute:: disk_name
                                    
                                    	(Deprecated) Disk name
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: disk_size
                                    
                                    	(Deprecated) Disk size in mega\-bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: disks
                                    
                                    	Disk attributes
                                    	**type**\: list of :py:class:`Disks <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks>`
                                    
                                    .. attribute:: sector_size
                                    
                                    	(Deprecated) Disk sector size in bytes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.disk_name = None
                                        self.disk_size = None
                                        self.disks = YList()
                                        self.disks.parent = self
                                        self.disks.name = 'disks'
                                        self.sector_size = None


                                    class Disks(object):
                                        """
                                        Disk attributes
                                        
                                        .. attribute:: disk_name
                                        
                                        	Disk name
                                        	**type**\: str
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: disk_size
                                        
                                        	Disk size in mega\-bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: sector_size
                                        
                                        	Disk sector size in bytes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.disk_name = None
                                            self.disk_size = None
                                            self.sector_size = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:disks'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.disk_name is not None:
                                                return True

                                            if self.disk_size is not None:
                                                return True

                                            if self.sector_size is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:disk-information'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.disk_name is not None:
                                            return True

                                        if self.disk_size is not None:
                                            return True

                                        if self.disks is not None:
                                            for child_ref in self.disks:
                                                if child_ref._has_data():
                                                    return True

                                        if self.sector_size is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:hardware-information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.bootflash_information is not None and self.bootflash_information._has_data():
                                        return True

                                    if self.disk_information is not None and self.disk_information._has_data():
                                        return True

                                    if self.motherboard_information is not None and self.motherboard_information._has_data():
                                        return True

                                    if self.processor_information is not None and self.processor_information._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']


                            class SubSlots(object):
                                """
                                Table of subslots
                                
                                .. attribute:: sub_slot
                                
                                	Subslot number
                                	**type**\: list of :py:class:`SubSlot <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.sub_slot = YList()
                                    self.sub_slot.parent = self
                                    self.sub_slot.name = 'sub_slot'


                                class SubSlot(object):
                                    """
                                    Subslot number
                                    
                                    .. attribute:: name  <key>
                                    
                                    	Subslot name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes>`
                                    
                                    .. attribute:: module
                                    
                                    	Module of a subslot
                                    	**type**\: :py:class:`Module <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.name = None
                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes()
                                        self.attributes.parent = self
                                        self.module = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self


                                    class Module(object):
                                        """
                                        Module of a subslot
                                        
                                        .. attribute:: attributes
                                        
                                        	Attributes
                                        	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes>`
                                        
                                        .. attribute:: port_slots
                                        
                                        	Table of port slots
                                        	**type**\: :py:class:`PortSlots <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots>`
                                        
                                        .. attribute:: sensors
                                        
                                        	Table of sensors
                                        	**type**\: :py:class:`Sensors <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes()
                                            self.attributes.parent = self
                                            self.port_slots = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self


                                        class PortSlots(object):
                                            """
                                            Table of port slots
                                            
                                            .. attribute:: port_slot
                                            
                                            	Port slot number
                                            	**type**\: list of :py:class:`PortSlot <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.port_slot = YList()
                                                self.port_slot.parent = self
                                                self.port_slot.name = 'port_slot'


                                            class PortSlot(object):
                                                """
                                                Port slot number
                                                
                                                .. attribute:: name  <key>
                                                
                                                	Port slot name
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: attributes
                                                
                                                	Attributes
                                                	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes>`
                                                
                                                .. attribute:: port
                                                
                                                	Port
                                                	**type**\: :py:class:`Port <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port>`
                                                
                                                .. attribute:: sensors
                                                
                                                	Table of sensors
                                                	**type**\: :py:class:`Sensors <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.name = None
                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes()
                                                    self.attributes.parent = self
                                                    self.port = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port()
                                                    self.port.parent = self
                                                    self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors()
                                                    self.sensors.parent = self


                                                class Port(object):
                                                    """
                                                    Port
                                                    
                                                    .. attribute:: attributes
                                                    
                                                    	Attributes
                                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes()
                                                        self.attributes.parent = self


                                                    class Attributes(object):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Entity attributes
                                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) attributes
                                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo()
                                                            self.fru_info.parent = self


                                                        class BasicInfo(object):
                                                            """
                                                            Entity attributes
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms                 what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**range:** 0..255
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.description = None
                                                                self.firmware_revision = None
                                                                self.hardware_revision = None
                                                                self.is_field_replaceable_unit = None
                                                                self.model_name = None
                                                                self.name = None
                                                                self.serial_number = None
                                                                self.software_revision = None
                                                                self.vendor_type = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.description is not None:
                                                                    return True

                                                                if self.firmware_revision is not None:
                                                                    return True

                                                                if self.hardware_revision is not None:
                                                                    return True

                                                                if self.is_field_replaceable_unit is not None:
                                                                    return True

                                                                if self.model_name is not None:
                                                                    return True

                                                                if self.name is not None:
                                                                    return True

                                                                if self.serial_number is not None:
                                                                    return True

                                                                if self.software_revision is not None:
                                                                    return True

                                                                if self.vendor_type is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo']['meta_info']


                                                        class FruInfo(object):
                                                            """
                                                            Field Replaceable Unit (FRU) attributes
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	Time operational state is   last changed
                                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: module_administrative_state
                                                            
                                                            	Administrative    state
                                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                            
                                                            .. attribute:: module_monitor_state
                                                            
                                                            	Monitor state
                                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                            
                                                            .. attribute:: module_operational_state
                                                            
                                                            	Operation state
                                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                            
                                                            .. attribute:: module_power_administrative_state
                                                            
                                                            	Power administrative state
                                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                            
                                                            .. attribute:: module_reset_reason
                                                            
                                                            	Reset reason
                                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                            
                                                            .. attribute:: module_up_time
                                                            
                                                            	Module up time
                                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self.module_administrative_state = None
                                                                self.module_monitor_state = None
                                                                self.module_operational_state = None
                                                                self.module_power_administrative_state = None
                                                                self.module_reset_reason = None
                                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime()
                                                                self.module_up_time.parent = self


                                                            class LastOperationalStateChange(object):
                                                                """
                                                                Time operational state is   last changed
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-oper'
                                                                _revision = '2015-01-07'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.time_in_nano_seconds = None
                                                                    self.time_in_seconds = None

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if not self.is_config():
                                                                        return False
                                                                    if self.time_in_nano_seconds is not None:
                                                                        return True

                                                                    if self.time_in_seconds is not None:
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                            class ModuleUpTime(object):
                                                                """
                                                                Module up time
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-oper'
                                                                _revision = '2015-01-07'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.time_in_nano_seconds = None
                                                                    self.time_in_seconds = None

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if not self.is_config():
                                                                        return False
                                                                    if self.time_in_nano_seconds is not None:
                                                                        return True

                                                                    if self.time_in_seconds is not None:
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                    return True

                                                                if self.module_administrative_state is not None:
                                                                    return True

                                                                if self.module_monitor_state is not None:
                                                                    return True

                                                                if self.module_operational_state is not None:
                                                                    return True

                                                                if self.module_power_administrative_state is not None:
                                                                    return True

                                                                if self.module_reset_reason is not None:
                                                                    return True

                                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.basic_info is not None and self.basic_info._has_data():
                                                                return True

                                                            if self.fru_info is not None and self.fru_info._has_data():
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.attributes is not None and self.attributes._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info']


                                                class Sensors(object):
                                                    """
                                                    Table of sensors
                                                    
                                                    .. attribute:: sensor
                                                    
                                                    	Sensor number
                                                    	**type**\: list of :py:class:`Sensor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.sensor = YList()
                                                        self.sensor.parent = self
                                                        self.sensor.name = 'sensor'


                                                    class Sensor(object):
                                                        """
                                                        Sensor number
                                                        
                                                        .. attribute:: name  <key>
                                                        
                                                        	Sensor name
                                                        	**type**\: str
                                                        
                                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                        
                                                        .. attribute:: attributes
                                                        
                                                        	Attributes
                                                        	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.name = None
                                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes()
                                                            self.attributes.parent = self


                                                        class Attributes(object):
                                                            """
                                                            Attributes
                                                            
                                                            .. attribute:: basic_info
                                                            
                                                            	Entity attributes
                                                            	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo>`
                                                            
                                                            .. attribute:: fru_info
                                                            
                                                            	Field Replaceable Unit (FRU) attributes
                                                            	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo>`
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo()
                                                                self.basic_info.parent = self
                                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo()
                                                                self.fru_info.parent = self


                                                            class BasicInfo(object):
                                                                """
                                                                Entity attributes
                                                                
                                                                .. attribute:: description
                                                                
                                                                	describes in user\-readable terms                 what the entity in question does
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: firmware_revision
                                                                
                                                                	firmware revision string
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: hardware_revision
                                                                
                                                                	hw revision string
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: is_field_replaceable_unit
                                                                
                                                                	1 if Field Replaceable Unit 0, if not
                                                                	**type**\: bool
                                                                
                                                                .. attribute:: model_name
                                                                
                                                                	model name
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: name
                                                                
                                                                	name string for the entity
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: serial_number
                                                                
                                                                	serial number
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: software_revision
                                                                
                                                                	software revision string
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                .. attribute:: vendor_type
                                                                
                                                                	maps to the vendor OID string
                                                                	**type**\: str
                                                                
                                                                	**range:** 0..255
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-oper'
                                                                _revision = '2015-01-07'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.description = None
                                                                    self.firmware_revision = None
                                                                    self.hardware_revision = None
                                                                    self.is_field_replaceable_unit = None
                                                                    self.model_name = None
                                                                    self.name = None
                                                                    self.serial_number = None
                                                                    self.software_revision = None
                                                                    self.vendor_type = None

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if not self.is_config():
                                                                        return False
                                                                    if self.description is not None:
                                                                        return True

                                                                    if self.firmware_revision is not None:
                                                                        return True

                                                                    if self.hardware_revision is not None:
                                                                        return True

                                                                    if self.is_field_replaceable_unit is not None:
                                                                        return True

                                                                    if self.model_name is not None:
                                                                        return True

                                                                    if self.name is not None:
                                                                        return True

                                                                    if self.serial_number is not None:
                                                                        return True

                                                                    if self.software_revision is not None:
                                                                        return True

                                                                    if self.vendor_type is not None:
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info']


                                                            class FruInfo(object):
                                                                """
                                                                Field Replaceable Unit (FRU) attributes
                                                                
                                                                .. attribute:: last_operational_state_change
                                                                
                                                                	Time operational state is   last changed
                                                                	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                                
                                                                .. attribute:: module_administrative_state
                                                                
                                                                	Administrative    state
                                                                	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                                
                                                                .. attribute:: module_monitor_state
                                                                
                                                                	Monitor state
                                                                	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                                
                                                                .. attribute:: module_operational_state
                                                                
                                                                	Operation state
                                                                	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                                
                                                                .. attribute:: module_power_administrative_state
                                                                
                                                                	Power administrative state
                                                                	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                                
                                                                .. attribute:: module_reset_reason
                                                                
                                                                	Reset reason
                                                                	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                                
                                                                .. attribute:: module_up_time
                                                                
                                                                	Module up time
                                                                	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                                
                                                                

                                                                """

                                                                _prefix = 'plat-chas-invmgr-oper'
                                                                _revision = '2015-01-07'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                                    self.last_operational_state_change.parent = self
                                                                    self.module_administrative_state = None
                                                                    self.module_monitor_state = None
                                                                    self.module_operational_state = None
                                                                    self.module_power_administrative_state = None
                                                                    self.module_reset_reason = None
                                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                                    self.module_up_time.parent = self


                                                                class LastOperationalStateChange(object):
                                                                    """
                                                                    Time operational state is   last changed
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-oper'
                                                                    _revision = '2015-01-07'

                                                                    def __init__(self):
                                                                        self.parent = None
                                                                        self.time_in_nano_seconds = None
                                                                        self.time_in_seconds = None

                                                                    @property
                                                                    def _common_path(self):
                                                                        if self.parent is None:
                                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                                    def is_config(self):
                                                                        ''' Returns True if this instance represents config data else returns False '''
                                                                        return False

                                                                    def _has_data(self):
                                                                        if not self.is_config():
                                                                            return False
                                                                        if self.time_in_nano_seconds is not None:
                                                                            return True

                                                                        if self.time_in_seconds is not None:
                                                                            return True

                                                                        return False

                                                                    @staticmethod
                                                                    def _meta_info():
                                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                                class ModuleUpTime(object):
                                                                    """
                                                                    Module up time
                                                                    
                                                                    .. attribute:: time_in_nano_seconds
                                                                    
                                                                    	Time Value in Nano\-seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    .. attribute:: time_in_seconds
                                                                    
                                                                    	Time Value in Seconds
                                                                    	**type**\: int
                                                                    
                                                                    	**range:** \-2147483648..2147483647
                                                                    
                                                                    

                                                                    """

                                                                    _prefix = 'plat-chas-invmgr-oper'
                                                                    _revision = '2015-01-07'

                                                                    def __init__(self):
                                                                        self.parent = None
                                                                        self.time_in_nano_seconds = None
                                                                        self.time_in_seconds = None

                                                                    @property
                                                                    def _common_path(self):
                                                                        if self.parent is None:
                                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                                    def is_config(self):
                                                                        ''' Returns True if this instance represents config data else returns False '''
                                                                        return False

                                                                    def _has_data(self):
                                                                        if not self.is_config():
                                                                            return False
                                                                        if self.time_in_nano_seconds is not None:
                                                                            return True

                                                                        if self.time_in_seconds is not None:
                                                                            return True

                                                                        return False

                                                                    @staticmethod
                                                                    def _meta_info():
                                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if not self.is_config():
                                                                        return False
                                                                    if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                        return True

                                                                    if self.module_administrative_state is not None:
                                                                        return True

                                                                    if self.module_monitor_state is not None:
                                                                        return True

                                                                    if self.module_operational_state is not None:
                                                                        return True

                                                                    if self.module_power_administrative_state is not None:
                                                                        return True

                                                                    if self.module_reset_reason is not None:
                                                                        return True

                                                                    if self.module_up_time is not None and self.module_up_time._has_data():
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.basic_info is not None and self.basic_info._has_data():
                                                                    return True

                                                                if self.fru_info is not None and self.fru_info._has_data():
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.name is None:
                                                                raise YPYModelError('Key property name is None')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensor[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.name is not None:
                                                                return True

                                                            if self.attributes is not None and self.attributes._has_data():
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensors'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.sensor is not None:
                                                            for child_ref in self.sensor:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors']['meta_info']


                                                class Attributes(object):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Entity attributes
                                                    	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) attributes
                                                    	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo()
                                                        self.fru_info.parent = self


                                                    class BasicInfo(object):
                                                        """
                                                        Entity attributes
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms                 what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.description = None
                                                            self.firmware_revision = None
                                                            self.hardware_revision = None
                                                            self.is_field_replaceable_unit = None
                                                            self.model_name = None
                                                            self.name = None
                                                            self.serial_number = None
                                                            self.software_revision = None
                                                            self.vendor_type = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.description is not None:
                                                                return True

                                                            if self.firmware_revision is not None:
                                                                return True

                                                            if self.hardware_revision is not None:
                                                                return True

                                                            if self.is_field_replaceable_unit is not None:
                                                                return True

                                                            if self.model_name is not None:
                                                                return True

                                                            if self.name is not None:
                                                                return True

                                                            if self.serial_number is not None:
                                                                return True

                                                            if self.software_revision is not None:
                                                                return True

                                                            if self.vendor_type is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info']


                                                    class FruInfo(object):
                                                        """
                                                        Field Replaceable Unit (FRU) attributes
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self.module_administrative_state = None
                                                            self.module_monitor_state = None
                                                            self.module_operational_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_reset_reason = None
                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self


                                                        class LastOperationalStateChange(object):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                        class ModuleUpTime(object):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                return True

                                                            if self.module_administrative_state is not None:
                                                                return True

                                                            if self.module_monitor_state is not None:
                                                                return True

                                                            if self.module_operational_state is not None:
                                                                return True

                                                            if self.module_power_administrative_state is not None:
                                                                return True

                                                            if self.module_reset_reason is not None:
                                                                return True

                                                            if self.module_up_time is not None and self.module_up_time._has_data():
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.basic_info is not None and self.basic_info._has_data():
                                                            return True

                                                        if self.fru_info is not None and self.fru_info._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.name is None:
                                                        raise YPYModelError('Key property name is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port-slot[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.name is not None:
                                                        return True

                                                    if self.attributes is not None and self.attributes._has_data():
                                                        return True

                                                    if self.port is not None and self.port._has_data():
                                                        return True

                                                    if self.sensors is not None and self.sensors._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port-slots'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.port_slot is not None:
                                                    for child_ref in self.port_slot:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info']


                                        class Sensors(object):
                                            """
                                            Table of sensors
                                            
                                            .. attribute:: sensor
                                            
                                            	Sensor number
                                            	**type**\: list of :py:class:`Sensor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.sensor = YList()
                                                self.sensor.parent = self
                                                self.sensor.name = 'sensor'


                                            class Sensor(object):
                                                """
                                                Sensor number
                                                
                                                .. attribute:: name  <key>
                                                
                                                	Sensor name
                                                	**type**\: str
                                                
                                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                
                                                .. attribute:: attributes
                                                
                                                	Attributes
                                                	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.name = None
                                                    self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes()
                                                    self.attributes.parent = self


                                                class Attributes(object):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Entity attributes
                                                    	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) attributes
                                                    	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo()
                                                        self.fru_info.parent = self


                                                    class BasicInfo(object):
                                                        """
                                                        Entity attributes
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms                 what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**range:** 0..255
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.description = None
                                                            self.firmware_revision = None
                                                            self.hardware_revision = None
                                                            self.is_field_replaceable_unit = None
                                                            self.model_name = None
                                                            self.name = None
                                                            self.serial_number = None
                                                            self.software_revision = None
                                                            self.vendor_type = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.description is not None:
                                                                return True

                                                            if self.firmware_revision is not None:
                                                                return True

                                                            if self.hardware_revision is not None:
                                                                return True

                                                            if self.is_field_replaceable_unit is not None:
                                                                return True

                                                            if self.model_name is not None:
                                                                return True

                                                            if self.name is not None:
                                                                return True

                                                            if self.serial_number is not None:
                                                                return True

                                                            if self.software_revision is not None:
                                                                return True

                                                            if self.vendor_type is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo']['meta_info']


                                                    class FruInfo(object):
                                                        """
                                                        Field Replaceable Unit (FRU) attributes
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self.module_administrative_state = None
                                                            self.module_monitor_state = None
                                                            self.module_operational_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_reset_reason = None
                                                            self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self


                                                        class LastOperationalStateChange(object):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                        class ModuleUpTime(object):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'plat-chas-invmgr-oper'
                                                            _revision = '2015-01-07'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if not self.is_config():
                                                                    return False
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                return True

                                                            if self.module_administrative_state is not None:
                                                                return True

                                                            if self.module_monitor_state is not None:
                                                                return True

                                                            if self.module_operational_state is not None:
                                                                return True

                                                            if self.module_power_administrative_state is not None:
                                                                return True

                                                            if self.module_reset_reason is not None:
                                                                return True

                                                            if self.module_up_time is not None and self.module_up_time._has_data():
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.basic_info is not None and self.basic_info._has_data():
                                                            return True

                                                        if self.fru_info is not None and self.fru_info._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.name is None:
                                                        raise YPYModelError('Key property name is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensor[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.name is not None:
                                                        return True

                                                    if self.attributes is not None and self.attributes._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensors'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.sensor is not None:
                                                    for child_ref in self.sensor:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info']


                                        class Attributes(object):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Entity attributes
                                            	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) attributes
                                            	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo()
                                                self.fru_info.parent = self


                                            class BasicInfo(object):
                                                """
                                                Entity attributes
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms                 what the entity in question does
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.description = None
                                                    self.firmware_revision = None
                                                    self.hardware_revision = None
                                                    self.is_field_replaceable_unit = None
                                                    self.model_name = None
                                                    self.name = None
                                                    self.serial_number = None
                                                    self.software_revision = None
                                                    self.vendor_type = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.description is not None:
                                                        return True

                                                    if self.firmware_revision is not None:
                                                        return True

                                                    if self.hardware_revision is not None:
                                                        return True

                                                    if self.is_field_replaceable_unit is not None:
                                                        return True

                                                    if self.model_name is not None:
                                                        return True

                                                    if self.name is not None:
                                                        return True

                                                    if self.serial_number is not None:
                                                        return True

                                                    if self.software_revision is not None:
                                                        return True

                                                    if self.vendor_type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo']['meta_info']


                                            class FruInfo(object):
                                                """
                                                Field Replaceable Unit (FRU) attributes
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	Time operational state is   last changed
                                                	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: module_administrative_state
                                                
                                                	Administrative    state
                                                	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                
                                                .. attribute:: module_monitor_state
                                                
                                                	Monitor state
                                                	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                
                                                .. attribute:: module_operational_state
                                                
                                                	Operation state
                                                	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                
                                                .. attribute:: module_power_administrative_state
                                                
                                                	Power administrative state
                                                	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                
                                                .. attribute:: module_reset_reason
                                                
                                                	Reset reason
                                                	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                
                                                .. attribute:: module_up_time
                                                
                                                	Module up time
                                                	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self.module_administrative_state = None
                                                    self.module_monitor_state = None
                                                    self.module_operational_state = None
                                                    self.module_power_administrative_state = None
                                                    self.module_reset_reason = None
                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime()
                                                    self.module_up_time.parent = self


                                                class LastOperationalStateChange(object):
                                                    """
                                                    Time operational state is   last changed
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                class ModuleUpTime(object):
                                                    """
                                                    Module up time
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                        return True

                                                    if self.module_administrative_state is not None:
                                                        return True

                                                    if self.module_monitor_state is not None:
                                                        return True

                                                    if self.module_operational_state is not None:
                                                        return True

                                                    if self.module_power_administrative_state is not None:
                                                        return True

                                                    if self.module_reset_reason is not None:
                                                        return True

                                                    if self.module_up_time is not None and self.module_up_time._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.basic_info is not None and self.basic_info._has_data():
                                                    return True

                                                if self.fru_info is not None and self.fru_info._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.attributes is not None and self.attributes._has_data():
                                                return True

                                            if self.port_slots is not None and self.port_slots._has_data():
                                                return True

                                            if self.sensors is not None and self.sensors._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']


                                    class Attributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo()
                                            self.fru_info.parent = self


                                        class BasicInfo(object):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.description = None
                                                self.firmware_revision = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.model_name = None
                                                self.name = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.vendor_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.description is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo']['meta_info']


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.module_administrative_state = None
                                                self.module_monitor_state = None
                                                self.module_operational_state = None
                                                self.module_power_administrative_state = None
                                                self.module_reset_reason = None
                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self


                                            class LastOperationalStateChange(object):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class ModuleUpTime(object):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.module_administrative_state is not None:
                                                    return True

                                                if self.module_monitor_state is not None:
                                                    return True

                                                if self.module_operational_state is not None:
                                                    return True

                                                if self.module_power_administrative_state is not None:
                                                    return True

                                                if self.module_reset_reason is not None:
                                                    return True

                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sub-slot[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.name is not None:
                                            return True

                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.module is not None and self.module._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sub-slots'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.sub_slot is not None:
                                        for child_ref in self.sub_slot:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info']


                            class HwComponents(object):
                                """
                                Table of  HW components 
                                
                                .. attribute:: hw_component
                                
                                	HW component number
                                	**type**\: list of :py:class:`HwComponent <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.hw_component = YList()
                                    self.hw_component.parent = self
                                    self.hw_component.name = 'hw_component'


                                class HwComponent(object):
                                    """
                                    HW component number
                                    
                                    .. attribute:: name  <key>
                                    
                                    	HW component name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes>`
                                    
                                    .. attribute:: sensors
                                    
                                    	Table of sensors
                                    	**type**\: :py:class:`Sensors <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.name = None
                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes()
                                        self.attributes.parent = self
                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self


                                    class Sensors(object):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number
                                        	**type**\: list of :py:class:`Sensor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.sensor = YList()
                                            self.sensor.parent = self
                                            self.sensor.name = 'sensor'


                                        class Sensor(object):
                                            """
                                            Sensor number
                                            
                                            .. attribute:: name  <key>
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.name = None
                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes()
                                                self.attributes.parent = self


                                            class Attributes(object):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo()
                                                    self.fru_info.parent = self


                                                class BasicInfo(object):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.description = None
                                                        self.firmware_revision = None
                                                        self.hardware_revision = None
                                                        self.is_field_replaceable_unit = None
                                                        self.model_name = None
                                                        self.name = None
                                                        self.serial_number = None
                                                        self.software_revision = None
                                                        self.vendor_type = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.description is not None:
                                                            return True

                                                        if self.firmware_revision is not None:
                                                            return True

                                                        if self.hardware_revision is not None:
                                                            return True

                                                        if self.is_field_replaceable_unit is not None:
                                                            return True

                                                        if self.model_name is not None:
                                                            return True

                                                        if self.name is not None:
                                                            return True

                                                        if self.serial_number is not None:
                                                            return True

                                                        if self.software_revision is not None:
                                                            return True

                                                        if self.vendor_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo']['meta_info']


                                                class FruInfo(object):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self.module_administrative_state = None
                                                        self.module_monitor_state = None
                                                        self.module_operational_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_reset_reason = None
                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self


                                                    class LastOperationalStateChange(object):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                    class ModuleUpTime(object):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                            return True

                                                        if self.module_administrative_state is not None:
                                                            return True

                                                        if self.module_monitor_state is not None:
                                                            return True

                                                        if self.module_operational_state is not None:
                                                            return True

                                                        if self.module_power_administrative_state is not None:
                                                            return True

                                                        if self.module_reset_reason is not None:
                                                            return True

                                                        if self.module_up_time is not None and self.module_up_time._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.basic_info is not None and self.basic_info._has_data():
                                                        return True

                                                    if self.fru_info is not None and self.fru_info._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.name is None:
                                                    raise YPYModelError('Key property name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensor[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.name is not None:
                                                    return True

                                                if self.attributes is not None and self.attributes._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensors'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.sensor is not None:
                                                for child_ref in self.sensor:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info']


                                    class Attributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo()
                                            self.fru_info.parent = self


                                        class BasicInfo(object):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.description = None
                                                self.firmware_revision = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.model_name = None
                                                self.name = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.vendor_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.description is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo']['meta_info']


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.module_administrative_state = None
                                                self.module_monitor_state = None
                                                self.module_operational_state = None
                                                self.module_power_administrative_state = None
                                                self.module_reset_reason = None
                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self


                                            class LastOperationalStateChange(object):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class ModuleUpTime(object):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.module_administrative_state is not None:
                                                    return True

                                                if self.module_monitor_state is not None:
                                                    return True

                                                if self.module_operational_state is not None:
                                                    return True

                                                if self.module_power_administrative_state is not None:
                                                    return True

                                                if self.module_reset_reason is not None:
                                                    return True

                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:hw-component[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.name is not None:
                                            return True

                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.sensors is not None and self.sensors._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:hw-components'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.hw_component is not None:
                                        for child_ref in self.hw_component:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info']


                            class PortSlots(object):
                                """
                                Table of port slots
                                
                                .. attribute:: port_slot
                                
                                	Port slot number
                                	**type**\: list of :py:class:`PortSlot <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.port_slot = YList()
                                    self.port_slot.parent = self
                                    self.port_slot.name = 'port_slot'


                                class PortSlot(object):
                                    """
                                    Port slot number
                                    
                                    .. attribute:: name  <key>
                                    
                                    	Port slot name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes>`
                                    
                                    .. attribute:: port
                                    
                                    	Port
                                    	**type**\: :py:class:`Port <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port>`
                                    
                                    .. attribute:: sensors
                                    
                                    	Table of sensors
                                    	**type**\: :py:class:`Sensors <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.name = None
                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes()
                                        self.attributes.parent = self
                                        self.port = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port()
                                        self.port.parent = self
                                        self.sensors = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors()
                                        self.sensors.parent = self


                                    class Port(object):
                                        """
                                        Port
                                        
                                        .. attribute:: attributes
                                        
                                        	Attributes
                                        	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes()
                                            self.attributes.parent = self


                                        class Attributes(object):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Entity attributes
                                            	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) attributes
                                            	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo()
                                                self.fru_info.parent = self


                                            class BasicInfo(object):
                                                """
                                                Entity attributes
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms                 what the entity in question does
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**range:** 0..255
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.description = None
                                                    self.firmware_revision = None
                                                    self.hardware_revision = None
                                                    self.is_field_replaceable_unit = None
                                                    self.model_name = None
                                                    self.name = None
                                                    self.serial_number = None
                                                    self.software_revision = None
                                                    self.vendor_type = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.description is not None:
                                                        return True

                                                    if self.firmware_revision is not None:
                                                        return True

                                                    if self.hardware_revision is not None:
                                                        return True

                                                    if self.is_field_replaceable_unit is not None:
                                                        return True

                                                    if self.model_name is not None:
                                                        return True

                                                    if self.name is not None:
                                                        return True

                                                    if self.serial_number is not None:
                                                        return True

                                                    if self.software_revision is not None:
                                                        return True

                                                    if self.vendor_type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo']['meta_info']


                                            class FruInfo(object):
                                                """
                                                Field Replaceable Unit (FRU) attributes
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	Time operational state is   last changed
                                                	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: module_administrative_state
                                                
                                                	Administrative    state
                                                	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                
                                                .. attribute:: module_monitor_state
                                                
                                                	Monitor state
                                                	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                
                                                .. attribute:: module_operational_state
                                                
                                                	Operation state
                                                	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                
                                                .. attribute:: module_power_administrative_state
                                                
                                                	Power administrative state
                                                	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                
                                                .. attribute:: module_reset_reason
                                                
                                                	Reset reason
                                                	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                
                                                .. attribute:: module_up_time
                                                
                                                	Module up time
                                                	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self.module_administrative_state = None
                                                    self.module_monitor_state = None
                                                    self.module_operational_state = None
                                                    self.module_power_administrative_state = None
                                                    self.module_reset_reason = None
                                                    self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime()
                                                    self.module_up_time.parent = self


                                                class LastOperationalStateChange(object):
                                                    """
                                                    Time operational state is   last changed
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                class ModuleUpTime(object):
                                                    """
                                                    Module up time
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                        return True

                                                    if self.module_administrative_state is not None:
                                                        return True

                                                    if self.module_monitor_state is not None:
                                                        return True

                                                    if self.module_operational_state is not None:
                                                        return True

                                                    if self.module_power_administrative_state is not None:
                                                        return True

                                                    if self.module_reset_reason is not None:
                                                        return True

                                                    if self.module_up_time is not None and self.module_up_time._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.basic_info is not None and self.basic_info._has_data():
                                                    return True

                                                if self.fru_info is not None and self.fru_info._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.attributes is not None and self.attributes._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info']


                                    class Sensors(object):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number
                                        	**type**\: list of :py:class:`Sensor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.sensor = YList()
                                            self.sensor.parent = self
                                            self.sensor.name = 'sensor'


                                        class Sensor(object):
                                            """
                                            Sensor number
                                            
                                            .. attribute:: name  <key>
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: attributes
                                            
                                            	Attributes
                                            	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.name = None
                                                self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes()
                                                self.attributes.parent = self


                                            class Attributes(object):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Entity attributes
                                                	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) attributes
                                                	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo()
                                                    self.fru_info.parent = self


                                                class BasicInfo(object):
                                                    """
                                                    Entity attributes
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms                 what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**range:** 0..255
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.description = None
                                                        self.firmware_revision = None
                                                        self.hardware_revision = None
                                                        self.is_field_replaceable_unit = None
                                                        self.model_name = None
                                                        self.name = None
                                                        self.serial_number = None
                                                        self.software_revision = None
                                                        self.vendor_type = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.description is not None:
                                                            return True

                                                        if self.firmware_revision is not None:
                                                            return True

                                                        if self.hardware_revision is not None:
                                                            return True

                                                        if self.is_field_replaceable_unit is not None:
                                                            return True

                                                        if self.model_name is not None:
                                                            return True

                                                        if self.name is not None:
                                                            return True

                                                        if self.serial_number is not None:
                                                            return True

                                                        if self.software_revision is not None:
                                                            return True

                                                        if self.vendor_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info']


                                                class FruInfo(object):
                                                    """
                                                    Field Replaceable Unit (FRU) attributes
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'plat-chas-invmgr-oper'
                                                    _revision = '2015-01-07'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self.module_administrative_state = None
                                                        self.module_monitor_state = None
                                                        self.module_operational_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_reset_reason = None
                                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self


                                                    class LastOperationalStateChange(object):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                    class ModuleUpTime(object):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'plat-chas-invmgr-oper'
                                                        _revision = '2015-01-07'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if not self.is_config():
                                                                return False
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if not self.is_config():
                                                            return False
                                                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                            return True

                                                        if self.module_administrative_state is not None:
                                                            return True

                                                        if self.module_monitor_state is not None:
                                                            return True

                                                        if self.module_operational_state is not None:
                                                            return True

                                                        if self.module_power_administrative_state is not None:
                                                            return True

                                                        if self.module_reset_reason is not None:
                                                            return True

                                                        if self.module_up_time is not None and self.module_up_time._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.basic_info is not None and self.basic_info._has_data():
                                                        return True

                                                    if self.fru_info is not None and self.fru_info._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.name is None:
                                                    raise YPYModelError('Key property name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensor[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.name is not None:
                                                    return True

                                                if self.attributes is not None and self.attributes._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensors'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.sensor is not None:
                                                for child_ref in self.sensor:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors']['meta_info']


                                    class Attributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo()
                                            self.fru_info.parent = self


                                        class BasicInfo(object):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.description = None
                                                self.firmware_revision = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.model_name = None
                                                self.name = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.vendor_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.description is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info']


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.module_administrative_state = None
                                                self.module_monitor_state = None
                                                self.module_operational_state = None
                                                self.module_power_administrative_state = None
                                                self.module_reset_reason = None
                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self


                                            class LastOperationalStateChange(object):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class ModuleUpTime(object):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.module_administrative_state is not None:
                                                    return True

                                                if self.module_monitor_state is not None:
                                                    return True

                                                if self.module_operational_state is not None:
                                                    return True

                                                if self.module_power_administrative_state is not None:
                                                    return True

                                                if self.module_reset_reason is not None:
                                                    return True

                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port-slot[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.name is not None:
                                            return True

                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.port is not None and self.port._has_data():
                                            return True

                                        if self.sensors is not None and self.sensors._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:port-slots'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.port_slot is not None:
                                        for child_ref in self.port_slot:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info']


                            class Sensors(object):
                                """
                                Table of sensors
                                
                                .. attribute:: sensor
                                
                                	Sensor number
                                	**type**\: list of :py:class:`Sensor <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.sensor = YList()
                                    self.sensor.parent = self
                                    self.sensor.name = 'sensor'


                                class Sensor(object):
                                    """
                                    Sensor number
                                    
                                    .. attribute:: name  <key>
                                    
                                    	Sensor name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: attributes
                                    
                                    	Attributes
                                    	**type**\: :py:class:`Attributes <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.name = None
                                        self.attributes = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes()
                                        self.attributes.parent = self


                                    class Attributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Entity attributes
                                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) attributes
                                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo()
                                            self.fru_info.parent = self


                                        class BasicInfo(object):
                                            """
                                            Entity attributes
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms                 what the entity in question does
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.description = None
                                                self.firmware_revision = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.model_name = None
                                                self.name = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.vendor_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.description is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo']['meta_info']


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) attributes
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime>`
                                            
                                            

                                            """

                                            _prefix = 'plat-chas-invmgr-oper'
                                            _revision = '2015-01-07'

                                            def __init__(self):
                                                self.parent = None
                                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.module_administrative_state = None
                                                self.module_monitor_state = None
                                                self.module_operational_state = None
                                                self.module_power_administrative_state = None
                                                self.module_reset_reason = None
                                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self


                                            class LastOperationalStateChange(object):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class ModuleUpTime(object):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'plat-chas-invmgr-oper'
                                                _revision = '2015-01-07'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.module_administrative_state is not None:
                                                    return True

                                                if self.module_monitor_state is not None:
                                                    return True

                                                if self.module_operational_state is not None:
                                                    return True

                                                if self.module_power_administrative_state is not None:
                                                    return True

                                                if self.module_reset_reason is not None:
                                                    return True

                                                if self.module_up_time is not None and self.module_up_time._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensor[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.name is not None:
                                            return True

                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:sensors'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.sensor is not None:
                                        for child_ref in self.sensor:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info']


                            class Attributes(object):
                                """
                                Attributes
                                
                                .. attribute:: basic_info
                                
                                	Entity attributes
                                	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo>`
                                
                                .. attribute:: fru_info
                                
                                	Field Replaceable Unit (FRU) attributes
                                	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo>`
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo()
                                    self.basic_info.parent = self
                                    self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo()
                                    self.fru_info.parent = self


                                class BasicInfo(object):
                                    """
                                    Entity attributes
                                    
                                    .. attribute:: description
                                    
                                    	describes in user\-readable terms                 what the entity in question does
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: firmware_revision
                                    
                                    	firmware revision string
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	hw revision string
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: is_field_replaceable_unit
                                    
                                    	1 if Field Replaceable Unit 0, if not
                                    	**type**\: bool
                                    
                                    .. attribute:: model_name
                                    
                                    	model name
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: name
                                    
                                    	name string for the entity
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: serial_number
                                    
                                    	serial number
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: software_revision
                                    
                                    	software revision string
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: vendor_type
                                    
                                    	maps to the vendor OID string
                                    	**type**\: str
                                    
                                    	**range:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.description = None
                                        self.firmware_revision = None
                                        self.hardware_revision = None
                                        self.is_field_replaceable_unit = None
                                        self.model_name = None
                                        self.name = None
                                        self.serial_number = None
                                        self.software_revision = None
                                        self.vendor_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.description is not None:
                                            return True

                                        if self.firmware_revision is not None:
                                            return True

                                        if self.hardware_revision is not None:
                                            return True

                                        if self.is_field_replaceable_unit is not None:
                                            return True

                                        if self.model_name is not None:
                                            return True

                                        if self.name is not None:
                                            return True

                                        if self.serial_number is not None:
                                            return True

                                        if self.software_revision is not None:
                                            return True

                                        if self.vendor_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo']['meta_info']


                                class FruInfo(object):
                                    """
                                    Field Replaceable Unit (FRU) attributes
                                    
                                    .. attribute:: last_operational_state_change
                                    
                                    	Time operational state is   last changed
                                    	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange>`
                                    
                                    .. attribute:: module_administrative_state
                                    
                                    	Administrative    state
                                    	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                                    
                                    .. attribute:: module_monitor_state
                                    
                                    	Monitor state
                                    	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                                    
                                    .. attribute:: module_operational_state
                                    
                                    	Operation state
                                    	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                                    
                                    .. attribute:: module_power_administrative_state
                                    
                                    	Power administrative state
                                    	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                                    
                                    .. attribute:: module_reset_reason
                                    
                                    	Reset reason
                                    	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                                    
                                    .. attribute:: module_up_time
                                    
                                    	Module up time
                                    	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime>`
                                    
                                    

                                    """

                                    _prefix = 'plat-chas-invmgr-oper'
                                    _revision = '2015-01-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self.module_administrative_state = None
                                        self.module_monitor_state = None
                                        self.module_operational_state = None
                                        self.module_power_administrative_state = None
                                        self.module_reset_reason = None
                                        self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime()
                                        self.module_up_time.parent = self


                                    class LastOperationalStateChange(object):
                                        """
                                        Time operational state is   last changed
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_in_nano_seconds = None
                                            self.time_in_seconds = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.time_in_nano_seconds is not None:
                                                return True

                                            if self.time_in_seconds is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                                    class ModuleUpTime(object):
                                        """
                                        Module up time
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        

                                        """

                                        _prefix = 'plat-chas-invmgr-oper'
                                        _revision = '2015-01-07'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_in_nano_seconds = None
                                            self.time_in_seconds = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.time_in_nano_seconds is not None:
                                                return True

                                            if self.time_in_seconds is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                            return True

                                        if self.module_administrative_state is not None:
                                            return True

                                        if self.module_monitor_state is not None:
                                            return True

                                        if self.module_operational_state is not None:
                                            return True

                                        if self.module_power_administrative_state is not None:
                                            return True

                                        if self.module_reset_reason is not None:
                                            return True

                                        if self.module_up_time is not None and self.module_up_time._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.basic_info is not None and self.basic_info._has_data():
                                        return True

                                    if self.fru_info is not None and self.fru_info._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:card[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.name is not None:
                                    return True

                                if self.attributes is not None and self.attributes._has_data():
                                    return True

                                if self.hardware_information is not None and self.hardware_information._has_data():
                                    return True

                                if self.hw_components is not None and self.hw_components._has_data():
                                    return True

                                if self.port_slots is not None and self.port_slots._has_data():
                                    return True

                                if self.portses is not None and self.portses._has_data():
                                    return True

                                if self.sensors is not None and self.sensors._has_data():
                                    return True

                                if self.sub_slots is not None and self.sub_slots._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:cards'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.card is not None:
                                for child_ref in self.card:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards']['meta_info']


                    class Attributes(object):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Entity attributes
                        	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo>`
                        
                        .. attribute:: fru_info
                        
                        	Field Replaceable Unit (FRU) attributes
                        	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo>`
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.basic_info = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo()
                            self.basic_info.parent = self
                            self.fru_info = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo()
                            self.fru_info.parent = self


                        class BasicInfo(object):
                            """
                            Entity attributes
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms                 what the entity in question does
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\: bool
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\: str
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-oper'
                            _revision = '2015-01-07'

                            def __init__(self):
                                self.parent = None
                                self.description = None
                                self.firmware_revision = None
                                self.hardware_revision = None
                                self.is_field_replaceable_unit = None
                                self.model_name = None
                                self.name = None
                                self.serial_number = None
                                self.software_revision = None
                                self.vendor_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.description is not None:
                                    return True

                                if self.firmware_revision is not None:
                                    return True

                                if self.hardware_revision is not None:
                                    return True

                                if self.is_field_replaceable_unit is not None:
                                    return True

                                if self.model_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.serial_number is not None:
                                    return True

                                if self.software_revision is not None:
                                    return True

                                if self.vendor_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo']['meta_info']


                        class FruInfo(object):
                            """
                            Field Replaceable Unit (FRU) attributes
                            
                            .. attribute:: last_operational_state_change
                            
                            	Time operational state is   last changed
                            	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange>`
                            
                            .. attribute:: module_administrative_state
                            
                            	Administrative    state
                            	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                            
                            .. attribute:: module_monitor_state
                            
                            	Monitor state
                            	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                            
                            .. attribute:: module_operational_state
                            
                            	Operation state
                            	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                            
                            .. attribute:: module_power_administrative_state
                            
                            	Power administrative state
                            	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                            
                            .. attribute:: module_reset_reason
                            
                            	Reset reason
                            	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                            
                            .. attribute:: module_up_time
                            
                            	Module up time
                            	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime>`
                            
                            

                            """

                            _prefix = 'plat-chas-invmgr-oper'
                            _revision = '2015-01-07'

                            def __init__(self):
                                self.parent = None
                                self.last_operational_state_change = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self.module_administrative_state = None
                                self.module_monitor_state = None
                                self.module_operational_state = None
                                self.module_power_administrative_state = None
                                self.module_reset_reason = None
                                self.module_up_time = PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime()
                                self.module_up_time.parent = self


                            class LastOperationalStateChange(object):
                                """
                                Time operational state is   last changed
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.time_in_nano_seconds = None
                                    self.time_in_seconds = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.time_in_nano_seconds is not None:
                                        return True

                                    if self.time_in_seconds is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                            class ModuleUpTime(object):
                                """
                                Module up time
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'plat-chas-invmgr-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    self.parent = None
                                    self.time_in_nano_seconds = None
                                    self.time_in_seconds = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.time_in_nano_seconds is not None:
                                        return True

                                    if self.time_in_seconds is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                    return True

                                if self.module_administrative_state is not None:
                                    return True

                                if self.module_monitor_state is not None:
                                    return True

                                if self.module_operational_state is not None:
                                    return True

                                if self.module_power_administrative_state is not None:
                                    return True

                                if self.module_reset_reason is not None:
                                    return True

                                if self.module_up_time is not None and self.module_up_time._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                                return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.basic_info is not None and self.basic_info._has_data():
                                return True

                            if self.fru_info is not None and self.fru_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:slot[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.attributes is not None and self.attributes._has_data():
                            return True

                        if self.cards is not None and self.cards._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                        return meta._meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:slots'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.slot is not None:
                        for child_ref in self.slot:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                    return meta._meta_table['PlatformInventory.Racks.Rack.Slots']['meta_info']


            class Attributes(object):
                """
                Attributes
                
                .. attribute:: basic_info
                
                	Entity attributes
                	**type**\: :py:class:`BasicInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Attributes.BasicInfo>`
                
                .. attribute:: fru_info
                
                	Field Replaceable Unit (FRU) attributes
                	**type**\: :py:class:`FruInfo <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo>`
                
                

                """

                _prefix = 'plat-chas-invmgr-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.basic_info = PlatformInventory.Racks.Rack.Attributes.BasicInfo()
                    self.basic_info.parent = self
                    self.fru_info = PlatformInventory.Racks.Rack.Attributes.FruInfo()
                    self.fru_info.parent = self


                class BasicInfo(object):
                    """
                    Entity attributes
                    
                    .. attribute:: description
                    
                    	describes in user\-readable terms                 what the entity in question does
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: firmware_revision
                    
                    	firmware revision string
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: hardware_revision
                    
                    	hw revision string
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: is_field_replaceable_unit
                    
                    	1 if Field Replaceable Unit 0, if not
                    	**type**\: bool
                    
                    .. attribute:: model_name
                    
                    	model name
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: name
                    
                    	name string for the entity
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: serial_number
                    
                    	serial number
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: software_revision
                    
                    	software revision string
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: vendor_type
                    
                    	maps to the vendor OID string
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.description = None
                        self.firmware_revision = None
                        self.hardware_revision = None
                        self.is_field_replaceable_unit = None
                        self.model_name = None
                        self.name = None
                        self.serial_number = None
                        self.software_revision = None
                        self.vendor_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:basic-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.description is not None:
                            return True

                        if self.firmware_revision is not None:
                            return True

                        if self.hardware_revision is not None:
                            return True

                        if self.is_field_replaceable_unit is not None:
                            return True

                        if self.model_name is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.serial_number is not None:
                            return True

                        if self.software_revision is not None:
                            return True

                        if self.vendor_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                        return meta._meta_table['PlatformInventory.Racks.Rack.Attributes.BasicInfo']['meta_info']


                class FruInfo(object):
                    """
                    Field Replaceable Unit (FRU) attributes
                    
                    .. attribute:: last_operational_state_change
                    
                    	Time operational state is   last changed
                    	**type**\: :py:class:`LastOperationalStateChange <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange>`
                    
                    .. attribute:: module_administrative_state
                    
                    	Administrative    state
                    	**type**\: :py:class:`InvAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvAdminStateEnum>`
                    
                    .. attribute:: module_monitor_state
                    
                    	Monitor state
                    	**type**\: :py:class:`InvMonitorStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvMonitorStateEnum>`
                    
                    .. attribute:: module_operational_state
                    
                    	Operation state
                    	**type**\: :py:class:`InvCardStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvCardStateEnum>`
                    
                    .. attribute:: module_power_administrative_state
                    
                    	Power administrative state
                    	**type**\: :py:class:`InvPowerAdminStateEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvPowerAdminStateEnum>`
                    
                    .. attribute:: module_reset_reason
                    
                    	Reset reason
                    	**type**\: :py:class:`InvResetReasonEnum <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.InvResetReasonEnum>`
                    
                    .. attribute:: module_up_time
                    
                    	Module up time
                    	**type**\: :py:class:`ModuleUpTime <ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper.PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime>`
                    
                    

                    """

                    _prefix = 'plat-chas-invmgr-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.last_operational_state_change = PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange()
                        self.last_operational_state_change.parent = self
                        self.module_administrative_state = None
                        self.module_monitor_state = None
                        self.module_operational_state = None
                        self.module_power_administrative_state = None
                        self.module_reset_reason = None
                        self.module_up_time = PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime()
                        self.module_up_time.parent = self


                    class LastOperationalStateChange(object):
                        """
                        Time operational state is   last changed
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Time Value in Nano\-seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: time_in_seconds
                        
                        	Time Value in Seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.time_in_nano_seconds = None
                            self.time_in_seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:last-operational-state-change'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.time_in_nano_seconds is not None:
                                return True

                            if self.time_in_seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange']['meta_info']


                    class ModuleUpTime(object):
                        """
                        Module up time
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Time Value in Nano\-seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: time_in_seconds
                        
                        	Time Value in Seconds
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'plat-chas-invmgr-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.time_in_nano_seconds = None
                            self.time_in_seconds = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:module-up-time'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.time_in_nano_seconds is not None:
                                return True

                            if self.time_in_seconds is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                            return meta._meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:fru-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                            return True

                        if self.module_administrative_state is not None:
                            return True

                        if self.module_monitor_state is not None:
                            return True

                        if self.module_operational_state is not None:
                            return True

                        if self.module_power_administrative_state is not None:
                            return True

                        if self.module_reset_reason is not None:
                            return True

                        if self.module_up_time is not None and self.module_up_time._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                        return meta._meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-plat-chas-invmgr-oper:attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.basic_info is not None and self.basic_info._has_data():
                        return True

                    if self.fru_info is not None and self.fru_info._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                    return meta._meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform-inventory/Cisco-IOS-XR-plat-chas-invmgr-oper:racks/Cisco-IOS-XR-plat-chas-invmgr-oper:rack[Cisco-IOS-XR-plat-chas-invmgr-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.attributes is not None and self.attributes._has_data():
                    return True

                if self.slots is not None and self.slots._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
                return meta._meta_table['PlatformInventory.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform-inventory/Cisco-IOS-XR-plat-chas-invmgr-oper:racks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.rack is not None:
                for child_ref in self.rack:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
            return meta._meta_table['PlatformInventory.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-plat-chas-invmgr-oper:platform-inventory'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.plat._meta import _Cisco_IOS_XR_plat_chas_invmgr_oper as meta
        return meta._meta_table['PlatformInventory']['meta_info']



""" Cisco_IOS_XR_snmp_test_trap_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SnmpColdStartRpc(object):
    """
    Generate SNMPv2\-MIB\:\:coldStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:snmp-cold-start'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['SnmpColdStartRpc']['meta_info']


class SnmpWarmStartRpc(object):
    """
    Generate SNMPv2\-MIB\:\:warmStart
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:snmp-warm-start'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['SnmpWarmStartRpc']['meta_info']


class InterfaceLinkUpRpc(object):
    """
    Generate IF\-MIB\:\:linkUp
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkUpRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = InterfaceLinkUpRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkUp trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:interface-link-up/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['InterfaceLinkUpRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:interface-link-up'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InterfaceLinkUpRpc']['meta_info']


class InterfaceLinkDownRpc(object):
    """
    Generate IF\-MIB\:\:linkDown
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.InterfaceLinkDownRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = InterfaceLinkDownRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate LinkDown trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:interface-link-down/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['InterfaceLinkDownRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:interface-link-down'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InterfaceLinkDownRpc']['meta_info']


class SonetSectionStatusRpc(object):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetSectionStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetSectionStatusRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = SonetSectionStatusRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetSectionStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['SonetSectionStatusRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-section-status'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['SonetSectionStatusRpc']['meta_info']


class SonetLineStatusRpc(object):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetLineStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetLineStatusRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = SonetLineStatusRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetLineStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['SonetLineStatusRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-line-status'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['SonetLineStatusRpc']['meta_info']


class SonetPathStatusRpc(object):
    """
    Generate CISCO\-SONET\-MIB\:\:ciscoSonetPathStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.SonetPathStatusRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = SonetPathStatusRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: ifindex
        
        	interface index for which to generate ciscoSonetPathStatusChange trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['SonetPathStatusRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:sonet-path-status'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['SonetPathStatusRpc']['meta_info']


class InfraSyslogMessageGeneratedRpc(object):
    """
    Generate CISCO\-SYSLOG\-MIB\:\:clogMessageGenerated
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-syslog-message-generated'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraSyslogMessageGeneratedRpc']['meta_info']


class InfraFlashDeviceInsertedRpc(object):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceInsertedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-inserted'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraFlashDeviceInsertedRpc']['meta_info']


class InfraFlashDeviceRemovedRpc(object):
    """
    Generate CISCO\-FLASH\-MIB\:\:ciscoFlashDeviceRemovedNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-flash-device-removed'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraFlashDeviceRemovedRpc']['meta_info']


class InfraRedundancyProgressionRpc(object):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFProgressionNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-progression'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraRedundancyProgressionRpc']['meta_info']


class InfraRedundancySwitchRpc(object):
    """
    Generate CISCO\-RF\-MIB\:\:ciscoRFSwactNotif
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-redundancy-switch'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraRedundancySwitchRpc']['meta_info']


class InfraBridgeNewRootRpc(object):
    """
    Generate BRIDGE\-MIB\:\:newRoot
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-new-root'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraBridgeNewRootRpc']['meta_info']


class InfraBridgeTopologyChangeRpc(object):
    """
    Generate BRIDGE\-MIB\:\:topologyChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-bridge-topology-change'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraBridgeTopologyChangeRpc']['meta_info']


class InfraConfigEventRpc(object):
    """
    Generate CISCO\-CONFIG\-MAN\-MIB\:\:ciscoConfigManEvent
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:infra-config-event'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['InfraConfigEventRpc']['meta_info']


class EntitySensorThresholdNotificationRpc(object):
    """
    Generate CISCO\-ENTITY\-SENSOR\-MIB\:\:entSensorThresholdNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntitySensorThresholdNotificationRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntitySensorThresholdNotificationRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntitySensorThresholdNotificationRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-sensor-threshold-notification'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntitySensorThresholdNotificationRpc']['meta_info']


class EntityFruPowerStatusChangeFailedRpc(object):
    """
    oper status changed to failed
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruPowerStatusChangeFailedRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruPowerStatusChangeFailedRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruPowerStatusChangeFailedRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-power-status-change-failed'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruPowerStatusChangeFailedRpc']['meta_info']


class EntityFruModuleStatusChangeUpRpc(object):
    """
    fu trap module status changed as ok
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeUpRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruModuleStatusChangeUpRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruModuleStatusChangeUpRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-up'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruModuleStatusChangeUpRpc']['meta_info']


class EntityFruModuleStatusChangeDownRpc(object):
    """
    fu trap module status changed as failed
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruModuleStatusChangeDownRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruModuleStatusChangeDownRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruModuleStatusChangeDownRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-module-status-change-down'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruModuleStatusChangeDownRpc']['meta_info']


class EntityFruFanTrayOperStatusUpRpc(object):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFanTrayStatusChange
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayOperStatusUpRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruFanTrayOperStatusUpRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruFanTrayOperStatusUpRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-oper-status-up'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruFanTrayOperStatusUpRpc']['meta_info']


class EntityFruFanTrayInsertedRpc(object):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRUInserted
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayInsertedRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruFanTrayInsertedRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruFanTrayInsertedRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-inserted'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruFanTrayInsertedRpc']['meta_info']


class EntityFruFanTrayRemovedRpc(object):
    """
    Generate CISCO\-ENTITY\-FRU\-CONTROL\-MIB\:\:cefcFRURemoved
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.EntityFruFanTrayRemovedRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = EntityFruFanTrayRemovedRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entindex
        
        	entity Physical Index for which to generate trap
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['EntityFruFanTrayRemovedRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:entity-fru-fan-tray-removed'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['EntityFruFanTrayRemovedRpc']['meta_info']


class PlatformHfrBundleDownedLinkRpc(object):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleDownedLinkNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleDownedLinkRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = PlatformHfrBundleDownedLinkRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\:  str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.bundle_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.bundle_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['PlatformHfrBundleDownedLinkRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-downed-link'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['PlatformHfrBundleDownedLinkRpc']['meta_info']


class PlatformHfrBundleStateRpc(object):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhBundleStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrBundleStateRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = PlatformHfrBundleStateRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: bundle_name
        
        	bundle name for which to generate the trap
        	**type**\:  str
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.bundle_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.bundle_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['PlatformHfrBundleStateRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-bundle-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['PlatformHfrBundleStateRpc']['meta_info']


class PlatformHfrPlaneStateRpc(object):
    """
    Generate CISCO\-FABRIC\-HFR\-MIB\:\:cfhPlaneStateNotification
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.PlatformHfrPlaneStateRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = PlatformHfrPlaneStateRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: plane_id
        
        	plane identifier for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.plane_id = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.plane_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['PlatformHfrPlaneStateRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:platform-hfr-plane-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['PlatformHfrPlaneStateRpc']['meta_info']


class RoutingBgpEstablishedRpc(object):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingBgpEstablishedRpc']['meta_info']


class RoutingBgpEstablishedRemotePeerRpc(object):
    """
    Generate BGP4\-MIB\:\:bglEstablishedNotification remote peer
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpEstablishedRemotePeerRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingBgpEstablishedRemotePeerRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.address = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.address is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingBgpEstablishedRemotePeerRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-established-remote-peer'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingBgpEstablishedRemotePeerRpc']['meta_info']


class RoutingBgpStateChangeRpc(object):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingBgpStateChangeRpc']['meta_info']


class RoutingBgpStateChangeRemotePeerRpc(object):
    """
    Generate CISCO\-BGP\-MIB\:\:cbgpBackwardTransition remote peer
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingBgpStateChangeRemotePeerRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingBgpStateChangeRemotePeerRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: address
        
        	BGP remote peer IP address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.address = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.address is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingBgpStateChangeRemotePeerRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-bgp-state-change-remote-peer'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingBgpStateChangeRemotePeerRpc']['meta_info']


class RoutingOspfNeighborStateChangeRpc(object):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingOspfNeighborStateChangeRpc']['meta_info']


class RoutingOspfNeighborStateChangeAddressRpc(object):
    """
    Generate OSPF\-TRAP\-MIB\:\:ospfNbrStateChange address
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingOspfNeighborStateChangeAddressRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingOspfNeighborStateChangeAddressRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: address
        
        	neighbor's IP source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: ifindex
        
        	0 for interfaces having IP addresses or IF\-MIB ifindex of addressless interface
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.address = None
            self.ifindex = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.address is not None:
                return True

            if self.ifindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingOspfNeighborStateChangeAddressRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-ospf-neighbor-state-change-address'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingOspfNeighborStateChangeAddressRpc']['meta_info']


class RoutingMplsLdpSessionDownRpc(object):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsLdpSessionDownRpc']['meta_info']


class RoutingMplsLdpSessionDownEntityIdRpc(object):
    """
    Generate MPLS\-LDP\-STD\-MIB\:\:mplsLdpSessionDown entity\-id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsLdpSessionDownEntityIdRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingMplsLdpSessionDownEntityIdRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: entity_id
        
        	entity ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\:  str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        .. attribute:: entity_index
        
        	entity index for which to generate the trap
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: peer_id
        
        	peer ldp\-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
        	**type**\:  str
        
        	**length:** 23
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.entity_id = None
            self.entity_index = None
            self.peer_id = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.entity_id is not None:
                return True

            if self.entity_index is not None:
                return True

            if self.peer_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingMplsLdpSessionDownEntityIdRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-ldp-session-down-entity-id'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsLdpSessionDownEntityIdRpc']['meta_info']


class RoutingMplsTunnelReRoutedRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelReRoutedRpc']['meta_info']


class RoutingMplsTunnelReRoutedIndexRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelRerouted index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReRoutedIndexRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingMplsTunnelReRoutedIndexRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.destination = None
            self.index = None
            self.instance = None
            self.source = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination is not None:
                return True

            if self.index is not None:
                return True

            if self.instance is not None:
                return True

            if self.source is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingMplsTunnelReRoutedIndexRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-routed-index'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelReRoutedIndexRpc']['meta_info']


class RoutingMplsTunnelReOptimizedRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelReOptimizedRpc']['meta_info']


class RoutingMplsTunnelReOptimizedIndexRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelReoptimized index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelReOptimizedIndexRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingMplsTunnelReOptimizedIndexRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	source address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.destination = None
            self.index = None
            self.instance = None
            self.source = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination is not None:
                return True

            if self.index is not None:
                return True

            if self.instance is not None:
                return True

            if self.source is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingMplsTunnelReOptimizedIndexRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-re-optimized-index'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelReOptimizedIndexRpc']['meta_info']


class RoutingMplsTunnelDownRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelDownRpc']['meta_info']


class RoutingMplsTunnelDownIndexRpc(object):
    """
    Generate MPLS\-TE\-STD\-MIB\:\:mplsTunnelDown index
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act.RoutingMplsTunnelDownIndexRpc.Input>`
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):
        self.input = RoutingMplsTunnelDownIndexRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination
        
        	destination address for which to generate the trap
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: index
        
        	tunnel index for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: instance
        
        	tunnel instance for which to generate the trap
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**mandatory**\: True
        
        .. attribute:: source
        
        	src address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'snmp-test-trap-act'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.destination = None
            self.index = None
            self.instance = None
            self.source = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index/Cisco-IOS-XR-snmp-test-trap-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination is not None:
                return True

            if self.index is not None:
                return True

            if self.instance is not None:
                return True

            if self.source is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
            return meta._meta_table['RoutingMplsTunnelDownIndexRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:routing-mpls-tunnel-down-index'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['RoutingMplsTunnelDownIndexRpc']['meta_info']


class AllRpc(object):
    """
    generate all the supported traps
    
    

    """

    _prefix = 'snmp-test-trap-act'
    _revision = '2016-10-25'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-snmp-test-trap-act:all'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_snmp_test_trap_act as meta
        return meta._meta_table['AllRpc']['meta_info']



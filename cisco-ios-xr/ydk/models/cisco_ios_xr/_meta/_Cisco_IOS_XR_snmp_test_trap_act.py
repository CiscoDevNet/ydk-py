


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SnmpColdStartRpc' : {
        'meta_info' : _MetaInfoClass('SnmpColdStartRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'snmp-cold-start',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SnmpWarmStartRpc' : {
        'meta_info' : _MetaInfoClass('SnmpWarmStartRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'snmp-warm-start',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InterfaceLinkUpRpc.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceLinkUpRpc.Input',
            False, 
            [
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                interface index for which to generate LinkUp trap
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InterfaceLinkUpRpc' : {
        'meta_info' : _MetaInfoClass('InterfaceLinkUpRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'InterfaceLinkUpRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'interface-link-up',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InterfaceLinkDownRpc.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceLinkDownRpc.Input',
            False, 
            [
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                interface index for which to generate LinkDown trap
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InterfaceLinkDownRpc' : {
        'meta_info' : _MetaInfoClass('InterfaceLinkDownRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'InterfaceLinkDownRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'interface-link-down',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetSectionStatusRpc.Input' : {
        'meta_info' : _MetaInfoClass('SonetSectionStatusRpc.Input',
            False, 
            [
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                interface index for which to generate ciscoSonetSectionStatusChange trap
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetSectionStatusRpc' : {
        'meta_info' : _MetaInfoClass('SonetSectionStatusRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'SonetSectionStatusRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'sonet-section-status',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetLineStatusRpc.Input' : {
        'meta_info' : _MetaInfoClass('SonetLineStatusRpc.Input',
            False, 
            [
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                interface index for which to generate ciscoSonetLineStatusChange trap
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetLineStatusRpc' : {
        'meta_info' : _MetaInfoClass('SonetLineStatusRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'SonetLineStatusRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'sonet-line-status',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetPathStatusRpc.Input' : {
        'meta_info' : _MetaInfoClass('SonetPathStatusRpc.Input',
            False, 
            [
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                interface index for which to generate ciscoSonetPathStatusChange trap
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'SonetPathStatusRpc' : {
        'meta_info' : _MetaInfoClass('SonetPathStatusRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'SonetPathStatusRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'sonet-path-status',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraSyslogMessageGeneratedRpc' : {
        'meta_info' : _MetaInfoClass('InfraSyslogMessageGeneratedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-syslog-message-generated',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraFlashDeviceInsertedRpc' : {
        'meta_info' : _MetaInfoClass('InfraFlashDeviceInsertedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-flash-device-inserted',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraFlashDeviceRemovedRpc' : {
        'meta_info' : _MetaInfoClass('InfraFlashDeviceRemovedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-flash-device-removed',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraRedundancyProgressionRpc' : {
        'meta_info' : _MetaInfoClass('InfraRedundancyProgressionRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-redundancy-progression',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraRedundancySwitchRpc' : {
        'meta_info' : _MetaInfoClass('InfraRedundancySwitchRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-redundancy-switch',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraBridgeNewRootRpc' : {
        'meta_info' : _MetaInfoClass('InfraBridgeNewRootRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-bridge-new-root',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraBridgeTopologyChangeRpc' : {
        'meta_info' : _MetaInfoClass('InfraBridgeTopologyChangeRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-bridge-topology-change',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'InfraConfigEventRpc' : {
        'meta_info' : _MetaInfoClass('InfraConfigEventRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'infra-config-event',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntitySensorThresholdNotificationRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntitySensorThresholdNotificationRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntitySensorThresholdNotificationRpc' : {
        'meta_info' : _MetaInfoClass('EntitySensorThresholdNotificationRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntitySensorThresholdNotificationRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-sensor-threshold-notification',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruPowerStatusChangeFailedRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruPowerStatusChangeFailedRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruPowerStatusChangeFailedRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruPowerStatusChangeFailedRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruPowerStatusChangeFailedRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-power-status-change-failed',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruModuleStatusChangeUpRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruModuleStatusChangeUpRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruModuleStatusChangeUpRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruModuleStatusChangeUpRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruModuleStatusChangeUpRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-module-status-change-up',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruModuleStatusChangeDownRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruModuleStatusChangeDownRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruModuleStatusChangeDownRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruModuleStatusChangeDownRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruModuleStatusChangeDownRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-module-status-change-down',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayOperStatusUpRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayOperStatusUpRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayOperStatusUpRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayOperStatusUpRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruFanTrayOperStatusUpRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-fan-tray-oper-status-up',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayInsertedRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayInsertedRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayInsertedRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayInsertedRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruFanTrayInsertedRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-fan-tray-inserted',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayRemovedRpc.Input' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayRemovedRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entindex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                entity Physical Index for which to generate trap
                ''',
                'entindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'EntityFruFanTrayRemovedRpc' : {
        'meta_info' : _MetaInfoClass('EntityFruFanTrayRemovedRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'EntityFruFanTrayRemovedRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'entity-fru-fan-tray-removed',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrBundleDownedLinkRpc.Input' : {
        'meta_info' : _MetaInfoClass('PlatformHfrBundleDownedLinkRpc.Input',
            False, 
            [
            _MetaInfoClassMember('bundle-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                bundle name for which to generate the trap
                ''',
                'bundle_name',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrBundleDownedLinkRpc' : {
        'meta_info' : _MetaInfoClass('PlatformHfrBundleDownedLinkRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'PlatformHfrBundleDownedLinkRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'platform-hfr-bundle-downed-link',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrBundleStateRpc.Input' : {
        'meta_info' : _MetaInfoClass('PlatformHfrBundleStateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('bundle-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                bundle name for which to generate the trap
                ''',
                'bundle_name',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrBundleStateRpc' : {
        'meta_info' : _MetaInfoClass('PlatformHfrBundleStateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'PlatformHfrBundleStateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'platform-hfr-bundle-state',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrPlaneStateRpc.Input' : {
        'meta_info' : _MetaInfoClass('PlatformHfrPlaneStateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('plane-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                plane identifier for which to generate the trap
                ''',
                'plane_id',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'PlatformHfrPlaneStateRpc' : {
        'meta_info' : _MetaInfoClass('PlatformHfrPlaneStateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'PlatformHfrPlaneStateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'platform-hfr-plane-state',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpEstablishedRpc' : {
        'meta_info' : _MetaInfoClass('RoutingBgpEstablishedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-bgp-established',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpEstablishedRemotePeerRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingBgpEstablishedRemotePeerRpc.Input',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP remote peer IP address for which to generate the trap
                ''',
                'address',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpEstablishedRemotePeerRpc' : {
        'meta_info' : _MetaInfoClass('RoutingBgpEstablishedRemotePeerRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingBgpEstablishedRemotePeerRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-bgp-established-remote-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpStateChangeRpc' : {
        'meta_info' : _MetaInfoClass('RoutingBgpStateChangeRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-bgp-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpStateChangeRemotePeerRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingBgpStateChangeRemotePeerRpc.Input',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP remote peer IP address for which to generate the trap
                ''',
                'address',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingBgpStateChangeRemotePeerRpc' : {
        'meta_info' : _MetaInfoClass('RoutingBgpStateChangeRemotePeerRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingBgpStateChangeRemotePeerRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-bgp-state-change-remote-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingOspfNeighborStateChangeRpc' : {
        'meta_info' : _MetaInfoClass('RoutingOspfNeighborStateChangeRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-ospf-neighbor-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingOspfNeighborStateChangeAddressRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingOspfNeighborStateChangeAddressRpc.Input',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                neighbor's IP source address for which to generate the trap
                ''',
                'address',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('ifindex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                0 for interfaces having IP addresses or IF-MIB ifindex of addressless interface
                ''',
                'ifindex',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingOspfNeighborStateChangeAddressRpc' : {
        'meta_info' : _MetaInfoClass('RoutingOspfNeighborStateChangeAddressRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingOspfNeighborStateChangeAddressRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-ospf-neighbor-state-change-address',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsLdpSessionDownRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsLdpSessionDownRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-ldp-session-down',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsLdpSessionDownEntityIdRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingMplsLdpSessionDownEntityIdRpc.Input',
            False, 
            [
            _MetaInfoClassMember('entity-id', ATTRIBUTE, 'str' , None, None, 
                [(23, None)], [], 
                '''                entity ldp-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
                ''',
                'entity_id',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('entity-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                entity index for which to generate the trap
                ''',
                'entity_index',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('peer-id', ATTRIBUTE, 'str' , None, None, 
                [(23, None)], [], 
                '''                peer ldp-id in x.x.x.x.y.y format where x.x.x.x is the entity IP address and y.y is the label space
                ''',
                'peer_id',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsLdpSessionDownEntityIdRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsLdpSessionDownEntityIdRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingMplsLdpSessionDownEntityIdRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-ldp-session-down-entity-id',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReRoutedRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReRoutedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-re-routed',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReRoutedIndexRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReRoutedIndexRpc.Input',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel index for which to generate the trap
                ''',
                'index',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel instance for which to generate the trap
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                source address for which to generate the trap
                ''',
                'source',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                destination address for which to generate the trap
                ''',
                'destination',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReRoutedIndexRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReRoutedIndexRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingMplsTunnelReRoutedIndexRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-re-routed-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReOptimizedRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReOptimizedRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-re-optimized',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReOptimizedIndexRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReOptimizedIndexRpc.Input',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel index for which to generate the trap
                ''',
                'index',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel instance for which to generate the trap
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                source address for which to generate the trap
                ''',
                'source',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                destination address for which to generate the trap
                ''',
                'destination',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelReOptimizedIndexRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelReOptimizedIndexRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingMplsTunnelReOptimizedIndexRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-re-optimized-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelDownRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelDownRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-down',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelDownIndexRpc.Input' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelDownIndexRpc.Input',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel index for which to generate the trap
                ''',
                'index',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                tunnel instance for which to generate the trap
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                src address
                ''',
                'source',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                destination address for which to generate the trap
                ''',
                'destination',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'RoutingMplsTunnelDownIndexRpc' : {
        'meta_info' : _MetaInfoClass('RoutingMplsTunnelDownIndexRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act', 'RoutingMplsTunnelDownIndexRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-snmp-test-trap-act', False),
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'routing-mpls-tunnel-down-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
    'AllRpc' : {
        'meta_info' : _MetaInfoClass('AllRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-snmp-test-trap-act',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-test-trap-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_test_trap_act'
        ),
    },
}
_meta_table['InterfaceLinkUpRpc.Input']['meta_info'].parent =_meta_table['InterfaceLinkUpRpc']['meta_info']
_meta_table['InterfaceLinkDownRpc.Input']['meta_info'].parent =_meta_table['InterfaceLinkDownRpc']['meta_info']
_meta_table['SonetSectionStatusRpc.Input']['meta_info'].parent =_meta_table['SonetSectionStatusRpc']['meta_info']
_meta_table['SonetLineStatusRpc.Input']['meta_info'].parent =_meta_table['SonetLineStatusRpc']['meta_info']
_meta_table['SonetPathStatusRpc.Input']['meta_info'].parent =_meta_table['SonetPathStatusRpc']['meta_info']
_meta_table['EntitySensorThresholdNotificationRpc.Input']['meta_info'].parent =_meta_table['EntitySensorThresholdNotificationRpc']['meta_info']
_meta_table['EntityFruPowerStatusChangeFailedRpc.Input']['meta_info'].parent =_meta_table['EntityFruPowerStatusChangeFailedRpc']['meta_info']
_meta_table['EntityFruModuleStatusChangeUpRpc.Input']['meta_info'].parent =_meta_table['EntityFruModuleStatusChangeUpRpc']['meta_info']
_meta_table['EntityFruModuleStatusChangeDownRpc.Input']['meta_info'].parent =_meta_table['EntityFruModuleStatusChangeDownRpc']['meta_info']
_meta_table['EntityFruFanTrayOperStatusUpRpc.Input']['meta_info'].parent =_meta_table['EntityFruFanTrayOperStatusUpRpc']['meta_info']
_meta_table['EntityFruFanTrayInsertedRpc.Input']['meta_info'].parent =_meta_table['EntityFruFanTrayInsertedRpc']['meta_info']
_meta_table['EntityFruFanTrayRemovedRpc.Input']['meta_info'].parent =_meta_table['EntityFruFanTrayRemovedRpc']['meta_info']
_meta_table['PlatformHfrBundleDownedLinkRpc.Input']['meta_info'].parent =_meta_table['PlatformHfrBundleDownedLinkRpc']['meta_info']
_meta_table['PlatformHfrBundleStateRpc.Input']['meta_info'].parent =_meta_table['PlatformHfrBundleStateRpc']['meta_info']
_meta_table['PlatformHfrPlaneStateRpc.Input']['meta_info'].parent =_meta_table['PlatformHfrPlaneStateRpc']['meta_info']
_meta_table['RoutingBgpEstablishedRemotePeerRpc.Input']['meta_info'].parent =_meta_table['RoutingBgpEstablishedRemotePeerRpc']['meta_info']
_meta_table['RoutingBgpStateChangeRemotePeerRpc.Input']['meta_info'].parent =_meta_table['RoutingBgpStateChangeRemotePeerRpc']['meta_info']
_meta_table['RoutingOspfNeighborStateChangeAddressRpc.Input']['meta_info'].parent =_meta_table['RoutingOspfNeighborStateChangeAddressRpc']['meta_info']
_meta_table['RoutingMplsLdpSessionDownEntityIdRpc.Input']['meta_info'].parent =_meta_table['RoutingMplsLdpSessionDownEntityIdRpc']['meta_info']
_meta_table['RoutingMplsTunnelReRoutedIndexRpc.Input']['meta_info'].parent =_meta_table['RoutingMplsTunnelReRoutedIndexRpc']['meta_info']
_meta_table['RoutingMplsTunnelReOptimizedIndexRpc.Input']['meta_info'].parent =_meta_table['RoutingMplsTunnelReOptimizedIndexRpc']['meta_info']
_meta_table['RoutingMplsTunnelDownIndexRpc.Input']['meta_info'].parent =_meta_table['RoutingMplsTunnelDownIndexRpc']['meta_info']




import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'InterfaceModeEnum_Enum' : _MetaInfoEnum('InterfaceModeEnum_Enum', 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg',
        {
            'default':'DEFAULT',
            'point-to-point':'POINT_TO_POINT',
            'multipoint':'MULTIPOINT',
            'l2-transport':'L2_TRANSPORT',
        }, 'Cisco-IOS-XR-ifmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg']),
    'SecondaryAdminStateEnum_Enum' : _MetaInfoEnum('SecondaryAdminStateEnum_Enum', 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg',
        {
            'maintenance':'MAINTENANCE',
        }, 'Cisco-IOS-XR-ifmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg']),
    'LinkStatusEnum_Enum' : _MetaInfoEnum('LinkStatusEnum_Enum', 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg',
        {
            'default':'DEFAULT',
            'disable':'DISABLE',
            'software-interfaces':'SOFTWARE_INTERFACES',
        }, 'Cisco-IOS-XR-ifmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg']),
    'GlobalInterfaceConfiguration' : {
        'meta_info' : _MetaInfoClass('GlobalInterfaceConfiguration',
            False, 
            [
            _MetaInfoClassMember('link-status', REFERENCE_ENUM_CLASS, 'LinkStatusEnum_Enum' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'LinkStatusEnum_Enum', 
                [], [], 
                '''                Enable or disable link-status messages
                ''',
                'link_status',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'global-interface-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Afs.Af' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'VrfAddressFamily_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamily_Enum', 
                [], [], 
                '''                Address-family
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'VrfSubAddressFamily_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamily_Enum', 
                [], [], 
                '''                Sub-address-family
                ''',
                'saf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Afs.AfTopologyName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Afs.AfTopologyName',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'VrfAddressFamily_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamily_Enum', 
                [], [], 
                '''                Address-family
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'VrfSubAddressFamily_Enum' , 'ydk.models.infra.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamily_Enum', 
                [], [], 
                '''                Sub-address-family
                ''',
                'saf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Topology name
                ''',
                'topology_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'af-topology-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Afs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Afs.Af', 
                [], [], 
                '''                The presence of this object enables the
                givenaddress-family and topology on the
                interface.
                ''',
                'af',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('af-topology-name', REFERENCE_LIST, 'AfTopologyName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Afs.AfTopologyName', 
                [], [], 
                '''                The presence of this object enables the
                givenaddress-family and topology on the
                interface.
                ''',
                'af_topology_name',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.MaximumCellPackingTimers' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.MaximumCellPackingTimers',
            False, 
            [
            _MetaInfoClassMember('cell-packing-timer1', ATTRIBUTE, 'int' , None, None, 
                [(50, 4095)], [], 
                '''                Cell-packing timer1 (micro seconds)
                ''',
                'cell_packing_timer1',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('cell-packing-timer2', ATTRIBUTE, 'int' , None, None, 
                [(50, 4095)], [], 
                '''                Cell-packing timer2 (micro seconds)
                ''',
                'cell_packing_timer2',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('cell-packing-timer3', ATTRIBUTE, 'int' , None, None, 
                [(50, 4095)], [], 
                '''                Cell-packing timer3 (micro seconds)
                ''',
                'cell_packing_timer3',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'maximum-cell-packing-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.CellPacking' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.CellPacking',
            False, 
            [
            _MetaInfoClassMember('cell-packing-timer-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 3)], [], 
                '''                Which cell packing timer to use
                ''',
                'cell_packing_timer_id',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('maximum-cells-packed', ATTRIBUTE, 'int' , None, None, 
                [(2, 255)], [], 
                '''                Maximum number of cells to be packed in a
                packet
                ''',
                'maximum_cells_packed',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'cell-packing',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.OamEmulation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.OamEmulation',
            False, 
            [
            _MetaInfoClassMember('ais-transmit-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 60)], [], 
                '''                AIS cell transmit rate (1 per x seconds)
                ''',
                'ais_transmit_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OAM emulation
                ''',
                'enable',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'oam-emulation',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.Shape' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.Shape',
            False, 
            [
            _MetaInfoClassMember('burst-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 8192)], [], 
                '''                Burst size in cells
                ''',
                'burst_size',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Peak cell rate (kbps)
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Sustained cell rate (kbps)
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AtmPvcShaping_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcShaping_Enum', 
                [], [], 
                '''                Traffic shaping type
                ''',
                'type',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc',
            False, 
            [
            _MetaInfoClassMember('pv-ctype', REFERENCE_ENUM_CLASS, 'AtmPvcData_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcData_Enum', 
                [], [], 
                '''                PVC type
                ''',
                'pv_ctype',
                'Cisco-IOS-XR-atm-vcm-cfg', True),
            _MetaInfoClassMember('vci', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                VCI value
                ''',
                'vci',
                'Cisco-IOS-XR-atm-vcm-cfg', True),
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                VPI value
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-cfg', True),
            _MetaInfoClassMember('cell-packing', REFERENCE_CLASS, 'CellPacking' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.CellPacking', 
                [], [], 
                '''                Configure cell-packing parameters.  All
                parameters are mandatory.
                ''',
                'cell_packing',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create the PVC
                ''',
                'enable',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'AtmPvcEncapsulation_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcEncapsulation_Enum', 
                [], [], 
                '''                Configure encapsulation
                ''',
                'encapsulation',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('oam-emulation', REFERENCE_CLASS, 'OamEmulation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.OamEmulation', 
                [], [], 
                '''                L2VPN OAM emulation
                ''',
                'oam_emulation',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('oam-segment-endpoint', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2VPN PVC OAM segment endpoint
                ''',
                'oam_segment_endpoint',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.Shape', 
                [], [], 
                '''                Configure traffic shaping parameters
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('test-mode', REFERENCE_ENUM_CLASS, 'AtmPvcTestMode_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg', 'AtmPvcTestMode_Enum', 
                [], [], 
                '''                Configure the PVC test mode
                ''',
                'test_mode',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('vc-class', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Name of the VC class
                ''',
                'vc_class',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'pvc',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs',
            False, 
            [
            _MetaInfoClassMember('pvc', REFERENCE_LIST, 'Pvc' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc', 
                [], [], 
                '''                Configuration particular PVC
                ''',
                'pvc',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'pvcs',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.CellPacking' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.CellPacking',
            False, 
            [
            _MetaInfoClassMember('cell-packing-timer-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 3)], [], 
                '''                Which cell packing timer to use
                ''',
                'cell_packing_timer_id',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('maximum-cells-packed', ATTRIBUTE, 'int' , None, None, 
                [(2, 255)], [], 
                '''                Maximum number of cells to be packed in a
                packet
                ''',
                'maximum_cells_packed',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'cell-packing',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.Shape' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.Shape',
            False, 
            [
            _MetaInfoClassMember('burst-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 8192)], [], 
                '''                Burst size in cells
                ''',
                'burst_size',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Peak cell rate (kbps)
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Sustained cell rate (kbps)
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AtmPvcShaping_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes', 'AtmPvcShaping_Enum', 
                [], [], 
                '''                Traffic shaping type
                ''',
                'type',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp',
            False, 
            [
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                VPI value
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-cfg', True),
            _MetaInfoClassMember('cell-packing', REFERENCE_CLASS, 'CellPacking' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.CellPacking', 
                [], [], 
                '''                Configure cell-packing parameters.  All
                parameters are mandatory.
                ''',
                'cell_packing',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create the PVP
                ''',
                'enable',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('oam-segment-endpoint', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2VPN PVP OAM segment endpoint
                ''',
                'oam_segment_endpoint',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.Shape', 
                [], [], 
                '''                Configure traffic shaping parameters
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('test-mode', REFERENCE_ENUM_CLASS, 'AtmPvpTestMode_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg', 'AtmPvpTestMode_Enum', 
                [], [], 
                '''                Configure the PVP test mode
                ''',
                'test_mode',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'pvp',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps',
            False, 
            [
            _MetaInfoClassMember('pvp', REFERENCE_LIST, 'Pvp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp', 
                [], [], 
                '''                Configuration of particular PVP
                ''',
                'pvp',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'pvps',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel.Shape' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel.Shape',
            False, 
            [
            _MetaInfoClassMember('burst-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 8192)], [], 
                '''                Burst size in cells
                ''',
                'burst_size',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Peak cell rate (kbps)
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [(8, 622080)], [], 
                '''                Sustained cell rate (kbps)
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AtmVpShaping_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes', 'AtmVpShaping_Enum', 
                [], [], 
                '''                Traffic shaping type
                ''',
                'type',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel',
            False, 
            [
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                VPI value
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-cfg', True),
            _MetaInfoClassMember('disable-f4oam', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable F4 OAM configuration
                ''',
                'disable_f4oam',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create the VP Tunnel
                ''',
                'enable',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enable-hierarchical-shaping', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Hierarchical Shaping configuration
                ''',
                'enable_hierarchical_shaping',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel.Shape', 
                [], [], 
                '''                Configure Traffic shaping parameters
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'vp-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels',
            False, 
            [
            _MetaInfoClassMember('vp-tunnel', REFERENCE_LIST, 'VpTunnel' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel', 
                [], [], 
                '''                Configure a VP tunnel on this interface
                ''',
                'vp_tunnel',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'vp-tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Atm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Atm',
            False, 
            [
            _MetaInfoClassMember('max-vpi-bits', REFERENCE_ENUM_CLASS, 'AtmVpiBitsMode_Enum' , 'ydk.models.atm.Cisco_IOS_XR_atm_vcm_cfg', 'AtmVpiBitsMode_Enum', 
                [], [], 
                '''                Support 12-bits VPI cell format
                ''',
                'max_vpi_bits',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('maximum-cell-packing-timers', REFERENCE_CLASS, 'MaximumCellPackingTimers' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.MaximumCellPackingTimers', 
                [], [], 
                '''                Configure maximum cell-packing timers.  All
                parameters are mandatory.
                ''',
                'maximum_cell_packing_timers',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('pvcs', REFERENCE_CLASS, 'Pvcs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs', 
                [], [], 
                '''                PVC Configuration
                ''',
                'pvcs',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('pvps', REFERENCE_CLASS, 'Pvps' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps', 
                [], [], 
                '''                PVP Configuration
                ''',
                'pvps',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('vc-class', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Name of the VC class
                ''',
                'vc_class',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('vp-tunnels', REFERENCE_CLASS, 'VpTunnels' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels', 
                [], [], 
                '''                VP tunnel configuration
                ''',
                'vp_tunnels',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'atm',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Echo' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Echo',
            False, 
            [
            _MetaInfoClassMember('min-interval', ATTRIBUTE, 'int' , None, None, 
                [(15, 2000)], [], 
                '''                Configure echo min-interval for bundle
                interface
                ''',
                'min_interval',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'echo',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Timers' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Timers',
            False, 
            [
            _MetaInfoClassMember('nbor-unconfig-timer', ATTRIBUTE, 'int' , None, None, 
                [(60, 3600)], [], 
                '''                Timer associated with aggressiveness on BFD
                session peer being unconfigured
                ''',
                'nbor_unconfig_timer',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('start-timer', ATTRIBUTE, 'int' , None, None, 
                [(60, 3600)], [], 
                '''                Timer associated with aggressiveness on BFD
                session creation
                ''',
                'start_timer',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address for BFD sessions created
                by bundlemgr
                ''',
                'destination_address',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by bundlemgr
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('echo', REFERENCE_CLASS, 'Echo' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Echo', 
                [], [], 
                '''                Container for Echo min-multiplier
                ''',
                'echo',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('fast-detect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure to enable BFD over bundle members
                ''',
                'fast_detect',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by
                bundlemgr
                ''',
                'interval',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Timers', 
                [], [], 
                '''                Timers associated with BFDoBM
                ''',
                'timers',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4', 
                [], [], 
                '''                Configuration of BFDoBM for IPv4 address
                family
                ''',
                'ipv4',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'address-family',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bfd' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bfd',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_CLASS, 'AddressFamily' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily', 
                [], [], 
                '''                Configuration of BFDoBM for all address
                families
                ''',
                'address_family',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'BfdMode_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'BfdMode_Enum', 
                [], [], 
                '''                Configuration of BFDoBM mode [cisco|ietf]
                ''',
                'mode',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing.HashFunction' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing.HashFunction',
            False, 
            [
            _MetaInfoClassMember('hash-type', REFERENCE_ENUM_CLASS, 'BundleLoadBalance_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleLoadBalance_Enum', 
                [], [], 
                '''                The specified hash function to use
                ''',
                'hash_type',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('hash-value', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                The loadbalance hash value selected. For
                non-EFP Value methods, this value must be set
                to 1.
                ''',
                'hash_value',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'hash-function',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing',
            False, 
            [
            _MetaInfoClassMember('hash-function', REFERENCE_CLASS, 'HashFunction' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing.HashFunction', 
                [], [], 
                '''                Enable loadbalancing on this Bundle / EFP
                ''',
                'hash_function',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('localize-links', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Set thresholds for forwarding bundle traffic
                within a rack
                ''',
                'localize_links',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'bundle-load-balancing',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive.Links' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive.Links',
            False, 
            [
            _MetaInfoClassMember('links', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Number of active links
                ''',
                'links',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('max-active-links-mode', REFERENCE_ENUM_CLASS, 'BundleMaximumActiveLinksMode_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleMaximumActiveLinksMode_Enum', 
                [], [], 
                '''                Maximum active links mode
                ''',
                'max_active_links_mode',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'links',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive',
            False, 
            [
            _MetaInfoClassMember('links', REFERENCE_CLASS, 'Links' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive.Links', 
                [], [], 
                '''                Maximum number of active links in a bundle
                ''',
                'links',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'maximum-active',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle.MinimumActive' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle.MinimumActive',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Bandwidth (in kbps) needed to bring up a
                bundle
                ''',
                'bandwidth',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('links', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Number of active links needed to bring up a
                bundle
                ''',
                'links',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'minimum-active',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Bundle' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Bundle',
            False, 
            [
            _MetaInfoClassMember('bundle-load-balancing', REFERENCE_CLASS, 'BundleLoadBalancing' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing', 
                [], [], 
                '''                Load-balance configuration
                ''',
                'bundle_load_balancing',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('maximum-active', REFERENCE_CLASS, 'MaximumActive' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive', 
                [], [], 
                '''                Set a limit on the number of links that can be
                active
                ''',
                'maximum_active',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('minimum-active', REFERENCE_CLASS, 'MinimumActive' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle.MinimumActive', 
                [], [], 
                '''                Minimum criteria for a bundle to be active
                ''',
                'minimum_active',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Deactivate all member links (down to Standby
                state)
                ''',
                'shutdown',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('wait-while', ATTRIBUTE, 'int' , None, None, 
                [(0, 2000)], [], 
                '''                Set the wait-while timeout for members of this
                bundle
                ''',
                'wait_while',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'bundle',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.BundleMember.Id' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.BundleMember.Id',
            False, 
            [
            _MetaInfoClassMember('bundle-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Identifier of the bundle to add the port to.
                ''',
                'bundle_id',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('port-activity', REFERENCE_ENUM_CLASS, 'BundlePortActivity_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'BundlePortActivity_Enum', 
                [], [], 
                '''                Port Activity
                ''',
                'port_activity',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'id',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.BundleMember' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.BundleMember',
            False, 
            [
            _MetaInfoClassMember('id', REFERENCE_CLASS, 'Id' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.BundleMember.Id', 
                [], [], 
                '''                Add the port to an aggregated interface.
                ''',
                'id',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('port-priority', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Priority for this port. Lower value is higher
                priority.
                ''',
                'port_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'bundle-member',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Cdp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Cdp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable or disable CDP on an interface
                ''',
                'enable',
                'Cisco-IOS-XR-cdp-cfg', False),
            ],
            'Cisco-IOS-XR-cdp-cfg',
            'cdp',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('service-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of policy-map
                ''',
                'service_policy_name',
                'Cisco-IOS-XR-ncs5500-qos-cfg', True),
            _MetaInfoClassMember('account-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccount_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosPolicyAccount_Enum', 
                [], [], 
                '''                Turn off L2 or L3 accounting.
                ''',
                'account_type',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('l1-user-defined', ATTRIBUTE, 'int' , None, None, 
                [(-63, 63)], [], 
                '''                User specified value
                ''',
                'l1_user_defined',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('policy-merge', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'policy_merge',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('resource-id', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'resource_id',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('service-fragment-parent-policy', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'service_fragment_parent_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'spi_name',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('subscriber-parent-policy', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'subscriber_parent_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input.ServicePolicy', 
                [], [], 
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('service-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of policy-map
                ''',
                'service_policy_name',
                'Cisco-IOS-XR-ncs5500-qos-cfg', True),
            _MetaInfoClassMember('account-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccount_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosPolicyAccount_Enum', 
                [], [], 
                '''                Turn off L2 or L3 accounting.
                ''',
                'account_type',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('l1-user-defined', ATTRIBUTE, 'int' , None, None, 
                [(-63, 63)], [], 
                '''                User specified value
                ''',
                'l1_user_defined',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('policy-merge', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'policy_merge',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('resource-id', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'resource_id',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('service-fragment-parent-policy', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'service_fragment_parent_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'spi_name',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('subscriber-parent-policy', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'subscriber_parent_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output.ServicePolicy', 
                [], [], 
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos',
            False, 
            [
            _MetaInfoClassMember('actual-rate-down', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Minimum bandwidth guaranteed for a subscriber
                ''',
                'actual_rate_down',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('actual-rate-up', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Minimum bandwidth guaranteed for a subscriber
                ''',
                'actual_rate_up',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input', 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output', 
                [], [], 
                '''                Egress service policy
                ''',
                'output',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-cfg',
            'Cisco-IOS-XR-ncs5500-qos-cfg_qos',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('service-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of policy-map
                ''',
                'service_policy_name',
                'Cisco-IOS-XR-skp-qos-cfg', True),
            _MetaInfoClassMember('account-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccount_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'QosPolicyAccount_Enum', 
                [], [], 
                '''                Turn off L2 or L3 accounting.
                ''',
                'account_type',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('l1-user-defined', ATTRIBUTE, 'int' , None, None, 
                [(-63, 63)], [], 
                '''                User specified value
                ''',
                'l1_user_defined',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('policy-merge', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'policy_merge',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('resource-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                Resource ID value
                ''',
                'resource_id',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('service-fragment-parent-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if service-policy applied is a
                service-fragment policy).
                ''',
                'service_fragment_parent_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('subscriber-parent-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if service-policy applied on svlan.
                ''',
                'subscriber_parent_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input.ServicePolicy', 
                [], [], 
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead.Account' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead.Account',
            False, 
            [
            _MetaInfoClassMember('atm-cell-tax', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ATM cell tax to be included for overhead
                calculation
                ''',
                'atm_cell_tax',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('data-link-type', REFERENCE_ENUM_CLASS, 'Qosl2DataLink_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'Qosl2DataLink_Enum', 
                [], [], 
                '''                Data link type
                ''',
                'data_link_type',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('encap-type', REFERENCE_ENUM_CLASS, 'Qosl2Encap_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'Qosl2Encap_Enum', 
                [], [], 
                '''                Encap used between the DSLAM and CPE
                ''',
                'encap_type',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('l2-user-defined', ATTRIBUTE, 'int' , None, None, 
                [(-63, 63)], [], 
                '''                User specified value 
                ''',
                'l2_user_defined',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'account',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead',
            False, 
            [
            _MetaInfoClassMember('account', REFERENCE_CLASS, 'Account' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead.Account', 
                [], [], 
                '''                Access Loop Encapsulation
                ''',
                'account',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('iwf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IWF for L2 overhead accounting
                ''',
                'iwf',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'l2-overhead',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('service-policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of policy-map
                ''',
                'service_policy_name',
                'Cisco-IOS-XR-skp-qos-cfg', True),
            _MetaInfoClassMember('account-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccount_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'QosPolicyAccount_Enum', 
                [], [], 
                '''                Turn off L2 or L3 accounting.
                ''',
                'account_type',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('l1-user-defined', ATTRIBUTE, 'int' , None, None, 
                [(-63, 63)], [], 
                '''                User specified value
                ''',
                'l1_user_defined',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('policy-merge', REFERENCE_ENUM_CLASS, 'QosFieldNotSupported_Enum' , 'ydk.models.skp.Cisco_IOS_XR_skp_qos_cfg', 'QosFieldNotSupported_Enum', 
                [], [], 
                '''                Not supported (Leave unspecified).
                ''',
                'policy_merge',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('resource-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                Resource ID value
                ''',
                'resource_id',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('service-fragment-parent-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if service-policy applied is a
                service-fragment policy).
                ''',
                'service_fragment_parent_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('spi-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the SPI
                ''',
                'spi_name',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('subscriber-parent-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if service-policy applied on svlan.
                ''',
                'subscriber_parent_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_LIST, 'ServicePolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output.ServicePolicy', 
                [], [], 
                '''                Service policy details
                ''',
                'service_policy',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos',
            False, 
            [
            _MetaInfoClassMember('actual-rate-down', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Minimum bandwidth guaranteed for a subscriber
                ''',
                'actual_rate_down',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('actual-rate-up', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Minimum bandwidth guaranteed for a subscriber
                ''',
                'actual_rate_up',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input', 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('l2-overhead', REFERENCE_CLASS, 'L2Overhead' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead', 
                [], [], 
                '''                Layer 2 overhead accounting
                ''',
                'l2_overhead',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('minimum-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Minimum bandwidth guaranteed for a subscriber
                ''',
                'minimum_bandwidth',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output', 
                [], [], 
                '''                Egress service policy
                ''',
                'output',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            ],
            'Cisco-IOS-XR-skp-qos-cfg',
            'Cisco-IOS-XR-skp-qos-cfg_qos',
            _yang_ns._namespaces['Cisco-IOS-XR-skp-qos-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Distance' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Distance',
            False, 
            [
            _MetaInfoClassMember('dist-norm', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                Normal Route Distance
                ''',
                'dist_norm',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('dist-prio', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                Priority Route Distance
                ''',
                'dist_prio',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Metric' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Metric',
            False, 
            [
            _MetaInfoClassMember('metric-norm', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                Normal Route Metric
                ''',
                'metric_norm',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('metric-prio', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                Priority Route Metric
                ''',
                'metric_prio',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Timers' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Timers',
            False, 
            [
            _MetaInfoClassMember('query-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 10000)], [], 
                '''                Query Timeout
                ''',
                'query_time',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('sby-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 10000)], [], 
                '''                Standby Query Timeout
                ''',
                'sby_time',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub',
            False, 
            [
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Distance', 
                [], [], 
                '''                Set Route Distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Metric', 
                [], [], 
                '''                Set Route Metric
                ''',
                'metric',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('priority-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 10000)], [], 
                '''                Priority Timeout value
                ''',
                'priority_timeout',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Timers', 
                [], [], 
                '''                Set Query Timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'sub',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr',
            False, 
            [
            _MetaInfoClassMember('ip-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DAGR Peer IPv4 address
                ''',
                'ip_addr',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('enter', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DAGR Group Enter item
                ''',
                'enter',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('sub', REFERENCE_CLASS, 'Sub' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub', 
                [], [], 
                '''                DAGR Submode configuration
                ''',
                'sub',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'dagr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dagrs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dagrs',
            False, 
            [
            _MetaInfoClassMember('dagr', REFERENCE_LIST, 'Dagr' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr', 
                [], [], 
                '''                The DAGR entry being configured
                ''',
                'dagr',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'dagrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Dampening.Args_Enum' : _MetaInfoEnum('Args_Enum', 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg',
        {
            'default-values':'DEFAULT_VALUES',
            'specify-half-life':'SPECIFY_HALF_LIFE',
            'specify-all':'SPECIFY_ALL',
            'specify-rp':'SPECIFY_RP',
        }, 'Cisco-IOS-XR-ifmgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg']),
    'InterfaceConfigurations.InterfaceConfiguration.Dampening' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Dampening',
            False, 
            [
            _MetaInfoClassMember('args', REFERENCE_ENUM_CLASS, 'Args_Enum' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dampening.Args_Enum', 
                [], [], 
                '''                Dampening Arguments
                ''',
                'args',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [(1, 45)], [], 
                '''                Decay half life (in minutes)
                ''',
                'half_life',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('restart-penalty', ATTRIBUTE, 'int' , None, None, 
                [(0, 20000)], [], 
                '''                Restart penalty
                ''',
                'restart_penalty',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 20000)], [], 
                '''                Reuse threshold
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 20000)], [], 
                '''                Suppress threshold
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('suppress-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Max suppress time (in minutes)
                ''',
                'suppress_time',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Encapsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Encapsulation',
            False, 
            [
            _MetaInfoClassMember('capsulation-options', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The options for this capsulation, usually '0'
                ''',
                'capsulation_options',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('encapsulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The encapsulation - e.g. hdlc, ppp
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EsPacketFilter' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EsPacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Name of filter to be applied to inbound packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('outbound', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Name of filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'es-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ethernet.CarrierDelay' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ethernet.CarrierDelay',
            False, 
            [
            _MetaInfoClassMember('carrier-delay-down', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Carrier Delay (down) in msecs
                ''',
                'carrier_delay_down',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('carrier-delay-up', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Carrier Delay (up) in msecs
                ''',
                'carrier_delay_up',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-media-eth-cfg',
            'carrier-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalDegradeBitErrorRate' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalDegradeBitErrorRate',
            False, 
            [
            _MetaInfoClassMember('signal-degrade-report', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Generate an alarm whenever the SD-BER
                threshold is crossed for this interface
                ''',
                'signal_degrade_report',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('signal-degrade-threshold', ATTRIBUTE, 'int' , None, None, 
                [(3, 12)], [], 
                '''                Set the Signal Degrade bit error rate
                threshold on an interface to a value of 10e-x,
                where x is the value passed in here
                ''',
                'signal_degrade_threshold',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-media-eth-cfg',
            'signal-degrade-bit-error-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalFailBitErrorRate' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalFailBitErrorRate',
            False, 
            [
            _MetaInfoClassMember('signal-fail-report-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable generation of an alarm whenever the
                SF-BER threshold is crossed for this interface
                ''',
                'signal_fail_report_disable',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('signal-fail-threshold', ATTRIBUTE, 'int' , None, None, 
                [(4, 12)], [], 
                '''                Set the Signal Fail bit error rate threshold
                on an interface to a value of 10e-x, where x
                is the value passed in here
                ''',
                'signal_fail_threshold',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('signal-remote-fault', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Signal a remote fault to the peer device
                whenever the link is taken down due to
                crossing the SF-BER threshold
                ''',
                'signal_remote_fault',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-media-eth-cfg',
            'signal-fail-bit-error-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ethernet' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ethernet',
            False, 
            [
            _MetaInfoClassMember('auto-negotiation', REFERENCE_ENUM_CLASS, 'EthernetAutoNegotiation_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetAutoNegotiation_Enum', 
                [], [], 
                '''                Link auto-negotiation
                ''',
                'auto_negotiation',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('carrier-delay', REFERENCE_CLASS, 'CarrierDelay' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ethernet.CarrierDelay', 
                [], [], 
                '''                Set the carrier transition delay on an
                interface in msecs
                ''',
                'carrier_delay',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('duplex', REFERENCE_ENUM_CLASS, 'EthernetDuplex_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetDuplex_Enum', 
                [], [], 
                '''                Configure duplex operational mode
                ''',
                'duplex',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('flow-control', REFERENCE_ENUM_CLASS, 'EthernetFlowCtrl_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetFlowCtrl_Enum', 
                [], [], 
                '''                Configure flow-control mode
                ''',
                'flow_control',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('forward-error-correction', REFERENCE_ENUM_CLASS, 'EthernetFec_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetFec_Enum', 
                [], [], 
                '''                Forward Error Correction
                ''',
                'forward_error_correction',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('inter-packet-gap', REFERENCE_ENUM_CLASS, 'EthernetIpg_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetIpg_Enum', 
                [], [], 
                '''                Inter-packet gap
                ''',
                'inter_packet_gap',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('loopback', REFERENCE_ENUM_CLASS, 'EthernetLoopback_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetLoopback_Enum', 
                [], [], 
                '''                Configure loopback mode
                ''',
                'loopback',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('signal-degrade-bit-error-rate', REFERENCE_CLASS, 'SignalDegradeBitErrorRate' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalDegradeBitErrorRate', 
                [], [], 
                '''                Signal Degrade Bit Error Rate handling options
                ''',
                'signal_degrade_bit_error_rate',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('signal-fail-bit-error-rate', REFERENCE_CLASS, 'SignalFailBitErrorRate' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalFailBitErrorRate', 
                [], [], 
                '''                Signal Fail Bit Error Rate handling options
                ''',
                'signal_fail_bit_error_rate',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'EthernetSpeed_Enum' , 'ydk.models.drivers.Cisco_IOS_XR_drivers_media_eth_cfg', 'EthernetSpeed_Enum', 
                [], [], 
                '''                Set the ethernet speed on an interface
                ''',
                'speed',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            ],
            'Cisco-IOS-XR-drivers-media-eth-cfg',
            'ethernet',
            _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetBng.AmbiguousEncapsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetBng.AmbiguousEncapsulation',
            False, 
            [
            _MetaInfoClassMember('additional-range1-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of first additional range for tag
                match
                ''',
                'additional_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first additional range for tag
                match
                ''',
                'additional_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of first additional range for tag
                        match
                        ''',
                        'additional_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of first additional range for tag
                        match
                        ''',
                        'additional_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range2-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of second additional range for tag
                match
                ''',
                'additional_range2_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range2-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of second additional range for tag
                match
                ''',
                'additional_range2_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range2-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of second additional range for tag
                        match
                        ''',
                        'additional_range2_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range2-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of second additional range for tag
                        match
                        ''',
                        'additional_range2_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range3-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of third additional range for tag
                match
                ''',
                'additional_range3_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range3-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of third additional range for tag
                match
                ''',
                'additional_range3_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range3-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of third additional range for tag
                        match
                        ''',
                        'additional_range3_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range3-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of third additional range for tag
                        match
                        ''',
                        'additional_range3_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range4-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of forth additional range for tag
                match
                ''',
                'additional_range4_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range4-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of forth additional range for tag
                match
                ''',
                'additional_range4_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range4-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of forth additional range for tag
                        match
                        ''',
                        'additional_range4_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range4-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of forth additional range for tag
                        match
                        ''',
                        'additional_range4_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range5-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of fifth additional range for tag
                match
                ''',
                'additional_range5_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range5-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of fifth additional range for tag
                match
                ''',
                'additional_range5_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range5-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of fifth additional range for tag
                        match
                        ''',
                        'additional_range5_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range5-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of fifth additional range for tag
                        match
                        ''',
                        'additional_range5_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range6-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of sixth additional range for tag
                match
                ''',
                'additional_range6_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range6-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of sixth additional range for tag
                match
                ''',
                'additional_range6_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range6-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of sixth additional range for tag
                        match
                        ''',
                        'additional_range6_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range6-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of sixth additional range for tag
                        match
                        ''',
                        'additional_range6_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range7-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of seventh additional range for tag
                match
                ''',
                'additional_range7_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range7-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of seventh additional range for tag
                match
                ''',
                'additional_range7_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range7-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of seventh additional range for tag
                        match
                        ''',
                        'additional_range7_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range7-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of seventh additional range for tag
                        match
                        ''',
                        'additional_range7_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range8-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of eighth additional range for tag
                match
                ''',
                'additional_range8_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range8-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of eighth additional range for tag
                match
                ''',
                'additional_range8_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range8-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of eighth additional range for tag
                        match
                        ''',
                        'additional_range8_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range8-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of eighth additional range for tag
                        match
                        ''',
                        'additional_range8_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('exact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only match packets with no more tags than
                explicitly matched
                ''',
                'exact',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ingress-destination-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Destination MAC address to match on egress
                ''',
                'ingress_destination_mac',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ingress-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address to match on ingress
                ''',
                'ingress_source_mac',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-class-of-service', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Value to match against Class Of Service bits
                for inner tag
                ''',
                'inner_class_of_service',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-range1-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of first range for inner tag match
                ''',
                'inner_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first range for inner tag match
                ''',
                'inner_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('inner-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrAny_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny_Enum', 
                        [], [], 
                        '''                        Low value of first range for inner tag match
                        ''',
                        'inner_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('inner-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 4096)], [], 
                        '''                        Low value of first range for inner tag match
                        ''',
                        'inner_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('inner-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Type of tag for inner match (if present)
                ''',
                'inner_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-class-of-service', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Value to match against Class Of Service bits
                for outer tag
                ''',
                'outer_class_of_service',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-range1-high', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                High value of first range for outer tag match
                ''',
                'outer_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('outer-range1-high', REFERENCE_ENUM_CLASS, 'VlanTagOrNative_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrNative_Enum', 
                        [], [], 
                        '''                        High value of first range for outer tag match
                        ''',
                        'outer_range1_high',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('outer-range1-high', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65535)], [], 
                        '''                        High value of first range for outer tag match
                        ''',
                        'outer_range1_high',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('outer-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first range for outer tag match
                ''',
                'outer_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('outer-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrAny_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny_Enum', 
                        [], [], 
                        '''                        Low value of first range for outer tag match
                        ''',
                        'outer_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('outer-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 4096)], [], 
                        '''                        Low value of first range for outer tag match
                        ''',
                        'outer_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('outer-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Whether to match all unmatched packets,
                untagged packets or tagged packets, and if
                matching tagged packets, the outer tag type to
                match
                ''',
                'outer_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('payload-ethertype-match', REFERENCE_ENUM_CLASS, 'EthertypeMatch_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'EthertypeMatch_Enum', 
                [], [], 
                '''                Which payload ethertype values to match
                ''',
                'payload_ethertype_match',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'ambiguous-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetBng' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetBng',
            False, 
            [
            _MetaInfoClassMember('ambiguous-encapsulation', REFERENCE_CLASS, 'AmbiguousEncapsulation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetBng.AmbiguousEncapsulation', 
                [], [], 
                '''                L3 Ambiguous encapsulation
                ''',
                'ambiguous_encapsulation',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'ethernet-bng',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp.Transmission' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp.Transmission',
            False, 
            [
            _MetaInfoClassMember('ais-interval', REFERENCE_ENUM_CLASS, 'CfmAisInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmAisInterval_Enum', 
                [], [], 
                '''                AIS Interval
                ''',
                'ais_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Class of Service bits
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'transmission',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp',
            False, 
            [
            _MetaInfoClassMember('transmission', REFERENCE_CLASS, 'Transmission' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp.Transmission', 
                [], [], 
                '''                AIS transmission configuration
                ''',
                'transmission',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'ais-up',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.LossMeasurementCounters' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.LossMeasurementCounters',
            False, 
            [
            _MetaInfoClassMember('cfg-type', REFERENCE_ENUM_CLASS, 'CfmLmCountersCfg_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg', 'CfmLmCountersCfg_Enum', 
                [], [], 
                '''                Aggregate, List, or Range
                ''',
                'cfg_type',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos0', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - start of
                range or list item
                ''',
                'cos0',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos1', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - end of
                range or list item
                ''',
                'cos1',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos2', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos2',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos3', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos3',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos4', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos4',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos5', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos5',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos6', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos6',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('cos7', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                CoS bits for per-CoS counters - list item
                ''',
                'cos7',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'loss-measurement-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.MepProperties' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.MepProperties',
            False, 
            [
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEP ID
                ''',
                'mep_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service (Maintenance Association)
                ''',
                'service',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'mep-properties',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMacAddress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMacAddress',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SLA profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('target-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Target MAC address
                ''',
                'target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'sla-profile-target-mac-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMepId' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMepId',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SLA profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('target-mep-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                Target MEP-ID
                ''',
                'target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'sla-profile-target-mep-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds',
            False, 
            [
            _MetaInfoClassMember('sla-profile-target-mac-address', REFERENCE_LIST, 'SlaProfileTargetMacAddress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMacAddress', 
                [], [], 
                '''                Configuration for a particular SLA
                operation
                ''',
                'sla_profile_target_mac_address',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('sla-profile-target-mep-id', REFERENCE_LIST, 'SlaProfileTargetMepId' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMepId', 
                [], [], 
                '''                Configuration for a particular SLA
                operation
                ''',
                'sla_profile_target_mep_id',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'sla-profile-target-mep-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Class of Service bits for this MEP
                ''',
                'cos',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('loss-measurement-counters', REFERENCE_CLASS, 'LossMeasurementCounters' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.LossMeasurementCounters', 
                [], [], 
                '''                Loss-measurement specific configuration
                ''',
                'loss_measurement_counters',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('mep-properties', REFERENCE_CLASS, 'MepProperties' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.MepProperties', 
                [], [], 
                '''                Properties for this MEP
                ''',
                'mep_properties',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('sla-profile-target-mep-ids', REFERENCE_CLASS, 'SlaProfileTargetMepIds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds', 
                [], [], 
                '''                SLA specific configuration
                ''',
                'sla_profile_target_mep_ids',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'mep',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain',
            False, 
            [
            _MetaInfoClassMember('domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-cfg', True),
            _MetaInfoClassMember('mep', REFERENCE_CLASS, 'Mep' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep', 
                [], [], 
                '''                MEP Configuration
                ''',
                'mep',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains',
            False, 
            [
            _MetaInfoClassMember('domain', REFERENCE_LIST, 'Domain' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain', 
                [], [], 
                '''                Configuration for a particular Maintenance
                Domain
                ''',
                'domain',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'domains',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm',
            False, 
            [
            _MetaInfoClassMember('ais-up', REFERENCE_CLASS, 'AisUp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp', 
                [], [], 
                '''                Interface specific AIS configuration
                ''',
                'ais_up',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('domains', REFERENCE_CLASS, 'Domains' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains', 
                [], [], 
                '''                Domain-specific interface configuration
                ''',
                'domains',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cfm',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.Action' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.Action',
            False, 
            [
            _MetaInfoClassMember('capabilities-conflict', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd_Enum', 
                [], [], 
                '''                Action to perform when a capabilities conflict
                occurs
                ''',
                'capabilities_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('critical-event', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum_Enum', 
                [], [], 
                '''                Action to perform when a critical event occurs
                ''',
                'critical_event',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('discovery-timeout', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd_Enum', 
                [], [], 
                '''                Action to perform when discovery timeout
                occurs
                ''',
                'discovery_timeout',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('dying-gasp', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum_Enum', 
                [], [], 
                '''                Action to perform when a dying gasp occurs
                ''',
                'dying_gasp',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('high-threshold', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnum_Enum', 
                [], [], 
                '''                Action to perform when a high-threshold event
                occurs
                ''',
                'high_threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('link-fault', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd_Enum', 
                [], [], 
                '''                Action to perform when a link fault occurs
                ''',
                'link_fault',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionPrimEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum_Enum', 
                [], [], 
                '''                Action to perform when remote loopback is
                entered or exited
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('session-down', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd_Enum', 
                [], [], 
                '''                Action to perform when a session comes down
                ''',
                'session_down',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('session-up', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionPrimEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionPrimEnum_Enum', 
                [], [], 
                '''                Action to perform when a session comes up
                ''',
                'session_up',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('wiring-conflict', REFERENCE_ENUM_CLASS, 'EtherLinkOamEventActionEnumEfd_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamEventActionEnumEfd_Enum', 
                [], [], 
                '''                Action to perform when a wiring conflict
                occurs
                ''',
                'wiring_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'action',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame.Threshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame.Threshold',
            False, 
            [
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 12000000)], [], 
                '''                The high threshold for frame events
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(1, 12000000)], [], 
                '''                The low threshold for frame events
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame.Threshold', 
                [], [], 
                '''                Threshold configuration for frame events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int' , None, None, 
                [(1000, 60000)], [], 
                '''                Window size configuration for frame events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod.Threshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod.Threshold',
            False, 
            [
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000000)], [], 
                '''                The high threshold for frame-period events
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000000)], [], 
                '''                The low threshold for frame-period events
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod.Threshold', 
                [], [], 
                '''                Threshold for frame-period events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int' , None, None, 
                [(100, 60000)], [], 
                '''                Window size configuration for frame-period
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame-period',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds.Threshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds.Threshold',
            False, 
            [
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 900)], [], 
                '''                The high threshold for frame-seconds
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(1, 900)], [], 
                '''                The low threshold for frame-seconds
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds.Threshold', 
                [], [], 
                '''                Threshold for frame-seconds events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int' , None, None, 
                [(10000, 900000)], [], 
                '''                Window size configuration for frame-seconds
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'frame-seconds',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod.Threshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod.Threshold',
            False, 
            [
            _MetaInfoClassMember('threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 60000000)], [], 
                '''                The high threshold for symbol-period
                ''',
                'threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(1, 60000000)], [], 
                '''                The low threshold for symbol-period
                ''',
                'threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod.Threshold', 
                [], [], 
                '''                Threshold configuration for symbol-period
                events
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int' , None, None, 
                [(1000, 60000)], [], 
                '''                Window size configuration for symbol-period
                events
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'symbol-period',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor',
            False, 
            [
            _MetaInfoClassMember('frame', REFERENCE_CLASS, 'Frame' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame', 
                [], [], 
                '''                Frame event configuration
                ''',
                'frame',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('frame-period', REFERENCE_CLASS, 'FramePeriod' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod', 
                [], [], 
                '''                Frame-period event configuration
                ''',
                'frame_period',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('frame-seconds', REFERENCE_CLASS, 'FrameSeconds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds', 
                [], [], 
                '''                Frame-seconds event configuration
                ''',
                'frame_seconds',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('monitoring', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable monitoring
                ''',
                'monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('symbol-period', REFERENCE_CLASS, 'SymbolPeriod' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod', 
                [], [], 
                '''                Symbol-period event configuration
                ''',
                'symbol_period',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'link-monitor',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.RequireRemote' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.RequireRemote',
            False, 
            [
            _MetaInfoClassMember('link-monitoring', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable link monitoring peer
                requirement
                ''',
                'link_monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mib-retrieval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable MIB retrieval peer
                requirement
                ''',
                'mib_retrieval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'EtherLinkOamInterfaceRequireModeEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamInterfaceRequireModeEnum_Enum', 
                [], [], 
                '''                Possible required peer modes
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable remote loopback peer
                requirement
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'require-remote',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_CLASS, 'Action' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.Action', 
                [], [], 
                '''                Configure action parameters
                ''',
                'action',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('hello-interval', REFERENCE_ENUM_CLASS, 'EtherLinkOamInterfaceHelloIntervalEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamInterfaceHelloIntervalEnum_Enum', 
                [], [], 
                '''                Possible Ethernet Link OAM hello intervals
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('link-monitor', REFERENCE_CLASS, 'LinkMonitor' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor', 
                [], [], 
                '''                Configure link monitor parameters
                ''',
                'link_monitor',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mib-retrieval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable MIB retrieval
                ''',
                'mib_retrieval',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'EtherLinkOamInterfaceModeEnum_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg', 'EtherLinkOamInterfaceModeEnum_Enum', 
                [], [], 
                '''                Possible Ethernet Link OAM modes
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set the profile to use on the interface
                ''',
                'profile_name',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('remote-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable remote loopback
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('require-remote', REFERENCE_CLASS, 'RequireRemote' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.RequireRemote', 
                [], [], 
                '''                Configure remote requirement parameters
                ''',
                'require_remote',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(2, 30)], [], 
                '''                Connection timeout period in number of lost
                heartbeats
                ''',
                'timeout',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('udlf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable uni-directional link-fault
                detection
                ''',
                'udlf',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'ether-link-oam',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures',
            False, 
            [
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm', 
                [], [], 
                '''                CFM interface configuration
                ''',
                'cfm',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('ether-link-oam', REFERENCE_CLASS, 'EtherLinkOam' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam', 
                [], [], 
                '''                Ethernet Link OAM Interface Configuration
                ''',
                'ether_link_oam',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('ether-link-oam-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Ethernet Link OAM on the interface
                ''',
                'ether_link_oam_enable',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('filtering', REFERENCE_ENUM_CLASS, 'Filtering_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg', 'Filtering_Enum', 
                [], [], 
                '''                Ingress Ethernet frame filtering
                ''',
                'filtering',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'ethernet-features',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetService.Encapsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetService.Encapsulation',
            False, 
            [
            _MetaInfoClassMember('additional-range1-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of first additional range for tag
                match
                ''',
                'additional_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first additional range for tag
                match
                ''',
                'additional_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of first additional range for tag
                        match
                        ''',
                        'additional_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of first additional range for tag
                        match
                        ''',
                        'additional_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range2-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of second additional range for tag
                match
                ''',
                'additional_range2_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range2-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of second additional range for tag
                match
                ''',
                'additional_range2_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range2-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of second additional range for tag
                        match
                        ''',
                        'additional_range2_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range2-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of second additional range for tag
                        match
                        ''',
                        'additional_range2_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range3-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of third additional range for tag
                match
                ''',
                'additional_range3_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range3-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of third additional range for tag
                match
                ''',
                'additional_range3_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range3-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of third additional range for tag
                        match
                        ''',
                        'additional_range3_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range3-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of third additional range for tag
                        match
                        ''',
                        'additional_range3_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range4-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of forth additional range for tag
                match
                ''',
                'additional_range4_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range4-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of forth additional range for tag
                match
                ''',
                'additional_range4_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range4-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of forth additional range for tag
                        match
                        ''',
                        'additional_range4_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range4-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of forth additional range for tag
                        match
                        ''',
                        'additional_range4_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range5-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of fifth additional range for tag
                match
                ''',
                'additional_range5_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range5-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of fifth additional range for tag
                match
                ''',
                'additional_range5_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range5-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of fifth additional range for tag
                        match
                        ''',
                        'additional_range5_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range5-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of fifth additional range for tag
                        match
                        ''',
                        'additional_range5_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range6-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of sixth additional range for tag
                match
                ''',
                'additional_range6_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range6-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of sixth additional range for tag
                match
                ''',
                'additional_range6_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range6-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of sixth additional range for tag
                        match
                        ''',
                        'additional_range6_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range6-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of sixth additional range for tag
                        match
                        ''',
                        'additional_range6_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range7-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of seventh additional range for tag
                match
                ''',
                'additional_range7_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range7-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of seventh additional range for tag
                match
                ''',
                'additional_range7_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range7-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of seventh additional range for tag
                        match
                        ''',
                        'additional_range7_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range7-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of seventh additional range for tag
                        match
                        ''',
                        'additional_range7_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('additional-range8-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of eighth additional range for tag
                match
                ''',
                'additional_range8_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('additional-range8-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of eighth additional range for tag
                match
                ''',
                'additional_range8_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('additional-range8-low', REFERENCE_ENUM_CLASS, 'VlanTagOrCvp_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrCvp_Enum', 
                        [], [], 
                        '''                        Low value of eighth additional range for tag
                        match
                        ''',
                        'additional_range8_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('additional-range8-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65534)], [], 
                        '''                        Low value of eighth additional range for tag
                        match
                        ''',
                        'additional_range8_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('exact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only match packets with no more tags than
                explicitly matched
                ''',
                'exact',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ingress-destination-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Destination MAC address to match on egress
                ''',
                'ingress_destination_mac',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ingress-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC address to match on ingress
                ''',
                'ingress_source_mac',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-class-of-service', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Value to match against Class Of Service bits
                for inner tag
                ''',
                'inner_class_of_service',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-range1-high', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                High value of first range for inner tag match
                ''',
                'inner_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first range for inner tag match
                ''',
                'inner_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('inner-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrAny_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny_Enum', 
                        [], [], 
                        '''                        Low value of first range for inner tag match
                        ''',
                        'inner_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('inner-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 4096)], [], 
                        '''                        Low value of first range for inner tag match
                        ''',
                        'inner_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('inner-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Type of tag for inner match (if present)
                ''',
                'inner_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-class-of-service', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Value to match against Class Of Service bits
                for outer tag
                ''',
                'outer_class_of_service',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-range1-high', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                High value of first range for outer tag match
                ''',
                'outer_range1_high',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('outer-range1-high', REFERENCE_ENUM_CLASS, 'VlanTagOrNative_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrNative_Enum', 
                        [], [], 
                        '''                        High value of first range for outer tag match
                        ''',
                        'outer_range1_high',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('outer-range1-high', ATTRIBUTE, 'int' , None, None, 
                        [(1, 65535)], [], 
                        '''                        High value of first range for outer tag match
                        ''',
                        'outer_range1_high',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('outer-range1-low', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Low value of first range for outer tag match
                ''',
                'outer_range1_low',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('outer-range1-low', REFERENCE_ENUM_CLASS, 'VlanTagOrAny_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAny_Enum', 
                        [], [], 
                        '''                        Low value of first range for outer tag match
                        ''',
                        'outer_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('outer-range1-low', ATTRIBUTE, 'int' , None, None, 
                        [(1, 4096)], [], 
                        '''                        Low value of first range for outer tag match
                        ''',
                        'outer_range1_low',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('outer-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Whether to match all unmatched packets,
                untagged packets or tagged packets, and if
                matching tagged packets, the outer tag type to
                match
                ''',
                'outer_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('payload-ethertype-match', REFERENCE_ENUM_CLASS, 'EthertypeMatch_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'EthertypeMatch_Enum', 
                [], [], 
                '''                Which payload ethertype values to match
                ''',
                'payload_ethertype_match',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetService.LocalTrafficDefaultEncapsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetService.LocalTrafficDefaultEncapsulation',
            False, 
            [
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                Optional VLAN Id for inner Dot1Q tag
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-tag-type', REFERENCE_ENUM_CLASS, 'Vlan_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Vlan_Enum', 
                [], [], 
                '''                Type of outer tag
                ''',
                'outer_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                VLAN id for outer tag
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'local-traffic-default-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetService.Rewrite' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetService.Rewrite',
            False, 
            [
            _MetaInfoClassMember('inner-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Type of innermost tag to be pushed
                ''',
                'inner_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('inner-tag-value', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                VLAN Id of innermost tag to be pushed
                ''',
                'inner_tag_value',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-tag-type', REFERENCE_ENUM_CLASS, 'Match_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Match_Enum', 
                [], [], 
                '''                Type of outermost tag to be pushed
                ''',
                'outer_tag_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('outer-tag-value', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                VLAN Id of outermost tag to be pushed
                ''',
                'outer_tag_value',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('rewrite-type', REFERENCE_ENUM_CLASS, 'Rewrite_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Rewrite_Enum', 
                [], [], 
                '''                The type of rewrite to perform
                ''',
                'rewrite_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'rewrite',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.EthernetService' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.EthernetService',
            False, 
            [
            _MetaInfoClassMember('encapsulation', REFERENCE_CLASS, 'Encapsulation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetService.Encapsulation', 
                [], [], 
                '''                The encapsulation of this Ethernet service
                ''',
                'encapsulation',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('local-traffic-default-encapsulation', REFERENCE_CLASS, 'LocalTrafficDefaultEncapsulation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetService.LocalTrafficDefaultEncapsulation', 
                [], [], 
                '''                The default encapsulation to be used for
                locally-sourced packets
                ''',
                'local_traffic_default_encapsulation',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('rewrite', REFERENCE_CLASS, 'Rewrite' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetService.Rewrite', 
                [], [], 
                '''                The rewrite operation for the Ethernet service
                ''',
                'rewrite',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'ethernet-service',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Primary' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Primary',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                RouteTag
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'primary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries.Secondary' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries.Secondary',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-io-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                RouteTag
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'secondary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries',
            False, 
            [
            _MetaInfoClassMember('secondary', REFERENCE_LIST, 'Secondary' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries.Secondary', 
                [], [], 
                '''                IP address and Mask
                ''',
                'secondary',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'secondaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses',
            False, 
            [
            _MetaInfoClassMember('dhcp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                IPv4 address and Mask negotiated via DHCP
                ''',
                'dhcp',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('primary', REFERENCE_CLASS, 'Primary' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Primary', 
                [], [], 
                '''                IP address and Mask
                ''',
                'primary',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('secondaries', REFERENCE_CLASS, 'Secondaries' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries', 
                [], [], 
                '''                Specify a secondary address
                ''',
                'secondaries',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Enable IP processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag.FlowTagInput' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag.FlowTagInput',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FlowTag configuration on destination
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FlowTag configuration on source
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'flow-tag-input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag',
            False, 
            [
            _MetaInfoClassMember('flow-tag-input', REFERENCE_CLASS, 'FlowTagInput' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag.FlowTagInput', 
                [], [], 
                '''                Input
                ''',
                'flow_tag_input',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'flow-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb.Input',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_ENUM_CLASS, 'Ipv4InterfaceQppb_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4InterfaceQppb_Enum', 
                [], [], 
                '''                QPPB configuration on destination
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'Ipv4InterfaceQppb_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4InterfaceQppb_Enum', 
                [], [], 
                '''                QPPB configuration on source
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb.Input', 
                [], [], 
                '''                Input
                ''',
                'input',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'qppb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp',
            False, 
            [
            _MetaInfoClassMember('flow-tag', REFERENCE_CLASS, 'FlowTag' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag', 
                [], [], 
                '''                Interface ipv4 bgp policy propagation flow tag
                configuration
                ''',
                'flow_tag',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('qppb', REFERENCE_CLASS, 'Qppb' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb', 
                [], [], 
                '''                Interface ipv4 bgp policy propagation
                configuration
                ''',
                'qppb',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Input' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Input',
            False, 
            [
            _MetaInfoClassMember('destination-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configuration on destination
                ''',
                'destination_accounting',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('source-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configuration on source
                ''',
                'source_accounting',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Output' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Output',
            False, 
            [
            _MetaInfoClassMember('destination-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configuration on destination
                ''',
                'destination_accounting',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('source-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configuration on source
                ''',
                'source_accounting',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Input', 
                [], [], 
                '''                Input
                ''',
                'input',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Output', 
                [], [], 
                '''                Output
                ''',
                'output',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'bgp-pa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP destination address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-io-cfg', True),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-io-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses.HelperAddress', 
                [], [], 
                '''                An IP destination addresses for UDP broadcasts
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Verify' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Verify',
            False, 
            [
            _MetaInfoClassMember('default-ping', REFERENCE_ENUM_CLASS, 'Ipv4DefaultPing_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4DefaultPing_Enum', 
                [], [], 
                '''                Allow default route to match when checking
                source address
                ''',
                'default_ping',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('reachable', REFERENCE_ENUM_CLASS, 'Ipv4Reachable_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4Reachable_Enum', 
                [], [], 
                '''                Source is reachable via any interface or
                interface on which packet was received
                ''',
                'reachable',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('self-ping', REFERENCE_ENUM_CLASS, 'Ipv4SelfPing_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_io_cfg', 'Ipv4SelfPing_Enum', 
                [], [], 
                '''                Allow router to ping itself (opens
                vulnerability in verification)
                ''',
                'self_ping',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'verify',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4Network',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses', 
                [], [], 
                '''                Set the IP address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp', 
                [], [], 
                '''                Interface ipv4 bgp configuration
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('bgp-pa', REFERENCE_CLASS, 'BgpPa' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa', 
                [], [], 
                '''                Interface ipv4 bgp configuration
                ''',
                'bgp_pa',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses', 
                [], [], 
                '''                The set of IP destination addresses for UDP
                broadcasts
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('icmp-mask-reply', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The flag for enabling sending of ICMP mask
                reply messages
                ''',
                'icmp_mask_reply',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [(68, 65535)], [], 
                '''                The IP Maximum Transmission Unit
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('point-to-point', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable point-to-point handling for this
                interface.
                ''',
                'point_to_point',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('tcp-mss-adjust-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable TCP MSS Adjust on an interface
                ''',
                'tcp_mss_adjust_enable',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('ttl-propagate-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable TTL propagate on an interface
                ''',
                'ttl_propagate_disable',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('verify', REFERENCE_CLASS, 'Verify' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Verify', 
                [], [], 
                '''                Enable Verify handling for this interface
                ''',
                'verify',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'ipv4-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4NetworkForwarding' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4NetworkForwarding',
            False, 
            [
            _MetaInfoClassMember('directed-broadcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable forwarding of directed broadcast
                ''',
                'directed_broadcast',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('redirects', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sending ICMP Redirect messages
                ''',
                'redirects',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable sending ICMP unreachables
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-io-cfg',
            'ipv4-network-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('acl-name-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Array of IPv4 Packet Filter Names to be
                applied to Inbound packets
                ''',
                'acl_name_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv4
                Packet Filter Name to be applied to Inbound
                packets, ACL providing HW optimization when
                applied on multiple interfaces. NOTE: This
                parameter is mandatory if 'Name' is not
                specified.
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('compression-level', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                The level of compression applied to the ACL on
                this interface. The range is 0 to 3 with
                default being no compression (0).
                ''',
                'compression_level',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in the hardware.  The default is not
                to count them. NOTE: HardwareCount is allowed
                only if Name is specified.
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in hardware per interface.The default
                is not to count them. NOTE:
                InterfaceStatistics is allowed only if Name is
                specified.
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('is-common-array', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Array of CommonACL flags for each ACL. TRUE
                indicates HW optimization on multiple
                interfaces is provided
                ''',
                'is_common_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv4
                Packet Filter Name to be applied to Inbound
                packets NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('acl-name-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Array of IPv4 Packet Filter Names to be
                applied to Outbound packets
                ''',
                'acl_name_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('compression-level', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                The level of compression applied to the ACL on
                this interface. The range is 0 to 3 with
                default being no compression (0).
                ''',
                'compression_level',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('do-not-use', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved.  Error if specified.
                ''',
                'do_not_use',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('hardware-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in the hardware.  The default is not
                to count them.
                ''',
                'hardware_count',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in hardware per interface.The default
                is not to count them.
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('is-common-array', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Array of CommonACL flags for each ACL. TRUE
                indicates HW optimization on multiple
                interfaces is provided
                ''',
                'is_common_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv4
                Packet Filter Name to be applied to Outbound
                packets NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Inbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Outbound', 
                [], [], 
                '''                IPv4 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'ipv4-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv4arp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv4arp',
            False, 
            [
            _MetaInfoClassMember('gratuitous-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore the receipt of Gratuitous ARP packets on
                the interface
                ''',
                'gratuitous_ignore',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('learning-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable the dynamic learning of ARP entries on
                the interface
                ''',
                'learning_disable',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('learning-local', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the dynamic learning of ARP entries(for
                local subnet) on the interface
                ''',
                'learning_local',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('local-proxy-arp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Local Proxy ARP configuration
                ''',
                'local_proxy_arp',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('proxy-arp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Proxy ARP configuration
                ''',
                'proxy_arp',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('purge-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time to delay purging arp entries when the
                interface goes down
                ''',
                'purge_delay',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(30, 2144448000)], [], 
                '''                Number of seconds for ARP cache timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'ipv4arp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.DuplicateAddressDetection' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.DuplicateAddressDetection',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [(0, 600)], [], 
                '''                Set IPv6 duplicate address detection transmits
                ''',
                'attempts',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'duplicate-address-detection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes.Ipv6Prefix' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes.Ipv6Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-nd-cfg', True),
            _MetaInfoClassMember('expiry-date', ATTRIBUTE, 'int' , None, None, 
                [(1, 31)], [], 
                '''                Date to expire valid lifetime
                ''',
                'expiry_date',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('expiry-hour', ATTRIBUTE, 'int' , None, None, 
                [(0, 23)], [], 
                '''                Hour to expire valid lifetime
                ''',
                'expiry_hour',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('expiry-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 59)], [], 
                '''                Minute to expire valid lifetime
                ''',
                'expiry_minute',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('expiry-month', REFERENCE_ENUM_CLASS, 'Ipv6ndMonth_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6ndMonth_Enum', 
                [], [], 
                '''                Month to expire valid lifetime
                ''',
                'expiry_month',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('expiry-year', ATTRIBUTE, 'int' , None, None, 
                [(2003, 2035)], [], 
                '''                Year to expire valid lifetime
                ''',
                'expiry_year',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('no-advertize', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set, prefix will not be advertized
                ''',
                'no_advertize',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('no-auto-config', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set, prefix will not be used for auto
                configuration
                ''',
                'no_auto_config',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('off-link', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set, prefix will not be used for onlink
                determination
                ''',
                'off_link',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('pref-expiry-date', ATTRIBUTE, 'int' , None, None, 
                [(1, 31)], [], 
                '''                Date to expire preferred lifetime
                ''',
                'pref_expiry_date',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('pref-expiry-hour', ATTRIBUTE, 'int' , None, None, 
                [(0, 23)], [], 
                '''                Hour to expire preferred lifetime
                ''',
                'pref_expiry_hour',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('pref-expiry-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 59)], [], 
                '''                Minute to expire preferred lifetime
                ''',
                'pref_expiry_minute',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('pref-expiry-month', REFERENCE_ENUM_CLASS, 'Ipv6ndMonth_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6ndMonth_Enum', 
                [], [], 
                '''                Month to expire preferred lifetime
                ''',
                'pref_expiry_month',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('pref-expiry-year', ATTRIBUTE, 'int' , None, None, 
                [(2003, 2035)], [], 
                '''                Year to expire preferred lifetime
                ''',
                'pref_expiry_year',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('preferred-lifetime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Preferred Lifetime (seconds) must be <= Valid
                Lifetime
                ''',
                'preferred_lifetime',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                Prefix mask length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('prefix-zone', ATTRIBUTE, 'str' , None, None, 
                [(0, 9)], [], 
                '''                Prefix zone
                ''',
                'prefix_zone',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('valid-lifetime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Valid Lifetime (seconds)
                ''',
                'valid_lifetime',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ipv6-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes',
            False, 
            [
            _MetaInfoClassMember('ipv6-prefix', REFERENCE_LIST, 'Ipv6Prefix' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes.Ipv6Prefix', 
                [], [], 
                '''                Configure prefix with paramemters
                ''',
                'ipv6_prefix',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ipv6-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.RaInterval' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.RaInterval',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(4, 1800)], [], 
                '''                Maximum RA interval in seconds
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(3, 1800)], [], 
                '''                Minimum RA interval in seconds
                ''',
                'minimum',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ra-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor',
            False, 
            [
            _MetaInfoClassMember('cache-limit', ATTRIBUTE, 'int' , None, None, 
                [(0, 128000)], [], 
                '''                Set the cache limit for neighbor entries
                ''',
                'cache_limit',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('duplicate-address-detection', REFERENCE_CLASS, 'DuplicateAddressDetection' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.DuplicateAddressDetection', 
                [], [], 
                '''                Duplicate Address Detection (DAD)
                ''',
                'duplicate_address_detection',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ipv6-prefixes', REFERENCE_CLASS, 'Ipv6Prefixes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes', 
                [], [], 
                '''                Prefixes 
                ''',
                'ipv6_prefixes',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('managed-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for address
                configuration
                ''',
                'managed_config',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ns-interval', ATTRIBUTE, 'int' , None, None, 
                [(1000, 4294967295)], [], 
                '''                Set advertised NS retransmission interval in
                milliseconds
                ''',
                'ns_interval',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('other-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Host to use stateful protocol for non-address
                configuration
                ''',
                'other_config',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ra-interval', REFERENCE_CLASS, 'RaInterval' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.RaInterval', 
                [], [], 
                '''                Set IPv6 Router Advertisement (RA) interval in
                seconds
                ''',
                'ra_interval',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ra-lifetime', ATTRIBUTE, 'int' , None, None, 
                [(0, 9000)], [], 
                '''                Set IPv6 Router Advertisement (RA) lifetime in
                seconds
                ''',
                'ra_lifetime',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ra-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable suppress IPv6 router advertisement
                ''',
                'ra_suppress',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ra-unspecify-hoplimit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unspecify IPv6 Router Advertisement (RA)
                hop-limit
                ''',
                'ra_unspecify_hoplimit',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ramtu-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable suppress MTU in IPv6 router
                advertisement
                ''',
                'ramtu_suppress',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('reachable-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 3600000)], [], 
                '''                Set advertised reachability time in
                milliseconds
                ''',
                'reachable_time',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('redirect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sending of ICMP Redirect messages
                ''',
                'redirect',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('router-preference', REFERENCE_ENUM_CLASS, 'Ipv6NdRouterPref_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6NdRouterPref_Enum', 
                [], [], 
                '''                RA Router Preference
                ''',
                'router_preference',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('srp-multicast-encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6srpEncapsulation_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6srpEncapsulation_Enum', 
                [], [], 
                '''                Set SRP multicast prefer encapsulation
                ''',
                'srp_multicast_encapsulation',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('srp-unicast-encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6srpEncapsulation_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6srpEncapsulation_Enum', 
                [], [], 
                '''                Set SRP unicast prefer encapsulation
                ''',
                'srp_unicast_encapsulation',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ipv6-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.AutoConfiguration' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.AutoConfiguration',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The flag to enable auto ipv6 interface
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'auto-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses.Eui64Address' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses.Eui64Address',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                RouteTag
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 address zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'eui64-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses',
            False, 
            [
            _MetaInfoClassMember('eui64-address', REFERENCE_LIST, 'Eui64Address' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses.Eui64Address', 
                [], [], 
                '''                EUI-64 IPv6 address
                ''',
                'eui64_address',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'eui64-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.LinkLocalAddress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.LinkLocalAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-cfg', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', False),
                ]),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                RouteTag
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 address zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'link-local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses.RegularAddress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses.RegularAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv6-ma-cfg', True),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                RouteTag
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 address zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'regular-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses',
            False, 
            [
            _MetaInfoClassMember('regular-address', REFERENCE_LIST, 'RegularAddress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses.RegularAddress', 
                [], [], 
                '''                Regular IPv6 address
                ''',
                'regular_address',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'regular-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses',
            False, 
            [
            _MetaInfoClassMember('auto-configuration', REFERENCE_CLASS, 'AutoConfiguration' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.AutoConfiguration', 
                [], [], 
                '''                Auto IPv6 Interface Configuration
                ''',
                'auto_configuration',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('eui64-addresses', REFERENCE_CLASS, 'Eui64Addresses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses', 
                [], [], 
                '''                EUI-64 IPv6 address Table
                ''',
                'eui64_addresses',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('link-local-address', REFERENCE_CLASS, 'LinkLocalAddress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.LinkLocalAddress', 
                [], [], 
                '''                Link local IPv6 address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('regular-addresses', REFERENCE_CLASS, 'RegularAddresses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses', 
                [], [], 
                '''                Regular IPv6 address Table
                ''',
                'regular_addresses',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable.BgpFlowTagPolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable.BgpFlowTagPolicy',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Tag configuration on destination
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Tag configuration on source
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'bgp-flow-tag-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable',
            False, 
            [
            _MetaInfoClassMember('bgp-flow-tag-policy', REFERENCE_CLASS, 'BgpFlowTagPolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable.BgpFlowTagPolicy', 
                [], [], 
                '''                Input
                ''',
                'bgp_flow_tag_policy',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'bgp-flow-tag-policy-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings.BgpPolicyAccounting' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings.BgpPolicyAccounting',
            False, 
            [
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Accouting on input or output
                ''',
                'direction',
                'Cisco-IOS-XR-ipv6-ma-cfg', True),
            _MetaInfoClassMember('destination-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accounting on Destination IP Address
                ''',
                'destination_accounting',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('source-accounting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accounting on Source IP Address
                ''',
                'source_accounting',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'bgp-policy-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings',
            False, 
            [
            _MetaInfoClassMember('bgp-policy-accounting', REFERENCE_LIST, 'BgpPolicyAccounting' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings.BgpPolicyAccounting', 
                [], [], 
                '''                Accounting input or output
                ''',
                'bgp_policy_accounting',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'bgp-policy-accountings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpQosPolicyPropagation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpQosPolicyPropagation',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_ENUM_CLASS, 'Ipv6Qppb_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6Qppb_Enum', 
                [], [], 
                '''                QPPB configuration on destination
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'Ipv6Qppb_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6Qppb_Enum', 
                [], [], 
                '''                QPPB configuration on source
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'bgp-qos-policy-propagation',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters.MacAddressFilter' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters.MacAddressFilter',
            False, 
            [
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Multicast Address
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ipv6-ma-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'mac-address-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters',
            False, 
            [
            _MetaInfoClassMember('mac-address-filter', REFERENCE_LIST, 'MacAddressFilter' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters.MacAddressFilter', 
                [], [], 
                '''                Allow IPv6 Mac-Filter for a multicast address
                ''',
                'mac_address_filter',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'mac-address-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Verify' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Verify',
            False, 
            [
            _MetaInfoClassMember('default-ping', REFERENCE_ENUM_CLASS, 'Ipv6DefaultPing_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6DefaultPing_Enum', 
                [], [], 
                '''                Allow Default Route
                ''',
                'default_ping',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('reachable', REFERENCE_ENUM_CLASS, 'Ipv6Reachable_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6Reachable_Enum', 
                [], [], 
                '''                Source Reachable Interface
                ''',
                'reachable',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('self-ping', REFERENCE_ENUM_CLASS, 'Ipv6SelfPing_Enum' , 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_ma_cfg', 'Ipv6SelfPing_Enum', 
                [], [], 
                '''                Allow Self Ping
                ''',
                'self_ping',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'verify',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6Network',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses', 
                [], [], 
                '''                Set the IPv6 address of an interface
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('bgp-flow-tag-policy-table', REFERENCE_CLASS, 'BgpFlowTagPolicyTable' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable', 
                [], [], 
                '''                Interface ipv6 bgp policy propagation flowtag
                configuration
                ''',
                'bgp_flow_tag_policy_table',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('bgp-policy-accountings', REFERENCE_CLASS, 'BgpPolicyAccountings' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings', 
                [], [], 
                '''                IPv6 BGP Policy Accounting
                ''',
                'bgp_policy_accountings',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('bgp-qos-policy-propagation', REFERENCE_CLASS, 'BgpQosPolicyPropagation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpQosPolicyPropagation', 
                [], [], 
                '''                Configure BGP QoS policy propagation
                ''',
                'bgp_qos_policy_propagation',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('mac-address-filters', REFERENCE_CLASS, 'MacAddressFilters' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters', 
                [], [], 
                '''                IPv6 Mac-Filter for a multicast address
                ''',
                'mac_address_filters',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [(1280, 65535)], [], 
                '''                MTU Setting of Interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('tcp-mss-adjust-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable TCP MSS adjust on an interface
                ''',
                'tcp_mss_adjust_enable',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('ttl-propagate-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disabled TTL propagate on an interface
                ''',
                'ttl_propagate_disable',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Enable IPv6 processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Override Sending of ICMP Unreachable Messages
                ''',
                'unreachables',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('verify', REFERENCE_CLASS, 'Verify' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Verify', 
                [], [], 
                '''                IPv6 Verify Unicast Souce Reachable
                ''',
                'verify',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-cfg',
            'ipv6-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Inbound' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Inbound',
            False, 
            [
            _MetaInfoClassMember('acl-name-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Array of IPv6 Packet Filter Names to be
                applied to Inbound packets
                ''',
                'acl_name_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('common-acl-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv6
                Packet Filter Name to be applied to Inbound
                packets, ACL providing HW optimization when
                applied on multiple interfaces. NOTE: This
                parameter is mandatory if 'Name' is not
                specified.
                ''',
                'common_acl_name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('compression-level', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                The level of compression applied to the ACL on
                this interface. The range is 0 to 3 with
                default being no compression (0).
                ''',
                'compression_level',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in hardware per interface.The default
                is not to count them. NOTE:
                InterfaceStatistics is allowed only if Name is
                specified.
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('is-common-array', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Array of CommonACL flags for each ACL. TRUE
                indicates HW optimization on multiple
                interfaces is provided
                ''',
                'is_common_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv6
                Packet Filter Name to be applied to Inbound 
                NOTE: This parameter is mandatory if
                'CommonACLName' is not specified.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Outbound' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Outbound',
            False, 
            [
            _MetaInfoClassMember('acl-name-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Array of IPv6 Packet Filter Names to be
                applied to Inbound packets
                ''',
                'acl_name_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('compression-level', ATTRIBUTE, 'int' , None, None, 
                [(0, 3)], [], 
                '''                The level of compression applied to the ACL on
                this interface. The range is 0 to 3 with
                default being no compression (0).
                ''',
                'compression_level',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('do-not-use', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved.  Error if specified.
                ''',
                'do_not_use',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('interface-statistics', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True if packets hitting the ACL should be
                counted in hardware per interface.The default
                is not to count them.
                ''',
                'interface_statistics',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('is-common-array', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Array of CommonACL flags for each ACL. TRUE
                indicates HW optimization on multiple
                interfaces is provided
                ''',
                'is_common_array',
                'Cisco-IOS-XR-ip-pfilter-cfg', False, max_elements=5),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Reserved for backward compatibility. IPv6
                Packet Filter Name to be applied to Outbound 
                packets.
                ''',
                'name',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'outbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter',
            False, 
            [
            _MetaInfoClassMember('inbound', REFERENCE_CLASS, 'Inbound' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Inbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to inbound
                packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('outbound', REFERENCE_CLASS, 'Outbound' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Outbound', 
                [], [], 
                '''                IPv6 Packet filter to be applied to outbound
                packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-cfg',
            'ipv6-packet-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters.CellPacking' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters.CellPacking',
            False, 
            [
            _MetaInfoClassMember('cell-packing-timer-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 3)], [], 
                '''                Which cell packing timer to use
                ''',
                'cell_packing_timer_id',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('maximum-cells-packed', ATTRIBUTE, 'int' , None, None, 
                [(2, 255)], [], 
                '''                Maximum number of cells to be packed in a
                packet
                ''',
                'maximum_cells_packed',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'cell-packing',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters',
            False, 
            [
            _MetaInfoClassMember('cell-packing', REFERENCE_CLASS, 'CellPacking' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters.CellPacking', 
                [], [], 
                '''                Configure cell-packing parameters.  All
                parameters are mandatory.
                ''',
                'cell_packing',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            ],
            'Cisco-IOS-XR-atm-vcm-cfg',
            'atm-port-mode-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2EthernetFeatures' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2EthernetFeatures',
            False, 
            [
            _MetaInfoClassMember('egress-filtering', REFERENCE_ENUM_CLASS, 'EgressFiltering_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg', 'EgressFiltering_Enum', 
                [], [], 
                '''                Egress Ethernet filtering
                ''',
                'egress_filtering',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('source-bypass-egress-filtering', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Mark all ingress packets to bypass any egress
                VLAN filter
                ''',
                'source_bypass_egress_filtering',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'l2-ethernet-features',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols.L2Protocol' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols.L2Protocol',
            False, 
            [
            _MetaInfoClassMember('l2-protocol-name', REFERENCE_ENUM_CLASS, 'L2ProtocolName_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg', 'L2ProtocolName_Enum', 
                [], [], 
                '''                Protocol name
                ''',
                'l2_protocol_name',
                'Cisco-IOS-XR-l2-eth-infra-cfg', True),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'L2ProtocolMode_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_cfg', 'L2ProtocolMode_Enum', 
                [], [], 
                '''                How to handle the protocol's packets
                ''',
                'mode',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('mpls-exp-bits-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The value to set the MPLS Exp bits to within
                the PW.This value may be specified if the mode
                is forward or tunnel and must not be specified
                if the mode is drop
                ''',
                'mpls_exp_bits_value',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'l2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols',
            False, 
            [
            _MetaInfoClassMember('l2-protocol', REFERENCE_LIST, 'L2Protocol' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols.L2Protocol', 
                [], [], 
                '''                Handling of a specific Layer 2 protocol
                ''',
                'l2_protocol',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'l2-protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession.Attachment',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirection_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanTrafficDirection_Enum', 
                [], [], 
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClass_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass_Enum', 
                [], [], 
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', True),
            _MetaInfoClassMember('acl', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession.Attachment', 
                [], [], 
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int' , None, None, 
                [(1, 10000)], [], 
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMirrorInterval_Enum', 
                [], [], 
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession', 
                [], [], 
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.L2Transport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.L2Transport',
            False, 
            [
            _MetaInfoClassMember('atm-port-mode-parameters', REFERENCE_CLASS, 'AtmPortModeParameters' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters', 
                [], [], 
                '''                ATM L2transport Port Mode Parameters
                Configuration
                ''',
                'atm_port_mode_parameters',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object is only valid on physical
                interfaces and it controls whether that
                interface is a port mode Layer 2 attachment
                circuit (note that for subinterfaces, the Layer
                2 property is specified when the subinterface
                is created).The object must be set before any
                other L2Transport configuration is supplied for
                the interface, and must be the last
                per-interface configuration object to be
                removed.
                ''',
                'enabled',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2-ethernet-features', REFERENCE_CLASS, 'L2EthernetFeatures' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2EthernetFeatures', 
                [], [], 
                '''                L2 Ethernet Features Configuration
                ''',
                'l2_ethernet_features',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('l2-protocols', REFERENCE_CLASS, 'L2Protocols' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols', 
                [], [], 
                '''                Interface specific Layer 2 protocol handling
                ''',
                'l2_protocols',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('propagate-remote-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable propagation of the remote
                attachment-circuit link state to the
                localattachment-circuit link state
                ''',
                'propagate_remote_status',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions', 
                [], [], 
                '''                Monitor Session container for this source
                interface
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2-transport',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lacp.CiscoExtensions' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lacp.CiscoExtensions',
            False, 
            [
            _MetaInfoClassMember('cisco-ext', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Cisco extensions
                ''',
                'cisco_ext',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('cisco-ext-type', REFERENCE_ENUM_CLASS, 'BundleCiscoExtTypes_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'BundleCiscoExtTypes_Enum', 
                [], [], 
                '''                Specific Cisco extension to enable / disable
                ''',
                'cisco_ext_type',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'cisco-extensions',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lacp.Timeout' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lacp.Timeout',
            False, 
            [
            _MetaInfoClassMember('actor-churn', ATTRIBUTE, 'int' , None, None, 
                [(0, 120)], [], 
                '''                The time in milliseconds for which to run the
                timer
                ''',
                'actor_churn',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('partner-churn', ATTRIBUTE, 'int' , None, None, 
                [(0, 120)], [], 
                '''                Set the timeout to use before declaring
                partner churn
                ''',
                'partner_churn',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('rx-default', ATTRIBUTE, 'int' , None, None, 
                [(0, 3000)], [], 
                '''                Set the timeout between expired and defaulted
                states
                ''',
                'rx_default',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lacp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lacp',
            False, 
            [
            _MetaInfoClassMember('churn-logging', REFERENCE_ENUM_CLASS, 'ChurnLogging_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'ChurnLogging_Enum', 
                [], [], 
                '''                Log churn notifications on the specified
                system(s)
                ''',
                'churn_logging',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('cisco-extensions', REFERENCE_CLASS, 'CiscoExtensions' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lacp.CiscoExtensions', 
                [], [], 
                '''                Enable bundle Cisco extensions
                ''',
                'cisco_extensions',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('collector-max-delay', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Collector Max Delay value to signal to the LACP
                partner
                ''',
                'collector_max_delay',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('fast-switchover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure to enable the fast-switchover mode
                ''',
                'fast_switchover',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('lacp-nonrevertive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure to enable lacp non-revertive mode
                ''',
                'lacp_nonrevertive',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('period-short', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LACP period to request from the partner (LACP
                standard short period, or rate in milliseconds
                for use with Cisco-specific extensions).
                Default is LACP standard long period (30s).
                ''',
                'period_short',
                'Cisco-IOS-XR-bundlemgr-cfg', False, [
                    _MetaInfoClassMember('period-short', REFERENCE_ENUM_CLASS, 'PeriodShortEnum_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'PeriodShortEnum_Enum', 
                        [], [], 
                        '''                        LACP period to request from the partner (LACP
                        standard short period, or rate in milliseconds
                        for use with Cisco-specific extensions).
                        Default is LACP standard long period (30s).
                        ''',
                        'period_short',
                        'Cisco-IOS-XR-bundlemgr-cfg', False),
                    _MetaInfoClassMember('period-short', ATTRIBUTE, 'int' , None, None, 
                        [(1, 1000)], [], 
                        '''                        LACP period to request from the partner (LACP
                        standard short period, or rate in milliseconds
                        for use with Cisco-specific extensions).
                        Default is LACP standard long period (30s).
                        ''',
                        'period_short',
                        'Cisco-IOS-XR-bundlemgr-cfg', False),
                ]),
            _MetaInfoClassMember('suppress-flaps', ATTRIBUTE, 'int' , None, None, 
                [(100, 65535)], [], 
                '''                Suppress flaps on switchover for the specified
                period (in ms)
                ''',
                'suppress_flaps',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                System identifier for this bundle.
                ''',
                'system_mac',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                System priority for this bundle. Lower value is
                higher priority.
                ''',
                'system_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lacp.Timeout', 
                [], [], 
                '''                Set timeout values for LACP-related timers
                ''',
                'timeout',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'lacp',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lldp.Receive' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lldp.Receive',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable LLDP RX
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'receive',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lldp.Transmit' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lldp.Transmit',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable LLDP TX
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'transmit',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Lldp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Lldp',
            False, 
            [
            _MetaInfoClassMember('lldp-intf-enter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enter LLDP interface submode
                ''',
                'lldp_intf_enter',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('receive', REFERENCE_CLASS, 'Receive' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lldp.Receive', 
                [], [], 
                '''                Disable LLDP RX
                ''',
                'receive',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('transmit', REFERENCE_CLASS, 'Transmit' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lldp.Transmit', 
                [], [], 
                '''                Disable LLDP TX
                ''',
                'transmit',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'lldp',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MacAccounting' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MacAccounting',
            False, 
            [
            _MetaInfoClassMember('egress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Per MAC address accounting statistics
                ''',
                'egress',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ingress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Per MAC address accounting statistics
                ''',
                'ingress',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'mac-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Mlacp.Maximize' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Mlacp.Maximize',
            False, 
            [
            _MetaInfoClassMember('bandwidth-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bandwidth (in kbps) below which to switch
                to the peer if it has more bandwidth available
                . Only applicable if maximizing by bandwidth.
                If 0, no threshold is applied.
                ''',
                'bandwidth_threshold',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('link-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 64)], [], 
                '''                The number of links below which to switch to
                the peer if it has more links available. Only
                applicable if maximizing by links. If 0, no
                threshold is applied.
                ''',
                'link_threshold',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('maximize-by', REFERENCE_ENUM_CLASS, 'MlacpMaximizeParameter_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'MlacpMaximizeParameter_Enum', 
                [], [], 
                '''                The paramenter which should be maximized
                ''',
                'maximize_by',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'maximize',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Mlacp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Mlacp',
            False, 
            [
            _MetaInfoClassMember('iccp-group', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Specify an ICCP Group in which this bundle
                should operate
                ''',
                'iccp_group',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('maximize', REFERENCE_CLASS, 'Maximize' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Mlacp.Maximize', 
                [], [], 
                '''                Set parameters to maximize between the mLACP
                peers
                ''',
                'maximize',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('port-priority', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The LACP port priority (lower value is higher
                priority)
                ''',
                'port_priority',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('recovery-delay', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Set the delay before the bundle becomes active
                after recovery from failure
                ''',
                'recovery_delay',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('switchover-type', REFERENCE_ENUM_CLASS, 'MlacpSwitchover_Enum' , 'ydk.models.bundlemgr.Cisco_IOS_XR_bundlemgr_cfg', 'MlacpSwitchover_Enum', 
                [], [], 
                '''                Set the type of mLACP switchover to use for
                this bundle
                ''',
                'switchover_type',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            ],
            'Cisco-IOS-XR-bundlemgr-cfg',
            'mlacp',
            _yang_ns._namespaces['Cisco-IOS-XR-bundlemgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.AffinityMask' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Bandwidth' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type for the bandwith allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDste_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDste_Enum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                Path option properties
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The ID of the IP explicit path associated
                with this option
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the IP explicit path associated
                with this option
                ''',
                'path_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOption_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOption_Enum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('verbatim', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                Path option properties
                ''',
                'verbatim',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions.PathOption', 
                [], [], 
                '''                P2MP destination path option
                ''',
                'path_option',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-options',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.S2lLogging' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.S2lLogging',
            False, 
            [
            _MetaInfoClassMember('s2l-insufficient-bw-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel destination s2l insufficient BW
                messages
                ''',
                's2l_insufficient_bw_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('s2l-pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for destination s2l
                path-calculation failures
                ''',
                's2l_pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('s2l-reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel destination s2l rereoute messages
                ''',
                's2l_reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('s2l-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel destination s2l state messages
                ''',
                's2l_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            's2l-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of P2MP destination
                ''',
                'address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disables P2MP destination
                ''',
                'destination_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions', 
                [], [], 
                '''                P2MP destination path-options attributes
                table
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('s2l-logging', REFERENCE_CLASS, 'S2lLogging' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.S2lLogging', 
                [], [], 
                '''                Log tunnel destination s2l messages
                ''',
                's2l_logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination-leaf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs',
            False, 
            [
            _MetaInfoClassMember('destination-leaf', REFERENCE_LIST, 'DestinationLeaf' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf', 
                [], [], 
                '''                P2MP destination leaf
                ''',
                'destination_leaf',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination-leafs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Logging' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Logging',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all events for a tunnel
                ''',
                'all',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-change-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel bandwidth change messages
                ''',
                'bandwidth_change_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bw-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel messages for insufficient bandwidth
                ''',
                'insufficient_bw_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pcalc-failure-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging for path-calculation failures
                ''',
                'pcalc_failure_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize-attempts-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimization attempts messages
                ''',
                'reoptimize_attempts_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimized-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel reoptimized messages
                ''',
                'reoptimized_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute-messsage', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel rereoute messages
                ''',
                'reroute_messsage',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log tunnel state messages
                ''',
                'state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sub-lsp-state-message', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Log all tunnel sub-LSP state messages
                ''',
                'sub_lsp_state_message',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinity_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinity_Enum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Priority' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes',
            False, 
            [
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.AffinityMask', 
                [], [], 
                '''                P2MP tunnel affinity and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Bandwidth', 
                [], [], 
                '''                P2MP tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-leafs', REFERENCE_CLASS, 'DestinationLeafs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs', 
                [], [], 
                '''                P2MP destination table
                ''',
                'destination_leafs',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify P2MP tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('impose-explicit-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Impose an explicit null bellow the TE label
                ''',
                'impose_explicit_null',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Logging', 
                [], [], 
                '''                Log tunnel LSP messages
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities', 
                [], [], 
                '''                P2MP tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetric_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetric_Enum', 
                [], [], 
                '''                Path selection configuration for this specific
                tunnel
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Priority', 
                [], [], 
                '''                P2MP tunnel setup and hold priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record route used by individual P2MP S2L(s)
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 254)], [], 
                '''                The name of the P2MP tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-payload', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                P2MP tunnel ipv6 signalled payload
                ''',
                'signalled_payload',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mte-tunnel-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Mtus.Mtu' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Mtus.Mtu',
            False, 
            [
            _MetaInfoClassMember('owner', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The Owner of the interface - eg. for
                'LoopbackX' main interface this is 'loopback'
                ''',
                'owner',
                'Cisco-IOS-XR-ifmgr-cfg', True),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [(64, 65535)], [], 
                '''                The MTU value
                ''',
                'mtu',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'mtu',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Mtus' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Mtus',
            False, 
            [
            _MetaInfoClassMember('mtu', REFERENCE_LIST, 'Mtu' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Mtus.Mtu', 
                [], [], 
                '''                The MTU for the interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'mtus',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'egress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('egress', REFERENCE_CLASS, 'Egress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress', 
                [], [], 
                '''                Configure egress monitoring direction
                ''',
                'egress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('ingress', REFERENCE_CLASS, 'Ingress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress', 
                [], [], 
                '''                Configure ingress monitoring direction
                ''',
                'ingress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_CLASS, 'FlowMonitorMap' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap', 
                [], [], 
                '''                Configure a flow monitor map
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'egress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('egress', REFERENCE_CLASS, 'Egress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress', 
                [], [], 
                '''                Configure egress monitoring direction
                ''',
                'egress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('ingress', REFERENCE_CLASS, 'Ingress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress', 
                [], [], 
                '''                Configure ingress monitoring direction
                ''',
                'ingress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_CLASS, 'FlowMonitorMap' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap', 
                [], [], 
                '''                Configure a flow monitor map
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'egress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress.FlowMonitorName' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress.FlowMonitorName',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Flow monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-name', REFERENCE_LIST, 'FlowMonitorName' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress.FlowMonitorName', 
                [], [], 
                '''                Specify a sampler for a flow monitor
                ''',
                'flow_monitor_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'ingress',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('egress', REFERENCE_CLASS, 'Egress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress', 
                [], [], 
                '''                Configure egress monitoring direction
                ''',
                'egress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('ingress', REFERENCE_CLASS, 'Ingress' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress', 
                [], [], 
                '''                Configure ingress monitoring direction
                ''',
                'ingress',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_CLASS, 'FlowMonitorMap' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap', 
                [], [], 
                '''                Configure a flow monitor map
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NetFlow' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NetFlow',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4', 
                [], [], 
                '''                Configure IPv4 netflow
                ''',
                'ipv4',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6', 
                [], [], 
                '''                Configure IPv6 netflow
                ''',
                'ipv6',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls', 
                [], [], 
                '''                Configure MPLS netflow
                ''',
                'mpls',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'net-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteAccess' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteAccess',
            False, 
            [
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite-access',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures.Cfm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures.Cfm',
            False, 
            [
            _MetaInfoClassMember('continuity-check-interval', REFERENCE_ENUM_CLASS, 'CfmCcmInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes', 'CfmCcmInterval_Enum', 
                [], [], 
                '''                Continuity-Check Interval
                ''',
                'continuity_check_interval',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CFM on Satellite
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Maintenance Domain Level
                ''',
                'level',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cfm',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures',
            False, 
            [
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures.Cfm', 
                [], [], 
                '''                CFM Satellite configuration
                ''',
                'cfm',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'ethernet-features',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.Redundancy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.Redundancy',
            False, 
            [
            _MetaInfoClassMember('iccp-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Links the satellite fabric to the given ICCP
                group
                ''',
                'iccp_group',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('minimum-preferred-links', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Mininum number of active links preferred
                ''',
                'minimum_preferred_links',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts.RemotePort' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts.RemotePort',
            False, 
            [
            _MetaInfoClassMember('port-type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 8)], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('sub-slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 8)], [], 
                '''                Sub slot
                ''',
                'sub_slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('port-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port range
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'remote-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts',
            False, 
            [
            _MetaInfoClassMember('remote-port', REFERENCE_LIST, 'RemotePort' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts.RemotePort', 
                [], [], 
                '''                Remote Ports
                ''',
                'remote_port',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'remote-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink',
            False, 
            [
            _MetaInfoClassMember('ethernet-features', REFERENCE_CLASS, 'EthernetFeatures' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures', 
                [], [], 
                '''                Ethernet Satellite configuration
                ''',
                'ethernet_features',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.Redundancy', 
                [], [], 
                '''                Redundancy submode
                ''',
                'redundancy',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('remote-ports', REFERENCE_CLASS, 'RemotePorts' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts', 
                [], [], 
                '''                Remote Ports table
                ''',
                'remote_ports',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('satellite', ATTRIBUTE, 'int' , None, None, 
                [(100, 65534)], [], 
                '''                Hub & Spoke connection to a single Satellite
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite-fabric-link',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Redundancy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Redundancy',
            False, 
            [
            _MetaInfoClassMember('iccp-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Links the satellite fabric to the given ICCP
                group
                ''',
                'iccp_group',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('minimum-preferred-links', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Mininum number of active links preferred
                ''',
                'minimum_preferred_links',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts.RemotePort' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts.RemotePort',
            False, 
            [
            _MetaInfoClassMember('port-type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 8)], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('sub-slot', ATTRIBUTE, 'int' , None, None, 
                [(0, 8)], [], 
                '''                Sub slot
                ''',
                'sub_slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('port-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port range
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'remote-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts',
            False, 
            [
            _MetaInfoClassMember('remote-port', REFERENCE_LIST, 'RemotePort' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts.RemotePort', 
                [], [], 
                '''                Remote Ports
                ''',
                'remote_port',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'remote-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [(100, 65534)], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable
                ''',
                'enable',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('remote-ports', REFERENCE_CLASS, 'RemotePorts' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts', 
                [], [], 
                '''                Remote Ports table
                ''',
                'remote_ports',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites',
            False, 
            [
            _MetaInfoClassMember('satellite', REFERENCE_LIST, 'Satellite' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite', 
                [], [], 
                '''                Connected Satellite
                ''',
                'satellite',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'satellites',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable
                ''',
                'enable',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Redundancy', 
                [], [], 
                '''                Redundancy submode
                ''',
                'redundancy',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('satellites', REFERENCE_CLASS, 'Satellites' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites', 
                [], [], 
                '''                Connected Satellite table
                ''',
                'satellites',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite-fabric-network',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsDwdmCarrier' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsDwdmCarrier',
            False, 
            [
            _MetaInfoClassMember('grid-type', REFERENCE_ENUM_CLASS, 'OpticsDwdmCarrierGrid_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg', 'OpticsDwdmCarrierGrid_Enum', 
                [], [], 
                '''                DWDM Channel Grid Type
                ''',
                'grid_type',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('param-type', REFERENCE_ENUM_CLASS, 'OpticsDwdmCarrierParam_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg', 'OpticsDwdmCarrierParam_Enum', 
                [], [], 
                '''                DWDM Channel Parameter Type ITU-Channel or
                Frequency or Wavelength
                ''',
                'param_type',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('param-value', ATTRIBUTE, 'int' , None, None, 
                [(1, 1961000)], [], 
                '''                Type ITU-Channel Range 1-100, Frequency Range
                19115-19610, Wavelength Range 1528773-1568362,
                100MHz Frequency Range 1911500-1961000
                ''',
                'param_value',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'optics-dwdm-carrier',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs.OpticsNetworkSrlg' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs.OpticsNetworkSrlg',
            False, 
            [
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 17)], [], 
                '''                Set index
                ''',
                'set_id',
                'Cisco-IOS-XR-controller-optics-cfg', True),
            _MetaInfoClassMember('srlg1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg1',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('srlg2', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg2',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('srlg3', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg3',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('srlg4', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg4',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('srlg5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg5',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('srlg6', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                none
                ''',
                'srlg6',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'optics-network-srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs',
            False, 
            [
            _MetaInfoClassMember('optics-network-srlg', REFERENCE_LIST, 'OpticsNetworkSrlg' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs.OpticsNetworkSrlg', 
                [], [], 
                '''                Configure network srlg sets
                ''',
                'optics_network_srlg',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'optics-network-srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds.RxThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds.RxThreshold',
            False, 
            [
            _MetaInfoClassMember('rx-threshold-type', REFERENCE_ENUM_CLASS, 'Threshold_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg', 'Threshold_Enum', 
                [], [], 
                '''                Low or high rx threshold
                ''',
                'rx_threshold_type',
                'Cisco-IOS-XR-controller-optics-cfg', True),
            _MetaInfoClassMember('rx-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-400, 300)], [], 
                '''                Select power level (in units of 0.1dBm)
                ''',
                'rx_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'rx-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds',
            False, 
            [
            _MetaInfoClassMember('rx-threshold', REFERENCE_LIST, 'RxThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds.RxThreshold', 
                [], [], 
                '''                Optics RX Low or high threshold configuration
                ''',
                'rx_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'rx-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds.TxThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds.TxThreshold',
            False, 
            [
            _MetaInfoClassMember('tx-threshold-type', REFERENCE_ENUM_CLASS, 'Threshold_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg', 'Threshold_Enum', 
                [], [], 
                '''                Low or high tx threshold
                ''',
                'tx_threshold_type',
                'Cisco-IOS-XR-controller-optics-cfg', True),
            _MetaInfoClassMember('tx-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-400, 300)], [], 
                '''                Select power level (in units of 0.1dBm)
                ''',
                'tx_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'tx-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds',
            False, 
            [
            _MetaInfoClassMember('tx-threshold', REFERENCE_LIST, 'TxThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds.TxThreshold', 
                [], [], 
                '''                Optics TX Low or high threshold configuration
                ''',
                'tx_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'tx-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Optics' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Optics',
            False, 
            [
            _MetaInfoClassMember('optics-cd-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-70000, 70000)], [], 
                '''                Select chromatic dispersion high threshold(in
                units of ps/nm)
                ''',
                'optics_cd_high_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-cd-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-70000, 70000)], [], 
                '''                Select chromatic dispersion low threshold(in
                units of ps/nm)
                ''',
                'optics_cd_low_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-cd-max', ATTRIBUTE, 'int' , None, None, 
                [(-70000, 70000)], [], 
                '''                Select max chromatic dispersion (in units of
                ps/nm)
                ''',
                'optics_cd_max',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-cd-min', ATTRIBUTE, 'int' , None, None, 
                [(-70000, 70000)], [], 
                '''                Select min chromatic dispersion (in units of
                ps/nm)
                ''',
                'optics_cd_min',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Configure optics port description 
                ''',
                'optics_description',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-dgd-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 18000)], [], 
                '''                Select DGD high threshold(in units of 0.1ps)
                ''',
                'optics_dgd_high_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-dwdm-carrier', REFERENCE_CLASS, 'OpticsDwdmCarrier' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsDwdmCarrier', 
                [], [], 
                '''                Configure optics DWDM Carrier
                ''',
                'optics_dwdm_carrier',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-lbc-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Select power level (in units of percentage)
                ''',
                'optics_lbc_high_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-loopback', REFERENCE_ENUM_CLASS, 'OpticsLoopback_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg', 'OpticsLoopback_Enum', 
                [], [], 
                '''                Configure optics loopback mode 
                ''',
                'optics_loopback',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-network-srlgs', REFERENCE_CLASS, 'OpticsNetworkSrlgs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs', 
                [], [], 
                '''                Configure Network srlgs
                ''',
                'optics_network_srlgs',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-osnr-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4000)], [], 
                '''                Select OSNR low threshold(in units of 0.01db)
                ''',
                'optics_osnr_low_threshold',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-performance-monitoring', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Select Performance Monitoring as Enable or
                Disable
                ''',
                'optics_performance_monitoring',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-transmit-power', ATTRIBUTE, 'int' , None, None, 
                [(-190, 15)], [], 
                '''                Select power level (in units of 0.1dBm)
                ''',
                'optics_transmit_power',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('optics-transmit-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure optics transmit laser shutdown 
                ''',
                'optics_transmit_shutdown',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('rx-thresholds', REFERENCE_CLASS, 'RxThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds', 
                [], [], 
                '''                Configure Rx threshold
                ''',
                'rx_thresholds',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('tx-thresholds', REFERENCE_CLASS, 'TxThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds', 
                [], [], 
                '''                Configure Tx threshold
                ''',
                'tx_thresholds',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            ],
            'Cisco-IOS-XR-controller-optics-cfg',
            'optics',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs.NetworkSrlg' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs.NetworkSrlg',
            False, 
            [
            _MetaInfoClassMember('set-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 17)], [], 
                '''                Set index
                ''',
                'set_id',
                'Cisco-IOS-XR-controller-otu-cfg', True),
            _MetaInfoClassMember('srlg1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                First value for Network SRLG
                ''',
                'srlg1',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('srlg2', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                Second value for Network SRLG
                ''',
                'srlg2',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('srlg3', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                Third value for Network SRLG
                ''',
                'srlg3',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('srlg4', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                Forth value for Network SRLG
                ''',
                'srlg4',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('srlg5', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                Fifth value for Network SRLG
                ''',
                'srlg5',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('srlg6', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967294)], [], 
                '''                Sixth value for Network SRLG
                ''',
                'srlg6',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'network-srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs',
            False, 
            [
            _MetaInfoClassMember('network-srlg', REFERENCE_LIST, 'NetworkSrlg' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs.NetworkSrlg', 
                [], [], 
                '''                Configure network srlg sets
                ''',
                'network_srlg',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'network-srlgs',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTti' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTti',
            False, 
            [
            _MetaInfoClassMember('full-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Full ASCII text (Max 64 characters)
                ''',
                'full_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('hex-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Hex nibbles (Max 128 - The string length
                should be an even number)
                ''',
                'hex_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnExpTtiTypeFull_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeFull_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-expected-tti',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtisapi' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtisapi',
            False, 
            [
            _MetaInfoClassMember('sapi-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 14)], [], 
                '''                SAPI ASCII text (Max 14 characters)
                ''',
                'sapi_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnExpTtiTypeSapi_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeSapi_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-expected-ttisapi',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmdapi' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmdapi',
            False, 
            [
            _MetaInfoClassMember('dapi-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 14)], [], 
                '''                DAPI ASCII text (Max 14 characters)
                ''',
                'dapi_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnExpTtiTypeDapi_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeDapi_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-expected-ttitcmdapi',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmos' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmos',
            False, 
            [
            _MetaInfoClassMember('osascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                OS ASCII text (Max 32 characters)
                ''',
                'osascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('oshex-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                OS HEX text (Max 64 characters)
                ''',
                'oshex_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnExpTtiTypeOs_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnExpTtiTypeOs_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-expected-ttitcmos',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTti' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTti',
            False, 
            [
            _MetaInfoClassMember('full-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Full ASCII text (Max 64 characters)
                ''',
                'full_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('hex-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Hex nibbles (Max 128 - The string length
                should be an even number)
                ''',
                'hex_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnSendTtiTypeFull_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeFull_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-send-tti',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtisapi' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtisapi',
            False, 
            [
            _MetaInfoClassMember('sapi-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 14)], [], 
                '''                SAPI ASCII text (Max 14 characters)
                ''',
                'sapi_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnSendTtiTypeSapi_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeSapi_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-send-ttisapi',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmdapi' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmdapi',
            False, 
            [
            _MetaInfoClassMember('dapi-ascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 14)], [], 
                '''                DAPI ASCII text (Max 14 characters)
                ''',
                'dapi_ascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnSendTtiTypeDapi_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeDapi_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-send-ttitcmdapi',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmos' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmos',
            False, 
            [
            _MetaInfoClassMember('osascii-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                OS ASCII text (Max 32 characters)
                ''',
                'osascii_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('oshex-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                OS HEX text (Max 64 characters)
                ''',
                'oshex_string',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('string-type', REFERENCE_ENUM_CLASS, 'OtnSendTtiTypeOs_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnSendTtiTypeOs_Enum', 
                [], [], 
                '''                TTI string type (FULL ASCII or  DAPI ASCII or
                SAPI ASCII or hex format or OS ASCII or OS
                HEX)
                ''',
                'string_type',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otn-send-ttitcmos',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertThreshold',
            False, 
            [
            _MetaInfoClassMember('coefficient', ATTRIBUTE, 'int' , None, None, 
                [(1, 9)], [], 
                '''                Bit error rate coefficient
                ''',
                'coefficient',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Proactive Protection supported
                ''',
                'enable',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [(4, 10)], [], 
                '''                Bit error rate power
                ''',
                'power',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'revert-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertWindow' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertWindow',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Proactive Protection
                ''',
                'enable',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [(2000, 10000)], [], 
                '''                Integration window for FRR trigger in MS
                ''',
                'value',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'revert-window',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerThreshold',
            False, 
            [
            _MetaInfoClassMember('coefficient', ATTRIBUTE, 'int' , None, None, 
                [(1, 9)], [], 
                '''                Bit error rate coefficient
                ''',
                'coefficient',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Proactive Protection supported
                ''',
                'enable',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [(3, 9)], [], 
                '''                Bit error rate power
                ''',
                'power',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'trigger-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerWindow' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerWindow',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Proactive Protection
                ''',
                'enable',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [(10, 10000)], [], 
                '''                Integration window for FRR trigger in MS
                ''',
                'value',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'trigger-window',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection',
            False, 
            [
            _MetaInfoClassMember('revert-threshold', REFERENCE_CLASS, 'RevertThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertThreshold', 
                [], [], 
                '''                Proactive Protection Threshold
                ''',
                'revert_threshold',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('revert-window', REFERENCE_CLASS, 'RevertWindow' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertWindow', 
                [], [], 
                '''                Proactive Protection Window
                ''',
                'revert_window',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Proactive Protection
                ''',
                'status',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('trigger-threshold', REFERENCE_CLASS, 'TriggerThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerThreshold', 
                [], [], 
                '''                Proactive Protection Threshold
                ''',
                'trigger_threshold',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('trigger-window', REFERENCE_CLASS, 'TriggerWindow' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerWindow', 
                [], [], 
                '''                Proactive Protection Window
                ''',
                'trigger_window',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'proactive-protection',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Otu' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Otu',
            False, 
            [
            _MetaInfoClassMember('fec', REFERENCE_ENUM_CLASS, 'OtuForwardErrorCorrection_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtuForwardErrorCorrection_Enum', 
                [], [], 
                '''                Configure forward error correction
                ''',
                'fec',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('gcc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                General Communication Channel configuration
                ''',
                'gcc',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('loopback', REFERENCE_ENUM_CLASS, 'OtnLoopback_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnLoopback_Enum', 
                [], [], 
                '''                Type of Loopback
                ''',
                'loopback',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('network-srlgs', REFERENCE_CLASS, 'NetworkSrlgs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs', 
                [], [], 
                '''                Configure Network srlgs
                ''',
                'network_srlgs',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-expected-tti', REFERENCE_CLASS, 'OtnExpectedTti' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTti', 
                [], [], 
                '''                Configure OTN Expected TTI value for Full
                ASCII/HEX
                ''',
                'otn_expected_tti',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-expected-ttisapi', REFERENCE_CLASS, 'OtnExpectedTtisapi' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtisapi', 
                [], [], 
                '''                Configure OTN Expected TTI value for SAPI
                configs
                ''',
                'otn_expected_ttisapi',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-expected-ttitcmdapi', REFERENCE_CLASS, 'OtnExpectedTtitcmdapi' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmdapi', 
                [], [], 
                '''                Configure OTN Expected TTI value for DAPI
                configs
                ''',
                'otn_expected_ttitcmdapi',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-expected-ttitcmos', REFERENCE_CLASS, 'OtnExpectedTtitcmos' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmos', 
                [], [], 
                '''                Configure OTN Expected TTI value for OS config
                ''',
                'otn_expected_ttitcmos',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-send-tti', REFERENCE_CLASS, 'OtnSendTti' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTti', 
                [], [], 
                '''                Configure OTN Send TTI value for Full ASCII/HEX
                ''',
                'otn_send_tti',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-send-ttisapi', REFERENCE_CLASS, 'OtnSendTtisapi' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtisapi', 
                [], [], 
                '''                Configure OTN Send TTI value for SAPI configs
                ''',
                'otn_send_ttisapi',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-send-ttitcmdapi', REFERENCE_CLASS, 'OtnSendTtitcmdapi' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmdapi', 
                [], [], 
                '''                Configure OTN Send TTI value for DAPI configs
                ''',
                'otn_send_ttitcmdapi',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('otn-send-ttitcmos', REFERENCE_CLASS, 'OtnSendTtitcmos' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmos', 
                [], [], 
                '''                Configure OTN Send TTI value for OS config
                ''',
                'otn_send_ttitcmos',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('performance-monitoring', REFERENCE_ENUM_CLASS, 'OtnPerMon_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnPerMon_Enum', 
                [], [], 
                '''                Configure performance monitoring
                ''',
                'performance_monitoring',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('proactive-protection', REFERENCE_CLASS, 'ProactiveProtection' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection', 
                [], [], 
                '''                Configure Proactive Protection
                ''',
                'proactive_protection',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('sd', ATTRIBUTE, 'int' , None, None, 
                [(5, 9)], [], 
                '''                Signal degrade threshold
                ''',
                'sd',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('secondary-admin-state', REFERENCE_ENUM_CLASS, 'OtnSecAdminState_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_otu_cfg', 'OtnSecAdminState_Enum', 
                [], [], 
                '''                Configure secondary admin state 
                ''',
                'secondary_admin_state',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('sf', ATTRIBUTE, 'int' , None, None, 
                [(5, 9)], [], 
                '''                Signal failure threshold
                ''',
                'sf',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            ],
            'Cisco-IOS-XR-controller-otu-cfg',
            'otu',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Pbr.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Pbr.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress service policy
                ''',
                'input',
                'Cisco-IOS-XR-pbr-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Pbr' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Pbr',
            False, 
            [
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Pbr.ServicePolicy', 
                [], [], 
                '''                PBR service policy configuration
                ''',
                'service_policy',
                'Cisco-IOS-XR-pbr-cfg', False),
            _MetaInfoClassMember('service-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class for subscriber ingress policy
                ''',
                'service_policy_in',
                'Cisco-IOS-XR-pbr-cfg', False),
            ],
            'Cisco-IOS-XR-pbr-cfg',
            'pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports.Hour24EtherReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports.Hour24EtherReport',
            False, 
            [
            _MetaInfoClassMember('ether-report', REFERENCE_ENUM_CLASS, 'EtherReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'EtherReport_Enum', 
                [], [], 
                '''                Ether Report Type
                ''',
                'ether_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-ether-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports',
            False, 
            [
            _MetaInfoClassMember('hour24-ether-report', REFERENCE_LIST, 'Hour24EtherReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports.Hour24EtherReport', 
                [], [], 
                '''                none
                ''',
                'hour24_ether_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-ether-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds.Hour24EtherThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds.Hour24EtherThreshold',
            False, 
            [
            _MetaInfoClassMember('ether-threshold', REFERENCE_ENUM_CLASS, 'EtherThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'EtherThreshold_Enum', 
                [], [], 
                '''                Ether Threshold Type
                ''',
                'ether_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ether-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ether Thresh Value
                ''',
                'ether_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-ether-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24-ether-threshold', REFERENCE_LIST, 'Hour24EtherThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds.Hour24EtherThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24_ether_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-ether-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether',
            False, 
            [
            _MetaInfoClassMember('hour24-ether-reports', REFERENCE_CLASS, 'Hour24EtherReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports', 
                [], [], 
                '''                set ether TCA reporting status
                ''',
                'hour24_ether_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24-ether-thresholds', REFERENCE_CLASS, 'Hour24EtherThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds', 
                [], [], 
                '''                Configure threshold on ether parameters
                ''',
                'hour24_ether_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-ether',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24',
            False, 
            [
            _MetaInfoClassMember('hour24-ether', REFERENCE_CLASS, 'Hour24Ether' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether', 
                [], [], 
                '''                Configure ether performance monitoring
                ''',
                'hour24_ether',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ethernet-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports.Minute15EtherReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports.Minute15EtherReport',
            False, 
            [
            _MetaInfoClassMember('ether-report', REFERENCE_ENUM_CLASS, 'EtherReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'EtherReport_Enum', 
                [], [], 
                '''                Ether Report Type
                ''',
                'ether_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-ether-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports',
            False, 
            [
            _MetaInfoClassMember('minute15-ether-report', REFERENCE_LIST, 'Minute15EtherReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports.Minute15EtherReport', 
                [], [], 
                '''                none
                ''',
                'minute15_ether_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-ether-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds.Minute15EtherThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds.Minute15EtherThreshold',
            False, 
            [
            _MetaInfoClassMember('ether-threshold', REFERENCE_ENUM_CLASS, 'EtherThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'EtherThreshold_Enum', 
                [], [], 
                '''                Ether Threshold Type
                ''',
                'ether_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ether-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ether Threshold Value
                ''',
                'ether_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-ether-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds',
            False, 
            [
            _MetaInfoClassMember('minute15-ether-threshold', REFERENCE_LIST, 'Minute15EtherThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds.Minute15EtherThreshold', 
                [], [], 
                '''                none
                ''',
                'minute15_ether_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-ether-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether',
            False, 
            [
            _MetaInfoClassMember('minute15-ether-reports', REFERENCE_CLASS, 'Minute15EtherReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports', 
                [], [], 
                '''                set ether TCA reporting status
                ''',
                'minute15_ether_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15-ether-thresholds', REFERENCE_CLASS, 'Minute15EtherThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds', 
                [], [], 
                '''                Configure threshold on ether parameters
                ''',
                'minute15_ether_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-ether',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15',
            False, 
            [
            _MetaInfoClassMember('minute15-ether', REFERENCE_CLASS, 'Minute15Ether' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether', 
                [], [], 
                '''                Configure ether performance monitoring
                ''',
                'minute15_ether',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ethernet-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports.HoVcHour24hoVcReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports.HoVcHour24hoVcReport',
            False, 
            [
            _MetaInfoClassMember('ho-vc-report', REFERENCE_ENUM_CLASS, 'HoVcReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'HoVcReport_Enum', 
                [], [], 
                '''                ho_vc Report Type
                ''',
                'ho_vc_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                ho_vc Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24ho-vc-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports',
            False, 
            [
            _MetaInfoClassMember('ho-vc-hour24ho-vc-report', REFERENCE_LIST, 'HoVcHour24hoVcReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports.HoVcHour24hoVcReport', 
                [], [], 
                '''                none
                ''',
                'ho_vc_hour24ho_vc_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24ho-vc-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds.HoVcHour24hoVcThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds.HoVcHour24hoVcThreshold',
            False, 
            [
            _MetaInfoClassMember('ho-vc-threshold', REFERENCE_ENUM_CLASS, 'HoVcThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'HoVcThreshold_Enum', 
                [], [], 
                '''                ho_vc Threshold Type
                ''',
                'ho_vc_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ho-vc-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ho_vc Thresh Value
                ''',
                'ho_vc_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24ho-vc-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds',
            False, 
            [
            _MetaInfoClassMember('ho-vc-hour24ho-vc-threshold', REFERENCE_LIST, 'HoVcHour24hoVcThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds.HoVcHour24hoVcThreshold', 
                [], [], 
                '''                none
                ''',
                'ho_vc_hour24ho_vc_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24ho-vc-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc',
            False, 
            [
            _MetaInfoClassMember('ho-vc-hour24ho-vc-reports', REFERENCE_CLASS, 'HoVcHour24hoVcReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports', 
                [], [], 
                '''                set ho_vc TCA reporting status
                ''',
                'ho_vc_hour24ho_vc_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('ho-vc-hour24ho-vc-thresholds', REFERENCE_CLASS, 'HoVcHour24hoVcThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds', 
                [], [], 
                '''                Configure threshold on ho_vc parameters
                ''',
                'ho_vc_hour24ho_vc_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24ho-vc',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24',
            False, 
            [
            _MetaInfoClassMember('ho-vc-hour24ho-vc', REFERENCE_CLASS, 'HoVcHour24hoVc' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc', 
                [], [], 
                '''                Configure ho_vc performance monitoring
                ''',
                'ho_vc_hour24ho_vc',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports.HoVcMinute15hoVcReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports.HoVcMinute15hoVcReport',
            False, 
            [
            _MetaInfoClassMember('ho-vc-report', REFERENCE_ENUM_CLASS, 'HoVcReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'HoVcReport_Enum', 
                [], [], 
                '''                ho_vc Report Type
                ''',
                'ho_vc_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                ho_vc Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15ho-vc-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports',
            False, 
            [
            _MetaInfoClassMember('ho-vc-minute15ho-vc-report', REFERENCE_LIST, 'HoVcMinute15hoVcReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports.HoVcMinute15hoVcReport', 
                [], [], 
                '''                none
                ''',
                'ho_vc_minute15ho_vc_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15ho-vc-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds.HoVcMinute15hoVcThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds.HoVcMinute15hoVcThreshold',
            False, 
            [
            _MetaInfoClassMember('ho-vc-threshold', REFERENCE_ENUM_CLASS, 'HoVcThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'HoVcThreshold_Enum', 
                [], [], 
                '''                ho_vc Threshold Type
                ''',
                'ho_vc_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ho-vc-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ho_vc Threshold Value
                ''',
                'ho_vc_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15ho-vc-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds',
            False, 
            [
            _MetaInfoClassMember('ho-vc-minute15ho-vc-threshold', REFERENCE_LIST, 'HoVcMinute15hoVcThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds.HoVcMinute15hoVcThreshold', 
                [], [], 
                '''                none
                ''',
                'ho_vc_minute15ho_vc_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15ho-vc-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc',
            False, 
            [
            _MetaInfoClassMember('ho-vc-minute15ho-vc-reports', REFERENCE_CLASS, 'HoVcMinute15hoVcReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports', 
                [], [], 
                '''                set ho_vc TCA reporting status
                ''',
                'ho_vc_minute15ho_vc_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('ho-vc-minute15ho-vc-thresholds', REFERENCE_CLASS, 'HoVcMinute15hoVcThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds', 
                [], [], 
                '''                Configure threshold on ho_vc parameters
                ''',
                'ho_vc_minute15ho_vc_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15ho-vc',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15',
            False, 
            [
            _MetaInfoClassMember('ho-vc-minute15ho-vc', REFERENCE_CLASS, 'HoVcMinute15hoVc' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc', 
                [], [], 
                '''                Configure ho_vc performance monitoring
                ''',
                'ho_vc_minute15ho_vc',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'ho-vc-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports.Hour24OpticsReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports.Hour24OpticsReport',
            False, 
            [
            _MetaInfoClassMember('optics-report', REFERENCE_ENUM_CLASS, 'OpticsReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OpticsReport_Enum', 
                [], [], 
                '''                Optics Report Type
                ''',
                'optics_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-optics-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports',
            False, 
            [
            _MetaInfoClassMember('hour24-optics-report', REFERENCE_LIST, 'Hour24OpticsReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports.Hour24OpticsReport', 
                [], [], 
                '''                none
                ''',
                'hour24_optics_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-optics-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds.Hour24OpticsThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds.Hour24OpticsThreshold',
            False, 
            [
            _MetaInfoClassMember('optics-threshold', REFERENCE_ENUM_CLASS, 'OpticsThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OpticsThreshold_Enum', 
                [], [], 
                '''                Optics Threshold Type
                ''',
                'optics_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('optics-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Optics Thresh Value
                ''',
                'optics_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-optics-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24-optics-threshold', REFERENCE_LIST, 'Hour24OpticsThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds.Hour24OpticsThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24_optics_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-optics-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics',
            False, 
            [
            _MetaInfoClassMember('hour24-optics-reports', REFERENCE_CLASS, 'Hour24OpticsReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports', 
                [], [], 
                '''                set optics TCA reporting status
                ''',
                'hour24_optics_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24-optics-thresholds', REFERENCE_CLASS, 'Hour24OpticsThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds', 
                [], [], 
                '''                Configure threshold on optics parameters
                ''',
                'hour24_optics_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-optics',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports.Hour24fecReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports.Hour24fecReport',
            False, 
            [
            _MetaInfoClassMember('fec-report', REFERENCE_ENUM_CLASS, 'FecReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'FecReport_Enum', 
                [], [], 
                '''                Fec Report type
                ''',
                'fec_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Fec Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24fec-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports',
            False, 
            [
            _MetaInfoClassMember('hour24fec-report', REFERENCE_LIST, 'Hour24fecReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports.Hour24fecReport', 
                [], [], 
                '''                none
                ''',
                'hour24fec_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24fec-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds.Hour24fecThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds.Hour24fecThreshold',
            False, 
            [
            _MetaInfoClassMember('fec-threshold', REFERENCE_ENUM_CLASS, 'FecThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'FecThreshold_Enum', 
                [], [], 
                '''                Fec Threshold Type
                ''',
                'fec_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('fec-threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Fec threshold value
                ''',
                'fec_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24fec-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24fec-threshold', REFERENCE_LIST, 'Hour24fecThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds.Hour24fecThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24fec_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24fec-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec',
            False, 
            [
            _MetaInfoClassMember('hour24fec-reports', REFERENCE_CLASS, 'Hour24fecReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports', 
                [], [], 
                '''                set fec TCA reporting status
                ''',
                'hour24fec_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24fec-thresholds', REFERENCE_CLASS, 'Hour24fecThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds', 
                [], [], 
                '''                Configure fec threshold
                ''',
                'hour24fec_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24fec',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports.Hour24otnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports.Hour24otnReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports',
            False, 
            [
            _MetaInfoClassMember('hour24otn-report', REFERENCE_LIST, 'Hour24otnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports.Hour24otnReport', 
                [], [], 
                '''                none
                ''',
                'hour24otn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds.Hour24otnThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds.Hour24otnThreshold',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24otn-threshold', REFERENCE_LIST, 'Hour24otnThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds.Hour24otnThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn',
            False, 
            [
            _MetaInfoClassMember('hour24otn-reports', REFERENCE_CLASS, 'Hour24otnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'hour24otn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24otn-thresholds', REFERENCE_CLASS, 'Hour24otnThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'hour24otn_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24',
            False, 
            [
            _MetaInfoClassMember('hour24-optics', REFERENCE_CLASS, 'Hour24Optics' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics', 
                [], [], 
                '''                Configure optics performance monitoring
                ''',
                'hour24_optics',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24fec', REFERENCE_CLASS, 'Hour24fec' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec', 
                [], [], 
                '''                Configure fec g709 performance monitoring
                ''',
                'hour24fec',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24otn', REFERENCE_CLASS, 'Hour24otn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn', 
                [], [], 
                '''                configure otn g709 performance monitoring
                ''',
                'hour24otn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports.Hour24GfpReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports.Hour24GfpReport',
            False, 
            [
            _MetaInfoClassMember('gfp-report', REFERENCE_ENUM_CLASS, 'GfpReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'GfpReport_Enum', 
                [], [], 
                '''                Gfp Report Type
                ''',
                'gfp_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports',
            False, 
            [
            _MetaInfoClassMember('hour24-gfp-report', REFERENCE_LIST, 'Hour24GfpReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports.Hour24GfpReport', 
                [], [], 
                '''                none
                ''',
                'hour24_gfp_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds.Hour24GfpThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds.Hour24GfpThreshold',
            False, 
            [
            _MetaInfoClassMember('gfp-threshold', REFERENCE_ENUM_CLASS, 'GfpThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'GfpThreshold_Enum', 
                [], [], 
                '''                Gfp Threshold Type
                ''',
                'gfp_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('gfp-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Gfp Thresh Value
                ''',
                'gfp_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24-gfp-threshold', REFERENCE_LIST, 'Hour24GfpThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds.Hour24GfpThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24_gfp_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp',
            False, 
            [
            _MetaInfoClassMember('hour24-gfp-reports', REFERENCE_CLASS, 'Hour24GfpReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports', 
                [], [], 
                '''                set gfp TCA reporting status
                ''',
                'hour24_gfp_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24-gfp-thresholds', REFERENCE_CLASS, 'Hour24GfpThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds', 
                [], [], 
                '''                Configure threshold on gfp parameters
                ''',
                'hour24_gfp_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp',
            False, 
            [
            _MetaInfoClassMember('hour24-gfp', REFERENCE_CLASS, 'Hour24Gfp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp', 
                [], [], 
                '''                Configure gfp performance monitoring
                ''',
                'hour24_gfp',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-gfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports.Hour24otnPathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports.Hour24otnPathReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports',
            False, 
            [
            _MetaInfoClassMember('hour24otn-path-report', REFERENCE_LIST, 'Hour24otnPathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports.Hour24otnPathReport', 
                [], [], 
                '''                none
                ''',
                'hour24otn_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds.Hour24otnPathThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds.Hour24otnPathThreshold',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-path-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24otn-path-threshold', REFERENCE_LIST, 'Hour24otnPathThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds.Hour24otnPathThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24otn_path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-path-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath',
            False, 
            [
            _MetaInfoClassMember('hour24otn-path-reports', REFERENCE_CLASS, 'Hour24otnPathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'hour24otn_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24otn-path-thresholds', REFERENCE_CLASS, 'Hour24otnPathThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'hour24otn_path_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path',
            False, 
            [
            _MetaInfoClassMember('hour24otn-path', REFERENCE_CLASS, 'Hour24otnPath' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath', 
                [], [], 
                '''                configure otn g709 performance monitoring
                ''',
                'hour24otn_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports.Hour24otnTcmReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports.Hour24otnTcmReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnTcmReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnTcmReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcm-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports',
            False, 
            [
            _MetaInfoClassMember('hour24otn-tcm-report', REFERENCE_LIST, 'Hour24otnTcmReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports.Hour24otnTcmReport', 
                [], [], 
                '''                none
                ''',
                'hour24otn_tcm_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcm-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds.Hour24otnTcmThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds.Hour24otnTcmThreshold',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnTcmThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnTcmThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcm-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds',
            False, 
            [
            _MetaInfoClassMember('hour24otn-tcm-threshold', REFERENCE_LIST, 'Hour24otnTcmThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds.Hour24otnTcmThreshold', 
                [], [], 
                '''                none
                ''',
                'hour24otn_tcm_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcm-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm',
            False, 
            [
            _MetaInfoClassMember('tcm-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                TCM number
                ''',
                'tcm_number',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('hour24otn-tcm-reports', REFERENCE_CLASS, 'Hour24otnTcmReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'hour24otn_tcm_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24otn-tcm-thresholds', REFERENCE_CLASS, 'Hour24otnTcmThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'hour24otn_tcm_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcm',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms',
            False, 
            [
            _MetaInfoClassMember('hour24otn-tcm', REFERENCE_LIST, 'Hour24otnTcm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm', 
                [], [], 
                '''                configure otn g709 tcm's performance
                monitoring
                ''',
                'hour24otn_tcm',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'hour24otn-tcms',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports.Minute15OpticsReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports.Minute15OpticsReport',
            False, 
            [
            _MetaInfoClassMember('optics-report', REFERENCE_ENUM_CLASS, 'OpticsReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OpticsReport_Enum', 
                [], [], 
                '''                Optics Report Type
                ''',
                'optics_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-optics-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports',
            False, 
            [
            _MetaInfoClassMember('minute15-optics-report', REFERENCE_LIST, 'Minute15OpticsReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports.Minute15OpticsReport', 
                [], [], 
                '''                none
                ''',
                'minute15_optics_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-optics-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds.Minute15OpticsThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds.Minute15OpticsThreshold',
            False, 
            [
            _MetaInfoClassMember('optics-threshold', REFERENCE_ENUM_CLASS, 'OpticsThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OpticsThreshold_Enum', 
                [], [], 
                '''                Optics Threshold Type
                ''',
                'optics_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('optics-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Optics Threshold Value
                ''',
                'optics_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-optics-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds',
            False, 
            [
            _MetaInfoClassMember('minute15-optics-threshold', REFERENCE_LIST, 'Minute15OpticsThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds.Minute15OpticsThreshold', 
                [], [], 
                '''                none
                ''',
                'minute15_optics_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-optics-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics',
            False, 
            [
            _MetaInfoClassMember('minute15-optics-reports', REFERENCE_CLASS, 'Minute15OpticsReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports', 
                [], [], 
                '''                set optics TCA reporting status
                ''',
                'minute15_optics_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15-optics-thresholds', REFERENCE_CLASS, 'Minute15OpticsThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds', 
                [], [], 
                '''                Configure threshold on optics parameters
                ''',
                'minute15_optics_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-optics',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports.Minute15fecReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports.Minute15fecReport',
            False, 
            [
            _MetaInfoClassMember('fec-report', REFERENCE_ENUM_CLASS, 'FecReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'FecReport_Enum', 
                [], [], 
                '''                Fec Report Type
                ''',
                'fec_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Fec Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15fec-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports',
            False, 
            [
            _MetaInfoClassMember('minute15fec-report', REFERENCE_LIST, 'Minute15fecReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports.Minute15fecReport', 
                [], [], 
                '''                none
                ''',
                'minute15fec_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15fec-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds.Minute15fecThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds.Minute15fecThreshold',
            False, 
            [
            _MetaInfoClassMember('fec-threshold', REFERENCE_ENUM_CLASS, 'FecThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'FecThreshold_Enum', 
                [], [], 
                '''                Fec Threshold Type
                ''',
                'fec_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('fec-threshold-value', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Fec Threshold Value
                ''',
                'fec_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15fec-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds',
            False, 
            [
            _MetaInfoClassMember('minute15fec-threshold', REFERENCE_LIST, 'Minute15fecThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds.Minute15fecThreshold', 
                [], [], 
                '''                none
                ''',
                'minute15fec_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15fec-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec',
            False, 
            [
            _MetaInfoClassMember('minute15fec-reports', REFERENCE_CLASS, 'Minute15fecReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports', 
                [], [], 
                '''                set fec TCA reporting status
                ''',
                'minute15fec_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15fec-thresholds', REFERENCE_CLASS, 'Minute15fecThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds', 
                [], [], 
                '''                Configure fec threshold
                ''',
                'minute15fec_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15fec',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes.Min15OtnThresh' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes.Min15OtnThresh',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-thresh',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes',
            False, 
            [
            _MetaInfoClassMember('min15-otn-thresh', REFERENCE_LIST, 'Min15OtnThresh' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes.Min15OtnThresh', 
                [], [], 
                '''                none
                ''',
                'min15_otn_thresh',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-threshes',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports.Minute15otnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports.Minute15otnReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports',
            False, 
            [
            _MetaInfoClassMember('minute15otn-report', REFERENCE_LIST, 'Minute15otnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports.Minute15otnReport', 
                [], [], 
                '''                none
                ''',
                'minute15otn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn',
            False, 
            [
            _MetaInfoClassMember('min15-otn-threshes', REFERENCE_CLASS, 'Min15OtnThreshes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'min15_otn_threshes',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15otn-reports', REFERENCE_CLASS, 'Minute15otnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'minute15otn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15',
            False, 
            [
            _MetaInfoClassMember('minute15-optics', REFERENCE_CLASS, 'Minute15Optics' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics', 
                [], [], 
                '''                Configure optics performance monitoring
                ''',
                'minute15_optics',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15fec', REFERENCE_CLASS, 'Minute15fec' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec', 
                [], [], 
                '''                Configure fec g709 performance monitoring
                ''',
                'minute15fec',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15otn', REFERENCE_CLASS, 'Minute15otn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn', 
                [], [], 
                '''                configure otn g709 performance monitoring
                ''',
                'minute15otn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports.Minute15GfpReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports.Minute15GfpReport',
            False, 
            [
            _MetaInfoClassMember('gfp-report', REFERENCE_ENUM_CLASS, 'GfpReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'GfpReport_Enum', 
                [], [], 
                '''                Gfp Report Type
                ''',
                'gfp_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports',
            False, 
            [
            _MetaInfoClassMember('minute15-gfp-report', REFERENCE_LIST, 'Minute15GfpReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports.Minute15GfpReport', 
                [], [], 
                '''                none
                ''',
                'minute15_gfp_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds.Minute15GfpThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds.Minute15GfpThreshold',
            False, 
            [
            _MetaInfoClassMember('gfp-threshold', REFERENCE_ENUM_CLASS, 'GfpThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'GfpThreshold_Enum', 
                [], [], 
                '''                Gfp Threshold Type
                ''',
                'gfp_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('gfp-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Gfp Threshold Value
                ''',
                'gfp_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds',
            False, 
            [
            _MetaInfoClassMember('minute15-gfp-threshold', REFERENCE_LIST, 'Minute15GfpThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds.Minute15GfpThreshold', 
                [], [], 
                '''                none
                ''',
                'minute15_gfp_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp',
            False, 
            [
            _MetaInfoClassMember('minute15-gfp-reports', REFERENCE_CLASS, 'Minute15GfpReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports', 
                [], [], 
                '''                set gfp TCA reporting status
                ''',
                'minute15_gfp_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15-gfp-thresholds', REFERENCE_CLASS, 'Minute15GfpThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds', 
                [], [], 
                '''                Configure threshold on gfp parameters
                ''',
                'minute15_gfp_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp',
            False, 
            [
            _MetaInfoClassMember('minute15-gfp', REFERENCE_CLASS, 'Minute15Gfp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp', 
                [], [], 
                '''                Configure gfp performance monitoring
                ''',
                'minute15_gfp',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-gfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes.Min15OtnPathThresh' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes.Min15OtnPathThresh',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-path-thresh',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes',
            False, 
            [
            _MetaInfoClassMember('min15-otn-path-thresh', REFERENCE_LIST, 'Min15OtnPathThresh' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes.Min15OtnPathThresh', 
                [], [], 
                '''                none
                ''',
                'min15_otn_path_thresh',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-path-threshes',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports.Minute15otnPathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports.Minute15otnPathReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports',
            False, 
            [
            _MetaInfoClassMember('minute15otn-path-report', REFERENCE_LIST, 'Minute15otnPathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports.Minute15otnPathReport', 
                [], [], 
                '''                none
                ''',
                'minute15otn_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath',
            False, 
            [
            _MetaInfoClassMember('min15-otn-path-threshes', REFERENCE_CLASS, 'Min15OtnPathThreshes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'min15_otn_path_threshes',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15otn-path-reports', REFERENCE_CLASS, 'Minute15otnPathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'minute15otn_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path',
            False, 
            [
            _MetaInfoClassMember('minute15otn-path', REFERENCE_CLASS, 'Minute15otnPath' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath', 
                [], [], 
                '''                configure otn g709 performance monitoring
                ''',
                'minute15otn_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes.Min15OtnTcmThresh' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes.Min15OtnTcmThresh',
            False, 
            [
            _MetaInfoClassMember('otn-threshold', REFERENCE_ENUM_CLASS, 'OtnTcmThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnTcmThreshold_Enum', 
                [], [], 
                '''                Otn Threshold Type
                ''',
                'otn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('otn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Otn Threshold Value
                ''',
                'otn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-tcm-thresh',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes',
            False, 
            [
            _MetaInfoClassMember('min15-otn-tcm-thresh', REFERENCE_LIST, 'Min15OtnTcmThresh' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes.Min15OtnTcmThresh', 
                [], [], 
                '''                none
                ''',
                'min15_otn_tcm_thresh',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'min15-otn-tcm-threshes',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports.Minute15otnTcmReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports.Minute15otnTcmReport',
            False, 
            [
            _MetaInfoClassMember('otn-report', REFERENCE_ENUM_CLASS, 'OtnTcmReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OtnTcmReport_Enum', 
                [], [], 
                '''                Otn Report Type
                ''',
                'otn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Otn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-tcm-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports',
            False, 
            [
            _MetaInfoClassMember('minute15otn-tcm-report', REFERENCE_LIST, 'Minute15otnTcmReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports.Minute15otnTcmReport', 
                [], [], 
                '''                none
                ''',
                'minute15otn_tcm_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-tcm-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm',
            False, 
            [
            _MetaInfoClassMember('tcm-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                TCM number
                ''',
                'tcm_number',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('min15-otn-tcm-threshes', REFERENCE_CLASS, 'Min15OtnTcmThreshes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes', 
                [], [], 
                '''                Configure threshold on otn parameters
                ''',
                'min15_otn_tcm_threshes',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15otn-tcm-reports', REFERENCE_CLASS, 'Minute15otnTcmReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports', 
                [], [], 
                '''                set otn TCA reporting status
                ''',
                'minute15otn_tcm_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-tcm',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms',
            False, 
            [
            _MetaInfoClassMember('minute15otn-tcm', REFERENCE_LIST, 'Minute15otnTcm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm', 
                [], [], 
                '''                configure otn g709 tcm's performance
                monitoring
                ''',
                'minute15otn_tcm',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'minute15otn-tcms',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports.OcHour24OcnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports.OcHour24OcnReport',
            False, 
            [
            _MetaInfoClassMember('ocn-report', REFERENCE_ENUM_CLASS, 'OcnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnReport_Enum', 
                [], [], 
                '''                Ocn Report Type
                ''',
                'ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Ocn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24-ocn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports',
            False, 
            [
            _MetaInfoClassMember('oc-hour24-ocn-report', REFERENCE_LIST, 'OcHour24OcnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports.OcHour24OcnReport', 
                [], [], 
                '''                none
                ''',
                'oc_hour24_ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24-ocn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds.OcHour24OcnThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds.OcHour24OcnThreshold',
            False, 
            [
            _MetaInfoClassMember('ocn-threshold', REFERENCE_ENUM_CLASS, 'OcnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnThreshold_Enum', 
                [], [], 
                '''                Ocn Threshold Type
                ''',
                'ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ocn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ocn Thresh Value
                ''',
                'ocn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24-ocn-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds',
            False, 
            [
            _MetaInfoClassMember('oc-hour24-ocn-threshold', REFERENCE_LIST, 'OcHour24OcnThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds.OcHour24OcnThreshold', 
                [], [], 
                '''                none
                ''',
                'oc_hour24_ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24-ocn-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn',
            False, 
            [
            _MetaInfoClassMember('oc-hour24-ocn-reports', REFERENCE_CLASS, 'OcHour24OcnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports', 
                [], [], 
                '''                set ocn TCA reporting status
                ''',
                'oc_hour24_ocn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('oc-hour24-ocn-thresholds', REFERENCE_CLASS, 'OcHour24OcnThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds', 
                [], [], 
                '''                Configure threshold on ocn parameters
                ''',
                'oc_hour24_ocn_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24-ocn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24',
            False, 
            [
            _MetaInfoClassMember('oc-hour24-ocn', REFERENCE_CLASS, 'OcHour24Ocn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn', 
                [], [], 
                '''                Configure ocn performance monitoring
                ''',
                'oc_hour24_ocn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports.OcMinute15OcnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports.OcMinute15OcnReport',
            False, 
            [
            _MetaInfoClassMember('ocn-report', REFERENCE_ENUM_CLASS, 'OcnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnReport_Enum', 
                [], [], 
                '''                Ocn Report Type
                ''',
                'ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Ocn Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15-ocn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports',
            False, 
            [
            _MetaInfoClassMember('oc-minute15-ocn-report', REFERENCE_LIST, 'OcMinute15OcnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports.OcMinute15OcnReport', 
                [], [], 
                '''                none
                ''',
                'oc_minute15_ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15-ocn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds.OcMinute15OcnThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds.OcMinute15OcnThreshold',
            False, 
            [
            _MetaInfoClassMember('ocn-threshold', REFERENCE_ENUM_CLASS, 'OcnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnThreshold_Enum', 
                [], [], 
                '''                Ocn Threshold Type
                ''',
                'ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ocn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ocn Threshold Value
                ''',
                'ocn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15-ocn-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds',
            False, 
            [
            _MetaInfoClassMember('oc-minute15-ocn-threshold', REFERENCE_LIST, 'OcMinute15OcnThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds.OcMinute15OcnThreshold', 
                [], [], 
                '''                none
                ''',
                'oc_minute15_ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15-ocn-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn',
            False, 
            [
            _MetaInfoClassMember('oc-minute15-ocn-reports', REFERENCE_CLASS, 'OcMinute15OcnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports', 
                [], [], 
                '''                set ocn TCA reporting status
                ''',
                'oc_minute15_ocn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('oc-minute15-ocn-thresholds', REFERENCE_CLASS, 'OcMinute15OcnThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds', 
                [], [], 
                '''                Configure threshold on ocn parameters
                ''',
                'oc_minute15_ocn_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15-ocn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15',
            False, 
            [
            _MetaInfoClassMember('oc-minute15-ocn', REFERENCE_CLASS, 'OcMinute15Ocn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn', 
                [], [], 
                '''                Configure ocn performance monitoring
                ''',
                'oc_minute15_ocn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'oc-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports.SonetHour24OcnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports.SonetHour24OcnReport',
            False, 
            [
            _MetaInfoClassMember('ocn-report', REFERENCE_ENUM_CLASS, 'OcnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnReport_Enum', 
                [], [], 
                '''                Ocn Report Type
                ''',
                'ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-ocn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-ocn-report', REFERENCE_LIST, 'SonetHour24OcnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports.SonetHour24OcnReport', 
                [], [], 
                '''                none
                ''',
                'sonet_hour24_ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-ocn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds.SonetHour24OcnThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds.SonetHour24OcnThreshold',
            False, 
            [
            _MetaInfoClassMember('ocn-threshold', REFERENCE_ENUM_CLASS, 'OcnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnThreshold_Enum', 
                [], [], 
                '''                Ocn Threshold Type
                ''',
                'ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ocn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ocn Thresh Value
                ''',
                'ocn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-ocn-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-ocn-threshold', REFERENCE_LIST, 'SonetHour24OcnThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds.SonetHour24OcnThreshold', 
                [], [], 
                '''                none
                ''',
                'sonet_hour24_ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-ocn-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-ocn-reports', REFERENCE_CLASS, 'SonetHour24OcnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports', 
                [], [], 
                '''                set ocn TCA reporting status
                ''',
                'sonet_hour24_ocn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-hour24-ocn-thresholds', REFERENCE_CLASS, 'SonetHour24OcnThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds', 
                [], [], 
                '''                Configure threshold on ocn parameters
                ''',
                'sonet_hour24_ocn_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-ocn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports.SonetHour24PathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports.SonetHour24PathReport',
            False, 
            [
            _MetaInfoClassMember('path-report', REFERENCE_ENUM_CLASS, 'PathReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'PathReport_Enum', 
                [], [], 
                '''                Path Report Type
                ''',
                'path_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-path-report', REFERENCE_LIST, 'SonetHour24PathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports.SonetHour24PathReport', 
                [], [], 
                '''                none
                ''',
                'sonet_hour24_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds.SonetHour24PathThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds.SonetHour24PathThreshold',
            False, 
            [
            _MetaInfoClassMember('path-threshold', REFERENCE_ENUM_CLASS, 'PathThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'PathThreshold_Enum', 
                [], [], 
                '''                Path Threshold Type
                ''',
                'path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('path-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Path Thresh Value
                ''',
                'path_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-path-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-path-threshold', REFERENCE_LIST, 'SonetHour24PathThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds.SonetHour24PathThreshold', 
                [], [], 
                '''                none
                ''',
                'sonet_hour24_path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-path-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-path-reports', REFERENCE_CLASS, 'SonetHour24PathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports', 
                [], [], 
                '''                set Path TCA reporting status
                ''',
                'sonet_hour24_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-hour24-path-thresholds', REFERENCE_CLASS, 'SonetHour24PathThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds', 
                [], [], 
                '''                Configure threshold on Path parameters
                ''',
                'sonet_hour24_path_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24',
            False, 
            [
            _MetaInfoClassMember('sonet-hour24-ocn', REFERENCE_CLASS, 'SonetHour24Ocn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn', 
                [], [], 
                '''                Configure ocn performance monitoring
                ''',
                'sonet_hour24_ocn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-hour24-path', REFERENCE_CLASS, 'SonetHour24Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path', 
                [], [], 
                '''                Configure Path performance monitoring
                ''',
                'sonet_hour24_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports.SonetMinute15OcnReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports.SonetMinute15OcnReport',
            False, 
            [
            _MetaInfoClassMember('ocn-report', REFERENCE_ENUM_CLASS, 'OcnReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnReport_Enum', 
                [], [], 
                '''                Ocn Report Type
                ''',
                'ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-ocn-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-ocn-report', REFERENCE_LIST, 'SonetMinute15OcnReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports.SonetMinute15OcnReport', 
                [], [], 
                '''                none
                ''',
                'sonet_minute15_ocn_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-ocn-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds.SonetMinute15OcnThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds.SonetMinute15OcnThreshold',
            False, 
            [
            _MetaInfoClassMember('ocn-threshold', REFERENCE_ENUM_CLASS, 'OcnThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'OcnThreshold_Enum', 
                [], [], 
                '''                Ocn Threshold Type
                ''',
                'ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('ocn-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ocn Threshold Value
                ''',
                'ocn_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-ocn-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-ocn-threshold', REFERENCE_LIST, 'SonetMinute15OcnThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds.SonetMinute15OcnThreshold', 
                [], [], 
                '''                none
                ''',
                'sonet_minute15_ocn_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-ocn-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-ocn-reports', REFERENCE_CLASS, 'SonetMinute15OcnReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports', 
                [], [], 
                '''                set ocn TCA reporting status
                ''',
                'sonet_minute15_ocn_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-minute15-ocn-thresholds', REFERENCE_CLASS, 'SonetMinute15OcnThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds', 
                [], [], 
                '''                Configure threshold on ocn parameters
                ''',
                'sonet_minute15_ocn_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-ocn',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports.SonetMinute15PathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports.SonetMinute15PathReport',
            False, 
            [
            _MetaInfoClassMember('path-report', REFERENCE_ENUM_CLASS, 'PathReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'PathReport_Enum', 
                [], [], 
                '''                Path Report Type
                ''',
                'path_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-path-report', REFERENCE_LIST, 'SonetMinute15PathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports.SonetMinute15PathReport', 
                [], [], 
                '''                none
                ''',
                'sonet_minute15_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds.SonetMinute15PathThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds.SonetMinute15PathThreshold',
            False, 
            [
            _MetaInfoClassMember('path-threshold', REFERENCE_ENUM_CLASS, 'PathThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'PathThreshold_Enum', 
                [], [], 
                '''                Path Threshold Type
                ''',
                'path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('path-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Path Threshold Value
                ''',
                'path_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-path-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-path-threshold', REFERENCE_LIST, 'SonetMinute15PathThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds.SonetMinute15PathThreshold', 
                [], [], 
                '''                none
                ''',
                'sonet_minute15_path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-path-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-path-reports', REFERENCE_CLASS, 'SonetMinute15PathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports', 
                [], [], 
                '''                set Path TCA reporting status
                ''',
                'sonet_minute15_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-minute15-path-thresholds', REFERENCE_CLASS, 'SonetMinute15PathThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds', 
                [], [], 
                '''                Configure threshold on Path parameters
                ''',
                'sonet_minute15_path_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15',
            False, 
            [
            _MetaInfoClassMember('sonet-minute15-ocn', REFERENCE_CLASS, 'SonetMinute15Ocn' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn', 
                [], [], 
                '''                Configure ocn performance monitoring
                ''',
                'sonet_minute15_ocn',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-minute15-path', REFERENCE_CLASS, 'SonetMinute15Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path', 
                [], [], 
                '''                Configure Path performance monitoring
                ''',
                'sonet_minute15_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sonet-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports.StmHour24StmReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports.StmHour24StmReport',
            False, 
            [
            _MetaInfoClassMember('stm-report', REFERENCE_ENUM_CLASS, 'StmReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StmReport_Enum', 
                [], [], 
                '''                Stm Report Type
                ''',
                'stm_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Stm Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24-stm-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports',
            False, 
            [
            _MetaInfoClassMember('stm-hour24-stm-report', REFERENCE_LIST, 'StmHour24StmReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports.StmHour24StmReport', 
                [], [], 
                '''                none
                ''',
                'stm_hour24_stm_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24-stm-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds.StmHour24StmThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds.StmHour24StmThreshold',
            False, 
            [
            _MetaInfoClassMember('stm-threshold', REFERENCE_ENUM_CLASS, 'StmThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StmThreshold_Enum', 
                [], [], 
                '''                Stm Threshold Type
                ''',
                'stm_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('stm-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Stm Thresh Value
                ''',
                'stm_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24-stm-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds',
            False, 
            [
            _MetaInfoClassMember('stm-hour24-stm-threshold', REFERENCE_LIST, 'StmHour24StmThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds.StmHour24StmThreshold', 
                [], [], 
                '''                none
                ''',
                'stm_hour24_stm_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24-stm-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm',
            False, 
            [
            _MetaInfoClassMember('stm-hour24-stm-reports', REFERENCE_CLASS, 'StmHour24StmReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports', 
                [], [], 
                '''                set stm TCA reporting status
                ''',
                'stm_hour24_stm_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('stm-hour24-stm-thresholds', REFERENCE_CLASS, 'StmHour24StmThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds', 
                [], [], 
                '''                Configure threshold on stm parameters
                ''',
                'stm_hour24_stm_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24-stm',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24',
            False, 
            [
            _MetaInfoClassMember('stm-hour24-stm', REFERENCE_CLASS, 'StmHour24Stm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm', 
                [], [], 
                '''                Configure stm performance monitoring
                ''',
                'stm_hour24_stm',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports.StmMinute15StmReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports.StmMinute15StmReport',
            False, 
            [
            _MetaInfoClassMember('stm-report', REFERENCE_ENUM_CLASS, 'StmReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StmReport_Enum', 
                [], [], 
                '''                Stm Report Type
                ''',
                'stm_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Stm Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15-stm-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports',
            False, 
            [
            _MetaInfoClassMember('stm-minute15-stm-report', REFERENCE_LIST, 'StmMinute15StmReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports.StmMinute15StmReport', 
                [], [], 
                '''                none
                ''',
                'stm_minute15_stm_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15-stm-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds.StmMinute15StmThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds.StmMinute15StmThreshold',
            False, 
            [
            _MetaInfoClassMember('stm-threshold', REFERENCE_ENUM_CLASS, 'StmThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StmThreshold_Enum', 
                [], [], 
                '''                Stm Threshold Type
                ''',
                'stm_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('stm-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Stm Threshold Value
                ''',
                'stm_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15-stm-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds',
            False, 
            [
            _MetaInfoClassMember('stm-minute15-stm-threshold', REFERENCE_LIST, 'StmMinute15StmThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds.StmMinute15StmThreshold', 
                [], [], 
                '''                none
                ''',
                'stm_minute15_stm_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15-stm-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm',
            False, 
            [
            _MetaInfoClassMember('stm-minute15-stm-reports', REFERENCE_CLASS, 'StmMinute15StmReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports', 
                [], [], 
                '''                set stm TCA reporting status
                ''',
                'stm_minute15_stm_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('stm-minute15-stm-thresholds', REFERENCE_CLASS, 'StmMinute15StmThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds', 
                [], [], 
                '''                Configure threshold on stm parameters
                ''',
                'stm_minute15_stm_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15-stm',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15',
            False, 
            [
            _MetaInfoClassMember('stm-minute15-stm', REFERENCE_CLASS, 'StmMinute15Stm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm', 
                [], [], 
                '''                Configure stm performance monitoring
                ''',
                'stm_minute15_stm',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'stm-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports.StsHour24PathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports.StsHour24PathReport',
            False, 
            [
            _MetaInfoClassMember('path-report', REFERENCE_ENUM_CLASS, 'StsReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StsReport_Enum', 
                [], [], 
                '''                Path Report Type
                ''',
                'path_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Path Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports',
            False, 
            [
            _MetaInfoClassMember('sts-hour24-path-report', REFERENCE_LIST, 'StsHour24PathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports.StsHour24PathReport', 
                [], [], 
                '''                none
                ''',
                'sts_hour24_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds.StsHour24PathThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds.StsHour24PathThreshold',
            False, 
            [
            _MetaInfoClassMember('path-threshold', REFERENCE_ENUM_CLASS, 'StsThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StsThreshold_Enum', 
                [], [], 
                '''                Path Threshold Type
                ''',
                'path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('path-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Path Thresh Value
                ''',
                'path_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24-path-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds',
            False, 
            [
            _MetaInfoClassMember('sts-hour24-path-threshold', REFERENCE_LIST, 'StsHour24PathThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds.StsHour24PathThreshold', 
                [], [], 
                '''                none
                ''',
                'sts_hour24_path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24-path-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path',
            False, 
            [
            _MetaInfoClassMember('sts-hour24-path-reports', REFERENCE_CLASS, 'StsHour24PathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports', 
                [], [], 
                '''                set Path TCA reporting status
                ''',
                'sts_hour24_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sts-hour24-path-thresholds', REFERENCE_CLASS, 'StsHour24PathThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds', 
                [], [], 
                '''                Configure threshold on Path parameters
                ''',
                'sts_hour24_path_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24',
            False, 
            [
            _MetaInfoClassMember('sts-hour24-path', REFERENCE_CLASS, 'StsHour24Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path', 
                [], [], 
                '''                Configure Path performance monitoring
                ''',
                'sts_hour24_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-hour24',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports.StsMinute15PathReport' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports.StsMinute15PathReport',
            False, 
            [
            _MetaInfoClassMember('path-report', REFERENCE_ENUM_CLASS, 'StsReport_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StsReport_Enum', 
                [], [], 
                '''                Path Report Type
                ''',
                'path_report',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'Report_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'Report_Enum', 
                [], [], 
                '''                Path Report
                ''',
                'enable',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15-path-report',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports',
            False, 
            [
            _MetaInfoClassMember('sts-minute15-path-report', REFERENCE_LIST, 'StsMinute15PathReport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports.StsMinute15PathReport', 
                [], [], 
                '''                none
                ''',
                'sts_minute15_path_report',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15-path-reports',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds.StsMinute15PathThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds.StsMinute15PathThreshold',
            False, 
            [
            _MetaInfoClassMember('path-threshold', REFERENCE_ENUM_CLASS, 'StsThreshold_Enum' , 'ydk.models.pmengine.Cisco_IOS_XR_pmengine_cfg', 'StsThreshold_Enum', 
                [], [], 
                '''                Path Threshold Type
                ''',
                'path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', True),
            _MetaInfoClassMember('path-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Path Threshold Value
                ''',
                'path_threshold_value',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15-path-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds',
            False, 
            [
            _MetaInfoClassMember('sts-minute15-path-threshold', REFERENCE_LIST, 'StsMinute15PathThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds.StsMinute15PathThreshold', 
                [], [], 
                '''                none
                ''',
                'sts_minute15_path_threshold',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15-path-thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path',
            False, 
            [
            _MetaInfoClassMember('sts-minute15-path-reports', REFERENCE_CLASS, 'StsMinute15PathReports' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports', 
                [], [], 
                '''                set Path TCA reporting status
                ''',
                'sts_minute15_path_reports',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sts-minute15-path-thresholds', REFERENCE_CLASS, 'StsMinute15PathThresholds' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds', 
                [], [], 
                '''                Configure threshold on Path parameters
                ''',
                'sts_minute15_path_thresholds',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15',
            False, 
            [
            _MetaInfoClassMember('sts-minute15-path', REFERENCE_CLASS, 'StsMinute15Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path', 
                [], [], 
                '''                Configure Path performance monitoring
                ''',
                'sts_minute15_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'sts-minute15',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement',
            False, 
            [
            _MetaInfoClassMember('ethernet-hour24', REFERENCE_CLASS, 'EthernetHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24', 
                [], [], 
                '''                Configure pm parameters of 24 hour interval
                ''',
                'ethernet_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('ethernet-minute15', REFERENCE_CLASS, 'EthernetMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15', 
                [], [], 
                '''                set opr min threshold
                ''',
                'ethernet_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('ho-vc-hour24', REFERENCE_CLASS, 'HoVcHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24', 
                [], [], 
                '''                set HO_VC threshold
                ''',
                'ho_vc_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('ho-vc-minute15', REFERENCE_CLASS, 'HoVcMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15', 
                [], [], 
                '''                set HO_VC threshold
                ''',
                'ho_vc_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24', REFERENCE_CLASS, 'Hour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24', 
                [], [], 
                '''                Configure pm parameters of 24 hour interval
                ''',
                'hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24-gfp', REFERENCE_CLASS, 'Hour24Gfp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp', 
                [], [], 
                '''                Configure pm parameters of gfp 24 hour interval
                ''',
                'hour24_gfp',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24-path', REFERENCE_CLASS, 'Hour24Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path', 
                [], [], 
                '''                Configure pm parameters of pathmonitor 24 hour
                interval
                ''',
                'hour24_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('hour24otn-tcms', REFERENCE_CLASS, 'Hour24otnTcms' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms', 
                [], [], 
                '''                Configure pm parameters of tcm's 24 hour
                interval
                ''',
                'hour24otn_tcms',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15', REFERENCE_CLASS, 'Minute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15', 
                [], [], 
                '''                set opr min threshold
                ''',
                'minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15-gfp', REFERENCE_CLASS, 'Minute15Gfp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp', 
                [], [], 
                '''                set opr min threshold
                ''',
                'minute15_gfp',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15-path', REFERENCE_CLASS, 'Minute15Path' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path', 
                [], [], 
                '''                set opr min threshold
                ''',
                'minute15_path',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('minute15otn-tcms', REFERENCE_CLASS, 'Minute15otnTcms' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms', 
                [], [], 
                '''                set opr min threshold
                ''',
                'minute15otn_tcms',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('oc-hour24', REFERENCE_CLASS, 'OcHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24', 
                [], [], 
                '''                set Oc threshold
                ''',
                'oc_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('oc-minute15', REFERENCE_CLASS, 'OcMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15', 
                [], [], 
                '''                set OC threshold
                ''',
                'oc_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-hour24', REFERENCE_CLASS, 'SonetHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24', 
                [], [], 
                '''                set Sonet threshold
                ''',
                'sonet_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sonet-minute15', REFERENCE_CLASS, 'SonetMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15', 
                [], [], 
                '''                set Sonet threshold
                ''',
                'sonet_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('stm-hour24', REFERENCE_CLASS, 'StmHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24', 
                [], [], 
                '''                set STM threshold
                ''',
                'stm_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('stm-minute15', REFERENCE_CLASS, 'StmMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15', 
                [], [], 
                '''                set STM threshold
                ''',
                'stm_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sts-hour24', REFERENCE_CLASS, 'StsHour24' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24', 
                [], [], 
                '''                set STS threshold
                ''',
                'sts_hour24',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('sts-minute15', REFERENCE_CLASS, 'StsMinute15' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15', 
                [], [], 
                '''                set STS threshold
                ''',
                'sts_minute15',
                'Cisco-IOS-XR-pmengine-cfg', False),
            ],
            'Cisco-IOS-XR-pmengine-cfg',
            'performance-management',
            _yang_ns._namespaces['Cisco-IOS-XR-pmengine-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PseudowireEther' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PseudowireEther',
            False, 
            [
            _MetaInfoClassMember('generic-interface-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Name of the interface list
                ''',
                'generic_interface_list',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2-overhead', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                PW Ether L2 overhead requirement
                ''',
                'l2_overhead',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-ether',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.PseudowireIw' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.PseudowireIw',
            False, 
            [
            _MetaInfoClassMember('generic-interface-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Name of the interface list
                ''',
                'generic_interface_list',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('l2-overhead', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                L2 overhead size in bytes
                ''',
                'l2_overhead',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'pseudowire-iw',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession.Attachment' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession.Attachment',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'SpanTrafficDirection_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanTrafficDirection_Enum', 
                [], [], 
                '''                Specify the direction of traffic to replicate
                (optional)
                ''',
                'direction',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('port-level-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable port level traffic mirroring
                ''',
                'port_level_enable',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClass_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass_Enum', 
                [], [], 
                '''                Session Class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', True),
            _MetaInfoClassMember('acl', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ACL matching for traffic mirroring
                ''',
                'acl',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('attachment', REFERENCE_CLASS, 'Attachment' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession.Attachment', 
                [], [], 
                '''                Attach the interface to a Monitor Session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('mirror-first', ATTRIBUTE, 'int' , None, None, 
                [(1, 10000)], [], 
                '''                Mirror a specified number of bytes from start of
                packet
                ''',
                'mirror_first',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'SpanMirrorInterval_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMirrorInterval_Enum', 
                [], [], 
                '''                Specify the mirror interval
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions',
            False, 
            [
            _MetaInfoClassMember('span-monitor-session', REFERENCE_LIST, 'SpanMonitorSession' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession', 
                [], [], 
                '''                Configuration for a particular class of Monitor
                Session
                ''',
                'span_monitor_session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Statistics' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Statistics',
            False, 
            [
            _MetaInfoClassMember('load-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 600)], [], 
                '''                Specify interval for load calculation for an
                interface
                ''',
                'load_interval',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-statsd-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinInterval' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinInterval',
            False, 
            [
            _MetaInfoClassMember('interval-ms', ATTRIBUTE, 'int' , None, None, 
                [(3, 5000)], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-us', ATTRIBUTE, 'int' , None, None, 
                [(3000, 5000000)], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinIntervalStandby' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinIntervalStandby',
            False, 
            [
            _MetaInfoClassMember('interval-standby-ms', ATTRIBUTE, 'int' , None, None, 
                [(3, 5000)], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval_standby_ms',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interval-standby-us', ATTRIBUTE, 'int' , None, None, 
                [(3000, 5000000)], [], 
                '''                Hello interval in micro-seconds
                ''',
                'interval_standby_us',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'min-interval-standby',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-interval', REFERENCE_CLASS, 'MinInterval' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinInterval', 
                [], [], 
                '''                Hello interval, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('min-interval-standby', REFERENCE_CLASS, 'MinIntervalStandby' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinIntervalStandby', 
                [], [], 
                '''                Hello interval for standby transport profile
                LSP, either in milli-seconds or in
                micro-seconds
                ''',
                'min_interval_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('multiplier-standby', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                Detect multiplier for standby transport
                profile LSP
                ''',
                'multiplier_standby',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Destination' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Destination',
            False, 
            [
            _MetaInfoClassMember('global-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Numeric global identifier
                ''',
                'global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Node identifier in IPv4 address format
                ''',
                'node_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Numeric tunnel identifier
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault.ProtectionTrigger' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault.ProtectionTrigger',
            False, 
            [
            _MetaInfoClassMember('ais', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable protection switching due to AIS event
                ''',
                'ais',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ldi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable protection switching due to LDI event
                ''',
                'ldi',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lkr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable protection switching due to LKR event
                ''',
                'lkr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'protection-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter transport profile tunnel fault
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protection-trigger', REFERENCE_CLASS, 'ProtectionTrigger' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault.ProtectionTrigger', 
                [], [], 
                '''                OAM events that trigger protection switching
                ''',
                'protection_trigger',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fault',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp.OutLabel' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp.OutLabel',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                MPLS label
                ''',
                'label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Transport profile identifier of outgoing link
                ''',
                'link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'out-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 4015)], [], 
                '''                Incoming MPLS label of the protect LSP
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockout', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable lockout of protect LSP
                ''',
                'lockout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP Identifier of the protect LSP
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', REFERENCE_CLASS, 'OutLabel' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp.OutLabel', 
                [], [], 
                '''                Outgoing MPLS label of the protect LSP
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'protect-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp.OutLabel' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp.OutLabel',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                MPLS label
                ''',
                'label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Transport profile identifier of outgoing link
                ''',
                'link',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'out-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 4015)], [], 
                '''                Incoming MPLS label of the working LSP
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockout', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable lockout of working LSP
                ''',
                'lockout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP Identifier of the working LSP
                ''',
                'lsp_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('out-label', REFERENCE_CLASS, 'OutLabel' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp.OutLabel', 
                [], [], 
                '''                Outgoing MPLS label of the working LSP
                ''',
                'out_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'working-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Destination', 
                [], [], 
                '''                Node identifier and optional global identifier
                and tunnel identifier at destination
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault', REFERENCE_CLASS, 'Fault' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault', 
                [], [], 
                '''                Fault management
                ''',
                'fault',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protect-lsp', REFERENCE_CLASS, 'ProtectLsp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp', 
                [], [], 
                '''                Protect LSP
                ''',
                'protect_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Transport profile node identifier in IPv4
                address format
                ''',
                'source',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('working-lsp', REFERENCE_CLASS, 'WorkingLsp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp', 
                [], [], 
                '''                Working LSP
                ''',
                'working_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transport-profile-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AdminMode' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AdminMode',
            False, 
            [
            _MetaInfoClassMember('deactivate-tunnel', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Performs signalling operation to deactivate
                optical tunnel
                ''',
                'deactivate_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'admin-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AffinityMask' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AffinityMask',
            False, 
            [
            _MetaInfoClassMember('affinity', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity flags
                ''',
                'affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Affinity mask
                ''',
                'mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'affinity-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.AdjustmentThreshold' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.AdjustmentThreshold',
            False, 
            [
            _MetaInfoClassMember('adjustment-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Bandwidth change percent to trigger
                adjustment
                ''',
                'adjustment_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('adjustment-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(10, 4294967295)], [], 
                '''                Bandwidth change value to trigger adjustment
                (kbps)
                ''',
                'adjustment_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'adjustment-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.BandwidthLimits' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.BandwidthLimits',
            False, 
            [
            _MetaInfoClassMember('bandwidth-max-limit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Set maximum bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_max_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-min-limit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Set minimum bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_min_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Overflow' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Overflow',
            False, 
            [
            _MetaInfoClassMember('overflow-threshold-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Number of consecutive collections exceeding
                threshold
                ''',
                'overflow_threshold_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Bandwidth change percent to trigger an
                overflow
                ''',
                'overflow_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(10, 4294967295)], [], 
                '''                Bandwidth change value to trigger an overflow
                (kbps)
                ''',
                'overflow_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'overflow',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Underflow' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Underflow',
            False, 
            [
            _MetaInfoClassMember('underflow-threshold-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Number of consecutive collections exceeding
                threshold
                ''',
                'underflow_threshold_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Bandwidth change percent to trigger an
                underflow
                ''',
                'underflow_threshold_percent',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow-threshold-value', ATTRIBUTE, 'int' , None, None, 
                [(10, 4294967295)], [], 
                '''                Bandwidth change value to trigger an
                underflow (kbps)
                ''',
                'underflow_threshold_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'underflow',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth',
            False, 
            [
            _MetaInfoClassMember('adjustment-threshold', REFERENCE_CLASS, 'AdjustmentThreshold' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.AdjustmentThreshold', 
                [], [], 
                '''                Set the bandwidth change threshold to trigger
                adjustment
                ''',
                'adjustment_threshold',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('application-frequency', ATTRIBUTE, 'int' , None, None, 
                [(5, 10080)], [], 
                '''                Set the tunnel auto-bw application frequency
                in minutes
                ''',
                'application_frequency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth-limits', REFERENCE_CLASS, 'BandwidthLimits' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.BandwidthLimits', 
                [], [], 
                '''                Set min/max bandwidth auto-bw can apply on a
                tunnel
                ''',
                'bandwidth_limits',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('collection-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable bandwidth collection only, no auto-bw
                adjustment
                ''',
                'collection_only',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object is only valid for tunnel
                interfaces and it controls whether that
                interface has auto-bw enabled on it or not.The
                object must be set before any other auto-bw
                configuration is supplied for the interface,
                and must be the last auto-bw configuration
                object to be removed.
                ''',
                'enabled',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('overflow', REFERENCE_CLASS, 'Overflow' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Overflow', 
                [], [], 
                '''                Configuring the tunnel overflow detection
                ''',
                'overflow',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('underflow', REFERENCE_CLASS, 'Underflow' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Underflow', 
                [], [], 
                '''                Configuring the tunnel underflow detection
                ''',
                'underflow',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'auto-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce.Metric' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce.Metric',
            False, 
            [
            _MetaInfoClassMember('absolute-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The absolute metric value
                ''',
                'absolute_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('constant-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The constant metric value
                ''',
                'constant_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTeAutorouteMetric_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAutorouteMetric_Enum', 
                [], [], 
                '''                Autoroute tunnel metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('relative-metric', ATTRIBUTE, 'int' , None, None, 
                [(-10, 10)], [], 
                '''                The value of the adjustment
                ''',
                'relative_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable autoroute announce
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('include-ipv6', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that the tunnel should be an IPv6
                autoroute announce also
                ''',
                'include_ipv6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce.Metric', 
                [], [], 
                '''                Specify MPLS tunnel metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'autoroute-announce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr.Destination' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of destination
                ''',
                'destination_address',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_LIST, 'Destination' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr.Destination', 
                [], [], 
                '''                Destination address to add in RIB
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'destination-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.Metric' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.Metric',
            False, 
            [
            _MetaInfoClassMember('absolute-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The absolute metric value
                ''',
                'absolute_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('constant-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The constant metric value
                ''',
                'constant_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'MplsTeAutorouteMetric_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeAutorouteMetric_Enum', 
                [], [], 
                '''                Autoroute tunnel metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('relative-metric', ATTRIBUTE, 'int' , None, None, 
                [(-10, 10)], [], 
                '''                The value of the adjustment
                ''',
                'relative_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'metric',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute',
            False, 
            [
            _MetaInfoClassMember('autoroute-announce', REFERENCE_CLASS, 'AutorouteAnnounce' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce', 
                [], [], 
                '''                Announce tunnel to IGP
                ''',
                'autoroute_announce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Adds tunnel's destination in RIB
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination-xr', REFERENCE_CLASS, 'DestinationXr' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr', 
                [], [], 
                '''                Tunnel Autoroute Destination(s)
                ''',
                'destination_xr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('metric', REFERENCE_CLASS, 'Metric' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.Metric', 
                [], [], 
                '''                Specify MPLS tunnel metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'autoroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BackupBandwidth' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BackupBandwidth',
            False, 
            [
            _MetaInfoClassMember('backup-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Backup bandwidth requested by this tunnel in
                kbps. Ignored if bandwidth limit type is
                unlimited.
                ''',
                'backup_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-type', REFERENCE_ENUM_CLASS, 'MplsTeBackupBandwidthClass_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBackupBandwidthClass_Enum', 
                [], [], 
                '''                Backup bandwidth class type, relevant only if
                DSTEType is StandardDSTE
                ''',
                'class_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDste_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDste_Enum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('limit-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthLimit_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthLimit_Enum', 
                [], [], 
                '''                Backup bandwidth limit type
                ''',
                'limit_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pool-type', REFERENCE_ENUM_CLASS, 'MplsTeBackupBandwidthPool_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBackupBandwidthPool_Enum', 
                [], [], 
                '''                Backup bandwidth pool type, relevant only if
                DSTEType is PreStandardDSTE
                ''',
                'pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'backup-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bandwidth' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of the bandwidth reserved by this
                tunnel in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('class-or-pool-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Class type for the bandwith allocation
                ''',
                'class_or_pool_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dste-type', REFERENCE_ENUM_CLASS, 'MplsTeBandwidthDste_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeBandwidthDste_Enum', 
                [], [], 
                '''                DSTE-standard flag
                ''',
                'dste_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BfdOverLsp' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BfdOverLsp',
            False, 
            [
            _MetaInfoClassMember('bringup-timeout', ATTRIBUTE, 'int' , None, None, 
                [(60, 3600)], [], 
                '''                Wait for session to come up in seconds
                (default 60)
                ''',
                'bringup_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dampening-initial-wait', ATTRIBUTE, 'int' , None, None, 
                [(1, 518400000)], [], 
                '''                Initial delay in milliseconds (default 16000)
                ''',
                'dampening_initial_wait',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dampening-maximum-wait', ATTRIBUTE, 'int' , None, None, 
                [(1, 518400000)], [], 
                '''                Maximum delay in milliseconds (default 600000)
                ''',
                'dampening_maximum_wait',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('dampening-secondary-wait', ATTRIBUTE, 'int' , None, None, 
                [(1, 518400000)], [], 
                '''                Secondary delay in milliseconds (default
                20000)
                ''',
                'dampening_secondary_wait',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('encap-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Specify BFD Encap Mode on the tunnel
                ''',
                'encap_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-detect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BFD Fast Detect On the tunnel
                ''',
                'fast_detect',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Specify the minimum interval for BFD failure
                detection
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 10)], [], 
                '''                Specify the multiplier for BFD failure
                detection
                ''',
                'multiplier',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('periodic-ping-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Periodic LSP Ping for BFD over LSP
                ''',
                'periodic_ping_disable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('periodic-ping-interval', ATTRIBUTE, 'int' , None, None, 
                [(60, 3600)], [], 
                '''                Periodic LSP Ping Interval in seconds (default
                120)
                ''',
                'periodic_ping_interval',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bfd-over-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType.FaultOam' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType.FaultOam',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object is only valid for bidirectional
                tunnel interfaces and it controls whether
                that interface has fault OAM enabled on it
                or not.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fault-oam',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Controls whether association type is
                co-routed.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fault-oam', REFERENCE_CLASS, 'FaultOam' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType.FaultOam', 
                [], [], 
                '''                Tunnel Fault OAM
                ''',
                'fault_oam',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'association-corouted-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationParameters' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationParameters',
            False, 
            [
            _MetaInfoClassMember('association-global-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Association Global ID
                ''',
                'association_global_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('association-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Association ID
                ''',
                'association_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('association-is-global-id-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Association Global ID Configured
                ''',
                'association_is_global_id_configured',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('association-source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Association Source IP Address
                ''',
                'association_source_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'association-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional',
            False, 
            [
            _MetaInfoClassMember('association-corouted-type', REFERENCE_CLASS, 'AssociationCoroutedType' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType', 
                [], [], 
                '''                Association Corouted Type
                ''',
                'association_corouted_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('association-parameters', REFERENCE_CLASS, 'AssociationParameters' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationParameters', 
                [], [], 
                '''                Association ID, Source IP Address, and Global
                ID
                ''',
                'association_parameters',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This object is only valid for tunnel
                interfaces and it controls whether that
                interface has bidirectional enabled on it or
                not.
                ''',
                'enabled',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'bidirectional',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BindingSegmentIdMpls' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BindingSegmentIdMpls',
            False, 
            [
            _MetaInfoClassMember('label-value', ATTRIBUTE, 'int' , None, None, 
                [(16, 4015)], [], 
                '''                MPLS label
                ''',
                'label_value',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('segment-id-type', REFERENCE_ENUM_CLASS, 'BindingSegmentId_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'BindingSegmentId_Enum', 
                [], [], 
                '''                MPLS label value type
                ''',
                'segment_id_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'binding-segment-id-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.FastReroute' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.FastReroute',
            False, 
            [
            _MetaInfoClassMember('bandwidth-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Bandwidth Protection
                ''',
                'bandwidth_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('node-protection', ATTRIBUTE, 'int' , None, None, 
                [(0, 1)], [], 
                '''                Node Protection
                ''',
                'node_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.ForwardingAdjacency' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.ForwardingAdjacency',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable forwarding adjacency
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 20000)], [], 
                '''                Specify the holdtime for the tunnel as
                forwarding adjacency
                ''',
                'hold_time',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('include-ipv6', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that the tunnel should be an IPv6
                forwarding adjacency also
                ''',
                'include_ipv6',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'forwarding-adjacency',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities.NewStyleAffinity' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities.NewStyleAffinity',
            False, 
            [
            _MetaInfoClassMember('affinity1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the first affinity
                ''',
                'affinity1',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity10', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the tenth affinity
                ''',
                'affinity10',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity2', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the second affinity
                ''',
                'affinity2',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity3', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the third affinity
                ''',
                'affinity3',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity4', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fourth affinity
                ''',
                'affinity4',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity5', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the fifth affinity
                ''',
                'affinity5',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity6', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the sixth affinity
                ''',
                'affinity6',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity7', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the seventh affinity
                ''',
                'affinity7',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity8', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the eighth affinity
                ''',
                'affinity8',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity9', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the nineth affinity
                ''',
                'affinity9',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('affinity-type', REFERENCE_ENUM_CLASS, 'MplsTeTunnelAffinity_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeTunnelAffinity_Enum', 
                [], [], 
                '''                The type of the affinity entry
                ''',
                'affinity_type',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities',
            False, 
            [
            _MetaInfoClassMember('new-style-affinity', REFERENCE_LIST, 'NewStyleAffinity' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities.NewStyleAffinity', 
                [], [], 
                '''                Tunnel new style affinity attribute
                ''',
                'new_style_affinity',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'new-style-affinities',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathInvalidation' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathInvalidation',
            False, 
            [
            _MetaInfoClassMember('path-invalidation-action', REFERENCE_ENUM_CLASS, 'PathInvalidationAction_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'PathInvalidationAction_Enum', 
                [], [], 
                '''                Path Invalidation Action
                ''',
                'path_invalidation_action',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 60000)], [], 
                '''                Path Invalidation Timeout
                ''',
                'path_invalidation_timeout',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-invalidation',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions.PathOption' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions.PathOption',
            False, 
            [
            _MetaInfoClassMember('preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level for this path option
                ''',
                'preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Deprecated
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('igp-area', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                IGP area ID in integer format
                ''',
                'igp_area',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('igp-area-ip-address-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IGP area ID in IP address format
                ''',
                'igp_area_ip_address_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('igp-instance', ATTRIBUTE, 'str' , None, None, 
                [(0, 40)], [], 
                '''                IGP instance name
                ''',
                'igp_instance',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('igp-type', REFERENCE_ENUM_CLASS, 'MplsTeIgpProtocol_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeIgpProtocol_Enum', 
                [], [], 
                '''                IGP type
                ''',
                'igp_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Deprecated
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('lockdown', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                Lockdown properties
                ''',
                'lockdown',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Deprecated
                ''',
                'output_label',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The ID of the IP explicit path associated
                with this option
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the IP explicit path associated
                with this option
                ''',
                'path_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-option-attribute-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path option attribute set name
                ''',
                'path_option_attribute_set_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-property', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Deprecated
                ''',
                'path_property',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsTePathOption_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOption_Enum', 
                [], [], 
                '''                The type of the path option
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                PCE properties
                ''',
                'pce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PCE address
                ''',
                'pce_address',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected-by-preference-level', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Preference level of the protecting explicit
                path. Leave unset in order to not use an
                explicit protecting path
                ''',
                'protected_by_preference_level',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                SegmentRouting properties
                ''',
                'segment_routing',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('verbatim', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProperty_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProperty_Enum', 
                [], [], 
                '''                Verbatim properties
                ''',
                'verbatim',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions',
            False, 
            [
            _MetaInfoClassMember('path-option', REFERENCE_LIST, 'PathOption' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions.PathOption', 
                [], [], 
                '''                A tunnel path option
                ''',
                'path_option',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-options',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect',
            False, 
            [
            _MetaInfoClassMember('protection', REFERENCE_ENUM_CLASS, 'MplsTePathOptionProtection_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathOptionProtection_Enum', 
                [], [], 
                '''                Protection type for this path
                ''',
                'protection',
                'Cisco-IOS-XR-mpls-te-cfg', True),
            _MetaInfoClassMember('path-options', REFERENCE_CLASS, 'PathOptions' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions', 
                [], [], 
                '''                Tunnel path options
                ''',
                'path_options',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-protect',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects',
            False, 
            [
            _MetaInfoClassMember('path-option-protect', REFERENCE_LIST, 'PathOptionProtect' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect', 
                [], [], 
                '''                Tunnel path protection
                ''',
                'path_option_protect',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'path-option-protects',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Pce' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Pce',
            False, 
            [
            _MetaInfoClassMember('delegation', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PCE Delegation
                ''',
                'delegation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Always set to true
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'pce',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PolicyClasses' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PolicyClasses',
            False, 
            [
            _MetaInfoClassMember('policy-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(1, 8)], [], 
                '''                Array of Policy class
                ''',
                'policy_class',
                'Cisco-IOS-XR-mpls-te-cfg', False, max_elements=7),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'policy-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Priority' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Endpoint' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Endpoint',
            False, 
            [
            _MetaInfoClassMember('capability', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingCap_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingCap_Enum', 
                [], [], 
                '''                Switching capability
                ''',
                'capability',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingEncode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingEncode_Enum', 
                [], [], 
                '''                LSP encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'endpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Transit' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Transit',
            False, 
            [
            _MetaInfoClassMember('capability', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingCap_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingCap_Enum', 
                [], [], 
                '''                Switching capability
                ''',
                'capability',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('encoding', REFERENCE_ENUM_CLASS, 'MplsTeSwitchingEncode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTeSwitchingEncode_Enum', 
                [], [], 
                '''                LSP encoding
                ''',
                'encoding',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'transit',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching',
            False, 
            [
            _MetaInfoClassMember('endpoint', REFERENCE_CLASS, 'Endpoint' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Endpoint', 
                [], [], 
                '''                Specify end point switching descriptor
                parameters
                ''',
                'endpoint',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('transit', REFERENCE_CLASS, 'Transit' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Transit', 
                [], [], 
                '''                Specify transit switching descriptor
                parameters
                ''',
                'transit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'switching',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes',
            False, 
            [
            _MetaInfoClassMember('admin-mode', REFERENCE_CLASS, 'AdminMode' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AdminMode', 
                [], [], 
                '''                Performs admin operations on the optical tunnel
                interface
                ''',
                'admin_mode',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('affinity-mask', REFERENCE_CLASS, 'AffinityMask' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AffinityMask', 
                [], [], 
                '''                Set the affinity flags and mask
                ''',
                'affinity_mask',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('auto-bandwidth', REFERENCE_CLASS, 'AutoBandwidth' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth', 
                [], [], 
                '''                Tunnel Interface Auto-bandwidth configuration
                data
                ''',
                'auto_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('autoroute', REFERENCE_CLASS, 'Autoroute' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute', 
                [], [], 
                '''                Parameters for IGP routing over tunnel
                ''',
                'autoroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('backup-bandwidth', REFERENCE_CLASS, 'BackupBandwidth' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BackupBandwidth', 
                [], [], 
                '''                Tunnel backup bandwidth requirement
                ''',
                'backup_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bandwidth', 
                [], [], 
                '''                Tunnel bandwidth requirement
                ''',
                'bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bfd-over-lsp', REFERENCE_CLASS, 'BfdOverLsp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BfdOverLsp', 
                [], [], 
                '''                BFD over TE LSP
                ''',
                'bfd_over_lsp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('bidirectional', REFERENCE_CLASS, 'Bidirectional' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional', 
                [], [], 
                '''                Tunnel Interface Bidirectional configuration
                data
                ''',
                'bidirectional',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('binding-segment-id-mpls', REFERENCE_CLASS, 'BindingSegmentIdMpls' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BindingSegmentIdMpls', 
                [], [], 
                '''                Allocate MPLS binding segment ID
                ''',
                'binding_segment_id_mpls',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Set the destination of the tunnel
                ''',
                'destination',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.FastReroute', 
                [], [], 
                '''                Specify MPLS tunnel can be fast-rerouted
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [(1, 7)], [], 
                '''                Forward class value
                ''',
                'forward_class',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('forwarding-adjacency', REFERENCE_CLASS, 'ForwardingAdjacency' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.ForwardingAdjacency', 
                [], [], 
                '''                Forwarding adjacency announcement to IGP
                ''',
                'forwarding_adjacency',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('load-share', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Tunnel loadsharing metric
                ''',
                'load_share',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('new-style-affinities', REFERENCE_CLASS, 'NewStyleAffinities' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities', 
                [], [], 
                '''                Tunnel new style affinity attributes table
                ''',
                'new_style_affinities',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-invalidation', REFERENCE_CLASS, 'PathInvalidation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathInvalidation', 
                [], [], 
                '''                Path invalidation configuration for this
                specific tunnel
                ''',
                'path_invalidation',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-option-protects', REFERENCE_CLASS, 'PathOptionProtects' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects', 
                [], [], 
                '''                Tunnel path protection state
                ''',
                'path_option_protects',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-protection', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify MPLS tunnel to be path protected
                ''',
                'path_protection',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-cost-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Path selection cost limit configuration for this
                specific tunnel
                ''',
                'path_selection_cost_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-hop-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Path selection hop limit configuration for this
                specific tunnel
                ''',
                'path_selection_hop_limit',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('path-selection-metric', REFERENCE_ENUM_CLASS, 'MplsTePathSelectionMetric_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg', 'MplsTePathSelectionMetric_Enum', 
                [], [], 
                '''                Path selection metric configuration for this
                specific tunnel
                ''',
                'path_selection_metric',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('pce', REFERENCE_CLASS, 'Pce' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Pce', 
                [], [], 
                '''                PCE config
                ''',
                'pce',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('policy-classes', REFERENCE_CLASS, 'PolicyClasses' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PolicyClasses', 
                [], [], 
                '''                Policy classes for PBTS
                ''',
                'policy_classes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('record-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Record the route used by the tunnel
                ''',
                'record_route',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('signalled-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 254)], [], 
                '''                The name of the tunnel to be included in
                signalling messages
                ''',
                'signalled_name',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the soft-preemption feature on the tunnel
                ''',
                'soft_preemption',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('switching', REFERENCE_CLASS, 'Switching' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching', 
                [], [], 
                '''                Specify tunnel LSPs switching capability
                descriptor
                ''',
                'switching',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'tunnel-te-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration.VlanIdentifier' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration.VlanIdentifier',
            False, 
            [
            _MetaInfoClassMember('first-tag', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                First (outermost) VLAN tag value
                ''',
                'first_tag',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('second-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Second VLAN tag value. The any value may only
                be used for Layer 2 subinterfaces
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False, [
                    _MetaInfoClassMember('second-tag', REFERENCE_ENUM_CLASS, 'VlanTagOrNull_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrNull_Enum', 
                        [], [], 
                        '''                        Second VLAN tag value. The any value may only
                        be used for Layer 2 subinterfaces
                        ''',
                        'second_tag',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                    _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                        [(0, 4094)], [], 
                        '''                        Second VLAN tag value. The any value may only
                        be used for Layer 2 subinterfaces
                        ''',
                        'second_tag',
                        'Cisco-IOS-XR-l2-eth-infra-cfg', False),
                ]),
            _MetaInfoClassMember('vlan-type', REFERENCE_ENUM_CLASS, 'Vlan_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Vlan_Enum', 
                [], [], 
                '''                Whether this sub-interface is dot1ad or dot1Q
                ''',
                'vlan_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'vlan-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration',
            False, 
            [
            _MetaInfoClassMember('vlan-identifier', REFERENCE_CLASS, 'VlanIdentifier' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration.VlanIdentifier', 
                [], [], 
                '''                The VLAN tag stack associated with this
                sub-interface.
                ''',
                'vlan_identifier',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'vlan-sub-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.NativeVlanIdentifier' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.NativeVlanIdentifier',
            False, 
            [
            _MetaInfoClassMember('vlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                VLAN identifier
                ''',
                'vlan_identifier',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('vlan-type', REFERENCE_ENUM_CLASS, 'Vlan_Enum' , 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes', 'Vlan_Enum', 
                [], [], 
                '''                Whether this interface is dot1ad or dot1Q
                ''',
                'vlan_type',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'native-vlan-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.TunnelingEthertype_Enum' : _MetaInfoEnum('TunnelingEthertype_Enum', 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg',
        {
            '0x9100':'Y_0X9100',
            '0x9200':'Y_0X9200',
        }, 'Cisco-IOS-XR-l2-eth-infra-cfg', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg']),
    'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration',
            False, 
            [
            _MetaInfoClassMember('native-vlan-identifier', REFERENCE_CLASS, 'NativeVlanIdentifier' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.NativeVlanIdentifier', 
                [], [], 
                '''                The Native VLAN identifier associated with this
                trunk interface
                ''',
                'native_vlan_identifier',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('tunneling-ethertype', REFERENCE_ENUM_CLASS, 'TunnelingEthertype_Enum' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.TunnelingEthertype_Enum', 
                [], [], 
                '''                The outer ethertype used in Q-in-Q frames. The
                default value is 0x8100
                ''',
                'tunneling_ethertype',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-cfg',
            'vlan-trunk-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration.Wanphy' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration.Wanphy',
            False, 
            [
            _MetaInfoClassMember('lan-mode', REFERENCE_ENUM_CLASS, 'WanphyLanMode_Enum' , 'ydk.models.wanphy.Cisco_IOS_XR_wanphy_ui_cfg', 'WanphyLanMode_Enum', 
                [], [], 
                '''                Configure LAN Mode
                ''',
                'lan_mode',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-line-ais', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Line Alarm Indication Signal
                reporting
                ''',
                'report_line_ais',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-lof', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Loss Of Frame reporting
                ''',
                'report_lof',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-lop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Loss Of Pointer reporting
                ''',
                'report_lop',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-los', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Loss Of Signal reporting
                ''',
                'report_los',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-ais', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Alarm Indication Signal
                reporting
                ''',
                'report_path_ais',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-fe-ais', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Far End Payload Label Mismatch
                reporting
                ''',
                'report_path_fe_ais',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-fe-plm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Far End Payload Label Mismatch
                reporting
                ''',
                'report_path_fe_plm',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-lcd', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Loss Of Code-Group Delineation
                reporting
                ''',
                'report_path_lcd',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-plm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Payload Label Mismatch reporting
                ''',
                'report_path_plm',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-path-rdi', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Path Remote Defect Indicator
                reporting
                ''',
                'report_path_rdi',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-rdi', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure Remote Defect Indicator reporting
                ''',
                'report_rdi',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-sd-ber', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure B2 BER in excess of SD threshold
                reporting
                ''',
                'report_sd_ber',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('report-sf-ber', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure B2 BER in excess of SF threshold
                reporting
                ''',
                'report_sf_ber',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('threshold-sd-ber', ATTRIBUTE, 'int' , None, None, 
                [(3, 9)], [], 
                '''                Bit error rate is 10 to the minus n, where n is
                threshold value
                ''',
                'threshold_sd_ber',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('threshold-sf-ber', ATTRIBUTE, 'int' , None, None, 
                [(3, 9)], [], 
                '''                Bit error rate is 10 to the minus n, where n is
                threshold value
                ''',
                'threshold_sf_ber',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            _MetaInfoClassMember('wan-mode', REFERENCE_ENUM_CLASS, 'WanphyWanMode_Enum' , 'ydk.models.wanphy.Cisco_IOS_XR_wanphy_ui_cfg', 'WanphyWanMode_Enum', 
                [], [], 
                '''                Configure WAN Mode
                ''',
                'wan_mode',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            ],
            'Cisco-IOS-XR-wanphy-ui-cfg',
            'wanphy',
            _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations.InterfaceConfiguration' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations.InterfaceConfiguration',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str' , None, None, 
                [], ['(act)|(pre)'], 
                '''                Whether the interface is active or
                preconfigured
                ''',
                'active',
                'Cisco-IOS-XR-ifmgr-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Afs', 
                [], [], 
                '''                Per-address-family and topology configuration
                ''',
                'afs',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('atm', REFERENCE_CLASS, 'Atm' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Atm', 
                [], [], 
                '''                ATM Configuration
                ''',
                'atm',
                'Cisco-IOS-XR-atm-vcm-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The bandwidth of the interface in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bfd', 
                [], [], 
                '''                BFD over bundle members configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('bundle', REFERENCE_CLASS, 'Bundle' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Bundle', 
                [], [], 
                '''                Generic per-bundle configuration
                ''',
                'bundle',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('bundle-member', REFERENCE_CLASS, 'BundleMember' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.BundleMember', 
                [], [], 
                '''                Generic per-member configuration
                ''',
                'bundle_member',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('cdp', REFERENCE_CLASS, 'Cdp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Cdp', 
                [], [], 
                '''                Interface specific CDP configuration
                ''',
                'cdp',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('Cisco-IOS-XR-ncs5500-qos-cfg_qos', REFERENCE_CLASS, 'CiscoIOSXRNcs5500QosCfg_qos' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos', 
                [], [], 
                '''                Interface QOS configuration
                ''',
                'cisco_ios_xr_ncs5500_qos_cfg_qos',
                'Cisco-IOS-XR-ncs5500-qos-cfg', False),
            _MetaInfoClassMember('Cisco-IOS-XR-skp-qos-cfg_qos', REFERENCE_CLASS, 'CiscoIOSXRSkpQosCfg_qos' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos', 
                [], [], 
                '''                Interface QOS configuration
                ''',
                'cisco_ios_xr_skp_qos_cfg_qos',
                'Cisco-IOS-XR-skp-qos-cfg', False),
            _MetaInfoClassMember('dagrs', REFERENCE_CLASS, 'Dagrs' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dagrs', 
                [], [], 
                '''                Direct-Attached Gateway Redundancy configuration
                ''',
                'dagrs',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('dampening', REFERENCE_CLASS, 'Dampening' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Dampening', 
                [], [], 
                '''                Whether this interface's state changes are
                dampened or not
                ''',
                'dampening',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The description of this interface
                ''',
                'description',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_CLASS, 'Encapsulation' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Encapsulation', 
                [], [], 
                '''                The encapsulation on the interface
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('es-packet-filter', REFERENCE_CLASS, 'EsPacketFilter' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EsPacketFilter', 
                [], [], 
                '''                ES Packet Filtering configuration for the
                interface
                ''',
                'es_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ethernet', 
                [], [], 
                '''                Ether specific interface configuration
                ''',
                'ethernet',
                'Cisco-IOS-XR-drivers-media-eth-cfg', False),
            _MetaInfoClassMember('ethernet-bng', REFERENCE_CLASS, 'EthernetBng' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetBng', 
                [], [], 
                '''                Ethernet Infra BNG specific configuration
                ''',
                'ethernet_bng',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ethernet-features', REFERENCE_CLASS, 'EthernetFeatures' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures', 
                [], [], 
                '''                Ethernet Features Configuration
                ''',
                'ethernet_features',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('ethernet-service', REFERENCE_CLASS, 'EthernetService' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.EthernetService', 
                [], [], 
                '''                Ethernet service configuration
                ''',
                'ethernet_service',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('interface-mode-non-physical', REFERENCE_ENUM_CLASS, 'InterfaceModeEnum_Enum' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceModeEnum_Enum', 
                [], [], 
                '''                The mode in which an interface is running. The
                existence of this object causes the creation of
                the software subinterface.
                ''',
                'interface_mode_non_physical',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('interface-virtual', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The mode in which an interface is running. The
                existence of this object causes the creation of
                the software virtual/subinterface.
                ''',
                'interface_virtual',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('ipv4-network', REFERENCE_CLASS, 'Ipv4Network' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4Network', 
                [], [], 
                '''                Interface IPv4 Network configuration data
                ''',
                'ipv4_network',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('ipv4-network-forwarding', REFERENCE_CLASS, 'Ipv4NetworkForwarding' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4NetworkForwarding', 
                [], [], 
                '''                Interface IPv4 Network configuration data also
                used for forwarding
                ''',
                'ipv4_network_forwarding',
                'Cisco-IOS-XR-ipv4-io-cfg', False),
            _MetaInfoClassMember('ipv4-packet-filter', REFERENCE_CLASS, 'Ipv4PacketFilter' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter', 
                [], [], 
                '''                IPv4 Packet Filtering configuration for the
                interface
                ''',
                'ipv4_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('ipv4arp', REFERENCE_CLASS, 'Ipv4arp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv4arp', 
                [], [], 
                '''                Configure Address Resolution Protocol
                ''',
                'ipv4arp',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('ipv6-neighbor', REFERENCE_CLASS, 'Ipv6Neighbor' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor', 
                [], [], 
                '''                IPv6 interface neighbor or neighbor discovery
                configuration
                ''',
                'ipv6_neighbor',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('ipv6-network', REFERENCE_CLASS, 'Ipv6Network' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6Network', 
                [], [], 
                '''                Interface IPv6 Network configuration data
                ''',
                'ipv6_network',
                'Cisco-IOS-XR-ipv6-ma-cfg', False),
            _MetaInfoClassMember('ipv6-packet-filter', REFERENCE_CLASS, 'Ipv6PacketFilter' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter', 
                [], [], 
                '''                IPv6 Packet Filtering configuration for the
                interface
                ''',
                'ipv6_packet_filter',
                'Cisco-IOS-XR-ip-pfilter-cfg', False),
            _MetaInfoClassMember('l2-transport', REFERENCE_CLASS, 'L2Transport' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.L2Transport', 
                [], [], 
                '''                Interface Layer 2 Transport service
                configuration data
                ''',
                'l2_transport',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('lacp', REFERENCE_CLASS, 'Lacp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lacp', 
                [], [], 
                '''                Link Aggregation Control Protocol per-interface
                configuration (for bundle or member)
                ''',
                'lacp',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('link-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable interface and line-protocol state change
                alarms
                ''',
                'link_status',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('lldp', REFERENCE_CLASS, 'Lldp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Lldp', 
                [], [], 
                '''                Disable LLDP TX or RX
                ''',
                'lldp',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('mac-accounting', REFERENCE_CLASS, 'MacAccounting' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MacAccounting', 
                [], [], 
                '''                MAC Accounting Configuration
                ''',
                'mac_accounting',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('mlacp', REFERENCE_CLASS, 'Mlacp' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Mlacp', 
                [], [], 
                '''                Multi-chassis LACP configuration
                ''',
                'mlacp',
                'Cisco-IOS-XR-bundlemgr-cfg', False),
            _MetaInfoClassMember('mte-tunnel-attributes', REFERENCE_CLASS, 'MteTunnelAttributes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes', 
                [], [], 
                '''                MPLS P2MP tunnel attributes
                ''',
                'mte_tunnel_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mtus', REFERENCE_CLASS, 'Mtus' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Mtus', 
                [], [], 
                '''                The MTU configuration for the interface
                ''',
                'mtus',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('net-flow', REFERENCE_CLASS, 'NetFlow' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NetFlow', 
                [], [], 
                '''                Interface netflow configuration
                ''',
                'net_flow',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('nv-satellite-access', REFERENCE_CLASS, 'NvSatelliteAccess' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteAccess', 
                [], [], 
                '''                nV Satellite Access Link Configuration
                ''',
                'nv_satellite_access',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('nv-satellite-fabric-link', REFERENCE_CLASS, 'NvSatelliteFabricLink' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink', 
                [], [], 
                '''                nV Satellite Fabric Link Configuration
                ''',
                'nv_satellite_fabric_link',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('nv-satellite-fabric-network', REFERENCE_CLASS, 'NvSatelliteFabricNetwork' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork', 
                [], [], 
                '''                Complex Network connection to one or more
                Satellites
                ''',
                'nv_satellite_fabric_network',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('optics', REFERENCE_CLASS, 'Optics' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Optics', 
                [], [], 
                '''                Optics controller configuration
                ''',
                'optics',
                'Cisco-IOS-XR-controller-optics-cfg', False),
            _MetaInfoClassMember('otu', REFERENCE_CLASS, 'Otu' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Otu', 
                [], [], 
                '''                OTU port controller configuration
                ''',
                'otu',
                'Cisco-IOS-XR-controller-otu-cfg', False),
            _MetaInfoClassMember('pbr', REFERENCE_CLASS, 'Pbr' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Pbr', 
                [], [], 
                '''                Dynamic Template PBR configuration
                ''',
                'pbr',
                'Cisco-IOS-XR-pbr-cfg', False),
            _MetaInfoClassMember('performance-management', REFERENCE_CLASS, 'PerformanceManagement' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement', 
                [], [], 
                '''                Configure pm parameters
                ''',
                'performance_management',
                'Cisco-IOS-XR-pmengine-cfg', False),
            _MetaInfoClassMember('pseudowire-ether', REFERENCE_CLASS, 'PseudowireEther' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PseudowireEther', 
                [], [], 
                '''                PW-Ether attributes
                ''',
                'pseudowire_ether',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('pseudowire-iw', REFERENCE_CLASS, 'PseudowireIw' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.PseudowireIw', 
                [], [], 
                '''                PW-IW attributes
                ''',
                'pseudowire_iw',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('secondary-admin-state', REFERENCE_ENUM_CLASS, 'SecondaryAdminStateEnum_Enum' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'SecondaryAdminStateEnum_Enum', 
                [], [], 
                '''                The secondary admin state of the interface
                ''',
                'secondary_admin_state',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The existence of this configuration indicates
                the interface is shut down
                ''',
                'shutdown',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            _MetaInfoClassMember('span-monitor-sessions', REFERENCE_CLASS, 'SpanMonitorSessions' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions', 
                [], [], 
                '''                Monitor Session container for this source
                interface
                ''',
                'span_monitor_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Statistics', 
                [], [], 
                '''                Per-interface statistics configuration
                ''',
                'statistics',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            _MetaInfoClassMember('transport-profile-tunnel', REFERENCE_CLASS, 'TransportProfileTunnel' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel', 
                [], [], 
                '''                MPLS-TP tunnel attributes
                ''',
                'transport_profile_tunnel',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('tunnel-te-attributes', REFERENCE_CLASS, 'TunnelTeAttributes' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes', 
                [], [], 
                '''                MPLS tunnel attributes
                ''',
                'tunnel_te_attributes',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('vlan-sub-configuration', REFERENCE_CLASS, 'VlanSubConfiguration' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration', 
                [], [], 
                '''                IEEE 802.1Q VLAN subinterface configuration
                ''',
                'vlan_sub_configuration',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('vlan-trunk-configuration', REFERENCE_CLASS, 'VlanTrunkConfiguration' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration', 
                [], [], 
                '''                IEEE 802.1Q VLAN trunk interface configuration
                ''',
                'vlan_trunk_configuration',
                'Cisco-IOS-XR-l2-eth-infra-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Assign the interface to a VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('wanphy', REFERENCE_CLASS, 'Wanphy' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration.Wanphy', 
                [], [], 
                '''                WANPHY port controller configuration
                ''',
                'wanphy',
                'Cisco-IOS-XR-wanphy-ui-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'interface-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
    'InterfaceConfigurations' : {
        'meta_info' : _MetaInfoClass('InterfaceConfigurations',
            False, 
            [
            _MetaInfoClassMember('interface-configuration', REFERENCE_LIST, 'InterfaceConfiguration' , 'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg', 'InterfaceConfigurations.InterfaceConfiguration', 
                [], [], 
                '''                The configuration for an interface
                ''',
                'interface_configuration',
                'Cisco-IOS-XR-ifmgr-cfg', False),
            ],
            'Cisco-IOS-XR-ifmgr-cfg',
            'interface-configurations',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-cfg'],
        'ydk.models.ifmgr.Cisco_IOS_XR_ifmgr_cfg'
        ),
    },
}
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Afs.Af']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Afs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Afs.AfTopologyName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Afs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.CellPacking']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.OamEmulation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc.Shape']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs.Pvc']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.CellPacking']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp.Shape']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps.Pvp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel.Shape']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels.VpTunnel']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.MaximumCellPackingTimers']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvcs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.Pvps']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm.VpTunnels']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Echo']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4.Timers']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily.Ipv4']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd.AddressFamily']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing.HashFunction']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive.Links']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.BundleLoadBalancing']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.MaximumActive']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle.MinimumActive']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.BundleMember.Id']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.BundleMember']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input.ServicePolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output.ServicePolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Input']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos.Output']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input.ServicePolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead.Account']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output.ServicePolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Input']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.L2Overhead']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos.Output']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Distance']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Metric']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub.Timers']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr.Sub']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs.Dagr']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet.CarrierDelay']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalDegradeBitErrorRate']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet.SignalFailBitErrorRate']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetBng.AmbiguousEncapsulation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetBng']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp.Transmission']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMacAddress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds.SlaProfileTargetMepId']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.LossMeasurementCounters']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.MepProperties']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep.SlaProfileTargetMepIds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain.Mep']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains.Domain']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.AisUp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm.Domains']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame.Threshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod.Threshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds.Threshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod.Threshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.Frame']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FramePeriod']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.FrameSeconds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor.SymbolPeriod']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.Action']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.LinkMonitor']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam.RequireRemote']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.Cfm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures.EtherLinkOam']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService.Encapsulation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService.LocalTrafficDefaultEncapsulation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService.Rewrite']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries.Secondary']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Primary']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses.Secondaries']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag.FlowTagInput']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb.Input']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.FlowTag']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp.Qppb']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Input']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa.Output']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Addresses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Bgp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.BgpPa']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.HelperAddresses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network.Verify']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Inbound']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter.Outbound']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes.Ipv6Prefix']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.DuplicateAddressDetection']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.Ipv6Prefixes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor.RaInterval']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses.Eui64Address']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses.RegularAddress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.AutoConfiguration']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.Eui64Addresses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.LinkLocalAddress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses.RegularAddresses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable.BgpFlowTagPolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings.BgpPolicyAccounting']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters.MacAddressFilter']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Addresses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpFlowTagPolicyTable']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpPolicyAccountings']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.BgpQosPolicyPropagation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.MacAddressFilters']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network.Verify']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Inbound']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter.Outbound']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters.CellPacking']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols.L2Protocol']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.AtmPortModeParameters']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2EthernetFeatures']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.L2Protocols']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport.SpanMonitorSessions']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lacp.CiscoExtensions']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lacp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lacp.Timeout']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lacp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lldp.Receive']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lldp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lldp.Transmit']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lldp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mlacp.Maximize']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mlacp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions.PathOption']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.PathOptions']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf.S2lLogging']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs.DestinationLeaf']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.AffinityMask']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Bandwidth']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.DestinationLeafs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Logging']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.NewStyleAffinities']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes.Priority']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mtus.Mtu']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mtus']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Egress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap.Ingress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4.FlowMonitorMap']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Egress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap.Ingress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6.FlowMonitorMap']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress.FlowMonitorName']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Egress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap.Ingress']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls.FlowMonitorMap']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv4']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Ipv6']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow.Mpls']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures.Cfm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts.RemotePort']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.EthernetFeatures']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.Redundancy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink.RemotePorts']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts.RemotePort']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite.RemotePorts']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites.Satellite']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Redundancy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork.Satellites']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs.OpticsNetworkSrlg']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds.RxThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds.TxThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsDwdmCarrier']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.OpticsNetworkSrlgs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.RxThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics.TxThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs.NetworkSrlg']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.RevertWindow']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection.TriggerWindow']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.NetworkSrlgs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTti']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtisapi']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmdapi']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnExpectedTtitcmos']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTti']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtisapi']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmdapi']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.OtnSendTtitcmos']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu.ProactiveProtection']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Pbr.ServicePolicy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.Pbr']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports.Hour24EtherReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds.Hour24EtherThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether.Hour24EtherThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24.Hour24Ether']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports.Minute15EtherReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds.Minute15EtherThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether.Minute15EtherThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15.Minute15Ether']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports.HoVcHour24hoVcReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds.HoVcHour24hoVcThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc.HoVcHour24hoVcThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24.HoVcHour24hoVc']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports.HoVcMinute15hoVcReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds.HoVcMinute15hoVcThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc.HoVcMinute15hoVcThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15.HoVcMinute15hoVc']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports.Hour24OpticsReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds.Hour24OpticsThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics.Hour24OpticsThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports.Hour24fecReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds.Hour24fecThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec.Hour24fecThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports.Hour24otnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds.Hour24otnThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn.Hour24otnThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24Optics']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24fec']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24.Hour24otn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports.Hour24GfpReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds.Hour24GfpThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp.Hour24GfpThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp.Hour24Gfp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports.Hour24otnPathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds.Hour24otnPathThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath.Hour24otnPathThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path.Hour24otnPath']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports.Hour24otnTcmReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds.Hour24otnTcmThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm.Hour24otnTcmThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms.Hour24otnTcm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports.Minute15OpticsReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds.Minute15OpticsThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics.Minute15OpticsThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports.Minute15fecReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds.Minute15fecThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec.Minute15fecThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes.Min15OtnThresh']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports.Minute15otnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Min15OtnThreshes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn.Minute15otnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15Optics']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15fec']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15.Minute15otn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports.Minute15GfpReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds.Minute15GfpThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp.Minute15GfpThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp.Minute15Gfp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes.Min15OtnPathThresh']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports.Minute15otnPathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Min15OtnPathThreshes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath.Minute15otnPathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path.Minute15otnPath']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes.Min15OtnTcmThresh']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports.Minute15otnTcmReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Min15OtnTcmThreshes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm.Minute15otnTcmReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms.Minute15otnTcm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports.OcHour24OcnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds.OcHour24OcnThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn.OcHour24OcnThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24.OcHour24Ocn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports.OcMinute15OcnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds.OcMinute15OcnThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn.OcMinute15OcnThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15.OcMinute15Ocn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports.SonetHour24OcnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds.SonetHour24OcnThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn.SonetHour24OcnThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports.SonetHour24PathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds.SonetHour24PathThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path.SonetHour24PathThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Ocn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24.SonetHour24Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports.SonetMinute15OcnReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds.SonetMinute15OcnThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn.SonetMinute15OcnThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports.SonetMinute15PathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds.SonetMinute15PathThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path.SonetMinute15PathThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Ocn']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15.SonetMinute15Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports.StmHour24StmReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds.StmHour24StmThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm.StmHour24StmThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24.StmHour24Stm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports.StmMinute15StmReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds.StmMinute15StmThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm.StmMinute15StmThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15.StmMinute15Stm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports.StsHour24PathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds.StsHour24PathThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path.StsHour24PathThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24.StsHour24Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports.StsMinute15PathReport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds.StsMinute15PathThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathReports']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path.StsMinute15PathThresholds']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15.StsMinute15Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.EthernetMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.HoVcMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Gfp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Hour24otnTcms']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Gfp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15Path']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.Minute15otnTcms']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.OcMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.SonetMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StmMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsHour24']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement.StsMinute15']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession.Attachment']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions.SpanMonitorSession']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinInterval']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd.MinIntervalStandby']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault.ProtectionTrigger']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp.OutLabel']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp.OutLabel']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Bfd']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Destination']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.Fault']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.ProtectLsp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel.WorkingLsp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.AdjustmentThreshold']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.BandwidthLimits']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Overflow']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth.Underflow']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce.Metric']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr.Destination']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.AutorouteAnnounce']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.DestinationXr']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute.Metric']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType.FaultOam']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationCoroutedType']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional.AssociationParameters']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities.NewStyleAffinity']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions.PathOption']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect.PathOptions']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects.PathOptionProtect']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Endpoint']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching.Transit']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AdminMode']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AffinityMask']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.AutoBandwidth']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Autoroute']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BackupBandwidth']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bandwidth']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BfdOverLsp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Bidirectional']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.BindingSegmentIdMpls']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.FastReroute']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.ForwardingAdjacency']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.NewStyleAffinities']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathInvalidation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PathOptionProtects']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Pce']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.PolicyClasses']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Priority']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes.Switching']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration.VlanIdentifier']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration.NativeVlanIdentifier']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Afs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Atm']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bfd']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Bundle']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.BundleMember']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Cdp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRNcs5500QosCfg_qos']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.CiscoIOSXRSkpQosCfg_qos']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dagrs']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Dampening']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Encapsulation']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EsPacketFilter']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ethernet']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetBng']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetFeatures']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.EthernetService']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4Network']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4NetworkForwarding']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4PacketFilter']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv4arp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Neighbor']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6Network']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Ipv6PacketFilter']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.L2Transport']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lacp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Lldp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MacAccounting']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mlacp']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.MteTunnelAttributes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Mtus']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NetFlow']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteAccess']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricLink']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.NvSatelliteFabricNetwork']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Optics']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Otu']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Pbr']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PerformanceManagement']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PseudowireEther']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.PseudowireIw']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.SpanMonitorSessions']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Statistics']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TransportProfileTunnel']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.TunnelTeAttributes']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanSubConfiguration']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.VlanTrunkConfiguration']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration.Wanphy']['meta_info'].parent =_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info']
_meta_table['InterfaceConfigurations.InterfaceConfiguration']['meta_info'].parent =_meta_table['InterfaceConfigurations']['meta_info']

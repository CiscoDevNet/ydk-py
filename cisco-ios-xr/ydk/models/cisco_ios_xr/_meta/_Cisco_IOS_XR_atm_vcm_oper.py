


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VcManageLevelEnum' : _MetaInfoEnum('VcManageLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'manage':'manage',
            'not-managed':'not_managed',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'ClassLinkOamInheritLevelEnum' : _MetaInfoEnum('ClassLinkOamInheritLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'vc-configured-onvc':'vc_configured_onvc',
            'vc-class-onvc':'vc_class_onvc',
            'vc-class-on-sub-interface':'vc_class_on_sub_interface',
            'vc-class-on-main-interface':'vc_class_on_main_interface',
            'vc-global-default':'vc_global_default',
            'vc-inherit-level-unknown':'vc_inherit_level_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcStateEnum' : _MetaInfoEnum('VcStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'initialized':'initialized',
            'modifying':'modifying',
            'modified':'modified',
            'activating':'activating',
            'activated':'activated',
            'not-verified':'not_verified',
            'ready':'ready',
            'deactivating':'deactivating',
            'inactive':'inactive',
            'deleting':'deleting',
            'deleted':'deleted',
            'state-unknown':'state_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcInheritLevelEnum' : _MetaInfoEnum('VcInheritLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'directly-configured-onvc':'directly_configured_onvc',
            'vc-class-configured-onvc':'vc_class_configured_onvc',
            'vc-class-configured-on-sub-interface':'vc_class_configured_on_sub_interface',
            'vc-class-configured-on-main-interface':'vc_class_configured_on_main_interface',
            'global-default':'global_default',
            'unknown':'unknown',
            'not-supported':'not_supported',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcTrafShapingEnum' : _MetaInfoEnum('VcTrafShapingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'cbr':'cbr',
            'vbr-nrt':'vbr_nrt',
            'vbr-rt':'vbr_rt',
            'abr':'abr',
            'ubr-plus':'ubr_plus',
            'ubr':'ubr',
            'traf-shaping-unknown':'traf_shaping_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcEncapEnum' : _MetaInfoEnum('VcEncapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'ilmi':'ilmi',
            'qsaal':'qsaal',
            'snap':'snap',
            'mux':'mux',
            'nlpid':'nlpid',
            'f4oam':'f4oam',
            'aal0':'aal0',
            'aal5':'aal5',
            'encap-unknown':'encap_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcEnum' : _MetaInfoEnum('VcEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'layer3-vc':'layer3_vc',
            'layer2-vc':'layer2_vc',
            'layer2-vp':'layer2_vp',
            'vc-type-unknown':'vc_type_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcCellPackingModeEnum' : _MetaInfoEnum('VcCellPackingModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'vp':'vp',
            'vc':'vc',
            'port-mode':'port_mode',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VpStateEnum' : _MetaInfoEnum('VpStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'vp-initialized':'vp_initialized',
            'vp-modifying':'vp_modifying',
            'vp-ready':'vp_ready',
            'vp-mgd-down':'vp_mgd_down',
            'vp-deleting':'vp_deleting',
            'vp-deleted':'vp_deleted',
            'vp-state-unknown':'vp_state_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VpTrafShapingEnum' : _MetaInfoEnum('VpTrafShapingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'vp-cbr':'vp_cbr',
            'vp-vbr-nrt':'vp_vbr_nrt',
            'vp-vbr-rt':'vp_vbr_rt',
            'vp-abr':'vp_abr',
            'vp-ubr-plus':'vp_ubr_plus',
            'vp-ubr':'vp_ubr',
            'vp-traf-shaping-unknown':'vp_traf_shaping_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcTestModeEnum' : _MetaInfoEnum('VcTestModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'test-mode-none':'test_mode_none',
            'loop':'loop',
            'reserved':'reserved',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'VcmPortEnum' : _MetaInfoEnum('VcmPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper',
        {
            'port-type-layer-2':'port_type_layer_2',
            'port-type-layer-3':'port_type_layer_3',
            'port-type-unknown':'port_type_unknown',
        }, 'Cisco-IOS-XR-atm-vcm-oper', _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper']),
    'AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData',
            False, 
            [
            _MetaInfoClassMember('local-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local configuration of maximum number of cells
                to be packed per packet
                ''',
                'local_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('max-cell-packed-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum cell packing timeout inmicro seconds
                ''',
                'max_cell_packed_timeout',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('negotiated-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Negotiated value of maximum number of cells to
                be packed per packed
                ''',
                'negotiated_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-packing-data',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Vcs.Vc' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Vcs.Vc',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('amin-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VC is
                administratively UP
                ''',
                'amin_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('burst-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst size in cells
                ''',
                'burst_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('cell-packing-data', REFERENCE_CLASS, 'CellPackingData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData', 
                [], [], 
                '''                Cell packing specific data
                ''',
                'cell_packing_data',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('encaps-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Encapsulation inherit level - identifies if
                encapsulation is set to default, configured on
                the VC, or inherited from the vcclass.
                ''',
                'encaps_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'VcEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncapEnum', 
                [], [], 
                '''                Encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('internal-state', REFERENCE_ENUM_CLASS, 'VcStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcStateEnum', 
                [], [], 
                '''                VC Internal state
                ''',
                'internal_state',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('last-state-change-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time when VC was last changed
                ''',
                'last_state_change_time',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('main-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main Interface handle
                ''',
                'main_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('oper-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VC is
                operationally UP
                ''',
                'oper_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak cell rate in Kbps
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('qos-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Quality of Service inherit level - identifies if
                QoS is set to default, configured on the VC, or
                inherited from the vcclass.
                ''',
                'qos_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('receive-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive MTU
                ''',
                'receive_mtu',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_ENUM_CLASS, 'VcTrafShapingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShapingEnum', 
                [], [], 
                '''                ATM VC traffic shaping type
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sub-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Subinterface handle
                ''',
                'sub_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sustained cell rate in Kbps
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('test-mode', REFERENCE_ENUM_CLASS, 'VcTestModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTestModeEnum', 
                [], [], 
                '''                VC test mode
                ''',
                'test_mode',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('transmit-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmit MTU
                ''',
                'transmit_mtu',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEnum', 
                [], [], 
                '''                VC Type
                ''',
                'type',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                VC Interfcace handle
                ''',
                'vc_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-on-p2p-sub-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VC on Point-to-point Sub-interface
                ''',
                'vc_on_p2p_sub_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-onvp-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VC on VP-tunnel flag
                ''',
                'vc_onvp_tunnel',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vci', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                VCI
                ''',
                'vci',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vci-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VC VCI value
                ''',
                'vci_xr',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                VPI
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VC VPI value
                ''',
                'vpi_xr',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'vc',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Vcs' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Vcs',
            False, 
            [
            _MetaInfoClassMember('vc', REFERENCE_LIST, 'Vc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Vcs.Vc', 
                [], [], 
                '''                All VC information on a node
                ''',
                'vc',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'vcs',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking',
            False, 
            [
            _MetaInfoClassMember('local-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local configuration of maximum number of cells
                to be packed per packet
                ''',
                'local_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('max-cell-packed-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum cell packing timeout inmicro seconds
                ''',
                'max_cell_packed_timeout',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('negotiated-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Negotiated value of maximum number of cells to
                be packed per packed
                ''',
                'negotiated_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-packing',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.CellPacks.CellPack' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.CellPacks.CellPack',
            False, 
            [
            _MetaInfoClassMember('cell-packing', REFERENCE_CLASS, 'CellPacking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking', 
                [], [], 
                '''                Cell packing specific data
                ''',
                'cell_packing',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('cell-packing-mode', REFERENCE_ENUM_CLASS, 'VcCellPackingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcCellPackingModeEnum', 
                [], [], 
                '''                ATM cell packing mode
                ''',
                'cell_packing_mode',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pci', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCI
                ''',
                'pci',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('received-average-cells-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average cells/packets received
                ''',
                'received_average_cells_packets',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sent-cells-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average cells/packets sent
                ''',
                'sent_cells_packets',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sub-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Sub-interface name
                ''',
                'sub_interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VCI
                ''',
                'vci',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPI
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-pack',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.CellPacks' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.CellPacks',
            False, 
            [
            _MetaInfoClassMember('cell-pack', REFERENCE_LIST, 'CellPack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.CellPacks.CellPack', 
                [], [], 
                '''                All cell packing information on a node
                ''',
                'cell_pack',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-packs',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData',
            False, 
            [
            _MetaInfoClassMember('local-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local configuration of maximum number of cells
                to be packed per packet
                ''',
                'local_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('max-cell-packed-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum cell packing timeout inmicro seconds
                ''',
                'max_cell_packed_timeout',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('negotiated-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Negotiated value of maximum number of cells to
                be packed per packed
                ''',
                'negotiated_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-packing-data',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Pvps.Pvp' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Pvps.Pvp',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('amin-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VC is
                administratively UP
                ''',
                'amin_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('burst-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst size in cells
                ''',
                'burst_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('cell-packing-data', REFERENCE_CLASS, 'CellPackingData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData', 
                [], [], 
                '''                Cell packing specific data
                ''',
                'cell_packing_data',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('encaps-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Encapsulation inherit level - identifies if
                encapsulation is set to default, configured on
                the VC, or inherited from the vcclass.
                ''',
                'encaps_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'VcEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncapEnum', 
                [], [], 
                '''                Encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('internal-state', REFERENCE_ENUM_CLASS, 'VcStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcStateEnum', 
                [], [], 
                '''                VC Internal state
                ''',
                'internal_state',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('last-state-change-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time when VC was last changed
                ''',
                'last_state_change_time',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('main-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main Interface handle
                ''',
                'main_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('oper-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VC is
                operationally UP
                ''',
                'oper_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak cell rate in Kbps
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('qos-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Quality of Service inherit level - identifies if
                QoS is set to default, configured on the VC, or
                inherited from the vcclass.
                ''',
                'qos_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('receive-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive MTU
                ''',
                'receive_mtu',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_ENUM_CLASS, 'VcTrafShapingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShapingEnum', 
                [], [], 
                '''                ATM VC traffic shaping type
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sub-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Subinterface handle
                ''',
                'sub_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sustained cell rate in Kbps
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('test-mode', REFERENCE_ENUM_CLASS, 'VcTestModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTestModeEnum', 
                [], [], 
                '''                VC test mode
                ''',
                'test_mode',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('transmit-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmit MTU
                ''',
                'transmit_mtu',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEnum', 
                [], [], 
                '''                VC Type
                ''',
                'type',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                VC Interfcace handle
                ''',
                'vc_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-on-p2p-sub-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VC on Point-to-point Sub-interface
                ''',
                'vc_on_p2p_sub_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-onvp-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VC on VP-tunnel flag
                ''',
                'vc_onvp_tunnel',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vci-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VC VCI value
                ''',
                'vci_xr',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VPI
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VC VPI value
                ''',
                'vpi_xr',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'pvp',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Pvps' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Pvps',
            False, 
            [
            _MetaInfoClassMember('pvp', REFERENCE_LIST, 'Pvp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Pvps.Pvp', 
                [], [], 
                '''                All L2 PVP information on a node
                ''',
                'pvp',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'pvps',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported',
            False, 
            [
            _MetaInfoClassMember('encapsulation-not-supported', REFERENCE_ENUM_CLASS, 'VcEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncapEnum', 
                [], [], 
                '''                Encapsulation type not supported
                ''',
                'encapsulation_not_supported',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('not-supported-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                NotSupportedInheritLevel
                ''',
                'not_supported_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'vc-class-not-supported',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping',
            False, 
            [
            _MetaInfoClassMember('average-output-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average output rate
                ''',
                'average_output_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('burst-output-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst output rate
                ''',
                'burst_output_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('peak-output-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak output rate in Kbps
                ''',
                'peak_output_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('shaping-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Shaping inherit level
                ''',
                'shaping_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('shaping-type', REFERENCE_ENUM_CLASS, 'VcTrafShapingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShapingEnum', 
                [], [], 
                '''                ATM VC traffic shaping type
                ''',
                'shaping_type',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'class-link-shaping',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation',
            False, 
            [
            _MetaInfoClassMember('encapsulation-inherit-level', REFERENCE_ENUM_CLASS, 'VcInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevelEnum', 
                [], [], 
                '''                Encapsulation inherit level
                ''',
                'encapsulation_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'VcEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncapEnum', 
                [], [], 
                '''                Encapsulation type
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'class-link-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc',
            False, 
            [
            _MetaInfoClassMember('ais-rdi-failure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AIS RDI failure
                ''',
                'ais_rdi_failure',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('keep-vc-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keep vc up
                ''',
                'keep_vc_up',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('manage-inherit-level', REFERENCE_ENUM_CLASS, 'ClassLinkOamInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevelEnum', 
                [], [], 
                '''                Manage inherit level
                ''',
                'manage_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('manage-level', REFERENCE_ENUM_CLASS, 'VcManageLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcManageLevelEnum', 
                [], [], 
                '''                Manage Level
                ''',
                'manage_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pvc-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PVC Frequency
                ''',
                'pvc_frequency',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'oam-pvc',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Down Count
                ''',
                'down_count',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('retry-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Retry frequency
                ''',
                'retry_frequency',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('retry-inherit-level', REFERENCE_ENUM_CLASS, 'ClassLinkOamInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevelEnum', 
                [], [], 
                '''                Retry inherit level
                ''',
                'retry_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('retry-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Retry Count
                ''',
                'retry_up_count',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'oam-retry',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi',
            False, 
            [
            _MetaInfoClassMember('ais-rdi-inherit-level', REFERENCE_ENUM_CLASS, 'ClassLinkOamInheritLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevelEnum', 
                [], [], 
                '''                AIS RDI inherit level
                ''',
                'ais_rdi_inherit_level',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('ais-rdi-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AIS RDI up count
                ''',
                'ais_rdi_up_count',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('ais-rdi-up-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time (in seconds) with no AIS/RDI cells before
                declaring a VC as up
                ''',
                'ais_rdi_up_time',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'ais-rdi',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig',
            False, 
            [
            _MetaInfoClassMember('ais-rdi', REFERENCE_CLASS, 'AisRdi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi', 
                [], [], 
                '''                AIS RDI details of a VC class
                ''',
                'ais_rdi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('class-link-encapsulation', REFERENCE_CLASS, 'ClassLinkEncapsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation', 
                [], [], 
                '''                Encapsulation details of VC class
                ''',
                'class_link_encapsulation',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('class-link-shaping', REFERENCE_CLASS, 'ClassLinkShaping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping', 
                [], [], 
                '''                Traffic Shaping detail of VC class
                ''',
                'class_link_shaping',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('oam-pvc', REFERENCE_CLASS, 'OamPvc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc', 
                [], [], 
                '''                OAM PVC details of VC class
                ''',
                'oam_pvc',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('oam-retry', REFERENCE_CLASS, 'OamRetry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry', 
                [], [], 
                '''                OAM Retry details of VC class
                ''',
                'oam_retry',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'oam-config',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks.ClassLink' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks.ClassLink',
            False, 
            [
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VPI
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('oam-config', REFERENCE_CLASS, 'OamConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig', 
                [], [], 
                '''                Oam values for class link
                ''',
                'oam_config',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sub-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Sub-interface handle
                ''',
                'sub_interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vc-class-not-supported', REFERENCE_CLASS, 'VcClassNotSupported' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported', 
                [], [], 
                '''                Not supported VC class
                ''',
                'vc_class_not_supported',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vci', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VCI
                ''',
                'vci',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'class-link',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.ClassLinks' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.ClassLinks',
            False, 
            [
            _MetaInfoClassMember('class-link', REFERENCE_LIST, 'ClassLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks.ClassLink', 
                [], [], 
                '''                All ATM VC information on a node
                ''',
                'class_link',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'class-links',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData',
            False, 
            [
            _MetaInfoClassMember('local-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local configuration of maximum number of cells
                to be packed per packet
                ''',
                'local_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('max-cell-packed-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum cell packing timeout inmicro seconds
                ''',
                'max_cell_packed_timeout',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('negotiated-max-cells-packed-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Negotiated value of maximum number of cells to
                be packed per packed
                ''',
                'negotiated_max_cells_packed_per_packet',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'cell-packing-data',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('cell-packing-data', REFERENCE_CLASS, 'CellPackingData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData', 
                [], [], 
                '''                Cell packing specific information
                ''',
                'cell_packing_data',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('configured-layer2pv-cs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Layer 2 PVCs configured
                ''',
                'configured_layer2pv_cs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('configured-layer2pv-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Layer 2 PVPs configured
                ''',
                'configured_layer2pv_ps',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('configured-layer3pv-cs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Layer 3 PVCs configured
                ''',
                'configured_layer3pv_cs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('configured-layer3vp-tunnels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Layer 3 VP tunnels configured
                ''',
                'configured_layer3vp_tunnels',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('currently-failing-layer2pv-cs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of currently failing Layer 2 PVCs
                ''',
                'currently_failing_layer2pv_cs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('currently-failing-layer2pv-ps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of currently failing Layer 2 PVPs
                ''',
                'currently_failing_layer2pv_ps',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('currently-failing-layer3pv-cs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of currently failing Layer 3 PVCs
                ''',
                'currently_failing_layer3pv_cs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('currently-failing-layer3vp-tunnels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of currently failing Layer 3 VP tunnels
                ''',
                'currently_failing_layer3vp_tunnels',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('ilmi-vci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ILMI VCI
                ''',
                'ilmi_vci',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('ilmi-vpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ILMI VPI
                ''',
                'ilmi_vpi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('l2-cell-packing-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of L2 attachment circuits with the cell
                packing feature enabled on this main interface
                ''',
                'l2_cell_packing_count',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('main-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main Interface handle
                ''',
                'main_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'VcmPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcmPortEnum', 
                [], [], 
                '''                ATM interface port type
                ''',
                'port_type',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pvc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of PVC Failures
                ''',
                'pvc_failures',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pvc-failures-trap-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, PVC failures trap is enabled
                ''',
                'pvc_failures_trap_enable',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pvc-notification-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PVC trap notification interval
                ''',
                'pvc_notification_interval',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                ATM Interface data
                ''',
                'interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.VpTunnels.VpTunnel' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.VpTunnels.VpTunnel',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('amin-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VP is
                administratively UP
                ''',
                'amin_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('burst-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst size in cells
                ''',
                'burst_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('data-vc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Data PVCs under this VP-tunnel
                ''',
                'data_vc_count',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('f4oam-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                F4OAM Enabled flag
                ''',
                'f4oam_enabled',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('internal-state', REFERENCE_ENUM_CLASS, 'VpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VpStateEnum', 
                [], [], 
                '''                Internal state
                ''',
                'internal_state',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('last-vp-state-change-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time when VP-Tunnel state was last changed
                ''',
                'last_vp_state_change_time',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('main-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main Interface handle
                ''',
                'main_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('oper-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE value indicates that the VP is
                operationally UP
                ''',
                'oper_status',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('peak-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak cell rate in Kbps
                ''',
                'peak_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('shape', REFERENCE_ENUM_CLASS, 'VpTrafShapingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VpTrafShapingEnum', 
                [], [], 
                '''                ATM VP traffic shaping type
                ''',
                'shape',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('sustained-cell-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sustained cell rate in Kbps
                ''',
                'sustained_cell_rate',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vp-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                VP Interfcace handle
                ''',
                'vp_interface',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VPI
                ''',
                'vpi',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vpi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VP-Tunnel VPI value
                ''',
                'vpi_xr',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'vp-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node.VpTunnels' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node.VpTunnels',
            False, 
            [
            _MetaInfoClassMember('vp-tunnel', REFERENCE_LIST, 'VpTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.VpTunnels.VpTunnel', 
                [], [], 
                '''                All VP-tunnel information on a node
                ''',
                'vp_tunnel',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'vp-tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-atm-vcm-oper', True),
            _MetaInfoClassMember('cell-packs', REFERENCE_CLASS, 'CellPacks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.CellPacks', 
                [], [], 
                '''                Contains all cell packing information for node
                ''',
                'cell_packs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('class-links', REFERENCE_CLASS, 'ClassLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.ClassLinks', 
                [], [], 
                '''                Contains all class link information for node
                ''',
                'class_links',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Interfaces', 
                [], [], 
                '''                Contains all Interface information for node
                ''',
                'interfaces',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('pvps', REFERENCE_CLASS, 'Pvps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Pvps', 
                [], [], 
                '''                Contains all L2 PVP information for node
                ''',
                'pvps',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vcs', REFERENCE_CLASS, 'Vcs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.Vcs', 
                [], [], 
                '''                Contains all VC information for node
                ''',
                'vcs',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            _MetaInfoClassMember('vp-tunnels', REFERENCE_CLASS, 'VpTunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node.VpTunnels', 
                [], [], 
                '''                Contains all VP-tunnel information for node
                ''',
                'vp_tunnels',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm.Nodes' : {
        'meta_info' : _MetaInfoClass('AtmVcm.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes.Node', 
                [], [], 
                '''                The node on which ATM Interfaces/VCs/VPs are
                located
                ''',
                'node',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
    'AtmVcm' : {
        'meta_info' : _MetaInfoClass('AtmVcm',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'AtmVcm.Nodes', 
                [], [], 
                '''                Contains all the nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-atm-vcm-oper', False),
            ],
            'Cisco-IOS-XR-atm-vcm-oper',
            'atm-vcm',
            _yang_ns._namespaces['Cisco-IOS-XR-atm-vcm-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper'
        ),
    },
}
_meta_table['AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Vcs.Vc']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Vcs.Vc']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Vcs']['meta_info']
_meta_table['AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.CellPacks.CellPack']['meta_info']
_meta_table['AtmVcm.Nodes.Node.CellPacks.CellPack']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.CellPacks']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Pvps.Pvp']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Pvps.Pvp']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Pvps']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.ClassLinks']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.Interfaces']['meta_info']
_meta_table['AtmVcm.Nodes.Node.VpTunnels.VpTunnel']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node.VpTunnels']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Vcs']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node.CellPacks']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Pvps']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node.ClassLinks']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node.VpTunnels']['meta_info'].parent =_meta_table['AtmVcm.Nodes.Node']['meta_info']
_meta_table['AtmVcm.Nodes.Node']['meta_info'].parent =_meta_table['AtmVcm.Nodes']['meta_info']
_meta_table['AtmVcm.Nodes']['meta_info'].parent =_meta_table['AtmVcm']['meta_info']

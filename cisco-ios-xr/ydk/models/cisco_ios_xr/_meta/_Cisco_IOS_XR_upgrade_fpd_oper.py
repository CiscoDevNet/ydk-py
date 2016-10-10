


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'FpdSub1Enum' : _MetaInfoEnum('FpdSub1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper',
        {
            'fpga1':'FPGA1',
            'rommon':'ROMMON',
            'rommona':'ROMMONA',
            'fabric-loader':'FABRIC_LOADER',
            'fpga2':'FPGA2',
            'fpga3':'FPGA3',
            'fpga4':'FPGA4',
            'fpga5':'FPGA5',
            'fpga6':'FPGA6',
            'fpga7':'FPGA7',
            'fpga8':'FPGA8',
            'fpga9':'FPGA9',
            'fpga10':'FPGA10',
            'fpga11':'FPGA11',
            'fpga12':'FPGA12',
            'fpga13':'FPGA13',
            'fpga14':'FPGA14',
            'cpld1':'CPLD1',
            'cpld2':'CPLD2',
            'cpld3':'CPLD3',
            'cpld4':'CPLD4',
            'cpld5':'CPLD5',
            'cpld6':'CPLD6',
            'cbc':'CBC',
            'hsbi':'HSBI',
            'txpod':'TXPOD',
            'rxpod':'RXPOD',
            'ibmc':'IBMC',
            'fsbl':'FSBL',
            'lnx':'LNX',
            'fpga15':'FPGA15',
            'fpga16':'FPGA16',
            'fc-fsbl':'FC_FSBL',
            'fc-lnx':'FC_LNX',
        }, 'Cisco-IOS-XR-upgrade-fpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper']),
    'FpdEnum' : _MetaInfoEnum('FpdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper',
        {
            'spa':'SPA',
            'lc':'LC',
            'sam':'SAM',
        }, 'Cisco-IOS-XR-upgrade-fpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper']),
    'Fpd1Enum' : _MetaInfoEnum('Fpd1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper',
        {
            'spa':'SPA',
            'lc':'LC',
            'sam':'SAM',
        }, 'Cisco-IOS-XR-upgrade-fpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper']),
    'FpdSubEnum' : _MetaInfoEnum('FpdSubEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper',
        {
            'fpga1':'FPGA1',
            'rommon':'ROMMON',
            'rommona':'ROMMONA',
            'fabldr':'FABLDR',
            'fpga2':'FPGA2',
            'fpga3':'FPGA3',
            'fpga4':'FPGA4',
            'fpga5':'FPGA5',
            'fpga6':'FPGA6',
            'fpga7':'FPGA7',
            'fpga8':'FPGA8',
            'fpga9':'FPGA9',
            'fpga10':'FPGA10',
            'fpga11':'FPGA11',
            'fpga12':'FPGA12',
            'fpga13':'FPGA13',
            'fpga14':'FPGA14',
            'cpld1':'CPLD1',
            'cpld2':'CPLD2',
            'cpld3':'CPLD3',
            'cpld4':'CPLD4',
            'cpld5':'CPLD5',
            'cpld6':'CPLD6',
            'cbc':'CBC',
            'hsbi':'HSBI',
            'txpod':'TXPOD',
            'rxpod':'RXPOD',
            'ibmc':'IBMC',
            'fsbl':'FSBL',
            'lnx':'LNX',
            'fpga15':'FPGA15',
            'fpga16':'FPGA16',
            'fc-fsbl':'FC_FSBL',
            'fc-lnx':'FC_LNX',
        }, 'Cisco-IOS-XR-upgrade-fpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper']),
    'Fpd.Nodes.Node.Devices.Device' : {
        'meta_info' : _MetaInfoClass('Fpd.Nodes.Node.Devices.Device',
            False, 
            [
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card type containing FPD
                ''',
                'card_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('fpd-type', REFERENCE_ENUM_CLASS, 'FpdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'FpdEnum', 
                [], [], 
                '''                FPD type
                ''',
                'fpd_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('hardware-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FPD hardware version inX.Y format. X-Major
                version, Y-Minor version
                ''',
                'hardware_version',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('is-upgrade-downgrade', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, upgrade or downgrade
                ''',
                'is_upgrade_downgrade',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('software-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FPD software version in X.Y format X-Major
                version, Y-Minor version Note: 'Unknown' is
                returned in case the software version of the FPD
                cannot be determined.
                ''',
                'software_version',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('sub-type', REFERENCE_ENUM_CLASS, 'FpdSubEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'FpdSubEnum', 
                [], [], 
                '''                FPD sub type
                ''',
                'sub_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'device',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd.Nodes.Node.Devices' : {
        'meta_info' : _MetaInfoClass('Fpd.Nodes.Node.Devices',
            False, 
            [
            _MetaInfoClassMember('device', REFERENCE_LIST, 'Device' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Nodes.Node.Devices.Device', 
                [], [], 
                '''                FPD information for a particular fpd type
                ''',
                'device',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'devices',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Fpd.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-upgrade-fpd-oper', True),
            _MetaInfoClassMember('devices', REFERENCE_CLASS, 'Devices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Nodes.Node.Devices', 
                [], [], 
                '''                FPD information table
                ''',
                'devices',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd.Nodes' : {
        'meta_info' : _MetaInfoClass('Fpd.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Nodes.Node', 
                [], [], 
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd.Packages.AllPackage' : {
        'meta_info' : _MetaInfoClass('Fpd.Packages.AllPackage',
            False, 
            [
            _MetaInfoClassMember('card-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card description
                ''',
                'card_description',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card type containing FPD
                ''',
                'card_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('fpd-sub-type', REFERENCE_ENUM_CLASS, 'FpdSub1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'FpdSub1Enum', 
                [], [], 
                '''                FPD sub type
                ''',
                'fpd_sub_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('fpd-type', REFERENCE_ENUM_CLASS, 'Fpd1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd1Enum', 
                [], [], 
                '''                FPD type
                ''',
                'fpd_type',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('minimum-required-hardware-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum required FPD hardware version in X.Y
                format X-Major version, Y-Minor version 
                ''',
                'minimum_required_hardware_version',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('minimum-required-software-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum required FPD software version in X.Y
                format X-Major version, Y-Minor version Note:
                'Unknown' is returned in case the software
                version of the FPD cannot be determined.
                ''',
                'minimum_required_software_version',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('software-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FPD software version in X.Y format X-Major
                version, Y-Minor version Note: 'Unknown' is
                returned in case the software version of the FPD
                cannot be determined.
                ''',
                'software_version',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'all-package',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd.Packages' : {
        'meta_info' : _MetaInfoClass('Fpd.Packages',
            False, 
            [
            _MetaInfoClassMember('all-package', REFERENCE_LIST, 'AllPackage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Packages.AllPackage', 
                [], [], 
                '''                List of packages
                ''',
                'all_package',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'packages',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
    'Fpd' : {
        'meta_info' : _MetaInfoClass('Fpd',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Nodes', 
                [], [], 
                '''                List of FPD supported nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            _MetaInfoClassMember('packages', REFERENCE_CLASS, 'Packages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper', 'Fpd.Packages', 
                [], [], 
                '''                FPD packages information
                ''',
                'packages',
                'Cisco-IOS-XR-upgrade-fpd-oper', False),
            ],
            'Cisco-IOS-XR-upgrade-fpd-oper',
            'fpd',
            _yang_ns._namespaces['Cisco-IOS-XR-upgrade-fpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper'
        ),
    },
}
_meta_table['Fpd.Nodes.Node.Devices.Device']['meta_info'].parent =_meta_table['Fpd.Nodes.Node.Devices']['meta_info']
_meta_table['Fpd.Nodes.Node.Devices']['meta_info'].parent =_meta_table['Fpd.Nodes.Node']['meta_info']
_meta_table['Fpd.Nodes.Node']['meta_info'].parent =_meta_table['Fpd.Nodes']['meta_info']
_meta_table['Fpd.Packages.AllPackage']['meta_info'].parent =_meta_table['Fpd.Packages']['meta_info']
_meta_table['Fpd.Nodes']['meta_info'].parent =_meta_table['Fpd']['meta_info']
_meta_table['Fpd.Packages']['meta_info'].parent =_meta_table['Fpd']['meta_info']

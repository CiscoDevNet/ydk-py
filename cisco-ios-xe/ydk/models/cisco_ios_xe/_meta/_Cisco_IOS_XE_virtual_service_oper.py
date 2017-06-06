


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VirtualServices.VirtualService.Details.PackageInformation.Application' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.PackageInformation.Application',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the application.
                ''',
                'description',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('installed-version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the application.
                ''',
                'installed_version',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the application.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'application',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.PackageInformation.Signing' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.PackageInformation.Signing',
            False, 
            [
            _MetaInfoClassMember('key-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Type of the signed key.
                ''',
                'key_type',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The method the key was signed.
                ''',
                'method',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'signing',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.PackageInformation.Licensing' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.PackageInformation.Licensing',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the license.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The version of the license.
                ''',
                'version',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'licensing',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.PackageInformation' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.PackageInformation',
            False, 
            [
            _MetaInfoClassMember('application', REFERENCE_CLASS, 'Application' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.PackageInformation.Application', 
                [], [], 
                '''                Details of the application.
                ''',
                'application',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('licensing', REFERENCE_CLASS, 'Licensing' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.PackageInformation.Licensing', 
                [], [], 
                '''                Details about the license.
                ''',
                'licensing',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the package for the virtual-service.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path to the package.
                ''',
                'path',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('signing', REFERENCE_CLASS, 'Signing' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.PackageInformation.Signing', 
                [], [], 
                '''                Details of the key signing.
                ''',
                'signing',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'package-information',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Memory of the proccess.
                ''',
                'memory',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the proccess.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process ID.
                ''',
                'pid',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status of the proccess.
                ''',
                'status',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up time of the proccess.
                ''',
                'uptime',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'processes',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.DetailedGuestStatus' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.DetailedGuestStatus',
            False, 
            [
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes', 
                [], [], 
                '''                All the processes.
                ''',
                'processes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'detailed-guest-status',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.ResourceReservation' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.ResourceReservation',
            False, 
            [
            _MetaInfoClassMember('cpu', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The percentage of reserved cpu.
                ''',
                'cpu',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('disk', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The amount of reserverd disk space in MB.
                ''',
                'disk',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The amount of reserved memory in MB.
                ''',
                'memory',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'resource-reservation',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details.ResourceAdmission' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details.ResourceAdmission',
            False, 
            [
            _MetaInfoClassMember('cpu', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The percentage of cpu being allocated for the virtual-service
                ''',
                'cpu',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('disk-space', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The amount of disk space being allocated for the virtual-service.
                ''',
                'disk_space',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('memory', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The amount of memory being allocated for the virtual-service.
                ''',
                'memory',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Thes status the of the resource allocation.
                ''',
                'state',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('vcpus', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The amount of VCPUs being allocated for the virtual-service.
                ''',
                'vcpus',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'resource-admission',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Details' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Details',
            False, 
            [
            _MetaInfoClassMember('activated-profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The activated profile name.
                ''',
                'activated_profile_name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('detailed-guest-status', REFERENCE_CLASS, 'DetailedGuestStatus' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.DetailedGuestStatus', 
                [], [], 
                '''                Details on the guest status.
                ''',
                'detailed_guest_status',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('guest-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of a guest interface.
                ''',
                'guest_interface',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('package-information', REFERENCE_CLASS, 'PackageInformation' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.PackageInformation', 
                [], [], 
                '''                Details of the package for the virtual-service.
                ''',
                'package_information',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('resource-admission', REFERENCE_CLASS, 'ResourceAdmission' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.ResourceAdmission', 
                [], [], 
                '''                Resources being allocated for the virtual-service.
                ''',
                'resource_admission',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('resource-reservation', REFERENCE_CLASS, 'ResourceReservation' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details.ResourceReservation', 
                [], [], 
                '''                Details of the resources reserved for this virtual service.
                ''',
                'resource_reservation',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                State of the virtual service.
                ''',
                'state',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Utilization.CpuUtil' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Utilization.CpuUtil',
            False, 
            [
            _MetaInfoClassMember('actual-application-util', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Percetnage of CPU actual utilization for the virtual-service.
                ''',
                'actual_application_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('cpu-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The state of the CPU utilization for the virtual-service.
                ''',
                'cpu_state',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('requested-application-util', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Percentage of requested CPU utilization by the virtual-service.
                ''',
                'requested_application_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'cpu-util',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Utilization.MemoryUtil' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Utilization.MemoryUtil',
            False, 
            [
            _MetaInfoClassMember('memory-allocation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Amount of memory being allocated for the virtual-service in KB.
                ''',
                'memory_allocation',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('memory-used', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Amount of memory being used for the virtual-service in KB.
                ''',
                'memory_used',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'memory-util',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.Utilization' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.Utilization',
            False, 
            [
            _MetaInfoClassMember('cpu-util', REFERENCE_CLASS, 'CpuUtil' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Utilization.CpuUtil', 
                [], [], 
                '''                Details on the CPU utilization for the virtual-service.
                ''',
                'cpu_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('memory-util', REFERENCE_CLASS, 'MemoryUtil' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Utilization.MemoryUtil', 
                [], [], 
                '''                Details on the memory usage for the virtual-service.
                ''',
                'memory_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the virtual service.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'utilization',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.NetworkUtils.NetworkUtil' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.NetworkUtils.NetworkUtil',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the network that is being used for the virtual-service.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The alias of the network that is being used for the virtual-service.
                ''',
                'alias',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('rx-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of rx bytes being utilized for the virtual-service.
                ''',
                'rx_bytes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('rx-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of rx errors.
                ''',
                'rx_errors',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('rx-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of rx packets being utilized for the virtual-service.
                ''',
                'rx_packets',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('tx-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of tx bytes being utilized for the virtual-service.
                ''',
                'tx_bytes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('tx-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of tx errors.
                ''',
                'tx_errors',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('tx-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of tx packets being utilized for the virtual-service.
                ''',
                'tx_packets',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'network-util',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.NetworkUtils' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.NetworkUtils',
            False, 
            [
            _MetaInfoClassMember('network-util', REFERENCE_LIST, 'NetworkUtil' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.NetworkUtils.NetworkUtil', 
                [], [], 
                '''                Details on a network utilization for the virtual-service.
                ''',
                'network_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'network-utils',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.StorageUtils.StorageUtil' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.StorageUtils.StorageUtil',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the storage process being used for the virtual-service.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The alias of the storage process being used for the virtual-service.
                ''',
                'alias',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('available', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The available storage in 1K blocks.
                ''',
                'available',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('capacity', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The storage capactity in 1K blocks.
                ''',
                'capacity',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The name of errors on the storage process.
                ''',
                'errors',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('rd-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of RD bytes being used for the virtual-service.
                ''',
                'rd_bytes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('rd-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of rd requests being used for the virtual-service.
                ''',
                'rd_requests',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('usage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percetage of storage capactiy being used.
                ''',
                'usage',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of 1K blocks being used.
                ''',
                'used',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('wr-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of WR bytes for the virtual-service.
                ''',
                'wr_bytes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('wr-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of WR requests for the virtual-service.
                ''',
                'wr_requests',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'storage-util',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.StorageUtils' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.StorageUtils',
            False, 
            [
            _MetaInfoClassMember('storage-util', REFERENCE_LIST, 'StorageUtil' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.StorageUtils.StorageUtil', 
                [], [], 
                '''                Details on a storage utilization for the virtual-service.
                ''',
                'storage_util',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'storage-utils',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.AttachedDevices.AttachedDevice' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.AttachedDevices.AttachedDevice',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the attached device.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The alias for the attached device.
                ''',
                'alias',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The type of the attached device.
                ''',
                'type',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'attached-device',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.AttachedDevices' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.AttachedDevices',
            False, 
            [
            _MetaInfoClassMember('attached-device', REFERENCE_LIST, 'AttachedDevice' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.AttachedDevices.AttachedDevice', 
                [], [], 
                '''                List of attached devices.
                ''',
                'attached_device',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'attached-devices',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address for the network interface.
                ''',
                'mac_address',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('attached-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the the attached interface
                ''',
                'attached_interface',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'network-interface',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.NetworkInterfaces' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.NetworkInterfaces',
            False, 
            [
            _MetaInfoClassMember('network-interface', REFERENCE_LIST, 'NetworkInterface' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface', 
                [], [], 
                '''                Details for a network interface.
                ''',
                'network_interface',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'network-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.GuestRoutes.GuestRoute' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.GuestRoutes.GuestRoute',
            False, 
            [
            _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A guest route for a guest interface.
                ''',
                'route',
                'Cisco-IOS-XE-virtual-service-oper', True),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'guest-route',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService.GuestRoutes' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService.GuestRoutes',
            False, 
            [
            _MetaInfoClassMember('guest-route', REFERENCE_LIST, 'GuestRoute' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.GuestRoutes.GuestRoute', 
                [], [], 
                '''                List of guest routes for a guest interface.
                ''',
                'guest_route',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'guest-routes',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices.VirtualService' : {
        'meta_info' : _MetaInfoClass('VirtualServices.VirtualService',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the virtual service.
                ''',
                'name',
                'Cisco-IOS-XE-virtual-service-oper', True),
            _MetaInfoClassMember('attached-devices', REFERENCE_CLASS, 'AttachedDevices' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.AttachedDevices', 
                [], [], 
                '''                Details for the devices attached to this virtual service.
                ''',
                'attached_devices',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Details', 
                [], [], 
                '''                Details of the virtual service.
                ''',
                'details',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('guest-routes', REFERENCE_CLASS, 'GuestRoutes' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.GuestRoutes', 
                [], [], 
                '''                Routes for the guest interface.
                ''',
                'guest_routes',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('network-interfaces', REFERENCE_CLASS, 'NetworkInterfaces' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.NetworkInterfaces', 
                [], [], 
                '''                Details for the network interfaces.
                ''',
                'network_interfaces',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('network-utils', REFERENCE_CLASS, 'NetworkUtils' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.NetworkUtils', 
                [], [], 
                '''                list of the network utilizations for the virtual-service.
                ''',
                'network_utils',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('storage-utils', REFERENCE_CLASS, 'StorageUtils' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.StorageUtils', 
                [], [], 
                '''                List of the storage utilizations for the virtual-service.
                ''',
                'storage_utils',
                'Cisco-IOS-XE-virtual-service-oper', False),
            _MetaInfoClassMember('utilization', REFERENCE_CLASS, 'Utilization' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService.Utilization', 
                [], [], 
                '''                Utilization of device resources for a virtual-service.
                ''',
                'utilization',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'virtual-service',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
    'VirtualServices' : {
        'meta_info' : _MetaInfoClass('VirtualServices',
            False, 
            [
            _MetaInfoClassMember('virtual-service', REFERENCE_LIST, 'VirtualService' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper', 'VirtualServices.VirtualService', 
                [], [], 
                '''                A virtual service.
                ''',
                'virtual_service',
                'Cisco-IOS-XE-virtual-service-oper', False),
            ],
            'Cisco-IOS-XE-virtual-service-oper',
            'virtual-services',
            _yang_ns._namespaces['Cisco-IOS-XE-virtual-service-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper'
        ),
    },
}
_meta_table['VirtualServices.VirtualService.Details.PackageInformation.Application']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details.PackageInformation']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.PackageInformation.Signing']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details.PackageInformation']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.PackageInformation.Licensing']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details.PackageInformation']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details.DetailedGuestStatus']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.PackageInformation']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.DetailedGuestStatus']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.ResourceReservation']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details']['meta_info']
_meta_table['VirtualServices.VirtualService.Details.ResourceAdmission']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Details']['meta_info']
_meta_table['VirtualServices.VirtualService.Utilization.CpuUtil']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Utilization']['meta_info']
_meta_table['VirtualServices.VirtualService.Utilization.MemoryUtil']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.Utilization']['meta_info']
_meta_table['VirtualServices.VirtualService.NetworkUtils.NetworkUtil']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.NetworkUtils']['meta_info']
_meta_table['VirtualServices.VirtualService.StorageUtils.StorageUtil']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.StorageUtils']['meta_info']
_meta_table['VirtualServices.VirtualService.AttachedDevices.AttachedDevice']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.AttachedDevices']['meta_info']
_meta_table['VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.NetworkInterfaces']['meta_info']
_meta_table['VirtualServices.VirtualService.GuestRoutes.GuestRoute']['meta_info'].parent =_meta_table['VirtualServices.VirtualService.GuestRoutes']['meta_info']
_meta_table['VirtualServices.VirtualService.Details']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.Utilization']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.NetworkUtils']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.StorageUtils']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.AttachedDevices']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.NetworkInterfaces']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService.GuestRoutes']['meta_info'].parent =_meta_table['VirtualServices.VirtualService']['meta_info']
_meta_table['VirtualServices.VirtualService']['meta_info'].parent =_meta_table['VirtualServices']['meta_info']

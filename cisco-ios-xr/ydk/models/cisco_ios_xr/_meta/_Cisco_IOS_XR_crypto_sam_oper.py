


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LogTablesEnum' : _MetaInfoEnum('LogTablesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unkown':'unkown',
            'memory-digest-table':'memory_digest_table',
            'system-database-digest':'system_database_digest',
            'sam-tables':'sam_tables',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'CertificateIssuerEnum' : _MetaInfoEnum('CertificateIssuerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'unknown',
            'code-signing-server-certificate-authority':'code_signing_server_certificate_authority',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'LogErrorEnum' : _MetaInfoEnum('LogErrorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'unknown',
            'log-message-error':'log_message_error',
            'get-issuer-name-failed':'get_issuer_name_failed',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'LogCodeEnum' : _MetaInfoEnum('LogCodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper',
        {
            'unknown':'unknown',
            'sam-server-restared-router-reboot':'sam_server_restared_router_reboot',
            'sam-server-restared':'sam_server_restared',
            'added-certificate-in-table':'added_certificate_in_table',
            'copied-certificate-in-table':'copied_certificate_in_table',
            'certificate-flag-changed':'certificate_flag_changed',
            'validated-certificate':'validated_certificate',
            'certificate-expired-detected':'certificate_expired_detected',
            'certificate-revoked-detected':'certificate_revoked_detected',
            'ca-certificate-expired-detected':'ca_certificate_expired_detected',
            'ca-certificate-revoked-detected':'ca_certificate_revoked_detected',
            'deleted-certificate-from-table':'deleted_certificate_from_table',
            'crl-added-updated-in-table':'crl_added_updated_in_table',
            'checked-memory-digest':'checked_memory_digest',
            'nvram-digest-mismatch-detected':'nvram_digest_mismatch_detected',
            'insecure-backup-file-detected':'insecure_backup_file_detected',
            'error-restore-operation':'error_restore_operation',
            'backup-file-on-nvram-deleted':'backup_file_on_nvram_deleted',
            'sam-log-file-recovered-from-system-database':'sam_log_file_recovered_from_system_database',
            'validated-elf':'validated_elf',
            'namespace-deleted-recovered-by-sam':'namespace_deleted_recovered_by_sam',
        }, 'Cisco-IOS-XR-crypto-sam-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper']),
    'Sam.SystemInformation' : {
        'meta_info' : _MetaInfoClass('Sam.SystemInformation',
            False, 
            [
            _MetaInfoClassMember('is-default-response', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if promptdefault response is true
                ''',
                'is_default_response',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-running', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if SAM status information runs
                ''',
                'is_running',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('prompt-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prompt interval atreboot time in seconds
                ''',
                'prompt_interval',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'system-information',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents.LogContent.Logs' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents.LogContent.Logs',
            False, 
            [
            _MetaInfoClassMember('code', REFERENCE_ENUM_CLASS, 'LogCodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogCodeEnum', 
                [], [], 
                '''                Log code
                ''',
                'code',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'LogErrorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogErrorEnum', 
                [], [], 
                '''                Log error message
                ''',
                'error',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Device index
                ''',
                'index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_ENUM_CLASS, 'CertificateIssuerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'CertificateIssuerEnum', 
                [], [], 
                '''                Issuer of the certificate
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('sam-table-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAM table index
                ''',
                'sam_table_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('serial-no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Serial number
                ''',
                'serial_no',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('source-device', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                source device name
                ''',
                'source_device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('table', REFERENCE_ENUM_CLASS, 'LogTablesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogTablesEnum', 
                [], [], 
                '''                Log table information
                ''',
                'table',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('target-device', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target device
                ''',
                'target_device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Log time
                ''',
                'time',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last update time of the certificate
                ''',
                'update_time',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents.LogContent' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents.LogContent',
            False, 
            [
            _MetaInfoClassMember('number-of-lines', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of lines
                ''',
                'number_of_lines',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('entries-shown', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total entries shown
                ''',
                'entries_shown',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('logs', REFERENCE_LIST, 'Logs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents.LogContent.Logs', 
                [], [], 
                '''                SAM logs
                ''',
                'logs',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('total-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total log entries available
                ''',
                'total_entries',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'log-content',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.LogContents' : {
        'meta_info' : _MetaInfoClass('Sam.LogContents',
            False, 
            [
            _MetaInfoClassMember('log-content', REFERENCE_LIST, 'LogContent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents.LogContent', 
                [], [], 
                '''                Number of lines for SAM log message
                ''',
                'log_content',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.Brief.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.Brief.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.Brief' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.Brief',
            False, 
            [
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.Brief.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail',
            False, 
            [
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specify certificate index
                ''',
                'index',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail', 
                [], [], 
                '''                Certificate table detail information
                ''',
                'detail',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-index',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate.CertificateIndexes' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate.CertificateIndexes',
            False, 
            [
            _MetaInfoClassMember('certificate-index', REFERENCE_LIST, 'CertificateIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex', 
                [], [], 
                '''                Certificate detail index information
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device.Certificate' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device.Certificate',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.Brief', 
                [], [], 
                '''                Certificate table brief information
                ''',
                'brief',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-indexes', REFERENCE_CLASS, 'CertificateIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate.CertificateIndexes', 
                [], [], 
                '''                Certificate detail index table information
                ''',
                'certificate_indexes',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices.Device' : {
        'meta_info' : _MetaInfoClass('Sam.Devices.Device',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Specify device name
                ''',
                'device_name',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate', REFERENCE_CLASS, 'Certificate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device.Certificate', 
                [], [], 
                '''                Certificate table information
                ''',
                'certificate',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'device',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Devices' : {
        'meta_info' : _MetaInfoClass('Sam.Devices',
            False, 
            [
            _MetaInfoClassMember('device', REFERENCE_LIST, 'Device' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices.Device', 
                [], [], 
                '''                Certificate table device information
                ''',
                'device',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'devices',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages.Package.CertificateFlags' : {
        'meta_info' : _MetaInfoClass('Sam.Packages.Package.CertificateFlags',
            False, 
            [
            _MetaInfoClassMember('is-expired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Expired flag
                ''',
                'is_expired',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-revoked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Revoked flag
                ''',
                'is_revoked',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-trusted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Trusted flag
                ''',
                'is_trusted',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('is-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Validated flag
                ''',
                'is_validated',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages.Package' : {
        'meta_info' : _MetaInfoClass('Sam.Packages.Package',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify package name
                ''',
                'package_name',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate-flags', REFERENCE_CLASS, 'CertificateFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages.Package.CertificateFlags', 
                [], [], 
                '''                Certificate flags
                ''',
                'certificate_flags',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Certificate index
                ''',
                'certificate_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate location
                ''',
                'location',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.Packages' : {
        'meta_info' : _MetaInfoClass('Sam.Packages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages.Package', 
                [], [], 
                '''                SAM certificate information for a specific
                package
                ''',
                'package',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'packages',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer',
            False, 
            [
            _MetaInfoClassMember('common-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common name
                ''',
                'common_name',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('country', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Country
                ''',
                'country',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('organization', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Organization
                ''',
                'organization',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'issuer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_CLASS, 'Issuer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer', 
                [], [], 
                '''                Issuer name
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('updates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Updated time of CRL is displayed
                ''',
                'updates',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation-list-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations.CertificateRevocation' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations.CertificateRevocation',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', True),
            _MetaInfoClassMember('certificate-revocation-list-detail', REFERENCE_CLASS, 'CertificateRevocationListDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail', 
                [], [], 
                '''                Certificate revocation list detail information
                ''',
                'certificate_revocation_list_detail',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocations' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocations',
            False, 
            [
            _MetaInfoClassMember('certificate-revocation', REFERENCE_LIST, 'CertificateRevocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations.CertificateRevocation', 
                [], [], 
                '''                Certificate revocation list index information
                ''',
                'certificate_revocation',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocations',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocationListSummary.Issuer' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocationListSummary.Issuer',
            False, 
            [
            _MetaInfoClassMember('common-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common name
                ''',
                'common_name',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('country', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Country
                ''',
                'country',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('organization', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Organization
                ''',
                'organization',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'issuer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam.CertificateRevocationListSummary' : {
        'meta_info' : _MetaInfoClass('Sam.CertificateRevocationListSummary',
            False, 
            [
            _MetaInfoClassMember('crl-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 CRL index
                ''',
                'crl_index',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('issuer', REFERENCE_CLASS, 'Issuer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocationListSummary.Issuer', 
                [], [], 
                '''                Issuer name
                ''',
                'issuer',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('updates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Updated time of CRL is displayed
                ''',
                'updates',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'certificate-revocation-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
    'Sam' : {
        'meta_info' : _MetaInfoClass('Sam',
            False, 
            [
            _MetaInfoClassMember('certificate-revocation-list-summary', REFERENCE_CLASS, 'CertificateRevocationListSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocationListSummary', 
                [], [], 
                '''                Certificate revocation list summary information 
                ''',
                'certificate_revocation_list_summary',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('certificate-revocations', REFERENCE_CLASS, 'CertificateRevocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.CertificateRevocations', 
                [], [], 
                '''                Certificate revocation list index table
                information
                ''',
                'certificate_revocations',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('devices', REFERENCE_CLASS, 'Devices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Devices', 
                [], [], 
                '''                Certificate device table information
                ''',
                'devices',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.LogContents', 
                [], [], 
                '''                SAM log content table information
                ''',
                'log_contents',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('packages', REFERENCE_CLASS, 'Packages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.Packages', 
                [], [], 
                '''                SAM certificate information  package
                ''',
                'packages',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            _MetaInfoClassMember('system-information', REFERENCE_CLASS, 'SystemInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'Sam.SystemInformation', 
                [], [], 
                '''                SAM system information
                ''',
                'system_information',
                'Cisco-IOS-XR-crypto-sam-oper', False),
            ],
            'Cisco-IOS-XR-crypto-sam-oper',
            'sam',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper'
        ),
    },
}
_meta_table['Sam.LogContents.LogContent.Logs']['meta_info'].parent =_meta_table['Sam.LogContents.LogContent']['meta_info']
_meta_table['Sam.LogContents.LogContent']['meta_info'].parent =_meta_table['Sam.LogContents']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.Brief.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate']['meta_info']
_meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info'].parent =_meta_table['Sam.Devices.Device.Certificate']['meta_info']
_meta_table['Sam.Devices.Device.Certificate']['meta_info'].parent =_meta_table['Sam.Devices.Device']['meta_info']
_meta_table['Sam.Devices.Device']['meta_info'].parent =_meta_table['Sam.Devices']['meta_info']
_meta_table['Sam.Packages.Package.CertificateFlags']['meta_info'].parent =_meta_table['Sam.Packages.Package']['meta_info']
_meta_table['Sam.Packages.Package']['meta_info'].parent =_meta_table['Sam.Packages']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer']['meta_info'].parent =_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info'].parent =_meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info']
_meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info'].parent =_meta_table['Sam.CertificateRevocations']['meta_info']
_meta_table['Sam.CertificateRevocationListSummary.Issuer']['meta_info'].parent =_meta_table['Sam.CertificateRevocationListSummary']['meta_info']
_meta_table['Sam.SystemInformation']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.LogContents']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.Devices']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.Packages']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.CertificateRevocations']['meta_info'].parent =_meta_table['Sam']['meta_info']
_meta_table['Sam.CertificateRevocationListSummary']['meta_info'].parent =_meta_table['Sam']['meta_info']

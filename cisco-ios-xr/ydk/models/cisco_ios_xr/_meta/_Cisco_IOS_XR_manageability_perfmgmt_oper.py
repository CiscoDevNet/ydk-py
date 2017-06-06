


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('checksum-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with checksum errors
                ''',
                'checksum_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples', 
                [], [], 
                '''                Sample Table for an OSPV v2 instance
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv2-protocol-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-instance', REFERENCE_LIST, 'Ospfv2ProtocolInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance', 
                [], [], 
                '''                Protocol samples for a particular OSPF v2
                instance
                ''',
                'ospfv2_protocol_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv2-protocol-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('input-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples', 
                [], [], 
                '''                Sample Table for an OSPV v3 instance
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv3-protocol-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances',
            False, 
            [
            _MetaInfoClassMember('ospfv3-protocol-instance', REFERENCE_LIST, 'Ospfv3ProtocolInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance', 
                [], [], 
                '''                Protocol samples for a particular OSPF v3
                instance
                ''',
                'ospfv3_protocol_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv3-protocol-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Ospf' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-instances', REFERENCE_CLASS, 'Ospfv2ProtocolInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances', 
                [], [], 
                '''                OSPF v2 instances for which protocol statistics
                are collected
                ''',
                'ospfv2_protocol_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('ospfv3-protocol-instances', REFERENCE_CLASS, 'Ospfv3ProtocolInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances', 
                [], [], 
                '''                OSPF v3 instances for which protocol statistics
                are collected
                ''',
                'ospfv3_protocol_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('address-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address messages received
                ''',
                'address_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address messages sent
                ''',
                'address_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-withdraw-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address withdraw messages received
                ''',
                'address_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-withdraw-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address withdraw messages sent
                ''',
                'address_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('init-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tnit messages received
                ''',
                'init_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('init-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Init messages sent
                ''',
                'init_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('keepalive-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive messages received
                ''',
                'keepalive_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('keepalive-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive messages sent
                ''',
                'keepalive_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-mapping-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label mapping messages received
                ''',
                'label_mapping_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-mapping-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label mapping messages sent
                ''',
                'label_mapping_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-release-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label release messages received
                ''',
                'label_release_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-release-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label release messages sent
                ''',
                'label_release_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-withdraw-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label withdraw messages received
                ''',
                'label_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-withdraw-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label withdraw messages sent
                ''',
                'label_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('notification-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Notification messages received
                ''',
                'notification_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('notification-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Notification messages sent
                ''',
                'notification_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('total-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total messages received
                ''',
                'total_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('total-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total messages sent
                ''',
                'total_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample', 
                [], [], 
                '''                LDP neighbor statistics sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor',
            False, 
            [
            _MetaInfoClassMember('nbr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor Address
                ''',
                'nbr',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples', 
                [], [], 
                '''                Samples for a particular LDP neighbor
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ldp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Mpls.LdpNeighbors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Mpls.LdpNeighbors',
            False, 
            [
            _MetaInfoClassMember('ldp-neighbor', REFERENCE_LIST, 'LdpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor', 
                [], [], 
                '''                Samples for a particular LDP neighbor
                ''',
                'ldp_neighbor',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ldp-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Mpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Mpls',
            False, 
            [
            _MetaInfoClassMember('ldp-neighbors', REFERENCE_CLASS, 'LdpNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Mpls.LdpNeighbors', 
                [], [], 
                '''                LDP neighbors for which statistics are
                collected
                ''',
                'ldp_neighbors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('average-cpu-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average system %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('no-processes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of processes in the system
                ''',
                'no_processes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.SampleXr' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.SampleXr',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample', 
                [], [], 
                '''                Node CPU data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('average-cpu-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('no-threads', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of threads
                ''',
                'no_threads',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('peak-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max. dynamic memory (KBytes) used since startup
                time
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample', 
                [], [], 
                '''                Process data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Processes.Process' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Processes.Process',
            False, 
            [
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Process ID
                ''',
                'process_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples', 
                [], [], 
                '''                Process data
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Processes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Processes',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Processes.Process', 
                [], [], 
                '''                Process data
                ''',
                'process',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'processes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('curr-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current application memory (Bytes) in use
                ''',
                'curr_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('peak-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max. system memory (MBytes) used since bootup
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Samples.Sample', 
                [], [], 
                '''                Node Memory data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Processes', 
                [], [], 
                '''                Processes data
                ''',
                'processes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('sample-xr', REFERENCE_CLASS, 'SampleXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.SampleXr', 
                [], [], 
                '''                Node CPU data
                ''',
                'sample_xr',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node.Samples', 
                [], [], 
                '''                Node Memory data
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes.Node', 
                [], [], 
                '''                Node Instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('conn-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times connection was dropped
                ''',
                'conn_dropped',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('conn-established', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the connection was established
                ''',
                'conn_established',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('errors-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of error notifications received on the
                connection
                ''',
                'errors_received',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('errors-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of error notifications sent on the
                connection
                ''',
                'errors_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages received
                ''',
                'input_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of update messages received
                ''',
                'input_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent
                ''',
                'output_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of update messages sent
                ''',
                'output_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample', 
                [], [], 
                '''                Neighbor statistics sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Neighbor Identifier
                ''',
                'ip_address',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples', 
                [], [], 
                '''                Sample Table for a BGP neighbor
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Bgp.BgpNeighbors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Bgp.BgpNeighbors',
            False, 
            [
            _MetaInfoClassMember('bgp-neighbor', REFERENCE_LIST, 'BgpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor', 
                [], [], 
                '''                Samples for particular neighbor
                ''',
                'bgp_neighbor',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Bgp',
            False, 
            [
            _MetaInfoClassMember('bgp-neighbors', REFERENCE_CLASS, 'BgpNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Bgp.BgpNeighbors', 
                [], [], 
                '''                Neighbors for which statistics are collected
                ''',
                'bgp_neighbors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast packets received
                ''',
                'in_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast packets received
                ''',
                'in_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes received
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-ucast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast packets received
                ''',
                'in_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-crc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound packets discarded with incorrect CRC
                ''',
                'input_crc',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-frame', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound framing errors
                ''',
                'input_frame',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-overrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input overruns
                ''',
                'input_overrun',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound incorrect packets discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-unknown-proto', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound packets discarded with unknown proto
                ''',
                'input_unknown_proto',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast packets sent
                ''',
                'out_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast packets sent
                ''',
                'out_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes sent
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-ucast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast packets sent
                ''',
                'out_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outbound incorrect packets discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-underrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output underruns
                ''',
                'output_underrun',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples', 
                [], [], 
                '''                Generic Counter samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.GenericCounterInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.GenericCounterInterfaces',
            False, 
            [
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_LIST, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'generic-counter-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes received
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Inbound incorrect packets discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes sent
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Output queue drops
                ''',
                'output_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Outbound incorrect packets discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds from UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample', 
                [], [], 
                '''                Basic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples', 
                [], [], 
                '''                Basic Counter samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.BasicCounterInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.BasicCounterInterfaces',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_LIST, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'basic-counter-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bandwidth (in kbps)
                ''',
                'bandwidth',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-data-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input datarate in 1000's of bps
                ''',
                'input_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packet-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input packets per second
                ''',
                'input_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-peak-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak input packet rate
                ''',
                'input_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-peak-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak input datarate
                ''',
                'input_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-data-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output datarate in 1000's of bps
                ''',
                'output_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packet-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output packets per second
                ''',
                'output_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-peak-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak output packet rate
                ''',
                'output_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-peak-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak output datarate
                ''',
                'output_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample', 
                [], [], 
                '''                Data Rates sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples', 
                [], [], 
                '''                Data Rate samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface.DataRateInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface.DataRateInterfaces',
            False, 
            [
            _MetaInfoClassMember('data-rate-interface', REFERENCE_LIST, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'data-rate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic.Interface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic.Interface',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interfaces', REFERENCE_CLASS, 'BasicCounterInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.BasicCounterInterfaces', 
                [], [], 
                '''                Interfaces for which Basic Counters are
                collected
                ''',
                'basic_counter_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('data-rate-interfaces', REFERENCE_CLASS, 'DataRateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.DataRateInterfaces', 
                [], [], 
                '''                Interfaces for which Data Rates are collected
                ''',
                'data_rate_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('generic-counter-interfaces', REFERENCE_CLASS, 'GenericCounterInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface.GenericCounterInterfaces', 
                [], [], 
                '''                Interfaces for which Generic Counters are
                collected
                ''',
                'generic_counter_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Periodic' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Periodic',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Bgp', 
                [], [], 
                '''                Collected BGP data
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Interface', 
                [], [], 
                '''                Collected Interface data
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Mpls', 
                [], [], 
                '''                Collected MPLS data
                ''',
                'mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Nodes', 
                [], [], 
                '''                Nodes for which data is collected
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic.Ospf', 
                [], [], 
                '''                Collected OSPF data
                ''',
                'ospf',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'periodic',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('checksum-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with checksum errors
                ''',
                'checksum_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples', 
                [], [], 
                '''                Sample Table for an OSPV v2 instance
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv2-protocol-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-instance', REFERENCE_LIST, 'Ospfv2ProtocolInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance', 
                [], [], 
                '''                Protocol samples for a particular OSPF v2
                instance
                ''',
                'ospfv2_protocol_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv2-protocol-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('input-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-db-ds-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-hello-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-ls-requests-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples', 
                [], [], 
                '''                Sample Table for an OSPV v3 instance
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv3-protocol-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances',
            False, 
            [
            _MetaInfoClassMember('ospfv3-protocol-instance', REFERENCE_LIST, 'Ospfv3ProtocolInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance', 
                [], [], 
                '''                Protocol samples for a particular OSPF v3
                instance
                ''',
                'ospfv3_protocol_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospfv3-protocol-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Ospf' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-instances', REFERENCE_CLASS, 'Ospfv2ProtocolInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances', 
                [], [], 
                '''                OSPF v2 instances for which protocol statistics
                are collected
                ''',
                'ospfv2_protocol_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('ospfv3-protocol-instances', REFERENCE_CLASS, 'Ospfv3ProtocolInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances', 
                [], [], 
                '''                OSPF v3 instances for which protocol statistics
                are collected
                ''',
                'ospfv3_protocol_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('address-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address messages received
                ''',
                'address_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address messages sent
                ''',
                'address_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-withdraw-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address withdraw messages received
                ''',
                'address_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('address-withdraw-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Address withdraw messages sent
                ''',
                'address_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('init-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tnit messages received
                ''',
                'init_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('init-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Init messages sent
                ''',
                'init_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('keepalive-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive messages received
                ''',
                'keepalive_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('keepalive-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive messages sent
                ''',
                'keepalive_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-mapping-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label mapping messages received
                ''',
                'label_mapping_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-mapping-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label mapping messages sent
                ''',
                'label_mapping_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-release-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label release messages received
                ''',
                'label_release_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-release-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label release messages sent
                ''',
                'label_release_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-withdraw-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label withdraw messages received
                ''',
                'label_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('label-withdraw-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Label withdraw messages sent
                ''',
                'label_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('notification-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Notification messages received
                ''',
                'notification_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('notification-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Notification messages sent
                ''',
                'notification_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('total-msgs-rcvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total messages received
                ''',
                'total_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('total-msgs-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total messages sent
                ''',
                'total_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample', 
                [], [], 
                '''                LDP neighbor statistics sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor',
            False, 
            [
            _MetaInfoClassMember('nbr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor Address
                ''',
                'nbr',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples', 
                [], [], 
                '''                Samples for a particular LDP neighbor
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ldp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Mpls.LdpNeighbors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Mpls.LdpNeighbors',
            False, 
            [
            _MetaInfoClassMember('ldp-neighbor', REFERENCE_LIST, 'LdpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor', 
                [], [], 
                '''                Samples for a particular LDP neighbor
                ''',
                'ldp_neighbor',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'ldp-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Mpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Mpls',
            False, 
            [
            _MetaInfoClassMember('ldp-neighbors', REFERENCE_CLASS, 'LdpNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Mpls.LdpNeighbors', 
                [], [], 
                '''                LDP neighbors for which statistics are
                collected
                ''',
                'ldp_neighbors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('average-cpu-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average system %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('no-processes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of processes in the system
                ''',
                'no_processes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.SampleXr' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.SampleXr',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample', 
                [], [], 
                '''                Node CPU data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('average-cpu-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('no-threads', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of threads
                ''',
                'no_threads',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('peak-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max. dynamic memory (KBytes) used since startup
                time
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample', 
                [], [], 
                '''                Process data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Processes.Process' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Processes.Process',
            False, 
            [
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Process ID
                ''',
                'process_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples', 
                [], [], 
                '''                Process data
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Processes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Processes',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Processes.Process', 
                [], [], 
                '''                Process data
                ''',
                'process',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'processes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('curr-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current application memory (Bytes) in use
                ''',
                'curr_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('peak-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max. system memory (MBytes) used since bootup
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Samples.Sample', 
                [], [], 
                '''                Node Memory data sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Processes', 
                [], [], 
                '''                Processes data
                ''',
                'processes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('sample-xr', REFERENCE_CLASS, 'SampleXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.SampleXr', 
                [], [], 
                '''                Node CPU data
                ''',
                'sample_xr',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node.Samples', 
                [], [], 
                '''                Node Memory data
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes.Node', 
                [], [], 
                '''                Node Instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('conn-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times connection was dropped
                ''',
                'conn_dropped',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('conn-established', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times the connection was established
                ''',
                'conn_established',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('errors-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of error notifications received on the
                connection
                ''',
                'errors_received',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('errors-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of error notifications sent on the
                connection
                ''',
                'errors_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages received
                ''',
                'input_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of update messages received
                ''',
                'input_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent
                ''',
                'output_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of update messages sent
                ''',
                'output_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample', 
                [], [], 
                '''                Neighbor statistics sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Neighbor Identifier
                ''',
                'ip_address',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples', 
                [], [], 
                '''                Sample Table for a BGP neighbor
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Bgp.BgpNeighbors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Bgp.BgpNeighbors',
            False, 
            [
            _MetaInfoClassMember('bgp-neighbor', REFERENCE_LIST, 'BgpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor', 
                [], [], 
                '''                Samples for particular neighbor
                ''',
                'bgp_neighbor',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Bgp',
            False, 
            [
            _MetaInfoClassMember('bgp-neighbors', REFERENCE_CLASS, 'BgpNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Bgp.BgpNeighbors', 
                [], [], 
                '''                Neighbors for which statistics are collected
                ''',
                'bgp_neighbors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast packets received
                ''',
                'in_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast packets received
                ''',
                'in_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes received
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-ucast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast packets received
                ''',
                'in_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-crc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound packets discarded with incorrect CRC
                ''',
                'input_crc',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-frame', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound framing errors
                ''',
                'input_frame',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-overrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input overruns
                ''',
                'input_overrun',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound incorrect packets discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-unknown-proto', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound packets discarded with unknown proto
                ''',
                'input_unknown_proto',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast packets sent
                ''',
                'out_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast packets sent
                ''',
                'out_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes sent
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-ucast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast packets sent
                ''',
                'out_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outbound incorrect packets discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-underrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output underruns
                ''',
                'output_underrun',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample', 
                [], [], 
                '''                Generic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples', 
                [], [], 
                '''                Generic Counter samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.GenericCounterInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.GenericCounterInterfaces',
            False, 
            [
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_LIST, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'generic-counter-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes received
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets received
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Inbound incorrect packets discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes sent
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-queue-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Output queue drops
                ''',
                'output_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-total-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Outbound incorrect packets discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds from UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample', 
                [], [], 
                '''                Basic Counters sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples', 
                [], [], 
                '''                Basic Counter samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.BasicCounterInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.BasicCounterInterfaces',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_LIST, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'basic-counter-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample',
            False, 
            [
            _MetaInfoClassMember('sample-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Sample ID
                ''',
                'sample_id',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bandwidth (in kbps)
                ''',
                'bandwidth',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-data-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input datarate in 1000's of bps
                ''',
                'input_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-packet-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input packets per second
                ''',
                'input_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-peak-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak input packet rate
                ''',
                'input_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('input-peak-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak input datarate
                ''',
                'input_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-data-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output datarate in 1000's of bps
                ''',
                'output_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-packet-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output packets per second
                ''',
                'output_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-peak-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak output packet rate
                ''',
                'output_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('output-peak-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak output datarate
                ''',
                'output_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of sample in seconds drom UCT
                ''',
                'time_stamp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'sample',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples',
            False, 
            [
            _MetaInfoClassMember('sample', REFERENCE_LIST, 'Sample' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample', 
                [], [], 
                '''                Data Rates sample
                ''',
                'sample',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'samples',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', True),
            _MetaInfoClassMember('samples', REFERENCE_CLASS, 'Samples' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples', 
                [], [], 
                '''                Data Rate samples for an interface
                ''',
                'samples',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface.DataRateInterfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface.DataRateInterfaces',
            False, 
            [
            _MetaInfoClassMember('data-rate-interface', REFERENCE_LIST, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface', 
                [], [], 
                '''                Samples for a particular interface
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'data-rate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor.Interface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor.Interface',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interfaces', REFERENCE_CLASS, 'BasicCounterInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.BasicCounterInterfaces', 
                [], [], 
                '''                Interfaces for which Basic Counters are
                collected
                ''',
                'basic_counter_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('data-rate-interfaces', REFERENCE_CLASS, 'DataRateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.DataRateInterfaces', 
                [], [], 
                '''                Interfaces for which Data Rates are collected
                ''',
                'data_rate_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('generic-counter-interfaces', REFERENCE_CLASS, 'GenericCounterInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface.GenericCounterInterfaces', 
                [], [], 
                '''                Interfaces for which Generic Counters are
                collected
                ''',
                'generic_counter_interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt.Monitor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Monitor',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Bgp', 
                [], [], 
                '''                Collected BGP data
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Interface', 
                [], [], 
                '''                Collected Interface data
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Mpls', 
                [], [], 
                '''                Collected MPLS data
                ''',
                'mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Nodes', 
                [], [], 
                '''                Nodes for which data is collected
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor.Ospf', 
                [], [], 
                '''                Collected OSPF data
                ''',
                'ospf',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'monitor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
    'PerfMgmt' : {
        'meta_info' : _MetaInfoClass('PerfMgmt',
            False, 
            [
            _MetaInfoClassMember('monitor', REFERENCE_CLASS, 'Monitor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Monitor', 
                [], [], 
                '''                Data from monitor (one history period) requests
                ''',
                'monitor',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            _MetaInfoClassMember('periodic', REFERENCE_CLASS, 'Periodic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper', 'PerfMgmt.Periodic', 
                [], [], 
                '''                Data from periodic requests
                ''',
                'periodic',
                'Cisco-IOS-XR-manageability-perfmgmt-oper', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-oper',
            'perf-mgmt',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper'
        ),
    },
}
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Ospf']['meta_info']
_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor']['meta_info']
_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors']['meta_info']
_meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Mpls']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node.SampleXr']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.SampleXr']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Processes']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Nodes']['meta_info']
_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor']['meta_info']
_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors']['meta_info']
_meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Bgp']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Periodic.Interface']['meta_info']
_meta_table['PerfMgmt.Periodic.Ospf']['meta_info'].parent =_meta_table['PerfMgmt.Periodic']['meta_info']
_meta_table['PerfMgmt.Periodic.Mpls']['meta_info'].parent =_meta_table['PerfMgmt.Periodic']['meta_info']
_meta_table['PerfMgmt.Periodic.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Periodic']['meta_info']
_meta_table['PerfMgmt.Periodic.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Periodic']['meta_info']
_meta_table['PerfMgmt.Periodic.Interface']['meta_info'].parent =_meta_table['PerfMgmt.Periodic']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Ospf']['meta_info']
_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor']['meta_info']
_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors']['meta_info']
_meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Mpls']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node.SampleXr']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.SampleXr']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Processes']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes.Node']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Nodes']['meta_info']
_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor']['meta_info']
_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors']['meta_info']
_meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Bgp']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces']['meta_info'].parent =_meta_table['PerfMgmt.Monitor.Interface']['meta_info']
_meta_table['PerfMgmt.Monitor.Ospf']['meta_info'].parent =_meta_table['PerfMgmt.Monitor']['meta_info']
_meta_table['PerfMgmt.Monitor.Mpls']['meta_info'].parent =_meta_table['PerfMgmt.Monitor']['meta_info']
_meta_table['PerfMgmt.Monitor.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Monitor']['meta_info']
_meta_table['PerfMgmt.Monitor.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Monitor']['meta_info']
_meta_table['PerfMgmt.Monitor.Interface']['meta_info'].parent =_meta_table['PerfMgmt.Monitor']['meta_info']
_meta_table['PerfMgmt.Periodic']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
_meta_table['PerfMgmt.Monitor']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']

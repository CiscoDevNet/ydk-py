


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Cisco2505RptrGroup_Identity' : {
        'meta_info' : _MetaInfoClass('Cisco2505RptrGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2505RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Cisco2507RptrGroup_Identity' : {
        'meta_info' : _MetaInfoClass('Cisco2507RptrGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2507RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Cisco2516RptrGroup_Identity' : {
        'meta_info' : _MetaInfoClass('Cisco2516RptrGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2516RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoAdmin_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoAdmin_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoAdmin',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoAgentCapability_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoAgentCapability_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoAgentCapability',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoCIB_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoCIB_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCIB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoChipSetSaint1_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoChipSetSaint1_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint1',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoChipSetSaint2_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoChipSetSaint2_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint2',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoChipSetSaint3_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoChipSetSaint3_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint3',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoChipSetSaint4_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoChipSetSaint4_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoChipSets_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoChipSets_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSets',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoCibMmiGroup_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoCibMmiGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCibMmiGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoCibProvGroup_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoCibProvGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCibProvGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoConfig_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoConfig_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoConfig',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoDomains_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoDomains_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoDomains',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoExperiment_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoExperiment_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoExperiment',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoMgmt_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoMgmt_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoMgmt',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoModules_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoModules_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoModules',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPIB_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPIB_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPIB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPKI_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPKI_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPKI',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPartnerProducts_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPartnerProducts_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPartnerProducts',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPibToMib_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPibToMib_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPibToMib',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPolicyAuto_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPolicyAuto_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPolicyAuto',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoPolicy_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoPolicy_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPolicy',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoProducts_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoProducts_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoProducts',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoProxy_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoProxy_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoProxy',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoRptrGroupObjectID_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoRptrGroupObjectID_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoRptrGroupObjectID',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoSB_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoSB_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoSB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoSMB_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoSMB_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoSMB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainClns_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainClns_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainClns',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainCons_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainCons_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainCons',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainDdp_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainDdp_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainDdp',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainIpx_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainIpx_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainIpx',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainLocal_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainLocal_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainLocal',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainSctpIpv4_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainSctpIpv4_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainSctpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainSctpIpv6_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainSctpIpv6_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainSctpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainTcpIpv4_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainTcpIpv4_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainTcpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainTcpIpv6_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainTcpIpv6_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainTcpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainUdpIpv4_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainUdpIpv4_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainUdpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoTDomainUdpIpv6_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoTDomainUdpIpv6_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainUdpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoUnknownRptrGroup_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoUnknownRptrGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoUnknownRptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'CiscoWsx5020RptrGroup_Identity' : {
        'meta_info' : _MetaInfoClass('CiscoWsx5020RptrGroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoWsx5020RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Ciscoworks_Identity' : {
        'meta_info' : _MetaInfoClass('Ciscoworks_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoworks',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Lightstream_Identity' : {
        'meta_info' : _MetaInfoClass('Lightstream_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'lightstream',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Local_Identity' : {
        'meta_info' : _MetaInfoClass('Local_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'local',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Newport_Identity' : {
        'meta_info' : _MetaInfoClass('Newport_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'newport',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'OtherEnterprises_Identity' : {
        'meta_info' : _MetaInfoClass('OtherEnterprises_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'otherEnterprises',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Pakmon_Identity' : {
        'meta_info' : _MetaInfoClass('Pakmon_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'pakmon',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Temporary_Identity' : {
        'meta_info' : _MetaInfoClass('Temporary_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'temporary',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
    'Workgroup_Identity' : {
        'meta_info' : _MetaInfoClass('Workgroup_Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'workgroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.smi.CISCO_SMI'
        ),
    },
}

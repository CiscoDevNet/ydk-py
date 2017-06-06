


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscocibmmigroupIdentity' : {
        'meta_info' : _MetaInfoClass('CiscocibmmigroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCibMmiGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoconfigIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoconfigIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoConfig',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'TemporaryIdentity' : {
        'meta_info' : _MetaInfoClass('TemporaryIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'temporary',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoproductsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoproductsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoProducts',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomaintcpipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomaintcpipv6Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainTcpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscotdomainddpIdentity' : {
        'meta_info' : _MetaInfoClass('CiscotdomainddpIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainDdp',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscochipsetsaint4Identity' : {
        'meta_info' : _MetaInfoClass('Ciscochipsetsaint4Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomainsctpipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomainsctpipv6Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainSctpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscomodulesIdentity' : {
        'meta_info' : _MetaInfoClass('CiscomodulesIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoModules',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopartnerproductsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopartnerproductsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPartnerProducts',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscomgmtIdentity' : {
        'meta_info' : _MetaInfoClass('CiscomgmtIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoMgmt',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'LightstreamIdentity' : {
        'meta_info' : _MetaInfoClass('LightstreamIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'lightstream',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopkiIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopkiIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPKI',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscochipsetsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscochipsetsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSets',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscounknownrptrgroupIdentity' : {
        'meta_info' : _MetaInfoClass('CiscounknownrptrgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoUnknownRptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoworksIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoworksIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoworks',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoexperimentIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoexperimentIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoExperiment',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'NewportIdentity' : {
        'meta_info' : _MetaInfoClass('NewportIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'newport',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Cisco2516RptrgroupIdentity' : {
        'meta_info' : _MetaInfoClass('Cisco2516RptrgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2516RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomainudpipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomainudpipv6Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainUdpIpv6',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'OtherenterprisesIdentity' : {
        'meta_info' : _MetaInfoClass('OtherenterprisesIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'otherEnterprises',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopibIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopibIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPIB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscotdomainlocalIdentity' : {
        'meta_info' : _MetaInfoClass('CiscotdomainlocalIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainLocal',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'LocalIdentity' : {
        'meta_info' : _MetaInfoClass('LocalIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'local',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Cisco2507RptrgroupIdentity' : {
        'meta_info' : _MetaInfoClass('Cisco2507RptrgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2507RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscotdomainclnsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscotdomainclnsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainClns',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscochipsetsaint2Identity' : {
        'meta_info' : _MetaInfoClass('Ciscochipsetsaint2Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint2',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomainsctpipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomainsctpipv4Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainSctpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscosmbIdentity' : {
        'meta_info' : _MetaInfoClass('CiscosmbIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoSMB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscosbIdentity' : {
        'meta_info' : _MetaInfoClass('CiscosbIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoSB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'PakmonIdentity' : {
        'meta_info' : _MetaInfoClass('PakmonIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'pakmon',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoagentcapabilityIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoagentcapabilityIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoAgentCapability',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Cisco2505RptrgroupIdentity' : {
        'meta_info' : _MetaInfoClass('Cisco2505RptrgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'cisco2505RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopolicyIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopolicyIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPolicy',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopibtomibIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopibtomibIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPibToMib',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscorptrgroupobjectidIdentity' : {
        'meta_info' : _MetaInfoClass('CiscorptrgroupobjectidIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoRptrGroupObjectID',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscocibprovgroupIdentity' : {
        'meta_info' : _MetaInfoClass('CiscocibprovgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCibProvGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscowsx5020RptrgroupIdentity' : {
        'meta_info' : _MetaInfoClass('Ciscowsx5020RptrgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoWsx5020RptrGroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoproxyIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoproxyIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoProxy',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscodomainsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscodomainsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoDomains',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscoadminIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoadminIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoAdmin',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscochipsetsaint3Identity' : {
        'meta_info' : _MetaInfoClass('Ciscochipsetsaint3Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint3',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscotdomainipxIdentity' : {
        'meta_info' : _MetaInfoClass('CiscotdomainipxIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainIpx',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscocibIdentity' : {
        'meta_info' : _MetaInfoClass('CiscocibIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoCIB',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'WorkgroupIdentity' : {
        'meta_info' : _MetaInfoClass('WorkgroupIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'workgroup',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomaintcpipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomaintcpipv4Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainTcpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscotdomainudpipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ciscotdomainudpipv4Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainUdpIpv4',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'Ciscochipsetsaint1Identity' : {
        'meta_info' : _MetaInfoClass('Ciscochipsetsaint1Identity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoChipSetSaint1',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscopolicyautoIdentity' : {
        'meta_info' : _MetaInfoClass('CiscopolicyautoIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoPolicyAuto',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
    'CiscotdomainconsIdentity' : {
        'meta_info' : _MetaInfoClass('CiscotdomainconsIdentity',
            False, 
            [
            ],
            'CISCO-SMI',
            'ciscoTDomainCons',
            _yang_ns._namespaces['CISCO-SMI'],
        'ydk.models.cisco_ios_xe.CISCO_SMI'
        ),
    },
}

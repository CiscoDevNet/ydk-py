


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IanaInterfaceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IanaInterfaceTypeIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iana-interface-type',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'H323ProxyIdentity' : {
        'meta_info' : _MetaInfoClass('H323ProxyIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Proxy',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SipsigIdentity' : {
        'meta_info' : _MetaInfoClass('SipsigIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sipSig',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropdocswirelessmaclayerIdentity' : {
        'meta_info' : _MetaInfoClass('PropdocswirelessmaclayerIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VirtualtgIdentity' : {
        'meta_info' : _MetaInfoClass('VirtualtgIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MplsIdentity' : {
        'meta_info' : _MetaInfoClass('MplsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mpls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'StarlanIdentity' : {
        'meta_info' : _MetaInfoClass('StarlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'starLan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DigitalwrapperoverheadchannelIdentity' : {
        'meta_info' : _MetaInfoClass('DigitalwrapperoverheadchannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalWrapperOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Rs232Identity' : {
        'meta_info' : _MetaInfoClass('Rs232Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rs232',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Capwapdot11ProfileIdentity' : {
        'meta_info' : _MetaInfoClass('Capwapdot11ProfileIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Profile',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SmdsicipIdentity' : {
        'meta_info' : _MetaInfoClass('SmdsicipIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsIcip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ddnx25Identity' : {
        'meta_info' : _MetaInfoClass('Ddnx25Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ddnX25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Proteon80MbitIdentity' : {
        'meta_info' : _MetaInfoClass('Proteon80MbitIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon80Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmlogicalIdentity' : {
        'meta_info' : _MetaInfoClass('AtmlogicalIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmLogical',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropcnlsIdentity' : {
        'meta_info' : _MetaInfoClass('PropcnlsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propCnls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbrccdownstreamIdentity' : {
        'meta_info' : _MetaInfoClass('DvbrccdownstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ds0BundleIdentity' : {
        'meta_info' : _MetaInfoClass('Ds0BundleIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0Bundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmbondIdentity' : {
        'meta_info' : _MetaInfoClass('AtmbondIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmbond',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbrccmaclayerIdentity' : {
        'meta_info' : _MetaInfoClass('DvbrccmaclayerIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Pon155Identity' : {
        'meta_info' : _MetaInfoClass('Pon155Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon155',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DlswIdentity' : {
        'meta_info' : _MetaInfoClass('DlswIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dlsw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Regular1822Identity' : {
        'meta_info' : _MetaInfoClass('Regular1822Identity',
            False, 
            [
            ],
            'iana-if-type',
            'regular1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'TransphdlcIdentity' : {
        'meta_info' : _MetaInfoClass('TransphdlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'transpHdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HostpadIdentity' : {
        'meta_info' : _MetaInfoClass('HostpadIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hostPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbrcsmaclayerIdentity' : {
        'meta_info' : _MetaInfoClass('DvbrcsmaclayerIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DcnIdentity' : {
        'meta_info' : _MetaInfoClass('DcnIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dcn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee80212Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80212Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80212',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SipIdentity' : {
        'meta_info' : _MetaInfoClass('SipIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbrcstdmaIdentity' : {
        'meta_info' : _MetaInfoClass('DvbrcstdmaIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsTdma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'QllcIdentity' : {
        'meta_info' : _MetaInfoClass('QllcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'qllc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'X25PleIdentity' : {
        'meta_info' : _MetaInfoClass('X25PleIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'x25ple',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PipIdentity' : {
        'meta_info' : _MetaInfoClass('PipIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'pip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Rfc877X25Identity' : {
        'meta_info' : _MetaInfoClass('Rfc877X25Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc877x25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88026ManIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88026ManIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88026Man',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'TdlcIdentity' : {
        'meta_info' : _MetaInfoClass('TdlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'tdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OpticalchannelgroupIdentity' : {
        'meta_info' : _MetaInfoClass('OpticalchannelgroupIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannelGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FrforwardIdentity' : {
        'meta_info' : _MetaInfoClass('FrforwardIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IsupIdentity' : {
        'meta_info' : _MetaInfoClass('IsupIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'isup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SonetpathIdentity' : {
        'meta_info' : _MetaInfoClass('SonetpathIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetPath',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ModemIdentity' : {
        'meta_info' : _MetaInfoClass('ModemIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'modem',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PrimaryisdnIdentity' : {
        'meta_info' : _MetaInfoClass('PrimaryisdnIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'primaryISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropatmIdentity' : {
        'meta_info' : _MetaInfoClass('PropatmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscablemaclayerIdentity' : {
        'meta_info' : _MetaInfoClass('DocscablemaclayerIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'X25MlpIdentity' : {
        'meta_info' : _MetaInfoClass('X25MlpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'x25mlp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IsdnIdentity' : {
        'meta_info' : _MetaInfoClass('IsdnIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'isdn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'TermpadIdentity' : {
        'meta_info' : _MetaInfoClass('TermpadIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'termPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AviciopticaletherIdentity' : {
        'meta_info' : _MetaInfoClass('AviciopticaletherIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aviciOpticalEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LapdIdentity' : {
        'meta_info' : _MetaInfoClass('LapdIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'lapd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CnrIdentity' : {
        'meta_info' : _MetaInfoClass('CnrIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'cnr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ChannelIdentity' : {
        'meta_info' : _MetaInfoClass('ChannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'channel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpoveratmIdentity' : {
        'meta_info' : _MetaInfoClass('IpoveratmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'NsipIdentity' : {
        'meta_info' : _MetaInfoClass('NsipIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'nsip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Miox25Identity' : {
        'meta_info' : _MetaInfoClass('Miox25Identity',
            False, 
            [
            ],
            'iana-if-type',
            'miox25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LapfIdentity' : {
        'meta_info' : _MetaInfoClass('LapfIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'lapf',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Aflane8023Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8023Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8023',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MediamailoveripIdentity' : {
        'meta_info' : _MetaInfoClass('MediamailoveripIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mediaMailOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'X213Identity' : {
        'meta_info' : _MetaInfoClass('X213Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x213',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'EplrsIdentity' : {
        'meta_info' : _MetaInfoClass('EplrsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'eplrs',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Gr303RdtIdentity' : {
        'meta_info' : _MetaInfoClass('Gr303RdtIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303RDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HdlcIdentity' : {
        'meta_info' : _MetaInfoClass('HdlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoicefgdeanaIdentity' : {
        'meta_info' : _MetaInfoClass('VoicefgdeanaIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDEANA',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CiscoislvlanIdentity' : {
        'meta_info' : _MetaInfoClass('CiscoislvlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ciscoISLvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PppIdentity' : {
        'meta_info' : _MetaInfoClass('PppIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ppp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceoveratmIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceoveratmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Gr303IdtIdentity' : {
        'meta_info' : _MetaInfoClass('Gr303IdtIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303IDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SoftwareloopbackIdentity' : {
        'meta_info' : _MetaInfoClass('SoftwareloopbackIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'softwareLoopback',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ds1Identity' : {
        'meta_info' : _MetaInfoClass('Ds1Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Pon622Identity' : {
        'meta_info' : _MetaInfoClass('Pon622Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon622',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropmultiplexorIdentity' : {
        'meta_info' : _MetaInfoClass('PropmultiplexorIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propMultiplexor',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpoverclawIdentity' : {
        'meta_info' : _MetaInfoClass('IpoverclawIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverClaw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ss7SiglinkIdentity' : {
        'meta_info' : _MetaInfoClass('Ss7SiglinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ss7SigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CctemulIdentity' : {
        'meta_info' : _MetaInfoClass('CctemulIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'cctEmul',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FastIdentity' : {
        'meta_info' : _MetaInfoClass('FastIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fast',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbtdmIdentity' : {
        'meta_info' : _MetaInfoClass('DvbtdmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbTdm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'V36Identity' : {
        'meta_info' : _MetaInfoClass('V36Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v36',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'G9983Identity' : {
        'meta_info' : _MetaInfoClass('G9983Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9983',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MpcIdentity' : {
        'meta_info' : _MetaInfoClass('MpcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mpc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'QamIdentity' : {
        'meta_info' : _MetaInfoClass('QamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'qam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ethernet3MbitIdentity' : {
        'meta_info' : _MetaInfoClass('Ethernet3MbitIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernet3Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'G703At64KIdentity' : {
        'meta_info' : _MetaInfoClass('G703At64KIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at64k',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ImtIdentity' : {
        'meta_info' : _MetaInfoClass('ImtIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'imt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OtnoduIdentity' : {
        'meta_info' : _MetaInfoClass('OtnoduIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOdu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmIdentity' : {
        'meta_info' : _MetaInfoClass('AtmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ArapIdentity' : {
        'meta_info' : _MetaInfoClass('ArapIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'arap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FciplinkIdentity' : {
        'meta_info' : _MetaInfoClass('FciplinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fcipLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee8023AdlagIdentity' : {
        'meta_info' : _MetaInfoClass('Ieee8023AdlagIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee8023adLag',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'InfinibandIdentity' : {
        'meta_info' : _MetaInfoClass('InfinibandIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'infiniband',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmvciendptIdentity' : {
        'meta_info' : _MetaInfoClass('AtmvciendptIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'X25HuntgroupIdentity' : {
        'meta_info' : _MetaInfoClass('X25HuntgroupIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'x25huntGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ArcnetplusIdentity' : {
        'meta_info' : _MetaInfoClass('ArcnetplusIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnetPlus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee1394Identity' : {
        'meta_info' : _MetaInfoClass('Ieee1394Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee1394',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmvirtualIdentity' : {
        'meta_info' : _MetaInfoClass('AtmvirtualIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Vdsl2Identity' : {
        'meta_info' : _MetaInfoClass('Vdsl2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'RsrbIdentity' : {
        'meta_info' : _MetaInfoClass('RsrbIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'rsrb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Propbwap2MpIdentity' : {
        'meta_info' : _MetaInfoClass('Propbwap2MpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propBWAp2Mp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Tr008Identity' : {
        'meta_info' : _MetaInfoClass('Tr008Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tr008',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SonetvtIdentity' : {
        'meta_info' : _MetaInfoClass('SonetvtIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetVT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'L2VlanIdentity' : {
        'meta_info' : _MetaInfoClass('L2VlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'l2vlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MpegtransportIdentity' : {
        'meta_info' : _MetaInfoClass('MpegtransportIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mpegTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Pdnetherloop1Identity' : {
        'meta_info' : _MetaInfoClass('Pdnetherloop1Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IlanIdentity' : {
        'meta_info' : _MetaInfoClass('IlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ilan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ds0Identity' : {
        'meta_info' : _MetaInfoClass('Ds0Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ParaIdentity' : {
        'meta_info' : _MetaInfoClass('ParaIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'para',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Hiperlan2Identity' : {
        'meta_info' : _MetaInfoClass('Hiperlan2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hiperlan2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'BscIdentity' : {
        'meta_info' : _MetaInfoClass('BscIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'bsc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88025CrfpintIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88025CrfpintIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025CRFPInt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Adsl2Identity' : {
        'meta_info' : _MetaInfoClass('Adsl2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceoveripIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceoveripIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SonetIdentity' : {
        'meta_info' : _MetaInfoClass('SonetIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sonet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FibrechannelIdentity' : {
        'meta_info' : _MetaInfoClass('FibrechannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fibreChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'G703At2MbIdentity' : {
        'meta_info' : _MetaInfoClass('G703At2MbIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at2mb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Propwirelessp2PIdentity' : {
        'meta_info' : _MetaInfoClass('Propwirelessp2PIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propWirelessP2P',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceebsIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceebsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEBS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee802154Identity' : {
        'meta_info' : _MetaInfoClass('Ieee802154Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee802154',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'BitsIdentity' : {
        'meta_info' : _MetaInfoClass('BitsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'bits',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CabledownstreamrfportIdentity' : {
        'meta_info' : _MetaInfoClass('CabledownstreamrfportIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'cableDownstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AlugponphysicaluniIdentity' : {
        'meta_info' : _MetaInfoClass('AlugponphysicaluniIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VdslIdentity' : {
        'meta_info' : _MetaInfoClass('VdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IfGsnIdentity' : {
        'meta_info' : _MetaInfoClass('IfGsnIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'if-gsn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'L3IpvlanIdentity' : {
        'meta_info' : _MetaInfoClass('L3IpvlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FramerelayIdentity' : {
        'meta_info' : _MetaInfoClass('FramerelayIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HssiIdentity' : {
        'meta_info' : _MetaInfoClass('HssiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hssi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ProppointtopointserialIdentity' : {
        'meta_info' : _MetaInfoClass('ProppointtopointserialIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propPointToPointSerial',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HomepnaIdentity' : {
        'meta_info' : _MetaInfoClass('HomepnaIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'homepna',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscablemcmtsdownstreamIdentity' : {
        'meta_info' : _MetaInfoClass('DocscablemcmtsdownstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMCmtsDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FramerelaympiIdentity' : {
        'meta_info' : _MetaInfoClass('FramerelaympiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayMPI',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HippiIdentity' : {
        'meta_info' : _MetaInfoClass('HippiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hippi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'NfasIdentity' : {
        'meta_info' : _MetaInfoClass('NfasIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'nfas',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OpticalchannelIdentity' : {
        'meta_info' : _MetaInfoClass('OpticalchannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'RadiomacIdentity' : {
        'meta_info' : _MetaInfoClass('RadiomacIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'radioMAC',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AlueponphysicaluniIdentity' : {
        'meta_info' : _MetaInfoClass('AlueponphysicaluniIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'E1Identity' : {
        'meta_info' : _MetaInfoClass('E1Identity',
            False, 
            [
            ],
            'iana-if-type',
            'e1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Proteon10MbitIdentity' : {
        'meta_info' : _MetaInfoClass('Proteon10MbitIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon10Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropdocswirelessdownstreamIdentity' : {
        'meta_info' : _MetaInfoClass('PropdocswirelessdownstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'RprIdentity' : {
        'meta_info' : _MetaInfoClass('RprIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'rpr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LmpIdentity' : {
        'meta_info' : _MetaInfoClass('LmpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'lmp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'TelinkIdentity' : {
        'meta_info' : _MetaInfoClass('TelinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'teLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DigitalpowerlineIdentity' : {
        'meta_info' : _MetaInfoClass('DigitalpowerlineIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalPowerline',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AlueponlogicallinkIdentity' : {
        'meta_info' : _MetaInfoClass('AlueponlogicallinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponLogicalLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'GponIdentity' : {
        'meta_info' : _MetaInfoClass('GponIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MplstunnelIdentity' : {
        'meta_info' : _MetaInfoClass('MplstunnelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mplsTunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoicedidIdentity' : {
        'meta_info' : _MetaInfoClass('VoicedidIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceDID',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OtnotuIdentity' : {
        'meta_info' : _MetaInfoClass('OtnotuIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOtu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoicefxoIdentity' : {
        'meta_info' : _MetaInfoClass('VoicefxoIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXO',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'StacktostackIdentity' : {
        'meta_info' : _MetaInfoClass('StacktostackIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'stackToStack',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88025DtrIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88025DtrIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Dtr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ds3Identity' : {
        'meta_info' : _MetaInfoClass('Ds3Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds3',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FramerelayserviceIdentity' : {
        'meta_info' : _MetaInfoClass('FramerelayserviceIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayService',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropdocswirelessupstreamIdentity' : {
        'meta_info' : _MetaInfoClass('PropdocswirelessupstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpswitchIdentity' : {
        'meta_info' : _MetaInfoClass('IpswitchIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ipSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'BridgeIdentity' : {
        'meta_info' : _MetaInfoClass('BridgeIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'bridge',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FramerelayinterconnectIdentity' : {
        'meta_info' : _MetaInfoClass('FramerelayinterconnectIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayInterconnect',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'EthernetcsmacdIdentity' : {
        'meta_info' : _MetaInfoClass('EthernetcsmacdIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernetCsmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MfsiglinkIdentity' : {
        'meta_info' : _MetaInfoClass('MfsiglinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mfSigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88024TokenbusIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88024TokenbusIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88024TokenBus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MsdslIdentity' : {
        'meta_info' : _MetaInfoClass('MsdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'msdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PppmultilinkbundleIdentity' : {
        'meta_info' : _MetaInfoClass('PppmultilinkbundleIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'pppMultilinkBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'X86LapsIdentity' : {
        'meta_info' : _MetaInfoClass('X86LapsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'x86Laps',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'GfpIdentity' : {
        'meta_info' : _MetaInfoClass('GfpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gfp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'BasicisdnIdentity' : {
        'meta_info' : _MetaInfoClass('BasicisdnIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'basicISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'TunnelIdentity' : {
        'meta_info' : _MetaInfoClass('TunnelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'tunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'V11Identity' : {
        'meta_info' : _MetaInfoClass('V11Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v11',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FastetherIdentity' : {
        'meta_info' : _MetaInfoClass('FastetherIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PropvirtualIdentity' : {
        'meta_info' : _MetaInfoClass('PropvirtualIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'propVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SlipIdentity' : {
        'meta_info' : _MetaInfoClass('SlipIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'slip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'L3IpxvlanIdentity' : {
        'meta_info' : _MetaInfoClass('L3IpxvlanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipxvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CompositelinkIdentity' : {
        'meta_info' : _MetaInfoClass('CompositelinkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'compositeLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ShdslIdentity' : {
        'meta_info' : _MetaInfoClass('ShdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'shdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SrpIdentity' : {
        'meta_info' : _MetaInfoClass('SrpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'srp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Aal5Identity' : {
        'meta_info' : _MetaInfoClass('Aal5Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal5',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SonetoverheadchannelIdentity' : {
        'meta_info' : _MetaInfoClass('SonetoverheadchannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'UsbIdentity' : {
        'meta_info' : _MetaInfoClass('UsbIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'usb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LapbIdentity' : {
        'meta_info' : _MetaInfoClass('LapbIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'lapb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DtmIdentity' : {
        'meta_info' : _MetaInfoClass('DtmIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Pdnetherloop2Identity' : {
        'meta_info' : _MetaInfoClass('Pdnetherloop2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ds1FdlIdentity' : {
        'meta_info' : _MetaInfoClass('Ds1FdlIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1FDL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LinegroupIdentity' : {
        'meta_info' : _MetaInfoClass('LinegroupIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'linegroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'V35Identity' : {
        'meta_info' : _MetaInfoClass('V35Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v35',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscableupstreamIdentity' : {
        'meta_info' : _MetaInfoClass('DocscableupstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Capwapdot11BssIdentity' : {
        'meta_info' : _MetaInfoClass('Capwapdot11BssIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Bss',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'UltraIdentity' : {
        'meta_info' : _MetaInfoClass('UltraIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ultra',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AdslIdentity' : {
        'meta_info' : _MetaInfoClass('AdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ReachdslIdentity' : {
        'meta_info' : _MetaInfoClass('ReachdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'reachDSL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmfuniIdentity' : {
        'meta_info' : _MetaInfoClass('AtmfuniIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmFuni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'G9981Identity' : {
        'meta_info' : _MetaInfoClass('G9981Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9981',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FddiIdentity' : {
        'meta_info' : _MetaInfoClass('FddiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fddi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IfvfitypeIdentity' : {
        'meta_info' : _MetaInfoClass('IfvfitypeIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ifVfiType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'A12MppswitchIdentity' : {
        'meta_info' : _MetaInfoClass('A12MppswitchIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'a12MppSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpovercdlcIdentity' : {
        'meta_info' : _MetaInfoClass('IpovercdlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverCdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Hdsl2Identity' : {
        'meta_info' : _MetaInfoClass('Hdsl2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AsyncIdentity' : {
        'meta_info' : _MetaInfoClass('AsyncIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'async',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SixtofourIdentity' : {
        'meta_info' : _MetaInfoClass('SixtofourIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sixToFour',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'BgppolicyaccountingIdentity' : {
        'meta_info' : _MetaInfoClass('BgppolicyaccountingIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'bgppolicyaccounting',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceemIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceemIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEM',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IfpwtypeIdentity' : {
        'meta_info' : _MetaInfoClass('IfpwtypeIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ifPwType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscableupstreamrfportIdentity' : {
        'meta_info' : _MetaInfoClass('DocscableupstreamrfportIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VirtualipaddressIdentity' : {
        'meta_info' : _MetaInfoClass('VirtualipaddressIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualIpAddress',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VmwarevirtualnicIdentity' : {
        'meta_info' : _MetaInfoClass('VmwarevirtualnicIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareVirtualNic',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88025FiberIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88025FiberIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Fiber',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'RadslIdentity' : {
        'meta_info' : _MetaInfoClass('RadslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'radsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmsubinterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('AtmsubinterfaceIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmSubInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscableupstreamchannelIdentity' : {
        'meta_info' : _MetaInfoClass('DocscableupstreamchannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SmdsdxiIdentity' : {
        'meta_info' : _MetaInfoClass('SmdsdxiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VmwarenicteamIdentity' : {
        'meta_info' : _MetaInfoClass('VmwarenicteamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareNicTeam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoicefgdosIdentity' : {
        'meta_info' : _MetaInfoClass('VoicefgdosIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDOS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'GtpIdentity' : {
        'meta_info' : _MetaInfoClass('GtpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gtp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MacseccontrolledifIdentity' : {
        'meta_info' : _MetaInfoClass('MacseccontrolledifIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecControlledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FrdlciendptIdentity' : {
        'meta_info' : _MetaInfoClass('FrdlciendptIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frDlciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmimaIdentity' : {
        'meta_info' : _MetaInfoClass('AtmimaIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmIma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DocscabledownstreamIdentity' : {
        'meta_info' : _MetaInfoClass('DocscabledownstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ArcnetIdentity' : {
        'meta_info' : _MetaInfoClass('ArcnetIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Frf16MfrbundleIdentity' : {
        'meta_info' : _MetaInfoClass('Frf16MfrbundleIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'frf16MfrBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CoffeeIdentity' : {
        'meta_info' : _MetaInfoClass('CoffeeIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'coffee',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HippiinterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('HippiinterfaceIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hippiInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88025TokenringIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88025TokenringIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025TokenRing',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee80216WmanIdentity' : {
        'meta_info' : _MetaInfoClass('Ieee80216WmanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80216WMAN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'G9982Identity' : {
        'meta_info' : _MetaInfoClass('G9982Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9982',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OpticaltransportIdentity' : {
        'meta_info' : _MetaInfoClass('OpticaltransportIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CesIdentity' : {
        'meta_info' : _MetaInfoClass('CesIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ces',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpforwardIdentity' : {
        'meta_info' : _MetaInfoClass('IpforwardIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ipForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmdxiIdentity' : {
        'meta_info' : _MetaInfoClass('AtmdxiIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IsdnuIdentity' : {
        'meta_info' : _MetaInfoClass('IsdnuIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'isdnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Aflane8025Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8025Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8025',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AlueponIdentity' : {
        'meta_info' : _MetaInfoClass('AlueponIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MacsecuncontrolledifIdentity' : {
        'meta_info' : _MetaInfoClass('MacsecuncontrolledifIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecUncontrolledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Hdh1822Identity' : {
        'meta_info' : _MetaInfoClass('Hdh1822Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdh1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'WwanppIdentity' : {
        'meta_info' : _MetaInfoClass('WwanppIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoicefxsIdentity' : {
        'meta_info' : _MetaInfoClass('VoicefxsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SdlcIdentity' : {
        'meta_info' : _MetaInfoClass('SdlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SdslIdentity' : {
        'meta_info' : _MetaInfoClass('SdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ibm370ParchanIdentity' : {
        'meta_info' : _MetaInfoClass('Ibm370ParchanIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ibm370parChan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AluelpIdentity' : {
        'meta_info' : _MetaInfoClass('AluelpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluELP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CapwapwtpvirtualradioIdentity' : {
        'meta_info' : _MetaInfoClass('CapwapwtpvirtualradioIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapWtpVirtualRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88023CsmacdIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88023CsmacdIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88023Csmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'EsconIdentity' : {
        'meta_info' : _MetaInfoClass('EsconIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'escon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Aal2Identity' : {
        'meta_info' : _MetaInfoClass('Aal2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Adsl2PlusIdentity' : {
        'meta_info' : _MetaInfoClass('Adsl2PlusIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2plus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'HyperchannelIdentity' : {
        'meta_info' : _MetaInfoClass('HyperchannelIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'hyperchannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceencapIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceencapIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEncap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbasiinIdentity' : {
        'meta_info' : _MetaInfoClass('DvbasiinIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiIn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'LocaltalkIdentity' : {
        'meta_info' : _MetaInfoClass('LocaltalkIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'localTalk',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Rfc1483Identity' : {
        'meta_info' : _MetaInfoClass('Rfc1483Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc1483',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceovercableIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceovercableIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverCable',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Ieee80211Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80211Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80211',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceemfgdIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceemfgdIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEMFGD',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Mocaversion1Identity' : {
        'meta_info' : _MetaInfoClass('Mocaversion1Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mocaVersion1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PlcIdentity' : {
        'meta_info' : _MetaInfoClass('PlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'plc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'H323GatekeeperIdentity' : {
        'meta_info' : _MetaInfoClass('H323GatekeeperIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Gatekeeper',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IsdnsIdentity' : {
        'meta_info' : _MetaInfoClass('IsdnsIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'isdns',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Q2931Identity' : {
        'meta_info' : _MetaInfoClass('Q2931Identity',
            False, 
            [
            ],
            'iana-if-type',
            'q2931',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AluepononuIdentity' : {
        'meta_info' : _MetaInfoClass('AluepononuIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'GigabitethernetIdentity' : {
        'meta_info' : _MetaInfoClass('GigabitethernetIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'gigabitEthernet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'FastetherfxIdentity' : {
        'meta_info' : _MetaInfoClass('FastetherfxIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEtherFX',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'EconetIdentity' : {
        'meta_info' : _MetaInfoClass('EconetIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'econet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbrccupstreamIdentity' : {
        'meta_info' : _MetaInfoClass('DvbrccupstreamIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'OtherIdentity' : {
        'meta_info' : _MetaInfoClass('OtherIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'other',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'CblvectastarIdentity' : {
        'meta_info' : _MetaInfoClass('CblvectastarIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'cblVectaStar',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AtmradioIdentity' : {
        'meta_info' : _MetaInfoClass('AtmradioIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'atmRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'ActelismetaloopIdentity' : {
        'meta_info' : _MetaInfoClass('ActelismetaloopIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'actelisMetaLOOP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'V37Identity' : {
        'meta_info' : _MetaInfoClass('V37Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v37',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'InterleaveIdentity' : {
        'meta_info' : _MetaInfoClass('InterleaveIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'interleave',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Wwanpp2Identity' : {
        'meta_info' : _MetaInfoClass('Wwanpp2Identity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'PosIdentity' : {
        'meta_info' : _MetaInfoClass('PosIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'pos',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IdslIdentity' : {
        'meta_info' : _MetaInfoClass('IdslIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'idsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'Iso88022LlcIdentity' : {
        'meta_info' : _MetaInfoClass('Iso88022LlcIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88022llc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'VoiceoverframerelayIdentity' : {
        'meta_info' : _MetaInfoClass('VoiceoverframerelayIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverFrameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'IpIdentity' : {
        'meta_info' : _MetaInfoClass('IpIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'ip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MvlIdentity' : {
        'meta_info' : _MetaInfoClass('MvlIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'mvl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'DvbasioutIdentity' : {
        'meta_info' : _MetaInfoClass('DvbasioutIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiOut',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'SiptgIdentity' : {
        'meta_info' : _MetaInfoClass('SiptgIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'sipTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'MyrinetIdentity' : {
        'meta_info' : _MetaInfoClass('MyrinetIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'myrinet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'EonIdentity' : {
        'meta_info' : _MetaInfoClass('EonIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'eon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
    'AlugpononuIdentity' : {
        'meta_info' : _MetaInfoClass('AlugpononuIdentity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.ietf.iana_if_type'
        ),
    },
}

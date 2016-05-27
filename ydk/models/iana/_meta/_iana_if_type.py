


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IanaInterfaceType_Identity' : {
        'meta_info' : _MetaInfoClass('IanaInterfaceType_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iana-interface-type',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Otnodu_Identity' : {
        'meta_info' : _MetaInfoClass('Otnodu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOdu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ipoverclaw_Identity' : {
        'meta_info' : _MetaInfoClass('Ipoverclaw_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverClaw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Capwapdot11Bss_Identity' : {
        'meta_info' : _MetaInfoClass('Capwapdot11Bss_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Bss',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmsubinterface_Identity' : {
        'meta_info' : _MetaInfoClass('Atmsubinterface_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmSubInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Coffee_Identity' : {
        'meta_info' : _MetaInfoClass('Coffee_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'coffee',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Framerelayservice_Identity' : {
        'meta_info' : _MetaInfoClass('Framerelayservice_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayService',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V36_Identity' : {
        'meta_info' : _MetaInfoClass('V36_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v36',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Radsl_Identity' : {
        'meta_info' : _MetaInfoClass('Radsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'radsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G703At64K_Identity' : {
        'meta_info' : _MetaInfoClass('G703At64K_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at64k',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lmp_Identity' : {
        'meta_info' : _MetaInfoClass('Lmp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lmp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vdsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Vdsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rs232_Identity' : {
        'meta_info' : _MetaInfoClass('Rs232_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rs232',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mediamailoverip_Identity' : {
        'meta_info' : _MetaInfoClass('Mediamailoverip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mediaMailOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Localtalk_Identity' : {
        'meta_info' : _MetaInfoClass('Localtalk_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'localTalk',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'E1_Identity' : {
        'meta_info' : _MetaInfoClass('E1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'e1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Fiber_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Fiber_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Fiber',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Reachdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Reachdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'reachDSL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Softwareloopback_Identity' : {
        'meta_info' : _MetaInfoClass('Softwareloopback_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'softwareLoopback',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pon155_Identity' : {
        'meta_info' : _MetaInfoClass('Pon155_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon155',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceovercable_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceovercable_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverCable',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbrccdownstream_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbrccdownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aflane8023_Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8023_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8023',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80216Wman_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80216Wman_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80216WMAN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Opticaltransport_Identity' : {
        'meta_info' : _MetaInfoClass('Opticaltransport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tr008_Identity' : {
        'meta_info' : _MetaInfoClass('Tr008_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tr008',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'A12Mppswitch_Identity' : {
        'meta_info' : _MetaInfoClass('A12Mppswitch_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'a12MppSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Smdsicip_Identity' : {
        'meta_info' : _MetaInfoClass('Smdsicip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsIcip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceoverip_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceoverip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverIp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Modem_Identity' : {
        'meta_info' : _MetaInfoClass('Modem_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'modem',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapf_Identity' : {
        'meta_info' : _MetaInfoClass('Lapf_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapf',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atm_Identity' : {
        'meta_info' : _MetaInfoClass('Atm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ces_Identity' : {
        'meta_info' : _MetaInfoClass('Ces_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ces',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Otnotu_Identity' : {
        'meta_info' : _MetaInfoClass('Otnotu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'otnOtu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds3_Identity' : {
        'meta_info' : _MetaInfoClass('Ds3_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds3',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ilan_Identity' : {
        'meta_info' : _MetaInfoClass('Ilan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ilan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmradio_Identity' : {
        'meta_info' : _MetaInfoClass('Atmradio_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds0_Identity' : {
        'meta_info' : _MetaInfoClass('Ds0_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25Huntgroup_Identity' : {
        'meta_info' : _MetaInfoClass('X25Huntgroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25huntGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds1_Identity' : {
        'meta_info' : _MetaInfoClass('Ds1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Alueponlogicallink_Identity' : {
        'meta_info' : _MetaInfoClass('Alueponlogicallink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponLogicalLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Srp_Identity' : {
        'meta_info' : _MetaInfoClass('Srp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'srp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sip_Identity' : {
        'meta_info' : _MetaInfoClass('Sip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscabledownstream_Identity' : {
        'meta_info' : _MetaInfoClass('Docscabledownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbrcstdma_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbrcstdma_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsTdma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Framerelayinterconnect_Identity' : {
        'meta_info' : _MetaInfoClass('Framerelayinterconnect_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayInterconnect',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fibrechannel_Identity' : {
        'meta_info' : _MetaInfoClass('Fibrechannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fibreChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9983_Identity' : {
        'meta_info' : _MetaInfoClass('G9983_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9983',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Plc_Identity' : {
        'meta_info' : _MetaInfoClass('Plc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'plc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Nsip_Identity' : {
        'meta_info' : _MetaInfoClass('Nsip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'nsip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Sdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Framerelaympi_Identity' : {
        'meta_info' : _MetaInfoClass('Framerelaympi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelayMPI',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Sdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hyperchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Hyperchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hyperchannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Digitalpowerline_Identity' : {
        'meta_info' : _MetaInfoClass('Digitalpowerline_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalPowerline',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdh1822_Identity' : {
        'meta_info' : _MetaInfoClass('Hdh1822_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdh1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mvl_Identity' : {
        'meta_info' : _MetaInfoClass('Mvl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mvl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mocaversion1_Identity' : {
        'meta_info' : _MetaInfoClass('Mocaversion1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mocaVersion1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ethernetcsmacd_Identity' : {
        'meta_info' : _MetaInfoClass('Ethernetcsmacd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernetCsmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propmultiplexor_Identity' : {
        'meta_info' : _MetaInfoClass('Propmultiplexor_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propMultiplexor',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Arcnetplus_Identity' : {
        'meta_info' : _MetaInfoClass('Arcnetplus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnetPlus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pppmultilinkbundle_Identity' : {
        'meta_info' : _MetaInfoClass('Pppmultilinkbundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pppMultilinkBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Capwapdot11Profile_Identity' : {
        'meta_info' : _MetaInfoClass('Capwapdot11Profile_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapDot11Profile',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voicedid_Identity' : {
        'meta_info' : _MetaInfoClass('Voicedid_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceDID',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Shdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Shdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'shdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceem_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceem_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEM',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Compositelink_Identity' : {
        'meta_info' : _MetaInfoClass('Compositelink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'compositeLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propatm_Identity' : {
        'meta_info' : _MetaInfoClass('Propatm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rsrb_Identity' : {
        'meta_info' : _MetaInfoClass('Rsrb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rsrb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Crfpint_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Crfpint_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025CRFPInt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Proteon10Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Proteon10Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon10Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Econet_Identity' : {
        'meta_info' : _MetaInfoClass('Econet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'econet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ifvfitype_Identity' : {
        'meta_info' : _MetaInfoClass('Ifvfitype_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ifVfiType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Interleave_Identity' : {
        'meta_info' : _MetaInfoClass('Interleave_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'interleave',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmbond_Identity' : {
        'meta_info' : _MetaInfoClass('Atmbond_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmbond',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V35_Identity' : {
        'meta_info' : _MetaInfoClass('V35_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v35',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Frf16Mfrbundle_Identity' : {
        'meta_info' : _MetaInfoClass('Frf16Mfrbundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frf16MfrBundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X86Laps_Identity' : {
        'meta_info' : _MetaInfoClass('X86Laps_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x86Laps',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Other_Identity' : {
        'meta_info' : _MetaInfoClass('Other_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'other',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Cctemul_Identity' : {
        'meta_info' : _MetaInfoClass('Cctemul_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cctEmul',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'IfGsn_Identity' : {
        'meta_info' : _MetaInfoClass('IfGsn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'if-gsn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mplstunnel_Identity' : {
        'meta_info' : _MetaInfoClass('Mplstunnel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mplsTunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voicefgdeana_Identity' : {
        'meta_info' : _MetaInfoClass('Voicefgdeana_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDEANA',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gpon_Identity' : {
        'meta_info' : _MetaInfoClass('Gpon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isup_Identity' : {
        'meta_info' : _MetaInfoClass('Isup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Vdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pos_Identity' : {
        'meta_info' : _MetaInfoClass('Pos_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pos',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9982_Identity' : {
        'meta_info' : _MetaInfoClass('G9982_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9982',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee8023Adlag_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee8023Adlag_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee8023adLag',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bridge_Identity' : {
        'meta_info' : _MetaInfoClass('Bridge_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bridge',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gtp_Identity' : {
        'meta_info' : _MetaInfoClass('Gtp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gtp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscablemaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('Docscablemaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Opticalchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Opticalchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdnu_Identity' : {
        'meta_info' : _MetaInfoClass('Isdnu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aflane8025_Identity' : {
        'meta_info' : _MetaInfoClass('Aflane8025_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aflane8025',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscablemcmtsdownstream_Identity' : {
        'meta_info' : _MetaInfoClass('Docscablemcmtsdownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableMCmtsDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pdnetherloop1_Identity' : {
        'meta_info' : _MetaInfoClass('Pdnetherloop1_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop1',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aviciopticalether_Identity' : {
        'meta_info' : _MetaInfoClass('Aviciopticalether_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aviciOpticalEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Framerelay_Identity' : {
        'meta_info' : _MetaInfoClass('Framerelay_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88022Llc_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88022Llc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88022llc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ppp_Identity' : {
        'meta_info' : _MetaInfoClass('Ppp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ppp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Cabledownstreamrfport_Identity' : {
        'meta_info' : _MetaInfoClass('Cabledownstreamrfport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cableDownstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Eplrs_Identity' : {
        'meta_info' : _MetaInfoClass('Eplrs_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'eplrs',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pip_Identity' : {
        'meta_info' : _MetaInfoClass('Pip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vmwarenicteam_Identity' : {
        'meta_info' : _MetaInfoClass('Vmwarenicteam_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareNicTeam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapd_Identity' : {
        'meta_info' : _MetaInfoClass('Lapd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Lapb_Identity' : {
        'meta_info' : _MetaInfoClass('Lapb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'lapb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voicefxo_Identity' : {
        'meta_info' : _MetaInfoClass('Voicefxo_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXO',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Channel_Identity' : {
        'meta_info' : _MetaInfoClass('Channel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'channel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Frforward_Identity' : {
        'meta_info' : _MetaInfoClass('Frforward_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80211_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80211_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80211',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Transphdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Transphdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'transpHdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X213_Identity' : {
        'meta_info' : _MetaInfoClass('X213_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x213',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Macsecuncontrolledif_Identity' : {
        'meta_info' : _MetaInfoClass('Macsecuncontrolledif_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecUncontrolledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Virtualipaddress_Identity' : {
        'meta_info' : _MetaInfoClass('Virtualipaddress_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualIpAddress',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88023Csmacd_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88023Csmacd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88023Csmacd',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aluepon_Identity' : {
        'meta_info' : _MetaInfoClass('Aluepon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEpon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Usb_Identity' : {
        'meta_info' : _MetaInfoClass('Usb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'usb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmfuni_Identity' : {
        'meta_info' : _MetaInfoClass('Atmfuni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmFuni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gr303Rdt_Identity' : {
        'meta_info' : _MetaInfoClass('Gr303Rdt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303RDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88026Man_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88026Man_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88026Man',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Telink_Identity' : {
        'meta_info' : _MetaInfoClass('Telink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'teLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pon622_Identity' : {
        'meta_info' : _MetaInfoClass('Pon622_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pon622',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88024Tokenbus_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88024Tokenbus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88024TokenBus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbasiin_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbasiin_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiIn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Pdnetherloop2_Identity' : {
        'meta_info' : _MetaInfoClass('Pdnetherloop2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'pdnEtherLoop2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmvciendpt_Identity' : {
        'meta_info' : _MetaInfoClass('Atmvciendpt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Alueponphysicaluni_Identity' : {
        'meta_info' : _MetaInfoClass('Alueponphysicaluni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Tdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Imt_Identity' : {
        'meta_info' : _MetaInfoClass('Imt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'imt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds0Bundle_Identity' : {
        'meta_info' : _MetaInfoClass('Ds0Bundle_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds0Bundle',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propbwap2Mp_Identity' : {
        'meta_info' : _MetaInfoClass('Propbwap2Mp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propBWAp2Mp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propdocswirelessmaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('Propdocswirelessmaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessMaclayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propvirtual_Identity' : {
        'meta_info' : _MetaInfoClass('Propvirtual_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee1394_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee1394_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee1394',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mpls_Identity' : {
        'meta_info' : _MetaInfoClass('Mpls_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V37_Identity' : {
        'meta_info' : _MetaInfoClass('V37_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v37',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propdocswirelessdownstream_Identity' : {
        'meta_info' : _MetaInfoClass('Propdocswirelessdownstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessDownstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bgppolicyaccounting_Identity' : {
        'meta_info' : _MetaInfoClass('Bgppolicyaccounting_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bgppolicyaccounting',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Primaryisdn_Identity' : {
        'meta_info' : _MetaInfoClass('Primaryisdn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'primaryISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ip_Identity' : {
        'meta_info' : _MetaInfoClass('Ip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hssi_Identity' : {
        'meta_info' : _MetaInfoClass('Hssi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hssi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'V11_Identity' : {
        'meta_info' : _MetaInfoClass('V11_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'v11',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propwirelessp2P_Identity' : {
        'meta_info' : _MetaInfoClass('Propwirelessp2P_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propWirelessP2P',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Radiomac_Identity' : {
        'meta_info' : _MetaInfoClass('Radiomac_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'radioMAC',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Hdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Siptg_Identity' : {
        'meta_info' : _MetaInfoClass('Siptg_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sipTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voicefgdos_Identity' : {
        'meta_info' : _MetaInfoClass('Voicefgdos_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFGDOS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dtm_Identity' : {
        'meta_info' : _MetaInfoClass('Dtm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aluepononu_Identity' : {
        'meta_info' : _MetaInfoClass('Aluepononu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluEponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fastetherfx_Identity' : {
        'meta_info' : _MetaInfoClass('Fastetherfx_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEtherFX',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmlogical_Identity' : {
        'meta_info' : _MetaInfoClass('Atmlogical_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmLogical',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Regular1822_Identity' : {
        'meta_info' : _MetaInfoClass('Regular1822_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'regular1822',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Msdsl_Identity' : {
        'meta_info' : _MetaInfoClass('Msdsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'msdsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbtdm_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbtdm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbTdm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceemfgd_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceemfgd_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEMFGD',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Nfas_Identity' : {
        'meta_info' : _MetaInfoClass('Nfas_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'nfas',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Async_Identity' : {
        'meta_info' : _MetaInfoClass('Async_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'async',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ifpwtype_Identity' : {
        'meta_info' : _MetaInfoClass('Ifpwtype_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ifPwType',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmima_Identity' : {
        'meta_info' : _MetaInfoClass('Atmima_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmIma',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L2Vlan_Identity' : {
        'meta_info' : _MetaInfoClass('L2Vlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l2vlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sonet_Identity' : {
        'meta_info' : _MetaInfoClass('Sonet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Wwanpp_Identity' : {
        'meta_info' : _MetaInfoClass('Wwanpp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl2Plus_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl2Plus_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl2plus',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G703At2Mb_Identity' : {
        'meta_info' : _MetaInfoClass('G703At2Mb_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g703at2mb',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Opticalchannelgroup_Identity' : {
        'meta_info' : _MetaInfoClass('Opticalchannelgroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'opticalChannelGroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbrccmaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbrccmaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voicefxs_Identity' : {
        'meta_info' : _MetaInfoClass('Voicefxs_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceFXS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscableupstreamchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Docscableupstreamchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propdocswirelessupstream_Identity' : {
        'meta_info' : _MetaInfoClass('Propdocswirelessupstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propDocsWirelessUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee802154_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee802154_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee802154',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fddi_Identity' : {
        'meta_info' : _MetaInfoClass('Fddi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fddi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hdsl2_Identity' : {
        'meta_info' : _MetaInfoClass('Hdsl2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hdsl2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Q2931_Identity' : {
        'meta_info' : _MetaInfoClass('Q2931_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'q2931',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Termpad_Identity' : {
        'meta_info' : _MetaInfoClass('Termpad_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'termPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dcn_Identity' : {
        'meta_info' : _MetaInfoClass('Dcn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dcn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Infiniband_Identity' : {
        'meta_info' : _MetaInfoClass('Infiniband_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'infiniband',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ddnx25_Identity' : {
        'meta_info' : _MetaInfoClass('Ddnx25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ddnX25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Proteon80Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Proteon80Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'proteon80Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Wwanpp2_Identity' : {
        'meta_info' : _MetaInfoClass('Wwanpp2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'wwanPP2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscableupstream_Identity' : {
        'meta_info' : _MetaInfoClass('Docscableupstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sixtofour_Identity' : {
        'meta_info' : _MetaInfoClass('Sixtofour_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sixToFour',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Eon_Identity' : {
        'meta_info' : _MetaInfoClass('Eon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'eon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ciscoislvlan_Identity' : {
        'meta_info' : _MetaInfoClass('Ciscoislvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ciscoISLvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ethernet3Mbit_Identity' : {
        'meta_info' : _MetaInfoClass('Ethernet3Mbit_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ethernet3Mbit',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gr303Idt_Identity' : {
        'meta_info' : _MetaInfoClass('Gr303Idt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gr303IDT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmdxi_Identity' : {
        'meta_info' : _MetaInfoClass('Atmdxi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Docscableupstreamrfport_Identity' : {
        'meta_info' : _MetaInfoClass('Docscableupstreamrfport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'docsCableUpstreamRfPort',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Frdlciendpt_Identity' : {
        'meta_info' : _MetaInfoClass('Frdlciendpt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'frDlciEndPt',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbrccupstream_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbrccupstream_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRccUpstream',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Cnr_Identity' : {
        'meta_info' : _MetaInfoClass('Cnr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cnr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aal5_Identity' : {
        'meta_info' : _MetaInfoClass('Aal5_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal5',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'H323Proxy_Identity' : {
        'meta_info' : _MetaInfoClass('H323Proxy_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Proxy',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Slip_Identity' : {
        'meta_info' : _MetaInfoClass('Slip_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'slip',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbrcsmaclayer_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbrcsmaclayer_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbRcsMacLayer',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hippiinterface_Identity' : {
        'meta_info' : _MetaInfoClass('Hippiinterface_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hippiInterface',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ipoveratm_Identity' : {
        'meta_info' : _MetaInfoClass('Ipoveratm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceoverframerelay_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceoverframerelay_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverFrameRelay',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L3Ipvlan_Identity' : {
        'meta_info' : _MetaInfoClass('L3Ipvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Alugponphysicaluni_Identity' : {
        'meta_info' : _MetaInfoClass('Alugponphysicaluni_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponPhysicalUni',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Miox25_Identity' : {
        'meta_info' : _MetaInfoClass('Miox25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'miox25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Para_Identity' : {
        'meta_info' : _MetaInfoClass('Para_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'para',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sipsig_Identity' : {
        'meta_info' : _MetaInfoClass('Sipsig_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sipSig',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ipswitch_Identity' : {
        'meta_info' : _MetaInfoClass('Ipswitch_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipSwitch',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Tokenring_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Tokenring_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025TokenRing',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Atmvirtual_Identity' : {
        'meta_info' : _MetaInfoClass('Atmvirtual_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'atmVirtual',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hiperlan2_Identity' : {
        'meta_info' : _MetaInfoClass('Hiperlan2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hiperlan2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Qam_Identity' : {
        'meta_info' : _MetaInfoClass('Qam_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'qam',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Alugpononu_Identity' : {
        'meta_info' : _MetaInfoClass('Alugpononu_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluGponOnu',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Tunnel_Identity' : {
        'meta_info' : _MetaInfoClass('Tunnel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'tunnel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rfc1483_Identity' : {
        'meta_info' : _MetaInfoClass('Rfc1483_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc1483',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdn_Identity' : {
        'meta_info' : _MetaInfoClass('Isdn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdn',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gfp_Identity' : {
        'meta_info' : _MetaInfoClass('Gfp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gfp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Smdsdxi_Identity' : {
        'meta_info' : _MetaInfoClass('Smdsdxi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'smdsDxi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Proppointtopointserial_Identity' : {
        'meta_info' : _MetaInfoClass('Proppointtopointserial_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propPointToPointSerial',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceoveratm_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceoveratm_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceOverAtm',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'L3Ipxvlan_Identity' : {
        'meta_info' : _MetaInfoClass('L3Ipxvlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'l3ipxvlan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceebs_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceebs_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEBS',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Myrinet_Identity' : {
        'meta_info' : _MetaInfoClass('Myrinet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'myrinet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Arap_Identity' : {
        'meta_info' : _MetaInfoClass('Arap_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Idsl_Identity' : {
        'meta_info' : _MetaInfoClass('Idsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'idsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fastether_Identity' : {
        'meta_info' : _MetaInfoClass('Fastether_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fastEther',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mpc_Identity' : {
        'meta_info' : _MetaInfoClass('Mpc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sonetoverheadchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Sonetoverheadchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Linegroup_Identity' : {
        'meta_info' : _MetaInfoClass('Linegroup_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'linegroup',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Homepna_Identity' : {
        'meta_info' : _MetaInfoClass('Homepna_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'homepna',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ultra_Identity' : {
        'meta_info' : _MetaInfoClass('Ultra_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ultra',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hippi_Identity' : {
        'meta_info' : _MetaInfoClass('Hippi_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hippi',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Adsl_Identity' : {
        'meta_info' : _MetaInfoClass('Adsl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'adsl',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dlsw_Identity' : {
        'meta_info' : _MetaInfoClass('Dlsw_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dlsw',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'H323Gatekeeper_Identity' : {
        'meta_info' : _MetaInfoClass('H323Gatekeeper_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'h323Gatekeeper',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rpr_Identity' : {
        'meta_info' : _MetaInfoClass('Rpr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rpr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ds1Fdl_Identity' : {
        'meta_info' : _MetaInfoClass('Ds1Fdl_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ds1FDL',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Basicisdn_Identity' : {
        'meta_info' : _MetaInfoClass('Basicisdn_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'basicISDN',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Propcnls_Identity' : {
        'meta_info' : _MetaInfoClass('Propcnls_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'propCnls',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sonetvt_Identity' : {
        'meta_info' : _MetaInfoClass('Sonetvt_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetVT',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Voiceencap_Identity' : {
        'meta_info' : _MetaInfoClass('Voiceencap_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'voiceEncap',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ipovercdlc_Identity' : {
        'meta_info' : _MetaInfoClass('Ipovercdlc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipOverCdlc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fast_Identity' : {
        'meta_info' : _MetaInfoClass('Fast_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fast',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ss7Siglink_Identity' : {
        'meta_info' : _MetaInfoClass('Ss7Siglink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ss7SigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bsc_Identity' : {
        'meta_info' : _MetaInfoClass('Bsc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bsc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Arcnet_Identity' : {
        'meta_info' : _MetaInfoClass('Arcnet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'arcnet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Gigabitethernet_Identity' : {
        'meta_info' : _MetaInfoClass('Gigabitethernet_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'gigabitEthernet',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Actelismetaloop_Identity' : {
        'meta_info' : _MetaInfoClass('Actelismetaloop_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'actelisMetaLOOP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Escon_Identity' : {
        'meta_info' : _MetaInfoClass('Escon_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'escon',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Capwapwtpvirtualradio_Identity' : {
        'meta_info' : _MetaInfoClass('Capwapwtpvirtualradio_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'capwapWtpVirtualRadio',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aal2_Identity' : {
        'meta_info' : _MetaInfoClass('Aal2_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aal2',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Digitalwrapperoverheadchannel_Identity' : {
        'meta_info' : _MetaInfoClass('Digitalwrapperoverheadchannel_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'digitalWrapperOverheadChannel',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Qllc_Identity' : {
        'meta_info' : _MetaInfoClass('Qllc_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'qllc',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Bits_Identity' : {
        'meta_info' : _MetaInfoClass('Bits_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'bits',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Rfc877X25_Identity' : {
        'meta_info' : _MetaInfoClass('Rfc877X25_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'rfc877x25',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Vmwarevirtualnic_Identity' : {
        'meta_info' : _MetaInfoClass('Vmwarevirtualnic_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'vmwareVirtualNic',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mpegtransport_Identity' : {
        'meta_info' : _MetaInfoClass('Mpegtransport_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mpegTransport',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Stacktostack_Identity' : {
        'meta_info' : _MetaInfoClass('Stacktostack_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'stackToStack',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Isdns_Identity' : {
        'meta_info' : _MetaInfoClass('Isdns_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'isdns',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Mfsiglink_Identity' : {
        'meta_info' : _MetaInfoClass('Mfsiglink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'mfSigLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Sonetpath_Identity' : {
        'meta_info' : _MetaInfoClass('Sonetpath_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'sonetPath',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25Mlp_Identity' : {
        'meta_info' : _MetaInfoClass('X25Mlp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25mlp',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Virtualtg_Identity' : {
        'meta_info' : _MetaInfoClass('Virtualtg_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'virtualTg',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Dvbasiout_Identity' : {
        'meta_info' : _MetaInfoClass('Dvbasiout_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'dvbAsiOut',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Hostpad_Identity' : {
        'meta_info' : _MetaInfoClass('Hostpad_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'hostPad',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ieee80212_Identity' : {
        'meta_info' : _MetaInfoClass('Ieee80212_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ieee80212',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Starlan_Identity' : {
        'meta_info' : _MetaInfoClass('Starlan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'starLan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Cblvectastar_Identity' : {
        'meta_info' : _MetaInfoClass('Cblvectastar_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'cblVectaStar',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ipforward_Identity' : {
        'meta_info' : _MetaInfoClass('Ipforward_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ipForward',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Iso88025Dtr_Identity' : {
        'meta_info' : _MetaInfoClass('Iso88025Dtr_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'iso88025Dtr',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Macseccontrolledif_Identity' : {
        'meta_info' : _MetaInfoClass('Macseccontrolledif_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'macSecControlledIF',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'X25Ple_Identity' : {
        'meta_info' : _MetaInfoClass('X25Ple_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'x25ple',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'G9981_Identity' : {
        'meta_info' : _MetaInfoClass('G9981_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'g9981',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Ibm370Parchan_Identity' : {
        'meta_info' : _MetaInfoClass('Ibm370Parchan_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'ibm370parChan',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Fciplink_Identity' : {
        'meta_info' : _MetaInfoClass('Fciplink_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'fcipLink',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
    'Aluelp_Identity' : {
        'meta_info' : _MetaInfoClass('Aluelp_Identity',
            False, 
            [
            ],
            'iana-if-type',
            'aluELP',
            _yang_ns._namespaces['iana-if-type'],
        'ydk.models.iana.iana_if_type'
        ),
    },
}




import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CfrMapProtocols_Enum' : _MetaInfoEnum('CfrMapProtocols_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'arp':'ARP',
            'serialArp':'SERIALARP',
            'ip':'IP',
            'xns':'XNS',
            'novell':'NOVELL',
            'apollo':'APOLLO',
            'vines':'VINES',
            'appletalk':'APPLETALK',
            'ieeeSpanning':'IEEESPANNING',
            'decnet':'DECNET',
            'clns':'CLNS',
            'rsrb':'RSRB',
            'bridge':'BRIDGE',
            'stun':'STUN',
            'frArp':'FRARP',
            'uncompressedTcp':'UNCOMPRESSEDTCP',
            'compressedTcp':'COMPRESSEDTCP',
            'llc2':'LLC2',
            'frSwitch':'FRSWITCH',
            'dlsw':'DLSW',
            'nhrp':'NHRP',
            'compressedRtp':'COMPRESSEDRTP',
            'wildcard':'WILDCARD',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnClpBit_Enum' : _MetaInfoEnum('CfrConnClpBit_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'setClpTo0AndCopyDeToFrsscsDe':'SETCLPTO0ANDCOPYDETOFRSSCSDE',
            'setClpTo1AndCopyDeToFrsscsDe':'SETCLPTO1ANDCOPYDETOFRSSCSDE',
            'copyDeToFrsscsDeAndClp':'COPYDETOFRSSCSDEANDCLP',
            'copyDeToClp':'COPYDETOCLP',
            'setClp1':'SETCLP1',
            'setClp0':'SETCLP0',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnDeBit_Enum' : _MetaInfoEnum('CfrConnDeBit_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'noMapClp':'NOMAPCLP',
            'mapClp':'MAPCLP',
            'setDe0':'SETDE0',
            'setDe1':'SETDE1',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnEfciBit_Enum' : _MetaInfoEnum('CfrConnEfciBit_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'mapFecn':'MAPFECN',
            'notMapFecn':'NOTMAPFECN',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnServiceTranslation_Enum' : _MetaInfoEnum('CfrConnServiceTranslation_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'serviceTranslationEnabled':'SERVICETRANSLATIONENABLED',
            'serviceTranslationNotEnabled':'SERVICETRANSLATIONNOTENABLED',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry',
            False, 
            [
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitdlci',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrConnClpBit', REFERENCE_ENUM_CLASS, 'CfrConnClpBit_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnClpBit_Enum', 
                [], [], 
                '''                The method of operation used to map loss priority
                mapping in the FR to ATM direction.
                Not supported in case of FR-FR connection.
                ''',
                'cfrconnclpbit',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnDeBit', REFERENCE_ENUM_CLASS, 'CfrConnDeBit_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnDeBit_Enum', 
                [], [], 
                '''                The method of operation for loss priority mapping in the
                B-ISDN to FR direction..
                Not supported in case of FR-FR connection.
                ''',
                'cfrconndebit',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnEfciBit', REFERENCE_ENUM_CLASS, 'CfrConnEfciBit_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnEfciBit_Enum', 
                [], [], 
                '''                Shows whether the FECN field in the FR frame is mapped 
                to the ATM EFCI field of every cell generated out of the 
                FR frame. This is used to indicate congestion in FR to
                ATM direction in case of Frame Relay/ATM  Service PVC 
                Interworking.
                Not supported in FRF.5 (Frame Relay/ATM Network 
                Interworking and FR-FR connections.
                ''',
                'cfrconnefcibit',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnFrSscsDlci', ATTRIBUTE, 'int' , None, None, 
                [(0, 1023)], [], 
                '''                The DLCI value used at the FR-SSCS layer. This is one of
                connection multiplexing methods used in Frame Relay/ATM  
                Network Interworking.
                Not supported in case of FRF.8 (FR-ATM Service PVC 
                Interworking) and FR-FR connections
                ''',
                'cfrconnfrsscsdlci',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnID', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000)], [], 
                '''                The numerical identifier of a FR/FR or FR/ATM  
                Network/Service Interworking connection.
                ''',
                'cfrconnid',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The textual name of a for FR/FR or FR/ATM  
                Network/Service Interworking connection.
                ''',
                'cfrconnname',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment1Dlci', ATTRIBUTE, 'int' , None, None, 
                [(0, 1023)], [], 
                '''                The DLCI used as the first segment of a FR-FR or FR-ATM
                Network/Service Interworking connection.
                ''',
                'cfrconnsegment1dlci',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment1Name', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The textual name used to identify the first segment of 
                a FR/FR or FR/ATM  Network/Service Interworking 
                connection.
                ''',
                'cfrconnsegment1name',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment1VCGroup', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The textual name used to identify the VC-Group in the
                first segment of a Frame Relay/ATM  Network Interworking
                (FRF.5)connection. 
                This field is not applicabe in case of,
                         FRF.8 (Frame Relay/ATM  Service Interworking)
                         and
                         FR-FR connectione. 
                ''',
                'cfrconnsegment1vcgroup',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment2Name', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The interface on which second segment of a FR-FR or 
                FR-ATM  Network/Service Interworking connection is 
                configured.
                ''',
                'cfrconnsegment2name',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment2Vci', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The value of  VCI, in the ATM connection, used as the
                second segment of a FR-ATM  Network/Service Interworking
                connection. In case of FR-FR connection, this is not 
                supported.
                ''',
                'cfrconnsegment2vci',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnSegment2Vpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The value of  VPI, in the ATM connection, used as the
                second segment of a FR-ATM  Network/Service Interworking
                connection. In case of FR-FR connection, the same will 
                be used to display the DLCI used as the second segment.
                ''',
                'cfrconnsegment2vpi',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnServiceTranslation', REFERENCE_ENUM_CLASS, 'CfrConnServiceTranslation_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry.CfrConnServiceTranslation_Enum', 
                [], [], 
                '''                Shows whether Service Translation Mode is supported or
                not. Translation Mode is the interworking of 
                internetworking (routed and/or bridged) protocols used 
                in FR-ATM  Service PVC Interworking(FRF.8).
                This is not supported in case of FRF.5 (FR-ATM network
                Interworking) and FR-FR connections.
                ''',
                'cfrconnservicetranslation',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrConnState', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Status of a FR/FR or FR/ATM  Network/Service 
                Interworking connection.
                ''',
                'cfrconnstate',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrConnectionEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrConnectionTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrConnectionTable',
            False, 
            [
            _MetaInfoClassMember('cfrConnectionEntry', REFERENCE_LIST, 'CfrConnectionEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry', 
                [], [], 
                '''                Each entry of the table contains information of a
                connection that is established for Frame Relay/Frame 
                Relay and Frame Relay/ATM Network/Service Interworking.
                ''',
                'cfrconnectionentry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrConnectionTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry.CfrElmiNeighborArStatus_Enum' : _MetaInfoEnum('CfrElmiNeighborArStatus_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'notsupported':'NOTSUPPORTED',
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrElmiNeighborArStatus', REFERENCE_ENUM_CLASS, 'CfrElmiNeighborArStatus_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry.CfrElmiNeighborArStatus_Enum', 
                [], [], 
                '''                This variable indicates the status of ELMI Address 
                registration(AR) on the neighboring device. A value 
                of 1 indicates ELMI AR is not supported on the 
                neighboring device. A value of 2 indicates ELMI AR is
                enabled on the interface. A value of 3 indicates AR is
                supported, but user disabled the exchange of IP 
                address and ifIndex with the neighbor.
                ''',
                'cfrelmineighborarstatus',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborDeviceName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Device name of the neighboring device to which the
                other end of this interface is connected.
                ''',
                'cfrelmineighbordevicename',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The Interface index of the neighboring device to 
                which this interface is connected. If the value of
                cfrElmiNeighborArStatus is 2 then this will have a
                valid value. If the value of cfrElmiNeighborArStatus
                is 3 or 1 then value of this object will be 0. NMS
                uses this object in the topology discovery of the
                network.
                ''',
                'cfrelmineighborifindex',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Management IP address of the neighboring device 
                to which the other end of this interface is 
                connected. Network management system can use this
                address to send management messages to the device.
                If address registration is not supported on the
                remote end then the value will be 0.0.0.0.
                NMS uses this object in the topology discovery of the
                network.
                ''',
                'cfrelmineighboripaddress',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborPlatformName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Platform name of the neighboring device to which the
                other end of this interface is connected.
                ''',
                'cfrelmineighborplatformname',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborVendorName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Vendor name of the neighboring device to which the
                other end of this interface is connected.
                ''',
                'cfrelmineighborvendorname',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrElmiNeighborEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrElmiNeighborTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrElmiNeighborTable',
            False, 
            [
            _MetaInfoClassMember('cfrElmiNeighborEntry', REFERENCE_LIST, 'CfrElmiNeighborEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry', 
                [], [], 
                '''                Each entry of the table contains information of the
                neighboring device connected to a physical interface.
                The entry will be present only if ELMI is enabled on
                the neighboring device interface. If the value of the
                cfrElmiRemoteStatus in the cfrElmiEntry is 1 then a 
                valid entry exists for the interface. If ELMI is not 
                supported on the remote end then, the neighbor 
                information for the interface will not be present
                ''',
                'cfrelmineighborentry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrElmiNeighborTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrElmiObjs' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrElmiObjs',
            False, 
            [
            _MetaInfoClassMember('cfrElmiIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This object represents the Management address of the
                device used for address registration. 
                Network management station can send management
                messages to this IP address. This can be 
                user configured address or the address of one of the
                interfaces on the device. If address registration is
                disabled then this will have a value of 0.0.0.0. 
                This object is accessible only if the ELMI protocol 
                is supported on the device
                ''',
                'cfrelmiipaddr',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrElmiObjs',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiArStatus_Enum' : _MetaInfoEnum('CfrElmiArStatus_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiLinkStatus_Enum' : _MetaInfoEnum('CfrElmiLinkStatus_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiRemoteStatus_Enum' : _MetaInfoEnum('CfrElmiRemoteStatus_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrElmiArStatus', REFERENCE_ENUM_CLASS, 'CfrElmiArStatus_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiArStatus_Enum', 
                [], [], 
                '''                This variable states whether the Enhanced Link
                Management Interface(ELMI) address registration(AR)
                mechanism is enabled or not on a frame relay 
                interface. A value of 1 indicates ELMI AR is 
                supported on the interface. A value of 2 indicates
                ELMI AR is supported but the user disabled the
                exchange of IP address and ifIndex with the
                neighboring device. This object doesn't have any
                significance if cfrElmiLinkStatus is disabled
                on the interface.
                ''',
                'cfrelmiarstatus',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiLinkStatus', REFERENCE_ENUM_CLASS, 'CfrElmiLinkStatus_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiLinkStatus_Enum', 
                [], [], 
                '''                This variable states whether Enhanced Link Management
                Interface(ELMI) protocol is enabled or not on a 
                frame relay interface.
                ''',
                'cfrelmilinkstatus',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiRemoteStatus', REFERENCE_ENUM_CLASS, 'CfrElmiRemoteStatus_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry.CfrElmiRemoteStatus_Enum', 
                [], [], 
                '''                This variable states the Enhanced Link 
                Management(ELMI) status on the other end of the
                interface. If cfrElmiLinkStatus is enabled on the
                other end a value of 1 will be returned,
                else 2 will be returned. This object doesn't have any
                significance if cfrElmiLinkStatus is disabled on the
                interface
                ''',
                'cfrelmiremotestatus',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrElmiEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrElmiTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrElmiTable',
            False, 
            [
            _MetaInfoClassMember('cfrElmiEntry', REFERENCE_LIST, 'CfrElmiEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry', 
                [], [], 
                '''                Each entry of the table contains information about a
                physical interface. The table can be accessible only
                if the device supports ELMI protocol and if LMI is
                enabled on the interface.
                ''',
                'cfrelmientry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrElmiTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry',
            False, 
            [
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitdlci',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrFragAssembledInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes received in fully reassembled 
                frames. It also counts the number of packets received
                without FR fragmentation header (i.e.in un-fragmentated
                pkts).
                ''',
                'cfrfragassembledinoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragAssembledInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of fully reassembled frames. It also 
                counts the number of packets received without FR 
                fragmentation header (i.e. in un-fragmentated pkts).
                ''',
                'cfrfragassembledinpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragDroppedFragmentedOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of fragments dropped because of running 
                out of memory.
                ''',
                'cfrfragdroppedfragmentedoutpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragDroppedReAssembledInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of received fragments dropped for reasons such
                as : running out of memory, receiving segments out of 
                sequence, receiving an unexpected frame with a B bit 
                set, timing out on a reassembling frame.
                ''',
                'cfrfragdroppedreassembledinpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes received in frames that have a 
                fragmentation header. The number of bytes include the
                FR header.
                ''',
                'cfrfraginoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames received that have a 
                fragmentation header.
                ''',
                'cfrfraginpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragInterleavedOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets that have been interleaved between 
                segments.
                ''',
                'cfrfraginterleavedoutpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragNotInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes received in frames that do not 
                require reassembly and therefore will not contain the 
                fragmentation header. This counter is valid only when
                end-to-end fragmentation type is set.
                ''',
                'cfrfragnotinoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragNotInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames received that do not require 
                reassembly and therefore will not contain the 
                fragmentation header. This counter is valid only when
                end-to-end fragmentation type is set.
                ''',
                'cfrfragnotinpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragNotOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes transmitted in frames that are
                not fragmented and therefore will not contain the 
                fragmentation header. This counter is valid only when 
                end-to-end fragmentation type is set.
                ''',
                'cfrfragnotoutoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragNotOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames transmitted without fragmenting
                and therefore will not contain the fragmentation header.
                This counter is valid only when end-to-end fragmentation
                type is set.
                ''',
                'cfrfragnotoutpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes that are transmitted in frames
                with a fragmenation header. The number of bytes also
                includes the FR header.
                ''',
                'cfrfragoutoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragOutOfSeqFragPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the total number of packets received with an
                unexpected sequence number. All fragments being 
                reassembled are dropped. Start a new packet with the
                received segment only if the B bit is set on the 
                segment. Otherwise the new segment is also dropped.
                ''',
                'cfrfragoutofseqfragpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of fragments that are transmitted with a
                fragmenation header.
                ''',
                'cfrfragoutpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragPreOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes transmitted in fragmented frames.
                It also counts the number of bytes trasmitted in frames
                without FR fragmentation header (i.e. in un-fragmentated
                pkts).
                ''',
                'cfrfragpreoutoctets',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragPreOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of frames fragmented and trasmitted. It 
                also counts the number of packets trasmitted without FR
                fragmentation header (i.e. in un-fragmentated pkts).
                ''',
                'cfrfragpreoutpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragSeqMissedPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of fragments received in this circuit with 
                skipped sequence number.
                ''',
                'cfrfragseqmissedpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragSize', ATTRIBUTE, 'int' , None, None, 
                [(16, 1600)], [], 
                '''                cfrFragSize defines the payload size of a fragment 
                and it excludes the FR headers and any FR fragmentation
                header.
                ''',
                'cfrfragsize',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragTimeoutsIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 1000)], [], 
                '''                Number of reassemble timer timeouts for this circuit.
                A frame requiring more than two minutes to fully 
                reassemble is dropped and timeout will be incremented
                by one.
                ''',
                'cfrfragtimeoutsin',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragType', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Fragmentation type configured by the user. The types
                supported are end-to-end, VoFR-cisco and VoFR.
                ''',
                'cfrfragtype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragUnexpectedBBitSetPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of fragments received in this circuit with 
                a B bit set. All fragments being reassembled are dropped
                and a new packet is started with this segment.
                ''',
                'cfrfragunexpectedbbitsetpkts',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrFragEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrFragTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrFragTable',
            False, 
            [
            _MetaInfoClassMember('cfrFragEntry', REFERENCE_LIST, 'CfrFragEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry', 
                [], [], 
                '''                Each entry of the table contains details of 
                fragmentation configured on  this circuit. 
                ''',
                'cfrfragentry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrFragTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapEncaps_Enum' : _MetaInfoEnum('CfrMapEncaps_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'ietf':'IETF',
            'cisco':'CISCO',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapPayloadCompressType_Enum' : _MetaInfoEnum('CfrMapPayloadCompressType_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'inapplicable':'INAPPLICABLE',
            'cisco':'CISCO',
            'frf9Software':'FRF9SOFTWARE',
            'frf9Hardware':'FRF9HARDWARE',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapRtpHdrCompress_Enum' : _MetaInfoEnum('CfrMapRtpHdrCompress_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'inapplicable':'INAPPLICABLE',
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapTcpHdrCompress_Enum' : _MetaInfoEnum('CfrMapTcpHdrCompress_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'inapplicable':'INAPPLICABLE',
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapType_Enum' : _MetaInfoEnum('CfrMapType_Enum', 'ydk.models.frame.CISCO_FRAME_RELAY_MIB',
        {
            'static':'STATIC',
            'dynamic':'DYNAMIC',
            'svc':'SVC',
        }, 'CISCO-FRAME-RELAY-MIB', _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB']),
    'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry',
            False, 
            [
            _MetaInfoClassMember('cfrMapIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 999)], [], 
                '''                An arbitrary Index to the mapping information
                associated with a certain circuit. The maximum
                value is arbitrarily picked which is considered
                sufficient for usual configuration.
                ''',
                'cfrmapindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitdlci',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrMapAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Mapping protocol address at remote end for
                this DLCI.
                NOTE: For point-to-point DLCI, the string is fixed
                to be point-to-point.
                ''',
                'cfrmapaddress',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapBroadcast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Broadcast enabled or disabled.
                ''',
                'cfrmapbroadcast',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapEncaps', REFERENCE_ENUM_CLASS, 'CfrMapEncaps_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapEncaps_Enum', 
                [], [], 
                '''                Indication of the encapsulation type for this
                mapping protocol.
                ''',
                'cfrmapencaps',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapPayloadCompress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate if payload compression is enabled.
                ''',
                'cfrmappayloadcompress',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapPayloadCompressType', REFERENCE_ENUM_CLASS, 'CfrMapPayloadCompressType_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapPayloadCompressType_Enum', 
                [], [], 
                '''                FR payload compression type, if applicable.
                FRF.9 is the Frame Relay Forum Implementation Agreement
                on FR payload compression. The compression can be done
                by either software or hardware (when equipped with the
                supporting hardware), depending on configuration.
                ''',
                'cfrmappayloadcompresstype',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapProtocol', REFERENCE_ENUM_CLASS, 'CfrMapProtocols_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CfrMapProtocols_Enum', 
                [], [], 
                '''                Mapping protocol for this circuit.
                ''',
                'cfrmapprotocol',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapRtpHdrCompress', REFERENCE_ENUM_CLASS, 'CfrMapRtpHdrCompress_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapRtpHdrCompress_Enum', 
                [], [], 
                '''                RTP header compression type, if applicable.
                The value 'passive' means that the header of an
                outgoing RTP/IP packet is compressed only if an
                incoming RTP/IP packet had a compressed header.
                The value 'active' means the header of every outgoing
                RTP/IP packet is compressed.
                ''',
                'cfrmaprtphdrcompress',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapTcpHdrCompress', REFERENCE_ENUM_CLASS, 'CfrMapTcpHdrCompress_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapTcpHdrCompress_Enum', 
                [], [], 
                '''                TCP header compression type, if applicable.
                ''',
                'cfrmaptcphdrcompress',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapType', REFERENCE_ENUM_CLASS, 'CfrMapType_Enum' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry.CfrMapType_Enum', 
                [], [], 
                '''                Type for the map creation.
                ''',
                'cfrmaptype',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrMapEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrMapTable',
            False, 
            [
            _MetaInfoClassMember('cfrMapEntry', REFERENCE_LIST, 'CfrMapEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry', 
                [], [], 
                '''                Each entry of the table contains one mapping 
                information of a Frame Relay virtual circuit.
                ''',
                'cfrmapentry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrMapTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry',
            False, 
            [
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitdlci',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'frcircuitifindex',
                'CISCO-FRAME-RELAY-MIB', True),
            _MetaInfoClassMember('cfrSvcAddrLocal', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Local E.164/X.125 address for the circuit.
                ''',
                'cfrsvcaddrlocal',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcAddrRemote', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Remote E.164/X.125 address for the circuit.
                ''',
                'cfrsvcaddrremote',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcCommitBurstIn', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's incoming Committed Burst Rate.
                See ANSI and/or ITU specifications for
                definition and calculations. For outgoing
                CBR, see frCircuitCommittedBurst per RFC 1315.
                ''',
                'cfrsvccommitburstin',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcExcessBurstIn', ATTRIBUTE, 'int' , None, None, 
                [(9600, 2440000)], [], 
                '''                Circuit's incoming Excess Burst Rate.
                See ANSI and/or ITU specifications for
                definition and calculations. For outgoing
                EBR, see frCircuitExcessBurst per RFC 1315.
                ''',
                'cfrsvcexcessburstin',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcIdleTime', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Circuit's idle time period. If expires, the
                circuit is cleared.
                ''',
                'cfrsvcidletime',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcMinThruputIn', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's incoming minimal Throughput.
                ''',
                'cfrsvcminthruputin',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcMinThruputOut', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's outgoing minimal Throughput.
                ''',
                'cfrsvcminthruputout',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcThroughputIn', ATTRIBUTE, 'int' , None, None, 
                [(9600, 1544000)], [], 
                '''                Circuit's incoming throughput. For outgoing 
                throughput (commonly referred to as CIR) see
                frCircuitThroughput per RFC1315.
                ''',
                'cfrsvcthroughputin',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrSvcEntry',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB.CfrSvcTable' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB.CfrSvcTable',
            False, 
            [
            _MetaInfoClassMember('cfrSvcEntry', REFERENCE_LIST, 'CfrSvcEntry' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry', 
                [], [], 
                '''                Each entry of the table contains circuit information
                specific to a Frame Relay Switched Virtual Circuit.
                ''',
                'cfrsvcentry',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'cfrSvcTable',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
    'CISCOFRAMERELAYMIB' : {
        'meta_info' : _MetaInfoClass('CISCOFRAMERELAYMIB',
            False, 
            [
            _MetaInfoClassMember('cfrConnectionTable', REFERENCE_CLASS, 'CfrConnectionTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrConnectionTable', 
                [], [], 
                '''                Table of Frame Relay/Frame Relay and Frame Relay/ATM
                Network/Service Interworking connection information. 
                These are specific to Cisco's implementation.
                ''',
                'cfrconnectiontable',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiNeighborTable', REFERENCE_CLASS, 'CfrElmiNeighborTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiNeighborTable', 
                [], [], 
                '''                Table of CISCO Frame Relay Neighbor ELMI information
                that is specific to CISCO implementation.
                ''',
                'cfrelmineighbortable',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiObjs', REFERENCE_CLASS, 'CfrElmiObjs' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiObjs', 
                [], [], 
                '''                ''',
                'cfrelmiobjs',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrElmiTable', REFERENCE_CLASS, 'CfrElmiTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrElmiTable', 
                [], [], 
                '''                Table of CISCO Frame Relay ELMI information that is
                specific to CISCO implementation
                ''',
                'cfrelmitable',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrFragTable', REFERENCE_CLASS, 'CfrFragTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrFragTable', 
                [], [], 
                '''                Table of Frame Relay Fragmentation information. 
                These are specific to Cisco's implementation.
                ''',
                'cfrfragtable',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrMapTable', REFERENCE_CLASS, 'CfrMapTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrMapTable', 
                [], [], 
                '''                Table of protocols and addresses mapping
                information of FR virtual circuit.
                ''',
                'cfrmaptable',
                'CISCO-FRAME-RELAY-MIB', False),
            _MetaInfoClassMember('cfrSvcTable', REFERENCE_CLASS, 'CfrSvcTable' , 'ydk.models.frame.CISCO_FRAME_RELAY_MIB', 'CISCOFRAMERELAYMIB.CfrSvcTable', 
                [], [], 
                '''                Table of FR SVC specific, descriptive
                and statistics information.
                ''',
                'cfrsvctable',
                'CISCO-FRAME-RELAY-MIB', False),
            ],
            'CISCO-FRAME-RELAY-MIB',
            'CISCO-FRAME-RELAY-MIB',
            _yang_ns._namespaces['CISCO-FRAME-RELAY-MIB'],
        'ydk.models.frame.CISCO_FRAME_RELAY_MIB'
        ),
    },
}
_meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable.CfrConnectionEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable.CfrElmiNeighborEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrElmiTable.CfrElmiEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrElmiTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrFragTable.CfrFragEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrFragTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrMapTable.CfrMapEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrMapTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrSvcTable.CfrSvcEntry']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB.CfrSvcTable']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrConnectionTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrElmiNeighborTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrElmiObjs']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrElmiTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrFragTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrMapTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']
_meta_table['CISCOFRAMERELAYMIB.CfrSvcTable']['meta_info'].parent =_meta_table['CISCOFRAMERELAYMIB']['meta_info']

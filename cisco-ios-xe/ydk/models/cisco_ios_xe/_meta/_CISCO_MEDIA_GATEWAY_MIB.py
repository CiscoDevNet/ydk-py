


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CgwadminstateEnum' : _MetaInfoEnum('CgwadminstateEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'inService':'inService',
            'forcedOutOfService':'forcedOutOfService',
            'gracefulOutOfService':'gracefulOutOfService',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CcallcontroljitterdelaymodeEnum' : _MetaInfoEnum('CcallcontroljitterdelaymodeEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'adaptive':'adaptive',
            'fixed':'fixed',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CgwservicestateEnum' : _MetaInfoEnum('CgwservicestateEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'inService':'inService',
            'forcedOutOfService':'forcedOutOfService',
            'gracefulOutOfService':'gracefulOutOfService',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry.CmgwvtmappingmodeEnum' : _MetaInfoEnum('CmgwvtmappingmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'standard':'standard',
            'titan':'titan',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An index that uniquely identifies an entry in the 
                cMediaGwTable.
                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwAdminState', REFERENCE_ENUM_CLASS, 'CgwadminstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CgwadminstateEnum', 
                [], [], 
                '''                This object is used to change the service state of 
                the Media Gateway from inService to outOfService or from 
                outOfService to inService. 
                The resulting service state of the gateway is represented  
                by 'cmgwServiceState'.
                ''',
                'cmgwadminstate',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwDomainName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object is used to represent a domain name under which   
                the Media Gateway could also be registered in a DNS name
                server. 
                
                The value of this object reflects the value of 
                cmgwConfigDomainName from the entry with a value of 
                'gateway(1)' for object cmgwConfigDomainNameEntity of 
                cMediaGwDomainNameConfigTable.
                
                If there is no entry in cMediaGwDomainNameConfigTable with
                'gateway(1)' of cmgwConfigDomainNameEntity, then
                the value of this object will be empty string.
                ''',
                'cmgwdomainname',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwGraceTime', ATTRIBUTE, 'int' , None, None, 
                [('-1', '65535')], [], 
                '''                This object is used to represent grace period.
                The grace period (restart delay in RSIP message) is  
                expressed in a number of seconds. 
                It means how soon the gateway will be taken out of service.
                The value -1 indicates that the grace period time is
                disabled.
                ''',
                'cmgwgracetime',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwLawInterceptEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to enable or disable the lawful
                intercept for government.
                as follows:
                  'true'  - enable lawful intercept
                  'false' - disable lawful intercept
                ''',
                'cmgwlawinterceptenabled',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object represents the entPhysicalIndex of the
                card in which media gateway is running. It will contain
                value 0 if the entPhysicalIndex value is not available or 
                not applicable
                ''',
                'cmgwphysicalindex',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwServiceState', REFERENCE_ENUM_CLASS, 'CgwservicestateEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CgwservicestateEnum', 
                [], [], 
                '''                This object indicates the current service state of the Media 
                Gateway.
                This object is controlled by 'cmgwAdminState' 
                object.
                ''',
                'cmgwservicestate',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSrcFilterEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is used to enable or disable the source IP
                and port filtering with MGC for security consideration
                as follows:
                  'true'  - source IP and port filter is enabled 
                  'false' - source IP and port filter is disable 
                ''',
                'cmgwsrcfilterenabled',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwV23Enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is to enable or disable V23 tone.
                Setting the object value to 'true', will cause VXSM (Voice Switching
                Service Module) to detect V23 tone.
                ''',
                'cmgwv23enabled',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwVtMappingMode', REFERENCE_ENUM_CLASS, 'CmgwvtmappingmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry.CmgwvtmappingmodeEnum', 
                [], [], 
                '''                This object is used to represent the VT (sonet Virtual
                Tributary) counting.
                
                standard - standard counting (based on Bellcore TR253)
                titan    - TITAN5500 counting (based on Tellabs TITAN 5500)
                
                Note: 'titan' is valid only if sonet line medium type 
                      (sonetMediumType of SONET-MIB) is 'sonet' and 
                      sonet path payload type (cspSonetPathPayload of
                      CISCO-SONET-MIB) is 'vt15vc11'.
                ''',
                'cmgwvtmappingmode',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwtable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwtable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwEntry', REFERENCE_LIST, 'Cmediagwentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry', 
                [], [], 
                '''                A Media Gateway Entry.  
                At system power-up, an entry is created by the agent 
                if the system detects a media gateway module has been added 
                to the system, and an entry is deleted if the entry associated
                media gateway module has been removed from the system.
                ''',
                'cmediagwentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry.CmgwsignalprotocolEnum' : _MetaInfoEnum('CmgwsignalprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'other':'other',
            'mgcp':'mgcp',
            'h248':'h248',
            'tgcp':'tgcp',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwSignalProtocolIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                An index that uniquely identifies an entry in
                cmgwSignalProtocolTable.
                ''',
                'cmgwsignalprotocolindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwSignalMgcProtocolPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object specifies the protocol port of the Media Gateway
                Controller (MGC).
                If the value of cmgwSignalProtocol is 'mgcp(2)' or 'tgcp(4)'
                and the value of cmgwSignalProtcolVersion is '1.0', the
                default value of this object is '2427'.
                If the value of cmgwSignalProtocol is 'h248(3)' and the
                value of cmgwSignalProtcolVersion is '1.0', the default
                value of this object is '2944'.
                ''',
                'cmgwsignalmgcprotocolport',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocol', REFERENCE_ENUM_CLASS, 'CmgwsignalprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry.CmgwsignalprotocolEnum', 
                [], [], 
                '''                This object is used to represent the protocol type.
                other - None of the following types.
                mgcp  - Media Gateway Control Protocol
                h248 - Media Gateway Control (ITU H.248)
                tgcp - Trunking Gateway Control Protocol
                ''',
                'cmgwsignalprotocol',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocolConfigVer', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                This object specifies the protocol version
                used by the gateway in the messages to MGC
                in order to exchange the service capabilities.
                
                For example cmgwSignalProtocol is 'h248(3)' and
                this object can be string '1' or '1.0', '2' or '2.0'. 
                
                'MAX' is a special string indicating the gateway will
                use the highest protocol version supported in the 
                gateway, but it can be changed to lower version after 
                it negotiates with MGC. The final negotiated protocol
                version will be indicated in cmgwSignalProtocolVersion.
                
                The version strings other than 'MAX' can be specified for
                the gateway to communicate with the MGC which doesn't
                support service capabilities negotiation. For example if
                a MGC supports only version 1.0 MGCP, this object should
                be set to '1' to instruct the gateway using MGCP 
                version 1.0 format messages to communicate with MGC. 
                ''',
                'cmgwsignalprotocolconfigver',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocolPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object is used to represent the UDP port associated 
                with the protocol.
                If the value of cmgwSignalProtocol is 'mgcp(2)' and the
                value of cmgwSignalProtcolVersion is '1.0', the default
                value of this object is '2727'. 
                If the value of cmgwSignalProtocol is 'h248(3)' and the
                value of cmgwSignalProtcolVersion is '1.0', the default
                value of this object is '2944'.
                ''',
                'cmgwsignalprotocolport',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocolPreference', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the preference of the signal protocol 
                supported in the media gateway.
                
                If this object is set to 0, the corresponding signal
                protocol will not be used by the gateway.
                 
                The value of this object is unique within the corresponding
                gateway. The entry with lower value has higher preference.
                ''',
                'cmgwsignalprotocolpreference',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocolVersion', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                This object is used to represent the protocol version. 
                For example cmgwSignalProtocol is 'mgcp(2)' and
                this object is string '1.0'. cmgwSignalProtocol is 
                'h248(3)' and this object is set to '2.0'.
                ''',
                'cmgwsignalprotocolversion',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cmgwSignalProtocolEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmgwsignalprotocoltable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmgwsignalprotocoltable',
            False, 
            [
            _MetaInfoClassMember('cmgwSignalProtocolEntry', REFERENCE_LIST, 'Cmgwsignalprotocolentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry', 
                [], [], 
                '''                Each entry represents an signaling protocol supported
                by the media gateway.
                ''',
                'cmgwsignalprotocolentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cmgwSignalProtocolTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwIpConfigIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                A unique index to identify each media gateway IP address.
                ''',
                'cmgwipconfigindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwIpConfigAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The configured IP address of media gateway.
                This object can not be modified.
                ''',
                'cmgwipconfigaddress',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object is the IP address type.
                ''',
                'cmgwipconfigaddrtype',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigDefaultGwIp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies cmgwIpConfigAddress of the entry
                will become the default gateway address.
                This object can be set to 'true' for only one entry in
                the table.
                ''',
                'cmgwipconfigdefaultgwip',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigForRemoteMapping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the address defined in
                cmgwIpConfigAddress is the address mapping at the
                remote end of this PVC. 
                
                If this object is set to 'true', the address defined
                in cmgwIpConfigAddress is for the remote end of the PVC.
                If this object is set to 'false', the address defined
                in cmgwIpConfigAddress is for the local end of the PVC.
                ''',
                'cmgwipconfigforremotemapping',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object is ifIndex of the interface which is associated
                to the media gateway IP address.
                
                For ATM interface, the IP address should be associated to
                an existing PVC:
                   cmgwIpConfigIfIndex represents port of the PVC
                   cmgwIpConfigVpi represents VPI of the PVC
                   cmgwIpConfigVci represents VCI of the PVC
                And one PVC only can be associated with one IP address.
                
                If this object is set to zero which means the IP address
                is not associated to any interface.
                ''',
                'cmgwipconfigifindex',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to add and delete an entry.
                
                When an entry of the table is created, the following 
                objects are mandatory:
                    cmgwIpConfigIfIndex
                    cmgwIpConfigVpi
                    cmgwIpConfigVci
                    cmgwIpConfigAddress
                    cmgwIpConfigSubnetMask
                
                These objects can not be modified after the value of this
                object is set to 'active'. 
                Modification can only be done by deleting and re-adding the 
                entry again.
                
                After the system verify the validity of the data, it
                will set the cmgwIpConfigRowStatus to 'active'.
                ''',
                'cmgwipconfigrowstatus',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigSubnetMask', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                This object is used to specify the number of leading one   
                bits which from the mask to be logical-ANDed with the media  
                gateway address before being compared to the value in the 
                cmgwIpCofigAddress.
                
                Any assignment (implicit or otherwise) of an instance of
                this object to a value x must be rejected if the bitwise
                logical-AND of the mask formed from x with the value 
                of the corresponding instance of the cmgwIpCofigAddress 
                object is not equal to cmgwIpCofigAddress.
                ''',
                'cmgwipconfigsubnetmask',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigVci', ATTRIBUTE, 'int' , None, None, 
                [('-1', '65535')], [], 
                '''                This object represents VCI of the PVC which is associated
                to the IP address.
                If the IP address is not associated to PVC, the value
                of this object is set to -1.
                ''',
                'cmgwipconfigvci',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwIpConfigVpi', ATTRIBUTE, 'int' , None, None, 
                [('-1', '4095')], [], 
                '''                This object represents VPI of the PVC which is associated
                to the IP address.
                If the IP address is not associated to PVC, the value 
                of this object is set to -1.
                ''',
                'cmgwipconfigvpi',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwIpConfigEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwipconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwipconfigtable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwIpConfigEntry', REFERENCE_LIST, 'Cmediagwipconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry', 
                [], [], 
                '''                A Media Gateway IP configuration entry. 
                Each entry represents a media gateway IP address for MGCs
                to communicate with the media gateway.
                ''',
                'cmediagwipconfigentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwIpConfigTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry.CmgwconfigdomainnameentityEnum' : _MetaInfoEnum('CmgwconfigdomainnameentityEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'gateway':'gateway',
            'dnsServer':'dnsServer',
            'mgc':'mgc',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwConfigDomainNameIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                An index that is uniquely identifies a domain name
                configured in the system.
                ''',
                'cmgwconfigdomainnameindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwConfigDomainName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the domain name.
                
                The domain name should be unique if there are more than
                one entries having the same value in the object 
                cmgwConfigDomainNameEntity.
                For example, the gateway domain name should be unique 
                if the cmgwConfigDomainNameEntity has the value of 
                'gateway(1)'.
                ''',
                'cmgwconfigdomainname',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwConfigDomainNameEntity', REFERENCE_ENUM_CLASS, 'CmgwconfigdomainnameentityEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry.CmgwconfigdomainnameentityEnum', 
                [], [], 
                '''                This object indicates which entity to use this domain name.
                
                gateway(1)   - The domain name of media gateway.
                               With the same cmgwIndex, there is one and 
                               only one entry allowed with the value 
                               'gateway(1)' of this object.
                
                dnsServer(2) - The domain name of DNS name server that is used 
                               by Media gateway to find Internet Network 
                               Address from a DNS name.
                
                mgc(3)       - The domain name of a MGC (Media Gateway
                               Controller) associated with the media 
                               gateway. 
                ''',
                'cmgwconfigdomainnameentity',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwConfigDomainNameRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to add and delete an entry.
                
                When an entry is created, the following objects
                are mandatory:
                     cmgwConfigDomainName
                     cmgwConfigDomainNameEntity
                
                When deleting domain name of DNS name server
                (cmgwConfigDomainNameEntity is dnsServer (2)), the 
                cMediaGwDnsIpConfigTable should be empty.
                
                Adding/deleting entry with cmgwConfigDomainNameEntity
                of 'mgc' will cause adding/deleting entry in 
                cMgcConfigTable (CISCO-MGC-MIB) automatically.
                
                The cmgwConfigDomainName and cmgwConfigDomainNameEntity
                can not be modified if the value of this object is
                'active'. 
                ''',
                'cmgwconfigdomainnamerowstatus',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwDomainNameConfigEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwDomainNameConfigEntry', REFERENCE_LIST, 'Cmediagwdomainnameconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry', 
                [], [], 
                '''                Each entry represents a domain name used in the system.
                
                Creation and deletion are supported. Modification
                is prohibited.
                ''',
                'cmediagwdomainnameconfigentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwDomainNameConfigTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwDnsIpIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                An index that uniquely identifies an IP address of DNS
                name server.
                ''',
                'cmgwdnsipindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwDnsDomainName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The domain name of DNS name server.
                
                The value of this object reflects the value of 
                cmgwConfigDomainName from the entry with a value of 
                'dnsServer(2)' for object cmgwConfigDomainNameEntity of 
                cMediaGwDomainNameConfigTable.
                
                If there is no entry in cMediaGwDomainNameConfigTable with
                'dnsServer(2)' of cmgwConfigDomainNameEntity, then
                the value of this object will be empty string.
                ''',
                'cmgwdnsdomainname',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwDnsIp', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of DNS name server.
                The IP address of DNS name server must be unique
                in this table.
                ''',
                'cmgwdnsip',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwDnsIpRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to add and delete an entry.
                
                When an entry of the table is created, the value of
                this object should be set to 'createAndGo' and the
                following objects are mandatory:
                    cmgwDnsIp
                
                When the user wants to delete the entry, the value of
                this object should be set to 'destroy'.
                
                The entry can not be modified if the value of this 
                object is 'active'.
                ''',
                'cmgwdnsiprowstatus',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwDnsIpType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                DNS name server IP address type.
                ''',
                'cmgwdnsiptype',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwDnsIpConfigEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwdnsipconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwdnsipconfigtable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwDnsIpConfigEntry', REFERENCE_LIST, 'Cmediagwdnsipconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry', 
                [], [], 
                '''                Each entry represents an IP address of the DNS name 
                server.
                ''',
                'cmediagwdnsipconfigentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwDnsIpConfigTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwLifNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                An index that uniquely identifies a LIF in the 
                media gateway.
                ''',
                'cmgwlifnumber',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwLifPvcCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                This object represents the total number of PVC within 
                this LIF.
                
                When users associate/disassociate a PVC with a LIF 
                by giving a non-zero/zero value of cwacChanLifNum
                in cwAtmChanExtConfigTable, the value of this object 
                will be incremented/decremented accordingly.
                
                The value zero means there is no PVC associated with 
                the LIF.
                ''',
                'cmgwlifpvccount',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwLifVoiceIfCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                This object represents the total number of Voice Interfaces
                within this LIF.
                
                When users associate/disassociate a Voice Interface with
                a LIF by giving a non-zero/zero value of 
                ccasVoiceCfgLifNumber for the DS0 group in 
                ccasVoiceExtCfgTable, the value of this object will be 
                incremented/decremented accordingly. 
                
                The value zero means there is no Voice Interface associated
                with the LIF.
                ''',
                'cmgwlifvoiceifcount',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cmgwLifEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmgwliftable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmgwliftable',
            False, 
            [
            _MetaInfoClassMember('cmgwLifEntry', REFERENCE_LIST, 'Cmgwlifentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry', 
                [], [], 
                '''                An entry of this table is created by the media gateway
                when it supports the VoIP/VoATM application.
                ''',
                'cmgwlifentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cmgwLifTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.CmediagwcccfgclusterenabledEnum' : _MetaInfoEnum('CmediagwcccfgclusterenabledEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'disabled':'disabled',
            'enabled':'enabled',
            'conditionalEnabled':'conditionalEnabled',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.CmediagwcccfgdefbearertrafficEnum' : _MetaInfoEnum('CmediagwcccfgdefbearertrafficEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'ipPvcAal5':'ipPvcAal5',
            'atmPvcAal2':'atmPvcAal2',
            'atmSvcAal2':'atmSvcAal2',
            'atmSvcAal1':'atmSvcAal1',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cMediaGwCcCfgAal1SvcNamePrefix', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the prefix of the name schema for
                voice over AAL1 SVC (Switched Virtual Circuit)
                terminations.
                The value of this object must be unique among the 
                following objects:
                       cMediaGwCcCfgDsNamePrefix
                       cMediaGwCcCfgRtpNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgDefRtpNamePrefix
                This object can not be modified when there is any
                AAL1 SVC termination type existing in the media gateway.
                It is default to 'AAL1/SVC'.
                ''',
                'cmediagwcccfgaal1svcnameprefix',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgAal2SvcNamePrefix', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the prefix of the name schema for
                voice over AAL2 SVC (Switched Virtual Circuit)
                terminations.
                The value of this object must be unique among the 
                following objects:
                       cMediaGwCcCfgDsNamePrefix
                       cMediaGwCcCfgRtpNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgDefRtpNamePrefix
                This object can not be modified when there is any
                AAL2 SVC termination type existing in the media gateway.
                It is default to 'AAL2/SVC'.
                ''',
                'cmediagwcccfgaal2svcnameprefix',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgBearerTos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies Type Of Service (TOS) field
                of IP header for the voice payload packet in VoIP
                application.
                ''',
                'cmediagwcccfgbearertos',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgClusterEnabled', REFERENCE_ENUM_CLASS, 'CmediagwcccfgclusterenabledEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.CmediagwcccfgclusterenabledEnum', 
                [], [], 
                '''                This object specifies the condition of the cluster generation
                in the call control.
                
                A cluster is a group of endpoints that share a particular
                bearer possibility for connections among each other.
                
                disabled(1) - The generation of the cluster attribute
                              is disabled.
                enabled(2) - Unconditionally generate the cluster
                             attribute.
                conditionalEnabled(3) - The generation of the cluster 
                              attribute is upon MGC request.
                ''',
                'cmediagwcccfgclusterenabled',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgControlTos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies Type Of Service (TOS) field of
                IP header for the signaling control packet in VoIP
                application.
                ''',
                'cmediagwcccfgcontroltos',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgDefaultTonePlanId', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the default tone plan index
                (the value of cvtcTonePlanId) for the media gateway.
                ''',
                'cmediagwcccfgdefaulttoneplanid',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgDefBearerTraffic', REFERENCE_ENUM_CLASS, 'CmediagwcccfgdefbearertrafficEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry.CmediagwcccfgdefbearertrafficEnum', 
                [], [], 
                '''                This object specifies the combination of the network
                type (IP/ATM), virtual circuit type (PVC/SVC) and
                ATM adaptation layer type (AAL1/AAL2/AAL5) for the
                connection used in transporting bearer traffic.
                
                    ipPvcAal5 (1) - The bearer traffic is transported in
                                    IP network, through Permanent Virtual
                                    Circuit(PVC) over AAL5 adaptation layer.
                    atmPvcAal2 (2) - The bearer traffic is transported in
                                     ATM network, through Permanent Virtual
                                     Circuit(PVC) over AAL2 adaptation layer.
                    atmSvcAal2 (3) - The bearer traffic is transported in
                                     ATM network, through Switching Virtual
                                     Circuit(SVC) over AAL2 adaptation layer.
                    atmSvcAal1 (4) - The bearer traffic is transported in
                                     ATM network, through Switching Virtual
                                     Circuit(SVC) over AAL1 adaptation layer.
                
                In MGCP, if the call agent specifies the bear traffic type 
                in the local connection options (CRCX request), 
                configuration of this object will have no effect, 
                otherwise the value of this object will be used when 
                media gateway sending CRCX response.
                ''',
                'cmediagwcccfgdefbearertraffic',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgDefRtpNamePrefix', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the prefix of the name schema for
                default RTP terminations.
                The value of this object must be unique among the 
                following objects:
                       cMediaGwCcCfgDsNamePrefix
                       cMediaGwCcCfgRtpNamePrefix
                       cMediaGwCcCfgAal1SvcNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                
                It is defaulted to 'TGWRTP'.
                ''',
                'cmediagwcccfgdefrtpnameprefix',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgDescrInfoEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the media gateway supports
                descriptive suffix of the name schema for terminations.
                
                There are two parts in name schema of termination, prefix
                and suffix. For example the name schema for a DS (Digital
                Subscriber) termination, can be 'DS/OC3_2/DS1_6/DS0_24'.
                It represents DS type termination in 2nd OC3 line, 
                6th DS1 and 24th DS0 channel. In this example, 'DS' is 
                the prefix, 'OC3_2/DS1_6/DS0_24' is the suffix.
                
                The name schema in above example has a descriptive suffix.
                The non-descriptive suffix for the same termination is 
                '2/6/24' and name schema becomes 'DS/2/6/24'.
                
                This object can not be modified if there is any termination
                existing in the media gateway.
                ''',
                'cmediagwcccfgdescrinfoenabled',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgDsNamePrefix', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the prefix of the name schema for
                DS (Digital Subscriber) terminations.
                The value of this object must be unique among the 
                following objects:
                       cMediaGwCcCfgDsNamePrefix
                       cMediaGwCcCfgRtpNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgDefRtpNamePrefix
                This object can not be modified when there is any
                DS termination existing in the media gateway.
                It is default to 'DS'.
                ''',
                'cmediagwcccfgdsnameprefix',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgNsePayload', ATTRIBUTE, 'int' , None, None, 
                [('98', '117')], [], 
                '''                This object specifies NSE (Network Signaling Events)
                payload type.
                ''',
                'cmediagwcccfgnsepayload',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgNseRespTimer', ATTRIBUTE, 'int' , None, None, 
                [('250', '10000')], [], 
                '''                This object specifies Network Signaling Event (NSE)
                timeout value.
                ''',
                'cmediagwcccfgnseresptimer',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgNtePayload', ATTRIBUTE, 'int' , None, None, 
                [('96', '127')], [], 
                '''                This object specifies NTE (Named Telephony Events)
                payload type.
                ''',
                'cmediagwcccfgntepayload',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgRtpNamePrefix', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the prefix of the name schema for
                RTP (Real-Time Transport Protocol) terminations.
                The value of this object must be unique among the 
                following objects:
                       cMediaGwCcCfgDsNamePrefix
                       cMediaGwCcCfgRtpNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgAal2SvcNamePrefix
                       cMediaGwCcCfgDefRtpNamePrefix
                This object can not be modified when there is any
                RTP termination type existing in the media gateway.
                It is default to 'RTP'.
                ''',
                'cmediagwcccfgrtpnameprefix',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgVbdJitterDelayMode', REFERENCE_ENUM_CLASS, 'CcallcontroljitterdelaymodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CcallcontroljitterdelaymodeEnum', 
                [], [], 
                '''                The object specifies the jitter buffer mode applied to
                a VBD (Voice Band Data) call connection.
                
                adaptive - means to use cMediaGwCcCfgVbdJitterNomDelay as
                           the initial jitter buffers size and let the DSP
                           pick the optimal value of the jitter buffer
                           size between the range of
                           cMediaGwCcCfgVbcJitterMaxDelay and
                           cMediaGwCcCfgVbcJitterMinDelay.
                
                fixed - means to use a constant jitter buffer size
                        which is specified by cMediaGwCcCfgVbdJitterNomDelay.
                ''',
                'cmediagwcccfgvbdjitterdelaymode',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgVbdJitterMaxDelay', ATTRIBUTE, 'int' , None, None, 
                [('20', '135')], [], 
                '''                This object specifies the maximum jitter buffer size 
                in VBD (Voice Band Data)
                ''',
                'cmediagwcccfgvbdjittermaxdelay',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgVbdJitterMinDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '135')], [], 
                '''                This object specifies the nominal jitter buffer size 
                in VBD (Voice Band Data)
                ''',
                'cmediagwcccfgvbdjittermindelay',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwCcCfgVbdJitterNomDelay', ATTRIBUTE, 'int' , None, None, 
                [('5', '135')], [], 
                '''                This object specifies the nominal jitter buffer size 
                in VBD (Voice Band Data)
                ''',
                'cmediagwcccfgvbdjitternomdelay',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwCallControlConfigEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwCallControlConfigEntry', REFERENCE_LIST, 'Cmediagwcallcontrolconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry', 
                [], [], 
                '''                One entry for each media gateway which supports call control 
                protocol.
                ''',
                'cmediagwcallcontrolconfigentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwCallControlConfigTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry.CmgwrscstatsindexEnum' : _MetaInfoEnum('CmgwrscstatsindexEnum', 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB',
        {
            'cpu':'cpu',
            'staticmemory':'staticmemory',
            'dynamicmemory':'dynamicmemory',
            'sysmemory':'sysmemory',
            'commbuffer':'commbuffer',
            'msgq':'msgq',
            'atmq':'atmq',
            'svccongestion':'svccongestion',
            'rsvpq':'rsvpq',
            'dspq':'dspq',
            'h248congestion':'h248congestion',
            'callpersec':'callpersec',
            'smallipcbuffer':'smallipcbuffer',
            'mediumipcbuffer':'mediumipcbuffer',
            'largeipcbuffer':'largeipcbuffer',
            'hugeipcbuffer':'hugeipcbuffer',
            'mblkipcbuffer':'mblkipcbuffer',
        }, 'CISCO-MEDIA-GATEWAY-MIB', _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB']),
    'CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwRscStatsIndex', REFERENCE_ENUM_CLASS, 'CmgwrscstatsindexEnum' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry.CmgwrscstatsindexEnum', 
                [], [], 
                '''                An index that uniquely identifies a specific gateway
                resource.
                ''',
                'cmgwrscstatsindex',
                'CISCO-MEDIA-GATEWAY-MIB', True),
            _MetaInfoClassMember('cmgwRscAverageUtilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average utilization of the
                resource over the interval specified by the
                'cmgwRscSinceLastReset'.
                ''',
                'cmgwrscaverageutilization',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwRscMaximumUtilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum utilization of the
                resource over the interval specified by the
                'cmgwRscSinceLastReset'.
                ''',
                'cmgwrscmaximumutilization',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwRscMinimumUtilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the minimum utilization of the
                resource over the interval specified by the
                'cmgwRscSinceLastReset'.
                ''',
                'cmgwrscminimumutilization',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwRscSinceLastReset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The elapsed time (in seconds) from the last periodic reset.
                
                The following objects are reset at the last reset:
                
                    'cmgwRscMaximumUtilization'
                    'cmgwRscMinimumUtilization'
                    'cmgwRscAverageUtilization'
                ''',
                'cmgwrscsincelastreset',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwRscStatsEntry',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib.Cmediagwrscstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib.Cmediagwrscstatstable',
            False, 
            [
            _MetaInfoClassMember('cMediaGwRscStatsEntry', REFERENCE_LIST, 'Cmediagwrscstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry', 
                [], [], 
                '''                Each entry stores the statistics
                information for a specific resource.
                ''',
                'cmediagwrscstatsentry',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'cMediaGwRscStatsTable',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
    'CiscoMediaGatewayMib' : {
        'meta_info' : _MetaInfoClass('CiscoMediaGatewayMib',
            False, 
            [
            _MetaInfoClassMember('cMediaGwCallControlConfigTable', REFERENCE_CLASS, 'Cmediagwcallcontrolconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable', 
                [], [], 
                '''                This table defines general call control attributes for
                the media gateway.
                ''',
                'cmediagwcallcontrolconfigtable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwDnsIpConfigTable', REFERENCE_CLASS, 'Cmediagwdnsipconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwdnsipconfigtable', 
                [], [], 
                '''                There is only one DNS name server on a gateway
                and the domain name of the DNS name server is put on 
                cMediaGwDomainNameConfigTable with 'dnsServer (2)'.
                
                There could be multi IP addresses are associated with the
                DNS name server, this table is used to store these IP 
                addresses.
                
                If any domain name using external resolution, the last entry
                of this table is not allowed to be deleted.
                ''',
                'cmediagwdnsipconfigtable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwDomainNameConfigTable', REFERENCE_CLASS, 'Cmediagwdomainnameconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable', 
                [], [], 
                '''                This table provides the domain names which are configured by 
                users. 
                The domain names can be used to represent IP addresses 
                for:
                    gateway
                    External DNS name server
                    MGC (call agent) 
                ''',
                'cmediagwdomainnameconfigtable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwIpConfigTable', REFERENCE_CLASS, 'Cmediagwipconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwipconfigtable', 
                [], [], 
                '''                This table contains a list of media gateway IP address and
                the IP address associated interface information.
                
                If IP address associated interface is PVC, only 
                aal5 control PVC or aal5 bearer PVC are valid.       
                When the PVC is aal5 control, the IP address is used to 
                communicate to MGC; when the PVC is aal5 bearer, the IP
                address is used to communicate to other gateway.
                The PVC information is kept in cwAtmChanExtConfigTable:
                 cwacChanPvcType:      aal5/aal2/aal1
                 cwacChanApplication:  control/bearer/signaling
                
                If IP address associated interface is not PVC, refer to the 
                IP addresses associated interface table for the usage
                of IP address.
                ''',
                'cmediagwipconfigtable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwRscStatsTable', REFERENCE_CLASS, 'Cmediagwrscstatstable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwrscstatstable', 
                [], [], 
                '''                This table stores the gateway resource statistics
                information.
                ''',
                'cmediagwrscstatstable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cMediaGwTable', REFERENCE_CLASS, 'Cmediagwtable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmediagwtable', 
                [], [], 
                '''                This table contains the global media gateway parameters
                information.
                It supports the modification of the global media gateway 
                parameters.
                ''',
                'cmediagwtable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwLifTable', REFERENCE_CLASS, 'Cmgwliftable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmgwliftable', 
                [], [], 
                '''                This table is for managing LIF (Logical Interface) 
                in a media gateway. 
                
                LIF is a logical interface which groups the TDM 
                DSx1s associated with a set of packet resource partitions 
                (PVCs) in a media gateway.
                
                LIF is used for:
                1. VoIP switching 
                2. VoATM switching 
                ''',
                'cmgwliftable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            _MetaInfoClassMember('cmgwSignalProtocolTable', REFERENCE_CLASS, 'Cmgwsignalprotocoltable' , 'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB', 'CiscoMediaGatewayMib.Cmgwsignalprotocoltable', 
                [], [], 
                '''                This table contains the available signaling protocols that
                are supported by the media gateway for communication with
                MGCs.
                ''',
                'cmgwsignalprotocoltable',
                'CISCO-MEDIA-GATEWAY-MIB', False),
            ],
            'CISCO-MEDIA-GATEWAY-MIB',
            'CISCO-MEDIA-GATEWAY-MIB',
            _yang_ns._namespaces['CISCO-MEDIA-GATEWAY-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_MEDIA_GATEWAY_MIB'
        ),
    },
}
_meta_table['CiscoMediaGatewayMib.Cmediagwtable.Cmediagwentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwtable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmgwsignalprotocoltable.Cmgwsignalprotocolentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmgwsignalprotocoltable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwipconfigtable.Cmediagwipconfigentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwipconfigtable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable.Cmediagwdomainnameconfigentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwdnsipconfigtable.Cmediagwdnsipconfigentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwdnsipconfigtable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmgwliftable.Cmgwlifentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmgwliftable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable.Cmediagwcallcontrolconfigentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwrscstatstable.Cmediagwrscstatsentry']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib.Cmediagwrscstatstable']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwtable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmgwsignalprotocoltable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwipconfigtable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwdomainnameconfigtable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwdnsipconfigtable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmgwliftable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwcallcontrolconfigtable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']
_meta_table['CiscoMediaGatewayMib.Cmediagwrscstatstable']['meta_info'].parent =_meta_table['CiscoMediaGatewayMib']['meta_info']

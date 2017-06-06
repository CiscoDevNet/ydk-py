


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VlantypeEnum' : _MetaInfoEnum('VlantypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'ethernet':'ethernet',
            'fddi':'fddi',
            'tokenRing':'tokenRing',
            'fddiNet':'fddiNet',
            'trNet':'trNet',
            'deprecated':'deprecated',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpstatus.VtpversionEnum' : _MetaInfoEnum('VtpversionEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'one':'one',
            'two':'two',
            'none':'none',
            'three':'three',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpstatus' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpstatus',
            False, 
            [
            _MetaInfoClassMember('vtpMaxVlanStorage', ATTRIBUTE, 'int' , None, None, 
                [('-1', '1023')], [], 
                '''                An estimate of the maximum number of VLANs about which the
                local system can recover complete VTP information after a
                reboot.  If the number of defined VLANs is greater than this
                value, then the system can not act as a VTP Server. For a
                device which has no means to calculate the estimated number,
                this value is -1.
                ''',
                'vtpmaxvlanstorage',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpNotificationsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the notifications/traps defined by
                the vtpConfigNotificationsGroup, vtpConfigNotificationsGroup2,
                and vtpConfigNotificationsGroup8 are enabled.
                ''',
                'vtpnotificationsenabled',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVersion', REFERENCE_ENUM_CLASS, 'VtpversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpstatus.VtpversionEnum', 
                [], [], 
                '''                The version of VTP in use on the local system.  A device
                will report its version capability and not any particular
                version in use on the device. If the device does not support
                vtp, the version is none(3).
                ''',
                'vtpversion',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanCreatedNotifEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the notification should
                be generated when a VLAN is created. 
                
                If the value of this object is 'true' then the
                vtpVlanCreated notification will be generated.
                
                If the value of this object is 'false' then the
                vtpVlanCreated notification will not be generated.
                ''',
                'vtpvlancreatednotifenabled',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanDeletedNotifEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the notification should
                be generated when a VLAN is deleted.  
                
                If the value of this object is 'true' then the
                vtpVlanDeleted notification will be generated.
                
                If the value of this object is 'false' then the
                vtpVlanDeleted notification will not be generated.
                ''',
                'vtpvlandeletednotifenabled',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpStatus',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Internalvlaninfo.VtpinternalvlanallocpolicyEnum' : _MetaInfoEnum('VtpinternalvlanallocpolicyEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'ascending':'ascending',
            'descending':'descending',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Internalvlaninfo' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Internalvlaninfo',
            False, 
            [
            _MetaInfoClassMember('vtpInternalVlanAllocPolicy', REFERENCE_ENUM_CLASS, 'VtpinternalvlanallocpolicyEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Internalvlaninfo.VtpinternalvlanallocpolicyEnum', 
                [], [], 
                '''                The internal VLAN allocation policy.
                
                'ascending'  - internal VLANs are allocated
                               starting from a lowwer VLAN ID and 
                               upwards.
                'descending' - internal VLANs are allocated
                               starting from a higher VLAN ID and
                               downwards.
                ''',
                'vtpinternalvlanallocpolicy',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'internalVlanInfo',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vlantrunkports' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vlantrunkports',
            False, 
            [
            _MetaInfoClassMember('vlanTrunkPortsDot1qTag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the tagging on all VLANs including
                native VLAN for all 802.1q trunks is enabled.
                
                If this object has a value of true(1) then all VLANs
                including native VLAN are tagged.  If the value is false(2)
                then all VLANs excluding native VLAN are tagged.
                
                This object has been deprecated and is replaced by the
                object 'cltcDot1qAllTaggedEnabled' in the
                CISCO-L2-TUNNEL-CONFIG-MIB
                ''',
                'vlantrunkportsdot1qtag',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortSetSerialNo', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An advisory lock used to allow several cooperating SNMPv2
                managers to coordinate their use of the SNMPv2 set operation
                acting upon any instance of vlanTrunkPortVlansEnabled.
                ''',
                'vlantrunkportsetserialno',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vlanTrunkPorts',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vlanstatistics' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vlanstatistics',
            False, 
            [
            _MetaInfoClassMember('vlanStatsExtendedVlans', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of the
                existing manageable VLANs with VLAN indices
                greater than 1024 in the system.
                ''',
                'vlanstatsextendedvlans',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanStatsFreeVlans', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of the
                free or unused VLANs in the system.
                ''',
                'vlanstatsfreevlans',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanStatsInternalVlans', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of the
                internal VLANs existing in the system.
                ''',
                'vlanstatsinternalvlans',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanStatsVlans', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of the existing
                manageable VLANs with VLAN indices from 1 to
                1024 in the system.
                ''',
                'vlanstatsvlans',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vlanStatistics',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainlocalmodeEnum' : _MetaInfoEnum('ManagementdomainlocalmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'client':'client',
            'server':'server',
            'transparent':'transparent',
            'off':'off',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainpruningstateEnum' : _MetaInfoEnum('ManagementdomainpruningstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainpruningstateoperEnum' : _MetaInfoEnum('ManagementdomainpruningstateoperEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainversioninuseEnum' : _MetaInfoEnum('ManagementdomainversioninuseEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'version1':'version1',
            'version2':'version2',
            'none':'none',
            'version3':'version3',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.VtpvlanapplystatusEnum' : _MetaInfoEnum('VtpvlanapplystatusEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'inProgress':'inProgress',
            'succeeded':'succeeded',
            'configNumberError':'configNumberError',
            'inconsistentEdit':'inconsistentEdit',
            'tooBig':'tooBig',
            'localNVStoreFail':'localNVStoreFail',
            'remoteNVStoreFail':'remoteNVStoreFail',
            'editBufferEmpty':'editBufferEmpty',
            'someOtherError':'someOtherError',
            'notPrimaryServer':'notPrimaryServer',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry.VtpvlaneditoperationEnum' : _MetaInfoEnum('VtpvlaneditoperationEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'none':'none',
            'copy':'copy',
            'apply':'apply',
            'release':'release',
            'restartTimer':'restartTimer',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Managementdomaintable.Managementdomainentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Managementdomaintable.Managementdomainentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                An arbitrary value to uniquely identify the management
                domain on the local system.
                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('managementDomainAdminSrcIf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the interface to be used as the
                preferred source interface for the VTP IP updater address.
                
                A zero length value indicates that a source interface is not
                specified.
                ''',
                'managementdomainadminsrcif',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainConfigFile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the file name where VTP configuration
                is stored in the format of <filename> or <devices>:[<filename>].
                
                <device> can be (but not limited to): flash, bootflash,
                slot0, slot1, disk0.
                ''',
                'managementdomainconfigfile',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainConfigRevNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current Configuration Revision Number as known by
                the local device for this management domain when 
                managementDomainVersionInUse is version1(1) or 
                version2(2).
                
                If managementDomainVersionInUse is version3(4), this 
                object has the same value with vtpDatabaseRevisionNumber 
                of VLAN database type.
                
                This value is updated (if necessary) whenever a VTP
                advertisement is received or generated. When in the
                'no management-domain' state, this value is 0.
                ''',
                'managementdomainconfigrevnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainDeviceID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object indicates a value that uniquely identifies
                this device within a VTP Domain.
                
                The value of this object is zero length string if
                managementDomainVersionInUse is not 'version3'.
                ''',
                'managementdomaindeviceid',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainLastChange', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The time at which the Configuration Revision Number was
                (last) increased to its current value, as indicated in the
                most recently received VTP advertisement for this management
                domain when managementDomainVersionInUse is not version3(4)
                or in the most recently received VTP VLAN database 
                advertisement for this management domain when 
                managementDomainVersionInUse is version3(4).
                
                The value 0x0000010100000000 indicates that the device which
                last increased the Configuration Revision Number had no idea
                of the date/time, or that no advertisement has been
                received.
                ''',
                'managementdomainlastchange',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainLastUpdater', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP-address (or one of them) of the VTP Server which
                last updated the Configuration Revision Number, as indicated
                in the most recently received VTP advertisement for this
                management domain, when managementDomainVersionInUse is
                version1(1) or version2(2). 
                
                If managementDomainVersionInUse is version3(4), this object
                has the value of 0.0.0.0.
                
                Before an advertisement has been received, this value is
                0.0.0.0.
                ''',
                'managementdomainlastupdater',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainLocalMode', REFERENCE_ENUM_CLASS, 'ManagementdomainlocalmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainlocalmodeEnum', 
                [], [], 
                '''                The local VTP mode in this management domain when
                managementDomainVersionInUse is version1(1) or
                version2(2).
                
                If managementDomainVersionInUse is version3(4), this 
                object has the same value with vtpDatabaseLocalMode 
                of VLAN database type.
                
                - 'client' indicates that the local system is acting
                  as a VTP client.
                
                - 'server' indicates that the local system is acting
                  as a VTP server.
                
                - 'transparent' indicates that the local system does
                  not generate or listen to VTP messages, but forwards
                  messages. This mode can also be set by the device
                  itself when the amount of VLAN information is too
                  large for it to hold in DRAM.
                
                - 'off' indicates that the local system does not
                  generate, listen to or forward any VTP messages.
                ''',
                'managementdomainlocalmode',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainLocalUpdater', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The object indicates the Internet address of the
                preferred source interface for the VTP IP updater.
                ''',
                'managementdomainlocalupdater',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainLocalUpdaterType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The object indicates the type of the Internet address
                of the preferred source interface for the VTP IP updater.
                
                The value of this object is 'unknown' if
                managementDomainVersionInUse is 'version3' or
                managementDomainLocalMode is not 'server'.
                ''',
                'managementdomainlocalupdatertype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The management name of a domain in which the local system
                is participating.  The zero-length name corresponds to the
                'no management-domain' state which is the initial value at
                installation-time if not configured otherwise.  Note that
                the zero-length name does not correspond to an operational
                management domain, and a device does not send VTP
                advertisements while in the 'no management-domain' state.  A
                device leaves the 'no management-domain' state when it
                obtains a management-domain name, either through
                configuration or through inheriting the management-domain
                name from a received VTP advertisement.
                
                When the value of an existing instance of this object is
                modified by network management, the local system should re-
                initialize its VLAN information (for the given management
                domain) as if it had just been configured with a management
                domain name at installation time.
                ''',
                'managementdomainname',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainOperSrcIf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object indicates the interface used as the
                preferred source interface for the VTP IP updater address.
                
                A zero length string indicates that a source interface is not
                available.
                ''',
                'managementdomainopersrcif',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainPruningState', REFERENCE_ENUM_CLASS, 'ManagementdomainpruningstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainpruningstateEnum', 
                [], [], 
                '''                An indication of whether VTP pruning is enabled or disabled
                in this managament domain. 
                
                This object can only be modified, either when the 
                corresponding instance value of managementDomainVersionInUse 
                is 'version1' or 'version2' and the corresponding instance 
                value of managementDomainLocalMode is 'server', or when the 
                corresponding instance value of managementDomainVersionInUse 
                is 'version3' and the corresponding instance value of 
                managementDomainLocalMode is 'server' or 'client'.
                ''',
                'managementdomainpruningstate',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainPruningStateOper', REFERENCE_ENUM_CLASS, 'ManagementdomainpruningstateoperEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainpruningstateoperEnum', 
                [], [], 
                '''                Indicates whether VTP pruning is operationally enabled or
                disabled in this managament domain.
                ''',
                'managementdomainpruningstateoper',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.
                ''',
                'managementdomainrowstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainSourceOnlyMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object specifies whether to use only the IP address of
                managementDomainAdminSrcIf as the VTP IP updater address. 
                
                'true' indicates to only use the IP address of 
                       managementDomainAdminSrcIf as the VTP IP 
                       updater address. 
                
                'false' indicates to use the IP address of 
                        managementDomainAdminSrcIf as the VTP IP 
                        updater address if managementDomainAdminSrcIf 
                        is configured with an IP address.  Otherwise, the 
                        first available IP address of the system will
                        be used.
                ''',
                'managementdomainsourceonlymode',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainTftpPathname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The complete pathname of the file at the TFTP Server
                identified by the value of managementDomainTftpServer
                in/from which VTP VLAN information for this management
                domain is to be stored/retrieved.  If the value of
                corresponding instance of managementDomainTftpServer is
                0.0.0.0, the value of this object is ignored.
                ''',
                'managementdomaintftppathname',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainTftpServer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of a TFTP Server in/from which VTP VLAN
                information for this management domain is to be
                stored/retrieved.  If the information is being locally
                stored in NVRAM, this object should take the value 0.0.0.0.
                ''',
                'managementdomaintftpserver',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainVersionInUse', REFERENCE_ENUM_CLASS, 'ManagementdomainversioninuseEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.ManagementdomainversioninuseEnum', 
                [], [], 
                '''                The current version of the VTP that is in use by the
                designated management domain. 
                
                This object can be set to none(3) only when 
                vtpVersion is none(3).
                ''',
                'managementdomainversioninuse',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpConfigDigestErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of occurrences of configuration digest errors
                for this management domain.  A configuration digest error
                occurs when a device receives a VTP advertisement for which:
                
                - the advertisement's Configuration Revision Number is
                  greater than the current locally-held value, and
                
                -  the advertisement's digest value computed by the
                 receiving device does not match the checksum in the
                 summary advertisement that was received earlier. This
                 can happen, for example, if there is a mismatch in VTP
                 passwords between the VTP devices.
                ''',
                'vtpconfigdigesterrors',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpConfigRevNumberErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of occurrences of configuration revision number
                errors for this management domain.  A configuration revision
                number error occurs when a device receives a VTP
                advertisement for which:
                
                - the advertisement's Configuration Revision Number is the
                  same as the current locally-held value, and
                
                - the advertisement's digest value is different from the
                  current locally-held value.
                ''',
                'vtpconfigrevnumbererrors',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpInAdvertRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Advert Requests received for this
                management domain.
                ''',
                'vtpinadvertrequests',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpInSubsetAdverts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Subset Adverts received for this
                management domain.
                ''',
                'vtpinsubsetadverts',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpInSummaryAdverts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Summary Adverts received for this
                management domain.
                ''',
                'vtpinsummaryadverts',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpOutAdvertRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Advert Requests sent for this
                management domain.
                ''',
                'vtpoutadvertrequests',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpOutSubsetAdverts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Subset Adverts sent for this
                management domain.
                ''',
                'vtpoutsubsetadverts',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpOutSummaryAdverts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VTP Summary Adverts sent for this
                management domain.
                ''',
                'vtpoutsummaryadverts',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanApplyStatus', REFERENCE_ENUM_CLASS, 'VtpvlanapplystatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.VtpvlanapplystatusEnum', 
                [], [], 
                '''                The current status of an 'apply' operation to instanciate
                the Edit Buffer as the new global VLAN information (for this
                management domain).  If no apply is currently active, the
                status represented is that of the most recently completed
                apply.  The possible values are:
                
                   inProgress - 'apply' operation in progress;
                
                   succeeded - the 'apply' was successful (this value is
                          also used when no apply has been invoked since the
                          last time the local system restarted);
                
                   configNumberError - the apply failed because the value of
                          vtpVlanEditConfigRevNumber was less or equal to
                          the value of current value of 
                          managementDomainConfigRevNumber;
                
                   inconsistentEdit - the apply failed because the modified
                          information was not self-consistent;
                
                   tooBig - the apply failed because the modified
                          information was too large to fit in this VTP
                          Server's non-volatile storage location;
                
                   localNVStoreFail - the apply failed in trying to store
                          the new information in a local non-volatile
                          storage location;
                
                   remoteNVStoreFail - the apply failed in trying to store
                          the new information in a remote non-volatile
                          storage location;
                
                   editBufferEmpty - the apply failed because the Edit
                          Buffer was empty (for this management domain).
                
                   someOtherError - the apply failed for some other reason
                          (e.g., insufficient memory).
                
                   notPrimaryServer - the apply failed because the local 
                          device is not a VTP primary server for VLAN 
                          database type when managementDomainVersionInUse
                          is version3(4).
                ''',
                'vtpvlanapplystatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditBufferOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The management station which is currently using the Edit
                Buffer for this management domain.  When the Edit Buffer for
                a management domain is not currently in use, the value of
                this object is the zero-length string.  Note that it is also
                the zero-length string if a manager fails to set this object
                when invoking a copy operation.
                ''',
                'vtpvlaneditbufferowner',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditConfigRevNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Configuration Revision Number to be used for the next
                apply operation.  This value is initialized (by the agent)
                on a copy operation to be one greater than the value of
                managementDomainConfigRevNumber. On an apply, if the 
                number is less or equal to the value of 
                managementDomainConfigRevNumber, then the apply fails.
                The value can be modified (increased) by network management
                before an apply to ensure that an apply does not fail for 
                this reason.
                
                This object is used to allow management control over whether
                a configuration revision received via a VTP advertisement
                after a copy operation but before the succeeding apply
                operation is lost by being overwritten by the (local) edit
                operation.  By default, the apply operation will fail in
                this situation.  By increasing this object's value after the
                copy but before the apply, management can control whether
                the apply is to succeed (with the update via VTP
                advertisement being lost).
                ''',
                'vtpvlaneditconfigrevnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditModifiedVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN-id of the modified VLAN in the Edit Buffer.
                If the object has the value of zero, any VLAN can 
                be edited. If the value of the object is not zero,
                only this VLAN can be edited.
                
                The object's value is reset to zero after a successful
                'apply' operation or a 'release' operation. 
                
                This object is only supported for devices which allow 
                only one VLAN editing for each 'apply' operation. For
                devices which allow multiple VLAN editing for each
                'apply' operation, this object is not supported.
                ''',
                'vtpvlaneditmodifiedvlan',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditOperation', REFERENCE_ENUM_CLASS, 'VtpvlaneditoperationEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry.VtpvlaneditoperationEnum', 
                [], [], 
                '''                This object always has the value 'none' when read.  When
                written, each value causes the appropriate action:
                
                 'copy' - causes the creation of rows in the
                vtpVlanEditTable exactly corresponding to the current global
                VLAN information for this management domain.  If the Edit
                Buffer (for this management domain) is not currently empty,
                a copy operation fails.  A successful copy operation starts
                the deadman-timer.
                
                 'apply' - first performs a consistent check on the the
                modified information contained in the Edit Buffer, and if
                consistent, then tries to instanciate the modified
                information as the new global VLAN information.  Note that
                an empty Edit Buffer (for the management domain) would
                always result in an inconsistency since the default VLANs
                are required to be present.
                
                 'release' - flushes the Edit Buffer (for this management
                domain), clears the Owner information, and aborts the
                deadman-timer.  A release is generated automatically if the
                deadman-timer ever expires.
                
                 'restartTimer' - restarts the deadman-timer.
                
                 'none' - no operation is performed.
                ''',
                'vtpvlaneditoperation',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'managementDomainEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Managementdomaintable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Managementdomaintable',
            False, 
            [
            _MetaInfoClassMember('managementDomainEntry', REFERENCE_LIST, 'Managementdomainentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable.Managementdomainentry', 
                [], [], 
                '''                Information about the status of one management domain.
                ''',
                'managementdomainentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'managementDomainTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanbridgetypeEnum' : _MetaInfoEnum('VtpvlanbridgetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'none':'none',
            'srt':'srt',
            'srb':'srb',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanstateEnum' : _MetaInfoEnum('VtpvlanstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'operational':'operational',
            'suspended':'suspended',
            'mtuTooBigForDevice':'mtuTooBigForDevice',
            'mtuTooBigForTrunk':'mtuTooBigForTrunk',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanstptypeEnum' : _MetaInfoEnum('VtpvlanstptypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'ieee':'ieee',
            'ibm':'ibm',
            'hybrid':'hybrid',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlantable.Vtpvlanentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlantable.Vtpvlanentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN-id of this VLAN on ISL or 802.1q trunks.
                ''',
                'vtpvlanindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('stpxVlanMISTPInstMapInstIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                The MISTP instance, to which the corresponding vlan is mapped.
                If this value of this mib object is 0,  the corresponding vlan 
                is not configured to be mapped to any MISTP instance and all
                the ports under this VLAN remain in blocking state.
                ''',
                'stpxvlanmistpinstmapinstindex',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('vtpVlanAreHopCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '13')], [], 
                '''                The maximum number of bridge hops allowed in
                All Routes Explorer frames on this VLAN.  This
                object is only instantiated when the value of the
                corresponding instance of vtpVlanType has a value of fddi(2)
                or tokenRing(3) and Source Routing is in use on this VLAN.
                ''',
                'vtpvlanarehopcount',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanBridgeNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                The bridge number of the VTP-capable switches for this
                VLAN.  This object is only instantiated for VLANs that are
                involved with emulating token ring segments.
                ''',
                'vtpvlanbridgenumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanBridgeType', REFERENCE_ENUM_CLASS, 'VtpvlanbridgetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanbridgetypeEnum', 
                [], [], 
                '''                The type of the Source Route bridging mode in use on this
                VLAN.  This object is only instantiated when the value of 
                the corresponding instance of vtpVlanType has a value of 
                fddi(2) or tokenRing(3) and Source Routing is in use on
                this VLAN.
                ''',
                'vtpvlanbridgetype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanDot10Said', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The value of the 802.10 SAID field for this VLAN.
                ''',
                'vtpvlandot10said',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The value of the ifIndex corresponding to this VLAN ID.
                If the VLAN ID does not have its corresponding interface, 
                this object has the value of zero.
                ''',
                'vtpvlanifindex',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanIsCRFBackup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if this VLAN is of type trCrf and also is acting as
                a backup trCrf for the ISL distributed BRF
                ''',
                'vtpvlaniscrfbackup',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanMtu', ATTRIBUTE, 'int' , None, None, 
                [('1500', '18190')], [], 
                '''                The MTU size on this VLAN, defined as the size of largest
                MAC-layer (information field portion of the) data frame
                which can be transmitted on the VLAN.
                ''',
                'vtpvlanmtu',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name of this VLAN.  This name is used as the ELAN-name
                for an ATM LAN-Emulation segment of this VLAN.
                ''',
                'vtpvlanname',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanParentVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The parent VLAN for this VLAN.  This object is only
                instantiated when the value of the corresponding instance of
                vtpVlanType has a value of 'fddi' or 'tokenRing' and Source
                Routing is in use on this VLAN.  The parent VLAN must have 
                a vtpVlanType value of fddiNet(4) or trNet(5), 
                respectively.
                ''',
                'vtpvlanparentvlan',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanRingNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The ring number of this VLAN.  This object is only
                instantiated when the value of the corresponding instance of
                vtpVlanType has a value of 'fddi' or 'tokenRing' and Source
                Routing is in use on this VLAN.
                ''',
                'vtpvlanringnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanState', REFERENCE_ENUM_CLASS, 'VtpvlanstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanstateEnum', 
                [], [], 
                '''                The state of this VLAN.
                
                The state 'mtuTooBigForDevice' indicates that this device
                cannot participate in this VLAN because the VLAN's MTU is
                larger than the device can support.
                
                The state 'mtuTooBigForTrunk' indicates that while this
                VLAN's MTU is supported by this device, it is too large for
                one or more of the device's trunk ports.
                ''',
                'vtpvlanstate',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanSteHopCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '13')], [], 
                '''                The maximum number of bridge hops allowed in
                Spanning Tree Explorer frames on this VLAN.  This
                object is only instantiated when the value of the
                corresponding instance of vtpVlanType has a value of fddi(2)
                or tokenRing(3) and Source Routing is in use on this VLAN.
                ''',
                'vtpvlanstehopcount',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanStpType', REFERENCE_ENUM_CLASS, 'VtpvlanstptypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlantable.Vtpvlanentry.VtpvlanstptypeEnum', 
                [], [], 
                '''                The type of the Spanning Tree Protocol (STP) running on
                this VLAN.  This object is only instanciated when the
                value of the corresponding instance of vtpVlanType has a
                value of 'fddiNet' or 'trNet'.
                
                The value returned by this object depends upon the value
                of the corresponding instance of vtpVlanEditStpType.
                
                - 'ieee' indicates IEEE STP is running exclusively.
                
                - 'ibm' indicates IBM STP is running exclusively.
                
                - 'hybrid' indicates a STP that allows a combination of
                  IEEE and IBM is running.
                
                The 'hybrid' STP type results from tokenRing/fddi VLANs
                that are children of this trNet/fddiNet parent VLAN being
                configured in a combination of SRT and SRB
                vtpVlanBridgeTypes while the instance of
                vtpVlanEditStpType that corresponds to this object is set
                to 'auto'.
                ''',
                'vtpvlanstptype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanTranslationalVlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                A VLAN to which this VLAN is being translational-bridged.
                If this value and the corresponding instance of
                vtpVlanTranslationalVlan2 are both zero, then this VLAN is
                not being translational-bridged.
                ''',
                'vtpvlantranslationalvlan1',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanTranslationalVlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Another VLAN, i.e., other than that indicated by
                vtpVlanTranslationalVlan1, to which this VLAN is being
                translational-bridged.  If this value and the corresponding
                instance of vtpVlanTranslationalVlan1 are both zero, then
                this VLAN is not being translational-bridged.
                ''',
                'vtpvlantranslationalvlan2',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanType', REFERENCE_ENUM_CLASS, 'VlantypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'VlantypeEnum', 
                [], [], 
                '''                The type of this VLAN.
                ''',
                'vtpvlantype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanTypeExt', REFERENCE_BITS, 'Vlantypeext' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'Vlantypeext', 
                [], [], 
                '''                The additional type information of this VLAN.
                ''',
                'vtpvlantypeext',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlantable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlantable',
            False, 
            [
            _MetaInfoClassMember('vtpVlanEntry', REFERENCE_LIST, 'Vtpvlanentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlantable.Vtpvlanentry', 
                [], [], 
                '''                Information about one current VLAN.  The
                managementDomainIndex value in the INDEX clause indicates
                which management domain the VLAN is in.
                ''',
                'vtpvlanentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'vtpvlanindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpInternalVlanOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The program name of the internal VLAN's
                owner application. This internal VLAN
                is allocated by the device specifically
                for this application and no one else
                could create, modify or delete this 
                VLAN.
                ''',
                'vtpinternalvlanowner',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpInternalVlanEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpinternalvlantable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpinternalvlantable',
            False, 
            [
            _MetaInfoClassMember('vtpInternalVlanEntry', REFERENCE_LIST, 'Vtpinternalvlanentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry', 
                [], [], 
                '''                Information about one current internal
                VLAN.
                ''',
                'vtpinternalvlanentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpInternalVlanTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditbridgetypeEnum' : _MetaInfoEnum('VtpvlaneditbridgetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'srt':'srt',
            'srb':'srb',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditstateEnum' : _MetaInfoEnum('VtpvlaneditstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'operational':'operational',
            'suspended':'suspended',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditstptypeEnum' : _MetaInfoEnum('VtpvlaneditstptypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'ieee':'ieee',
            'ibm':'ibm',
            'auto':'auto',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpVlanEditIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN-id which this VLAN would have on ISL or
                802.1q trunks.
                ''',
                'vtpvlaneditindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('stpxVlanMISTPInstMapEditInstIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                The MISTP instance, to which the corresponding vlan would be 
                mapped. The value of this mib object is from 0 to the value of
                stpxMISTPInstanceNumber. If setting the value of this object
                to 0, the corresponding vlan will not be mapped to a MISTP 
                instance and all the ports under this VLAN will be moved into
                the blocking state.
                ''',
                'stpxvlanmistpinstmapeditinstindex',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('vtpVlanEditAreHopCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '13')], [], 
                '''                The maximum number of bridge hops allowed in
                All Routes Explorer frames on this VLAN.  This
                object is only instantiated when the value of the
                corresponding instance of vtpVlanType has a value of fddi(2)
                or tokenRing(3) and Source Routing is in use on this VLAN.
                ''',
                'vtpvlaneditarehopcount',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditBridgeNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                The bridge number of the VTP-capable switches which would
                be used for this VLAN.  This object is only instantiated
                when the value of the corresponding instance of
                vtpVlanEditType has a value of fddiNet(4) or trNet(5).
                ''',
                'vtpvlaneditbridgenumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditBridgeType', REFERENCE_ENUM_CLASS, 'VtpvlaneditbridgetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditbridgetypeEnum', 
                [], [], 
                '''                The type of Source Route bridging mode which would be in
                use on this VLAN.  This object is only instantiated when 
                the value of  the corresponding instance of vtpVlanEditType
                has a value of fddi(2) or tokenRing(3) and Source Routing 
                is in use on this VLAN.
                ''',
                'vtpvlaneditbridgetype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditDot10Said', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The value of the 802.10 SAID field which would be used for
                this VLAN.
                
                An implementation may restrict access to this object.
                ''',
                'vtpvlaneditdot10said',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditIsCRFBackup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if this VLAN is of type trCrf and also is acting as
                a backup trCrf for the ISL distributed BRF.  This object is
                only instantiated when the value of the corresponding
                instance of vtpVlanEditType has a value of tokenRing(3).
                ''',
                'vtpvlaneditiscrfbackup',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditMtu', ATTRIBUTE, 'int' , None, None, 
                [('1500', '18190')], [], 
                '''                The MTU size which this VLAN would have, defined as the
                size of largest MAC-layer (information field portion of the)
                data frame which can be transmitted on the VLAN.
                
                An implementation may restrict access to this object.
                ''',
                'vtpvlaneditmtu',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name which this VLAN would have.  This name would be
                used as the ELAN-name for an ATM LAN-Emulation segment of
                this VLAN.
                
                An implementation may restrict access to this object.
                ''',
                'vtpvlaneditname',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditParentVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN index of the VLAN which would be the parent for
                this VLAN.  This object is only instantiated when the value
                of the corresponding instance of vtpVlanEditType has a value
                of 'fddi' or 'tokenRing' and Source Routing is in use on
                this VLAN.  The parent VLAN must have a vtpVlanEditType 
                value of fddiNet(4) or trNet(5), respectively.
                ''',
                'vtpvlaneditparentvlan',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditRingNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The ring number which would be used for this VLAN.  This
                object is only instantiated when the value of the
                corresponding instance of vtpVlanEditType has a value of
                'fddi' or 'tokenRing' and Source Routing is in use on 
                this VLAN.
                ''',
                'vtpvlaneditringnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row.  Any and all columnar objects in an
                existing row can be modified irrespective of the status of
                the row.
                
                A row is not qualified for activation until instances of at
                least its vtpVlanEditType, vtpVlanEditName and
                vtpVlanEditDot10Said columns have appropriate values.
                
                The management station should endeavor to make all rows
                consistent in the table before 'apply'ing the buffer.  An
                inconsistent entry in the table will cause the entire
                buffer to be rejected with the vtpVlanApplyStatus object
                set to the appropriate error value.
                ''',
                'vtpvlaneditrowstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditState', REFERENCE_ENUM_CLASS, 'VtpvlaneditstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditstateEnum', 
                [], [], 
                '''                The state which this VLAN would have.
                ''',
                'vtpvlaneditstate',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditSteHopCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '13')], [], 
                '''                The maximum number of bridge hops allowed in
                Spanning Tree Explorer frames on this VLAN.  This
                object is only instantiated when the value of the
                corresponding instance of vtpVlanType has a value of fddi(2)
                or tokenRing(3) and Source Routing is in use on this VLAN.
                ''',
                'vtpvlaneditstehopcount',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditStpType', REFERENCE_ENUM_CLASS, 'VtpvlaneditstptypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.VtpvlaneditstptypeEnum', 
                [], [], 
                '''                The type of the Spanning Tree Protocol which would be
                running on this VLAN.  This object is only instantiated
                when the value of the corresponding instance of
                vtpVlanEditType has a value of fddiNet(4) or trNet(5).
                
                If 'ieee' is selected, the STP that runs will be IEEE.
                
                If 'ibm' is selected, the STP that runs will be IBM.
                
                If 'auto' is selected, the STP that runs will be
                dependant on the values of vtpVlanEditBridgeType for all
                children tokenRing/fddi type VLANs.  This will result in
                a 'hybrid' STP (see vtpVlanStpType).
                ''',
                'vtpvlaneditstptype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditTranslationalVlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                A VLAN to which this VLAN would be translational-bridged.
                If this value and the corresponding instance of
                vtpVlanTranslationalVlan2 are both zero, then this VLAN
                would not be translational-bridged.
                
                An implementation may restrict access to this object.
                ''',
                'vtpvlanedittranslationalvlan1',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditTranslationalVlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Another VLAN, i.e., other than that indicated by
                vtpVlanEditTranslationalVlan1, to which this VLAN would be
                translational-bridged.  If this value and the corresponding
                instance of vtpVlanTranslationalVlan1 are both zero, then
                this VLAN would not be translational-bridged.
                
                An implementation may restrict access to this object.
                ''',
                'vtpvlanedittranslationalvlan2',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditType', REFERENCE_ENUM_CLASS, 'VlantypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'VlantypeEnum', 
                [], [], 
                '''                The type which this VLAN would have.
                An implementation may restrict access to this object.
                ''',
                'vtpvlanedittype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditTypeExt', REFERENCE_BITS, 'Vlantypeext' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'Vlantypeext', 
                [], [], 
                '''                The additional type information of this VLAN.
                vtpVlanEditTypeExt object is superseded by vtpVlanEditTypeExt2.
                ''',
                'vtpvlanedittypeext',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditTypeExt2', REFERENCE_BITS, 'Vlantypeext' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'Vlantypeext', 
                [], [], 
                '''                The additional type information of this VLAN.
                The VlanTypeExt TC specifies which bits may
                be written by a management application.
                The agent should provide a default value.
                ''',
                'vtpvlanedittypeext2',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanEditEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlanedittable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlanedittable',
            False, 
            [
            _MetaInfoClassMember('vtpVlanEditEntry', REFERENCE_LIST, 'Vtpvlaneditentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry', 
                [], [], 
                '''                Information about one VLAN in the Edit Buffer for a
                particular management domain.
                ''',
                'vtpvlaneditentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanEditTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry.VtpvlanlocalshutdownEnum' : _MetaInfoEnum('VtpvlanlocalshutdownEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'vtpvlanindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpVlanLocalShutdown', REFERENCE_ENUM_CLASS, 'VtpvlanlocalshutdownEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry.VtpvlanlocalshutdownEnum', 
                [], [], 
                '''                The object specifies the VLAN local shutdown state.
                ''',
                'vtpvlanlocalshutdown',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanLocalShutdownEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpvlanlocalshutdowntable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpvlanlocalshutdowntable',
            False, 
            [
            _MetaInfoClassMember('vtpVlanLocalShutdownEntry', REFERENCE_LIST, 'Vtpvlanlocalshutdownentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry', 
                [], [], 
                '''                An entry containing VLAN local shutdown information for a
                particular VLAN in the management domain.
                
                An entry is created if a VLAN which supports local shutdown
                has been created.
                
                An entry is deleted if a VLAN which supports local shutdown
                has been removed.
                ''',
                'vtpvlanlocalshutdownentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpVlanLocalShutdownTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdot1QtunnelEnum' : _MetaInfoEnum('Vlantrunkportdot1QtunnelEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'trunk':'trunk',
            'access':'access',
            'disabled':'disabled',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportdynamicstateEnum' : _MetaInfoEnum('VlantrunkportdynamicstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'on':'on',
            'off':'off',
            'desirable':'desirable',
            'auto':'auto',
            'onNoNegotiate':'onNoNegotiate',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportdynamicstatusEnum' : _MetaInfoEnum('VlantrunkportdynamicstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'trunking':'trunking',
            'notTrunking':'notTrunking',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportencapsulationopertypeEnum' : _MetaInfoEnum('VlantrunkportencapsulationopertypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'isl':'isl',
            'dot10':'dot10',
            'lane':'lane',
            'dot1Q':'dot1Q',
            'negotiating':'negotiating',
            'notApplicable':'notApplicable',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportencapsulationtypeEnum' : _MetaInfoEnum('VlantrunkportencapsulationtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'isl':'isl',
            'dot10':'dot10',
            'lane':'lane',
            'dot1Q':'dot1Q',
            'negotiate':'negotiate',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry',
            False, 
            [
            _MetaInfoClassMember('vlanTrunkPortIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The value of ifIndex for the interface corresponding to
                this trunk port.
                ''',
                'vlantrunkportifindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('stpxPreferredMISTPInstancesMap', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A string of octets containing one bit per MISTP instances 
                in the management domain on this trunk port. The first octet
                corresponds to MISTP instances with InstIndex values of 1 
                through 8; the second octet to MISTP instances 9 through 16;
                etc. The most significant bit of each octet corresponds to 
                the lowest value instanceIndex in that octet. The number of 
                bits for this mib object will be determined by the value of 
                stpxMISTPInstanceNumber.
                
                For each instance, if it is preferred on this trunk port,
                then the bit corresponding to that instance is set to '1'.
                
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                instance on the trunk port), any SNMP Set operation 
                accessing an instance of this object should also write the 
                value of vlanTrunkPortSetSerialNo.
                ''',
                'stpxpreferredmistpinstancesmap',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPreferredMSTInstancesMap', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A string of octets containing one bit per MST instances 
                on this trunk port.  The first octet corresponds to MST 
                instances of 0 through 7; the second octet to MST instances 
                8 through 15; etc. The most significant bit of each octet 
                corresponds to the lowest MST instance value in that octet. 
                The number of bits for this mib object will be determined 
                by the value of stpxMSTMaxInstanceNumber.
                
                For each instance, if it is preferred on this trunk port, 
                then the bit corresponding to that instance is set to '1'.
                ''',
                'stpxpreferredmstinstancesmap',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPreferredVlansMap', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                A string of octets containing one bit per VLAN in the
                management domain on this trunk port.  The first octet
                corresponds to VLANs with VlanIndex values of 0 through 7;
                the second octet to VLANs 8 through 15; etc.  The most
                significant bit of each octet corresponds to the lowest
                value VlanIndex in that octet.
                
                For each VLAN, if it is preferred on this trunk port, then
                the bit corresponding to that VLAN is set to '1'.
                The default value is 128 bytes of zeros.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'stpxpreferredvlansmap',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPreferredVlansMap2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS 
                with VlanIndex values of 1024 through 2047 in the management
                domain on this trunk port.  The first octet corresponds to 
                VLANs with VlanIndex values of 1024 through 1031; 
                the second octet to VLANs 1032 through 1039; etc. 
                The most significant bit of each octet corresponds to the 
                lowest value VlanIndex in that octet. 
                
                For each VLAN, if it is preferred on this trunk port, then 
                the bit corresponding to that VLAN is set to '1'. 
                The default value is 128 bytes of zeros. 
                
                To avoid conflicts between overlapping partial updates by 
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of 
                vlanTrunkPortSetSerialNo.
                ''',
                'stpxpreferredvlansmap2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPreferredVlansMap3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS 
                with VlanIndex values of 2048 through 3071 in the management
                domain on this trunk port.  The first octet corresponds to 
                VLANs with VlanIndex values of 2048 through 2055; 
                the second octet to VLANs 2056 through 2063; etc. 
                The most significant bit of each octet corresponds to the 
                lowest value VlanIndex in that octet. 
                
                For each VLAN, if it is preferred on this trunk port, then 
                the bit corresponding to that VLAN is set to '1'. 
                The default value is 128 bytes of zeros. 
                
                To avoid conflicts between overlapping partial updates by 
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of 
                vlanTrunkPortSetSerialNo.
                ''',
                'stpxpreferredvlansmap3k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPreferredVlansMap4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS 
                with VlanIndex values of 3072 through 4095 in the management
                domain on this trunk port.  The first octet corresponds to 
                VLANs with VlanIndex values of 3072 through 3079; 
                the second octet to VLANs 3080 through 3087; etc. 
                The most significant bit of each octet corresponds to the 
                lowest value VlanIndex in that octet. 
                
                For each VLAN, if it is preferred on this trunk port, then 
                the bit corresponding to that VLAN is set to '1'. 
                The default value is 128 bytes of zeros. 
                
                To avoid conflicts between overlapping partial updates by 
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of 
                vlanTrunkPortSetSerialNo.
                ''',
                'stpxpreferredvlansmap4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortDot1qTunnel', REFERENCE_ENUM_CLASS, 'Vlantrunkportdot1QtunnelEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdot1QtunnelEnum', 
                [], [], 
                '''                Indicates dot1qtunnel mode of the port.
                
                If the portDot1qTunnel  is set to 'trunk' mode, the port's
                vlanTrunkPortDynamicState will be changed to 'onNoNegotiate'
                and the vlanTrunkPortEncapsulationType will be set to
                'dot1Q'. These values cannot be changed unless dot1q tunnel
                is disabled on this port.
                
                If the portDot1qTunnel mode is set to 'access' mode, the
                port's vlanTrunkPortDynamicState will be set to 'off'.And
                the value of vlanTrunkPortDynamicState cannot be changed
                unless dot1q tunnel is disabled on this port. 1Q packets
                received on this access port will remain.
                
                Setting the port to dot1q tunnel 'disabled' mode causes the
                dot1q tunnel feature to be disabled on this port.  This
                object can't be set to 'trunk' or 'access' mode, when
                vlanTrunkPortsDot1qTag  object is set to 'false'.
                
                This object has been deprecated and is replaced by the
                object 'cltcDot1qTunnelMode' in the
                CISCO-L2-TUNNEL-CONFIG-MIB
                ''',
                'vlantrunkportdot1qtunnel',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortDynamicState', REFERENCE_ENUM_CLASS, 'VlantrunkportdynamicstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportdynamicstateEnum', 
                [], [], 
                '''                For devices that allows dynamic determination of whether
                a link between two switches should be a trunk or not, this
                object allows the operator to mandate the behavior of that
                dynamic mechanism.
                
                on(1) dictates that the interface will always be a
                trunk. This is the value for static entries (those that
                show no dynamic behavior). If the negotiation is supported
                on this port, negotiation will take place with the far end
                to attempt to bring the far end into trunking state.
                
                off(2) allows an operator to specify that the specified
                interface is never to be trunk, regardless of any dynamic
                mechanisms to the contrary.  This value is useful for
                overriding the default behavior of some switches. If the
                negotiation is supported on this port, negotiation will take
                place with the far end to attempt on the link to bring the
                far end into non-trunking state.
                
                desirable(3) is used to indicate that it is desirable for
                the interface to become a trunk.  The device will initiate
                any negotiation necessary to become a trunk but will not
                become a trunk unless it receives confirmation from the far
                end on the link.
                
                auto(4) is used to indicate that the interface is capable
                and willing to become a trunk but will not initiate
                trunking negotiations.  The far end on the link are
                required to either start negotiations or start sending
                encapsulated packets, on which event the specified
                interface will become a trunk.
                
                onNoNegotiate(5) is used to indicate that the interface is
                permanently set to be a trunk, and no negotiation takes
                place with the far end on the link to ensure consistent
                operation. This is similar to on(1) except no negotiation
                takes place with the far end.
                
                If the port does not support negotiation or its
                vlanTrunkPortEncapsulationType is set to negotiate(5),
                onNoNegotiate(5) is not allowed.
                
                Devices that do no support dynamic determination (for just
                a particular interface, encapsulation or for the whole
                device) need only support the 'on', and 'off' values.
                ''',
                'vlantrunkportdynamicstate',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortDynamicStatus', REFERENCE_ENUM_CLASS, 'VlantrunkportdynamicstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportdynamicstatusEnum', 
                [], [], 
                '''                Indicates whether the specified interface is either
                acting as a trunk or not. This is a result of the
                vlanTrunkPortDynamicState and the ifOperStatus of the
                trunk port itself.
                ''',
                'vlantrunkportdynamicstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortEncapsulationOperType', REFERENCE_ENUM_CLASS, 'VlantrunkportencapsulationopertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportencapsulationopertypeEnum', 
                [], [], 
                '''                The type of VLAN encapsulation in use on this trunk port.
                For intefaces with vlanTrunkPortDynamicStatus of
                notTrunking(2) the vlanTrunkPortEncapsulationOperType shall
                be notApplicable(6).
                ''',
                'vlantrunkportencapsulationopertype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortEncapsulationType', REFERENCE_ENUM_CLASS, 'VlantrunkportencapsulationtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.VlantrunkportencapsulationtypeEnum', 
                [], [], 
                '''                The type of VLAN encapsulation desired to be used on this
                trunk port. It is either a particular type, or 'negotiate'
                meaning whatever type results from the negotiation.
                negotiate(5) is not allowed if the port does not support
                negotiation or if its vlanTrunkPortDynamicState is set to
                on(1) or onNoNegotiate(5). Whether writing to this object
                in order to modify the encapsulation is supported is both
                device and interface specific.
                ''',
                'vlantrunkportencapsulationtype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortInJoins', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VTP Join messages received on this trunk
                port.
                ''',
                'vlantrunkportinjoins',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortManagementDomain', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The value of managementDomainIndex for the management
                domain on this trunk port.  Devices which support only one
                management domain will support this object read-only.
                ''',
                'vlantrunkportmanagementdomain',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortNativeVlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VlanIndex of the VLAN which is represented by native
                frames on this trunk port.  For trunk ports not supporting
                the sending and receiving of native frames, this value
                should be set to zero.
                ''',
                'vlantrunkportnativevlan',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortOldAdverts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VTP Advertisement messages which indicated
                the sender does not support VLAN-pruning received on this
                trunk port.
                ''',
                'vlantrunkportoldadverts',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortOutJoins', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VTP Join messages sent on this trunk port.
                ''',
                'vlantrunkportoutjoins',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this row.  In some circumstances, the
                creation of a row in this table is needed to enable the
                appropriate trunking/tagging protocol on the port, to enable
                the use of VTP on the port, and to assign the port to the
                appropriate management domain.  In other circumstances, rows
                in this table will be created as a by-product of other
                operations.
                ''',
                'vlantrunkportrowstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansActiveFirst2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN
                with VlanIndex values of 0 through 2047.
                
                If the bit corresponding to a VLAN is set to 1,
                it indicates that vlan is allowed and active in
                management domain.
                
                If the bit corresponding to a VLAN is set to 0,
                it indicates that vlan is not allowed or not active
                in management domain.
                ''',
                'vlantrunkportvlansactivefirst2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansActiveSecond2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN
                with VlanIndex values of 2048 through 4095.
                
                If the bit corresponding to a VLAN is set to 1,
                it indicates that vlan is allowed and active in
                management domain.
                
                If the bit corresponding to a VLAN is set to 0,
                it indicates that vlan is not allowed or not active
                in management domain.
                ''',
                'vlantrunkportvlansactivesecond2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansEnabled', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                A string of octets containing one bit per VLAN in the
                management domain on this trunk port.  The first octet
                corresponds to VLANs with VlanIndex values of 0 through 7;
                the second octet to VLANs 8 through 15; etc.  The most
                significant bit of each octet corresponds to the lowest
                value VlanIndex in that octet.  If the bit corresponding to
                a VLAN is set to '1', then the local system is enabled for
                sending and receiving frames on that VLAN; if the bit is set
                to '0', then the system is disabled from sending and
                receiving frames on that VLAN.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vlantrunkportvlansenabled',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansEnabled2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 1024 through 2047 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 1024 through 1031; the second
                octet to VLANs 1032 through 1039; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet. If the bit corresponding to a VLAN is set to
                '1', then the local system is enabled for sending and
                receiving frames on that VLAN; if the bit is set to '0',
                then the system is disabled from sending and receiving
                frames on that VLAN. The default value is zero length
                string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vlantrunkportvlansenabled2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansEnabled3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 2048 through 3071 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 2048 through 2055; the second
                octet to VLANs 2056 through 2063; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet. If the bit corresponding to a VLAN is set to
                '1', then the local system is enabled for sending and
                receiving frames on that VLAN; if the bit is set to '0',
                then the system is disabled from sending and receiving
                frames on that VLAN. The default value is zero length
                string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vlantrunkportvlansenabled3k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansEnabled4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 3072 through 4095 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 3072 through 3079; the second
                octet to VLANs 3080 through 3087; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet. If the bit corresponding to a VLAN is set to
                '1', then the local system is enabled for sending and
                receiving frames on that VLAN; if the bit is set to '0',
                then the system is disabled from sending and receiving
                frames on that VLAN. The default value is zero length
                string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vlantrunkportvlansenabled4k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansPruningEligible', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                A string of octets containing one bit per VLAN in the
                management domain on this trunk port.  The first octet
                corresponds to VLANs with VlanIndex values of 0 through 7;
                the second octet to VLANs 8 through 15; etc.  The most
                significant bit of each octet corresponds to the lowest
                value VlanIndex in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local system is permitted to prune that VLAN on this trunk
                port; if the bit is set to '0', then the system must not
                prune that VLAN on this trunk port.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vlantrunkportvlanspruningeligible',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansRcvJoined', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                A string of octets containing one bit per VLAN in the
                management domain on this trunk port.  The first octet
                corresponds to VLANs with VlanIndex values of 0 through 7;
                the second octet to VLANs 8 through 15; etc.  The most
                significant bit of each octet corresponds to the lowest
                value VlanIndex in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local switch is currently sending joins for this VLAN on
                this trunk port, i.e., it is asking to receive frames for
                this VLAN; if the bit is set to '0', then the local switch
                is not currently sending joins for this VLAN on this trunk
                port.
                ''',
                'vlantrunkportvlansrcvjoined',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansRcvJoined2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 1024 through 2047 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 1024 through 1031; the second
                octet to VLANs 1032 through 1039; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local switch is currently sending joins for this VLAN on
                this trunk port, i.e., it is asking to receive frames for
                this VLAN; if the bit is set to '0', then the local switch
                is not currently sending joins for this VLAN on this trunk
                port.
                ''',
                'vlantrunkportvlansrcvjoined2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansRcvJoined3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 2048 through 3071 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 2048 through 2055; the second
                octet to VLANs 2056 through 2063; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local switch is currently sending joins for this VLAN on
                this trunk port, i.e., it is asking to receive frames for
                this VLAN; if the bit is set to '0', then the local switch
                is not currently sending joins for this VLAN on this trunk
                port.
                ''',
                'vlantrunkportvlansrcvjoined3k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansRcvJoined4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 3072 through 4095 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 3072 through 3079; the second
                octet to VLANs 3080 through 3087; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local switch is currently sending joins for this VLAN on
                this trunk port, i.e., it is asking to receive frames for
                this VLAN; if the bit is set to '0', then the local switch
                is not currently sending joins for this VLAN on this trunk
                port.
                ''',
                'vlantrunkportvlansrcvjoined4k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansXmitJoined', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                A string of octets containing one bit per VLAN in the
                management domain on this trunk port.  The first octet
                corresponds to VLANs with VlanIndex values of 0 through 7;
                the second octet to VLANs 8 through 15; etc.  The most
                significant bit of each octet corresponds to the lowest
                value VlanIndex in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then this
                VLAN is presently being forwarded on this trunk port, i.e.,
                it is not pruned; if the bit is set to '0', then this VLAN
                is presently not being forwarded on this trunk port, either
                because it is pruned or for some other reason.
                ''',
                'vlantrunkportvlansxmitjoined',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansXmitJoined2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 1024 through 2047 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 1024 through 1031; the second
                octet to VLANs 1032 through 1039; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then this
                VLAN is presently being forwarded on this trunk port, i.e.,
                it is not pruned; if the bit is set to '0', then this VLAN
                is presently not being forwarded on this trunk port, either
                because it is pruned or for some other reason.
                ''',
                'vlantrunkportvlansxmitjoined2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansXmitJoined3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 2048 through 3071 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 2048 through 2055; the second
                octet to VLANs 2056 through 2063; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then this
                VLAN is presently being forwarded on this trunk port, i.e.,
                it is not pruned; if the bit is set to '0', then this VLAN
                is presently not being forwarded on this trunk port, either
                because it is pruned or for some other reason.
                ''',
                'vlantrunkportvlansxmitjoined3k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVlansXmitJoined4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 3072 through 4095 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 3072 through 3079; the second
                octet to VLANs 3080 through 3087; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then this
                VLAN is presently being forwarded on this trunk port, i.e.,
                it is not pruned; if the bit is set to '0', then this VLAN
                is presently not being forwarded on this trunk port, either
                because it is pruned or for some other reason.
                ''',
                'vlantrunkportvlansxmitjoined4k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortVtpEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Some trunk interface modules allow VTP to be
                enabled/disabled seperately from that of the central
                device.  In such a case this object provides management a
                way to remotely enable VTP on that module.  If a module
                does not support a seperate VTP enabled state then this
                object shall always return 'true' and will accept no other
                value during a SET operation.
                ''',
                'vlantrunkportvtpenabled',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlansPruningEligible2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 1024 through 2047 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 1024 through 1031; the second
                octet to VLANs 1032 through 1039; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local system is permitted to prune that VLAN on this trunk
                port; if the bit is set to '0', then the system must not
                prune that VLAN on this trunk port.
                The default value is zero length string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vtpvlanspruningeligible2k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlansPruningEligible3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 2048 through 3071 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 2048 through 2055; the second
                octet to VLANs 2056 through 2063; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local system is permitted to prune that VLAN on this trunk
                port; if the bit is set to '0', then the system must not
                prune that VLAN on this trunk port.
                The default value is zero length string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vtpvlanspruningeligible3k',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlansPruningEligible4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for VLANS
                with VlanIndex values of 3072 through 4095 in the management
                domain on this trunk port.  The first octet corresponds to
                VLANs with VlanIndex values of 3072 through 3079; the second
                octet to VLANs 3080 through 3087; etc.  The most significant
                bit of each octet corresponds to the lowest value VlanIndex
                in that octet.
                
                If the bit corresponding to a VLAN is set to '1', then the
                local system is permitted to prune that VLAN on this trunk
                port; if the bit is set to '0', then the system must not
                prune that VLAN on this trunk port.
                The default value is zero length string.
                
                To avoid conflicts between overlapping partial updates by
                multiple managers, i.e., updates which modify only a portion
                of an instance of this object (e.g., enable/disable a single
                VLAN on the trunk port), any SNMP Set operation accessing an
                instance of this object should also write the value of
                vlanTrunkPortSetSerialNo.
                ''',
                'vtpvlanspruningeligible4k',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vlanTrunkPortEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vlantrunkporttable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vlantrunkporttable',
            False, 
            [
            _MetaInfoClassMember('vlanTrunkPortEntry', REFERENCE_LIST, 'Vlantrunkportentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry', 
                [], [], 
                '''                Information about one trunk port.
                ''',
                'vlantrunkportentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vlanTrunkPortTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.VtpdiscoveractionEnum' : _MetaInfoEnum('VtpdiscoveractionEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'discover':'discover',
            'noOperation':'noOperation',
            'purgeResult':'purgeResult',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.VtpdiscoverstatusEnum' : _MetaInfoEnum('VtpdiscoverstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'inProgress':'inProgress',
            'succeeded':'succeeded',
            'resourceUnavailable':'resourceUnavailable',
            'someOtherError':'someOtherError',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpDiscoverAction', REFERENCE_ENUM_CLASS, 'VtpdiscoveractionEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.VtpdiscoveractionEnum', 
                [], [], 
                '''                When this object is set to discover(1), all the
                entries in vtpDiscoverResultTable for the
                corresponding management domain will be removed 
                and the local device will begin to discover all
                VTP members in the management domain. Upon the
                successful completion of discovery, the discovered
                result will be stored in the vtpDiscoverResultTable.
                
                If vtpDiscoverStatus is inProgress(1), setting 
                vtpDiscoverAction to discover(1) will fail. 
                
                When this object is set to purgeResult(3), 
                all the entries of vtpDiscoverResultTable for 
                the corresponding management domain will be
                removed from vtpDiscoverResultTable.
                
                When this object is set to noOperation(2), no
                action will be taken. When read, this object
                always returns noOperation(2).
                ''',
                'vtpdiscoveraction',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverStatus', REFERENCE_ENUM_CLASS, 'VtpdiscoverstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.VtpdiscoverstatusEnum', 
                [], [], 
                '''                The current status of VTP discovery.
                
                inProgress - a discovery is in progress;
                
                succeeded - the discovery was completed successfully
                            (this value is also used when 
                            no discover has been invoked since the
                            last time the local system restarted);
                
                resourceUnavailable - the discovery failed because
                            the required allocation of a resource is
                            presently unavailable.
                
                someOtherError - 'the discovery failed due to a
                            reason no listed.
                ''',
                'vtpdiscoverstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpLastDiscoverTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at which the last discovery
                was completed.
                
                A value of zero indicates that no discovery has been
                invoked since last time the local system restarted.
                ''',
                'vtplastdiscovertime',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDiscoverEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdiscovertable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdiscovertable',
            False, 
            [
            _MetaInfoClassMember('vtpDiscoverEntry', REFERENCE_LIST, 'Vtpdiscoverentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry', 
                [], [], 
                '''                Information related to the discovery of the
                VTP members in one management domain.
                ''',
                'vtpdiscoverentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDiscoverTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpDiscoverResultIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A value assigned by the system which identifies
                a VTP member and the associated database in the 
                management domain.
                ''',
                'vtpdiscoverresultindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpDiscoverResultConflicting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this VTP member contains
                conflicting information.
                
                true(1) indicates that this member has conflicting 
                information of the database type in the management domain.
                
                false(2) indicates that there is no conflicting information
                of the database type in the management domain.
                ''',
                'vtpdiscoverresultconflicting',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultDatabaseName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The database name associated with the
                discovered VTP member.
                ''',
                'vtpdiscoverresultdatabasename',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultDeviceId', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The unique identifier of the device for this VTP member.
                ''',
                'vtpdiscoverresultdeviceid',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultPrimaryServer', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The unique identifier of the primary server for this VTP
                member and the associated database type.
                
                There are two different VTP servers, the primary server
                and the secondary server.  When a local device is
                configured as a server for a certain database type,
                it becomes secondary server by default. 
                Primary server is an operational role under which a
                server can initiate or change the VTP configuration of the
                database type.
                
                If this VTP member itself is the primary server, the   
                value of this object is the same as the value of 
                vtpDiscoverResultDeviceId of the instance.
                ''',
                'vtpdiscoverresultprimaryserver',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultRevNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current configuration revision number as known by the
                VTP member. When the database type is unknown for
                the VTP member, this value is 0.
                ''',
                'vtpdiscoverresultrevnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultSystemName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                sysName of the VTP member.
                ''',
                'vtpdiscoverresultsystemname',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDiscoverResultEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdiscoverresulttable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdiscoverresulttable',
            False, 
            [
            _MetaInfoClassMember('vtpDiscoverResultEntry', REFERENCE_LIST, 'Vtpdiscoverresultentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry', 
                [], [], 
                '''                A conceptual row is created for each VTP member which
                is found through successful discovery.
                ''',
                'vtpdiscoverresultentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDiscoverResultTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry.VtpdatabaselocalmodeEnum' : _MetaInfoEnum('VtpdatabaselocalmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'client':'client',
            'server':'server',
            'transparent':'transparent',
            'off':'off',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpDatabaseIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A value assigned by the system which uniquely identifies
                a VTP database in the local system.
                ''',
                'vtpdatabaseindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpDatabaseLocalMode', REFERENCE_ENUM_CLASS, 'VtpdatabaselocalmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry.VtpdatabaselocalmodeEnum', 
                [], [], 
                '''                The local VTP mode for a particular database type
                in this administrative domain.
                
                - 'client' indicates that the local system is acting
                  as a VTP client of the database type.
                
                - 'server' indicates that the local system is acting
                  as a VTP server of the database type.
                
                - 'transparent' indicates that the local system does
                  not generate or listen to VTP messages of this 
                  database type, but forwards
                  messages. This mode can also be set by the device
                  itself when the size of database is too large for it
                  to hold in DRAM.
                
                - 'off' indicates that the local system does not
                  generate, listen to or forward any VTP messages
                  of this database type.
                
                The default mode is 'client' for the database type 
                known to the local device and 'transparent' for the
                unknown database type.
                ''',
                'vtpdatabaselocalmode',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabaseName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The name of the database.
                ''',
                'vtpdatabasename',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabasePrimaryServer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                There are two kinds of VTP version 3 servers for a certain
                database type - the primary server and the secondary server.
                When a local device is configured as a server for a certain
                database type, it becomes secondary server by default.
                Primary server is an operational role under which a
                server can initiate or change the VTP configuration of the
                database type.
                
                A true(1) value indicates that the local device is the 
                primary server of the database type in the management
                domain. A false(2) value indicates that the local device
                is not the primary server, or the database type is unknown
                to the local device.
                ''',
                'vtpdatabaseprimaryserver',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabasePrimaryServerId', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The unique identifier of the primary server in the
                management domain for the database type. 
                
                If no primary server is discovered for the database
                type, the object has a value of zero length string.
                ''',
                'vtpdatabaseprimaryserverid',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabaseRevNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current configuration revision number as known by the
                local device for this VTP 3 database type in the management
                domain.  This value is updated (if necessary) whenever a 
                VTP advertisement for the database type is received 
                or generated. When the database type is unknown to the 
                local device or no VTP advertisement for the database
                type is received or generated, its value is 0.
                ''',
                'vtpdatabaserevnumber',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabaseTakeOverPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                When read, this object always returns the value of a
                zero-length octet string.
                
                In the case that the VTP password is hidden from the 
                configuration and the local device intends
                to take over the whole domain, this object must be 
                set to the matching password with the secret key 
                (vtpAuthSecretKey) in the same data packet as which 
                the vtpDatabaseTakeOverPrimary is in. In all the 
                other situations, setting a valid value to this object 
                has no impact on the system.
                ''',
                'vtpdatabasetakeoverpassword',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabaseTakeOverPrimary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                There are two kinds of VTP version 3 servers for a certain
                database type - the primary server and the secondary server.
                When a local device is configured as a server for a certain
                database type, it becomes secondary server by default.
                Primary server is an operational role under which a
                server can initiate or change the VTP configuration of the
                database type.
                
                Setting this object to a true(1) value will advertise the
                configuration of this database type to the whole domain.
                
                In order to successfully setting this object to true(1),
                the value of vtpDatabaseLocalMode must be server(2). Besides
                that, when the VTP password is hidden from the configuration
                file, the password (vtpDatabaseTakeOverPassword) which 
                matches  the secret key (vtpAuthSecretKey) must be provided
                in the same data packet. 
                
                When read, the object always returns false(2).
                ''',
                'vtpdatabasetakeoverprimary',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDatabaseEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpdatabasetable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpdatabasetable',
            False, 
            [
            _MetaInfoClassMember('vtpDatabaseEntry', REFERENCE_LIST, 'Vtpdatabaseentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry', 
                [], [], 
                '''                Information about the status of the VTP database
                in the domain.  Each VTP database type known to the
                local device type has an entry in this table.
                An entry is also created for unknown database which is
                notified through VTP advertisements from other VTP
                servers.
                ''',
                'vtpdatabaseentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpDatabaseTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry.VtpauthpasswordtypeEnum' : _MetaInfoEnum('VtpauthpasswordtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB',
        {
            'plaintext':'plaintext',
            'hidden':'hidden',
        }, 'CISCO-VTP-MIB', _yang_ns._namespaces['CISCO-VTP-MIB']),
    'CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry',
            False, 
            [
            _MetaInfoClassMember('managementDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                ''',
                'managementdomainindex',
                'CISCO-VTP-MIB', True),
            _MetaInfoClassMember('vtpAuthPassword', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                By default, this object has a value of a zero-length
                character string and is considered to be not
                configured.
                
                The device uses the password to generate the 
                secret key. It can be stored in the configuration in 
                plain text or hidden from the configuration. If a VTP 
                server intends to modify the database's configuration
                in the domain but the password was hidden from the
                configuration, the same password
                (vtpDatabaseTakeOverPassword) as the hidden one
                has to be provided.
                
                When this object is set alone, vtpAuthPasswordType is
                set to plaintext(1) automatically by the system.
                Setting this object to a zero length character string
                resets the password to its default value and the
                password is considered as not configured.
                
                This object is not allowed to be set at the same time
                when  vtpAuthSecretKey is set.
                
                When the vtpAuthPasswordType is hidden(2), this object 
                will return a zero-length character string when read.
                ''',
                'vtpauthpassword',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpAuthPasswordType', REFERENCE_ENUM_CLASS, 'VtpauthpasswordtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry.VtpauthpasswordtypeEnum', 
                [], [], 
                '''                By default this object has the value as plaintext(1)
                and the VTP password is stored in the configuration
                file in plain text.
                
                Setting this object to hidden(2) will hide the
                password from the configuration.
                
                Once this object is set to hidden(2), it cannot
                be set to plaintext(1) alone. However, it may
                be set to plaintext(1) at the same time the
                password is set.
                ''',
                'vtpauthpasswordtype',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpAuthSecretKey', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None)], [], 
                '''                The device creating or modifying the VTP configuration
                signs it using the MD5 digest generated from the secret
                key before advertising it. Other devices in the domain
                receiving this configuration use the same secret key
                to accept it if it was correctly signed or drop it 
                otherwise.
                
                By default, the object has the value as a zero-length
                string and this value is read only. It is set 
                to this value automatically when the password 
                (vtpAuthPassword) is set to a zero-length octet string.
                
                The secret key can be either generated using
                the password or configured by the user. Once
                the secret key is configured by the user, it is
                stored as a hexadecimal string in the device's
                configuration and the password is considered to be
                the secret key's matching password and hidden
                from the configuration automatically.
                
                This object is not allowed to be set at the same
                time when vtpAuthPassword is set.
                
                The secret key is overwritten by a newly generated
                secret key when the password is re-configured.
                ''',
                'vtpauthsecretkey',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpAuthEntry',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib.Vtpauthenticationtable' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib.Vtpauthenticationtable',
            False, 
            [
            _MetaInfoClassMember('vtpAuthEntry', REFERENCE_LIST, 'Vtpauthentry' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry', 
                [], [], 
                '''                Information about the status of the VTP
                authentication information in one domain.
                ''',
                'vtpauthentry',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'vtpAuthenticationTable',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
    'CiscoVtpMib' : {
        'meta_info' : _MetaInfoClass('CiscoVtpMib',
            False, 
            [
            _MetaInfoClassMember('internalVlanInfo', REFERENCE_CLASS, 'Internalvlaninfo' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Internalvlaninfo', 
                [], [], 
                '''                ''',
                'internalvlaninfo',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('managementDomainTable', REFERENCE_CLASS, 'Managementdomaintable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Managementdomaintable', 
                [], [], 
                '''                The table containing information on the management domains
                in which the local system is participating.  Devices which
                support only one management domain will support just one row
                in this table, and will not let it be deleted nor let other
                rows be created.  Devices which support multiple management
                domains will allow rows to be created and deleted, but will
                not allow the last row to be deleted. If the device does 
                not support VTP, the table is read-only.
                ''',
                'managementdomaintable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanStatistics', REFERENCE_CLASS, 'Vlanstatistics' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlanstatistics', 
                [], [], 
                '''                ''',
                'vlanstatistics',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPorts', REFERENCE_CLASS, 'Vlantrunkports' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkports', 
                [], [], 
                '''                ''',
                'vlantrunkports',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vlanTrunkPortTable', REFERENCE_CLASS, 'Vlantrunkporttable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vlantrunkporttable', 
                [], [], 
                '''                The table containing information on the local system's VLAN
                trunk ports.
                ''',
                'vlantrunkporttable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpAuthenticationTable', REFERENCE_CLASS, 'Vtpauthenticationtable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpauthenticationtable', 
                [], [], 
                '''                The table contains the authentication information of VTP
                in which the local system participates.
                
                The security mechanism of VTP relies on a secret key
                that is used to alter the MD5 digest of the packets
                transmitted on the wire.  The secret value is
                created from a password that may be saved in plain text
                in the configuration or hidden from the configuration.
                
                The device creating or modifying the VTP configuration
                signs it using the MD5 digest generated from the secret
                key before advertising it. Other devices in the domain
                receive this configuration use the same secret key
                to accept it if correctly signed or drop it otherwise.
                
                The user has the option to hide the password from the
                configuration. Once the password is hidden, the secret
                key generated from the password is shown in the 
                configuration instead, and there is no other way to 
                show the password in plain text again but clearing 
                it or resetting it. 
                
                In an un-trusted area, the password on a device can 
                be configured without being unveiled. After that,
                it has to be provided again by setting the same 
                value to vtpDatabaseTakeOverPassword if the user 
                wants to take over the whole VTP management domain
                of the database type.
                
                When managementDomainVersionInUse is version3(4), the 
                authentication mechanism is common to all VTP
                database type.
                ''',
                'vtpauthenticationtable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDatabaseTable', REFERENCE_CLASS, 'Vtpdatabasetable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdatabasetable', 
                [], [], 
                '''                This table contains information of the VTP
                databases. It is not instantiated when
                managementDomainVersionInUse is version1(1), 
                version2(3) or none(3).
                ''',
                'vtpdatabasetable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverResultTable', REFERENCE_CLASS, 'Vtpdiscoverresulttable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscoverresulttable', 
                [], [], 
                '''                The table containing information of discovered VTP members
                in the management domain in which the local system is
                participating. This table is not instantiated when 
                managementDomainVersionInUse is version1(1), version2(2) or
                none(3).
                ''',
                'vtpdiscoverresulttable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpDiscoverTable', REFERENCE_CLASS, 'Vtpdiscovertable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpdiscovertable', 
                [], [], 
                '''                This table contains information related to the discovery
                of the VTP members in the designated management
                domain. This table is not instantiated when 
                managementDomainVersionInUse is version1(1), version2(3)
                or none(3).
                ''',
                'vtpdiscovertable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpInternalVlanTable', REFERENCE_CLASS, 'Vtpinternalvlantable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpinternalvlantable', 
                [], [], 
                '''                A vtpInternalVlanTable entry contains
                information on an existing internal
                VLAN. It is internally created by the
                device for a specific application program 
                and hence owned by the application.  
                It cannot be modified or deleted by (local 
                or network) management.
                ''',
                'vtpinternalvlantable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpStatus', REFERENCE_CLASS, 'Vtpstatus' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpstatus', 
                [], [], 
                '''                ''',
                'vtpstatus',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanEditTable', REFERENCE_CLASS, 'Vtpvlanedittable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanedittable', 
                [], [], 
                '''                The table which contains the information in the Edit
                Buffers, one Edit Buffer per management domain.  The
                information for a particular management domain is
                initialized, by a 'copy' operation, to be the current global
                VLAN information for that management domain.  After
                initialization, editing can be performed to add VLANs,
                delete VLANs, or modify their global parameters.  The
                information as modified through editing is local to this
                Edit Buffer.  An apply operation using the
                vtpVlanEditOperation object is necessary to instanciate the
                modified information as the new global VLAN information for
                that management domain.
                
                To use the Edit Buffer, a manager acts as follows:
                
                1. ensures the Edit Buffer for a management domain is empty,
                i.e., there are no rows in this table for this management
                domain.
                
                2. issues a SNMP set operation which sets
                vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner
                to its own identifier (e.g., its own IP address).
                
                3. if this set operation is successful, proceeds to edit the
                information in the vtpVlanEditTable.
                
                4. if and when the edited information is to be instantiated,
                issues a SNMP set operation which sets vtpVlanEditOperation
                to 'apply'.
                
                5. issues retrieval requests to obtain the value of
                vtpVlanApplyStatus, until the result of the apply is
                determined.
                
                6. releases the Edit Buffer by issuing a SNMP set operation
                which sets vtpVlanEditOperation to 'release'.
                
                Note that the information contained in this table is not
                saved across agent reboots.
                ''',
                'vtpvlanedittable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanLocalShutdownTable', REFERENCE_CLASS, 'Vtpvlanlocalshutdowntable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlanlocalshutdowntable', 
                [], [], 
                '''                Ths table contains the VLAN local shutdown
                information within management domain.
                ''',
                'vtpvlanlocalshutdowntable',
                'CISCO-VTP-MIB', False),
            _MetaInfoClassMember('vtpVlanTable', REFERENCE_CLASS, 'Vtpvlantable' , 'ydk.models.cisco_ios_xe.CISCO_VTP_MIB', 'CiscoVtpMib.Vtpvlantable', 
                [], [], 
                '''                This table contains information on the VLANs which
                currently exist.
                ''',
                'vtpvlantable',
                'CISCO-VTP-MIB', False),
            ],
            'CISCO-VTP-MIB',
            'CISCO-VTP-MIB',
            _yang_ns._namespaces['CISCO-VTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VTP_MIB'
        ),
    },
}
_meta_table['CiscoVtpMib.Managementdomaintable.Managementdomainentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Managementdomaintable']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlantable.Vtpvlanentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpvlantable']['meta_info']
_meta_table['CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpinternalvlantable']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpvlanedittable']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpvlanlocalshutdowntable']['meta_info']
_meta_table['CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vlantrunkporttable']['meta_info']
_meta_table['CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpdiscovertable']['meta_info']
_meta_table['CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpdiscoverresulttable']['meta_info']
_meta_table['CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpdatabasetable']['meta_info']
_meta_table['CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry']['meta_info'].parent =_meta_table['CiscoVtpMib.Vtpauthenticationtable']['meta_info']
_meta_table['CiscoVtpMib.Vtpstatus']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Internalvlaninfo']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vlantrunkports']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vlanstatistics']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Managementdomaintable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlantable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpinternalvlantable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlanedittable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpvlanlocalshutdowntable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vlantrunkporttable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpdiscovertable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpdiscoverresulttable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpdatabasetable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']
_meta_table['CiscoVtpMib.Vtpauthenticationtable']['meta_info'].parent =_meta_table['CiscoVtpMib']['meta_info']

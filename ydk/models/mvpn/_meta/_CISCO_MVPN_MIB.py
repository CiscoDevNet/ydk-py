


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateGroup', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                MDT group address in the BGP MDT advertisement.
                ''',
                'ciscomvpnbgpmdtupdategroup',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateSource', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                MDT source address in the BGP MDT advertisement.
                ''',
                'ciscomvpnbgpmdtupdatesource',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnBgpMdtUpdateGroup.
                ''',
                'ciscomvpnbgpmdtupdgrpaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdSrcAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnBgpMdtUpdateSource.
                ''',
                'ciscomvpnbgpmdtupdsrcaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateNexthop', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The next-hop address (address of the border router to be
                used to reach the destination network) in the BGP MDT 
                advertisement.
                ''',
                'ciscomvpnbgpmdtupdatenexthop',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateOriginator', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The BGP peering address of the device that originated (or 
                advertized) the BGP MDT update.
                ''',
                'ciscomvpnbgpmdtupdateoriginator',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateRd', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                RD (route distinguisher) in the BGP MDT advertisement. This 
                is the RD corresponding to the originator PE.
                ''',
                'ciscomvpnbgpmdtupdaterd',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdNhAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnBgpMdtUpdateNexthop.
                ''',
                'ciscomvpnbgpmdtupdnhaddrtype',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdOrigAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnBgpMdtUpdateOriginator.
                ''',
                'ciscomvpnbgpmdtupdorigaddrtype',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnBgpMdtUpdateEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateEntry', REFERENCE_LIST, 'CiscoMvpnBgpMdtUpdateEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry', 
                [], [], 
                '''                An entry in this table is created when a BGP advertisement of 
                the MDT group is received and cached in the PE device. 
                An entry in this table deleted when such a cached BGP MDT 
                update is withdrawn.
                ''',
                'ciscomvpnbgpmdtupdateentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnBgpMdtUpdateTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry.CiscoMvpnGenOperStatusChange_Enum' : _MetaInfoEnum('CiscoMvpnGenOperStatusChange_Enum', 'ydk.models.mvpn.CISCO_MVPN_MIB',
        {
            'createdMvrf':'CREATEDMVRF',
            'deletedMvrf':'DELETEDMVRF',
            'modifiedMvrfDefMdtConfig':'MODIFIEDMVRFDEFMDTCONFIG',
            'modifiedMvrfDataMdtConfig':'MODIFIEDMVRFDATAMDTCONFIG',
        }, 'CISCO-MVPN-MIB', _yang_ns._namespaces['CISCO-MVPN-MIB']),
    'CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnGenAssociatedInterfaces', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of interfaces associated with this MVRF (including
                the MDT tunnel interface) with ifOperStatus = up(1).
                ''',
                'ciscomvpngenassociatedinterfaces',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnGenOperChangeTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time at which the last operational change for the 
                MVRF in question took place. The last operational change
                is specified by ciscoMvpnGenOperStatusChange.
                ''',
                'ciscomvpngenoperchangetime',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnGenOperStatusChange', REFERENCE_ENUM_CLASS, 'CiscoMvpnGenOperStatusChange_Enum' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry.CiscoMvpnGenOperStatusChange_Enum', 
                [], [], 
                '''                This object describes the last operational change that
                happened for the given MVRF. 
                
                createdMvrf - indicates that the MVRF was created in the 
                device.
                
                deletedMvrf - indicates that the MVRF was deleted from 
                the device. A row in this table will never have 
                ciscoMvpnGenOperStatusChange equal to deletedMvrf(2),
                because in that case the row itself will be deleted 
                from the table. This value for 
                ciscoMvpnGenOperStatusChange is defined mainly for use 
                in ciscoMvpnMvrfChange notification.
                
                modifiedMvrfDefMdtConfig - indicates that the default MDT 
                group for the MVRF was configured, deleted or changed.
                
                modifiedMvrfDataMdtConfig - indicates that the data MDT 
                group range or a associated variable (like the threshold) 
                for the MVRF was configured, deleted or changed.
                ''',
                'ciscomvpngenoperstatuschange',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnGenRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This variable is used to create or delete a row in this table.
                ''',
                'ciscomvpngenrowstatus',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnGenericEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnGenericTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnGenericTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnGenericEntry', REFERENCE_LIST, 'CiscoMvpnGenericEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry', 
                [], [], 
                '''                An entry in this table is created for every MVRF in the 
                device. 
                Note that many implementations may have MVRF for global 
                VRF (VRF0) by default in the device.
                Also note that existence of the correspoding VRF in 
                L3VPN-MPLS-VPN-MIB is necessary for a row to exist in
                this table. Deletion of corresponding VRF in 
                L3VPN-MPLS-VPN-MIB also results in deletion of a row here. 
                But deletion of a row ie deletion of a MVRF here does not 
                result in the deletion of the corresponding VRF in 
                L3VPN-MPLS-VPN-MIB.
                ''',
                'ciscomvpngenericentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnGenericTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtDataRangeAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The data MDT group range address for the given MVRF. 
                This along with ciscoMvpnMdtDataWildcardBits gives the 
                pool of data MDT addresses that can be used for
                encapsulation in the MVRF upon data MDT switchover.
                ''',
                'ciscomvpnmdtdatarangeaddress',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataRangeAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtDataRangeAddress.
                ''',
                'ciscomvpnmdtdatarangeaddrtype',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This variable is used to create, modify or delete a 
                row in this table.
                ''',
                'ciscomvpnmdtdatarowstatus',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bandwidth threshold value which when exceeded for a 
                multicast routing entry in the given MVRF, triggers usage 
                of data MDT address instead of default MDT address for 
                encapsulation.
                ''',
                'ciscomvpnmdtdatathreshold',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataWildcardBits', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Wildcard bits which when used along with data MDT range 
                address, give a pool of addresses to be used in a MVRF.
                
                For example, if ciscoMvpnMdtDataRangeAddress is 239.1.2.0 
                and ciscoMvpnMdtDataWildcardBits is 0.0.0.3, the possible 
                data MDT addresses are 239.1.2.0, 239.1.2.1, 239.1.2.2 
                and 239.1.2.3.
                
                Note that wild card bits should be right contiguous.
                ''',
                'ciscomvpnmdtdatawildcardbits',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataWildcardType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtDataWildcardBits.
                ''',
                'ciscomvpnmdtdatawildcardtype',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtDataEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtDataTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtDataTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtDataEntry', REFERENCE_LIST, 'CiscoMvpnMdtDataEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry', 
                [], [], 
                '''                An entry in this table is created for every MVRF for which 
                a data MDT group range is configured. A MVRF which does
                not have a data MDT group range configured will not appear
                in this table. 
                Creation of a row in this table is the equivalent of 
                configuring data MDT addresses for the given MVRF. Deletion 
                of a row in this table is the equivalent of deconfiguring 
                data MDT address usage in the given MVRF. 
                
                Note that ciscoMvpnMdtDefaultEntry for a MVRF should be 
                present in the device before ciscoMvpnMdtDataEntry for 
                that MVRF can be created.
                ''',
                'ciscomvpnmdtdataentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtDataTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry.CiscoMvpnMdtEncapsType_Enum' : _MetaInfoEnum('CiscoMvpnMdtEncapsType_Enum', 'ydk.models.mvpn.CISCO_MVPN_MIB',
        {
            'greIp':'GREIP',
            'ipIp':'IPIP',
            'mpls':'MPLS',
        }, 'CISCO-MVPN-MIB', _yang_ns._namespaces['CISCO-MVPN-MIB']),
    'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtDefaultAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The default MDT address to be used for the MVRF in question.
                ''',
                'ciscomvpnmdtdefaultaddress',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDefaultAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtDefaultAddress.
                ''',
                'ciscomvpnmdtdefaultaddrtype',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDefaultRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This variable is used to create, modify or delete a 
                row in this table.
                ''',
                'ciscomvpnmdtdefaultrowstatus',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtEncapsType', REFERENCE_ENUM_CLASS, 'CiscoMvpnMdtEncapsType_Enum' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry.CiscoMvpnMdtEncapsType_Enum', 
                [], [], 
                '''                The encapsulation type to be used in the MVRF in question.
                ''',
                'ciscomvpnmdtencapstype',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtDefaultEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtDefaultTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtDefaultEntry', REFERENCE_LIST, 'CiscoMvpnMdtDefaultEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry', 
                [], [], 
                '''                An entry in this table is created for every MVRF for which 
                a default MDT group is configured. A MVRF which does not 
                have a default MDT group configured will not appear in 
                this table.
                Creation of a row in this table is the equivalent of 
                configuring default MDT address for the given MVRF. 
                Deletion of a row in this table is the equivalent of 
                deconfiguring default MDT address for the given MVRF.
                ''',
                'ciscomvpnmdtdefaultentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtDefaultTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvGroup', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                Data MDT group address in the MDT join TLV.
                ''',
                'ciscomvpnmdtjnrcvgroup',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtJnRcvGroup.
                ''',
                'ciscomvpnmdtjnrcvgrpaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvSource', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                Source address for the MDT multicast routing entry created 
                following the receipt of MDT join TLV.
                ''',
                'ciscomvpnmdtjnrcvsource',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvSrcAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtJnRcvSource.
                ''',
                'ciscomvpnmdtjnrcvsrcaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvExpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The amount of time remaining before the cache corresponding 
                to this MDT join TLV is deleted from the device and the 
                corresponding  MDT multicast routing entry is marked as a 
                non-MDT entry.
                Note that multiple TLVs for a data MDT group may be received 
                by a device. Upon receipt, the expiry timer of an already 
                existing entry is restarted and so ciscoMvpnMdtJnRcvExpTime 
                is updated.
                ''',
                'ciscomvpnmdtjnrcvexptime',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The time since this MDT join TLV was first received by the 
                device.
                ''',
                'ciscomvpnmdtjnrcvuptime',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtJnRcvEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvEntry', REFERENCE_LIST, 'CiscoMvpnMdtJnRcvEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry', 
                [], [], 
                '''                An entry in this table is created or updated for every MDT 
                data join TLV received and cached in the device. The value of 
                mplsVpnVrfName in such an entry specifies the name of the 
                MVRF for which the data MDT groups from the TLVs are used.
                ''',
                'ciscomvpnmdtjnrcventry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtJnRcvTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtJnSendGroup', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                This indicates the address of a multicast group in the 
                MVRF specified by the column mplsVpnVrfName. This along 
                with ciscoMvpnMdtJnSendSource identifies the multicast 
                routing entry for which the MDT join TLV is sent.
                ''',
                'ciscomvpnmdtjnsendgroup',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtJnSendGroup.
                ''',
                'ciscomvpnmdtjnsendgrpaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendSource', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                This indicates the address of a source in the MVRF 
                specified by the column mplsVpnVrfName. This, along with 
                ciscoMvpnMdtJnSendGroup identifies the multicast routing entry
                for which the MDT join TLV is sent.
                ''',
                'ciscomvpnmdtjnsendsource',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendSrcAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtJnSendSource.
                ''',
                'ciscomvpnmdtjnsendsrcaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendMdtGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The data MDT group in the MDT Join TLV sent.
                ''',
                'ciscomvpnmdtjnsendmdtgroup',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendMdtGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMdtJnSendMdtGroup.
                ''',
                'ciscomvpnmdtjnsendmdtgrpaddrtype',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendMdtRefCt', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Indicates how many multicast routing entries in the MVRF 
                specified by the column mplsVpnVrfName are using 
                ciscoMvpnMdtJnSendMdtGroup for encapsulation.
                ''',
                'ciscomvpnmdtjnsendmdtrefct',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtJnSendEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMdtJnSendTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMdtJnSendTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMdtJnSendEntry', REFERENCE_LIST, 'CiscoMvpnMdtJnSendEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry', 
                [], [], 
                '''                Entries in this table exist for data MDT Join TLVs that are 
                being sent by this device to other PEs.
                ''',
                'ciscomvpnmdtjnsendentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMdtJnSendTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteMdtType_Enum' : _MetaInfoEnum('CiscoMvpnMrouteMdtType_Enum', 'ydk.models.mvpn.CISCO_MVPN_MIB',
        {
            'mdtDefault':'MDTDEFAULT',
            'mdtData':'MDTDATA',
        }, 'CISCO-MVPN-MIB', _yang_ns._namespaces['CISCO-MVPN-MIB']),
    'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteUpDownStreamInfo_Enum' : _MetaInfoEnum('CiscoMvpnMrouteUpDownStreamInfo_Enum', 'ydk.models.mvpn.CISCO_MVPN_MIB',
        {
            'upstream':'UPSTREAM',
            'downstream':'DOWNSTREAM',
        }, 'CISCO-MVPN-MIB', _yang_ns._namespaces['CISCO-MVPN-MIB']),
    'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMrouteMvrfGroup', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                Group adddress of multicast routing entry in question.
                ''',
                'ciscomvpnmroutemvrfgroup',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMrouteMvrfGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMrouteMvrfGroup.
                ''',
                'ciscomvpnmroutemvrfgrpaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMrouteMvrfSource', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None), (20, None)], [], 
                '''                Source adddress of the multicast routing entry in question.
                ''',
                'ciscomvpnmroutemvrfsource',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMrouteMvrfSrcAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMrouteMvrfSource.
                ''',
                'ciscomvpnmroutemvrfsrcaddrtype',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMrouteUpDownStreamInfo', REFERENCE_ENUM_CLASS, 'CiscoMvpnMrouteUpDownStreamInfo_Enum' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteUpDownStreamInfo_Enum', 
                [], [], 
                '''                Indicates if this PE is the upstream (sending) or the 
                downstream (receiving) router for the multicast routing entry 
                specified by ciscoMvpnMrouteMvrfSource and 
                ciscoMvpnMrouteMvrfGroup in the context MVRF specified by 
                mplsVpnVrfName.
                Note that there may be two rows for the same multicast 
                routing entry if the traffic is bi-directional, one row 
                for PE as an upstream router the other for PE as the 
                downstream router.
                ''',
                'ciscomvpnmrouteupdownstreaminfo',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnMrouteMdtGroup', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                MDT group address used to encapsulate the multicast routing 
                entry specified by ciscoMvpnMrouteMvrfSource and 
                ciscoMvpnMrouteMvrfGroup in the context MVRF specified by 
                mplsVpnVrfName.
                ''',
                'ciscomvpnmroutemdtgroup',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMrouteMdtGrpAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Internet address type of ciscoMvpnMrouteMdtGroup.
                ''',
                'ciscomvpnmroutemdtgrpaddrtype',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMrouteMdtType', REFERENCE_ENUM_CLASS, 'CiscoMvpnMrouteMdtType_Enum' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry.CiscoMvpnMrouteMdtType_Enum', 
                [], [], 
                '''                Indicates the type of MDT group used for encapsulation.
                ''',
                'ciscomvpnmroutemdttype',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMrouteMdtEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnMrouteMdtTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMrouteMdtEntry', REFERENCE_LIST, 'CiscoMvpnMrouteMdtEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry', 
                [], [], 
                '''                An entry in this table exists for a multicast routing entry 
                the traffic for which is being encapsulated in a context 
                MVRF.
                ''',
                'ciscomvpnmroutemdtentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnMrouteMdtTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnScalars' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnScalars',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnMvrfNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of MVRFs that are present in this device.
                ''',
                'ciscomvpnmvrfnumber',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is TRUE, then the generation of 
                all notifications defined in this MIB is enabled.
                ''',
                'ciscomvpnnotificationenable',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnScalars',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-MVPN-MIB', True),
            _MetaInfoClassMember('ciscoMvpnTunnelMvrf', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                Name of the MVRF that this tunnel is associated with.
                This object has the same value as mplsVpnVrfName
                for the MVRF.
                ''',
                'ciscomvpntunnelmvrf',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnTunnelName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The canonical name assigned to the tunnel. The ifName of 
                this tunnel interface should have a value equal to 
                ciscoMvpnTunnelName.
                ''',
                'ciscomvpntunnelname',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnTunnelEntry',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB.CiscoMvpnTunnelTable' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB.CiscoMvpnTunnelTable',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnTunnelEntry', REFERENCE_LIST, 'CiscoMvpnTunnelEntry' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry', 
                [], [], 
                '''                An entry in this table is created for every MVPN tunnel 
                interface present in the device. The ifType for a MVPN
                tunnel is 'tunnel' (131). 
                (A MVPN tunnel interface should have relevant generic 
                support in the IF-MIB and in the internet draft,
                draft-thaler-inet-tunnel-mib. Only MVPN specific aspects
                of such a tunnel interface are to be specified in this
                table.)
                ''',
                'ciscomvpntunnelentry',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'ciscoMvpnTunnelTable',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
    'CISCOMVPNMIB' : {
        'meta_info' : _MetaInfoClass('CISCOMVPNMIB',
            False, 
            [
            _MetaInfoClassMember('ciscoMvpnBgpMdtUpdateTable', REFERENCE_CLASS, 'CiscoMvpnBgpMdtUpdateTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable', 
                [], [], 
                '''                This table has information about the BGP advertisement of the 
                the MDT groups. (These advertisements are generated 
                and used for source discovery when SSM is used.)
                ''',
                'ciscomvpnbgpmdtupdatetable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnGenericTable', REFERENCE_CLASS, 'CiscoMvpnGenericTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnGenericTable', 
                [], [], 
                '''                This table gives the generic information about the MVRFs 
                present in this device.
                ''',
                'ciscomvpngenerictable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDataTable', REFERENCE_CLASS, 'CiscoMvpnMdtDataTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtDataTable', 
                [], [], 
                '''                This table specifies the range of data MDT addresses and 
                associated variables for a MVRF instance.
                ''',
                'ciscomvpnmdtdatatable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtDefaultTable', REFERENCE_CLASS, 'CiscoMvpnMdtDefaultTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtDefaultTable', 
                [], [], 
                '''                This table specifies the default MDT address and the 
                encapsulation type used for a MVRF instance.
                ''',
                'ciscomvpnmdtdefaulttable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtJnRcvTable', REFERENCE_CLASS, 'CiscoMvpnMdtJnRcvTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable', 
                [], [], 
                '''                This table has information about the data MDT join TLVs 
                received by a device.
                ''',
                'ciscomvpnmdtjnrcvtable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMdtJnSendTable', REFERENCE_CLASS, 'CiscoMvpnMdtJnSendTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMdtJnSendTable', 
                [], [], 
                '''                This table specifies the data MDT Join TLVs sent by a 
                device.
                ''',
                'ciscomvpnmdtjnsendtable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnMrouteMdtTable', REFERENCE_CLASS, 'CiscoMvpnMrouteMdtTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnMrouteMdtTable', 
                [], [], 
                '''                Given a multicast routing entry and the context MVRF, this 
                table provides information about the MDT group being used for 
                encapsulating the traffic for the multicast routing entry in 
                the provider network at the instance of querying. Note that
                this table is a read-only table and is the result of the 
                default MDT and data MDT configurations and the operational 
                conditions like the traffic rate and sometimes, the 
                implementation choices.
                ''',
                'ciscomvpnmroutemdttable',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnScalars', REFERENCE_CLASS, 'CiscoMvpnScalars' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnScalars', 
                [], [], 
                '''                ''',
                'ciscomvpnscalars',
                'CISCO-MVPN-MIB', False),
            _MetaInfoClassMember('ciscoMvpnTunnelTable', REFERENCE_CLASS, 'CiscoMvpnTunnelTable' , 'ydk.models.mvpn.CISCO_MVPN_MIB', 'CISCOMVPNMIB.CiscoMvpnTunnelTable', 
                [], [], 
                '''                This table gives information about the MVPN/MDT tunnels 
                present in the device.
                ''',
                'ciscomvpntunneltable',
                'CISCO-MVPN-MIB', False),
            ],
            'CISCO-MVPN-MIB',
            'CISCO-MVPN-MIB',
            _yang_ns._namespaces['CISCO-MVPN-MIB'],
        'ydk.models.mvpn.CISCO_MVPN_MIB'
        ),
    },
}
_meta_table['CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable.CiscoMvpnBgpMdtUpdateEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable.CiscoMvpnGenericEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDataTable.CiscoMvpnMdtDataEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDataTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable.CiscoMvpnMdtDefaultEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable.CiscoMvpnMdtJnRcvEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnSendTable.CiscoMvpnMdtJnSendEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnSendTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable.CiscoMvpnMrouteMdtEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnTunnelTable.CiscoMvpnTunnelEntry']['meta_info'].parent =_meta_table['CISCOMVPNMIB.CiscoMvpnTunnelTable']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnBgpMdtUpdateTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnGenericTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDataTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtDefaultTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnRcvTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMdtJnSendTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnMrouteMdtTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnScalars']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']
_meta_table['CISCOMVPNMIB.CiscoMvpnTunnelTable']['meta_info'].parent =_meta_table['CISCOMVPNMIB']['meta_info']

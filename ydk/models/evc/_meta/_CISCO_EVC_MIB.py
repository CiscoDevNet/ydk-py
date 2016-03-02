


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ServiceInstanceTargetType_Enum' : _MetaInfoEnum('ServiceInstanceTargetType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'other':'OTHER',
            'interface':'INTERFACE',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CevcL2ControlProtocolType_Enum' : _MetaInfoEnum('CevcL2ControlProtocolType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'other':'OTHER',
            'cdp':'CDP',
            'dtp':'DTP',
            'pagp':'PAGP',
            'udld':'UDLD',
            'vtp':'VTP',
            'lacp':'LACP',
            'dot1x':'DOT1X',
            'stp':'STP',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CevcMacSecurityViolationCauseType_Enum' : _MetaInfoEnum('CevcMacSecurityViolationCauseType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'exceedSystemLimit':'EXCEEDSYSTEMLIMIT',
            'exceedBdLimit':'EXCEEDBDLIMIT',
            'exceedSILimit':'EXCEEDSILIMIT',
            'blackListDeny':'BLACKLISTDENY',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcEvcNotificationConfig' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcNotificationConfig',
            False, 
            [
            _MetaInfoClassMember('cevcEvcNotifyEnabled', REFERENCE_BITS, 'CevcEvcNotifyEnabled_Bits' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcNotificationConfig.CevcEvcNotifyEnabled_Bits', 
                [], [], 
                '''                This object specifies the system generation of notification,
                including:
                
                    'status'
                        This bit set to '1' specifies the system 
                        generation of cevcEvcStatusChangedNotification.
                
                
                    'creation'
                        This bit set to '1' specifies the system
                       generation of cevcEvcCreationNotification.
                
                
                    'deletion'
                        This bit set to '1' specifices the system
                        generation of cevcEvcDeletionNotification.
                        
                    'macSecurityViolation'
                      This bit set to '1' specifies the system 
                      generation of cevcMacSecurityViolation.
                ''',
                'cevcevcnotifyenabled',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcNotificationConfig',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry.CevcEvcOperStatus_Enum' : _MetaInfoEnum('CevcEvcOperStatus_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'unknown':'UNKNOWN',
            'active':'ACTIVE',
            'partiallyActive':'PARTIALLYACTIVE',
            'inactive':'INACTIVE',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry',
            False, 
            [
            _MetaInfoClassMember('cevcEvcIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcevcindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcEvcActiveUnis', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the number of active UNIs for the EVC
                in the MEN.  This value is derived from data gathered by 
                underlying OAM Protocol.
                ''',
                'cevcevcactiveunis',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcOperStatus', REFERENCE_ENUM_CLASS, 'CevcEvcOperStatus_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry.CevcEvcOperStatus_Enum', 
                [], [], 
                '''                This object specifies the operational status of the EVC:
                
                
                'unknown'
                    Not enough information available regarding the EVC to
                    determine the operational status at this time or EVC 
                    operational status is undefined.
                
                'active'
                    Fully operational between the UNIs in the EVC.  
                
                
                'partiallyActive'
                    Capable of transferring traffic among some but not all
                    of the UNIs in the EVC.  This operational status is
                    applicable only for Multipoint-to-Multipoint EVCs.
                
                
                'inactive'
                    Not capable of transferring traffic among any of the
                    UNIs in the EVC.  
                
                This value is derived from data gathered by underlying OAM
                protocol.
                ''',
                'cevcevcoperstatus',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcStateEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcStateTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcStateTable',
            False, 
            [
            _MetaInfoClassMember('cevcEvcStateEntry', REFERENCE_LIST, 'CevcEvcStateEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry', 
                [], [], 
                '''                This entry represents status atrributes of an EVC.
                
                The system automatically creates an entry when the system or
                the EMS/NMS creates a row in the cevcEvcTable.  Likewise, the
                system automatically destroys an entry when the system or the
                EMS/NMS destroys the corresponding row in the cevcEvcTable.
                ''',
                'cevcevcstateentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcStateTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcTable.CevcEvcEntry.CevcEvcType_Enum' : _MetaInfoEnum('CevcEvcType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'pointToPoint':'POINTTOPOINT',
            'multipointToMultipoint':'MULTIPOINTTOMULTIPOINT',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcEvcTable.CevcEvcEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcTable.CevcEvcEntry',
            False, 
            [
            _MetaInfoClassMember('cevcEvcIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates an arbitrary integer-value that uniquely
                identifies the EVC.
                ''',
                'cevcevcindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcEvcCfgUnis', ATTRIBUTE, 'int' , None, None, 
                [(2, 4294967295)], [], 
                '''                This object specifies the number of UNIs expected to be
                configured for the EVC in the MEN.  The underlying OAM
                protocol can use this value of UNIs to determine the EVC
                operational status, cevcEvcOperStatus.  For a 
                Multipoint-to-Multipoint EVC the minimum number of Uni's
                would be two.
                ''',
                'cevcevccfgunis',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                This object specifies a string-value identifying the EVC.
                This value should be unique across the MEN.
                ''',
                'cevcevcidentifier',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and
                delete rows in the cevcEvcTable. 
                
                cevcEvcIdentifier column must have a valid value before a 
                row can be set to 'active'.
                
                Writable objects in this table can be modified while the
                value of cevcEvcRowStatus column is 'active'.
                
                An entry cannot be deleted if there exists a service instance
                which is referring to the cevcEvcEntry i.e. cevcSIEvcIndex
                in the cevcSITable has the same value as cevcEvcIndex being
                deleted.
                ''',
                'cevcevcrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcevcstoragetype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcType', REFERENCE_ENUM_CLASS, 'CevcEvcType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcTable.CevcEvcEntry.CevcEvcType_Enum', 
                [], [], 
                '''                This object specifies the type of EVC:
                
                
                'pointToPoint' 
                    Exactly two UNIs are associated with one another.  An
                    ingress service frame at one UNI must not result in an
                    egress service frame at a UNI other than the other UNI
                    in the EVC.
                
                
                'multipointToMultipoint'
                    Two or more UNIs are associated with one another.  An
                    ingress service frame at one UNI must not result in an
                    egress service frame at a UNI that is not in the EVC.
                ''',
                'cevcevctype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcTable',
            False, 
            [
            _MetaInfoClassMember('cevcEvcEntry', REFERENCE_LIST, 'CevcEvcEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcTable.CevcEvcEntry', 
                [], [], 
                '''                This entry represents the EVC configured on the system and
                its service atrributes.
                
                Entries in this table may be created and deleted via the
                cevcEvcRowStatus object or the management console on the
                system.
                
                Using SNMP, rows are created by a SET request setting the value
                of cevcEvcRowStatus column to 'createAndGo'or 'createAndWait'. 
                Rows are deleted by a SET request setting the value of
                cevcEvcRowStatus column to 'destroy'.
                ''',
                'cevcevcentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry.CevcEvcUniOperStatus_Enum' : _MetaInfoEnum('CevcEvcUniOperStatus_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'unknown':'UNKNOWN',
            'notReachable':'NOTREACHABLE',
            'up':'UP',
            'down':'DOWN',
            'adminDown':'ADMINDOWN',
            'localExcessiveError':'LOCALEXCESSIVEERROR',
            'remoteExcessiveError':'REMOTEEXCESSIVEERROR',
            'localInLoopback':'LOCALINLOOPBACK',
            'remoteInLoopback':'REMOTEINLOOPBACK',
            'localOutLoopback':'LOCALOUTLOOPBACK',
            'remoteOutLoopback':'REMOTEOUTLOOPBACK',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry',
            False, 
            [
            _MetaInfoClassMember('cevcEvcIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcevcindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcEvcUniIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates an arbitrary integer-value that uniquely
                
                identifies the UNI in an EVC.
                ''',
                'cevcevcuniindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcEvcLocalUniIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                When the UNI is local on the system, this object specifies
                the ifIndex of the UNI.  The value '0' of this column
                indicates remote UNI.
                ''',
                'cevcevclocaluniifindex',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcUniId', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object indicates the string-value identifying the UNI
                that is in the EVC.  For UNI that is local, this value is the
                same as cevcUniIdentifier for the same ifIndex value as 
                cevcEvcLocalUniIfIndex.  For UNI that is not on the system, 
                this value may be derived from the underlying OAM protocol.
                
                If the UNI identifier value is not specified for the UNI or it
                is unknown, the value of the cevcEvcUniId column is a
                zero-length string.
                ''',
                'cevcevcuniid',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcUniOperStatus', REFERENCE_ENUM_CLASS, 'CevcEvcUniOperStatus_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry.CevcEvcUniOperStatus_Enum', 
                [], [], 
                '''                This object indicates the operational status derived from data
                gathered by the OAM protocol for an UNI.
                
                
                    'unknown' 
                        Status is not known; possible reason could be caused
                        by the OAM protocol has not provided information
                        regarding the UNI.
                
                
                    'notReachable'
                        UNI is not reachable; possible reason could be caused
                        by the OAM protocol messages having not been received
                        for an excessive length of time.
                
                
                    'up'
                        UNI is active, up, and able to pass traffic.
                
                
                    'down'
                        UNI is down and not passing traffic.
                
                
                    'adminDown'
                        UNI has been administratively put in down state.
                
                
                    'localExcessiveError'
                        UNI has experienced excessive number of invalid frames
                        on the local end of the physical link between UNI-C 
                        and UNI-N.
                
                
                    'remoteExcessiveError'
                        UNI has experienced excessive number of invalid frames
                        on the remote side of the physical connection between
                        UNI-C and UNI-N.
                
                
                    'localInLoopback'
                        UNI is loopback on the local end of the physical link
                        between UNI-C and UNI-N.
                
                
                    'remoteInLoopback'
                        UNI is looped back on the remote end of the link 
                        between UNI-C and UNI-N.
                
                
                    'localOutLoopback'
                        UNI just transitioned out of loopback on the local end
                        of the physcial link between UNI-C and UNI-N.
                
                    'remoteOutLoopback'
                        UNI just transitioned out of loopback on the remote 
                        end of the physcial link between UNI-C and UNI-N.
                ''',
                'cevcevcunioperstatus',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcUniEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcEvcUniTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcEvcUniTable',
            False, 
            [
            _MetaInfoClassMember('cevcEvcUniEntry', REFERENCE_LIST, 'CevcEvcUniEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry', 
                [], [], 
                '''                This entry represents a UNI, either local or remote, in the
                EVC.
                
                The system automatically creates an entry, when an UNI is
                attached to the EVC.  Entries are automatically destroyed
                when the system or the EMS/NMS destroys the corresponding 
                row in the cevcEvcTable or when an UNI is removed from the
                EVC.
                ''',
                'cevcevcunientry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcEvcUniTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcMacSecurityViolation' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcMacSecurityViolation',
            False, 
            [
            _MetaInfoClassMember('cevcMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                This object indicates the MAC Address which has violated
                the Mac security rules.
                ''',
                'cevcmacaddress',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcMaxMacConfigLimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the maximum MAC configuration limit. This
                is also sent as a part of MAC security violation notification.
                Every platform has their own forwarding table limitation. User 
                can also set the maximum MAC configuration limit and if the 
                limit set by user is not supported by platform then the object
                returns error.
                ''',
                'cevcmaxmacconfiglimit',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIID', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This object indicates the service instance ID for the MAC
                security violation notification.
                ''',
                'cevcsiid',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcViolationCause', REFERENCE_ENUM_CLASS, 'CevcMacSecurityViolationCauseType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CevcMacSecurityViolationCauseType_Enum', 
                [], [], 
                '''                This object indicates the MAC security violation cause.
                
                When the system MAC Address limit is exceeded, the
                cevcMacSecurityViolationCause will contain
                'exceedSystemLimit' value.
                
                When the Bridge domain limit is exceeded, the
                cevcMacSecurityViolationCause will contain
                'exceedBdLimit' value.
                
                When the Service Instance limit is exceeded, the
                cevcMacSecurityViolationCause will contain
                'exceedSILimit' value.
                
                If the MAC address is present in the Black list
                then cevcMacSecurityViolationCause will contain
                'blackListDeny' value.
                ''',
                'cevcviolationcause',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcMacSecurityViolation',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry.CevcPortL2ControlProtocolAction_Enum' : _MetaInfoEnum('CevcPortL2ControlProtocolAction_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'discard':'DISCARD',
            'peer':'PEER',
            'passToEvc':'PASSTOEVC',
            'peerAndPassToEvc':'PEERANDPASSTOEVC',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry',
            False, 
            [
            _MetaInfoClassMember('cevcPortL2ControlProtocolType', REFERENCE_ENUM_CLASS, 'CevcL2ControlProtocolType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CevcL2ControlProtocolType_Enum', 
                [], [], 
                '''                This object indicates the type of layer 2 control
                protocol service frame as denoted by the value of 
                cevcPortL2ControlProtocolAction column.
                ''',
                'cevcportl2controlprotocoltype',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcPortL2ControlProtocolAction', REFERENCE_ENUM_CLASS, 'CevcPortL2ControlProtocolAction_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry.CevcPortL2ControlProtocolAction_Enum', 
                [], [], 
                '''                This object specifies the action to be taken for the given
                layer 2 control protocol service frames which matches the 
                cevcPortL2ControlProtocolType, including:
                
                
                    'discard' 
                        The port must discard all ingress service frames
                        carrying the layer 2 control protocol service
                        frames and the port must not generate any egress
                        service frames carrying the layer 2 control protocol
                        service frames.  When this action is set at the port,
                        an EVC cannot process the layer 2 control protocol
                        service frames.
                
                
                    'peer' 
                        The port must act as a peer, meaning it actively
                        participates with the Customer Equipment, in the
                        operation of the layer 2 control protocol service
                        frames.  An example of this is port authentication
                        service at the UNI with 802.1x or enhanced link OAM
                        functionality by peering at the UNI with link OAM
                        (IEEE 802.3ah).  When this action is set at the port,
                        an EVC cannot process the layer 2 control protocol
                        service frames.
                
                
                    'passToEvc'
                        The disposition of the service frames which are layer 2
                        control protocol service frames must be determined by
                        the layer 2 control protocol action attribute of the
                        EVC, (see cevcSIL2ControlProtocolAction for further
                        details).
                
                
                    'peerAndPassToEvc' 
                        The layer 2 control protocol service frames will be
                        peered at the port and also passed to one or more EVCs
                        for tunneling.  An example of this possibility is where
                        an 802.1x authentication frame is peered at the UNI for
                        UNI-based authentication, but also passed to a given
                        EVC for customer end-to-end authentication.
                ''',
                'cevcportl2controlprotocolaction',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcPortL2ControlProtocolEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcPortL2ControlProtocolTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcPortL2ControlProtocolTable',
            False, 
            [
            _MetaInfoClassMember('cevcPortL2ControlProtocolEntry', REFERENCE_LIST, 'CevcPortL2ControlProtocolEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry', 
                [], [], 
                '''                This entry represents the layer 2 control protocol processing
                at the UNI.
                
                The system automatically creates an entry for each layer 2
                control protocol type when an entry is created in the
                cevcUniTable, and entries are automatically destroyed when the
                system destroys the corresponding row in the cevcUniTable.
                ''',
                'cevcportl2controlprotocolentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcPortL2ControlProtocolTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcPortTable.CevcPortEntry.CevcPortMode_Enum' : _MetaInfoEnum('CevcPortMode_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'uni':'UNI',
            'nni':'NNI',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcPortTable.CevcPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcPortTable.CevcPortEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcPortMaxNumEVCs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the maximum number of EVCs that the
                interface can support.
                ''',
                'cevcportmaxnumevcs',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcPortMaxNumServiceInstances', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the maximum number of service instances
                that the interface can support.
                ''',
                'cevcportmaxnumserviceinstances',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcPortMode', REFERENCE_ENUM_CLASS, 'CevcPortMode_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortTable.CevcPortEntry.CevcPortMode_Enum', 
                [], [], 
                '''                Port denotes the physcial interface which can provide
                Ethernet services.  This object indicates the mode of the
                port and its operational behaviour in the MEN. 
                
                
                   'uni'
                       User Network Interface
                       The port resides on the interface between the end user
                       and the network.  Additional information related
                       to the UNI is included in cevcUniTable.
                
                
                    'nni'
                        Network to Network Interface.  The port resides on the
                        interface between two networks.
                ''',
                'cevcportmode',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcPortEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcPortTable',
            False, 
            [
            _MetaInfoClassMember('cevcPortEntry', REFERENCE_LIST, 'CevcPortEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortTable.CevcPortEntry', 
                [], [], 
                '''                This entry represents a port, a physical point, at which
                signals can enter or leave the network en route to or from
                another network to provide Ethernet services for the MEN.
                
                The system automatically creates an entry for each ifEntry in
                the ifTable having an ifType of 'ethernetCsmacd' capable of
                supporting Ethernet services and entries are automatically
                destroyed when the corresponding row in the ifTable is
                destroyed.
                ''',
                'cevcportentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcPortTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSICEVlanBeginningVlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                If cevcSICEVlanEndingVlan is '0', then this object
                indicates a single VLAN in the list.
                
                If cevcSICEVlanEndingVlan is not '0', then this object
                indicates the first VLAN in a range of VLANs.
                ''',
                'cevcsicevlanbeginningvlan',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSICEVlanEndingVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                This object indicates the last VLAN in a range of VLANs.  If
                the row does not describe a range, then the value of this
                column must be '0'.
                ''',
                'cevcsicevlanendingvlan',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSICEVlanRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSICEVlanTable.
                
                This object cannot be set to 'active' until all objects have 
                been assigned valid values.
                
                Writable objects in this table can be modified while the
                value of the cevcSICEVlanRowStatus column is 'active'.
                ''',
                'cevcsicevlanrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSICEVlanStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsicevlanstoragetype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSICEVlanEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSICEVlanTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSICEVlanTable',
            False, 
            [
            _MetaInfoClassMember('cevcSICEVlanEntry', REFERENCE_LIST, 'CevcSICEVlanEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry', 
                [], [], 
                '''                This entry contains the CE-VLANs that are mapped at a Service
                Instance.
                
                Entries in this table may be created and deleted via the
                cevcSICEVlanRowStatus object or the management console on the
                system.
                
                Using SNMP, rows are created by a SET request setting the value
                of cevcSICEVlanRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of cevcSICEVlanRowStatus column to 'destroy'.
                ''',
                'cevcsicevlanentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSICEVlanTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry.CevcSIForwardBdNumberBase_Enum' : _MetaInfoEnum('CevcSIForwardBdNumberBase_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'bdNumBase0':'BDNUMBASE0',
            'bdNumBase4096':'BDNUMBASE4096',
            'bdNumBase8192':'BDNUMBASE8192',
            'bdNumBase12288':'BDNUMBASE12288',
            'bdNumBase16384':'BDNUMBASE16384',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIForwardBdNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The bridge domain identifier that is associated with the
                service instance.
                
                A bridge domain refers to a layer 2 broadcast domain spanning
                a set of physical or virtual ports.  Frames are switched 
                Multicast and unknown destination unicast frames are flooded
                within the confines of the bridge domain.
                ''',
                'cevcsiforwardbdnumber',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdNumber1kBitmap', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object specifies a string of octets containing one bit 
                per Bridge domain per service instance(generally we have one
                bridge domain per nontrunk service instance but can have more
                than one bridge configured with a trunk service instance).
                The first octet corresponds to Bridge domains with 
                Bridge domain ID values of 0 through 7; the second octet to
                Bridge domains 8 through 15; etc. Thus, this 128-octet bitmap
                represents bridge domain ID value 0~1023.
                
                For each Bridge domain configured, the bit corresponding to
                that bridge domain is set to '1'. SNMP Administrator uses
                cevcSIForwardBdNumberBase + (position of the set bit in 
                bitmap)to calculate BD number of a service instance.
                
                Note that if the length of this string is less than 128 octets, 
                any 'missing' octets are assumed to contain the value zero. An 
                NMS may omit any zero-valued octets from the end of this string 
                in order to reduce SetPDU size, and the agent may also omit 
                zero-valued trailing octets, to reduce the size of GetResponse 
                PDUs.
                ''',
                'cevcsiforwardbdnumber1kbitmap',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdNumber2kBitmap', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object specifies a string of octets containing one bit 
                per Bridge domain per service instance(generally we have one
                bridge domain per nontrunk service instance but can have more
                than one bridge configured with a trunk service instance).
                The first octet corresponds to Bridge domains with 
                Bridge domain ID values of 1024 through 1031; the second 
                octet to Bridge domains 1032 through 1039; etc. Thus, this 
                128-octet bitmap represents bridge domain ID value 1024~2047.
                
                For each Bridge domain configured, the bit corresponding to
                that bridge domain is set to 1. SNMP Administrator uses
                cevcSIForwardBdNumberBase + (position of the set bit in 
                bitmap)to calculate BD number of a service instance.  
                
                Note that if the length of this string is less than 128 octets, 
                any 'missing' octets are assumed to contain the value zero. An 
                NMS may omit any zero-valued octets from the end of this string 
                in order to reduce SetPDU size, and the agent may also omit 
                zero-valued trailing octets, to reduce the size of GetResponse 
                PDUs.
                ''',
                'cevcsiforwardbdnumber2kbitmap',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdNumber3kBitmap', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object specifies a string of octets containing one bit
                per Bridge domain per service instance(generally we have one
                bridge domain per non-trunk service instance but can have more
                than one bridge configured with a trunk service instance).
                The first octet corresponds to Bridge domains with Bridgedomain
                ID values of 2048 through 2055; the second octet to Bridge 
                domains 2056 through 2063; etc. Thus, this 128-octet bitmap
                represents bridge domain ID value 2048~3071.
                
                For each Bridge domain configured, the bit corresponding to
                that bridge domain is set to 1. SNMP Administrator uses
                cevcSIForwardBdNumberBase + (position of the set bit in
                 bitmap)to calculate BD number of a service instance.  
                
                Note that if the length of this string is less than 128 octets, 
                any 'missing' octets are assumed to contain the value zero. An 
                NMS may omit any zero-valued octets from the end of this string 
                in order to reduce SetPDU size, and the agent may also omit 
                zero-valued trailing octets, to reduce the size of GetResponse 
                PDUs.
                ''',
                'cevcsiforwardbdnumber3kbitmap',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdNumber4kBitmap', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object specifies a string of octets containing one bit 
                per Bridge domain per service instance(generally we have one
                bridge domain per non-trunk service instance but can have more
                than one bridge configured with a trunk service instance).
                The first octet corresponds to Bridge domains with 
                Bridgedomain ID values of 3078 through 3085; the second octet 
                to Bridge domains 3086 through 3093; etc. Thus, this 128-octet
                 bitmap represents bridge domain ID value 3072~4095.
                
                For each Bridge domain configured, the bit corresponding to
                that bridge domain is set to 1. SNMP Administrator uses
                cevcSIForwardBdNumberBase + (position of the set bit in
                 bitmap)to calculate BD number of a service instance.  
                
                Note that if the length of this string is less than 128 octets, 
                any 'missing' octets are assumed to contain the value zero. An 
                NMS may omit any zero-valued octets from the end of this string 
                in order to reduce SetPDU size, and the agent may also omit 
                zero-valued trailing octets, to reduce the size of GetResponse 
                PDUs.
                ''',
                'cevcsiforwardbdnumber4kbitmap',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdNumberBase', REFERENCE_ENUM_CLASS, 'CevcSIForwardBdNumberBase_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry.CevcSIForwardBdNumberBase_Enum', 
                [], [], 
                '''                This object specifies the base of bridge domain. The bridge
                domain range is 1~16k, cevcSIForwardBdNumberBase is to track what
                is the base of each 4k bitmap. In this way we can specify all the 
                16k bridge domains using four 1k bitmaps and having the base which
                describes that is the base of each 4k bitmap. The four 1k bitmaps,
                cevcSIForwardBdNumber1kBitmap represents 0~1023,
                cevcSIForwardBdNumber2kBitmap represents 1024~2047,
                cevcSIForwardBdNumber3kBitmap represents 2048~3071,
                cevcSIForwardBdNumber4kBitmap represents 3072~4095
                And cevcSIForwardBdNumberBase is one of 0, 4096, 8192, 12288, 
                16384.
                SNMP Administrator can use cevcSIForwardBdNumberBase + (position 
                of the set bit in four 1k bitmaps) to get BD number of a 
                service instance.
                ''',
                'cevcsiforwardbdnumberbase',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSIForwardBdTable.
                
                This column can not be set to 'active' until all objects have 
                been assigned valid values.
                
                Writable objects in this table can be modified while the
                value of the cevcSIForwardBdRowStatus column is 'active'.
                ''',
                'cevcsiforwardbdrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsiforwardbdstoragetype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIForwardBdEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIForwardBdTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIForwardBdTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIForwardBdEntry', REFERENCE_LIST, 'CevcSIForwardBdEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry', 
                [], [], 
                '''                This entry represents an bridged domain used to forward service
                frames by the service instance.
                
                Entries in this table may be created and deleted via the
                cevcSIForwardBdRowStatus object or the management console
                on the system.
                
                Using SNMP, rows are created by a SET request setting the value
                of the cevcSIForwardBdRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of the cevcSIForwardBdRowStatus column to 'destroy'.
                ''',
                'cevcsiforwardbdentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIForwardBdTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry.CevcSIL2ControlProtocolAction_Enum' : _MetaInfoEnum('CevcSIL2ControlProtocolAction_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'discard':'DISCARD',
            'tunnel':'TUNNEL',
            'forward':'FORWARD',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIL2ControlProtocolType', REFERENCE_ENUM_CLASS, 'CevcL2ControlProtocolType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CevcL2ControlProtocolType_Enum', 
                [], [], 
                '''                The layer 2 control protocol service frame that the
                service instance is to process as defined by object
                cevcSIL2ControlProtocolAction.
                ''',
                'cevcsil2controlprotocoltype',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIL2ControlProtocolAction', REFERENCE_ENUM_CLASS, 'CevcSIL2ControlProtocolAction_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry.CevcSIL2ControlProtocolAction_Enum', 
                [], [], 
                '''                The actions to be taken for a given layer 2 control protocol
                service frames that matches cevcSIL2ControlProtocolType, 
                including:
                
                
                    'discard'
                        The MEN must discard all ingress service frames 
                        carrying the layer 2 control protocol service frames
                        on the EVC and the MEN must not generate any egress
                        service frames carrying the layer 2 control protocol
                        frames on the EVC.
                
                
                    'tunnel'
                        Forward the layer 2 control protocol service frames 
                        with the MAC address changed as defined by the
                        individual layer 2 control protocol.  The EVC does not
                        process the layer 2 protocol service frames.  If a 
                        layer 2 control protocol service frame is to be
                        tunneled, all the UNIs in the EVC must be configured to
                        pass the layer 2 control protocol service frames to the
                        EVC, cevcPortL2ControlProtocolAction column has the
                        value of 'passToEvc' or 'peerAndPassToEvc'.
                
                
                    'forward'
                        Forward the layer 2 conrol protocol service frames as
                        data; similar to tunnel but layer 2 control protocol
                        service frames are forwarded without changing the MAC
                        address.
                ''',
                'cevcsil2controlprotocolaction',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIL2ControlProtocolEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIL2ControlProtocolTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIL2ControlProtocolTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIL2ControlProtocolEntry', REFERENCE_LIST, 'CevcSIL2ControlProtocolEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry', 
                [], [], 
                '''                This entry represents the layer 2 control protocol processing
                at a service instance.
                
                The system automatically creates an entry for each layer 2
                control protocol type when an entry is created in the
                cevcSITable, and entries are automatically destroyed when the
                system destroys the corresponding row in the cevcSITable.
                ''',
                'cevcsil2controlprotocolentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIL2ControlProtocolTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry.CevcSIMatchCriteriaType_Enum' : _MetaInfoEnum('CevcSIMatchCriteriaType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'unknown':'UNKNOWN',
            'dot1q':'DOT1Q',
            'dot1ad':'DOT1AD',
            'untagged':'UNTAGGED',
            'untaggedAndDot1q':'UNTAGGEDANDDOT1Q',
            'untaggedAndDot1ad':'UNTAGGEDANDDOT1AD',
            'priorityTagged':'PRIORITYTAGGED',
            'defaultTagged':'DEFAULTTAGGED',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchCriteriaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates an arbitrary integer-value that uniquely
                identifies a match criteria for a service instance.
                ''',
                'cevcsimatchcriteriaindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchCriteriaType', REFERENCE_ENUM_CLASS, 'CevcSIMatchCriteriaType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry.CevcSIMatchCriteriaType_Enum', 
                [], [], 
                '''                This object specifies the criteria used to match a service
                instance.
                
                    'unknown'
                        Match criteria for the service instance is not
                        defined or unknown.
                
                
                    'dot1q'
                        The IEEE 802.1q encapsulation is used as a match
                        criteria for the service instance.  The ether type
                        value of the IEEE 802.1q tag is specified by the
                        object cevcSIEncapEncapsulation with the same 
                        index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                
                    'dot1ad'
                        The IEEE 802.1ad encapsulation is used as a match
                        criteria for the service instance.  The ether type
                        value of the IEEE 802.1ad tag is specified by the
                        cevcSIEncapEncapsulation column with the same index
                        value of cevcSIIndex and cevcSIMatchCreriaIndex.
                
                    'untagged'
                        Service instance processes untagged service frames.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                
                
                    'untaggedAndDot1q'
                        Both untagged frames and the IEEE 802.1q encapsulation
                        are used as a match criteria for the service instance.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                        The ether type value of the IEEE 802.1q tag is
                        specified by the cevcSIEncapEncapsulation column
                        with the same index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                    'untaggedAndDot1ad'
                        Both untagged frames and the IEEE 802.1ad encapsulation
                        are used as a match criteria for the service instance.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                        The ether type value of the IEEE 802.1ad tag is
                        specified by the cevcSIEncapEncapsulation column
                        with the same index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                
                    'priorityTagged'
                        Service instance processes priority tagged frames.
                        Only one service instance on the interface/media
                        type can use priority tagged frames as a match 
                        criteria.
                
                
                    'defaultTagged'
                        Service instance is a default service instance.  The
                        default service instance processes frames with VLANs
                        that do not match to any other service instances
                        configured on the interface/media type.  Only one
                        service instance on the interface/media type can be
                        the default service instance.
                ''',
                'cevcsimatchcriteriatype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSIMatchCriteriaTable.
                
                If the value of cevcSIMatchCriteriaType column is 'dot1q(1)'
                or 'dot1ad(2)' or 'untaggedAndDot1q' or 'untaggedAndDot1ad,
                then cevcSIMatchCriteriaRowStatus can not be set to 'active'
                until there exist an active row in the cevcSIMatchEncapTable
                with the same index value for cevcSIIndex and
                cevcSIMatchCriteriaIndex.
                
                Writable objects in this table can be modified while the
                value of the cevcSIMatchRowStatus column is 'active'.
                ''',
                'cevcsimatchrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsimatchstoragetype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIMatchCriteriaEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIMatchCriteriaTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIMatchCriteriaTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIMatchCriteriaEntry', REFERENCE_LIST, 'CevcSIMatchCriteriaEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry', 
                [], [], 
                '''                This entry represents a group of match criteria for a service
                instance.  Each entry in the table with the same cevcSIIndex and
                different cevcSIMatchCriteriaIndex represents an OR operation of
                the match criteria for the service instance.
                
                Entries in this table may be created and deleted via the
                cevcSIMatchRowStatus object or the management console on the
                system.
                
                Using SNMP, rows are created by a SET request setting the value
                of cevcSIMatchRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of cevcSIMatchRowStatus column to 'destroy'.
                ''',
                'cevcsimatchcriteriaentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIMatchCriteriaTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapEncapsulation_Enum' : _MetaInfoEnum('CevcSIMatchEncapEncapsulation_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'dot1qEthertype0x8100':'DOT1QETHERTYPE0X8100',
            'dot1qEthertype0x9100':'DOT1QETHERTYPE0X9100',
            'dot1qEthertype0x9200':'DOT1QETHERTYPE0X9200',
            'dot1qEthertype0x88A8':'DOT1QETHERTYPE0X88A8',
            'dot1adEthertype0x88A8':'DOT1ADETHERTYPE0X88A8',
            'dot1ahEthertype0x88A8':'DOT1AHETHERTYPE0X88A8',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadType_Enum' : _MetaInfoEnum('CevcSIMatchEncapPayloadType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'other':'OTHER',
            'payloadType0x0800ip':'PAYLOADTYPE0X0800IP',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchCriteriaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsimatchcriteriaindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchEncapEncapsulation', REFERENCE_ENUM_CLASS, 'CevcSIMatchEncapEncapsulation_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapEncapsulation_Enum', 
                [], [], 
                '''                This object specifies the encapsulation type used as service
                match criteria.  The object also specifies the Ethertype for
                egress packets on the service instance.
                
                
                    'dot1qEthertype0x8100'
                        The IEEE 801.1q encapsulation with ether type value
                        0x8100.
                
                
                    'dot1qEthertype0x9100'
                        The IEEE 801.1q encapsulation with ether type value
                        0x9100.
                
                
                    'dot1qEthertype0x9200'
                        The IEEE 801.1q encapsulation with ether type value
                        0x9200.
                
                
                    'dot1qEthertype0x88A8'
                         The IEEE 801.1q encapsulation with ether type value
                         0x88A8.
                
                
                    'dot1adEthertype0x88A8'
                        The IEEE 801.1ad encapsulation with ether type value
                        0x88A8.
                
                
                    'dot1ahEthertype0x88A8'
                        The IEEE 801.1ah encapsulation with ether type value
                        0x88A8.
                ''',
                'cevcsimatchencapencapsulation',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapPayloadType', REFERENCE_ENUM_CLASS, 'CevcSIMatchEncapPayloadType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadType_Enum', 
                [], [], 
                '''                This object specifies the PayloadType(etype/protocol type)
                values that the service instance uses as a service match
                criteria.  This object is required when the forwarding of
                layer-2 ethernet packet is done through the payloadType i.e IP
                etc.
                
                
                    'other'
                        None of the following.
                
                
                    'payloadType0x0800ip'
                        Payload type value for IP is 0x0800.
                
                
                This object is valid only when 'payloadType' bit is set to '1'
                in corresponding instance of the object 
                cevcSIMatchEncapValid.
                
                This object is deprecated by cevcSIMatchEncapPayloadTypes.
                ''',
                'cevcsimatchencappayloadtype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapPayloadTypes', REFERENCE_BITS, 'CevcSIMatchEncapPayloadTypes_Bits' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadTypes_Bits', 
                [], [], 
                '''                This object specifies the etype/protocol type values that
                service instance uses as a service match criteria.  This
                object is required when the forwarding of layer-2 ethernet
                packet is done through the payload ether type i.e IP etc.
                
                
                    'payloadTypeIPv4'
                        Ethernet payload type value for IPv4 protocol.
                
                
                    'payloadTypeIPv6'
                        Ethernet payload type value for IPv6 protocol.
                
                
                    'payloadTypePPPoEDiscovery'
                        Ethernet payload type value for PPPoE discovery
                        stage.
                
                
                    'payloadTypePPPoESession'
                        Ethernet payload type value for PPPoE session
                        stage.
                
                
                    'payloadTypePPPoEAll'
                        All ethernet payload type values for PPPoE protocol.
                
                This object is valid only when 'payloadTypes' bit is set to
                '1' in corresponding instance of the object
                cevcSIMatchEncapValid.
                
                This object deprecates cevcSIMatchEncapPayloadType.
                ''',
                'cevcsimatchencappayloadtypes',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapPrimaryCos', REFERENCE_BITS, 'CiscoCosList_Bits' , 'ydk.models.tc.CISCO_TC', 'CiscoCosList_Bits', 
                [], [], 
                '''                This object specifies the CoS values which the Service
                Instance uses as service match criteria.  This object is valid
                only when 'primaryVlans' and 'primaryCos' bits are set to '1'
                in corresponding instance of the object
                cevcSIMatchEncapValid.
                ''',
                'cevcsimatchencapprimarycos',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapPriorityCos', REFERENCE_BITS, 'CiscoCosList_Bits' , 'ydk.models.tc.CISCO_TC', 'CiscoCosList_Bits', 
                [], [], 
                '''                This object specifies the priority CoS values which the
                service instance uses as service match criteria.  This 
                object is valid only when 'priorityCos' bit is set to '1'
                in corresponding instance of the object cevcSIMatchEncapValid.
                ''',
                'cevcsimatchencapprioritycos',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSIMatchEncapTable.
                
                This object cannot be set to 'active' until
                cevcSIEncapEncapsulation and objects referred by 
                cevcSIMatchEncapValid have been assigned their respective
                valid values.
                
                Writable objects in this table can be modified while the value
                of the cevcSIEncapMatchRowStatus column is 'active'.
                ''',
                'cevcsimatchencaprowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapSecondaryCos', REFERENCE_BITS, 'CiscoCosList_Bits' , 'ydk.models.tc.CISCO_TC', 'CiscoCosList_Bits', 
                [], [], 
                '''                This object specifies the CoS values which the Service
                Instance uses as service match criteria.  This object is valid
                only when 'secondaryVlans' and 'secondaryCos' bits are set to
                '1' in corresponding instance of the object
                cevcSIMatchEncapValid.
                ''',
                'cevcsimatchencapsecondarycos',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsimatchencapstoragetype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapValid', REFERENCE_BITS, 'CevcSIMatchEncapValid_Bits' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapValid_Bits', 
                [], [], 
                '''                This object specifies the encapsulation criteria used to match
                a service instance.
                
                
                    'primaryCos'
                        The 'primaryCos' bit set to '1' specifies the
                        Class of Service is used as service match criteria for
                        the service instance.  When this bit is set to '1'
                        there must exist aleast one active rows in the
                        cevcSIPrimaryVlanTable which has the same index values
                        of cevcSIIndex and cevcSIMatchCriteriaIndex.  When
                        'primaryCos' bit is '1', the cevcSIPrimaryCos column
                        indicates the CoS value(s).
                
                    'secondaryCos'
                        The 'secondaryCos' bit set to '1' specifies the
                        Class of Service is used as service match criteria for
                        the service instance.  When this bit is set to '1'
                        there must exist aleast one active rows in the
                        cevcSISecondaryVlanTable which has the same index
                        values of cevcSIIndex and cevcSIMatchCriteriaIndex.
                        When 'secondaryCos' bit is '1', the
                        cevcSISecondaryCos column indicates the CoS 
                        value(s).
                
                
                    'payloadType'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPayloadType
                        is used as service match criteria for the service
                        instance.
                
                
                    'payloadTypes'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPayloadTypes
                        is used as service match criteria for the service
                        instance.
                
                
                    'priorityCos'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPriorityCos
                        is used as service match criteria for the service
                        instance.
                
                
                    'dot1qNativeVlan'
                        This bit set to '1' specifies that the IEEE 802.1q
                        tag with native vlan is used as service match 
                        criteria for the service instance.
                
                
                    'dot1adNativeVlan'
                        This bit set to '1' specifies that the IEEE 802.1ad
                        tag with native vlan is used as service match 
                        criteria for the service instance.
                
                
                    'encapExact'
                        This bit set to '1' specifies that a service frame is
                        mapped to the service instance only if it matches
                        exactly to the encapsulation specified by the service
                        instance.
                ''',
                'cevcsimatchencapvalid',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIMatchEncapEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIMatchEncapTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIMatchEncapTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIMatchEncapEntry', REFERENCE_LIST, 'CevcSIMatchEncapEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry', 
                [], [], 
                '''                This entry represents a group of encapulation match criteria
                for a service instance.
                
                Entries in this table may be created and deleted via the
                cevcSIMatchEncapRowStatus object or the management console
                on the system.
                
                Using SNMP, rows are created by a SET request setting the value
                of cevcSIMatchEncapRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of cevcSIMatchEncapRowStatus column to 'destroy'.
                ''',
                'cevcsimatchencapentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIMatchEncapTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchCriteriaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsimatchcriteriaindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIPrimaryVlanBeginningVlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                If cevcSIPrimaryVlanEndingVlan is '0', then this object
                indicates a single VLAN in the list.
                
                If cevcSIPrimaryVlanEndingVlan is not '0', then this object
                indicates the first VLAN in a range of VLANs.
                ''',
                'cevcsiprimaryvlanbeginningvlan',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIPrimaryVlanEndingVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                This object indicates the last VLAN in a range of VLANs.  If
                the row does not describe a range, then the value of this
                column must be '0'.
                ''',
                'cevcsiprimaryvlanendingvlan',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIPrimaryVlanRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSIPrimaryVlanTable.
                
                This column cannot be set to 'active' until all objects have 
                been assigned valid values.
                
                Writable objects in this table can be modified while the
                value of the cevcSIPrimaryVlanRowStatus column is 'active'.
                ''',
                'cevcsiprimaryvlanrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIPrimaryVlanStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsiprimaryvlanstoragetype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIPrimaryVlanEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIPrimaryVlanTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIPrimaryVlanTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIPrimaryVlanEntry', REFERENCE_LIST, 'CevcSIPrimaryVlanEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry', 
                [], [], 
                '''                This entry specifies a single VLAN or a range of VLANs
                contained in the primary VLAN list that's part of the 
                encapsulation match criteria.
                
                Entries in this table may be created and deleted via the
                cevcSIPrimaryVlanRowStatus object or the management console
                on the system.
                
                Using SNMP, rows are created by a SET request setting the value
                of the cevcSIPrimaryVlanRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of the cevcSIPrimaryVlanRowStatus column to 'destroy'.
                ''',
                'cevcsiprimaryvlanentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIPrimaryVlanTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIMatchCriteriaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsimatchcriteriaindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSISecondaryVlanBeginningVlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                If cevcSISecondaryVlanEndingVlan is '0', then this object
                indicates a single VLAN in the list.
                
                If cevcSISecondaryVlanEndingVlan is not '0', then this
                object indicates the first VLAN in a range of VLANs.
                ''',
                'cevcsisecondaryvlanbeginningvlan',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSISecondaryVlanEndingVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                This object indicates the last VLAN in a range of VLANs.  If
                the row does not describe a range, then the value of this
                column must be '0'.
                ''',
                'cevcsisecondaryvlanendingvlan',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSISecondaryVlanRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSISecondaryVlanTable.
                
                This column can not be set to 'active' until all objects have 
                been assigned valid values.
                
                Writable objects in this table can be modified while the
                value of cevcSISecondaryVlanRowStatus column is 'active'.
                ''',
                'cevcsisecondaryvlanrowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSISecondaryVlanStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsisecondaryvlanstoragetype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSISecondaryVlanEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSISecondaryVlanTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSISecondaryVlanTable',
            False, 
            [
            _MetaInfoClassMember('cevcSISecondaryVlanEntry', REFERENCE_LIST, 'CevcSISecondaryVlanEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry', 
                [], [], 
                '''                This entry specifies a single VLAN or a range of VLANs
                contained in the secondary VLAN list that's part of the 
                encapsulation match criteria.
                
                Entries in this table may be created and deleted via the
                cevcSISecondaryVlanRowStatus object or the management console
                on the system.
                
                Using SNMP, rows are created by a SET request setting the value
                of the cevcSISecondaryVlanRowStatus column to 'createAndGo' or
                'createAndWait'.  Rows are deleted by a SET request setting the
                value of the cevcSISecondaryVlanRowStatus column to 'destroy'.
                ''',
                'cevcsisecondaryvlanentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSISecondaryVlanTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry.CevcSIOperStatus_Enum' : _MetaInfoEnum('CevcSIOperStatus_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'adminDown':'ADMINDOWN',
            'deleted':'DELETED',
            'errorDisabled':'ERRORDISABLED',
            'unknown':'UNKNOWN',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIOperStatus', REFERENCE_ENUM_CLASS, 'CevcSIOperStatus_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry.CevcSIOperStatus_Enum', 
                [], [], 
                '''                This object indicates the operational status of the Service
                Instance.
                
                
                    'up' 
                        Service instance is fully operational and able to
                        transfer traffic.
                
                
                    'down'
                        Service instance is down and not capable of
                        transferring traffic, and is not administratively
                        configured to be down by management system. 
                
                
                    'adminDown'
                        Service instance has been explicitly configured to
                        administratively down by a management system and is not
                        capable of transferring traffic.
                
                
                    'deleted'
                        Service instance has been deleted.
                
                
                    'errorDisabled'
                        Service instance has been shut down due to MAC 
                        security violations. 
                
                
                    'unknown'
                        Operational status of service instance is unknown or
                        undefined.
                ''',
                'cevcsioperstatus',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIStateEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIStateTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIStateTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIStateEntry', REFERENCE_LIST, 'CevcSIStateEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry', 
                [], [], 
                '''                This entry represents operational status of a service instance.
                
                The system automatically creates an entry when the system or
                the EMS NMS creates a row in the cevcSITable.  Likewise, the
                system automatically destroys an entry when the system or the
                EMS NMS destroys the corresponding row in the cevcSITable.
                ''',
                'cevcsistateentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIStateTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIAdminStatus_Enum' : _MetaInfoEnum('CevcSIAdminStatus_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSICreationType_Enum' : _MetaInfoEnum('CevcSICreationType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'static':'STATIC',
            'dynamic':'DYNAMIC',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIForwardingType_Enum' : _MetaInfoEnum('CevcSIForwardingType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'other':'OTHER',
            'bridgeDomain':'BRIDGEDOMAIN',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIType_Enum' : _MetaInfoEnum('CevcSIType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'regular':'REGULAR',
            'trunk':'TRUNK',
            'l2context':'L2CONTEXT',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSITable.CevcSIEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSITable.CevcSIEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates an arbitrary integer-value that uniquely
                identifies a service instance.  An implementation MAY assign
                an ifIndex-value assigned to the service instance to
                cevcSIIndex.
                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIAdminStatus', REFERENCE_ENUM_CLASS, 'CevcSIAdminStatus_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIAdminStatus_Enum', 
                [], [], 
                '''                This object specifies the desired state of the Service
                Instance.  
                
                
                    'up'
                        Ready to transfer traffic.  When a system initializes,
                        all service instances start with this state.  
                
                
                    'down'
                        The service instance is administratively down and is
                        not capable of transferring traffic.
                ''',
                'cevcsiadminstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSICreationType', REFERENCE_ENUM_CLASS, 'CevcSICreationType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSICreationType_Enum', 
                [], [], 
                '''                This object specifies whether the service instance created
                is statically configured by the user or is dynamically created.
                
                      'static'
                          If the service instance is configured manually this  
                          object is set to static(1).
                
                      'dynamic'
                          If the service instance is created dynamically
                           by the first sign of life of an Ethernet frame,
                            then this object is set to dynamic(2) for 
                            the service instance.
                ''',
                'cevcsicreationtype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIEvcIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the EVC Index that the service instance
                is associated.  The value of '0' this column indicates that
                the service instance is not associated to an EVC.
                
                If the value of cevcSIEvcIndex column is not '0', there must
                exist an active row in the cevcEvcTable with the same index
                value for cevcEvcIndex.
                ''',
                'cevcsievcindex',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardingType', REFERENCE_ENUM_CLASS, 'CevcSIForwardingType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIForwardingType_Enum', 
                [], [], 
                '''                This object indicates technique used by a service instance to
                forward service frames.
                
                    'other'
                        If the forwarding behavior of a service instance is
                        not defined or unknown, this object is set to other(0).
                
                
                    'bridgeDomain'
                        Bridge domain is used to forward service frames by a
                        service instance.  If cevcSIForwardingType is 
                        'bridgeDomain(1)', there must exist an active
                        row in the cevcSIForwardBdTable with the same
                        index value of cevcSIIndex.  The object
                        cevcSIForwardBdNumber indicates the identifier of
                        the bridge domain component being used.
                ''',
                'cevcsiforwardingtype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The textual name of the service instance.  The value of this
                column should be the name of the component as assigned by the
                local interface/media type and should be be suitable for use
                in commands entered at the device's 'console'.  This might be
                text name, such as 'si1' or a simple service instance number, 
                such as '1', depending on the interface naming syntax of the
                device.
                
                If there is no local name or this object is otherwise not
                applicable, then this object contains a zero-length string.
                ''',
                'cevcsiname',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSITable.
                
                This object cannot be set to 'active' until following
                corresponding objects are assigned to valid values:
                
                   - cevcSITargetType
                   - cevcSITarget
                   - cevcSIName
                   - cevcSIType
                
                Following writable objects in this table cannot be modified
                while the value of cevcSIRowStatus is 'active':
                
                   - cevcSITargetType
                   - cevcSITarget
                   - cevcSIName
                   - cevcSIType
                
                Objects in this table and all other tables that have the same
                cevcSIIndex value as an index disappear when cevcSIRowStatus is
                set to 'destroy'.
                ''',
                'cevcsirowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsistoragetype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSITarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 40)], [], 
                '''                This object indicates the target to which a service instance
                has an attachment.
                
                If the target is unknown, the value of the cevcSITarget column
                is a zero-length string.
                ''',
                'cevcsitarget',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSITargetType', REFERENCE_ENUM_CLASS, 'ServiceInstanceTargetType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'ServiceInstanceTargetType_Enum', 
                [], [], 
                '''                This object indicates the type of interface/media to which a
                service instance has an attachment.
                ''',
                'cevcsitargettype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIType', REFERENCE_ENUM_CLASS, 'CevcSIType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIType_Enum', 
                [], [], 
                '''                This object specifies the type of the service instance. It
                mentions if the service instance is either a regular or trunk
                or l2context service instance.
                
                        'regular'
                              If a service instance is configured without  
                              any type specified, then it is a regular service 
                              instance.
                              
                
                        'trunk'
                              If the service instance is configured
                              with trunk type, then it is a trunk service
                              instance. For a trunk service instance,
                              its Bridge domain IDs are derived from 
                              encapsulation VLAN plus an optional offset
                               (refer cevcSIForwardBdNumberBase object).
                             
                
                          'l2context'
                              If the service instance is configured 
                              with dynamic type, then it is a L2 context 
                              service instance. The Ethernet L2 Context
                              is a statically configured service instance
                              which contains the Ethernet Initiator
                              for attracting the first sign of life. In other
                              words, Ethernet L2 Context service instance is
                              used for catching the first sign of life of 
                              Ethernet frames to create dynamic Ethernet 
                              sessions service instances.
                ''',
                'cevcsitype',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSITable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSITable',
            False, 
            [
            _MetaInfoClassMember('cevcSIEntry', REFERENCE_LIST, 'CevcSIEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable.CevcSIEntry', 
                [], [], 
                '''                This entry represents a service instance configured on the
                system and its service attributes.
                
                Entries in this table may be created and deleted via the
                cevcSIRowStatus object or the management console on the
                system.
                
                Using SNMP, rows are created by a SET request setting the value
                of cevcSIRowStatus column to 'createAndGo'or 'createAndWait'. 
                Rows are deleted by a SET request setting the value of
                cevcSIRowStatus column to 'destroy'.
                ''',
                'cevcsientry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSITable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteAction_Enum' : _MetaInfoEnum('CevcSIVlanRewriteAction_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'push1':'PUSH1',
            'push2':'PUSH2',
            'pop1':'POP1',
            'pop2':'POP2',
            'translate1To1':'TRANSLATE1TO1',
            'translate1To2':'TRANSLATE1TO2',
            'translate2To1':'TRANSLATE2TO1',
            'translate2To2':'TRANSLATE2TO2',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteDirection_Enum' : _MetaInfoEnum('CevcSIVlanRewriteDirection_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'ingress':'INGRESS',
            'egress':'EGRESS',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteEncapsulation_Enum' : _MetaInfoEnum('CevcSIVlanRewriteEncapsulation_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'dot1q':'DOT1Q',
            'dot1ad':'DOT1AD',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry',
            False, 
            [
            _MetaInfoClassMember('cevcSIIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cevcsiindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIVlanRewriteDirection', REFERENCE_ENUM_CLASS, 'CevcSIVlanRewriteDirection_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteDirection_Enum', 
                [], [], 
                '''                This object specifies the VLAN adjustment for 'ingress'
                frames or 'egress' frames on the service instance.
                ''',
                'cevcsivlanrewritedirection',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcSIVlanRewriteAction', REFERENCE_ENUM_CLASS, 'CevcSIVlanRewriteAction_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteAction_Enum', 
                [], [], 
                '''                This object specifies the rewrite action the device performs
                for the service instance, including:
                
                    'push1'
                        Add cevcSIVlanRewriteVlan1 as the VLAN tag to the
                        service frame.
                
                
                    'push2'
                        Add cevcSIVlanRewriteVlan1 as the outer VLAN tag 
                        and cevcSIVlanRewriteVlan2 as the inner VLAN tag of
                        the service frame.
                
                
                    'pop1'
                        Remove the outermost VLAN tag from the service frame.
                
                
                    'pop2'
                        Remove the two outermost VLAN tags from the service
                        frame.
                
                
                    'translate1To1'
                        Replace the outermost VLAN tag with the 
                        cevcSIVlanRewriteVlan1 tag.
                
                
                   'translate1To2'
                       Replace the outermost VLAN tag with
                       cevcSIVlanRewriteVlan1 and add cevcSIVlanRewriteVlan2
                       to the second VLAN tag of the service frame.
                
                
                    'translate2To1'
                        Remove the outermost VLAN tag and replace the second
                        VLAN tag with cevcSIVlanVlanRewriteVlan1.
                
                
                   'translate2To2'
                       Replace the outermost VLAN tag with
                       cevcSIVlanRewriteVlan1 and the second VLAN tag with
                       cevcSIVlanRewriteVlan2.
                ''',
                'cevcsivlanrewriteaction',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteEncapsulation', REFERENCE_ENUM_CLASS, 'CevcSIVlanRewriteEncapsulation_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteEncapsulation_Enum', 
                [], [], 
                '''                This object specifies the encapsulation type to
                process for the service instance.
                
                
                    'dot1q'
                        The IEEE 802.1q encapsulation.
                
                
                    'dot1ad'
                        The IEEE 802.1ad encapsulation.
                ''',
                'cevcsivlanrewriteencapsulation',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object enables a SNMP peer to create, modify, and delete
                rows in the cevcSIVlanRewriteTable.
                
                cevcSIVlanRewriteAction and cevcSIVlanRewriteEncapsulation must
                have valid values before this object can be set to 'active'.
                
                Writable objects in this table can be modified while the
                value of cevcSIVlanRewriteRowStatus column is 'active'.
                ''',
                'cevcsivlanrewriterowstatus',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object specifies how the SNMP entity stores the data
                contained by the corresponding conceptual row.
                
                This object can be set to either 'volatile' or 'nonVolatile'.
                Other values are not applicable for this conceptual row and
                are not supported.
                ''',
                'cevcsivlanrewritestoragetype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteSymmetric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object is valid only when cevcSIVlanRewriteDirection is
                'ingress'.  The value 'true' of this column specifies that
                egress packets are tagged with a VLAN specified by an active
                row in cevcSIPrimaryVlanTable.
                
                There could only be one VLAN value assigned in the 
                cevcSIPrimaryVlanTable, i.e. only one 'active' entry
                that has the same index value of cevcSIIndex column and
                corresponding instance of cevcSIPrimaryVlanEndingVlan
                column has value '0'.
                ''',
                'cevcsivlanrewritesymmetric',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteVlan1', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                This object specifies the outermost VLAN ID tag of the
                frame for the service instance.  This object is valid 
                only when cevcSIVlanRewriteAction is 'push1', 'push2',
                'translate1To1', 'translate1To2', 'translate2To1', or 
                'translate2To2'.
                ''',
                'cevcsivlanrewritevlan1',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteVlan2', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                This object specifies the second VLAN ID tag of the
                frame for the service instance.  This object is valid 
                only when cevcSIVlanRewriteAction is 'push2',
                'translate1To2', or 'translate2To2'.
                ''',
                'cevcsivlanrewritevlan2',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIVlanRewriteEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSIVlanRewriteTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSIVlanRewriteTable',
            False, 
            [
            _MetaInfoClassMember('cevcSIVlanRewriteEntry', REFERENCE_LIST, 'CevcSIVlanRewriteEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry', 
                [], [], 
                '''                Each entry represents the VLAN adjustment for a Service
                Instance.
                ''',
                'cevcsivlanrewriteentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSIVlanRewriteTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcSystem' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcSystem',
            False, 
            [
            _MetaInfoClassMember('cevcMaxNumEvcs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the maximum number of EVCs that the
                system supports.
                ''',
                'cevcmaxnumevcs',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcNumCfgEvcs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the actual number of EVCs currently
                configured on the system.
                ''',
                'cevcnumcfgevcs',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcSystem',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry',
            False, 
            [
            _MetaInfoClassMember('cevcUniCEVlanEvcBeginningVlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                If cevcUniCEVlanEvcEndingVlan is '0', then this object
                indicates a single VLAN in the list.
                
                If cevcUniCEVlanEvcEndingVlan is not '0', then this object
                indicates the first VLAN in a range of VLANs.
                ''',
                'cevcunicevlanevcbeginningvlan',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcUniEvcIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object indicates an arbitrary integer-value that uniquely
                identifies the EVC attached at an UNI.
                ''',
                'cevcunievcindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcUniCEVlanEvcEndingVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                This object indicates the last VLAN in a range of VLANs.  If
                the row does not describe a range, then the value of this
                column must be '0'.
                ''',
                'cevcunicevlanevcendingvlan',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcUniCEVlanEvcEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcUniCEVlanEvcTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcUniCEVlanEvcTable',
            False, 
            [
            _MetaInfoClassMember('cevcUniCEVlanEvcEntry', REFERENCE_LIST, 'CevcUniCEVlanEvcEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry', 
                [], [], 
                '''                This entry represents an EVC and the CE-VLANs that are mapped
                to it at an UNI.
                
                For example, if CE-VLANs 10, 20-30, 40 are mapped to an EVC
                indicated by  cevcUniEvcIndex = 1, at an UNI with ifIndex = 2,
                this table will contain following rows to represent above
                CE-VLAN map:
                
                  cevcUniCEVlanEvcEndingVlan.2.1.10 = 0
                  cevcUniCEVlanEvcEndingVlan.2.1.20 = 30
                  cevcUniCEVlanEvcEndingVlan.2.1.40 = 0
                
                The system automatically creates an entry when the system
                creates an entry in the cevcUniTable and an entry is created in
                cevcSICEVlanTable for a service instance which is attached to
                an EVC on this UNI.  Likewise, the system automatically destroys
                an entry when the system or the EMS/NMS destroys the
                corresponding row in the cevcUniTable or in the
                cevcSICEVlanTable.
                ''',
                'cevcunicevlanevcentry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcUniCEVlanEvcTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniPortType_Enum' : _MetaInfoEnum('CevcUniPortType_Enum', 'ydk.models.evc.CISCO_EVC_MIB',
        {
            'dot1q':'DOT1Q',
            'dot1ad':'DOT1AD',
        }, 'CISCO-EVC-MIB', _yang_ns._namespaces['CISCO-EVC-MIB']),
    'CISCOEVCMIB.CevcUniTable.CevcUniEntry' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcUniTable.CevcUniEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-EVC-MIB', True),
            _MetaInfoClassMember('cevcUniIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object specifies a string-value assigned to a UNI for
                identification.  When the UNI identifier is configured by the
                system or the EMS/NMS, it should be unique among all UNIs for
                the MEN.
                
                If the UNI identifier value is not specified, the value of the
                cevcUniIdentifier column is a zero-length string.
                ''',
                'cevcuniidentifier',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcUniPortType', REFERENCE_ENUM_CLASS, 'CevcUniPortType_Enum' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniPortType_Enum', 
                [], [], 
                '''                This object specifies the UNI port type.
                
                
                'dot1q'
                    The UNI port is an IEEE 802.1q port.   
                
                
                'dot1ad'
                    The UNI port is an IEEE 802.1ad port.
                ''',
                'cevcuniporttype',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcUniServiceAttributes', REFERENCE_BITS, 'CevcUniServiceAttributes_Bits' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniServiceAttributes_Bits', 
                [], [], 
                '''                This object specifies the UNI service attributes.
                
                
                'serviceMultiplexing'
                    This bit specifies whether the UNI supports multiple
                    EVCs.  Point-to-Point EVCs and Multipoint-to-Multipoint
                    EVCs may be multiplexed in any combination at the UNI 
                    if this bit is set to '1'.
                
                
                'bundling'
                    This bit specifies whether the UNI has the bundling
                    attribute configured.  If this bit is set to '1', more
                    than one CE-VLAN ID can map to a particular EVC at the
                    UNI. 
                
                
                'allToOneBundling'
                    This bit specifies whether the UNI has the all to one
                    bundling attribute.  If this bit is set to '1', all
                    CE-VLAN IDs map to a single EVC at the UNI.
                
                To summarize the valid combinations of serviceMultiplexing(0),
                bundling(1) and allToOneBundling(2) bits for an UNI, consider 
                the following diagram:
                
                           VALID COMBINATIONS
                +---------------+-------+-------+-------+-------+-------+ 
                |UNI ATTRIBUTES |   1   |   2   |   3   |   4   |   5   |
                +---------------+-------+------+------------------------+
                |Service        |       |       |       |       |       |
                |Multiplexing   |       |   Y   |   Y   |       |       |
                |               |       |       |       |       |       |
                +---------------+-------+-------+-------+-------+-------+
                |               |       |       |       |       |       |
                |Bundling       |       |       |   Y   |   Y   |       |
                |               |       |       |       |       |       |
                +---------------+-------+-------+-------+-------+-------+
                |All to One     |       |       |       |       |       |
                |Bundling       |       |       |       |       |   Y   |
                |               |       |       |       |       |       |
                +---------------+-------+-------+------ +-------+-------+
                ''',
                'cevcuniserviceattributes',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcUniEntry',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB.CevcUniTable' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB.CevcUniTable',
            False, 
            [
            _MetaInfoClassMember('cevcUniEntry', REFERENCE_LIST, 'CevcUniEntry' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniTable.CevcUniEntry', 
                [], [], 
                '''                This entry represents an UNI and its service attributes.
                
                The system automatically creates an entry when the system or
                the EMS/NMS creates a row in the cevcPortTable with a 
                cevcPortMode of 'uni'.  Likewise, the system automatically
                destroys an entry when the system or the EMS/NMS destroys the
                corresponding row in the cevcPortTable.
                ''',
                'cevcunientry',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'cevcUniTable',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
    'CISCOEVCMIB' : {
        'meta_info' : _MetaInfoClass('CISCOEVCMIB',
            False, 
            [
            _MetaInfoClassMember('cevcEvcNotificationConfig', REFERENCE_CLASS, 'CevcEvcNotificationConfig' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcNotificationConfig', 
                [], [], 
                '''                ''',
                'cevcevcnotificationconfig',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcStateTable', REFERENCE_CLASS, 'CevcEvcStateTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcStateTable', 
                [], [], 
                '''                This table lists statical/status data of the EVC.
                
                This table has an one-to-one dependent relationship on the
                cevcEvcTable, containing a row for each EVC.
                ''',
                'cevcevcstatetable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcTable', REFERENCE_CLASS, 'CevcEvcTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcTable', 
                [], [], 
                '''                This table contains a list of EVCs and their service
                attributes.
                ''',
                'cevcevctable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcEvcUniTable', REFERENCE_CLASS, 'CevcEvcUniTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcEvcUniTable', 
                [], [], 
                '''                This table contains a list of UNI's for each EVC configured
                on the device.  The UNIs can be  local (i.e. physically 
                located on the system) or remote (i.e. not physically located
                on the device).  For local UNIs, the UNI Id is the same as 
                denoted by cevcUniIdentifier with the same ifIndex value as 
                cevcEvcLocalUniIfIndex.  For remote UNIs, the underlying OAM 
                protocol, if capable, provides the UNI Id via its protocol 
                messages.
                
                This table has an expansion dependent relationship on the
                cevcEvcTable, containing a row for each UNI that is in
                the EVC.
                ''',
                'cevcevcunitable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcMacSecurityViolation', REFERENCE_CLASS, 'CevcMacSecurityViolation' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcMacSecurityViolation', 
                [], [], 
                '''                ''',
                'cevcmacsecurityviolation',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcPortL2ControlProtocolTable', REFERENCE_CLASS, 'CevcPortL2ControlProtocolTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortL2ControlProtocolTable', 
                [], [], 
                '''                This table lists the layer 2 control protocol processing
                attributes at UNI ports.  
                
                This table has an expansion dependent relationship on the 
                cevcUniTable, containing zero or more rows for each UNI.
                ''',
                'cevcportl2controlprotocoltable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcPortTable', REFERENCE_CLASS, 'CevcPortTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcPortTable', 
                [], [], 
                '''                This table provides the operational mode and configuration
                limitations of the physical interfaces (ports) that provide
                Ethernet services for the MEN. 
                
                This table has a sparse depedent relationship on the ifTable, 
                containing a row for each ifEntry having an ifType of 
                'ethernetCsmacd' capable of supporting Ethernet services.
                ''',
                'cevcporttable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSICEVlanTable', REFERENCE_CLASS, 'CevcSICEVlanTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSICEVlanTable', 
                [], [], 
                '''                This table contains the CE-VLAN map list for each Service
                Instance.
                
                This table has an expansion dependent relationship on the
                cevcSITable, containing a row for each CE-VLAN or a range of
                CE-VLANs that are mapped to a service instance.
                ''',
                'cevcsicevlantable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIForwardBdTable', REFERENCE_CLASS, 'CevcSIForwardBdTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIForwardBdTable', 
                [], [], 
                '''                This table contains the forwarding bridge domain information
                for each service instance.
                
                This table has a sparse dependent relationship on the 
                cevcSITable, containing a row for each service instance having 
                a cevcSIForwardingType of 'bridgeDomain'.
                ''',
                'cevcsiforwardbdtable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIL2ControlProtocolTable', REFERENCE_CLASS, 'CevcSIL2ControlProtocolTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIL2ControlProtocolTable', 
                [], [], 
                '''                This table lists the layer 2 control protocol processing
                attributes at service instances.  
                
                This table has an expansion dependent relationship on the 
                cevcSITable, containing a row for each layer 2 
                control protocol disposition at each service instance.
                ''',
                'cevcsil2controlprotocoltable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchCriteriaTable', REFERENCE_CLASS, 'CevcSIMatchCriteriaTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchCriteriaTable', 
                [], [], 
                '''                This table contains the match criteria for each Service
                Instance.
                
                This table has an expansion dependent relationship on the
                cevcSITable, containing a row for each group of  match
                criteria of each service instance.
                ''',
                'cevcsimatchcriteriatable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIMatchEncapTable', REFERENCE_CLASS, 'CevcSIMatchEncapTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIMatchEncapTable', 
                [], [], 
                '''                This table contains the encapsulation based match criteria for
                each service instance.  
                
                This table has a sparse dependent relationship on the 
                cevcSIMatchCriteriaTable, containing a row for each match 
                criteria having one of the following values for 
                cevcSIMatchCriteriaType:
                
                    - 'dot1q'
                    - 'dot1ad'
                    - 'untaggedAndDot1q'
                    - 'untaggedAndDot1ad'
                    - 'priorityTagged'
                ''',
                'cevcsimatchencaptable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIPrimaryVlanTable', REFERENCE_CLASS, 'CevcSIPrimaryVlanTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIPrimaryVlanTable', 
                [], [], 
                '''                This table contains the primary VLAN ID list for each Service
                Instance.
                
                This table has an expansion dependent relationship on the 
                cevcSIMatchEncapTable, containing zero or more rows for each 
                encapsulation match criteria.
                ''',
                'cevcsiprimaryvlantable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSISecondaryVlanTable', REFERENCE_CLASS, 'CevcSISecondaryVlanTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSISecondaryVlanTable', 
                [], [], 
                '''                This table contains the seconadary VLAN ID list for each
                service instance.
                
                This table has an expansion dependent relationship on the 
                cevcSIMatchEncapTable, containing zero or more rows for each 
                encapsulation match criteria.
                ''',
                'cevcsisecondaryvlantable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIStateTable', REFERENCE_CLASS, 'CevcSIStateTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIStateTable', 
                [], [], 
                '''                This table lists statical status data of the service instance.
                
                This table has an one-to-one dependent relationship on the
                cevcSITable, containing a row for each service instance.
                ''',
                'cevcsistatetable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSITable', REFERENCE_CLASS, 'CevcSITable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSITable', 
                [], [], 
                '''                This table lists each service instance and its service
                attributes.
                ''',
                'cevcsitable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSIVlanRewriteTable', REFERENCE_CLASS, 'CevcSIVlanRewriteTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSIVlanRewriteTable', 
                [], [], 
                '''                This table lists the rewrite adjustments of the service
                frame's VLAN tags for service instances.
                
                This table has an expansion dependent relationship on the
                cevcSITable, containing a row for a VLAN adjustment
                for ingress and egress frames at each service instance.
                ''',
                'cevcsivlanrewritetable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcSystem', REFERENCE_CLASS, 'CevcSystem' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcSystem', 
                [], [], 
                '''                ''',
                'cevcsystem',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcUniCEVlanEvcTable', REFERENCE_CLASS, 'CevcUniCEVlanEvcTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniCEVlanEvcTable', 
                [], [], 
                '''                This table contains for each UNI, a list of EVCs and the
                association of CE-VLANs to the EVC.  The CE-VLAN mapping is 
                locally significant to the UNI.
                
                This table has an expansion dependent relationship on the 
                cevcUniTable, containing zero or more rows for each UNI.
                ''',
                'cevcunicevlanevctable',
                'CISCO-EVC-MIB', False),
            _MetaInfoClassMember('cevcUniTable', REFERENCE_CLASS, 'CevcUniTable' , 'ydk.models.evc.CISCO_EVC_MIB', 'CISCOEVCMIB.CevcUniTable', 
                [], [], 
                '''                This table contains a list of UNIs locally configured on the
                system.
                
                This table has a sparse dependent relationship on the 
                cevcPortTable, containing a row for each cevcPortEntry
                having a cevcPortMode column value 'uni'.
                ''',
                'cevcunitable',
                'CISCO-EVC-MIB', False),
            ],
            'CISCO-EVC-MIB',
            'CISCO-EVC-MIB',
            _yang_ns._namespaces['CISCO-EVC-MIB'],
        'ydk.models.evc.CISCO_EVC_MIB'
        ),
    },
}
_meta_table['CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcEvcStateTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcTable.CevcEvcEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcEvcTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcEvcUniTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcPortTable.CevcPortEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcPortTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSICEVlanTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIForwardBdTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIMatchEncapTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIPrimaryVlanTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSISecondaryVlanTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIStateTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSITable']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcUniCEVlanEvcTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcUniTable.CevcUniEntry']['meta_info'].parent =_meta_table['CISCOEVCMIB.CevcUniTable']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcNotificationConfig']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcStateTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcEvcUniTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcMacSecurityViolation']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcPortTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSICEVlanTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIForwardBdTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIMatchEncapTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIPrimaryVlanTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSISecondaryVlanTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIStateTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSITable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcSystem']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcUniCEVlanEvcTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']
_meta_table['CISCOEVCMIB.CevcUniTable']['meta_info'].parent =_meta_table['CISCOEVCMIB']['meta_info']

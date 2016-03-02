


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Dot1agCfmEgressActionFieldValue_Enum' : _MetaInfoEnum('Dot1agCfmEgressActionFieldValue_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'egrNoTlv':'EGRNOTLV',
            'egrOK':'EGROK',
            'egrDown':'EGRDOWN',
            'egrBlocked':'EGRBLOCKED',
            'egrVid':'EGRVID',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmInterfaceStatus_Enum' : _MetaInfoEnum('Dot1agCfmInterfaceStatus_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'isNoInterfaceStatusTLV':'ISNOINTERFACESTATUSTLV',
            'isUp':'ISUP',
            'isDown':'ISDOWN',
            'isTesting':'ISTESTING',
            'isUnknown':'ISUNKNOWN',
            'isDormant':'ISDORMANT',
            'isNotPresent':'ISNOTPRESENT',
            'isLowerLayerDown':'ISLOWERLAYERDOWN',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmFngState_Enum' : _MetaInfoEnum('Dot1agCfmFngState_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'fngReset':'FNGRESET',
            'fngDefect':'FNGDEFECT',
            'fngReportDefect':'FNGREPORTDEFECT',
            'fngDefectReported':'FNGDEFECTREPORTED',
            'fngDefectClearing':'FNGDEFECTCLEARING',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmIngressActionFieldValue_Enum' : _MetaInfoEnum('Dot1agCfmIngressActionFieldValue_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'ingNoTlv':'INGNOTLV',
            'ingOk':'INGOK',
            'ingDown':'INGDOWN',
            'ingBlocked':'INGBLOCKED',
            'ingVid':'INGVID',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmLowestAlarmPri_Enum' : _MetaInfoEnum('Dot1agCfmLowestAlarmPri_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'allDef':'ALLDEF',
            'macRemErrXcon':'MACREMERRXCON',
            'remErrXcon':'REMERRXCON',
            'errXcon':'ERRXCON',
            'xcon':'XCON',
            'noXcon':'NOXCON',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmMhfCreation_Enum' : _MetaInfoEnum('Dot1agCfmMhfCreation_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'defMHFnone':'DEFMHFNONE',
            'defMHFdefault':'DEFMHFDEFAULT',
            'defMHFexplicit':'DEFMHFEXPLICIT',
            'defMHFdefer':'DEFMHFDEFER',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmMaintAssocNameType_Enum' : _MetaInfoEnum('Dot1agCfmMaintAssocNameType_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'primaryVid':'PRIMARYVID',
            'charString':'CHARSTRING',
            'unsignedInt16':'UNSIGNEDINT16',
            'rfc2865VpnId':'RFC2865VPNID',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmMpDirection_Enum' : _MetaInfoEnum('Dot1agCfmMpDirection_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'down':'DOWN',
            'up':'UP',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmPortStatus_Enum' : _MetaInfoEnum('Dot1agCfmPortStatus_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'psNoPortStateTLV':'PSNOPORTSTATETLV',
            'psBlocked':'PSBLOCKED',
            'psUp':'PSUP',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmRemoteMepState_Enum' : _MetaInfoEnum('Dot1agCfmRemoteMepState_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'rMepIdle':'RMEPIDLE',
            'rMepStart':'RMEPSTART',
            'rMepFailed':'RMEPFAILED',
            'rMepOk':'RMEPOK',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmRelayActionFieldValue_Enum' : _MetaInfoEnum('Dot1agCfmRelayActionFieldValue_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'rlyHit':'RLYHIT',
            'rlyFdb':'RLYFDB',
            'rlyMpdb':'RLYMPDB',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmIdPermission_Enum' : _MetaInfoEnum('Dot1agCfmIdPermission_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'sendIdNone':'SENDIDNONE',
            'sendIdChassis':'SENDIDCHASSIS',
            'sendIdManage':'SENDIDMANAGE',
            'sendIdChassisManage':'SENDIDCHASSISMANAGE',
            'sendIdDefer':'SENDIDDEFER',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmCcmInterval_Enum' : _MetaInfoEnum('Dot1agCfmCcmInterval_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'intervalInvalid':'INTERVALINVALID',
            'interval300Hz':'INTERVAL300HZ',
            'interval10ms':'INTERVAL10MS',
            'interval100ms':'INTERVAL100MS',
            'interval1s':'INTERVAL1S',
            'interval10s':'INTERVAL10S',
            'interval1min':'INTERVAL1MIN',
            'interval10min':'INTERVAL10MIN',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmHighestDefectPri_Enum' : _MetaInfoEnum('Dot1agCfmHighestDefectPri_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'none':'NONE',
            'defRDICCM':'DEFRDICCM',
            'defMACstatus':'DEFMACSTATUS',
            'defRemoteCCM':'DEFREMOTECCM',
            'defErrorCCM':'DEFERRORCCM',
            'defXconCCM':'DEFXCONCCM',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'Dot1agCfmMaintDomainNameType_Enum' : _MetaInfoEnum('Dot1agCfmMaintDomainNameType_Enum', 'ydk.models.ieee8021.IEEE8021_CFM_MIB',
        {
            'none':'NONE',
            'dnsLikeName':'DNSLIKENAME',
            'macAddressAndUint':'MACADDRESSANDUINT',
            'charString':'CHARSTRING',
        }, 'IEEE8021-CFM-MIB', _yang_ns._namespaces['IEEE8021-CFM-MIB']),
    'IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmConfigErrorListIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object is the IfIndex of the interface.
                
                Upon a restart of the system, the system SHALL, if necessary,
                change the value of this variable so that it indexes the
                entry in the interface table with the same value of ifAlias
                that it indexed before the system restart.  If no such
                entry exists, then the system SHALL delete any entries in
                dot1agCfmConfigErrorListTable indexed by that
                InterfaceIndex value.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmconfigerrorlistifindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmConfigErrorListVid', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The VLAN ID of the VLAN with interfaces in error.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmconfigerrorlistvid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmConfigErrorListErrorType', REFERENCE_BITS, 'Dot1agCfmConfigErrors_Bits' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmConfigErrors_Bits', 
                [], [], 
                '''                A vector of Boolean error conditions from 22.2.4, any of
                which may be true:
                
                0) CFMleak;
                1) ConflictingVids;
                2) ExcessiveLevels;
                3) OverlappedLevels.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmconfigerrorlisterrortype',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmConfigErrorListEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmConfigErrorListEntry', REFERENCE_LIST, 'Dot1agCfmConfigErrorListEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry', 
                [], [], 
                '''                The Config Error List Table  entry
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmconfigerrorlistentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmConfigErrorListTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmDefaultMd' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmDefaultMd',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmDefaultMdDefIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MHFs
                created by the Default Maintenance Domain, for each
                dot1agCfmDefaultMdEntry whose dot1agCfmDefaultMdIdPermission
                object contains the value sendIdDefer.  Since, in this
                variable, there is no encompassing Maintenance Domain, the
                value sendIdDefer is not allowed.
                
                After this initialization, this object needs to be persistent
                upon reboot or restart of a device.
                ''',
                'dot1agcfmdefaultmddefidpermission',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdDefLevel', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                A value indicating the MD Level at which MHFs are to be
                created, and Sender ID TLV transmission by those MHFs is to
                be controlled, for each dot1agCfmDefaultMdEntry whose
                dot1agCfmDefaultMdLevel object contains the value -1.
                
                After this initialization, this object needs to be persistent
                upon reboot or restart of a device.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmddeflevel',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdDefMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                A value indicating if the Management entity can create MHFs
                (MIP Half Function) for the VID, for each
                dot1agCfmDefaultMdEntry whose dot1agCfmDefaultMdMhfCreation
                object contains the value defMHFdefer.  Since, in this
                variable, there is no encompassing Maintenance Domain, the
                value defMHFdefer is not allowed.
                
                After this initialization, this object needs to be persistent
                upon reboot or restart of a device.
                ''',
                'dot1agcfmdefaultmddefmhfcreation',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmDefaultMd',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmDefaultMdComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this dot1agCfmDefaultMdEntry applies.  If the system is not
                a Bridge, or if only one component is present in the Bridge,
                then this variable (index) MUST be equal to 1.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdcomponentid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmDefaultMdPrimaryVid', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The Primary VID of the VLAN to which this entry's objects
                apply.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdprimaryvid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmDefaultMdIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MHFs
                created by the Default Maintenance Domain.  If this object
                has the value sendIdDefer, Sender ID TLV transmission for
                this VLAN is controlled by dot1agCfmDefaultMdDefIdPermission.
                
                The value of this variable is meaningless if the values of
                dot1agCfmDefaultMdStatus is false.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdidpermission',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdLevel', ATTRIBUTE, 'int' , None, None, 
                [(-1, 7)], [], 
                '''                A value indicating the MD Level at which MHFs are to be
                created, and Sender ID TLV transmission by those MHFs is to
                be controlled, for the VLAN to which this entry's objects
                apply.  If this object has the value -1, the MD Level for MHF
                creation for this VLAN is controlled by
                dot1agCfmDefaultMdDefLevel.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdlevel',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                A value indicating if the Management entity can create MHFs
                (MIP Half Function) for this VID at this MD Level.  If this
                object has the value defMHFdefer, MHF creation for this VLAN
                is controlled by dot1agCfmDefaultMdDefMhfCreation.
                
                The value of this variable is meaningless if the values of
                dot1agCfmDefaultMdStatus is false.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdmhfcreation',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State of this Default MD Level table entry.  True if there is
                no entry in the Maintenance Association table defining an MA
                for the same VLAN ID and MD Level as this table's entry, and
                on which MA an Up MEP is defined, else false.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmDefaultMdEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmDefaultMdTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmDefaultMdTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmDefaultMdEntry', REFERENCE_LIST, 'Dot1agCfmDefaultMdEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry', 
                [], [], 
                '''                The Default MD Level table entry.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmDefaultMdTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmLtrReceiveOrder', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index to distinguish among multiple LTRs with the same LTR
                Transaction Identifier field value.  dot1agCfmLtrReceiveOrder
                are assigned sequentially from 1, in the order that the
                Linktrace Initiator received the LTRs.
                ''',
                'dot1agcfmltrreceiveorder',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmLtrSeqNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Transaction identifier/Sequence number returned by a previous
                transmit linktrace message command, indicating which LTM's
                response is going to be returned.
                ''',
                'dot1agcfmltrseqnumber',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                ''',
                'dot1agcfmmepidentifier',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmLtrChassisId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The Chassis ID returned in the Sender ID TLV of the LTR, if
                any. The format of this object is determined by the
                value of the dot1agCfmLtrChassisIdSubtype object.
                ''',
                'dot1agcfmltrchassisid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrChassisIdSubtype', REFERENCE_ENUM_CLASS, 'LldpChassisIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpChassisIdSubtype_Enum', 
                [], [], 
                '''                This object specifies the format of the Chassis ID returned
                in the Sender ID TLV of the LTR, if any.  This value is
                meaningless if the dot1agCfmLtrChassisId has a length of 0.
                ''',
                'dot1agcfmltrchassisidsubtype',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrEgress', REFERENCE_ENUM_CLASS, 'Dot1agCfmEgressActionFieldValue_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmEgressActionFieldValue_Enum', 
                [], [], 
                '''                The value returned in the Egress Action Field of the LTM.
                The value egrNoTlv(0) indicates that no Reply Egress TLV was
                returned in the LTM.
                ''',
                'dot1agcfmltregress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrEgressMac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address returned in the egress MAC address field.
                If the dot1agCfmLtrEgress object contains the value
                egrNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltregressmac',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrEgressPortId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Egress Port ID. The format of this object is determined by
                the value of the dot1agCfmLtrEgressPortIdSubtype object.
                If the dot1agCfmLtrEgress object contains the value
                egrNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltregressportid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrEgressPortIdSubtype', REFERENCE_ENUM_CLASS, 'LldpPortIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpPortIdSubtype_Enum', 
                [], [], 
                '''                Format of the egress Port ID.
                If the dot1agCfmLtrEgress object contains the value
                egrNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltregressportidsubtype',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrForwarded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if a LTM was forwarded by the responding MP, as
                returned in the 'FwdYes' flag of the flags field.
                ''',
                'dot1agcfmltrforwarded',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrIngress', REFERENCE_ENUM_CLASS, 'Dot1agCfmIngressActionFieldValue_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIngressActionFieldValue_Enum', 
                [], [], 
                '''                The value returned in the Ingress Action Field of the LTM.
                The value ingNoTlv(0) indicates that no Reply Ingress TLV was
                returned in the LTM.
                ''',
                'dot1agcfmltringress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrIngressMac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address returned in the ingress MAC address field.
                If the dot1agCfmLtrIngress object contains the value
                ingNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltringressmac',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrIngressPortId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Ingress Port ID. The format of this object is determined by
                the value of the dot1agCfmLtrIngressPortIdSubtype object.
                If the dot1agCfmLtrIngress object contains the value
                ingNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltringressportid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrIngressPortIdSubtype', REFERENCE_ENUM_CLASS, 'LldpPortIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpPortIdSubtype_Enum', 
                [], [], 
                '''                Format of the Ingress Port ID.
                If the dot1agCfmLtrIngress object contains the value
                ingNoTlv(0), then the contents of this object are meaningless.
                ''',
                'dot1agcfmltringressportidsubtype',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrLastEgressIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                An octet field holding the Last Egress Identifier returned
                in the LTR Egress Identifier TLV of the LTR.
                The Last Egress Identifier identifies the MEP Linktrace 
                Initiator that originated, or the Linktrace Responder that 
                forwarded, the LTM to which this LTR is the response.  This
                is the same value as the Egress Identifier TLV of that LTM.
                ''',
                'dot1agcfmltrlastegressidentifier',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrManAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(\\d*(.\\d*)*)?'], 
                '''                The TAddress that can be used to access the SNMP
                agent of the system transmitting the CCM, received in the CCM
                Sender ID TLV from that system.
                
                If the related object dot1agCfmLtrManAddressDomain contains
                the value 'zeroDotZero', this object dot1agCfmLtrManAddress
                MUST have a zero-length OCTET STRING as a value.
                ''',
                'dot1agcfmltrmanaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrManAddressDomain', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The TDomain that identifies the type and format of
                the related dot1agCfmMepDbManAddress object, used to access
                the SNMP agent of the system transmitting the LTR.  Received
                in the LTR Sender ID TLV from that system.
                
                Typical values will be one of (not all inclusive) list:
                
                
                   snmpUDPDomain          (from SNMPv2-TM, RFC3417)
                   snmpIeee802Domain      (from SNMP-IEEE802-TM-MIB, RFC4789)
                
                The value 'zeroDotZero' (from RFC2578) indicates 'no management
                address was present in the LTR', in which case the related
                object dot1agCfmMepDbManAddress MUST have a zero-length OCTET
                STRING as a value.
                ''',
                'dot1agcfmltrmanaddressdomain',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrNextEgressIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                An octet field holding the Next Egress Identifier returned
                in the LTR Egress Identifier TLV of the LTR.  The Next Egress
                Identifier Identifies the Linktrace Responder that
                transmitted this LTR, and can forward the LTM to the next
                hop.  This is the same value as the Egress Identifier TLV of
                the forwarded LTM, if any. If the FwdYes bit of the Flags
                field is false, the contents of this field are undefined,
                i.e., any value can be transmitted, and the field is ignored
                by the receiver.
                ''',
                'dot1agcfmltrnextegressidentifier',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrOrganizationSpecificTlv', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (4, 1500)], [], 
                '''                All Organization specific TLVs returned in the LTR, if
                any.  Includes all octets including and following the TLV
                Length field of each TLV, concatenated together.
                ''',
                'dot1agcfmltrorganizationspecifictlv',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrRelay', REFERENCE_ENUM_CLASS, 'Dot1agCfmRelayActionFieldValue_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmRelayActionFieldValue_Enum', 
                [], [], 
                '''                Value returned in the Relay Action field.
                ''',
                'dot1agcfmltrrelay',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrTerminalMep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A boolean value stating whether the forwarded LTM reached a
                MEP enclosing its MA, as returned in the Terminal MEP flag of
                the Flags field.
                ''',
                'dot1agcfmltrterminalmep',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrTtl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                TTL field value for a returned LTR.
                ''',
                'dot1agcfmltrttl',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmLtrEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmLtrTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmLtrTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmLtrEntry', REFERENCE_LIST, 'Dot1agCfmLtrEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry', 
                [], [], 
                '''                The Linktrace Reply table entry.
                ''',
                'dot1agcfmltrentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmLtrTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this dot1agCfmMaCompEntry applies.  If the system is not a
                Bridge, or if only one component is present in the Bridge, then
                this variable (index) MUST be equal to 1.
                	**NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacomponentid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaCompIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MPs
                configured in this MA.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacompidpermission',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaCompMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                Indicates if the Management entity can create MHFs (MIP Half
                Function) for this MA.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacompmhfcreation',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaCompNumberOfVids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of VIDs associated with the MA.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacompnumberofvids',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaCompPrimaryVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                The Primary VLAN ID with which the Maintenance Association is
                associated, or 0 if the MA is not attached to any VID.  If
                the MA is associated with more than one VID, the
                dot1agCfmVlanTable lists them.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacompprimaryvlanid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaCompRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacomprowstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaCompEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaCompTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaCompTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaCompEntry', REFERENCE_LIST, 'Dot1agCfmMaCompEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry', 
                [], [], 
                '''                The MA table entry.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacompentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaCompTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaMepListIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                MEPID
                ''',
                'dot1agcfmmameplistidentifier',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaMepListRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row. Read SNMPv2-TC (RFC1903) for an
                explanation of the possible values this object can take.
                ''',
                'dot1agcfmmameplistrowstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaMepListEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaMepListTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaMepListTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaMepListEntry', REFERENCE_LIST, 'Dot1agCfmMaMepListEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry', 
                [], [], 
                '''                The known MEPS table entry.
                ''',
                'dot1agcfmmameplistentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaMepListTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Index of the MA table dot1agCfmMdMaNextIndex needs to
                be inspected to find an available index for row-creation.
                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMaNetCcmInterval', REFERENCE_ENUM_CLASS, 'Dot1agCfmCcmInterval_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmCcmInterval_Enum', 
                [], [], 
                '''                Interval between CCM transmissions to be used by all MEPs
                in the MA.
                ''',
                'dot1agcfmmanetccminterval',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaNetFormat', REFERENCE_ENUM_CLASS, 'Dot1agCfmMaintAssocNameType_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMaintAssocNameType_Enum', 
                [], [], 
                '''                The type (and thereby format) of the Maintenance Association
                Name.
                ''',
                'dot1agcfmmanetformat',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaNetName', ATTRIBUTE, 'str' , None, None, 
                [(1, 45)], [], 
                '''                The Short Maintenance Association name. The type/format of
                this object is determined by the value of the
                dot1agCfmMaNetNameType object.  This name MUST be unique within
                a maintenance domain.
                ''',
                'dot1agcfmmanetname',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaNetRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                ''',
                'dot1agcfmmanetrowstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaNetEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMaNetTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMaNetTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaNetEntry', REFERENCE_LIST, 'Dot1agCfmMaNetEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry', 
                [], [], 
                '''                The MA table entry.
                ''',
                'dot1agcfmmanetentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMaNetTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMd' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMd',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMdTableNextIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains an unused value for dot1agCfmMdIndex in
                the dot1agCfmMdTable, or a zero to indicate that none exist.
                ''',
                'dot1agcfmmdtablenextindex',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMd',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The index to the Maintenance Domain table.
                
                dot1agCfmMdTableNextIndex needs to be inspected to find an
                available index for row-creation.
                
                Referential integrity is required, i.e., the index needs to be
                persistent upon a reboot or restart of a device.  The index
                can never be reused for other Maintenance Domain.  The index
                value SHOULD keep increasing up to the time that they wrap
                around. This is to facilitate access control based on OID.
                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdFormat', REFERENCE_ENUM_CLASS, 'Dot1agCfmMaintDomainNameType_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMaintDomainNameType_Enum', 
                [], [], 
                '''                The type (and thereby format) of the Maintenance Domain Name.
                ''',
                'dot1agcfmmdformat',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdMaNextIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Value to be used as the index of the MA table entries, both
                the dot1agCfmMaNetTable and the dot1agCfmMaCompTable, for
                this Maintenance Domain when the management entity wants to
                create a new row in those tables.
                ''',
                'dot1agcfmmdmanextindex',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdMdLevel', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Maintenance Domain Level.
                ''',
                'dot1agcfmmdmdlevel',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdMhfCreation', REFERENCE_ENUM_CLASS, 'Dot1agCfmMhfCreation_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMhfCreation_Enum', 
                [], [], 
                '''                Enumerated value indicating whether the management entity can
                create MHFs (MIP Half Function) for this Maintenance Domain.
                Since, in this variable, there is no encompassing Maintenance
                Domain, the value defMHFdefer is not allowed.
                ''',
                'dot1agcfmmdmhfcreation',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdMhfIdPermission', REFERENCE_ENUM_CLASS, 'Dot1agCfmIdPermission_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmIdPermission_Enum', 
                [], [], 
                '''                Enumerated value indicating what, if anything, is to be
                included in the Sender ID TLV (21.5.3) transmitted by MPs
                configured in this Maintenance Domain.  Since, in this
                variable, there is no encompassing Maintenance Domain, the
                value sendIdDefer is not allowed.
                ''',
                'dot1agcfmmdmhfidpermission',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdName', ATTRIBUTE, 'str' , None, None, 
                [(1, 43)], [], 
                '''                The Maintenance Domain name. The type/format of this object
                is determined by the value of the dot1agCfmMdNameType object.
                  
                Each Maintenance Domain has unique name amongst all those
                used or available to a service provider or operator.  It
                facilitates easy identification of administrative
                responsibility for each Maintenance Domain.
                
                Clause 3.24 defines a Maintenance Domain name as the
                identifier, unique over the domain for which CFM is to
                protect against accidental concatenation of Service
                Instances, of a particular Maintenance Domain.
                ''',
                'dot1agcfmmdname',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                ''',
                'dot1agcfmmdrowstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMdEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMdTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMdTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMdEntry', REFERENCE_LIST, 'Dot1agCfmMdEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry', 
                [], [], 
                '''                The Maintenance Domain table entry. This entry is not lost
                upon reboot. It is backed up by stable storage.
                ''',
                'dot1agcfmmdentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMdTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepDbRMepIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                Maintenance association End Point Identifier of a remote MEP
                whose information from the MEP Database is to be returned.
                ''',
                'dot1agcfmmepdbrmepidentifier',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                ''',
                'dot1agcfmmepidentifier',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepDbChassisId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The Chassis ID. The format of this object is determined by the
                value of the dot1agCfmLtrChassisIdSubtype object.
                ''',
                'dot1agcfmmepdbchassisid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbChassisIdSubtype', REFERENCE_ENUM_CLASS, 'LldpChassisIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpChassisIdSubtype_Enum', 
                [], [], 
                '''                This object specifies the format of the Chassis ID received
                in the last CCM.
                ''',
                'dot1agcfmmepdbchassisidsubtype',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbInterfaceStatusTlv', REFERENCE_ENUM_CLASS, 'Dot1agCfmInterfaceStatus_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmInterfaceStatus_Enum', 
                [], [], 
                '''                An enumerated value of the Interface status TLV received
                in the last CCM from the remote MEP or the default value
                isNoInterfaceStatus TLV indicating either no CCM has been
                received, or that no interface status TLV was received in
                the last CCM.
                ''',
                'dot1agcfmmepdbinterfacestatustlv',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address of the remote MEP.
                ''',
                'dot1agcfmmepdbmacaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbManAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(\\d*(.\\d*)*)?'], 
                '''                The TAddress that can be used to access the SNMP
                agent of the system transmitting the CCM, received in the CCM
                Sender ID TLV from that system.
                
                If the related object dot1agCfmMepDbManAddressDomain contains
                the value 'zeroDotZero', this object dot1agCfmMepDbManAddress
                MUST have a zero-length OCTET STRING as a value.
                ''',
                'dot1agcfmmepdbmanaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbManAddressDomain', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The TDomain that identifies the type and format of
                the related dot1agCfmMepDbManAddress object, used to access
                the SNMP agent of the system transmitting the CCM.  Received
                in the CCM Sender ID TLV from that system.
                
                Typical values will be one of (not all inclusive) list:
                
                
                   snmpUDPDomain          (from SNMPv2-TM, RFC3417)
                   snmpIeee802Domain      (from SNMP-IEEE802-TM-MIB, RFC4789)
                
                The value 'zeroDotZero' (from RFC2578) indicates 'no management
                address was present in the LTR', in which case the related
                object dot1agCfmMepDbManAddress MUST have a zero-length OCTET
                STRING as a value.
                ''',
                'dot1agcfmmepdbmanaddressdomain',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbPortStatusTlv', REFERENCE_ENUM_CLASS, 'Dot1agCfmPortStatus_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmPortStatus_Enum', 
                [], [], 
                '''                An enumerated value of the Port status TLV received in the
                last CCM from the remote MEP or the default value
                psNoPortStateTLV indicating either no CCM has been received,
                or that nor port status TLV was received in the last CCM.
                ''',
                'dot1agcfmmepdbportstatustlv',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbRdi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State of the RDI bit in the last received CCM (true for
                RDI=1), or false if none has been received.
                ''',
                'dot1agcfmmepdbrdi',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbRMepFailedOkTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time (SysUpTime) at which the IFF Remote MEP state machine
                last entered either the RMEP_FAILED or RMEP_OK state.
                ''',
                'dot1agcfmmepdbrmepfailedoktime',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbRMepState', REFERENCE_ENUM_CLASS, 'Dot1agCfmRemoteMepState_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmRemoteMepState_Enum', 
                [], [], 
                '''                The operational state of the remote MEP IFF State machines.
                ''',
                'dot1agcfmmepdbrmepstate',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMepDbEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMepDbTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMepDbTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMepDbEntry', REFERENCE_LIST, 'Dot1agCfmMepDbEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry', 
                [], [], 
                '''                The MEP Database table entry.
                ''',
                'dot1agcfmmepdbentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMepDbTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmaindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'dot1agcfmmdindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 8191)], [], 
                '''                Integer that is unique among all the MEPs in the same MA.
                Other definition is: a small integer, unique over a given
                Maintenance Association, identifying a specific Maintenance
                association End Point (3.19).
                
                MEP Identifier is also known as the MEPID.
                ''',
                'dot1agcfmmepidentifier',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmMepActive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Administrative state of the MEP
                
                A Boolean indicating the administrative state of the MEP.
                
                True indicates that the MEP is to function normally, and
                false that it is to cease functioning.
                ''',
                'dot1agcfmmepactive',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepCciEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, the MEP will generate CCM messages.
                ''',
                'dot1agcfmmepccienabled',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepCciSentCcms', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of Continuity Check messages transmitted.
                ''',
                'dot1agcfmmepccisentccms',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepCcmLtmPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The priority value for CCMs and LTMs transmitted by the MEP.
                Default Value is the highest priority value allowed to pass
                through the bridge port for any of this MEPs VIDs.
                The management entity can obtain the default value for this 
                variable from the priority regeneration table by extracting the 
                highest priority value in this table on this MEPs bridge port.
                (1 is lowest, then 2, then 0, then 3-7).
                ''',
                'dot1agcfmmepccmltmpriority',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepCcmSequenceErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of out-of-sequence CCMs received from all
                remote MEPs.
                ''',
                'dot1agcfmmepccmsequenceerrors',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDefects', REFERENCE_BITS, 'Dot1agCfmMepDefects_Bits' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMepDefects_Bits', 
                [], [], 
                '''                A vector of Boolean error conditions from Table 20-1, any of
                which may be true:
                
                DefRDICCM(0)
                DefMACstatus(1)
                DefRemoteCCM(2)
                DefErrorCCM(3)
                DefXconCCM(4)
                ''',
                'dot1agcfmmepdefects',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDirection', REFERENCE_ENUM_CLASS, 'Dot1agCfmMpDirection_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMpDirection_Enum', 
                [], [], 
                '''                The direction in which the MEP faces on the Bridge port.
                ''',
                'dot1agcfmmepdirection',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepErrorCcmLastFailure', ATTRIBUTE, 'str' , None, None, 
                [(1, 1522)], [], 
                '''                The last-received CCM that triggered an DefErrorCCM fault.
                ''',
                'dot1agcfmmeperrorccmlastfailure',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepFngAlarmTime', ATTRIBUTE, 'int' , None, None, 
                [(250, 1000)], [], 
                '''                The time that defects MUST be present before a Fault Alarm is
                issued (fngAlarmTime. 20.33.3) (default 2.5s).
                ''',
                'dot1agcfmmepfngalarmtime',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepFngResetTime', ATTRIBUTE, 'int' , None, None, 
                [(250, 1000)], [], 
                '''                The time that defects MUST be absent before resetting a
                Fault Alarm (fngResetTime, 20.33.4) (default 10s).
                ''',
                'dot1agcfmmepfngresettime',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepFngState', REFERENCE_ENUM_CLASS, 'Dot1agCfmFngState_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmFngState_Enum', 
                [], [], 
                '''                Current state of the MEP Fault Notification Generator
                State Machine.
                ''',
                'dot1agcfmmepfngstate',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepHighestPrDefect', REFERENCE_ENUM_CLASS, 'Dot1agCfmHighestDefectPri_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmHighestDefectPri_Enum', 
                [], [], 
                '''                The highest priority defect that has been present since the
                MEPs Fault Notification Generator State Machine was last in
                the FNG_RESET state.
                ''',
                'dot1agcfmmephighestprdefect',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object is the interface index of the interface either a
                bridge port, or an aggregated IEEE 802.1 link within a bridge
                port, to which the MEP is attached.
                
                Upon a restart of the system, the system SHALL, if necessary,
                change the value of this variable so that it indexes the
                entry in the interface table with the same value of ifAlias
                that it indexed before the system restart.  If no such
                entry exists, then the system SHALL set this variable to 0.
                ''',
                'dot1agcfmmepifindex',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLbrBadMsdu', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of LBRs received whose
                mac_service_data_unit did not match (except for the OpCode)
                that of the corresponding LBM (20.2.3).
                ''',
                'dot1agcfmmeplbrbadmsdu',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLbrIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of valid, in-order Loopback Replies received.
                ''',
                'dot1agcfmmeplbrin',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLbrInOutOfOrder', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of valid, out-of-order Loopback Replies
                received.
                ''',
                'dot1agcfmmeplbrinoutoforder',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLbrOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of Loopback Replies transmitted.
                ''',
                'dot1agcfmmeplbrout',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLowPrDef', REFERENCE_ENUM_CLASS, 'Dot1agCfmLowestAlarmPri_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmLowestAlarmPri_Enum', 
                [], [], 
                '''                An integer value specifying the lowest priority defect 
                that is allowed to generate fault alarm.
                ''',
                'dot1agcfmmeplowprdef',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepLtmNextSeqNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Next transaction identifier/sequence number to be sent in a
                Linktrace message. This sequence number can be zero because
                it wraps around.
                ''',
                'dot1agcfmmepltmnextseqnumber',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the MEP.
                ''',
                'dot1agcfmmepmacaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepNextLbmTransId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Next sequence number/transaction identifier to be sent in a
                Loopback message. This sequence number can be zero because
                it wraps around.
                ''',
                'dot1agcfmmepnextlbmtransid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepPrimaryVid', ATTRIBUTE, 'int' , None, None, 
                [(0, 16777215)], [], 
                '''                An integer indicating the Primary VID of the MEP, always
                one of the VIDs assigned to the MEP's MA.  The value 0
                indicates that either the Primary VID is that of the
                MEP's MA, or that the MEP's MA is associated with no VID.
                ''',
                'dot1agcfmmepprimaryvid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                ''',
                'dot1agcfmmeprowstatus',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmDataTlv', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary amount of data to be included in the Data TLV,
                if the Data TLV is selected to be sent.  The intent is to be able
                to fill the frame carrying the CFM PDU to its maximum length.
                This may lead to fragmentation in some cases.
                ''',
                'dot1agcfmmeptransmitlbmdatatlv',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmDestIsMepId', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True indicates that MEPID of the target MEP is used for
                Loopback transmission.
                False indicates that unicast destination MAC address of the
                target MEP is used for Loopback transmission.
                ''',
                'dot1agcfmmeptransmitlbmdestismepid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmDestMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The Target MAC Address Field to be transmitted: A unicast
                destination MAC address.
                This address will be used if the value of the column
                dot1agCfmMepTransmitLbmDestIsMepId is 'false'.
                ''',
                'dot1agcfmmeptransmitlbmdestmacaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmDestMepId', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                The Maintenance association End Point Identifier of another
                MEP in the same Maintenance Association to which the LBM is
                to be sent.
                This address will be used if the value of the column
                dot1agCfmMepTransmitLbmDestIsMepId is 'true'.
                ''',
                'dot1agcfmmeptransmitlbmdestmepid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmMessages', ATTRIBUTE, 'int' , None, None, 
                [(1, 1024)], [], 
                '''                The number of Loopback messages to be transmitted.
                ''',
                'dot1agcfmmeptransmitlbmmessages',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmResultOK', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the result of the operation:
                
                - true       The Loopback Message(s) will be
                             (or has been) sent.
                - false      The Loopback Message(s) will not
                             be sent.
                ''',
                'dot1agcfmmeptransmitlbmresultok',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmSeqNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Loopback Transaction Identifier
                (dot1agCfmMepNextLbmTransId) of the first LBM (to be) sent.
                 The value returned is undefined if
                 dot1agCfmMepTransmitLbmResultOK is false.
                ''',
                'dot1agcfmmeptransmitlbmseqnumber',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A Boolean flag set to true by the MEP Loopback Initiator State
                Machine or an MIB manager to indicate
                that another LBM is being transmitted.
                Reset to false by the MEP Loopback Initiator State Machine.
                ''',
                'dot1agcfmmeptransmitlbmstatus',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmVlanDropEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop Enable bit value to be used in the VLAN tag, if present
                in the transmitted frame.
                
                For more information about VLAN Drop Enable, please check
                IEEE 802.1ad.
                ''',
                'dot1agcfmmeptransmitlbmvlandropenable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLbmVlanPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Priority. 3 bit value to be used in the VLAN tag, if present
                in the transmitted frame.
                
                The default value is CCM priority.
                ''',
                'dot1agcfmmeptransmitlbmvlanpriority',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmEgressIdentifier', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                Identifies the MEP Linktrace Initiator that is originating,
                or the Linktrace Responder that is forwarding, this LTM.
                The low-order six octets contain a 48-bit IEEE MAC address
                unique to the system in which the MEP Linktrace Initiator
                or Linktrace Responder resides.  The high-order two octets
                contain a value sufficient to uniquely identify the MEP
                Linktrace Initiator or Linktrace Responder within that system.
                
                For most Bridges, the address of any MAC attached to the
                Bridge will suffice for the low-order six octets, and 0 for
                the high-order octets.  In some situations, e.g., if multiple
                virtual Bridges utilizing emulated LANs are implemented in a
                single physical system, the high-order two octets can be used
                to differentiate among the transmitting entities.
                
                The value returned is undefined if
                dot1agCfmMepTransmitLtmResult is false.
                ''',
                'dot1agcfmmeptransmitltmegressidentifier',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmFlags', REFERENCE_BITS, 'Dot1agCfmMepTransmitLtmFlags_Bits' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry.Dot1agCfmMepTransmitLtmFlags_Bits', 
                [], [], 
                '''                The flags field for LTMs transmitted by the MEP.
                ''',
                'dot1agcfmmeptransmitltmflags',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmResult', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the result of the operation:
                
                - true    The Linktrace Message will be (or has been) sent.
                - false   The Linktrace Message will not be sent
                ''',
                'dot1agcfmmeptransmitltmresult',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmSeqNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The LTM Transaction Identifier
                (dot1agCfmMepLtmNextSeqNumber) of the LTM sent.
                The value returned is undefined if
                dot1agCfmMepTransmitLtmResult is false.
                ''',
                'dot1agcfmmeptransmitltmseqnumber',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A Boolean flag set to true by the bridge port to indicate
                that another LTM may be transmitted. 
                Reset to false by the MEP Linktrace Initiator State Machine.
                ''',
                'dot1agcfmmeptransmitltmstatus',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmTargetIsMepId', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True indicates that MEPID of the target MEP is used for
                Linktrace transmission.
                False indicates that unicast destination MAC address of the
                target MEP is used for Loopback transmission.
                ''',
                'dot1agcfmmeptransmitltmtargetismepid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmTargetMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The Target MAC Address Field to be transmitted: A unicast
                destination MAC address.
                This address will be used if the value of the column
                dot1agCfmMepTransmitLtmTargetIsMepId is 'false'.
                ''',
                'dot1agcfmmeptransmitltmtargetmacaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmTargetMepId', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                An indication of the Target MAC Address Field to be
                transmitted:
                The Maintenance association End Point Identifier of
                another MEP in the same Maintenance Association
                This address will be used if the value of the column
                dot1agCfmMepTransmitLtmTargetIsMepId is 'true'.
                ''',
                'dot1agcfmmeptransmitltmtargetmepid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTransmitLtmTtl', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The LTM TTL field. Default value, if not specified, is 64.
                The TTL field indicates the number of hops remaining to the
                LTM.  Decremented by 1 by each Linktrace Responder that
                handles the LTM.  The value returned in the LTR is one less
                than that received in the LTM.  If the LTM TTL is 0 or 1, the
                LTM is not forwarded to the next hop, and if 0, no LTR is
                generated.
                ''',
                'dot1agcfmmeptransmitltmttl',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepUnexpLtrIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of unexpected LTRs received (20.39.1).
                ''',
                'dot1agcfmmepunexpltrin',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepXconCcmLastFailure', ATTRIBUTE, 'str' , None, None, 
                [(1, 1522)], [], 
                '''                The last-received CCM that triggered a DefXconCCM fault.
                ''',
                'dot1agcfmmepxconccmlastfailure',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMepEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmMepTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmMepTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmMepEntry', REFERENCE_LIST, 'Dot1agCfmMepEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry', 
                [], [], 
                '''                The MEP table entry
                ''',
                'dot1agcfmmepentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmMepTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmStackDirection', REFERENCE_ENUM_CLASS, 'Dot1agCfmMpDirection_Enum' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'Dot1agCfmMpDirection_Enum', 
                [], [], 
                '''                Direction in which the MP faces on the Bridge Port
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackdirection',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmStackifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object represents the  Bridge Port or aggregated port
                on which MEPs or MHFs might be configured.
                
                Upon a restart of the system, the system SHALL, if necessary,
                change the value of this variable, and  rearrange the
                dot1agCfmStackTable, so that it indexes the entry in the
                interface table with the same value of ifAlias that it
                indexed before the system restart.  If no such entry exists,
                then the system SHALL delete all entries in the
                dot1agCfmStackTable with the interface index.
                **NOTE: this object is deprecated due to re-indexing of
                	the table.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackifindex',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmStackMdLevel', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                MD Level of the Maintenance Point.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackmdlevel',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmStackVlanIdOrNone', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                VLAN ID to which the MP is attached, or 0, if none.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackvlanidornone',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmStackMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the MP.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackmacaddress',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmStackMaIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of the MA in the dot1agCfmMaNetTable and
                dot1agCfmMaCompTable to which the MP is associated, or 0, if
                none.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackmaindex',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmStackMdIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of the Maintenance Domain in the dot1agCfmMdTable
                to which the MP is associated, or 0, if none.
                ''',
                'dot1agcfmstackmdindex',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmStackMepId', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                If an MEP is configured, the MEPID, else 0
                ''',
                'dot1agcfmstackmepid',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmStackEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmStackTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmStackTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmStackEntry', REFERENCE_LIST, 'Dot1agCfmStackEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry', 
                [], [], 
                '''                The Stack table entry
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstackentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmStackTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmVlanComponentId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The bridge component within the system to which the information
                in this dot1agCfmVlanEntry applies.  If the system is not a
                Bridge, or if only one component is present in the Bridge, then
                this variable (index) MUST be equal to 1.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlancomponentid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmVlanVid', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                This is a VLAN ID belonging to a VLAN that is associated with
                more than one VLAN ID, and this is not the Primary VID of the
                VLAN.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlanvid',
                'IEEE8021-CFM-MIB', True),
            _MetaInfoClassMember('dot1agCfmVlanPrimaryVid', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                This is the Primary VLAN ID of the VLAN with which this
                entry's dot1agCfmVlanVid is associated.  This value MUST not
                equal the value of dot1agCfmVlanVid.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlanprimaryvid',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmVlanRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the row.
                
                The writable columns in a row can not be changed if the row
                is active. All columns MUST have a valid value before a row
                can be activated.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlanrowstatus',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmVlanEntry',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB.Dot1agCfmVlanTable' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB.Dot1agCfmVlanTable',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmVlanEntry', REFERENCE_LIST, 'Dot1agCfmVlanEntry' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry', 
                [], [], 
                '''                The VLAN table entry.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlanentry',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'dot1agCfmVlanTable',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
    'IEEE8021CFMMIB' : {
        'meta_info' : _MetaInfoClass('IEEE8021CFMMIB',
            False, 
            [
            _MetaInfoClassMember('dot1agCfmConfigErrorListTable', REFERENCE_CLASS, 'Dot1agCfmConfigErrorListTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable', 
                [], [], 
                '''                The CFM Configuration Error List table provides a list of
                Interfaces and VIDs that are incorrectly configured.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmconfigerrorlisttable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMd', REFERENCE_CLASS, 'Dot1agCfmDefaultMd' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmDefaultMd', 
                [], [], 
                '''                ''',
                'dot1agcfmdefaultmd',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmDefaultMdTable', REFERENCE_CLASS, 'Dot1agCfmDefaultMdTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmDefaultMdTable', 
                [], [], 
                '''                For each bridge component, the Default MD Level Managed Object
                controls MHF creation for VIDs that are not attached to a
                specific Maintenance Association Managed Object, and Sender ID
                TLV transmission by those MHFs.
                
                For each Bridge Port, and for each VLAN ID whose data can
                pass through that Bridge Port, an entry in this table is
                used by the algorithm in subclause 22.2.3 only if there is no
                entry in the Maintenance Association table defining an MA
                for the same VLAN ID and MD Level as this table's entry, and
                on which MA an Up MEP is defined.  If there exists such an
                MA, that MA's objects are used by the algorithm in
                subclause 22.2.3 in place of this table entry's objects.  The
                agent maintains the value of dot1agCfmDefaultMdStatus to
                indicate whether this entry is overridden by an MA.
                
                When first initialized, the agent creates this table
                automatically with entries for all VLAN IDs,
                with the default values specified for each object.
                
                After this initialization, the writable objects in this
                table need to be persistent upon reboot or restart of a
                device.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmdefaultmdtable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmLtrTable', REFERENCE_CLASS, 'Dot1agCfmLtrTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmLtrTable', 
                [], [], 
                '''                This table extends the MEP table and contains a list of
                Linktrace replies received by a specific MEP in response to
                a linktrace message.
                
                SNMP SMI does not allow to state in a MIB that an object in
                a table is an array.  The solution is to take the index (or
                indices) of the first table and add one or more indices.
                ''',
                'dot1agcfmltrtable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaCompTable', REFERENCE_CLASS, 'Dot1agCfmMaCompTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaCompTable', 
                [], [], 
                '''                The Maintenance Association table.  Each row in the table
                represents an MA.  An MA is a set of MEPs, each configured
                with a single service instance.
                
                This is the part of the complete MA table that is variable
                across the Bridges in a Maintenance Domain, or across the
                components of a single Bridge.  That part of the MA table that
                is constant across the Bridges and their components in a
                Maintenance Domain is contained in the dot1agCfmMaNetTable.
                
                This table uses three indices, first index is the
                Dot1agCfmPbbComponentIdentifier that identifies the component
                within the Bridge for which the information in the
                dot1agCfmMaCompEntry applies.  The second is the index of the
                Maintenance Domain table.  The third index is the same as the
                index of the dot1agCfmMaNetEntry for the same MA.
                
                The writable objects in this table need to be persistent
                upon reboot or restart of a device.
                
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmmacomptable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaMepListTable', REFERENCE_CLASS, 'Dot1agCfmMaMepListTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaMepListTable', 
                [], [], 
                '''                List of MEPIDs that belong to this MA.
                
                Clause 12.14.6.1.3 specifies that a list of MEPIDs in all
                bridges in that MA, but since SNMP SMI does not allow to
                state in a MIB that an object in a table is an array, the 
                information has to be stored in another table with two
                indices, being the first index, the index of the table that 
                contains the list or array.
                
                For all bridges in which the same MAID {dot1agCfmMdFormat,
                dot1agCfmMdName, dot1agCfmMaNetFormat, and dot1agCfmMaNetName}
                is configured, the same set of dot1agCfmMaMepListIdentifiers
                MUST be configured in the bridges' dot1agCfmMaMepListTables.
                This allows each MEP to determine whether or not it is
                receiving CCMs from all of the other MEPs in the MA.
                
                For example, if one were creating a new MA whose MAID were
                {charString, 'Dom1', charString, 'MA1'}, that had 2 MEPs, whose
                MEPIDs were 1 and 3, one could, in Bridge A:
                 1. Get a new MD index d from dot1agCfmMdTableNextIndex.
                 2. Create the Maintenance Domain {charString, 'Dom1'}.
                 3. Get a new MA index a from dot1agCfmMdMaNextIndex [d].
                 4. Create the Maintenance Association {charString, 'MA1'}.
                 5. Create a new dot1agCfmMaMepListEntry for each of the MEPs
                    in the MA: [d, a, 1] and [d, a, 3].
                 6. Create one of the new MEPs, say [d, a, 1].
                Then, in Bridge B:
                 7. Do all of these steps 1-6, except for using the other MEPID
                    for the new MEP in Step 6, in this example, MEPID 3.
                Note that, when creating the MA, MEP List Table, and MEP
                entries in the second bridge, the indices 'd' and 'a'
                identifying the MAID {charString, 'Dom1', charString, 'MA1'}
                may have different values than those in the first Bridge.
                ''',
                'dot1agcfmmameplisttable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMaNetTable', REFERENCE_CLASS, 'Dot1agCfmMaNetTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMaNetTable', 
                [], [], 
                '''                The Maintenance Association table.  Each row in the table
                represents an MA.  An MA is a set of MEPs, each configured
                with a single service instance.
                
                This is the part of the complete MA table that is constant
                across all Bridges in a Maintenance Domain, and across all
                components of a single Bridge.  That part of the MA table that
                can vary from Bridge component to Bridge component is contained
                in the dot1agCfmMaCompTable.
                
                Creation of a Service Instance establishes a connectionless
                association among the selected DSAPs.  Configuring a
                Maintenance association End Point (MEP) at each of the
                DSAPs creates a Maintenance Association (MA) to monitor
                that connectionless connectivity.  The MA is identified by a
                Short MA Name that is unique within the Maintenance Domain
                and chosen to facilitate easy identification of the Service
                Instance.  Together, the Maintenance Domain Name and the
                Short MA Name form the Maintenance Association Identifier
                (MAID) that is carried in CFM Messages to identify
                incorrect connectivity among Service Instances.  A small
                integer, the Maintenance association End Point Identifier
                (MEPID), identifies each MEP among those configured on a
                single MA (802.1ag clauses 3.19 and 18.2).
                
                This table uses two indices, first index is the index of the
                Maintenance Domain table.  The second index is the same as the
                index of the dot1agCfmMaCompEntry for the same MA.
                
                The writable objects in this table need to be persistent
                upon reboot or restart of a device.
                ''',
                'dot1agcfmmanettable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMd', REFERENCE_CLASS, 'Dot1agCfmMd' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMd', 
                [], [], 
                '''                ''',
                'dot1agcfmmd',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMdTable', REFERENCE_CLASS, 'Dot1agCfmMdTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMdTable', 
                [], [], 
                '''                The Maintenance Domain table. Each row in the table
                represents a different Maintenance Domain.
                
                A Maintenance Domain is described in 802.1ag (3.22) as the
                network or the part of the network for which faults in
                connectivity are to be managed. The boundary of a Maintenance
                Domain is defined by a set of DSAPs, each of which can become
                a point of connectivity to a service instance.
                ''',
                'dot1agcfmmdtable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepDbTable', REFERENCE_CLASS, 'Dot1agCfmMepDbTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMepDbTable', 
                [], [], 
                '''                The MEP Database. A database, maintained by every MEP, that
                maintains received information about other MEPs in the
                Maintenance Domain.
                
                The SMI does not allow to state in a MIB that an object in
                a table is an array. The solution is to take the index (or
                indices) of the first table and add one or more indices.
                ''',
                'dot1agcfmmepdbtable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmMepTable', REFERENCE_CLASS, 'Dot1agCfmMepTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmMepTable', 
                [], [], 
                '''                The Maintenance Association End Point (MEP) table.
                
                Each row in the table represents a different MEP.  A MEP is
                an actively managed CFM entity, associated with a specific
                DSAP of a Service Instance, which can generate and receive
                CFM PDUs and track any responses.  It is an end point of a
                single Maintenance Association, and is an endpoint of a
                separate Maintenance Entity for each of the other MEPs in
                the same Maintenance Association (802.1ag clause 3.19).
                
                This table uses three indices. The first two indices are the
                indices of the Maintenance Domain and MA tables, the reason
                being that a MEP is always related to an MA and Maintenance
                Domain.
                
                The MEP table also stores all the managed objects for sending
                LBM and LTM.
                
                *LBM Managed objects
                
                LBM Managed objects in the MEP table
                enables the management entity to initiate
                transmission of Loopback messages.  It will signal the MEP
                that it SHOULD transmit some number of Loopback messages
                and detect the detection (or lack thereof) of the
                corresponding Loopback messages.
                
                Steps to use entries in this table:
                
                1) Wait for dot1agCfmMepTransmitLbmStatus value to be
                   false.  To do this do this sequence:
                   a. an SNMP GET for both SnmpSetSerialNo and
                      dot1agCfmMepTransmitLbmStatus objects (in same SNMP
                      PDU).
                   b. Check if value for dot1agCfmMepTransmitLbmStatus is false.
                      - if not, wait x seconds, go to step a above.
                      - if yes, save the value of SnmpSetSerialNo and go
                        to step 2) below
                2) Change dot1agCfmMepTransmitLbmStatus value from false to
                   true to ensure no other management entity will use
                   the service. In order to not disturb a possible other NMS
                   do this by sending an SNMP SET for both SnmpSetSerialNo
                   and dot1agCfmMepTransmitLbmStatus objects (in same SNMP
                   PDU,  and make sure SNmpSetSerialNo is the first varBind).
                   For the SnmpSetSerialNo varBind, use the value that you
                   obtained in step 1)a.. This ensures that two cooperating
                   NMSes will not step on each others toes.
                   Setting this MIB object does not set the corresponding
                   LBIactive state machine variable.
                3) Setup the different data to be sent (number of messages,
                   optional TLVs,...), except do not set
                   dot1agCfmMepTransmitLbmMessages.
                4) Record the current values of dot1agCfmMepLbrIn,
                   dot1agCfmMepLbrInOutOfOrder, and dot1agCfmMepLbrBadMsdu.
                6) Set dot1agCfmMepTransmitLbmMessages to a non-zero value to
                   initiate transmission of Loopback messages.
                   The dot1agCfmMepTransmitLbmMessages indicates the
                   number of LBMs to be sent and is not decremented as
                   loopbacks are actually sent. dot1agCfmMepTransmitLbmMessages
                   is not equivalent to the LBMsToSend state machine variable.
                7) Check the value of dot1agCfmMepTransmitLbmResultOK to
                   find out if the operation was successfully initiated or
                   not.
                8) Monitor the value of dot1agCfmMepTransmitLbmStatus.
                   When it is reset to false, the last LBM has been transmitted.
                   Wait an additional 5 seconds to ensure that all LBRs have
                   been returned.
                9) Compare dot1agCfmMepLbrIn, dot1agCfmMepLbrInOutOfOrder,
                   and dot1agCfmMepLbrBadMsdu to their old values from step
                   4, above, to get the results of the test.
                
                *LTM Managed objects
                The LTM Managed objects in the MEP table are used in a manner
                similar to that described for LBM transmission, above.  Upon
                successfully initiating the transmission, the variables
                dot1agCfmMepTransmitLtmSeqNumber and
                dot1agCfmMepTransmitLtmEgressIdentifier return the information
                required to recover the results of the LTM from the
                dot1agCfmLtrTable.
                ''',
                'dot1agcfmmeptable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmStackTable', REFERENCE_CLASS, 'Dot1agCfmStackTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmStackTable', 
                [], [], 
                '''                There is one CFM Stack table per bridge. It permits
                the retrieval of information about the Maintenance Points
                configured on any given interface.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmstacktable',
                'IEEE8021-CFM-MIB', False),
            _MetaInfoClassMember('dot1agCfmVlanTable', REFERENCE_CLASS, 'Dot1agCfmVlanTable' , 'ydk.models.ieee8021.IEEE8021_CFM_MIB', 'IEEE8021CFMMIB.Dot1agCfmVlanTable', 
                [], [], 
                '''                This table defines the association of VIDs into VLANs.  There
                is an entry in this table, for each component of the bridge,
                for each VID that is:
                    a) a VID belonging to a VLAN associated with more than
                       one VID; and
                    b) not the Primary VLAN of that VID.
                The entry in this table contains the Primary VID of the VLAN.
                
                By default, this table is empty, meaning that every VID is
                the Primary VID of a single-VID VLAN.
                
                VLANs that are associated with only one VID SHOULD NOT have
                an entry in this table.
                
                The writable objects in this table need to be persistent
                upon reboot or restart of a device.
                **NOTE: this object is deprecated due to re-indexing of the 
                	table.
                ''',
                'dot1agcfmvlantable',
                'IEEE8021-CFM-MIB', False),
            ],
            'IEEE8021-CFM-MIB',
            'IEEE8021-CFM-MIB',
            _yang_ns._namespaces['IEEE8021-CFM-MIB'],
        'ydk.models.ieee8021.IEEE8021_CFM_MIB'
        ),
    },
}
_meta_table['IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMdTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmLtrTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMaCompTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMaMepListTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMaNetTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMdTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMepDbTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmMepTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmStackTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry']['meta_info'].parent =_meta_table['IEEE8021CFMMIB.Dot1agCfmVlanTable']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMd']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMdTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmLtrTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaCompTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaMepListTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMaNetTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMd']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMdTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMepDbTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmMepTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmStackTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']
_meta_table['IEEE8021CFMMIB.Dot1agCfmVlanTable']['meta_info'].parent =_meta_table['IEEE8021CFMMIB']['meta_info']

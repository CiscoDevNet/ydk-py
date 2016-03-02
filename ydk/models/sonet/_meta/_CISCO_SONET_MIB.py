


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CsApsLineSwitchReason_Enum' : _MetaInfoEnum('CsApsLineSwitchReason_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'csApsOther':'CSAPSOTHER',
            'csApsRevertive':'CSAPSREVERTIVE',
            'csApsManual':'CSAPSMANUAL',
            'csApsSignalDefectLow':'CSAPSSIGNALDEFECTLOW',
            'csApsSignalDefectHigh':'CSAPSSIGNALDEFECTHIGH',
            'csApsSignalFailureLow':'CSAPSSIGNALFAILURELOW',
            'csApsSignalFailureHigh':'CSAPSSIGNALFAILUREHIGH',
            'csApsForceSwitch':'CSAPSFORCESWITCH',
            'csApsLockOut':'CSAPSLOCKOUT',
            'csApsNoSwitch':'CSAPSNOSWITCH',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CsApsLineFailureCode_Enum' : _MetaInfoEnum('CsApsLineFailureCode_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'csApsChannelMismatch':'CSAPSCHANNELMISMATCH',
            'csApsProtectionByteFail':'CSAPSPROTECTIONBYTEFAIL',
            'csApsFEProtectionFailure':'CSAPSFEPROTECTIONFAILURE',
            'csApsModeMismatch':'CSAPSMODEMISMATCH',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfig' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsApsConfig',
            False, 
            [
            _MetaInfoClassMember('csApsLineFailureCode', REFERENCE_ENUM_CLASS, 'CsApsLineFailureCode_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CsApsLineFailureCode_Enum', 
                [], [], 
                '''                The object indicates the APS line failure code. This is the
                failure encountered by the APS line.
                Refer to CsApsLineFailureCode TC for failure code definitions.
                The object is used for notifications.
                ''',
                'csapslinefailurecode',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsLineSwitchReason', REFERENCE_ENUM_CLASS, 'CsApsLineSwitchReason_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CsApsLineSwitchReason_Enum', 
                [], [], 
                '''                This object indicates the APS line switch reason.
                When the working line on one end fails, its other end
                is told to do an APS switch. 
                Refer to CsApsLineSwitchReason TC for more information.
                The object is used for notifications.
                ''',
                'csapslineswitchreason',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csApsConfig',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsActiveLine_Enum' : _MetaInfoEnum('CsApsActiveLine_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'csApsWorkingLine':'CSAPSWORKINGLINE',
            'csApsProtectionLine':'CSAPSPROTECTIONLINE',
            'csApsNone':'CSAPSNONE',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchModeOperational_Enum' : _MetaInfoEnum('CsApsArchModeOperational_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'onePlusOne':'ONEPLUSONE',
            'oneToOne':'ONETOONE',
            'anexBOnePlusOne':'ANEXBONEPLUSONE',
            'ycableOnePlusOneNok1k2':'YCABLEONEPLUSONENOK1K2',
            'straightOnePlusOneNok1k2':'STRAIGHTONEPLUSONENOK1K2',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchMode_Enum' : _MetaInfoEnum('CsApsArchMode_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'onePlusOne':'ONEPLUSONE',
            'oneToOne':'ONETOONE',
            'anexBOnePlusOne':'ANEXBONEPLUSONE',
            'ycableOnePlusOneNok1k2':'YCABLEONEPLUSONENOK1K2',
            'straightOnePlusOneNok1k2':'STRAIGHTONEPLUSONENOK1K2',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsChannelProtocol_Enum' : _MetaInfoEnum('CsApsChannelProtocol_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'bellcore':'BELLCORE',
            'itu':'ITU',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirectionOperational_Enum' : _MetaInfoEnum('CsApsDirectionOperational_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'uniDirectional':'UNIDIRECTIONAL',
            'biDirectional':'BIDIRECTIONAL',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirection_Enum' : _MetaInfoEnum('CsApsDirection_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'uniDirectional':'UNIDIRECTIONAL',
            'biDirectional':'BIDIRECTIONAL',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsEnable_Enum' : _MetaInfoEnum('CsApsEnable_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'csApsDisabled':'CSAPSDISABLED',
            'csApsEnabled':'CSAPSENABLED',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsPrimarySection_Enum' : _MetaInfoEnum('CsApsPrimarySection_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'workingSection1':'WORKINGSECTION1',
            'workingSection2':'WORKINGSECTION2',
            'none':'NONE',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsRevertive_Enum' : _MetaInfoEnum('CsApsRevertive_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'nonrevertive':'NONREVERTIVE',
            'revertive':'REVERTIVE',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry',
            False, 
            [
            _MetaInfoClassMember('csApsWorkingIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                When a pair of APS lines is configured, one line has
                to be the working line, which is the primary line,
                and the other has to be the protection line, which
                is the backup line. This object refers to the working line
                in the APS pair. For G.783 AnnexB, this index refers to
                Working Section 1.
                ''',
                'csapsworkingindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('csApsActiveLine', REFERENCE_ENUM_CLASS, 'CsApsActiveLine_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsActiveLine_Enum', 
                [], [], 
                '''                This object indicates which line is currently active. 
                It could be the working line(Section 1 for Annex B),
                the protection line(Section 2 for Annex B) or none
                if neither working nor protection line is active. 
                This object reflects the status of receive direction.
                ''',
                'csapsactiveline',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsArchMode', REFERENCE_ENUM_CLASS, 'CsApsArchMode_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchMode_Enum', 
                [], [], 
                '''                This object is used to configure APS architecture mode
                on the working/protection line pairs.
                
                 All of the following are supported on single slot.
                 oneToOne(2) is not  supported across 2 slots,i.e. the 
                 working and protection slot numbers must be the same in 
                 oneToOne(2).
                
                 onePlusOne : This can be supported on the same card
                 and across 2 cards.
                 This mode means that the transmit and receive signals
                 go only over the active line(which could be working or 
                 protection line). (straight cable implied)
                
                 oneToOne : This is supported only on the same card
                 This mode means that the transmit and receive signals
                 go over the working and protection lines.
                 (straight cable implied)
                
                 anexBOnePlusOne : This can be supported on the same card
                 and across 2 cards.
                 This mode is like the onePlusOne mode, except that the
                 'csApsDirection' can only be bi-directional.
                 (straight cable implied)
                
                 ycableOnePlusOneNok1k2: With Y-cable ignore K1K2 bytes.
                 This mode is the Y-cable redundancy mode.
                
                 straightOnePlusOneNok1k2 : With straight cable, ignore 
                                            K1K2 bytes. This mode is like
                                            onePlusOne, but with K1, K2 
                                            bytes ignored.
                ''',
                'csapsarchmode',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsArchModeOperational', REFERENCE_ENUM_CLASS, 'CsApsArchModeOperational_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsArchModeOperational_Enum', 
                [], [], 
                '''                This object shows the actual APS architecture mode that
                is implemented on the Near End terminal. APS architecture
                mode configured through csApsArchMode object is 
                negotiated with the Far End through APS channel. 
                Architecture mode acceptable to both the Near End and 
                the Far End terminals is then operational at the Near 
                End. This value can be different than the APS 
                Architecture mode configured.
                ''',
                'csapsarchmodeoperational',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsChannelProtocol', REFERENCE_ENUM_CLASS, 'CsApsChannelProtocol_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsChannelProtocol_Enum', 
                [], [], 
                '''                This object allows to configure APS channel protocol to 
                be implemented at Near End terminal.
                
                K1 and K2 overhead bytes in a SONET signal are used as
                an APS channel.
                This channel is used to carry APS protocol.
                
                Possible values:
                bellcore(1) : Implements APS channel protocol as defined
                              in bellcore document GR-253-CORE.
                itu(2) : Implements APS channel protocol as defined in 
                         ITU document G.783.
                ''',
                'csapschannelprotocol',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsDirection', REFERENCE_ENUM_CLASS, 'CsApsDirection_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirection_Enum', 
                [], [], 
                '''                This object is used to configure the switching 
                direction which this APS line supports. 
                
                Unidirectional : APS switch only in one direction.
                Bidirectional  : APS switch in both ends of the line.
                ''',
                'csapsdirection',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsDirectionOperational', REFERENCE_ENUM_CLASS, 'CsApsDirectionOperational_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsDirectionOperational_Enum', 
                [], [], 
                '''                This object shows the actual APS direction that is 
                implemented on the Near End terminal. APS direction 
                configured through csApsDirection is negotiated with
                the Far End and APS direction setting acceptable to 
                both ends is operational at the Near End.
                ''',
                'csapsdirectionoperational',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsEnable', REFERENCE_ENUM_CLASS, 'CsApsEnable_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsEnable_Enum', 
                [], [], 
                '''                This object is used to enable or disable the APS feature
                on the working/protection line pairs. When enabled,
                the hardware will automatically switch the active line 
                from the working line to the protection line within 60ms,
                or vice versa.
                ''',
                'csapsenable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsFailureStatus', REFERENCE_BITS, 'CsApsLineFailureStatus_Bits' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CsApsLineFailureStatus_Bits', 
                [], [], 
                '''                This object indicates APS line failure status.
                ''',
                'csapsfailurestatus',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsPrimarySection', REFERENCE_ENUM_CLASS, 'CsApsPrimarySection_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsPrimarySection_Enum', 
                [], [], 
                '''                This object indicates which working section is the APS
                primary section. In G.783 AnnexB, the K1/K2 Bytes are
                received on the secondary Section. All the Switch
                Requests are for a switch from the primary section to
                the secondary section. The object csApsActiveline will
                indicate which section is currently carrying the
                traffic.  Once the switch request clears normally,
                traffic is maintained on the section to which it was
                switched by making that section the primary section. 
                
                Possible values: 
                workingSection1(1): Working Section 1 is Primary Section
                workingSection2(2): Working Section 2 is Primary Section
                none(3)           : none.
                ''',
                'csapsprimarysection',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsProtectionIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The protection line indicates that it will become
                the active line when an APS switch occurs (APS switch
                could occur because of a failure on the working line).
                For G.783 AnnexB, This index refers to Working Section
                2.
                ''',
                'csapsprotectionindex',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsRevertive', REFERENCE_ENUM_CLASS, 'CsApsRevertive_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry.CsApsRevertive_Enum', 
                [], [], 
                '''                This object is used to configure the APS revertive or
                nonrevertive option. 
                
                revertive : 
                  Will switch the working line back to active state after
                  the Wait-To-restore interval has expired and the 
                  working line Signal-Fault/Signal-Degrade has been 
                  cleared. Please refer to 'csApsWaitToRestore' for 
                  description of Wait-To-Restore interval.
                nonrevertive : 
                  The  protection line continues to be the active line,
                  The active line does not switch to the working line.
                ''',
                'csapsrevertive',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsSigDegradeBER', ATTRIBUTE, 'int' , None, None, 
                [(5, 9)], [], 
                '''                This object contains the Bit Error Rate threshold for
                Signal Degrade detection on the working line. Once this
                threshold is exceeded, an APS switch will occur.
                This value is 10 to -n where n is between 5 and 9.
                ''',
                'csapssigdegradeber',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsSigFaultBER', ATTRIBUTE, 'int' , None, None, 
                [(3, 5)], [], 
                '''                This object contains the Bit Error Rate threshold for
                Signal Fault detection on the working line. Once this
                threshold is exceeded, an APS switch will occur.
                This value is 10 to the -n, where n is between 3 and 5.
                ''',
                'csapssigfaultber',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsSwitchReason', REFERENCE_ENUM_CLASS, 'CsApsLineSwitchReason_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CsApsLineSwitchReason_Enum', 
                [], [], 
                '''                This object indicates APS line switch reason.
                ''',
                'csapsswitchreason',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsWaitToRestore', ATTRIBUTE, 'int' , None, None, 
                [(1, 12)], [], 
                '''                This object contains interval in minutes to wait 
                before attempting to switch back to working line. 
                Not applicable if the line is configured in 
                non-revertive mode, i.e. protection line will 
                continue to be active, even if failures on the 
                working line are cleared. The framer clears the 
                signal-fault and signal-degrade when APS switch 
                occurs. Please refer to 'csApsRevertive' for 
                description of non-revertive.
                ''',
                'csapswaittorestore',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csApsConfigEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsApsConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsApsConfigTable',
            False, 
            [
            _MetaInfoClassMember('csApsConfigEntry', REFERENCE_LIST, 'CsApsConfigEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry', 
                [], [], 
                '''                An entry is created when an APS pair is configured.
                To create an entry, the following objects must be 
                specified:
                csApsWorkingIndex, csApsProtectionIndex, csApsEnable,  
                csApsArchMode. The protection line must not be active,
                i.e, ifAdminStatus must be 'down',  while configuring 
                APS. An entry is created by setting the value of 
                'csApsEnable' to csApsEnabled (2) and deleted by 
                setting it to csApsDisabled (1). Once a line is 
                configured as working line or protection line, it 
                remains in that role until APS is disabled on that 
                sonet line pair. It remains in the  working/protection 
                role even after the card is reset.
                ''',
                'csapsconfigentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csApsConfigTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry.CsAu4Tug3Payload_Enum' : _MetaInfoEnum('CsAu4Tug3Payload_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'other':'OTHER',
            'vc11':'VC11',
            'vc12':'VC12',
            'tu3ds3':'TU3DS3',
            'tu3e3':'TU3E3',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry',
            False, 
            [
            _MetaInfoClassMember('csAu4Tug3', ATTRIBUTE, 'int' , None, None, 
                [(1, 3)], [], 
                '''                This object represents the TUG-3 number.
                ''',
                'csau4tug3',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('csAu4Tug3Payload', REFERENCE_ENUM_CLASS, 'CsAu4Tug3Payload_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry.CsAu4Tug3Payload_Enum', 
                [], [], 
                '''                This object is used for configuring the payload
                for the tributary group.
                
                The possible values are :
                
                vc11   : When set to 'vc11' following things are done:
                       - 28 entries created in ifTable for TU-11 with 
                         ifType = sonetVT(51)
                       - 28 entries created in ifTable for DS1 with 
                         ifType = ds1(18)
                
                         STM1<-AU-4<-TUG-3<-TUG-2<-TU-11<-VC11
                
                vc12   : When set to 'vc12' following things are done:
                       - 21 entries created in ifTable for TU-12 with 
                         ifType = sonetVT(51)
                       - 21 entries created in ifTable for E1 with 
                         ifType = ds1(18)
                
                         STM1<-AU-4<-TUG-3<-TUG-2<-TU-12<-VC12
                
                tu3ds3 : When set to 'tu3ds3' following things are done:
                       - 1 entry created in ifTable for TU-3 with 
                         ifType = sonetVT(51)
                       - 1 entry created in ifTable for DS3 with 
                         ifType = ds3(30)
                
                         STM1<-AU-4<-TUG-3<-TU-3<-VC3
                
                tu3e3  : When set to 'tu3e3' following things are done:
                       - 1 entry created in ifTable for TU-3 with 
                         ifType = sonetVT(51)
                       - 1 entry created in ifTable for E3 with 
                         ifType = ds3(30)
                
                         STM1<-AU-4<-TUG-3<-TU-3<-VC3
                
                The value 'other' can not be set.
                ''',
                'csau4tug3payload',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csAu4Tug3ConfigEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsAu4Tug3ConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsAu4Tug3ConfigTable',
            False, 
            [
            _MetaInfoClassMember('csAu4Tug3ConfigEntry', REFERENCE_LIST, 'CsAu4Tug3ConfigEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry', 
                [], [], 
                '''                There is an entry in this table for each TUG-3 within a 
                AU-4 SDH path that supports SDH virtual container VC-4.
                The ifIndex value represents an entry in ifTable with
                ifType = sonetPath(50).The ifTable entry applicable for
                this entry belongs to AU-4 path.
                ''',
                'csau4tug3configentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csAu4Tug3ConfigTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigFrameScramble_Enum' : _MetaInfoEnum('CsConfigFrameScramble_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigLoopbackType_Enum' : _MetaInfoEnum('CsConfigLoopbackType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'noLoopback':'NOLOOPBACK',
            'lineLocal':'LINELOCAL',
            'lineRemote':'LINEREMOTE',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIPType_Enum' : _MetaInfoEnum('CsConfigRDIPType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'onebit':'ONEBIT',
            'threebit':'THREEBIT',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIVType_Enum' : _MetaInfoEnum('CsConfigRDIVType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'onebit':'ONEBIT',
            'threebit':'THREEBIT',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigType_Enum' : _MetaInfoEnum('CsConfigType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'sonetSts3c':'SONETSTS3C',
            'sonetStm1':'SONETSTM1',
            'sonetSts12c':'SONETSTS12C',
            'sonetStm4':'SONETSTM4',
            'sonetSts48c':'SONETSTS48C',
            'sonetStm16':'SONETSTM16',
            'sonetSts192c':'SONETSTS192C',
            'sonetStm64':'SONETSTM64',
            'sonetSts3':'SONETSTS3',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigXmtClockSource_Enum' : _MetaInfoEnum('CsConfigXmtClockSource_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'loopTiming':'LOOPTIMING',
            'localTiming':'LOCALTIMING',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsSignallingTransportMode_Enum' : _MetaInfoEnum('CsSignallingTransportMode_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'signallingTransferMode':'SIGNALLINGTRANSFERMODE',
            'clearMode':'CLEARMODE',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryFramingType_Enum' : _MetaInfoEnum('CsTributaryFramingType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'dsx1D4':'DSX1D4',
            'dsx1ESF':'DSX1ESF',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryGroupingType_Enum' : _MetaInfoEnum('CsTributaryGroupingType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'au3Grouping':'AU3GROUPING',
            'au4Grouping':'AU4GROUPING',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryMappingType_Enum' : _MetaInfoEnum('CsTributaryMappingType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'asynchronous':'ASYNCHRONOUS',
            'byteSynchronous':'BYTESYNCHRONOUS',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryType_Enum' : _MetaInfoEnum('CsTributaryType_Enum', 'ydk.models.sonet.CISCO_SONET_MIB',
        {
            'vt15vc11':'VT15VC11',
            'vt2vc12':'VT2VC12',
        }, 'CISCO-SONET-MIB', _yang_ns._namespaces['CISCO-SONET-MIB']),
    'CISCOSONETMIB.CsConfigTable.CsConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsConfigTable.CsConfigEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('csConfigFrameScramble', REFERENCE_ENUM_CLASS, 'CsConfigFrameScramble_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigFrameScramble_Enum', 
                [], [], 
                '''                This object is used to disable or enable the Scrambling
                option in SONET line.
                ''',
                'csconfigframescramble',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigLoopbackType', REFERENCE_ENUM_CLASS, 'CsConfigLoopbackType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigLoopbackType_Enum', 
                [], [], 
                '''                This object specifies the desired loopback mode
                configuration of the SONET line.
                The possible values of this objects are follows:
                
                noLoopback :  
                        Not in the loopback state.  
                lineLocal : 
                        The signal transmitted from this interface
                        is connected to the associated incoming
                        receiver. This ensures that the SONET frame
                        transmitted from the interface is received back
                        at the interface.
                lineRemote :
                        The signal received at the interface is looped
                        back out to the associated transmitter.
                        This ensures that the remote equipment that
                        originated the signal receives it back. The 
                        signal may undergo degradation as a result of
                        the characteristics of the transmission 
                        medium.
                ''',
                'csconfigloopbacktype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigRDIPType', REFERENCE_ENUM_CLASS, 'CsConfigRDIPType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIPType_Enum', 
                [], [], 
                '''                This object represents the type of RDI-P (Remote Defect
                Indication - Path) sent by this Network Element (NE)
                to remote Network Element.
                
                      onebit     : use 1 bit RDI-P
                      threebit   : use 3 bit enhanced RDI-P.
                
                Default is onebit.
                ''',
                'csconfigrdiptype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigRDIVType', REFERENCE_ENUM_CLASS, 'CsConfigRDIVType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigRDIVType_Enum', 
                [], [], 
                '''                This object specifies the type of RDI-V (Remote Defect
                Indication - Virtual Tributary/Container) sent by this 
                Network Element (NE) to the remote Network Element.
                
                      onebit     : use 1 bit RDI-V
                      threebit   : use 3 bit enhanced RDI-V.
                
                Default is onebit.
                ''',
                'csconfigrdivtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigType', REFERENCE_ENUM_CLASS, 'CsConfigType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigType_Enum', 
                [], [], 
                '''                This object represents the configured line type.
                Sts is SONET format. Stm is SDH format. 
                    sonetSts3c   : OC3 concatenated
                    sonetStm1    : European standard OC3
                    sonetSts12c  : OC12 concatenated
                    sonetStm4    : European standard OC12
                    sonetSts48c  : OC48 concatenated
                    sonetStm16   : European standard OC48 
                    sonetSts192c : OC-192 concatenated
                    sonetStm64   : European standard OC-192
                    sonetSts3    : OC3 (unconcatenated)
                    
                ''',
                'csconfigtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigXmtClockSource', REFERENCE_ENUM_CLASS, 'CsConfigXmtClockSource_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsConfigXmtClockSource_Enum', 
                [], [], 
                '''                Specifies the source of the transmit clock.
                
                loopTiming: indicates that the recovered receive 
                            clock is used as the transmit clock.
                
                localTiming: indicates that a local clock source is
                             used or that an external clock is 
                             attached to the box containing the 
                             interface. 
                ''',
                'csconfigxmtclocksource',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csSignallingTransportMode', REFERENCE_ENUM_CLASS, 'CsSignallingTransportMode_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsSignallingTransportMode_Enum', 
                [], [], 
                '''                This object represents the mode used to transport DS0 
                signalling information for T1 byteSynchronous mapping (GR253).
                In signallingTransferMode(2), the robbed-bit signalling is 
                transferred to the VT header. In clearMode(3), only the 
                framing bit is transferred to the VT header.
                     
                Default is signallingTransferMode(2) if csTributaryMappingType 
                is byteSynchronous. For asynchronous mapping, it is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.
                ''',
                'cssignallingtransportmode',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csTributaryFramingType', REFERENCE_ENUM_CLASS, 'CsTributaryFramingType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryFramingType_Enum', 
                [], [], 
                '''                This object represents the framing type to be assigned to the
                virtual tributaries in byte sync mapping mode.
                
                      notApplicable  :  If VT mapping is not byteSynchronous(2).
                      dsx1ESF        :  Extended Superframe Format
                      dsx1D4         :  Superframe Format
                
                Default is dsx1ESF(3) if csTributaryMappingType is 
                byteSynchronous(2). For asynchronous(1) mapping, the default is 
                notApplicable(1).
                
                The value notApplicable(1) can not be set.
                ''',
                'cstributaryframingtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csTributaryGroupingType', REFERENCE_ENUM_CLASS, 'CsTributaryGroupingType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryGroupingType_Enum', 
                [], [], 
                '''                This object represents the method used to group VCs into an
                STM-1 signal. Applicable only to SDH.
                
                  au3Grouping: STM1<-AU-3<-TUG-2<-TU-12<-VC12 or
                               STM1<-AU-3<-TUG-2<-TU-11<-VC11.
                
                  au4Grouping: STM1<-AU-4<-TUG-3<-TUG-2<-TU-12<-VC12 or
                               STM1<-AU-4<-TUG-3<-TUG-2<-TU-11<-VC11.
                
                Default is au3Grouping(2) for SDH and notApplicable(1) for SONET.
                ''',
                'cstributarygroupingtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csTributaryMappingType', REFERENCE_ENUM_CLASS, 'CsTributaryMappingType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryMappingType_Enum', 
                [], [], 
                '''                This object represents the VT/VC mapping type.
                
                asynchronous:    In this mode, the channel structure of 
                                 DS1/E1 is neither visible nor preserved.
                
                byteSynchronous: In this mode, the DS0 signals inside the
                                 VT/VC can be found and extracted from the
                                 frame.
                
                Default is asynchronous(1).
                ''',
                'cstributarymappingtype',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csTributaryType', REFERENCE_ENUM_CLASS, 'CsTributaryType_Enum' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry.CsTributaryType_Enum', 
                [], [], 
                '''                Type of the tributary carried within the SONET/SDH signal.
                
                vt15vc11    : carries T1 signal
                vt2vc12     : carries E1 signal
                ''',
                'cstributarytype',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csConfigEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsConfigTable',
            False, 
            [
            _MetaInfoClassMember('csConfigEntry', REFERENCE_LIST, 'CsConfigEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable.CsConfigEntry', 
                [], [], 
                '''                An entry in the table. There is an entry for each SONET line 
                in the table. Entries are automatically created for an 
                ifType value of sonet(39). 'ifAdminStatus' from the ifTable 
                must be used to enable or disable a line. A line is in 
                disabled(down) state unless provisioned 'up' using 
                'ifAdminStatus'.
                ''',
                'csconfigentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csConfigTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsNotifications' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsNotifications',
            False, 
            [
            _MetaInfoClassMember('csNotificationsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object controls if the generation of 
                ciscoSonetSectionStatusChange, ciscoSonetLineStatusChange, 
                ciscoSonetPathStatusChange and ciscoSonetVTStatusChange
                notifications is enabled. If the value of this object
                is 'true(1)', then all notifications in this MIB are
                enabled; otherwise they are disabled.
                ''',
                'csnotificationsenabled',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csNotifications',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsStatsTable.CsStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsStatsTable.CsStatsEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cslAISs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of alarm indication signals(AIS)  encountered by 
                a SONET/SDH Line. A high value for this object may indicate a
                problem with the Sonet Line layer.
                ''',
                'cslaiss',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslRFIs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of remote failure indications (RFI) encountered 
                by a SONET/SDH Line. A high value for this object may 
                indicate a problem with the Sonet Line layer.
                ''',
                'cslrfis',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspAISs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The  number of alarm indication signals (AIS) encountered
                by a SONET/SDH Path. A high value for this object may 
                indicate a problem with the Sonet Path layer.
                ''',
                'cspaiss',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspRFIs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of  remote failure indications (RFI) 
                encountered by a SONET/SDH Path. A high value for this 
                object may indicate a problem with the Sonet Path layer.
                ''',
                'csprfis',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssLOFs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Loss of Frames (LOF) encountered by a 
                SONET/SDH Section. A high value for this object may 
                indicate a problem with the Sonet Section layer.
                ''',
                'csslofs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssLOSs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Loss of signals(LOS) encountered by a 
                SONET/SDH Section. A high value for this object may 
                indicate a problem with the Sonet Section layer.
                ''',
                'cssloss',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csStatsEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CsStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CsStatsTable',
            False, 
            [
            _MetaInfoClassMember('csStatsEntry', REFERENCE_LIST, 'CsStatsEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsStatsTable.CsStatsEntry', 
                [], [], 
                '''                An entry in the SONET/SDH statistics table. These are 
                realtime statistics for the Sonet section, line and path
                layers. The statistics are gathered for each sonet line. 
                An entry is created automatically and is indexed by 
                ifIndex.
                ''',
                'csstatsentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'csStatsTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cslFarEndTotalCVs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Coding Violations encountered by a SONET/SDH 
                Far End Line in the last 24 hours.
                ''',
                'cslfarendtotalcvs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslFarEndTotalESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Errored Seconds encountered by a SONET/SDH Far
                End Line in the last 24 hours.
                ''',
                'cslfarendtotaless',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslFarEndTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Seconds encountered by a 
                SONET/SDH Far End Line in the last 24 hours.
                ''',
                'cslfarendtotalsess',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslFarEndTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Unavailable Seconds encountered by a 
                SONET/SDH Far End Line in the last 24 hours.
                ''',
                'cslfarendtotaluass',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cslFarEndTotalEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CslFarEndTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CslFarEndTotalTable',
            False, 
            [
            _MetaInfoClassMember('cslFarEndTotalEntry', REFERENCE_LIST, 'CslFarEndTotalEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Far End Line Total table. Entries
                are created automatically for sonet lines.
                ''',
                'cslfarendtotalentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cslFarEndTotalTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CslTotalTable.CslTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CslTotalTable.CslTotalEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cslTotalCVs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Coding Violations encountered by a 
                SONET/SDH Line in the last 24 hours.
                ''',
                'csltotalcvs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslTotalESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Errored Seconds encountered by a SONET/SDH
                Line in the last 24 hours.
                ''',
                'csltotaless',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Seconds encountered by a 
                SONET/SDH Line in the last 24 hours.
                ''',
                'csltotalsess',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Unavailable Seconds encountered by a 
                SONET/SDH Line in the last 24 hours.
                ''',
                'csltotaluass',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cslTotalEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CslTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CslTotalTable',
            False, 
            [
            _MetaInfoClassMember('cslTotalEntry', REFERENCE_LIST, 'CslTotalEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CslTotalTable.CslTotalEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Line Total table. Entries
                are created automatically for sonet lines.
                ''',
                'csltotalentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cslTotalTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cspFarEndTotalCVs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Coding Violations encountered by a 
                SONET/SDH far end path in the last 24 hours.
                ''',
                'cspfarendtotalcvs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspFarEndTotalESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Errored Seconds encountered by a SONET/SDH
                far end path in the last 24 hours.
                ''',
                'cspfarendtotaless',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspFarEndTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Seconds encountered by a 
                SONET/SDH far end path in the last 24 hours.
                ''',
                'cspfarendtotalsess',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspFarEndTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Unavailable Seconds encountered by a 
                SONET/SDH far end path in the last 24 hours.
                ''',
                'cspfarendtotaluass',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspFarEndTotalEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspFarEndTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspFarEndTotalTable',
            False, 
            [
            _MetaInfoClassMember('cspFarEndTotalEntry', REFERENCE_LIST, 'CspFarEndTotalEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Far End Path Total table. 
                Entries are created automatically for sonet lines.
                ''',
                'cspfarendtotalentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspFarEndTotalTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspTotalTable.CspTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspTotalTable.CspTotalEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cspTotalCVs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Coding Violations encountered by a 
                SONET/SDH Path in the last 24 hours.
                ''',
                'csptotalcvs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTotalESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Errored Seconds encountered by a SONET/SDH
                Path in the last 24 hours.
                ''',
                'csptotaless',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Seconds encountered by a 
                SONET/SDH Path in the last 24 hours.
                ''',
                'csptotalsess',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTotalUASs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Unavailable Seconds encountered by a 
                SONET/SDH Path in the last 24 hours.
                ''',
                'csptotaluass',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspTotalEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspTotalTable',
            False, 
            [
            _MetaInfoClassMember('cspTotalEntry', REFERENCE_LIST, 'CspTotalEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspTotalTable.CspTotalEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Path Total table. Entries
                are created automatically for sonet lines.
                ''',
                'csptotalentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspTotalTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspTraceTable.CspTraceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspTraceTable.CspTraceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cspTraceFailure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of this object is set to 'true' when Sonet Path 
                received trace does not match the 'cspTraceToExpect'.
                ''',
                'csptracefailure',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTraceReceived', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                This object is used to view the Sonet Path Trace that is
                received by the receiving terminal.
                ''',
                'csptracereceived',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTraceToExpect', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                Sonet Path Trace To Expect.  The receiving terminal verifies
                if the incoming string matches this string. The value of 
                'cspTraceFailure' indicates whether a trace mismatch 
                occured. The default value is a zero-length string.
                ''',
                'csptracetoexpect',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTraceToTransmit', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                Sonet Path Trace To Transmit. The trace string is 
                repetitively transmited so that a trace receiving terminal 
                can verify its continued receiving terminal can verify its 
                continued connection to the intended transmitter. The 
                default value is a zero-length string. Unless this object 
                is set to a non-zero length string, tracing will not be 
                performed.
                ''',
                'csptracetotransmit',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspTraceEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CspTraceTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CspTraceTable',
            False, 
            [
            _MetaInfoClassMember('cspTraceEntry', REFERENCE_LIST, 'CspTraceEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspTraceTable.CspTraceEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Path Trace table. The entries 
                exist for active sonet lines. The objects in this table are 
                used to verify continued connection between the two ends of
                the line.
                ''',
                'csptraceentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cspTraceTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CssTotalTable.CssTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CssTotalTable.CssTotalEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cssTotalCVs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Coding Violations encountered by a 
                SONET/SDH Section in the last 24 hours.
                ''',
                'csstotalcvs',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTotalESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Errored Seconds encountered by a SONET/SDH
                Section in the last 24 hours.
                ''',
                'csstotaless',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTotalSEFSs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Framing Seconds 
                encountered by a SONET/SDH Section in the last 24 hours.
                ''',
                'csstotalsefss',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTotalSESs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Severely Errored Seconds encountered by a 
                SONET/SDH Section in the last 24 hours.
                ''',
                'csstotalsess',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cssTotalEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CssTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CssTotalTable',
            False, 
            [
            _MetaInfoClassMember('cssTotalEntry', REFERENCE_LIST, 'CssTotalEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CssTotalTable.CssTotalEntry', 
                [], [], 
                '''                An entry in the SONET/SDH Section Total table. Entries
                are created automatically for sonet lines.
                ''',
                'csstotalentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cssTotalTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CssTraceTable.CssTraceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CssTraceTable.CssTraceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-SONET-MIB', True),
            _MetaInfoClassMember('cssTraceFailure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of this object is set to 'true' when Sonet 
                Section received trace does not match the 
                'cssTraceToExpect'.
                ''',
                'csstracefailure',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTraceReceived', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                This object is used to view the Sonet Section Trace that 
                is received by the receiving terminal.
                ''',
                'csstracereceived',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTraceToExpect', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                Sonet Section Trace To Expect. The receiving terminal 
                verifies if the incoming string matches this string. 
                The value of 'cssTraceFailure' indicates whether a 
                trace mismatch occurred. The default value is a 
                zero-length string.
                ''',
                'csstracetoexpect',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTraceToTransmit', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (16, None), (64, None)], [], 
                '''                Sonet Section Trace To Transmit. This is string that
                is transmitted to perform Sonet section trace 
                diagnostics. The trace string is  repetitively 
                transmited so that a trace receiving terminal can 
                verify its continued connection to the intended 
                transmitter. The default value is a zero-length string.
                Unless this object is set to a non-zero length string, 
                tracing will not be performed.
                ''',
                'csstracetotransmit',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cssTraceEntry',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB.CssTraceTable' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB.CssTraceTable',
            False, 
            [
            _MetaInfoClassMember('cssTraceEntry', REFERENCE_LIST, 'CssTraceEntry' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CssTraceTable.CssTraceEntry', 
                [], [], 
                '''                An entry in the trace table. Entries exist for active sonet
                lines. The objects in this table are used to verify 
                continued connection between the two ends of the line.
                ''',
                'csstraceentry',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'cssTraceTable',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
    'CISCOSONETMIB' : {
        'meta_info' : _MetaInfoClass('CISCOSONETMIB',
            False, 
            [
            _MetaInfoClassMember('csApsConfig', REFERENCE_CLASS, 'CsApsConfig' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfig', 
                [], [], 
                '''                ''',
                'csapsconfig',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csApsConfigTable', REFERENCE_CLASS, 'CsApsConfigTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsApsConfigTable', 
                [], [], 
                '''                This table contains objects to configure APS 
                (Automatic Protection Switching) feature in a SONET 
                Line. APS is the ability to configure a pair of SONET 
                lines for redundancy so that the hardware will 
                automatically switch the active line from working line
                to the protection line or vice versa, within 60ms, 
                when the active line fails.
                ''',
                'csapsconfigtable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csAu4Tug3ConfigTable', REFERENCE_CLASS, 'CsAu4Tug3ConfigTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsAu4Tug3ConfigTable', 
                [], [], 
                '''                This table contains objects to configure the VC( Virtual
                Container) related properties of a TUG-3 within a AU-4 
                paths.
                
                This table allows creation of
                following multiplexing structure:
                STM-1/AU-4/TUG-3/TU-3/DS3
                STM-1/AU-4/TUG-3/TU-3/E3
                STM-1/AU-4/TUG-3/TUG-2/TU-11/DS1
                STM-1/AU-4/TUG-3/TUG-2/TU-12/E1
                
                Three entries are created in this table for a given AU-4 
                path when cspSonetPathPayload object is set to one of the 
                following:
                    vt15vc11(4),
                    vt2vc12(5),
                    ds3(3),
                    e3(8),
                    vtStructured(9)
                ''',
                'csau4tug3configtable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csConfigTable', REFERENCE_CLASS, 'CsConfigTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsConfigTable', 
                [], [], 
                '''                The SONET/SDH configuration table. This table has objects 
                for configuring sonet lines.
                ''',
                'csconfigtable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslFarEndTotalTable', REFERENCE_CLASS, 'CslFarEndTotalTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CslFarEndTotalTable', 
                [], [], 
                '''                The SONET/SDH Far End Line Total table. It contains the 
                cumulative sum of the various statistics for the 24 hour 
                period preceding the current interval. The object 
                'sonetMediumValidIntervals' from RFC2558 contains the 
                number of 15 minute intervals that have elapsed since the 
                line is enabled.
                ''',
                'cslfarendtotaltable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cslTotalTable', REFERENCE_CLASS, 'CslTotalTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CslTotalTable', 
                [], [], 
                '''                The SONET/SDH Line Total table. It contains the 
                cumulative sum of the various statistics for the 24 
                hour period preceding the current interval. The object 
                'sonetMediumValidIntervals' from RFC2558 contains the 
                number of 15 minute intervals that have elapsed since
                the line is enabled.
                ''',
                'csltotaltable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csNotifications', REFERENCE_CLASS, 'CsNotifications' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsNotifications', 
                [], [], 
                '''                ''',
                'csnotifications',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspFarEndTotalTable', REFERENCE_CLASS, 'CspFarEndTotalTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspFarEndTotalTable', 
                [], [], 
                '''                The SONET/SDH Far End Path Total table. Far End is the 
                remote end of the line. The table contains the cumulative
                sum of the various statistics for the 24 hour period 
                preceding the current interval. The object 
                'sonetMediumValidIntervals' from RFC2558 contains the
                number of 15 minute intervals that have elapsed since
                the line is enabled. 
                ''',
                'cspfarendtotaltable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTotalTable', REFERENCE_CLASS, 'CspTotalTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspTotalTable', 
                [], [], 
                '''                The SONET/SDH Path Total table. It contains the cumulative 
                sum of the various statistics for the 24 hour period 
                preceding the current interval.The object 
                'sonetMediumValidIntervals' from RFC2558 contains the number
                of 15 minute intervals that have elapsed since the line is 
                enabled.
                ''',
                'csptotaltable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cspTraceTable', REFERENCE_CLASS, 'CspTraceTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CspTraceTable', 
                [], [], 
                '''                The SONET/SDH Path Trace table. This table contains objects 
                for tracing the sonet path.
                ''',
                'csptracetable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('csStatsTable', REFERENCE_CLASS, 'CsStatsTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CsStatsTable', 
                [], [], 
                '''                The SONET/SDH Section statistics table. This table 
                maintains the number of times the line encountered Loss of
                Signal(LOS), Loss of frame(LOF), Alarm Indication 
                signals(AISs), Remote failure indications(RFIs).
                ''',
                'csstatstable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTotalTable', REFERENCE_CLASS, 'CssTotalTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CssTotalTable', 
                [], [], 
                '''                The SONET/SDH Section Total table. It contains the 
                cumulative sum of the various statistics for the 24 hour
                period preceding the current interval. The object 
                'sonetMediumValidIntervals' from RFC2558 contains the
                number of 15 minute intervals that have elapsed since
                the line is enabled. 
                ''',
                'csstotaltable',
                'CISCO-SONET-MIB', False),
            _MetaInfoClassMember('cssTraceTable', REFERENCE_CLASS, 'CssTraceTable' , 'ydk.models.sonet.CISCO_SONET_MIB', 'CISCOSONETMIB.CssTraceTable', 
                [], [], 
                '''                The SONET/SDH Section Trace table. This table contains 
                objects for tracing the sonet section.
                ''',
                'csstracetable',
                'CISCO-SONET-MIB', False),
            ],
            'CISCO-SONET-MIB',
            'CISCO-SONET-MIB',
            _yang_ns._namespaces['CISCO-SONET-MIB'],
        'ydk.models.sonet.CISCO_SONET_MIB'
        ),
    },
}
_meta_table['CISCOSONETMIB.CsApsConfigTable.CsApsConfigEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CsApsConfigTable']['meta_info']
_meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable.CsAu4Tug3ConfigEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable']['meta_info']
_meta_table['CISCOSONETMIB.CsConfigTable.CsConfigEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CsConfigTable']['meta_info']
_meta_table['CISCOSONETMIB.CsStatsTable.CsStatsEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CsStatsTable']['meta_info']
_meta_table['CISCOSONETMIB.CslFarEndTotalTable.CslFarEndTotalEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CslFarEndTotalTable']['meta_info']
_meta_table['CISCOSONETMIB.CslTotalTable.CslTotalEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CslTotalTable']['meta_info']
_meta_table['CISCOSONETMIB.CspFarEndTotalTable.CspFarEndTotalEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CspFarEndTotalTable']['meta_info']
_meta_table['CISCOSONETMIB.CspTotalTable.CspTotalEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CspTotalTable']['meta_info']
_meta_table['CISCOSONETMIB.CspTraceTable.CspTraceEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CspTraceTable']['meta_info']
_meta_table['CISCOSONETMIB.CssTotalTable.CssTotalEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CssTotalTable']['meta_info']
_meta_table['CISCOSONETMIB.CssTraceTable.CssTraceEntry']['meta_info'].parent =_meta_table['CISCOSONETMIB.CssTraceTable']['meta_info']
_meta_table['CISCOSONETMIB.CsApsConfig']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CsApsConfigTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CsAu4Tug3ConfigTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CsConfigTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CsNotifications']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CsStatsTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CslFarEndTotalTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CslTotalTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CspFarEndTotalTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CspTotalTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CspTraceTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CssTotalTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']
_meta_table['CISCOSONETMIB.CssTraceTable']['meta_info'].parent =_meta_table['CISCOSONETMIB']['meta_info']

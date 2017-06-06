


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoStpExtensionsMib.Stpxuplinkfastobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxuplinkfastobjects',
            False, 
            [
            _MetaInfoClassMember('stpxUplinkFastEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the UplinkFast capability is
                administratively enabled on the device.
                
                If the platform does not support configuration of this
                object when the object value of stpxSpanningTreeType is 
                mst(4), then this object is not instantiated.
                ''',
                'stpxuplinkfastenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkFastOperEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the UplinkFast capability is 
                operationally enabled on the device.
                ''',
                'stpxuplinkfastoperenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkFastTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cumulative number of UplinkFast transitions (from
                the STP 'Blocking' state directly to the STP 'Forwarding'
                state).  All transitions are included in this counter,
                irrespective of the instance of the Spanning Tree 
                Protocol on which they occur.
                
                If the platform supports the stpxUplinkFastOperEnabled 
                object, then this object is not instantiated when the 
                object value of stpxUplinkFastOperEnabled is false(2).
                If the platform does not support the 
                stpxUplinkFastOperEnabled object, then this object is 
                not instantiated when the object value of 
                stpxSpanningTreeType is mst(4).
                ''',
                'stpxuplinkfasttransitions',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkStationLearningFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cumulative number of station-learning frames generated
                due to UplinkFast transitions.  All generated
                station-learning frames are included in this counter,
                irrespective of the instance of the Spanning Tree Protocol
                on which the UplinkFast transition occurred.
                
                If the platform supports the stpxUplinkFastOperEnabled 
                object, then this object is not instantiated when the 
                object value of stpxUplinkFastOperEnabled is false(2).
                If the platform does not support the 
                stpxUplinkFastOperEnabled object, then this object is 
                not instantiated when the object value of 
                stpxSpanningTreeType is mst(4).
                ''',
                'stpxuplinkstationlearningframes',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkStationLearningGenRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '32000')], [], 
                '''                The maximum number of station-learning frames that this
                device will generate in each 100 milli-second period after
                a UplinkFast transition.  By configuring this object, the
                network administrator can limit the rate at which
                station-learning frames are generated.  
                
                If the platform does not support configuration of this
                object when the object value of stpxSpanningTreeType is
                mst(4), then this object is not instantiated.
                ''',
                'stpxuplinkstationlearninggenrate',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxUplinkFastObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxbackbonefastobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxbackbonefastobjects',
            False, 
            [
            _MetaInfoClassMember('stpxBackboneFastEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the BackboneFast capability is
                administratively enabled on the device.
                ''',
                'stpxbackbonefastenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastInInferiorBPDUs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of inferior BPDUs received by the switch 
                since the stpxBackboneFastOperEnabled has
                become true(1). If the value of 
                stpxBackboneFastOperEnabled is false(2), then this 
                mib object will have a value of 0.
                ''',
                'stpxbackbonefastininferiorbpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastInRLQRequestPDUs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Root Link Query request PDUs received by the
                switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastinrlqrequestpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastInRLQResponsePDUs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Root Link Query response PDUs received by the
                switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastinrlqresponsepdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastOperEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the BackboneFast capability is
                operationally enabled on the device.
                ''',
                'stpxbackbonefastoperenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastOutRLQRequestPDUs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Root Link Query request PDUs transmitted by
                the switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastoutrlqrequestpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastOutRLQResponsePDUs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Root Link Query response PDUs transmitted by
                the switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastoutrlqresponsepdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxBackboneFastObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreepathcostmodeEnum' : _MetaInfoEnum('StpxspanningtreepathcostmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'short':'short',
            'long':'long',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreepathcostopermodeEnum' : _MetaInfoEnum('StpxspanningtreepathcostopermodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'short':'short',
            'long':'long',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreetypeEnum' : _MetaInfoEnum('StpxspanningtreetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'pvstPlus':'pvstPlus',
            'mistp':'mistp',
            'mistpPvstPlus':'mistpPvstPlus',
            'mst':'mst',
            'rapidPvstPlus':'rapidPvstPlus',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxspanningtreeobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxspanningtreeobjects',
            False, 
            [
            _MetaInfoClassMember('stpxExtendedSysIDAdminEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Extended System ID feature 
                is administratively enabled on the device or not.
                ''',
                'stpxextendedsysidadminenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxExtendedSysIDOperEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Extended System ID feature 
                is operationaly enabled on the device or not.
                
                If the value of this object is true(1), then
                the accepted values for dot1dStpPriority
                in BRIDGE-MIB should be multiples of 4096 plus
                bridge instance ID, such as VlanIndex. Changing
                this object value might cause the values of
                dot1dBaseBridgeAddress and dot1dStpPriority
                in BRIDGE-MIB to be changed also.
                ''',
                'stpxextendedsysidoperenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxNotificationEnable', REFERENCE_BITS, 'Stpxnotificationenable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxspanningtreeobjects.Stpxnotificationenable', 
                [], [], 
                '''                Indicates whether a specified notification is enabled or not.
                If a bit corresponding to a notification is set to 1, then 
                the specified notification can be generated.
                
                newRoot -- the newRoot notification as defined in BRIDGE-MIB.
                
                topologyChange -- the topologyChange notification as
                                  defined in BRIDGE-MIB.
                
                inconsistency -- the stpxInconsistencyUpdate notification.
                
                rootInconsistency -- the stpxRootInconsistencyUpdate 
                                     notification.
                
                loopInconsistency -- the stpxLoopInconsistencyUpdate 
                                     notification.
                ''',
                'stpxnotificationenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreePathCostMode', REFERENCE_ENUM_CLASS, 'StpxspanningtreepathcostmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreepathcostmodeEnum', 
                [], [], 
                '''                Indicates the administrative  spanning tree path cost mode 
                configured on device.
                ''',
                'stpxspanningtreepathcostmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreePathCostOperMode', REFERENCE_ENUM_CLASS, 'StpxspanningtreepathcostopermodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreepathcostopermodeEnum', 
                [], [], 
                '''                Indicate the operational spanning tree path cost mode
                on device. This mode applies to all instances of the Spanning
                Tree protocol running on the device. 
                
                When the value of this MIB object gets changed, the path cost
                of all ports will be reassigned to the default path cost
                values based on the new spanning tree path cost mode and the
                ports' speed.
                
                When the value of this MIB object is long(2),
                the stpxLongStpPortPathCost MIB object must be used in order
                to retrieve/configure the spanning tree port path cost as a
                32 bits value. The set operation on dot1dStpPortPathCost in
                BRIDGE-MIB will be rejected. While retrieving the value of
                dot1dStpPortPathCost, the maximum value of 65535 will be
                returned if the value of stpxLongStpPortPathCost for the same
                instance exceeds 65535.
                
                When the value of this MIB object is short(1),
                the dot1dStpPortPathCost in BRIDGE-MIB must be used.
                ''',
                'stpxspanningtreepathcostopermode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreeType', REFERENCE_ENUM_CLASS, 'StpxspanningtreetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxspanningtreeobjects.StpxspanningtreetypeEnum', 
                [], [], 
                '''                The actual mode of spanning tree protocol runs
                on the  device. It can be one of the following:
                
                pvstPlus -- PVST+ (Per VLAN Spanning Tree+ Protocol).
                
                mistp -- MISTP (Multi Instance Spanning Tree Protocol).
                
                mistpPvstPlus --  MISTP with the tunneling scheme
                                     enabled for PVST+.
                
                mst -- IEEE 802.1s Multiple Spanning Tree (MST)
                       with IEEE 802.1w Rapid Spanning Tree Protocol
                       (RSTP).
                
                rapidPvstPlus -- IEEE 802.1w Rapid Spanning Tree 
                        Protocol (RSTP) for all vlans in PVST+.
                
                When the value of this MIB object gets changed, the 
                network connectivity would be affected and the 
                connectivity to this device would also be lost 
                temporarily.
                ''',
                'stpxspanningtreetype',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSpanningTreeObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmistpobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmistpobjects',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                The number of MISTP instances, that are supported by the device 
                when the value of stpxSpanningTreeType is either mistp(2)
                or mistpPvstPlus(3).
                ''',
                'stpxmistpinstancenumber',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMISTPObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxloopguardobjects.StpxloopguardglobaldefaultmodeEnum' : _MetaInfoEnum('StpxloopguardglobaldefaultmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxloopguardobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxloopguardobjects',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardGlobalDefaultMode', REFERENCE_ENUM_CLASS, 'StpxloopguardglobaldefaultmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopguardobjects.StpxloopguardglobaldefaultmodeEnum', 
                [], [], 
                '''                Indicates the global default config mode of LoopGuard 
                feature on the device.
                ''',
                'stpxloopguardglobaldefaultmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxLoopGuardObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxfaststartobjects.StpxfaststartglobaldefaultmodeEnum' : _MetaInfoEnum('StpxfaststartglobaldefaultmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxfaststartobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxfaststartobjects',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartBpduFilterEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the global default mode of the Bpdu 
                Filter feature on the device.
                
                On platforms that does not support per port 
                Bpdu Filter configuration as indicated by
                the object stpxFastStartPortBpduFilterMode,
                if  the value of this object is set to true(1), 
                and the Fast Start Feature is operationally 
                enabled on a port, then no BPDUs will be 
                transmitted on this port.
                ''',
                'stpxfaststartbpdufilterenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartBpduGuardEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the global default mode of the Bpdu
                Guard feature on the device.
                
                On platforms that does not support per port 
                Bpdu Guard configuration as indicated by
                the object stpxFastStartPortBpduGuardMode,
                if  the value of this object is set to true(1), 
                and the Fast Start Feature is operationally 
                enabled on a port, then that port will be 
                immediately disabled when the system receives
                a BPDU from that port.
                ''',
                'stpxfaststartbpduguardenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartGlobalDefaultMode', REFERENCE_ENUM_CLASS, 'StpxfaststartglobaldefaultmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartobjects.StpxfaststartglobaldefaultmodeEnum', 
                [], [], 
                '''                Indicates the global default mode of the Fast 
                Start feature on the device.
                ''',
                'stpxfaststartglobaldefaultmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxFastStartObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxbpduskewingobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxbpduskewingobjects',
            False, 
            [
            _MetaInfoClassMember('stpxBpduSkewingDetectionEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether BPDU skewing detection feature
                is enabled or not on the system. If this object has
                the value of true(1), then the system will detect
                whether BPDUs received by any port on any Spanning 
                Tree instance are processed at an interval longer
                than the object value of dot1dStpHelloTime in the
                BIRDGE-MIB of the Spanning Tree instance.
                ''',
                'stpxbpduskewingdetectionenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxBpduSkewingObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstobjects.StpxmstregioneditbufferoperationEnum' : _MetaInfoEnum('StpxmstregioneditbufferoperationEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'other':'other',
            'acquire':'acquire',
            'releaseWithForce':'releaseWithForce',
            'commit':'commit',
            'rollBack':'rollBack',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxmstobjects.StpxmstregioneditbufferstatusEnum' : _MetaInfoEnum('StpxmstregioneditbufferstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'released':'released',
            'acquiredBySnmp':'acquiredBySnmp',
            'acquiredByNonSnmp':'acquiredByNonSnmp',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxmstobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstobjects',
            False, 
            [
            _MetaInfoClassMember('stpxMSTMaxHopCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '40')], [], 
                '''                The maximum number of hops for the MST region. 
                
                This object will take on value of 40 if the object value
                of stpxSMSTMaxHopCount is greater than 40.
                
                This object is deprecated and replaced by
                stpxSMSTMaxHopCount.
                ''',
                'stpxmstmaxhopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTMaxInstanceNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                The maximum MST (Multiple Spanning Tree) instance id, 
                that can be supported by the device for Cisco proprietary
                implementation of the MST Protocol.
                
                This object is deprecated and replaced by 
                stpxSMSTMaxInstanceID.
                ''',
                'stpxmstmaxinstancenumber',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionEditBufferOperation', REFERENCE_ENUM_CLASS, 'StpxmstregioneditbufferoperationEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstobjects.StpxmstregioneditbufferoperationEnum', 
                [], [], 
                '''                Indicates the operation that is performed on the Region 
                Config Edit Buffer.
                
                other --   none of the following operations.  
                
                acquire -- acquire the Edit Buffer. This operation can 
                           only be performed when the object 
                           stpxMSTRegionEditBufferStatus has the value of
                           released(1). After the successful operation of 
                           this action, the stpxMSTRegionEditBufferStatus
                           will be changed to acquiredBySnmp(2). 
                            
                releaseWithForce -- release the Edit Buffer acquired by
                           non-SNMP users with force and discard the changes
                           in the Edit Buffer. This operation can only be 
                           performed when the object 
                           stpxMSTRegionEditBufferStatus has the value of 
                           acquiredByNonSnmp(2).
                
                commit --  commit the changes in the Edit Buffer
                           and release the Edit Buffer. The successful 
                           operation of this action will make the changes
                           in the Edit Buffer effective on the device.
                           This operation can only be performed when the 
                           object stpxMSTRegionEditBufferStatus has the 
                           value of acquiredBySnmp(3).
                 
                rollBack -- discard the changes in the Edit Buffer
                           and release the Edit Buffer. This operation can 
                           only be performed when the object 
                           stpxMSTRegionEditBufferStatus has the value 
                           of acquiredBySnmp(3).
                
                This object always returns other(1) when it is read.
                ''',
                'stpxmstregioneditbufferoperation',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionEditBufferStatus', REFERENCE_ENUM_CLASS, 'StpxmstregioneditbufferstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstobjects.StpxmstregioneditbufferstatusEnum', 
                [], [], 
                '''                Indicates the current ownership status of the unique 
                Region Config Edit Buffer. 
                
                released -- the Edit Buffer can be acquired by any of 
                            the SNMP management stations. 
                
                acquiredBySnmp -- the Edit Buffer is acquired by
                            any of the SNMP management stations. 
                
                acquiredByNonSnmp -- the Edit Buffer is acquired by the 
                            non-SNMP users managing the device.
                ''',
                'stpxmstregioneditbufferstatus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionEditName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The MST region name in the Edit Buffer. 
                
                This object is only instantiated when the 
                stpxMSTRegionEditBufferStatus has the value of 
                acquiredBySnmp(2).
                ''',
                'stpxmstregioneditname',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionEditRevision', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The MST region version in the Edit Buffer. This object is
                only instantiated when the stpxMSTRegionEditBufferStatus 
                has the value of acquiredBySnmp(2).
                
                This object is deprecated and replaced by
                stpxSMSTRegionEditRevision.
                ''',
                'stpxmstregioneditrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The operational MST region name.
                ''',
                'stpxmstregionname',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionRevision', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The operational MST region version.
                
                This object is deprecated and replaced by 
                stpxSMSTRegionRevision.
                ''',
                'stpxmstregionrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrstpobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrstpobjects',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPTransmitHoldCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Transmit Hold Count.
                ''',
                'stpxrstptransmitholdcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstobjects' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstobjects',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTConfigDigest', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The IEEE MST region configuration digest.
                ''',
                'stpxsmstconfigdigest',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTConfigPreStandardDigest', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pre-standard MST region configuration digest.
                ''',
                'stpxsmstconfigprestandarddigest',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTMaxHopCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of hops for the IEEE MST region.
                ''',
                'stpxsmstmaxhopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTMaxInstanceID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum MST instance ID that can be supported 
                by the device for IEEE MST.
                ''',
                'stpxsmstmaxinstanceid',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTMaxInstances', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of MST instances that can be 
                supported by the device for IEEE MST.
                ''',
                'stpxsmstmaxinstances',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTRegionEditRevision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MST region version in the Edit Buffer for IEEE 
                MST.
                
                This object is only instantiated when the 
                stpxMSTRegionEditBufferStatus has the value of 
                acquiredBySnmp(2).
                ''',
                'stpxsmstregioneditrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTRegionRevision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The operational region version for IEEE MST.
                ''',
                'stpxsmstregionrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry.StpxpvstvlanenableEnum' : _MetaInfoEnum('StpxpvstvlanenableEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
            'notApplicable':'notApplicable',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry',
            False, 
            [
            _MetaInfoClassMember('stpxPVSTVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                An index value that uniquely identifies the
                Virtual LAN associated with this information.
                ''',
                'stpxpvstvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxPVSTVlanEnable', REFERENCE_ENUM_CLASS, 'StpxpvstvlanenableEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry.StpxpvstvlanenableEnum', 
                [], [], 
                '''                Indicates whether Spanning Tree PVST+  
                Protocol is enabled for this Virtual LAN. If 
                Spanning Tree PVST+ Protocol is not supported 
                on this VLAN, then notApplicable(3) will be 
                returned while retrieving the object value for 
                this VLAN.
                
                If the device only supports a single global
                Spanning Tree PVST+ Protocol enable/disable 
                for all the existing VLANs, then the object 
                value assigned to this VLAN will be applied
                to the object values of all the instances
                in this table which do not have the value
                of notApplicable(3).
                
                If the value of stpxSpanningTreeType is neither 
                pvstPlus(1) nor rapidPvstPlus(5), then the value 
                of stpxPVSTVlanEnable for this VLAN can not be 
                changed.
                ''',
                'stpxpvstvlanenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxPVSTVlanEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxpvstvlantable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxpvstvlantable',
            False, 
            [
            _MetaInfoClassMember('stpxPVSTVlanEntry', REFERENCE_LIST, 'Stpxpvstvlanentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry', 
                [], [], 
                '''                An entry containing Spanning Tree PVST+ Protocol 
                information for a particular Virtual LAN.
                ''',
                'stpxpvstvlanentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxPVSTVlanTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry',
            False, 
            [
            _MetaInfoClassMember('stpxVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN id of the VLAN.
                ''',
                'stpxvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxInconsistentState', REFERENCE_BITS, 'Stpxinconsistentstate' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry.Stpxinconsistentstate', 
                [], [], 
                '''                The types of inconsistency which have been discovered on
                this port for this VLAN's Spanning Tree.
                
                When this object exists, the value of the corresponding
                instance of the Bridge MIB's dot1dStpPortState object will
                be 'broken(6)'.
                ''',
                'stpxinconsistentstate',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxInconsistencyEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxinconsistencytable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxinconsistencytable',
            False, 
            [
            _MetaInfoClassMember('stpxInconsistencyEntry', REFERENCE_LIST, 'Stpxinconsistencyentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry', 
                [], [], 
                '''                A VLAN on a particular port for which a Spanning Tree
                inconsistency is currently in effect.
                ''',
                'stpxinconsistencyentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxInconsistencyTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry',
            False, 
            [
            _MetaInfoClassMember('stpxRootGuardConfigPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrootguardconfigportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRootGuardConfigEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the RootGuard capability is 
                enabled on this port or not. This configuration will be
                applied to all Spanning Tree instances in which this port 
                exists.
                ''',
                'stpxrootguardconfigenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRootGuardConfigEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrootguardconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrootguardconfigtable',
            False, 
            [
            _MetaInfoClassMember('stpxRootGuardConfigEntry', REFERENCE_LIST, 'Stpxrootguardconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry', 
                [], [], 
                '''                A bridge port for which Spanning Tree RootGuard
                capability can be configured.
                ''',
                'stpxrootguardconfigentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRootGuardConfigTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry',
            False, 
            [
            _MetaInfoClassMember('stpxRootInconsistencyIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Spanning Tree instance id, such as the VLAN id
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1) or rapidPvstPlus(5).
                ''',
                'stpxrootinconsistencyindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRootInconsistencyPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrootinconsistencyportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRootInconsistencyState', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the port on a particular Spanning 
                Tree instance is currently in root-inconsistent 
                state or not.
                ''',
                'stpxrootinconsistencystate',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRootInconsistencyEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrootinconsistencytable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrootinconsistencytable',
            False, 
            [
            _MetaInfoClassMember('stpxRootInconsistencyEntry', REFERENCE_LIST, 'Stpxrootinconsistencyentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry', 
                [], [], 
                '''                A Spanning Tree instance on a particular port for 
                which a Spanning Tree root-inconsistency is currently 
                in effect.
                ''',
                'stpxrootinconsistencyentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRootInconsistencyTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                An arbitrary integer within the range from 1 to the value of
                stpxMISTPInstanceNumber that uniquely identifies an instance.
                ''',
                'stpxmistpinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMISTPInstanceEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the MISTP protocol is currently
                enabled on the MISTP instance.
                
                If this object is set to
                   'true'    - the MISTP protocol will run on this instance.
                              
                   'false'   - the MISTP protocol will stop running on this 
                               instance.
                ''',
                'stpxmistpinstanceenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPInstanceVlansMapped', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN. The
                first octet corresponds to VLANs with VlanIndex values
                of 0 through 7; the second octet to VLANs 8 through
                15; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MISTP instance,
                then the bit corresponding to that VLAN is set to '1'.
                ''',
                'stpxmistpinstancevlansmapped',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPInstanceVlansMapped2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 1024 through 2047. The
                first octet corresponds to VLANs with VlanIndex values
                of 1024 through 1031; the second octet to VLANs 1032
                through 1039; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MISTP instance,
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is only instantiated on devices with 
                support for VlanIndex up to 4095.
                ''',
                'stpxmistpinstancevlansmapped2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPInstanceVlansMapped3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 2048 through 3071. The
                first octet corresponds to VLANs with VlanIndex values
                of 2048 through 2055; the second octet to VLANs 2056
                through 2063; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MISTP instance,
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is only instantiated on devices with 
                support for VlanIndex up to 4095.
                ''',
                'stpxmistpinstancevlansmapped3k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPInstanceVlansMapped4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 3072 through 4095. The
                first octet corresponds to VLANs with VlanIndex values
                of 3072 through 3079; the second octet to VLANs 3080
                through 3087; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MISTP instance,
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is only instantiated on devices with 
                support for VlanIndex up to 4095.
                ''',
                'stpxmistpinstancevlansmapped4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMISTPInstanceEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmistpinstancetable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmistpinstancetable',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceEntry', REFERENCE_LIST, 'Stpxmistpinstanceentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry', 
                [], [], 
                '''                A conceptual row containing the status of the MISTP 
                instance.
                ''',
                'stpxmistpinstanceentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMISTPInstanceTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry.StpxloopguardconfigmodeEnum' : _MetaInfoEnum('StpxloopguardconfigmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
            'default':'default',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardConfigPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxloopguardconfigportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxLoopGuardConfigEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the LoopGuard capability is 
                enabled on this port or not. This configuration will be
                applied to all the Spanning Tree instances in which this 
                port exists.
                
                In order to support additional Loop Guard config mode
                (default) as defined in stpxLoopGuardConfigMode other 
                than enable (true(1)) or disable (false(2)) as defined 
                in this object, stpxLoopGuardConfigMode object needs to 
                be used.
                
                When the stpxLoopGuardConfigMode object has the value of
                enable(1), the value of stpxLoopGuardConfigEnabled for 
                the same instance will be true(1). When the 
                stpxLoopGuardConfigMode object has the value of disable(2), 
                the value of stpxLoopGuardConfigEnabled for the same 
                instance will be false(2). When the stpxLoopGuardConfigMode 
                object has the value of default(3), the value of 
                stpxLoopGuardConfigEnabled for the same instance will 
                depend on the object value of 
                stpxLoopGuardGlobalDefaultMode.
                ''',
                'stpxloopguardconfigenabled',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopGuardConfigMode', REFERENCE_ENUM_CLASS, 'StpxloopguardconfigmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry.StpxloopguardconfigmodeEnum', 
                [], [], 
                '''                Indicates the mode of Loop Guard Feature on this 
                port. This configuration will be applied to all 
                the Spanning Tree instances in which this port 
                exists.
                
                enable -- the Loop Guard feature is enabled on this 
                          port. 
                
                disable -- the Loop Guard feature is disabled on this 
                          port.  
                
                default -- whether the Loop Guard feature is enabled
                           or not on this port depends on the object 
                           value of stpxLoopGuardGlobalDefaultMode.
                ''',
                'stpxloopguardconfigmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxLoopGuardConfigEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxloopguardconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxloopguardconfigtable',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardConfigEntry', REFERENCE_LIST, 'Stpxloopguardconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry', 
                [], [], 
                '''                A bridge port for which Spanning Tree LoopGuard 
                capability can be configured.
                ''',
                'stpxloopguardconfigentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxLoopGuardConfigTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry',
            False, 
            [
            _MetaInfoClassMember('stpxLoopInconsistencyIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Spanning Tree instance id, such as the VLAN id
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1) or rapidPvstPlus(5).
                ''',
                'stpxloopinconsistencyindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxLoopInconsistencyPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxloopinconsistencyportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxLoopInconsistencyState', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the port on a particular Spanning 
                Tree instance is currently in loop-inconsistent 
                state or not.
                ''',
                'stpxloopinconsistencystate',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxLoopInconsistencyEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxloopinconsistencytable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxloopinconsistencytable',
            False, 
            [
            _MetaInfoClassMember('stpxLoopInconsistencyEntry', REFERENCE_LIST, 'Stpxloopinconsistencyentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry', 
                [], [], 
                '''                A Spanning Tree instance on a particular port for
                which a Spanning Tree loop-inconsistency is currently
                in effect.
                ''',
                'stpxloopinconsistencyentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxLoopInconsistencyTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportbpdufiltermodeEnum' : _MetaInfoEnum('StpxfaststartportbpdufiltermodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
            'default':'default',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportbpduguardmodeEnum' : _MetaInfoEnum('StpxfaststartportbpduguardmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
            'default':'default',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportmodeEnum' : _MetaInfoEnum('StpxfaststartportmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'enable',
            'disable':'disable',
            'enableForTrunk':'enableForTrunk',
            'default':'default',
            'network':'network',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxfaststartportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartPortBpduFilterMode', REFERENCE_ENUM_CLASS, 'StpxfaststartportbpdufiltermodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportbpdufiltermodeEnum', 
                [], [], 
                '''                Indicates the mode of Bpdu Filter Feature on the
                port. The system will not transmit BPDUs on a port 
                with Bpdu Filter feature enabled.
                
                enable -- the Bpdu Filter feature is enabled on this 
                          port. 
                
                disable -- the Bpdu Filter feature is disabled on this
                           port.
                
                default -- whether the Bpdu Filter feature is enabled
                           or not on this port depends on the object
                           value of stpxFastStartBpduFilterEnable. If
                           the value of stpxFastStartBpduFilterEnable
                           is true(1) and Fast Start feature is also
                           enabled operationally on this port, then
                           no BPDUs will be transmitted on this port.
                ''',
                'stpxfaststartportbpdufiltermode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartPortBpduGuardMode', REFERENCE_ENUM_CLASS, 'StpxfaststartportbpduguardmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportbpduguardmodeEnum', 
                [], [], 
                '''                Indicates the mode of Bpdu Guard Feature on the
                port. A port with Bpdu Guard enabled is 
                immediately disabled when the system 
                receives a BPDU from that port. 
                
                enable -- the Bpdu Guard feature is enabled on this
                          port. 
                
                disable -- the Bpdu Guard feature is disabled on this
                          port.
                
                default -- whether the Bpdu Guard feature is enabled
                           or not on this port depends on the object
                           value of stpxFastStartBpduGuardEnable. If 
                           the value of stpxFastStartBpduGuardEnable
                           is true(1) and Fast Start feature is also 
                           enabled operationally on this port, then
                           this port is immediately disabled when 
                           the system receives a BPDU from this port.
                ''',
                'stpxfaststartportbpduguardmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartPortEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the port is operating in spantree
                fast start mode.  A port with fast start enabled is
                immediately put in spanning tree forwarding state when
                that port is detected by the Spanning Tree, rather 
                than starting in blocking state which is the normal 
                operation.
                
                In order to support additional Fast Start enable mode
                (enableForTrunk and default) as defined in
                stpxFastStartPortMode other than enable (true(1))
                or disable (false(2)) as defined in this object,
                stpxFastStartPortMode object needs to be used.
                
                When the stpxFastStartPortMode has the value of
                enable(1) or enableForTrunk(3), the value of
                stpxFastStartPortEnable for the same instance
                will be true(1). When the stpxFastStartPortMode
                has the value of disable(2), the value of 
                stpxFastStartPortEnable for the same instance will be 
                false(2). When the stpxFastStartPortMode has the value 
                of default(4), the value of stpxFastStartPortEnable for 
                the same instance depends on the object value of 
                stpxFastStartGlobalDefaultMode.
                ''',
                'stpxfaststartportenable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartPortMode', REFERENCE_ENUM_CLASS, 'StpxfaststartportmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry.StpxfaststartportmodeEnum', 
                [], [], 
                '''                Indicates the mode of Fast Start Feature on the 
                port. A port with fast start enabled is immediately 
                put in spanning tree forwarding state when the port
                is detected by the Spanning Tree, rather than 
                starting in blocking state which is the normal 
                operation.
                
                enable -- the fast start feature is enabled on this 
                          port but will only take effect when the 
                          object value of its 
                          vlanTrunkPortDynamicStatus as specified 
                          in CISCO-VTP-MIB is notTrunking(2).
                
                disable -- the fast start feature is disabled on this 
                          port.  
                
                enableForTrunk -- the fast start feature is enabled 
                          on this port and will take effect 
                          regardless of the object value of 
                          its vlanTrunkPortDynamicStatus.
                
                default -- whether the fast start feature is enabled
                           or not on this port depends on the object 
                           value of stpxFastStartGlobalDefaultMode.
                
                network -- the fast start network mode is enabled on 
                           this port.
                ''',
                'stpxfaststartportmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxFastStartPortEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxfaststartporttable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxfaststartporttable',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartPortEntry', REFERENCE_LIST, 'Stpxfaststartportentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry', 
                [], [], 
                '''                A bridge port for which Spanning Tree Port Fast
                Start can be configured.
                ''',
                'stpxfaststartportentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxFastStartPortTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry.StpxfaststartopermodeEnum' : _MetaInfoEnum('StpxfaststartopermodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartOperModeInstIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Spanning Tree instance id, such as the VLAN id 
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1).
                ''',
                'stpxfaststartopermodeinstindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartOperModePortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxfaststartopermodeportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartOperMode', REFERENCE_ENUM_CLASS, 'StpxfaststartopermodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry.StpxfaststartopermodeEnum', 
                [], [], 
                '''                Indicates the fast start operational status of the 
                port on a particular Spanning Tree Instance.
                ''',
                'stpxfaststartopermode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxFastStartOperModeEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxfaststartopermodetable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxfaststartopermodetable',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartOperModeEntry', REFERENCE_LIST, 'Stpxfaststartopermodeentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry', 
                [], [], 
                '''                An entry with port fast start oper mode 
                information on a bridge port for a particular 
                Spanning Tree Instance.
                ''',
                'stpxfaststartopermodeentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxFastStartOperModeTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry',
            False, 
            [
            _MetaInfoClassMember('stpxBpduSkewingInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Spanning Tree instance id, such as the VLAN id 
                of the VLAN if the object value of stpxSpanningTreeType 
                is pvstPlus(1).
                ''',
                'stpxbpduskewinginstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxBpduSkewingPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxbpduskewingportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxBpduSkewingLastSkewDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the skew duration in milliseconds of the
                last BPDU skewing detected.
                ''',
                'stpxbpduskewinglastskewduration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingWorstSkewDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the skew duration in milliseconds of the
                worst BPDU skewing detected.
                ''',
                'stpxbpduskewingworstskewduration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingWorstSkewTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the value of sysUpTime when the worst
                BPDU skewing was detected.
                ''',
                'stpxbpduskewingworstskewtime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxBpduSkewingEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxbpduskewingtable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxbpduskewingtable',
            False, 
            [
            _MetaInfoClassMember('stpxBpduSkewingEntry', REFERENCE_LIST, 'Stpxbpduskewingentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry', 
                [], [], 
                '''                A Spanning Tree instance on a particular port for
                which BPDU skewing has been detected.
                ''',
                'stpxbpduskewingentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxBpduSkewingTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                An integer that uniquely identifies an MST instance 
                within the range of 0 to the object value of
                stpxMSTMaxInstanceNumber.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceIndex.
                ''',
                'stpxmstinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTInstanceRemainingHopCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '40')], [], 
                '''                The remaining hop count for this MST instance.
                
                This object will take on value of 40 if the object value
                of stpxSMSTInstanceRemainingHopCount is greater than 40.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4).
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceRemainingHopCount.
                ''',
                'stpxmstinstanceremaininghopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceVlansMapped', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN. The
                first octet corresponds to VLANs with VlanIndex values
                of 0 through 7; the second octet to VLANs 8 through
                15; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceVlansMapped1k2k.
                ''',
                'stpxmstinstancevlansmapped',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceVlansMapped2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 1024 through 2047. The
                first octet corresponds to VLANs with VlanIndex values
                of 1024 through 1031; the second octet to VLANs 1032
                through 1039; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceVlansMapped1k2k.
                ''',
                'stpxmstinstancevlansmapped2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceVlansMapped3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 2048 through 3071. The
                first octet corresponds to VLANs with VlanIndex values
                of 2048 through 2055; the second octet to VLANs 2056
                through 2063; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceVlansMapped3k4k.
                ''',
                'stpxmstinstancevlansmapped3k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceVlansMapped4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 3072 through 4095. The
                first octet corresponds to VLANs with VlanIndex values
                of 3072 through 3079; the second octet to VLANs 3080
                through 3087; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to '1'.
                
                This object is deprecated and replaced by
                stpxSMSTInstanceVlansMapped3k4k.
                ''',
                'stpxmstinstancevlansmapped4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTInstanceEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstinstancetable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstinstancetable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEntry', REFERENCE_LIST, 'Stpxmstinstanceentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry', 
                [], [], 
                '''                A conceptual row containing the MST instance 
                information.
                ''',
                'stpxmstinstanceentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTInstanceTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEditIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                An integer that uniquely identifies an MST instance 
                from 0 to the object value of stpxMSTMaxInstanceNumber.
                
                The instances of this table entry with 
                stpxMSTInstanceEditIndex of zero can not be 
                modified.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceEditIndex.
                ''',
                'stpxmstinstanceeditindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTInstanceEditVlansMap', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN. The
                first octet corresponds to VLANs with VlanIndex values
                of 0 through 7; the second octet to VLANs 8 through
                15; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to 
                '1'. Each VLAN can only be mapped to one unique MST 
                instance in the range from 1 to stpxMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1' 
                to '0', then that VLAN will be automatically mapped to 
                MST instance 0 by the device.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceEditVlansMap1k2k.
                ''',
                'stpxmstinstanceeditvlansmap',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceEditVlansMap2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 1024 through 2047. The
                first octet corresponds to VLANs with VlanIndex values
                of 1024 through 1031; the second octet to VLANs 1032
                through 1039; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to
                '1'. Each VLAN can only be mapped to one unique MST
                instance in the range from 1 to stpxMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1' 
                to '0', then that VLAN will be automatically mapped to 
                MST instance 0 by the device.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceEditVlansMap1k2k.
                ''',
                'stpxmstinstanceeditvlansmap2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceEditVlansMap3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 2048 through 3071. The
                first octet corresponds to VLANs with VlanIndex values
                of 2048 through 2055; the second octet to VLANs 2056
                through 2063; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to
                '1'. Each VLAN can only be mapped to one unique MST
                instance in the range from 1 to stpxMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1' 
                to '0', then that VLAN will be automatically mapped to 
                MST instance 0 by the device.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceEditVlansMap3k4k.
                ''',
                'stpxmstinstanceeditvlansmap3k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceEditVlansMap4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 3072 through 4095. The
                first octet corresponds to VLANs with VlanIndex values
                of 3072 through 3079; the second octet to VLANs 3080
                through 3087; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to
                '1'. Each VLAN can only be mapped to one unique MST
                instance in the range from 1 to stpxMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1' 
                to '0', then that VLAN will be automatically mapped to 
                MST instance 0 by the device.
                
                This object is deprecated and replaced by
                stpxSMSTInstanceEditVlansMap3k4k.
                ''',
                'stpxmstinstanceeditvlansmap4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTInstanceEditEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstinstanceedittable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstinstanceedittable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEditEntry', REFERENCE_LIST, 'Stpxmstinstanceeditentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry', 
                [], [], 
                '''                A conceptual row containing MST instance information 
                in the Edit Buffer.
                ''',
                'stpxmstinstanceeditentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTInstanceEditTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.StpxmstportadminlinktypeEnum' : _MetaInfoEnum('StpxmstportadminlinktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'pointToPoint',
            'shared':'shared',
            'auto':'auto',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.StpxmstportoperlinktypeEnum' : _MetaInfoEnum('StpxmstportoperlinktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'pointToPoint',
            'shared':'shared',
            'other':'other',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxmstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortAdminLinkType', REFERENCE_ENUM_CLASS, 'StpxmstportadminlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.StpxmstportadminlinktypeEnum', 
                [], [], 
                '''                Indicates the administrative link type configuration of 
                a bridge port for the MST protocol. 
                
                pointToPoint -- the port is administratively configured to
                        be connected to a point-to-point link.
                
                shared -- the port is administratively configured to be
                        connected to a shared medium. 
                
                auto -- the administrative configuration of the port's 
                        link type depends on link duplex of the port.
                        If the port link is full-duplex, the administrative 
                        link type configuration on this port will be taken 
                        as pointTopoint(1). If the port link is half-duplex, 
                        the administrative link type configuration on this
                        port will be taken as shared(2).
                
                This configuration of this object only takes effect when the
                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).
                stpxMSTPortAdminLinkType is deprecated and replaced 
                with stpxRSTPPortAdminLinkType.
                ''',
                'stpxmstportadminlinktype',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortOperLinkType', REFERENCE_ENUM_CLASS, 'StpxmstportoperlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.StpxmstportoperlinktypeEnum', 
                [], [], 
                '''                Indicates the operational link type of a bridge port
                for the MST protocol.
                
                pointToPoint -- the port is operationally connected to
                        a point-to-point link.
                
                shared -- the port is operationally connected to 
                        a shared medium.
                
                other -- none of the above.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4).  stpxMSTPortOperLinkType 
                is deprecated and replaced with stpxRSTPPortOperLinkType.
                ''',
                'stpxmstportoperlinktype',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortProtocolMigration', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The protocol migration control on this port. When the 
                object value of  stpxSpanningTreeType is mst(4) or 
                rapidPvstPlus(5), setting true(1) to this object forces 
                the device to try using version 2 BPDUs on this port. 
                When the object value of stpxSpanningTreeType is neither 
                mst(4) nor rapidPvstPlus(5), setting true(1) to this 
                object has no effect. Setting false(2) to this object has 
                no effect. This object always returns false(2) when read.
                stpxMSTPortProtocolMigration is deprecated and 
                replaced with stpxRSTPPortProtocolMigration.
                ''',
                'stpxmstportprotocolmigration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortStatus', REFERENCE_BITS, 'Stpxmstportstatus' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry.Stpxmstportstatus', 
                [], [], 
                '''                Indicates the operational status of the port for the 
                MST protocol. 
                
                edge -- this port is an edge port for the MST region.
                
                boundary -- this port is a boundary port for the 
                        MST region.
                
                pvst --  this port is connected to a PVST/PVST+ bridge.   
                
                stp -- this port is connected to a Single Spanning
                        Tree bridge. 
                
                This object is only instantiated when the object value
                of stpxSpanningTreeType is mst(4).
                
                This object is deprecated and replaced by 
                stpxSMSTPortStatus.
                ''',
                'stpxmstportstatus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTPortEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstporttable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstporttable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortEntry', REFERENCE_LIST, 'Stpxmstportentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry', 
                [], [], 
                '''                An entry with port information for the MST Protocol
                on a bridge port.
                ''',
                'stpxmstportentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTPortTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry.StpxmstportrolevalueEnum' : _MetaInfoEnum('StpxmstportrolevalueEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'disabled':'disabled',
            'root':'root',
            'designated':'designated',
            'alternate':'alternate',
            'backUp':'backUp',
            'boundary':'boundary',
            'master':'master',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortRoleInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                The MST instance id within the range of 0 to
                stpxMSTMaxInstanceNumber.
                ''',
                'stpxmstportroleinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortRolePortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxmstportroleportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortRoleValue', REFERENCE_ENUM_CLASS, 'StpxmstportrolevalueEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry.StpxmstportrolevalueEnum', 
                [], [], 
                '''                Indicates the port role on a particular MST instance
                for the MST protocol. 
                
                disabled --  this port has no role on this MST instance. 
                
                root -- this port has the role of root port on this MST
                            instance. 
                
                designated -- this port has the role of designated 
                            port on this MST instance.
                
                alternate -- this port has the role of alternate port
                            on this MST instance.
                
                backUp -- this port has the role of backup port on this  
                            MST instance.
                
                boundary -- this port has the role of boundary port on 
                            this MST instance.
                
                master -- this port has the role of master port on
                          this MST instance.
                ''',
                'stpxmstportrolevalue',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTPortRoleEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxmstportroletable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxmstportroletable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortRoleEntry', REFERENCE_LIST, 'Stpxmstportroleentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry', 
                [], [], 
                '''                An entry containing the port role information for the MST
                protocol on a port for a particular MST instance existing
                on the system.
                ''',
                'stpxmstportroleentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxMSTPortRoleTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.StpxrstpportadminlinktypeEnum' : _MetaInfoEnum('StpxrstpportadminlinktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'pointToPoint',
            'shared':'shared',
            'auto':'auto',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.StpxrstpportoperlinktypeEnum' : _MetaInfoEnum('StpxrstpportoperlinktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'pointToPoint',
            'shared':'shared',
            'other':'other',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrstpportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortAdminLinkType', REFERENCE_ENUM_CLASS, 'StpxrstpportadminlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.StpxrstpportadminlinktypeEnum', 
                [], [], 
                '''                Indicates the administrative link type configuration of 
                a bridge port for the RSTP protocol. 
                
                pointToPoint -- the port is administratively configured to
                        be connected to a point-to-point link.
                
                shared -- the port is administratively configured to be
                        connected to a shared medium. 
                
                auto -- the administrative configuration of the port's 
                        link type depends on link duplex of the port.
                        If the port link is full-duplex, the administrative 
                        link type configuration on this port will be taken 
                        as pointTopoint(1). If the port link is half-duplex, 
                        the administrative link type configuration on this
                        port will be taken as shared(2).
                
                This configuration of this object only takes effect when the
                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).
                ''',
                'stpxrstpportadminlinktype',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortOperLinkType', REFERENCE_ENUM_CLASS, 'StpxrstpportoperlinktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry.StpxrstpportoperlinktypeEnum', 
                [], [], 
                '''                Indicates the operational link type of a bridge port
                for the RSTP protocol.
                
                pointToPoint -- the port is operationally connected to
                        a point-to-point link.
                
                shared -- the port is operationally connected to 
                        a shared medium.
                
                other -- none of the above.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4) or rapidPvstPlus(5).
                ''',
                'stpxrstpportoperlinktype',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortProtocolMigration', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The protocol migration control on this port. When the 
                object value of  stpxSpanningTreeType is mst(4) or 
                rapidPvstPlus(5), setting true(1) to this object forces 
                the device to try using version 2 BPDUs on this port. 
                When the object value of stpxSpanningTreeType is neither 
                mst(4) nor rapidPvstPlus(5), setting true(1) to 
                this object has no effect. Setting false(2) to this 
                object has no effect. This object always returns 
                false(2) when read.
                ''',
                'stpxrstpportprotocolmigration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPPortEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrstpporttable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrstpporttable',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortEntry', REFERENCE_LIST, 'Stpxrstpportentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry', 
                [], [], 
                '''                An entry with port information for the RSTP Protocol
                on a bridge port.
                ''',
                'stpxrstpportentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPPortTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry.StpxrstpportrolevalueEnum' : _MetaInfoEnum('StpxrstpportrolevalueEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'disabled':'disabled',
            'root':'root',
            'designated':'designated',
            'alternate':'alternate',
            'backUp':'backUp',
            'boundary':'boundary',
            'master':'master',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortRoleInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The Spanning Tree instance id, it can either be a 
                VLAN number if the stpxSpanningTreeType is rapidPvstPlus(5) 
                or an MST instance id if the stpxSpanningTreeType is mst(4).
                ''',
                'stpxrstpportroleinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortRolePortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrstpportroleportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortRoleValue', REFERENCE_ENUM_CLASS, 'StpxrstpportrolevalueEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry.StpxrstpportrolevalueEnum', 
                [], [], 
                '''                Indicates the port role on a particular Spanning Tree 
                instance for the RSTP protocol. 
                
                disabled --  this port has no role in this Spanning
                            Tree instance. 
                
                root -- this port has the role of root port in this
                            Spanning Tree instance. 
                
                designated -- this port has the role of designated 
                            port in this Spanning Tree instance.
                
                alternate -- this port has the role of alternate port
                            in this Spanning Tree instance.
                
                backUp -- this port has the role of backup port in this  
                            Spanning Tree instance.
                
                boundary -- this port has the role of boundary port in 
                            this Spanning Tree instance.
                
                master -- this port has the role of master port in
                            this Spanning Tree instance.
                
                This object could have a value of 'boundary' or 'master'
                only when the object value of stpxSpanningTreeType is mst(4).
                ''',
                'stpxrstpportrolevalue',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPPortRoleEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrstpportroletable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrstpportroletable',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortRoleEntry', REFERENCE_LIST, 'Stpxrstpportroleentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry', 
                [], [], 
                '''                An entry containing the port role information for the RSTP
                protocol on a port for a particular Spanning Tree instance.
                ''',
                'stpxrstpportroleentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPPortRoleTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry',
            False, 
            [
            _MetaInfoClassMember('stpxRPVSTPortVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                The VLAN id of the VLAN.
                ''',
                'stpxrpvstportvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRPVSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrpvstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRPVSTPortStatus', REFERENCE_BITS, 'Stpxrpvstportstatus' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry.Stpxrpvstportstatus', 
                [], [], 
                '''                Indicates the operational status of the port for the 
                Rapid PVST+ protocol.
                
                edge -- this port is an edge port for the RST region.
                
                unused1 -- unused bit 1.
                
                unused2 -- unused bit 2.
                
                stp -- this port is connected to a Single Spanning
                       Tree/PVST+ bridge.
                
                dispute -- this port, as a designated port, received an
                       inferior BPDU with a designated role and the
                       learning bit being set.
                ''',
                'stpxrpvstportstatus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRPVSTPortEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxrpvstporttable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxrpvstporttable',
            False, 
            [
            _MetaInfoClassMember('stpxRPVSTPortEntry', REFERENCE_LIST, 'Stpxrpvstportentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry', 
                [], [], 
                '''                An entry with port status information on a 
                bridge port for a particular Spanning Tree 
                Instance.
                ''',
                'stpxrpvstportentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRPVSTPortTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MST instance ID, the value of which is in the range 
                from 0 to stpxSMSTMaxInstanceID.
                ''',
                'stpxsmstinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTInstanceCISTIntRootCost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the CIST Internal Root Path Cost, i.e., the
                path cost to the CIST Regional Root as specified by the
                corresponding stpxSMSTInstanceCISTRegionalRoot for the 
                MST region.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex
                is 0.
                ''',
                'stpxsmstinstancecistintrootcost',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceCISTRegionalRoot', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                Indicates the Bridge Identifier (refer to BridgeId 
                defined in BRIDGE-MIB) of CIST (Common and Internal 
                Spanning Tree) Regional Root for the MST region.
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4) and stpxSMSTInstanceIndex
                is 0.
                ''',
                'stpxsmstinstancecistregionalroot',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceRemainingHopCount', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The remaining hop count for this MST instance. If this object
                value is not applicable on an MST instance, then the value
                retrieved for this object for that MST instance will be -1. 
                
                This object is only instantiated when the object value of
                stpxSpanningTreeType is mst(4).
                ''',
                'stpxsmstinstanceremaininghopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceVlansMapped1k2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 0 through 2047. The
                first octet corresponds to VLANs with VlanIndex values
                of 0 through 7; the second octet to VLANs 8 through
                15; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to '1'.
                If the length of this string is less than 256 octets,
                any 'missing' octets are assumed to contain the value 
                of zero.
                ''',
                'stpxsmstinstancevlansmapped1k2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceVlansMapped3k4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 2048 through 4095. The
                first octet corresponds to VLANs with VlanIndex values
                of 2048 through 2055; the second octet to VLANs 2056
                through 2063; etc.  The most significant bit of each
                octet corresponds to the lowest value VlanIndex in that
                octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to '1'.
                If the length of this string is less than 256 octets,
                any 'missing' octets are assumed to contain the value 
                of zero.
                ''',
                'stpxsmstinstancevlansmapped3k4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTInstanceEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstinstancetable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstinstancetable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEntry', REFERENCE_LIST, 'Stpxsmstinstanceentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry', 
                [], [], 
                '''                A conceptual row containing the MST instance 
                information for IEEE MST.
                ''',
                'stpxsmstinstanceentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTInstanceTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEditIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MST instance ID, the value of which is in the range from
                0 to stpxSMSTMaxInstanceID. 
                
                The instances of this table entry with 
                stpxSMSTInstanceEditIndex of zero is automatically
                created by the device and can not modified.
                ''',
                'stpxsmstinstanceeditindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTInstanceEditRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object controls the creation and deletion of a row 
                in stpxSMSTInstanceEditTable.
                
                When creating an entry in this table, 'createAndGo' method
                is used and the value of this object is set to 'active'.
                Deactivation of an 'active' entry is not allowed.  When 
                deleting an entry in this table, 'destroy' method is used. 
                Once a row becomes active, value in any other column 
                within such a row may be modified. When a row is active, 
                setting the instance of stpxSMSTInstanceEditVlansMap1k2k
                stpxSMSTInstanceEditVlansMap3k4k for the same MST instance
                both to the value of zero length can not be allowed.
                ''',
                'stpxsmstinstanceeditrowstatus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceEditVlansMap1k2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 0 through 2047. The
                first octet corresponds to VLANs with VlanIndex values
                of 0 through 7; the second octet to VLANs 8 through
                15; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MST instance, 
                then the bit corresponding to that VLAN is set to 
                '1'. Each VLAN can only be mapped to one unique MST 
                instance with the range from 0 to stpxSMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1' 
                to '0', then that VLAN will be automatically mapped to 
                SMST instance 0 by the device. If the bit corresponding 
                to a VLAN is changed from '0' to '1', then that VLAN will 
                be automatically removed from the MST instance this VLAN was 
                previously mapped to. If the length of this string is 
                less than 256 octets, any 'missing' octets are assumed to 
                contain the value of zero.
                ''',
                'stpxsmstinstanceeditvlansmap1k2k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceEditVlansMap3k4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                A string of octets containing one bit per VLAN for
                VLANS with VlanIndex values of 2048 through 4095. The
                first octet corresponds to VLANs with VlanIndex values
                of 2048 through 2055; the second octet to VLANs 2056 through
                2063; etc.  The most significant bit of each octet
                corresponds to the lowest value VlanIndex in that octet.
                
                For each VLAN, if it is mapped to this MST instance,
                then the bit corresponding to that VLAN is set to
                '1'. Each VLAN can only be mapped to one unique MST
                instance with the range from 0 to stpxSMSTMaxInstanceNumber.
                If the bit corresponding to a VLAN is changed from '1'
                to '0', then that VLAN will be automatically mapped to
                SMST instance 0 by the device. If the bit corresponding
                to a VLAN is changed from '0' to '1', then that VLAN will
                be automatically removed from the MST instance this VLAN was
                previously mapped to. If the length of this string is 
                less than 256 octets, any 'missing' octets are assumed to 
                contain the value of zero.
                ''',
                'stpxsmstinstanceeditvlansmap3k4k',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTInstanceEditEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstinstanceedittable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstinstanceedittable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEditEntry', REFERENCE_LIST, 'Stpxsmstinstanceeditentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry', 
                [], [], 
                '''                A conceptual row containing MST instance information 
                in the Edit Buffer.
                
                The total number of entries in this table has to be 
                less than or equal to the object value of stpxSMSTMaxInstances.
                ''',
                'stpxsmstinstanceeditentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTInstanceEditTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.StpxsmstportadminmstmodeEnum' : _MetaInfoEnum('StpxsmstportadminmstmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'preStandard':'preStandard',
            'auto':'auto',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.StpxsmstportopermstmodeEnum' : _MetaInfoEnum('StpxsmstportopermstmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB',
        {
            'unknown':'unknown',
            'preStandard':'preStandard',
            'standard':'standard',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxsmstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTPortAdminHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The adminitratively configured hello time in hundredth 
                of seconds on a port for IEEE MST. The granularity 
                of this timer is 1 second. An agent may return a badValue 
                error if a set is attempted to a value which is not a 
                whole number of seconds. This object value of zero
                means the hello time is not specifically configured on 
                this port and object value of stpxSMSTPortConfigedHelloTime
                retrieved for this port will take on the value of 
                dot1dStpBridgeHelloTime defined in BRIDGE-MIB.
                ''',
                'stpxsmstportadminhellotime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortAdminMSTMode', REFERENCE_ENUM_CLASS, 'StpxsmstportadminmstmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.StpxsmstportadminmstmodeEnum', 
                [], [], 
                '''                The desired MST mode of this port.
                
                preStandard -- this port is administratively configured to
                    transmit pre-standard, i.e. pre IEEE MST, BPDUs.
                
                auto -- the BPDU transmission mode of this port is based 
                    on automatic detection of neighbor ports.
                ''',
                'stpxsmstportadminmstmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortConfigedHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the effective configuration of the hello time on 
                a port.
                ''',
                'stpxsmstportconfigedhellotime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortOperHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The operational hello time in hundredth of seconds on a 
                port for IEEE MST. If this object value is not
                applicable on a port, then the value retrieved on that
                port will be -1.
                ''',
                'stpxsmstportoperhellotime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortOperMSTMode', REFERENCE_ENUM_CLASS, 'StpxsmstportopermstmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.StpxsmstportopermstmodeEnum', 
                [], [], 
                '''                Indicates the current operational MST mode of this port.
                
                unknown -- the operational mode is currently unknown.
                
                preStandard -- this port is currently operating in 
                    pre-standard MSTP BPDU transmission mode.
                
                standard -- this port is currently operating in IEEE MST 
                    BPDU transmission mode.
                ''',
                'stpxsmstportopermstmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortStatus', REFERENCE_BITS, 'Stpxsmstportstatus' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry.Stpxsmstportstatus', 
                [], [], 
                '''                Indicates the operational status of the port for the 
                MST protocol. 
                
                edge -- this port is an edge port for the MST region.
                
                boundary -- this port is a boundary port for the 
                        MST region.
                
                pvst --  this port is connected to a PVST/PVST+ bridge.   
                
                stp -- this port is connected to a Single Spanning
                        Tree bridge.
                
                dispute -- this port, as a designated port, received an
                        inferior BPDU with a designated role and the
                        learning bit being set.
                
                rstp -- this port is connected to a RSTP bridge or an 
                        MST bridge in a different MST region.
                ''',
                'stpxsmstportstatus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTPortEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib.Stpxsmstporttable' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib.Stpxsmstporttable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTPortEntry', REFERENCE_LIST, 'Stpxsmstportentry' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry', 
                [], [], 
                '''                An entry with port information for the MST protocol
                on a bridge port.
                ''',
                'stpxsmstportentry',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTPortTable',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CiscoStpExtensionsMib' : {
        'meta_info' : _MetaInfoClass('CiscoStpExtensionsMib',
            False, 
            [
            _MetaInfoClassMember('stpxBackboneFastObjects', REFERENCE_CLASS, 'Stpxbackbonefastobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxbackbonefastobjects', 
                [], [], 
                '''                ''',
                'stpxbackbonefastobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingObjects', REFERENCE_CLASS, 'Stpxbpduskewingobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxbpduskewingobjects', 
                [], [], 
                '''                ''',
                'stpxbpduskewingobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingTable', REFERENCE_CLASS, 'Stpxbpduskewingtable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxbpduskewingtable', 
                [], [], 
                '''                A table containing a list of the bridge ports for 
                which a particular Spanning Tree instance has been 
                detected to have BPDU skewing occurred since the 
                object value of stpxBpduSkewingDetectionEnable was
                last changed to true(1).
                
                The agent creates a new entry in this table whenever
                a port in a particular Spanning Tree instance is 
                detected to be BPDU skewed since the object value of 
                stpxBpduSkewingDetectionEnable object is changed to 
                true(1). The agent deletes all the entries in this 
                table when the object value of 
                stpxBpduSkewingDetectionEnable is changed to false(2)
                or the object value of stpxSpanningTreeType is 
                changed.
                ''',
                'stpxbpduskewingtable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartObjects', REFERENCE_CLASS, 'Stpxfaststartobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartobjects', 
                [], [], 
                '''                ''',
                'stpxfaststartobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartOperModeTable', REFERENCE_CLASS, 'Stpxfaststartopermodetable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartopermodetable', 
                [], [], 
                '''                A table containing a list of the bridge ports 
                for a particular Spanning Tree Instance.
                ''',
                'stpxfaststartopermodetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartPortTable', REFERENCE_CLASS, 'Stpxfaststartporttable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxfaststartporttable', 
                [], [], 
                '''                A table containing a list of the bridge ports for
                which Spanning Tree Port Fast Start can be
                configured.
                ''',
                'stpxfaststartporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxInconsistencyTable', REFERENCE_CLASS, 'Stpxinconsistencytable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxinconsistencytable', 
                [], [], 
                '''                A table containing a list of the ports for which
                a particular VLAN's Spanning Tree has been found to
                have an inconsistency.  Two types of inconsistency
                are discovered: 1) an inconsistency where two different
                port types have been plugged together; and 2) an
                inconsistency where different switches have different
                PVIDs for the same link.
                ''',
                'stpxinconsistencytable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopGuardConfigTable', REFERENCE_CLASS, 'Stpxloopguardconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopguardconfigtable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                Spanning Tree LoopGuard capability can be configured.
                ''',
                'stpxloopguardconfigtable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopGuardObjects', REFERENCE_CLASS, 'Stpxloopguardobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopguardobjects', 
                [], [], 
                '''                ''',
                'stpxloopguardobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopInconsistencyTable', REFERENCE_CLASS, 'Stpxloopinconsistencytable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxloopinconsistencytable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                a particular Spanning Tree instance has been found
                to have a loop-inconsistency. The agent creates a new
                entry in this table whenever it detects a new
                loop-inconsistency, and deletes entries
                when/soon after the inconsistency is no longer present.
                ''',
                'stpxloopinconsistencytable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPInstanceTable', REFERENCE_CLASS, 'Stpxmistpinstancetable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmistpinstancetable', 
                [], [], 
                '''                This table contains one entry for each instance of MISTP and 
                it contains stpxMISTPInstanceNumber entries, numbered from 1
                to stpxMISTPInstanceNumber.
                
                This table is only instantiated when the value of 
                stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3).
                ''',
                'stpxmistpinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPObjects', REFERENCE_CLASS, 'Stpxmistpobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmistpobjects', 
                [], [], 
                '''                ''',
                'stpxmistpobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceEditTable', REFERENCE_CLASS, 'Stpxmstinstanceedittable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstinstanceedittable', 
                [], [], 
                '''                This table contains MST instance information in the 
                Edit Buffer with one entry for each MST
                instance numbered from 0 to stpxMSTMaxInstanceNumber. 
                
                This table is only instantiated when the 
                stpxMSTRegionEditBufferStatus has the value of
                acquiredBySnmp(2).
                
                This table is deprecated and replaced by 
                stpxSMSTInstanceEditTable.
                ''',
                'stpxmstinstanceedittable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceTable', REFERENCE_CLASS, 'Stpxmstinstancetable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstinstancetable', 
                [], [], 
                '''                This table contains MST instance information with
                one entry for an MST instance within the range of 
                0 to the object value of stpxMSTMaxInstanceNumber. 
                
                This table is deprecated and replaced by 
                stpxSMSTInstanceTable.
                ''',
                'stpxmstinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTObjects', REFERENCE_CLASS, 'Stpxmstobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstobjects', 
                [], [], 
                '''                ''',
                'stpxmstobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortRoleTable', REFERENCE_CLASS, 'Stpxmstportroletable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstportroletable', 
                [], [], 
                '''                A table containing a list of the bridge ports for a 
                particular MST instance.  This table is only instantiated 
                when the stpxSpanningTreeType is mst(4). 
                
                This table is deprecated and replaced with 
                stpxRSTPPortRoleTable.
                ''',
                'stpxmstportroletable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortTable', REFERENCE_CLASS, 'Stpxmstporttable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxmstporttable', 
                [], [], 
                '''                A table containing port information for the MST 
                Protocol on all the bridge ports existing on the 
                system.
                ''',
                'stpxmstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPVSTVlanTable', REFERENCE_CLASS, 'Stpxpvstvlantable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxpvstvlantable', 
                [], [], 
                '''                A list of Virtual LAN entries containing
                information for Spanning Tree PVST+ protocol. 
                An entry will exist for each VLAN existing on 
                the device.
                ''',
                'stpxpvstvlantable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRootGuardConfigTable', REFERENCE_CLASS, 'Stpxrootguardconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrootguardconfigtable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                Spanning Tree RootGuard capability can be configured.
                ''',
                'stpxrootguardconfigtable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRootInconsistencyTable', REFERENCE_CLASS, 'Stpxrootinconsistencytable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrootinconsistencytable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                a particular Spanning Tree instance has been found 
                to have an root-inconsistency. The agent creates a new 
                entry in this table whenever it detects a new 
                root-inconsistency, and deletes entries 
                when/soon after the inconsistency is no longer present.
                ''',
                'stpxrootinconsistencytable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRPVSTPortTable', REFERENCE_CLASS, 'Stpxrpvstporttable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrpvstporttable', 
                [], [], 
                '''                A table containing a list of the bridge ports 
                for a particular Spanning Tree Instance.
                This table is only instantiated when the object value
                of stpxSpanningTreeType is rapidPvstPlus(5).
                ''',
                'stpxrpvstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPObjects', REFERENCE_CLASS, 'Stpxrstpobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpobjects', 
                [], [], 
                '''                ''',
                'stpxrstpobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortRoleTable', REFERENCE_CLASS, 'Stpxrstpportroletable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpportroletable', 
                [], [], 
                '''                A table containing a list of the bridge ports for a 
                particular Spanning Tree instance.  This table is 
                only instantiated when the stpxSpanningTreeType is mst(4) 
                or rapidPvstPlus(5).
                ''',
                'stpxrstpportroletable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortTable', REFERENCE_CLASS, 'Stpxrstpporttable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxrstpporttable', 
                [], [], 
                '''                A table containing port information for the RSTP 
                Protocol on all the bridge ports existing in the 
                system.
                ''',
                'stpxrstpporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceEditTable', REFERENCE_CLASS, 'Stpxsmstinstanceedittable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstinstanceedittable', 
                [], [], 
                '''                This table contains MST instance information in the 
                Edit Buffer. 
                
                This table is only instantiated when the object value
                of  stpxMSTRegionEditBufferStatus has the value of
                acquiredBySnmp(2).
                ''',
                'stpxsmstinstanceedittable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceTable', REFERENCE_CLASS, 'Stpxsmstinstancetable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstinstancetable', 
                [], [], 
                '''                This table contains MST instance information
                for IEEE MST.
                ''',
                'stpxsmstinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTObjects', REFERENCE_CLASS, 'Stpxsmstobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstobjects', 
                [], [], 
                '''                ''',
                'stpxsmstobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortTable', REFERENCE_CLASS, 'Stpxsmstporttable' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxsmstporttable', 
                [], [], 
                '''                A table containing port information for the MST 
                Protocol on all the bridge ports existing on the 
                system.
                
                This table is only instantiated when the object 
                value of stpxSpanningTreeType is mst(4)
                ''',
                'stpxsmstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreeObjects', REFERENCE_CLASS, 'Stpxspanningtreeobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxspanningtreeobjects', 
                [], [], 
                '''                ''',
                'stpxspanningtreeobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkFastObjects', REFERENCE_CLASS, 'Stpxuplinkfastobjects' , 'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB', 'CiscoStpExtensionsMib.Stpxuplinkfastobjects', 
                [], [], 
                '''                ''',
                'stpxuplinkfastobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'CISCO-STP-EXTENSIONS-MIB',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
}
_meta_table['CiscoStpExtensionsMib.Stpxpvstvlantable.Stpxpvstvlanentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxpvstvlantable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxinconsistencytable.Stpxinconsistencyentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxinconsistencytable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrootguardconfigtable.Stpxrootguardconfigentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxrootguardconfigtable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrootinconsistencytable.Stpxrootinconsistencyentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxrootinconsistencytable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmistpinstancetable.Stpxmistpinstanceentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxmistpinstancetable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxloopguardconfigtable.Stpxloopguardconfigentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxloopguardconfigtable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxloopinconsistencytable.Stpxloopinconsistencyentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxloopinconsistencytable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxfaststartporttable.Stpxfaststartportentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxfaststartporttable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxfaststartopermodetable.Stpxfaststartopermodeentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxfaststartopermodetable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxbpduskewingtable.Stpxbpduskewingentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxbpduskewingtable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstinstancetable.Stpxmstinstanceentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxmstinstancetable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstinstanceedittable.Stpxmstinstanceeditentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxmstinstanceedittable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstporttable.Stpxmstportentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxmstporttable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstportroletable.Stpxmstportroleentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxmstportroletable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrstpporttable.Stpxrstpportentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxrstpporttable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrstpportroletable.Stpxrstpportroleentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxrstpportroletable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrpvstporttable.Stpxrpvstportentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxrpvstporttable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstinstancetable.Stpxsmstinstanceentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxsmstinstancetable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstinstanceedittable.Stpxsmstinstanceeditentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxsmstinstanceedittable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstporttable.Stpxsmstportentry']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib.Stpxsmstporttable']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxuplinkfastobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxbackbonefastobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxspanningtreeobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmistpobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxloopguardobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxfaststartobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxbpduskewingobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrstpobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstobjects']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxpvstvlantable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxinconsistencytable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrootguardconfigtable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrootinconsistencytable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmistpinstancetable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxloopguardconfigtable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxloopinconsistencytable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxfaststartporttable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxfaststartopermodetable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxbpduskewingtable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstinstancetable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstinstanceedittable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstporttable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxmstportroletable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrstpporttable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrstpportroletable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxrpvstporttable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstinstancetable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstinstanceedittable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']
_meta_table['CiscoStpExtensionsMib.Stpxsmstporttable']['meta_info'].parent =_meta_table['CiscoStpExtensionsMib']['meta_info']

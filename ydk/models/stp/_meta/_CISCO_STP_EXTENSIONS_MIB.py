


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects',
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
                [(0, 4294967295)], [], 
                '''                The number of inferior BPDUs received by the switch 
                since the stpxBackboneFastOperEnabled has
                become true(1). If the value of 
                stpxBackboneFastOperEnabled is false(2), then this 
                mib object will have a value of 0.
                ''',
                'stpxbackbonefastininferiorbpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastInRLQRequestPDUs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Root Link Query request PDUs received by the
                switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastinrlqrequestpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastInRLQResponsePDUs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                The number of Root Link Query request PDUs transmitted by
                the switch since the stpxBackboneFastOperEnabled has become
                true(1). If the value of stpxBackboneFastOperEnabled is
                false(2), then this mib object will have a value of 0.
                ''',
                'stpxbackbonefastoutrlqrequestpdus',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBackboneFastOutRLQResponsePDUs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects',
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry',
            False, 
            [
            _MetaInfoClassMember('stpxBpduSkewingInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The Spanning Tree instance id, such as the VLAN id 
                of the VLAN if the object value of stpxSpanningTreeType 
                is pvstPlus(1).
                ''',
                'stpxbpduskewinginstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxBpduSkewingPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxbpduskewingportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxBpduSkewingLastSkewDuration', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the skew duration in milliseconds of the
                last BPDU skewing detected.
                ''',
                'stpxbpduskewinglastskewduration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingWorstSkewDuration', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the skew duration in milliseconds of the
                worst BPDU skewing detected.
                ''',
                'stpxbpduskewingworstskewduration',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingWorstSkewTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the value of sysUpTime when the worst
                BPDU skewing was detected.
                ''',
                'stpxbpduskewingworstskewtime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxBpduSkewingEntry',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable',
            False, 
            [
            _MetaInfoClassMember('stpxBpduSkewingEntry', REFERENCE_LIST, 'StpxBpduSkewingEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxFastStartObjects.StpxFastStartGlobalDefaultMode_Enum' : _MetaInfoEnum('StpxFastStartGlobalDefaultMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxFastStartObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxFastStartObjects',
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
            _MetaInfoClassMember('stpxFastStartGlobalDefaultMode', REFERENCE_ENUM_CLASS, 'StpxFastStartGlobalDefaultMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartObjects.StpxFastStartGlobalDefaultMode_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry.StpxFastStartOperMode_Enum' : _MetaInfoEnum('StpxFastStartOperMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartOperModeInstIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The Spanning Tree instance id, such as the VLAN id 
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1).
                ''',
                'stpxfaststartopermodeinstindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartOperModePortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxfaststartopermodeportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartOperMode', REFERENCE_ENUM_CLASS, 'StpxFastStartOperMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry.StpxFastStartOperMode_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartOperModeEntry', REFERENCE_LIST, 'StpxFastStartOperModeEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduFilterMode_Enum' : _MetaInfoEnum('StpxFastStartPortBpduFilterMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
            'default':'DEFAULT',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduGuardMode_Enum' : _MetaInfoEnum('StpxFastStartPortBpduGuardMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
            'default':'DEFAULT',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortMode_Enum' : _MetaInfoEnum('StpxFastStartPortMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
            'enableForTrunk':'ENABLEFORTRUNK',
            'default':'DEFAULT',
            'network':'NETWORK',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxfaststartportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxFastStartPortBpduFilterMode', REFERENCE_ENUM_CLASS, 'StpxFastStartPortBpduFilterMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduFilterMode_Enum', 
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
            _MetaInfoClassMember('stpxFastStartPortBpduGuardMode', REFERENCE_ENUM_CLASS, 'StpxFastStartPortBpduGuardMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortBpduGuardMode_Enum', 
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
            _MetaInfoClassMember('stpxFastStartPortMode', REFERENCE_ENUM_CLASS, 'StpxFastStartPortMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry.StpxFastStartPortMode_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable',
            False, 
            [
            _MetaInfoClassMember('stpxFastStartPortEntry', REFERENCE_LIST, 'StpxFastStartPortEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry',
            False, 
            [
            _MetaInfoClassMember('stpxPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VLAN id of the VLAN.
                ''',
                'stpxvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxInconsistentState', REFERENCE_BITS, 'StpxInconsistentState_Bits' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry.StpxInconsistentState_Bits', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable',
            False, 
            [
            _MetaInfoClassMember('stpxInconsistencyEntry', REFERENCE_LIST, 'StpxInconsistencyEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry.StpxLoopGuardConfigMode_Enum' : _MetaInfoEnum('StpxLoopGuardConfigMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
            'default':'DEFAULT',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardConfigPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
            _MetaInfoClassMember('stpxLoopGuardConfigMode', REFERENCE_ENUM_CLASS, 'StpxLoopGuardConfigMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry.StpxLoopGuardConfigMode_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardConfigEntry', REFERENCE_LIST, 'StpxLoopGuardConfigEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects.StpxLoopGuardGlobalDefaultMode_Enum' : _MetaInfoEnum('StpxLoopGuardGlobalDefaultMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects',
            False, 
            [
            _MetaInfoClassMember('stpxLoopGuardGlobalDefaultMode', REFERENCE_ENUM_CLASS, 'StpxLoopGuardGlobalDefaultMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects.StpxLoopGuardGlobalDefaultMode_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry',
            False, 
            [
            _MetaInfoClassMember('stpxLoopInconsistencyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The Spanning Tree instance id, such as the VLAN id
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1) or rapidPvstPlus(5).
                ''',
                'stpxloopinconsistencyindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxLoopInconsistencyPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable',
            False, 
            [
            _MetaInfoClassMember('stpxLoopInconsistencyEntry', REFERENCE_LIST, 'StpxLoopInconsistencyEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 256)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceEntry', REFERENCE_LIST, 'StpxMISTPInstanceEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMISTPObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMISTPObjects',
            False, 
            [
            _MetaInfoClassMember('stpxMISTPInstanceNumber', ATTRIBUTE, 'int' , None, None, 
                [(1, 256)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEditIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEditEntry', REFERENCE_LIST, 'StpxMSTInstanceEditEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                An integer that uniquely identifies an MST instance 
                within the range of 0 to the object value of
                stpxMSTMaxInstanceNumber.
                
                This object is deprecated and replaced by 
                stpxSMSTInstanceIndex.
                ''',
                'stpxmstinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTInstanceRemainingHopCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 40)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTInstanceEntry', REFERENCE_LIST, 'StpxMSTInstanceEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferOperation_Enum' : _MetaInfoEnum('StpxMSTRegionEditBufferOperation_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'other':'OTHER',
            'acquire':'ACQUIRE',
            'releaseWithForce':'RELEASEWITHFORCE',
            'commit':'COMMIT',
            'rollBack':'ROLLBACK',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferStatus_Enum' : _MetaInfoEnum('StpxMSTRegionEditBufferStatus_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'released':'RELEASED',
            'acquiredBySnmp':'ACQUIREDBYSNMP',
            'acquiredByNonSnmp':'ACQUIREDBYNONSNMP',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxMSTObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTObjects',
            False, 
            [
            _MetaInfoClassMember('stpxMSTMaxHopCount', ATTRIBUTE, 'int' , None, None, 
                [(1, 40)], [], 
                '''                The maximum number of hops for the MST region. 
                
                This object will take on value of 40 if the object value
                of stpxSMSTMaxHopCount is greater than 40.
                
                This object is deprecated and replaced by
                stpxSMSTMaxHopCount.
                ''',
                'stpxmstmaxhopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTMaxInstanceNumber', ATTRIBUTE, 'int' , None, None, 
                [(1, 256)], [], 
                '''                The maximum MST (Multiple Spanning Tree) instance id, 
                that can be supported by the device for Cisco proprietary
                implementation of the MST Protocol.
                
                This object is deprecated and replaced by 
                stpxSMSTMaxInstanceID.
                ''',
                'stpxmstmaxinstancenumber',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTRegionEditBufferOperation', REFERENCE_ENUM_CLASS, 'StpxMSTRegionEditBufferOperation_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferOperation_Enum', 
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
            _MetaInfoClassMember('stpxMSTRegionEditBufferStatus', REFERENCE_ENUM_CLASS, 'StpxMSTRegionEditBufferStatus_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTObjects.StpxMSTRegionEditBufferStatus_Enum', 
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
                [(1, 65535)], [], 
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
                [(1, 65535)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry.StpxMSTPortRoleValue_Enum' : _MetaInfoEnum('StpxMSTPortRoleValue_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'disabled':'DISABLED',
            'root':'ROOT',
            'designated':'DESIGNATED',
            'alternate':'ALTERNATE',
            'backUp':'BACKUP',
            'boundary':'BOUNDARY',
            'master':'MASTER',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortRoleInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 256)], [], 
                '''                The MST instance id within the range of 0 to
                stpxMSTMaxInstanceNumber.
                ''',
                'stpxmstportroleinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortRolePortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxmstportroleportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortRoleValue', REFERENCE_ENUM_CLASS, 'StpxMSTPortRoleValue_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry.StpxMSTPortRoleValue_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortRoleEntry', REFERENCE_LIST, 'StpxMSTPortRoleEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortAdminLinkType_Enum' : _MetaInfoEnum('StpxMSTPortAdminLinkType_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'POINTTOPOINT',
            'shared':'SHARED',
            'auto':'AUTO',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortOperLinkType_Enum' : _MetaInfoEnum('StpxMSTPortOperLinkType_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'POINTTOPOINT',
            'shared':'SHARED',
            'other':'OTHER',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxmstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxMSTPortAdminLinkType', REFERENCE_ENUM_CLASS, 'StpxMSTPortAdminLinkType_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortAdminLinkType_Enum', 
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
            _MetaInfoClassMember('stpxMSTPortOperLinkType', REFERENCE_ENUM_CLASS, 'StpxMSTPortOperLinkType_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortOperLinkType_Enum', 
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
            _MetaInfoClassMember('stpxMSTPortStatus', REFERENCE_BITS, 'StpxMSTPortStatus_Bits' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry.StpxMSTPortStatus_Bits', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxMSTPortTable',
            False, 
            [
            _MetaInfoClassMember('stpxMSTPortEntry', REFERENCE_LIST, 'StpxMSTPortEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry.StpxPVSTVlanEnable_Enum' : _MetaInfoEnum('StpxPVSTVlanEnable_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
            'notApplicable':'NOTAPPLICABLE',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry',
            False, 
            [
            _MetaInfoClassMember('stpxPVSTVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                An index value that uniquely identifies the
                Virtual LAN associated with this information.
                ''',
                'stpxpvstvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxPVSTVlanEnable', REFERENCE_ENUM_CLASS, 'StpxPVSTVlanEnable_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry.StpxPVSTVlanEnable_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable',
            False, 
            [
            _MetaInfoClassMember('stpxPVSTVlanEntry', REFERENCE_LIST, 'StpxPVSTVlanEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry',
            False, 
            [
            _MetaInfoClassMember('stpxRPVSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrpvstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRPVSTPortVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VLAN id of the VLAN.
                ''',
                'stpxrpvstportvlanindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRPVSTPortStatus', REFERENCE_BITS, 'StpxRPVSTPortStatus_Bits' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry.StpxRPVSTPortStatus_Bits', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable',
            False, 
            [
            _MetaInfoClassMember('stpxRPVSTPortEntry', REFERENCE_LIST, 'StpxRPVSTPortEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRSTPObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRSTPObjects',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPTransmitHoldCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Transmit Hold Count.
                ''',
                'stpxrstptransmitholdcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxRSTPObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry.StpxRSTPPortRoleValue_Enum' : _MetaInfoEnum('StpxRSTPPortRoleValue_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'disabled':'DISABLED',
            'root':'ROOT',
            'designated':'DESIGNATED',
            'alternate':'ALTERNATE',
            'backUp':'BACKUP',
            'boundary':'BOUNDARY',
            'master':'MASTER',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortRoleInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The Spanning Tree instance id, it can either be a 
                VLAN number if the stpxSpanningTreeType is rapidPvstPlus(5) 
                or an MST instance id if the stpxSpanningTreeType is mst(4).
                ''',
                'stpxrstpportroleinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortRolePortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrstpportroleportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortRoleValue', REFERENCE_ENUM_CLASS, 'StpxRSTPPortRoleValue_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry.StpxRSTPPortRoleValue_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortRoleEntry', REFERENCE_LIST, 'StpxRSTPPortRoleEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortAdminLinkType_Enum' : _MetaInfoEnum('StpxRSTPPortAdminLinkType_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'POINTTOPOINT',
            'shared':'SHARED',
            'auto':'AUTO',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortOperLinkType_Enum' : _MetaInfoEnum('StpxRSTPPortOperLinkType_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'pointToPoint':'POINTTOPOINT',
            'shared':'SHARED',
            'other':'OTHER',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxrstpportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRSTPPortAdminLinkType', REFERENCE_ENUM_CLASS, 'StpxRSTPPortAdminLinkType_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortAdminLinkType_Enum', 
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
            _MetaInfoClassMember('stpxRSTPPortOperLinkType', REFERENCE_ENUM_CLASS, 'StpxRSTPPortOperLinkType_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry.StpxRSTPPortOperLinkType_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable',
            False, 
            [
            _MetaInfoClassMember('stpxRSTPPortEntry', REFERENCE_LIST, 'StpxRSTPPortEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry',
            False, 
            [
            _MetaInfoClassMember('stpxRootGuardConfigPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable',
            False, 
            [
            _MetaInfoClassMember('stpxRootGuardConfigEntry', REFERENCE_LIST, 'StpxRootGuardConfigEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry',
            False, 
            [
            _MetaInfoClassMember('stpxRootInconsistencyIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The Spanning Tree instance id, such as the VLAN id
                of the VLAN if the object value of stpxSpanningTreeType
                is pvstPlus(1) or rapidPvstPlus(5).
                ''',
                'stpxrootinconsistencyindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxRootInconsistencyPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable',
            False, 
            [
            _MetaInfoClassMember('stpxRootInconsistencyEntry', REFERENCE_LIST, 'StpxRootInconsistencyEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEditIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The MST instance ID, the value of which is in the range from
                0 to stpxSMSTMaxInstanceID. 
                
                The instances of this table entry with 
                stpxSMSTInstanceEditIndex of zero is automatically
                created by the device and can not modified.
                ''',
                'stpxsmstinstanceeditindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTInstanceEditRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEditEntry', REFERENCE_LIST, 'StpxSMSTInstanceEditEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The MST instance ID, the value of which is in the range 
                from 0 to stpxSMSTMaxInstanceID.
                ''',
                'stpxsmstinstanceindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTInstanceCISTIntRootCost', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(-1, 2147483647)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTInstanceEntry', REFERENCE_LIST, 'StpxSMSTInstanceEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTObjects',
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
                [(0, 4294967295)], [], 
                '''                The maximum number of hops for the IEEE MST region.
                ''',
                'stpxsmstmaxhopcount',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTMaxInstanceID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum MST instance ID that can be supported 
                by the device for IEEE MST.
                ''',
                'stpxsmstmaxinstanceid',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTMaxInstances', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of MST instances that can be 
                supported by the device for IEEE MST.
                ''',
                'stpxsmstmaxinstances',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTRegionEditRevision', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The MST region version in the Edit Buffer for IEEE 
                MST.
                
                This object is only instantiated when the 
                stpxMSTRegionEditBufferStatus has the value of 
                acquiredBySnmp(2).
                ''',
                'stpxsmstregioneditrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTRegionRevision', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The operational region version for IEEE MST.
                ''',
                'stpxsmstregionrevision',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'stpxSMSTObjects',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortAdminMSTMode_Enum' : _MetaInfoEnum('StpxSMSTPortAdminMSTMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'preStandard':'PRESTANDARD',
            'auto':'AUTO',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortOperMSTMode_Enum' : _MetaInfoEnum('StpxSMSTPortOperMSTMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'unknown':'UNKNOWN',
            'preStandard':'PRESTANDARD',
            'standard':'STANDARD',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of dot1dBasePort (i.e. dot1dBridge.1.4)
                for the bridge port.
                ''',
                'stpxsmstportindex',
                'CISCO-STP-EXTENSIONS-MIB', True),
            _MetaInfoClassMember('stpxSMSTPortAdminHelloTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('stpxSMSTPortAdminMSTMode', REFERENCE_ENUM_CLASS, 'StpxSMSTPortAdminMSTMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortAdminMSTMode_Enum', 
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
                [(0, 4294967295)], [], 
                '''                Indicates the effective configuration of the hello time on 
                a port.
                ''',
                'stpxsmstportconfigedhellotime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortOperHelloTime', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The operational hello time in hundredth of seconds on a 
                port for IEEE MST. If this object value is not
                applicable on a port, then the value retrieved on that
                port will be -1.
                ''',
                'stpxsmstportoperhellotime',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortOperMSTMode', REFERENCE_ENUM_CLASS, 'StpxSMSTPortOperMSTMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortOperMSTMode_Enum', 
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
            _MetaInfoClassMember('stpxSMSTPortStatus', REFERENCE_BITS, 'StpxSMSTPortStatus_Bits' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry.StpxSMSTPortStatus_Bits', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable',
            False, 
            [
            _MetaInfoClassMember('stpxSMSTPortEntry', REFERENCE_LIST, 'StpxSMSTPortEntry' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostMode_Enum' : _MetaInfoEnum('StpxSpanningTreePathCostMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'short':'SHORT',
            'long':'LONG',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostOperMode_Enum' : _MetaInfoEnum('StpxSpanningTreePathCostOperMode_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'short':'SHORT',
            'long':'LONG',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreeType_Enum' : _MetaInfoEnum('StpxSpanningTreeType_Enum', 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB',
        {
            'pvstPlus':'PVSTPLUS',
            'mistp':'MISTP',
            'mistpPvstPlus':'MISTPPVSTPLUS',
            'mst':'MST',
            'rapidPvstPlus':'RAPIDPVSTPLUS',
        }, 'CISCO-STP-EXTENSIONS-MIB', _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB']),
    'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects',
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
            _MetaInfoClassMember('stpxNotificationEnable', REFERENCE_BITS, 'StpxNotificationEnable_Bits' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxNotificationEnable_Bits', 
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
            _MetaInfoClassMember('stpxSpanningTreePathCostMode', REFERENCE_ENUM_CLASS, 'StpxSpanningTreePathCostMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostMode_Enum', 
                [], [], 
                '''                Indicates the administrative  spanning tree path cost mode 
                configured on device.
                ''',
                'stpxspanningtreepathcostmode',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreePathCostOperMode', REFERENCE_ENUM_CLASS, 'StpxSpanningTreePathCostOperMode_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreePathCostOperMode_Enum', 
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
            _MetaInfoClassMember('stpxSpanningTreeType', REFERENCE_ENUM_CLASS, 'StpxSpanningTreeType_Enum' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects.StpxSpanningTreeType_Enum', 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects',
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
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 32000)], [], 
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
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
    'CISCOSTPEXTENSIONSMIB' : {
        'meta_info' : _MetaInfoClass('CISCOSTPEXTENSIONSMIB',
            False, 
            [
            _MetaInfoClassMember('stpxBackboneFastObjects', REFERENCE_CLASS, 'StpxBackboneFastObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects', 
                [], [], 
                '''                ''',
                'stpxbackbonefastobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingObjects', REFERENCE_CLASS, 'StpxBpduSkewingObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects', 
                [], [], 
                '''                ''',
                'stpxbpduskewingobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxBpduSkewingTable', REFERENCE_CLASS, 'StpxBpduSkewingTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable', 
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
            _MetaInfoClassMember('stpxFastStartObjects', REFERENCE_CLASS, 'StpxFastStartObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartObjects', 
                [], [], 
                '''                ''',
                'stpxfaststartobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartOperModeTable', REFERENCE_CLASS, 'StpxFastStartOperModeTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable', 
                [], [], 
                '''                A table containing a list of the bridge ports 
                for a particular Spanning Tree Instance.
                ''',
                'stpxfaststartopermodetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxFastStartPortTable', REFERENCE_CLASS, 'StpxFastStartPortTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable', 
                [], [], 
                '''                A table containing a list of the bridge ports for
                which Spanning Tree Port Fast Start can be
                configured.
                ''',
                'stpxfaststartporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxInconsistencyTable', REFERENCE_CLASS, 'StpxInconsistencyTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable', 
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
            _MetaInfoClassMember('stpxLoopGuardConfigTable', REFERENCE_CLASS, 'StpxLoopGuardConfigTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                Spanning Tree LoopGuard capability can be configured.
                ''',
                'stpxloopguardconfigtable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopGuardObjects', REFERENCE_CLASS, 'StpxLoopGuardObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects', 
                [], [], 
                '''                ''',
                'stpxloopguardobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxLoopInconsistencyTable', REFERENCE_CLASS, 'StpxLoopInconsistencyTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable', 
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
            _MetaInfoClassMember('stpxMISTPInstanceTable', REFERENCE_CLASS, 'StpxMISTPInstanceTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable', 
                [], [], 
                '''                This table contains one entry for each instance of MISTP and 
                it contains stpxMISTPInstanceNumber entries, numbered from 1
                to stpxMISTPInstanceNumber.
                
                This table is only instantiated when the value of 
                stpxSpanningTreeType is mistp(2) or mistpPvstPlus(3).
                ''',
                'stpxmistpinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMISTPObjects', REFERENCE_CLASS, 'StpxMISTPObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMISTPObjects', 
                [], [], 
                '''                ''',
                'stpxmistpobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTInstanceEditTable', REFERENCE_CLASS, 'StpxMSTInstanceEditTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable', 
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
            _MetaInfoClassMember('stpxMSTInstanceTable', REFERENCE_CLASS, 'StpxMSTInstanceTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable', 
                [], [], 
                '''                This table contains MST instance information with
                one entry for an MST instance within the range of 
                0 to the object value of stpxMSTMaxInstanceNumber. 
                
                This table is deprecated and replaced by 
                stpxSMSTInstanceTable.
                ''',
                'stpxmstinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTObjects', REFERENCE_CLASS, 'StpxMSTObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTObjects', 
                [], [], 
                '''                ''',
                'stpxmstobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortRoleTable', REFERENCE_CLASS, 'StpxMSTPortRoleTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable', 
                [], [], 
                '''                A table containing a list of the bridge ports for a 
                particular MST instance.  This table is only instantiated 
                when the stpxSpanningTreeType is mst(4). 
                
                This table is deprecated and replaced with 
                stpxRSTPPortRoleTable.
                ''',
                'stpxmstportroletable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxMSTPortTable', REFERENCE_CLASS, 'StpxMSTPortTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxMSTPortTable', 
                [], [], 
                '''                A table containing port information for the MST 
                Protocol on all the bridge ports existing on the 
                system.
                ''',
                'stpxmstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxPVSTVlanTable', REFERENCE_CLASS, 'StpxPVSTVlanTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable', 
                [], [], 
                '''                A list of Virtual LAN entries containing
                information for Spanning Tree PVST+ protocol. 
                An entry will exist for each VLAN existing on 
                the device.
                ''',
                'stpxpvstvlantable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRootGuardConfigTable', REFERENCE_CLASS, 'StpxRootGuardConfigTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable', 
                [], [], 
                '''                A table containing a list of the bridge ports for which
                Spanning Tree RootGuard capability can be configured.
                ''',
                'stpxrootguardconfigtable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRootInconsistencyTable', REFERENCE_CLASS, 'StpxRootInconsistencyTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable', 
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
            _MetaInfoClassMember('stpxRPVSTPortTable', REFERENCE_CLASS, 'StpxRPVSTPortTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable', 
                [], [], 
                '''                A table containing a list of the bridge ports 
                for a particular Spanning Tree Instance.
                This table is only instantiated when the object value
                of stpxSpanningTreeType is rapidPvstPlus(5).
                ''',
                'stpxrpvstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPObjects', REFERENCE_CLASS, 'StpxRSTPObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPObjects', 
                [], [], 
                '''                ''',
                'stpxrstpobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortRoleTable', REFERENCE_CLASS, 'StpxRSTPPortRoleTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable', 
                [], [], 
                '''                A table containing a list of the bridge ports for a 
                particular Spanning Tree instance.  This table is 
                only instantiated when the stpxSpanningTreeType is mst(4) 
                or rapidPvstPlus(5).
                ''',
                'stpxrstpportroletable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxRSTPPortTable', REFERENCE_CLASS, 'StpxRSTPPortTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable', 
                [], [], 
                '''                A table containing port information for the RSTP 
                Protocol on all the bridge ports existing in the 
                system.
                ''',
                'stpxrstpporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceEditTable', REFERENCE_CLASS, 'StpxSMSTInstanceEditTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable', 
                [], [], 
                '''                This table contains MST instance information in the 
                Edit Buffer. 
                
                This table is only instantiated when the object value
                of  stpxMSTRegionEditBufferStatus has the value of
                acquiredBySnmp(2).
                ''',
                'stpxsmstinstanceedittable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTInstanceTable', REFERENCE_CLASS, 'StpxSMSTInstanceTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable', 
                [], [], 
                '''                This table contains MST instance information
                for IEEE MST.
                ''',
                'stpxsmstinstancetable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTObjects', REFERENCE_CLASS, 'StpxSMSTObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTObjects', 
                [], [], 
                '''                ''',
                'stpxsmstobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSMSTPortTable', REFERENCE_CLASS, 'StpxSMSTPortTable' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable', 
                [], [], 
                '''                A table containing port information for the MST 
                Protocol on all the bridge ports existing on the 
                system.
                
                This table is only instantiated when the object 
                value of stpxSpanningTreeType is mst(4)
                ''',
                'stpxsmstporttable',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxSpanningTreeObjects', REFERENCE_CLASS, 'StpxSpanningTreeObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects', 
                [], [], 
                '''                ''',
                'stpxspanningtreeobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            _MetaInfoClassMember('stpxUplinkFastObjects', REFERENCE_CLASS, 'StpxUplinkFastObjects' , 'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB', 'CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects', 
                [], [], 
                '''                ''',
                'stpxuplinkfastobjects',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'CISCO-STP-EXTENSIONS-MIB',
            'CISCO-STP-EXTENSIONS-MIB',
            _yang_ns._namespaces['CISCO-STP-EXTENSIONS-MIB'],
        'ydk.models.stp.CISCO_STP_EXTENSIONS_MIB'
        ),
    },
}
_meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable.StpxBpduSkewingEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable.StpxFastStartOperModeEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable.StpxFastStartPortEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable.StpxInconsistencyEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable.StpxLoopGuardConfigEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable.StpxLoopInconsistencyEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable.StpxMISTPInstanceEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable.StpxMSTInstanceEditEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable.StpxMSTInstanceEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable.StpxMSTPortRoleEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable.StpxMSTPortEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable.StpxPVSTVlanEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable.StpxRPVSTPortEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable.StpxRSTPPortRoleEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable.StpxRSTPPortEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable.StpxRootGuardConfigEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable.StpxRootInconsistencyEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable.StpxSMSTInstanceEditEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable.StpxSMSTInstanceEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable.StpxSMSTPortEntry']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxBackboneFastObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxBpduSkewingTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartOperModeTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxFastStartPortTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxInconsistencyTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardConfigTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopGuardObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxLoopInconsistencyTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPInstanceTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMISTPObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceEditTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTInstanceTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortRoleTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxMSTPortTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxPVSTVlanTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRPVSTPortTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortRoleTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRSTPPortTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootGuardConfigTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxRootInconsistencyTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceEditTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTInstanceTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSMSTPortTable']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxSpanningTreeObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']
_meta_table['CISCOSTPEXTENSIONSMIB.StpxUplinkFastObjects']['meta_info'].parent =_meta_table['CISCOSTPEXTENSIONSMIB']['meta_info']

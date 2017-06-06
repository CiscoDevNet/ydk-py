


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscobfddiagEnum' : _MetaInfoEnum('CiscobfddiagEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'noDiagnostic':'noDiagnostic',
            'controlDetectionTimeExpired':'controlDetectionTimeExpired',
            'echoFunctionFailed':'echoFunctionFailed',
            'neighborSignaledSessionDown':'neighborSignaledSessionDown',
            'forwardingPlaneReset':'forwardingPlaneReset',
            'pathDown':'pathDown',
            'concatenatedPathDown':'concatenatedPathDown',
            'administrativelyDown':'administrativelyDown',
            'reverseConcatenatedPathDown':'reverseConcatenatedPathDown',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdscalarobjects.CiscobfdadminstatusEnum' : _MetaInfoEnum('CiscobfdadminstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdscalarobjects' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdscalarobjects',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdAdminStatus', REFERENCE_ENUM_CLASS, 'CiscobfdadminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdscalarobjects.CiscobfdadminstatusEnum', 
                [], [], 
                '''                The global administrative status of BFD in this router.
                The value 'enabled' denotes that the BFD Process is 
                active on at least one interface; 'disabled' disables  
                it on all interfaces.
                ''',
                'ciscobfdadminstatus',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessNotificationsEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is set to true(1), then it enables
                the emission of ciscoBfdSessUp and ciscoBfdSessDown 
                notifications; otherwise these notifications are not 
                emitted.
                ''',
                'ciscobfdsessnotificationsenable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdVersionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current version number of the BFD protocol.
                ''',
                'ciscobfdversionnumber',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdScalarObjects',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessauthenticationtypeEnum' : _MetaInfoEnum('CiscobfdsessauthenticationtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'simplePassword':'simplePassword',
            'keyedMD5':'keyedMD5',
            'meticulousKeyedMD5':'meticulousKeyedMD5',
            'keyedSHA1':'keyedSHA1',
            'meticulousKeyedSHA1':'meticulousKeyedSHA1',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessopermodeEnum' : _MetaInfoEnum('CiscobfdsessopermodeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'asyncModeWEchoFun':'asyncModeWEchoFun',
            'asynchModeWOEchoFun':'asynchModeWOEchoFun',
            'demandModeWEchoFunction':'demandModeWEchoFunction',
            'demandModeWOEchoFunction':'demandModeWOEchoFunction',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessstateEnum' : _MetaInfoEnum('CiscobfdsessstateEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'adminDown':'adminDown',
            'down':'down',
            'init':'init',
            'up':'up',
            'failing':'failing',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsesstypeEnum' : _MetaInfoEnum('CiscobfdsesstypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB',
        {
            'singleHop':'singleHop',
            'multiHop':'multiHop',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object contains an index used to represent a
                unique BFD session on this device.
                ''',
                'ciscobfdsessindex',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the neighboring IP address which is
                being monitored with this BFD session.
                It can also be used to enabled BFD on a specific  
                interface. The value is set to zero when BFD session is not  
                associated with a specific interface.
                ''',
                'ciscobfdsessaddr',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies IP address type of the neighboring IP
                address which is being monitored with this BFD session.
                
                Only values unknown(0), ipv4(1) or ipv6(2) 
                have to be supported.  
                
                A value of unknown(0) is allowed only when  
                the outgoing interface is of type point-to-point, or 
                when the BFD session is not associated with a specific  
                interface. 
                
                If any other unsupported values are attempted in a set 
                operation, the agent MUST return an inconsistentValue  
                error.
                ''',
                'ciscobfdsessaddrtype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessApplicationId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an index used to indicate
                a local application which owns or maintains this 
                BFD session. For instance, the MPLS VPN process may 
                maintain a subset of the total number of BFD 
                sessions.  This application ID provides a convenient 
                way to segregate sessions by the applications which 
                maintain them.
                ''',
                'ciscobfdsessapplicationid',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessAuthenticationType', REFERENCE_ENUM_CLASS, 'CiscobfdsessauthenticationtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessauthenticationtypeEnum', 
                [], [], 
                '''                The Authentication Type used for this BFD session. This
                field is valid only when the Authentication Present bit is set
                ''',
                'ciscobfdsessauthenticationtype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessAuthPresFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates that the local system's
                desire to use Authentication. Specifically, it is set  
                to true(1) if the local system wishes the session  
                to be authenticated or false(0) if not
                ''',
                'ciscobfdsessauthpresflag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessControlPlanIndepFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates that the local system's
                ability to continue to function through a disruption of  
                the control plane. Specifically, it is set  
                to true(1) if the local system BFD implementation is 
                independent of the control plane. Otherwise, the  
                value is set to false(0)
                ''',
                'ciscobfdsesscontrolplanindepflag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDemandModeDesiredFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates that the local system's
                desire to use Demand mode. Specifically, it is set  
                to true(1) if the local system wishes to use  
                Demand mode or false(0) if not
                ''',
                'ciscobfdsessdemandmodedesiredflag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDesiredMinTxInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the minimum interval, in
                microseconds, that the local system would like to use when 
                     transmitting BFD Control packets.
                ''',
                'ciscobfdsessdesiredmintxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDetectMult', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the Detect time multiplier.
                ''',
                'ciscobfdsessdetectmult',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiag', REFERENCE_ENUM_CLASS, 'CiscobfddiagEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscobfddiagEnum', 
                [], [], 
                '''                A diagnostic code specifying the local system's reason
                for the last transition of the session from up(1)  
                to some other state.
                ''',
                'ciscobfdsessdiag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the local discriminator for this BFD
                session, used to uniquely identify it.
                ''',
                'ciscobfdsessdiscriminator',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessEchoFuncModeDesiredFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates that the local system's
                desire to use Echo mode. Specifically, it is set  
                to true(1) if the local system wishes to use  
                Echo mode or false(0) if not
                ''',
                'ciscobfdsessechofuncmodedesiredflag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object contains an interface index used to indicate
                the interface which this BFD session is running on.
                ''',
                'ciscobfdsessinterface',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessOperMode', REFERENCE_ENUM_CLASS, 'CiscobfdsessopermodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessopermodeEnum', 
                [], [], 
                '''                This object specifies current operating mode that BFD
                session is operating in.
                ''',
                'ciscobfdsessopermode',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfDiscTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which any one or more of the session counters suffered 
                a discontinuity.  
                
                The relevant counters are the specific instances associated  
                with this BFD session of any Counter32 object contained in 
                the ciscoBfdSessPerfTable. If no such discontinuities have occurred  
                since the last re-initialization of the local management 
                subsystem, then this object contains a zero value.
                ''',
                'ciscobfdsessperfdisctime',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfLastCommLostDiag', REFERENCE_ENUM_CLASS, 'CiscobfddiagEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscobfddiagEnum', 
                [], [], 
                '''                The BFD diag code for the last time communication was lost
                with the neighbor. If no such down event exists this object  
                contains a zero value.
                ''',
                'ciscobfdsessperflastcommlostdiag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfLastSessDownTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                the last time communication was lost with the neighbor. If  
                no such down event exist this object contains a zero value.
                ''',
                'ciscobfdsessperflastsessdowntime',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of BFD messages received for this BFD
                session.
                ''',
                'ciscobfdsessperfpktin',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktInHC', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This value represents the total number of BFD messages
                received for this BFD session. It MUST be equal to the 
                least significant 32 bits of ciscoBfdSessPerfPktIn 
                if ciscoBfdSessPerfPktInHC is supported according to 
                the rules spelled out in RFC2863.
                ''',
                'ciscobfdsessperfpktinhc',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of BFD messages sent for this BFD session.
                ''',
                'ciscobfdsessperfpktout',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktOutHC', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This value represents the total number of
                total number of BFD messages transmitted for this  
                BFD session. It MUST be equal to the 
                least significant 32 bits of ciscoBfdSessPerfPktIn 
                if ciscoBfdSessPerfPktOutHC is supported according to 
                the rules spelled out in RFC2863.
                ''',
                'ciscobfdsessperfpktouthc',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfSessUpCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this session has gone into the Up
                state since the router last rebooted.
                ''',
                'ciscobfdsessperfsessupcount',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessRemoteDiscr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the session discriminator chosen
                by the remote system for this BFD session.
                ''',
                'ciscobfdsessremotediscr',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessRemoteHeardFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies status of BFD packet reception from
                the remote system. Specifically, it is set to true(1) if 
                the local system is actively receiving BFD packets from the  
                remote system, and is set to false(0) if the local system  
                has not received BFD packets recently (within the detection  
                time) or if the local system is attempting to tear down 
                the BFD session.
                ''',
                'ciscobfdsessremoteheardflag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessReqMinEchoRxInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the minimum interval, in
                microseconds, between received BFD Echo packets that this 
                system is capable of supporting.
                ''',
                'ciscobfdsessreqminechorxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessReqMinRxInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the minimum interval, in
                microseconds, between received  BFD Control packets the  
                local system is capable of supporting.
                ''',
                'ciscobfdsessreqminrxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table. When a row in this 
                table has a row in the active(1) state, no  
                objects in this row can be modified except the 
                ciscoBfdSessRowStatus and ciscoBfdSessStorageType.
                ''',
                'ciscobfdsessrowstatus',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessState', REFERENCE_ENUM_CLASS, 'CiscobfdsessstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsessstateEnum', 
                [], [], 
                '''                The perceived state of the BFD session.
                ''',
                'ciscobfdsessstate',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessStorType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. Conceptual rows having the value  
                'permanent' need not allow write-access to any  
                columnar objects in the row.
                ''',
                'ciscobfdsessstortype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessType', REFERENCE_ENUM_CLASS, 'CiscobfdsesstypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry.CiscobfdsesstypeEnum', 
                [], [], 
                '''                The type of this BFD session.
                ''',
                'ciscobfdsesstype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessUdpPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The destination UDP Port for BFD. The default value is
                the well-known value for this port. BFD State failing(5)
                is only applicable if this BFD session is running
                version 0
                ''',
                'ciscobfdsessudpport',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                the session came up. If no such up event exists this object 
                contains a zero value.
                ''',
                'ciscobfdsessuptime',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessVersionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The version number of the BFD protocol that this session is
                running in.
                ''',
                'ciscobfdsessversionnumber',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessEntry',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsesstable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsesstable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessEntry', REFERENCE_LIST, 'Ciscobfdsessentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry', 
                [], [], 
                '''                The BFD Session Entry describes BFD session.
                ''',
                'ciscobfdsessentry',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessTable',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessApplicationId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'ciscobfdsessapplicationid',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscobfdsessdiscriminator',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'ciscobfdsessaddrtype',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'ciscobfdsessaddr',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessMapBfdIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the CiscoBfdSessIndexTC referred to
                by the indices of this row. In essence, a mapping is 
                provided between these indices and the ciscoBfdSessTable.
                ''',
                'ciscobfdsessmapbfdindex',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessMapEntry',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessmaptable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessMapEntry', REFERENCE_LIST, 'Ciscobfdsessmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry', 
                [], [], 
                '''                The BFD Session Entry describes BFD session
                that is mapped to this index.
                ''',
                'ciscobfdsessmapentry',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessMapTable',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscobfdsessdiscriminator',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessDiscMapIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the CiscoBfdSessIndexTC referred to by
                the index of this row. In essence, a mapping is 
                provided between this index and the ciscoBfdSessTable.
                ''',
                'ciscobfdsessdiscmapindex',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessDiscMapEntry',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessdiscmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessdiscmaptable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessDiscMapEntry', REFERENCE_LIST, 'Ciscobfdsessdiscmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry', 
                [], [], 
                '''                Each row contains a mapping between a local discriminator
                value to an entry in ciscoBfdSessTable.
                ''',
                'ciscobfdsessdiscmapentry',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessDiscMapTable',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ciscobfdsessinterface',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                ''',
                'ciscobfdsessaddrtype',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'ciscobfdsessaddr',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessIpMapIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the CiscoBfdSessIndexTC referred to by
                the indices of this row. In essence, a mapping is 
                provided between these indices and an entry in ciscoBfdSessTable.
                ''',
                'ciscobfdsessipmapindex',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessIpMapEntry',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib.Ciscobfdsessipmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib.Ciscobfdsessipmaptable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessIpMapEntry', REFERENCE_LIST, 'Ciscobfdsessipmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry', 
                [], [], 
                '''                Each row contains a mapping between ciscoBfdSessInterface,
                ciscoBfdSessAddrType and ciscoBfdSessAddr values to an 
                entry in ciscoBfdSessTable.
                ''',
                'ciscobfdsessipmapentry',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessIpMapTable',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
    'CiscoIetfBfdMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfBfdMib',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdScalarObjects', REFERENCE_CLASS, 'Ciscobfdscalarobjects' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdscalarobjects', 
                [], [], 
                '''                ''',
                'ciscobfdscalarobjects',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiscMapTable', REFERENCE_CLASS, 'Ciscobfdsessdiscmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessdiscmaptable', 
                [], [], 
                '''                The BFD Session Discriminator Mapping Table maps a
                local discriminator value to associated BFD sessions'
                CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
                ''',
                'ciscobfdsessdiscmaptable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessIpMapTable', REFERENCE_CLASS, 'Ciscobfdsessipmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessipmaptable', 
                [], [], 
                '''                The BFD Session IP Mapping Table maps given
                ciscoBfdSessInterface, ciscoBfdSessAddrType, and
                ciscoBbfdSessAddr to an associated BFD sessions'
                CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
                This table SHOULD contains those BFD sessions are
                of IP type: singleHop(1) and multiHop(2).
                ''',
                'ciscobfdsessipmaptable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessMapTable', REFERENCE_CLASS, 'Ciscobfdsessmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsessmaptable', 
                [], [], 
                '''                The BFD Session Mapping Table maps the complex
                indexing of the BFD sessions to the flat 
                CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
                ''',
                'ciscobfdsessmaptable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessTable', REFERENCE_CLASS, 'Ciscobfdsesstable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB', 'CiscoIetfBfdMib.Ciscobfdsesstable', 
                [], [], 
                '''                The BFD Session Table describes the BFD sessions.
                ''',
                'ciscobfdsesstable',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'CISCO-IETF-BFD-MIB',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB'
        ),
    },
}
_meta_table['CiscoIetfBfdMib.Ciscobfdsesstable.Ciscobfdsessentry']['meta_info'].parent =_meta_table['CiscoIetfBfdMib.Ciscobfdsesstable']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessmaptable.Ciscobfdsessmapentry']['meta_info'].parent =_meta_table['CiscoIetfBfdMib.Ciscobfdsessmaptable']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry']['meta_info'].parent =_meta_table['CiscoIetfBfdMib.Ciscobfdsessdiscmaptable']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry']['meta_info'].parent =_meta_table['CiscoIetfBfdMib.Ciscobfdsessipmaptable']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdscalarobjects']['meta_info'].parent =_meta_table['CiscoIetfBfdMib']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsesstable']['meta_info'].parent =_meta_table['CiscoIetfBfdMib']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessmaptable']['meta_info'].parent =_meta_table['CiscoIetfBfdMib']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessdiscmaptable']['meta_info'].parent =_meta_table['CiscoIetfBfdMib']['meta_info']
_meta_table['CiscoIetfBfdMib.Ciscobfdsessipmaptable']['meta_info'].parent =_meta_table['CiscoIetfBfdMib']['meta_info']

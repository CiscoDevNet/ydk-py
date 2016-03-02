


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CiscoBfdDiag_Enum' : _MetaInfoEnum('CiscoBfdDiag_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'noDiagnostic':'NODIAGNOSTIC',
            'controlDetectionTimeExpired':'CONTROLDETECTIONTIMEEXPIRED',
            'echoFunctionFailed':'ECHOFUNCTIONFAILED',
            'neighborSignaledSessionDown':'NEIGHBORSIGNALEDSESSIONDOWN',
            'forwardingPlaneReset':'FORWARDINGPLANERESET',
            'pathDown':'PATHDOWN',
            'concatenatedPathDown':'CONCATENATEDPATHDOWN',
            'administrativelyDown':'ADMINISTRATIVELYDOWN',
            'reverseConcatenatedPathDown':'REVERSECONCATENATEDPATHDOWN',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdScalarObjects.CiscoBfdAdminStatus_Enum' : _MetaInfoEnum('CiscoBfdAdminStatus_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdScalarObjects' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdScalarObjects',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdAdminStatus', REFERENCE_ENUM_CLASS, 'CiscoBfdAdminStatus_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdScalarObjects.CiscoBfdAdminStatus_Enum', 
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
                [(0, 4294967295)], [], 
                '''                The current version number of the BFD protocol.
                ''',
                'ciscobfdversionnumber',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdScalarObjects',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'ciscobfdsessdiscriminator',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessDiscMapIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessDiscMapEntry', REFERENCE_LIST, 'CiscoBfdSessDiscMapEntry' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry', 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'ciscobfdsessaddr',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                ''',
                'ciscobfdsessaddrtype',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessInterface', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciscobfdsessinterface',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessIpMapIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessIpMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessIpMapTable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessIpMapEntry', REFERENCE_LIST, 'CiscoBfdSessIpMapEntry' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry', 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                ''',
                'ciscobfdsessaddr',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                ''',
                'ciscobfdsessaddrtype',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessApplicationId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'ciscobfdsessapplicationid',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'ciscobfdsessdiscriminator',
                'CISCO-IETF-BFD-MIB', True),
            _MetaInfoClassMember('ciscoBfdSessMapBfdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessMapTable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessMapEntry', REFERENCE_LIST, 'CiscoBfdSessMapEntry' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry', 
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
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessAuthenticationType_Enum' : _MetaInfoEnum('CiscoBfdSessAuthenticationType_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'simplePassword':'SIMPLEPASSWORD',
            'keyedMD5':'KEYEDMD5',
            'meticulousKeyedMD5':'METICULOUSKEYEDMD5',
            'keyedSHA1':'KEYEDSHA1',
            'meticulousKeyedSHA1':'METICULOUSKEYEDSHA1',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessOperMode_Enum' : _MetaInfoEnum('CiscoBfdSessOperMode_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'asyncModeWEchoFun':'ASYNCMODEWECHOFUN',
            'asynchModeWOEchoFun':'ASYNCHMODEWOECHOFUN',
            'demandModeWEchoFunction':'DEMANDMODEWECHOFUNCTION',
            'demandModeWOEchoFunction':'DEMANDMODEWOECHOFUNCTION',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessState_Enum' : _MetaInfoEnum('CiscoBfdSessState_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'adminDown':'ADMINDOWN',
            'down':'DOWN',
            'init':'INIT',
            'up':'UP',
            'failing':'FAILING',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessType_Enum' : _MetaInfoEnum('CiscoBfdSessType_Enum', 'ydk.models.ietf.CISCO_IETF_BFD_MIB',
        {
            'singleHop':'SINGLEHOP',
            'multiHop':'MULTIHOP',
        }, 'CISCO-IETF-BFD-MIB', _yang_ns._namespaces['CISCO-IETF-BFD-MIB']),
    'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
            _MetaInfoClassMember('ciscoBfdSessAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
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
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('ciscoBfdSessAuthenticationType', REFERENCE_ENUM_CLASS, 'CiscoBfdSessAuthenticationType_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessAuthenticationType_Enum', 
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
                [(0, 4294967295)], [], 
                '''                This object specifies the minimum interval, in
                microseconds, that the local system would like to use when 
                     transmitting BFD Control packets.
                ''',
                'ciscobfdsessdesiredmintxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDetectMult', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the Detect time multiplier.
                ''',
                'ciscobfdsessdetectmult',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiag', REFERENCE_ENUM_CLASS, 'CiscoBfdDiag_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CiscoBfdDiag_Enum', 
                [], [], 
                '''                A diagnostic code specifying the local system's reason
                for the last transition of the session from up(1)  
                to some other state.
                ''',
                'ciscobfdsessdiag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiscriminator', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
                [(1, 2147483647)], [], 
                '''                This object contains an interface index used to indicate
                the interface which this BFD session is running on.
                ''',
                'ciscobfdsessinterface',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessOperMode', REFERENCE_ENUM_CLASS, 'CiscoBfdSessOperMode_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessOperMode_Enum', 
                [], [], 
                '''                This object specifies current operating mode that BFD
                session is operating in.
                ''',
                'ciscobfdsessopermode',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfDiscTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('ciscoBfdSessPerfLastCommLostDiag', REFERENCE_ENUM_CLASS, 'CiscoBfdDiag_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CiscoBfdDiag_Enum', 
                [], [], 
                '''                The BFD diag code for the last time communication was lost
                with the neighbor. If no such down event exists this object  
                contains a zero value.
                ''',
                'ciscobfdsessperflastcommlostdiag',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfLastSessDownTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                the last time communication was lost with the neighbor. If  
                no such down event exist this object contains a zero value.
                ''',
                'ciscobfdsessperflastsessdowntime',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of BFD messages received for this BFD
                session.
                ''',
                'ciscobfdsessperfpktin',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktInHC', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This value represents the total number of BFD messages
                received for this BFD session. It MUST be equal to the 
                least significant 32 bits of ciscoBfdSessPerfPktIn 
                if ciscoBfdSessPerfPktInHC is supported according to 
                the rules spelled out in RFC2863.
                ''',
                'ciscobfdsessperfpktinhc',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of BFD messages sent for this BFD session.
                ''',
                'ciscobfdsessperfpktout',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessPerfPktOutHC', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
                [(0, 4294967295)], [], 
                '''                The number of times this session has gone into the Up
                state since the router last rebooted.
                ''',
                'ciscobfdsessperfsessupcount',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessRemoteDiscr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                This object specifies the minimum interval, in
                microseconds, between received BFD Echo packets that this 
                system is capable of supporting.
                ''',
                'ciscobfdsessreqminechorxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessReqMinRxInterval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object specifies the minimum interval, in
                microseconds, between received  BFD Control packets the  
                local system is capable of supporting.
                ''',
                'ciscobfdsessreqminrxinterval',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table. When a row in this 
                table has a row in the active(1) state, no  
                objects in this row can be modified except the 
                ciscoBfdSessRowStatus and ciscoBfdSessStorageType.
                ''',
                'ciscobfdsessrowstatus',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessState', REFERENCE_ENUM_CLASS, 'CiscoBfdSessState_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessState_Enum', 
                [], [], 
                '''                The perceived state of the BFD session.
                ''',
                'ciscobfdsessstate',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessStorType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. Conceptual rows having the value  
                'permanent' need not allow write-access to any  
                columnar objects in the row.
                ''',
                'ciscobfdsessstortype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessType', REFERENCE_ENUM_CLASS, 'CiscoBfdSessType_Enum' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry.CiscoBfdSessType_Enum', 
                [], [], 
                '''                The type of this BFD session.
                ''',
                'ciscobfdsesstype',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessUdpPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The destination UDP Port for BFD. The default value is
                the well-known value for this port. BFD State failing(5)
                is only applicable if this BFD session is running
                version 0
                ''',
                'ciscobfdsessudpport',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime on the most recent occasion at which
                the session came up. If no such up event exists this object 
                contains a zero value.
                ''',
                'ciscobfdsessuptime',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessVersionNumber', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The version number of the BFD protocol that this session is
                running in.
                ''',
                'ciscobfdsessversionnumber',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessEntry',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB.CiscoBfdSessTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB.CiscoBfdSessTable',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdSessEntry', REFERENCE_LIST, 'CiscoBfdSessEntry' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry', 
                [], [], 
                '''                The BFD Session Entry describes BFD session.
                ''',
                'ciscobfdsessentry',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'ciscoBfdSessTable',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
    'CISCOIETFBFDMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIETFBFDMIB',
            False, 
            [
            _MetaInfoClassMember('ciscoBfdScalarObjects', REFERENCE_CLASS, 'CiscoBfdScalarObjects' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdScalarObjects', 
                [], [], 
                '''                ''',
                'ciscobfdscalarobjects',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessDiscMapTable', REFERENCE_CLASS, 'CiscoBfdSessDiscMapTable' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable', 
                [], [], 
                '''                The BFD Session Discriminator Mapping Table maps a
                local discriminator value to associated BFD sessions'
                CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
                ''',
                'ciscobfdsessdiscmaptable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessIpMapTable', REFERENCE_CLASS, 'CiscoBfdSessIpMapTable' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessIpMapTable', 
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
            _MetaInfoClassMember('ciscoBfdSessMapTable', REFERENCE_CLASS, 'CiscoBfdSessMapTable' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessMapTable', 
                [], [], 
                '''                The BFD Session Mapping Table maps the complex
                indexing of the BFD sessions to the flat 
                CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
                ''',
                'ciscobfdsessmaptable',
                'CISCO-IETF-BFD-MIB', False),
            _MetaInfoClassMember('ciscoBfdSessTable', REFERENCE_CLASS, 'CiscoBfdSessTable' , 'ydk.models.ietf.CISCO_IETF_BFD_MIB', 'CISCOIETFBFDMIB.CiscoBfdSessTable', 
                [], [], 
                '''                The BFD Session Table describes the BFD sessions.
                ''',
                'ciscobfdsesstable',
                'CISCO-IETF-BFD-MIB', False),
            ],
            'CISCO-IETF-BFD-MIB',
            'CISCO-IETF-BFD-MIB',
            _yang_ns._namespaces['CISCO-IETF-BFD-MIB'],
        'ydk.models.ietf.CISCO_IETF_BFD_MIB'
        ),
    },
}
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable.CiscoBfdSessDiscMapEntry']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessIpMapTable.CiscoBfdSessIpMapEntry']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB.CiscoBfdSessIpMapTable']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessMapTable.CiscoBfdSessMapEntry']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB.CiscoBfdSessMapTable']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable.CiscoBfdSessEntry']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdScalarObjects']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessDiscMapTable']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessIpMapTable']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessMapTable']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB']['meta_info']
_meta_table['CISCOIETFBFDMIB.CiscoBfdSessTable']['meta_info'].parent =_meta_table['CISCOIETFBFDMIB']['meta_info']

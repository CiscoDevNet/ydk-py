


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EndpointclassEnum' : _MetaInfoEnum('EndpointclassEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'none':'none',
            'local':'local',
            'ipV4Address':'ipV4Address',
            'macAddress':'macAddress',
            'magicNumber':'magicNumber',
            'phone':'phone',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'TunneltypeEnum' : _MetaInfoEnum('TunneltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'l2f':'l2f',
            'l2tp':'l2tp',
            'pptp':'pptp',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs.CvpdnnotifsessioneventEnum' : _MetaInfoEnum('CvpdnnotifsessioneventEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'up':'up',
            'down':'down',
            'pwUp':'pwUp',
            'pwDown':'pwDown',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs',
            False, 
            [
            _MetaInfoClassMember('cvpdnNotifSessionEvent', REFERENCE_ENUM_CLASS, 'CvpdnnotifsessioneventEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs.CvpdnnotifsessioneventEnum', 
                [], [], 
                '''                Indicates the event that generated the L2X session
                notification.
                
                The events are represented as follows:
                
                up:     Session has come up.
                
                down:   Session has gone down.
                
                pwUp:   Pseudowire associated with this 
                        session has come up.
                
                pwDown: Pseudowire associated with this 
                        session has gone down.
                ''',
                'cvpdnnotifsessionevent',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnNotifSessionID', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object contains the local session ID of the L2X
                session for which this notification has been
                generated.
                ''',
                'cvpdnnotifsessionid',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'ciscoVpdnMgmtMIBNotifs',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnsysteminfo.CvpdnsystemclearsessionsEnum' : _MetaInfoEnum('CvpdnsystemclearsessionsEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'none':'none',
            'all':'all',
            'l2f':'l2f',
            'l2tp':'l2tp',
            'pptp':'pptp',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdnsysteminfo' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnsysteminfo',
            False, 
            [
            _MetaInfoClassMember('cvpdnDeniedUsersTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of denied user attempts to all the
                active VPDN tunnels within this system.
                ''',
                'cvpdndenieduserstotal',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active users in all the active VPDN
                tunnels within this system.
                ''',
                'cvpdnsessiontotal',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemClearSessions', REFERENCE_ENUM_CLASS, 'CvpdnsystemclearsessionsEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsysteminfo.CvpdnsystemclearsessionsEnum', 
                [], [], 
                '''                Clears all the sessions in a given tunnel type.  When
                reading this object, the value of 'none' will always be
                returned.
                
                When setting these values, the following operations will be
                performed:
                
                    none: no operation.
                
                    all:  clears all the sessions in all the tunnels.
                
                    l2f:  clears all the L2F sessions.
                
                    l2tp: clears all the L2TP sessions.
                
                    pptp: clears all the PPTP sessions.
                ''',
                'cvpdnsystemclearsessions',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemNotifSessionEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Layer 2 VPN session notifications are
                enabled.
                ''',
                'cvpdnsystemnotifsessionenabled',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VPDN tunnels that are currently
                active within this system.
                ''',
                'cvpdntunneltotal',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnSystemInfo',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnmultilinkinfo' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnmultilinkinfo',
            False, 
            [
            _MetaInfoClassMember('cvpdnBundleLastChanged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the sysUpTime object when the contents of
                cvpdnBundleTable last changed.
                ''',
                'cvpdnbundlelastchanged',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundlesWithMoreThanTwoLinks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of bundles comprised of more than two
                links.
                ''',
                'cvpdnbundleswithmorethantwolinks',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundlesWithOneLink', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of bundles comprised of a single link.
                ''',
                'cvpdnbundleswithonelink',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundlesWithTwoLinks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of bundles comprised of two links.
                ''',
                'cvpdnbundleswithtwolinks',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnMultilinkInfo',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry',
            False, 
            [
            _MetaInfoClassMember('cvpdnSystemTunnelType', REFERENCE_ENUM_CLASS, 'TunneltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunneltypeEnum', 
                [], [], 
                '''                The tunnel type.  This is the tunnel protocol.
                ''',
                'cvpdnsystemtunneltype',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnSystemDeniedUsersTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of denied user attempts to all the VPDN
                tunnels of this tunnel type since last system
                re-initialization.
                ''',
                'cvpdnsystemdenieduserstotal',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemFailedConnReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number tunnel Failed connection attempts in VPDN
                tunnels of this tunnel type since last system
                re-initialization.
                ''',
                'cvpdnsystemfailedconnreq',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemInitialConnReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number tunnel connection attempts on all the VPDN
                tunnels of this tunnel type since last system
                re-initialization.
                ''',
                'cvpdnsysteminitialconnreq',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemSessionTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active sessions in all the active VPDN
                tunnels of this tunnel type.
                ''',
                'cvpdnsystemsessiontotal',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemSuccessConnReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number tunnel Successful connection attempts in VPDN
                tunnels of this tunnel type since last system
                re-initialization.
                ''',
                'cvpdnsystemsuccessconnreq',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemTunnelTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of VPDN tunnels that are currently active
                of this tunnel type.
                ''',
                'cvpdnsystemtunneltotal',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnSystemEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnsystemtable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnsystemtable',
            False, 
            [
            _MetaInfoClassMember('cvpdnSystemEntry', REFERENCE_LIST, 'Cvpdnsystementry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single type of VPDN tunnel.
                ''',
                'cvpdnsystementry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnSystemTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelnetworkservicetypeEnum' : _MetaInfoEnum('CvpdntunnelnetworkservicetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'ip':'ip',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelorigcauseEnum' : _MetaInfoEnum('CvpdntunnelorigcauseEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'domain':'domain',
            'dnis':'dnis',
            'stack':'stack',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelstateEnum' : _MetaInfoEnum('CvpdntunnelstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'unknown':'unknown',
            'opening':'opening',
            'open':'open',
            'closing':'closing',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnTunnelTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Tunnel ID of an active VPDN tunnel.  If it is the
                instigator of the tunnel, the ID is the HGW/LNS tunnel
                ID, otherwise it is the NAS/LAC tunnel ID.
                ''',
                'cvpdntunneltunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelActiveSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active session currently in the
                tunnel.
                ''',
                'cvpdntunnelactivesessions',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelDeniedUsers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the accumulated total of denied users for
                the tunnel.
                ''',
                'cvpdntunneldeniedusers',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelLocalInitConnection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the tunnel was generated
                locally or not.
                ''',
                'cvpdntunnellocalinitconnection',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelLocalIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address of the tunnel.  This IP address is
                that of the interface at the local end of the tunnel.
                ''',
                'cvpdntunnellocalipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelLocalName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The local name of an active VPDN tunnel.  It will be
                the NAS/LAC name of the tunnel if the router serves as
                the NAS/LAC, or the HGW/LNS name of the tunnel if the
                system serves as the home gateway.  Typically, the
                local name is the configured host name of the router.
                ''',
                'cvpdntunnellocalname',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelNetworkServiceType', REFERENCE_ENUM_CLASS, 'CvpdntunnelnetworkservicetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelnetworkservicetypeEnum', 
                [], [], 
                '''                The type of network service used in the active tunnel.
                For now it is IP only.
                ''',
                'cvpdntunnelnetworkservicetype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelOrigCause', REFERENCE_ENUM_CLASS, 'CvpdntunnelorigcauseEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelorigcauseEnum', 
                [], [], 
                '''                The cause which originated an active VPDN tunnel.  The
                tunnel can be projected via domain name, DNIS or a
                stack group (SGBP).
                ''',
                'cvpdntunnelorigcause',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelRemoteEndpointName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The remote end point name of an active VPDN tunnel.
                This name is either the domain name or the DNIS that
                this tunnel is projected with.
                ''',
                'cvpdntunnelremoteendpointname',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelRemoteIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address of the tunnel.  This IP address
                is that of the interface at the remote end of the
                tunnel.
                ''',
                'cvpdntunnelremoteipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelRemoteName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The remote name of an active VPDN tunnel.  It will be
                the home gateway name of the tunnel if the system is a
                NAS/LAC, or the NAS/LAC name of the tunnel if the
                system serves as the home gateway.
                ''',
                'cvpdntunnelremotename',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelRemoteTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remote Tunnel ID of an active VPDN tunnel.  If it
                is the instigator of the tunnel, the ID is the NAS/LAC
                tunnel ID, otherwise it is the HGW/LNS tunnel ID.
                ''',
                'cvpdntunnelremotetunnelid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSoftshut', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A VPDN tunnel can be put into a soft shut state to
                prevent any new user session to be added.  This object
                specifies whether this tunnel has been soft shut.
                ''',
                'cvpdntunnelsoftshut',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSourceIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the tunnel.  This IP address
                is the user configurable IP address for Stack Group
                Biding Protocol (SGBP) via the CLI command:
                vpdn source-ip
                ''',
                'cvpdntunnelsourceipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelState', REFERENCE_ENUM_CLASS, 'CvpdntunnelstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.CvpdntunnelstateEnum', 
                [], [], 
                '''                The current state of an active VPDN tunnel.  Each state
                code is explained below:
                
                       unknown: The current state of the tunnel is
                                unknown.
                
                       opening: The tunnel has just been instigated and
                                is pending for a remote end reply to
                                complete the process.
                
                       open:    The tunnel is active.
                
                       closing: The tunnel has just been shut down and
                                is pending for the remote end to reply
                                to complete the process.
                ''',
                'cvpdntunnelstate',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunneltable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunneltable',
            False, 
            [
            _MetaInfoClassMember('cvpdnTunnelEntry', REFERENCE_LIST, 'Cvpdntunnelentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single active VPDN tunnel.
                ''',
                'cvpdntunnelentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrnetworkservicetypeEnum' : _MetaInfoEnum('CvpdntunnelattrnetworkservicetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'ip':'ip',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrorigcauseEnum' : _MetaInfoEnum('CvpdntunnelattrorigcauseEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'domain':'domain',
            'dnis':'dnis',
            'stack':'stack',
            'xconnect':'xconnect',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrstateEnum' : _MetaInfoEnum('CvpdntunnelattrstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'unknown':'unknown',
            'l2fOpening':'l2fOpening',
            'l2fOpenWait':'l2fOpenWait',
            'l2fOpen':'l2fOpen',
            'l2fClosing':'l2fClosing',
            'l2fCloseWait':'l2fCloseWait',
            'l2tpIdle':'l2tpIdle',
            'l2tpWaitCtlReply':'l2tpWaitCtlReply',
            'l2tpEstablished':'l2tpEstablished',
            'l2tpShuttingDown':'l2tpShuttingDown',
            'l2tpNoSessionLeft':'l2tpNoSessionLeft',
            'pptpIdle':'pptpIdle',
            'pptpWaitConnect':'pptpWaitConnect',
            'pptpWaitCtlRequest':'pptpWaitCtlRequest',
            'pptpWaitCtlReply':'pptpWaitCtlReply',
            'pptpEstablished':'pptpEstablished',
            'pptpWaitStopReply':'pptpWaitStopReply',
            'pptpTerminal':'pptpTerminal',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnSystemTunnelType', REFERENCE_ENUM_CLASS, 'TunneltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunneltypeEnum', 
                [], [], 
                '''                ''',
                'cvpdnsystemtunneltype',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelAttrTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Tunnel ID of an active VPDN tunnel.  If this end is the
                instigator of the tunnel, the ID is the TS tunnel ID,
                otherwise it is the NAS tunnel ID.
                
                Two distinct tunnels with the same tunnel ID may exist, but
                with different tunnel types.
                ''',
                'cvpdntunnelattrtunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelAttrActiveSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active session currently in the
                tunnel.
                ''',
                'cvpdntunnelattractivesessions',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrDeniedUsers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the accumulated total of denied users for the
                tunnel.
                ''',
                'cvpdntunnelattrdeniedusers',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrLocalInetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The local IP address of the tunnel.  This IP address is
                that of the interface at the local end of the tunnel.
                The type of this address is determined by the value of 
                cvpdnTunnelAttrLocalInetAddressType.
                ''',
                'cvpdntunnelattrlocalinetaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrLocalInetAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnTunnelAttrLocalInetAddress
                ''',
                'cvpdntunnelattrlocalinetaddresstype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrLocalInitConnection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the tunnel was originated
                locally or not.  If it's true, the tunnel was originated
                locally.
                ''',
                'cvpdntunnelattrlocalinitconnection',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrLocalIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local IP address of the tunnel.  This IP address is
                that of the interface at the local end of the tunnel.
                ''',
                'cvpdntunnelattrlocalipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrLocalName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The local name of an active VPDN tunnel.  It will be the
                NAS name of the tunnel if the system serves as the NAS, or
                the TS name of the tunnel if the system serves as the
                tunnel server.  Typically, the local name is the configured
                host name of the system.
                ''',
                'cvpdntunnelattrlocalname',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrNetworkServiceType', REFERENCE_ENUM_CLASS, 'CvpdntunnelattrnetworkservicetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrnetworkservicetypeEnum', 
                [], [], 
                '''                The type of network service used in the active tunnel.
                ''',
                'cvpdntunnelattrnetworkservicetype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrOrigCause', REFERENCE_ENUM_CLASS, 'CvpdntunnelattrorigcauseEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrorigcauseEnum', 
                [], [], 
                '''                The cause which originated an active VPDN tunnel.  The
                tunnel can be projected via domain name, DNIS, stack group,
                or L2 Xconnect.
                ''',
                'cvpdntunnelattrorigcause',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteEndpointName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The remote end point name of an active VPDN tunnel.  This
                name is either the domain name or the DNIS that this tunnel
                is projected with.
                ''',
                'cvpdntunnelattrremoteendpointname',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteInetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The remote IP address of the tunnel.  This IP address is
                that of the interface at the remote end of the tunnel.
                The type of this address is determined by the value of 
                cvpdnTunnelAttrRemoteInetAddressType.
                ''',
                'cvpdntunnelattrremoteinetaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteInetAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnTunnelAttrRemoteInetAddress
                ''',
                'cvpdntunnelattrremoteinetaddresstype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The remote IP address of the tunnel.  This IP address is
                that of the interface at the remote end of the tunnel.
                ''',
                'cvpdntunnelattrremoteipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The remote name of an active VPDN tunnel.  It will be the
                tunnel server name of the tunnel if the system is a NAS,
                or the NAS name of the tunnel if the system serves as the
                tunnel server.
                ''',
                'cvpdntunnelattrremotename',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrRemoteTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The remote Tunnel ID of an active VPDN tunnel.  If this end
                is the instigator of the tunnel, the ID is the NAS tunnel
                ID, otherwise it is the TS tunnel ID.
                ''',
                'cvpdntunnelattrremotetunnelid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrSoftshut', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A VPDN tunnel can be put into a soft shut state to prevent
                any new session to be added.  This object specifies whether
                this tunnel has been soft shut.  If its true, it has been
                soft shut.
                ''',
                'cvpdntunnelattrsoftshut',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrSourceInetAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The source IP address of the tunnel.  This IP address is
                the user configurable IP address for Stack Group Biding
                Protocol.  The type of this address is determined by the 
                value of cvpdnTunnelAttrSourceInetAddressType.
                ''',
                'cvpdntunnelattrsourceinetaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrSourceInetAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnTunnelAttrSourceInetAddress
                ''',
                'cvpdntunnelattrsourceinetaddresstype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrSourceIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the tunnel.  This IP address is
                the user configurable IP address for Stack Group Biding
                Protocol.
                ''',
                'cvpdntunnelattrsourceipaddress',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrState', REFERENCE_ENUM_CLASS, 'CvpdntunnelattrstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.CvpdntunnelattrstateEnum', 
                [], [], 
                '''                The current state of an active VPDN tunnel.
                Tunnels of type l2f will have states with the 'l2f' prefix.
                Tunnels of type l2tp will have states with the 'l2tp'
                prefix.
                Tunnels of type pptp will have states with the 'pptp'
                prefix.
                
                Each state code is explained below:
                
                    unknown:            The current state of the tunnel is
                                        unknown.
                
                    l2fOpening:         The tunnel has just been initiated
                                        and is pending for a remote end
                                        reply to complete the process.
                
                    l2fOpenWait:        This end received a tunnel open
                                        request from the remote end and is
                                        waiting for the tunnel to be
                                        established.
                
                    l2fOpen:            The tunnel is active.
                
                    l2fClosing:         This end received a tunnel close
                                        request.
                
                    l2fCloseWait:       The tunnel has just been shut down
                                        and is pending for the remote end
                                        to reply to complete the process.
                
                    l2tpIdle:           No tunnel is initiated yet.
                
                    l2tpWaitCtlReply:   The tunnel has been initiated and
                                        is pending for a remote end reply
                                        to complete the process.
                
                    l2tpEstablished:    The tunnel is active.
                
                    l2tpShuttingDown:   The tunnel is in progress of
                                        shutting down.
                
                    l2tpNoSessionLeft:  There is no session left in the
                                        tunnel.
                
                    pptpIdle:           No tunnel is initiated yet.
                
                    pptpWaitConnect:    The tunnel is waiting for a TCP
                                        connection.
                
                    pptpWaitCtlRequest: The tunnel has been initiated and
                                        is pending for a remote end
                                        request.
                
                    pptpWaitCtlReply:   The tunnel has been initiated and
                                        is pending for a remote end reply.
                
                    pptpEstablished:    The tunnel is active.
                
                    pptpWaitStopReply:  The tunnel is being shut down and
                                        is pending for a remote end reply.
                
                    pptpTerminal:       The tunnel has been shut down.
                ''',
                'cvpdntunnelattrstate',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelAttrEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunnelattrtable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunnelattrtable',
            False, 
            [
            _MetaInfoClassMember('cvpdnTunnelAttrEntry', REFERENCE_LIST, 'Cvpdntunnelattrentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single active VPDN tunnel.
                ''',
                'cvpdntunnelattrentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelAttrTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.CvpdntunnelsessiondevicetypeEnum' : _MetaInfoEnum('CvpdntunnelsessiondevicetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'other':'other',
            'asyncInternalModem':'asyncInternalModem',
            'async':'async',
            'bchan':'bchan',
            'sync':'sync',
            'virtualAccess':'virtualAccess',
            'xdsl':'xdsl',
            'cable':'cable',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.CvpdntunnelsessionstateEnum' : _MetaInfoEnum('CvpdntunnelsessionstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'unknown':'unknown',
            'opening':'opening',
            'open':'open',
            'closing':'closing',
            'waitingForTunnel':'waitingForTunnel',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnTunnelTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cvpdntunneltunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The ID of an active VPDN tunnel user session.
                ''',
                'cvpdntunnelsessionid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelSessionBytesIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input bytes through this active
                user session.
                ''',
                'cvpdntunnelsessionbytesin',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionBytesOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of output bytes through this active
                user session.
                ''',
                'cvpdntunnelsessionbytesout',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionCallDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the call duration of the current
                active user session in value of system uptime.
                ''',
                'cvpdntunnelsessioncallduration',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDeviceCallerId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The incoming caller identification of the user.  It is
                the originating number that called into the device that
                initiates the user session.  This object can be empty
                since not all dial device can provide caller ID
                information.
                ''',
                'cvpdntunnelsessiondevicecallerid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDevicePhyId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The device ID of the physical interface for the user
                session.  The object is the the interface index which
                points to the ifTable.  For virtual interface that is
                not in the ifTable, it will have zero value.
                ''',
                'cvpdntunnelsessiondevicephyid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDeviceType', REFERENCE_ENUM_CLASS, 'CvpdntunnelsessiondevicetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.CvpdntunnelsessiondevicetypeEnum', 
                [], [], 
                '''                The type of physical devices that this user session
                is attached to for the local end of the tunnel.  The
                meaning of each device type is explained below:
                
                    other:              Any device that has not been
                                        defined.
                
                    asyncInternalModem: Modem Pool device of an access
                                        server.
                
                    async:              A regular asynchronous serial
                                        interface.
                
                    sync:               A regular synchronous serial
                                        interface.
                
                    bchan:              An ISDN call.
                
                    xdsl:               Future application with xDSL
                                        devices.
                
                    cable:              Future application with Cable
                                        modem devices.
                ''',
                'cvpdntunnelsessiondevicetype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDS1ChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database channel index if it is associated with
                this user session.  Only a session over a device of
                type asyncInternalModem will have a valid value for
                this object.
                ''',
                'cvpdntunnelsessionds1channelindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDS1PortIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database port index if it is associated with
                this user session.  Only a session with a device of
                type asyncInternalModem will have a a valid value for
                this object.
                ''',
                'cvpdntunnelsessionds1portindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionDS1SlotIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database slot index if it is associated with
                this user session.  Only a session with a device of
                type asyncInternalModem will have a valid value for
                this object.
                ''',
                'cvpdntunnelsessionds1slotindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionModemCallStartIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Arbitrary small integer to distinguish modem calls that
                occurred at the same time tick.  Only session over
                device asyncInternalModem will have a valid value for
                this object.
                ''',
                'cvpdntunnelsessionmodemcallstartindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionModemCallStartTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The start time of the current modem call.  Only a
                session with a  device of type asyncInternalModem will
                have a valid value for this object.
                ''',
                'cvpdntunnelsessionmodemcallstarttime',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionModemPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Modem Pool database port index if it is associated
                with this user session.  Only a session with a device
                of type asyncInternalModem will have a valid value for
                this object.
                ''',
                'cvpdntunnelsessionmodemportindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionModemSlotIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Modem Pool database slot index if it is associated
                with this user session.  Only a session with device of
                type asyncInternalModem will have a valid value for
                this object.
                ''',
                'cvpdntunnelsessionmodemslotindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionMultilink', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the session is part of a
                multilink or not.
                ''',
                'cvpdntunnelsessionmultilink',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionPacketsIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input packets through this active
                user session.
                ''',
                'cvpdntunnelsessionpacketsin',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionPacketsOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of output packets through this active
                user session.
                ''',
                'cvpdntunnelsessionpacketsout',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionState', REFERENCE_ENUM_CLASS, 'CvpdntunnelsessionstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.CvpdntunnelsessionstateEnum', 
                [], [], 
                '''                The current state of an active user session.  Each state
                code is explained below:
                
                    unknown:          The current state of the tunnel's
                                      session is unknown.
                
                    opening:          The user session has just been
                                      initiated through a tunnel and is
                                      pending for the remote end reply
                                      to complete the process.
                
                    open:             The user session is active.
                
                    closing:          The user session has just been
                                      closed and is pending for the
                                      remote end reply to complete the
                                      process.
                
                    waitingForTunnel: The user session is in this state
                                      when the tunnel which this session
                                      is going through is still in
                                      CLOSED state.  It waits for the
                                      tunnel to become OPEN before the
                                      session is allow to be fully
                                      established.
                ''',
                'cvpdntunnelsessionstate',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionUserName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The name of the user of the user session.
                ''',
                'cvpdntunnelsessionusername',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelSessionEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntunnelsessiontable',
            False, 
            [
            _MetaInfoClassMember('cvpdnTunnelSessionEntry', REFERENCE_LIST, 'Cvpdntunnelsessionentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single user session within the tunnel.
                ''',
                'cvpdntunnelsessionentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTunnelSessionTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.CvpdnsessionattrdevicetypeEnum' : _MetaInfoEnum('CvpdnsessionattrdevicetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'other':'other',
            'asyncInternalModem':'asyncInternalModem',
            'async':'async',
            'bchan':'bchan',
            'sync':'sync',
            'virtualAccess':'virtualAccess',
            'xdsl':'xdsl',
            'cable':'cable',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.CvpdnsessionattrstateEnum' : _MetaInfoEnum('CvpdnsessionattrstateEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'unknown':'unknown',
            'l2fOpening':'l2fOpening',
            'l2fOpen':'l2fOpen',
            'l2fCloseWait':'l2fCloseWait',
            'l2fWaitingForTunnel':'l2fWaitingForTunnel',
            'l2tpIdle':'l2tpIdle',
            'l2tpWaitingTunnel':'l2tpWaitingTunnel',
            'l2tpWaitReply':'l2tpWaitReply',
            'l2tpWaitConnect':'l2tpWaitConnect',
            'l2tpEstablished':'l2tpEstablished',
            'l2tpShuttingDown':'l2tpShuttingDown',
            'pptpWaitVAccess':'pptpWaitVAccess',
            'pptpPacEstablished':'pptpPacEstablished',
            'pptpWaitTunnel':'pptpWaitTunnel',
            'pptpWaitOCRP':'pptpWaitOCRP',
            'pptpPnsEstablished':'pptpPnsEstablished',
            'pptpWaitCallDisc':'pptpWaitCallDisc',
            'pptpTerminal':'pptpTerminal',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnSystemTunnelType', REFERENCE_ENUM_CLASS, 'TunneltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunneltypeEnum', 
                [], [], 
                '''                ''',
                'cvpdnsystemtunneltype',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTunnelAttrTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'cvpdntunnelattrtunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnSessionAttrSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The ID of an active VPDN session.
                ''',
                'cvpdnsessionattrsessionid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnSessionAttrBytesIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input bytes through this active
                session.
                ''',
                'cvpdnsessionattrbytesin',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrBytesOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of output bytes through this active
                session.
                ''',
                'cvpdnsessionattrbytesout',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrCallDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the call duration of the current
                active session.
                ''',
                'cvpdnsessionattrcallduration',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDeviceCallerId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The incoming caller identification of the user.  It is the
                originating number that called into the device that
                initiates the session.  This object can be empty since not
                all dial devices can provide caller ID information.
                ''',
                'cvpdnsessionattrdevicecallerid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDevicePhyId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The device ID of the physical interface for the session.
                The object is the the interface index which points to the
                ifTable.  For virtual interfaces that are not in the
                ifTable, the value will be zero.
                ''',
                'cvpdnsessionattrdevicephyid',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDeviceType', REFERENCE_ENUM_CLASS, 'CvpdnsessionattrdevicetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.CvpdnsessionattrdevicetypeEnum', 
                [], [], 
                '''                The type of physical devices that this session is attached
                to for the local end of the tunnel.  The meaning of each
                device type is explained below:
                
                    other:              Any device that has not been
                                        defined.
                
                    asyncInternalModem: Modem Pool device of an access
                                        server.
                
                    async:              A regular asynchronous serial
                                        interface.
                
                    sync:               A regular synchronous serial
                                        interface.
                
                    bchan:              An ISDN call.
                
                    xdsl:               xDSL interface.
                
                    cable:              cable modem interface.
                ''',
                'cvpdnsessionattrdevicetype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDS1ChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database channel index if it is associated with
                this session.  Only a session over a device of type
                'asyncInternalModem' will have a valid value for this
                object; otherwise it is not instantiated.
                ''',
                'cvpdnsessionattrds1channelindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDS1PortIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database port index if it is associated with this
                session.  Only a session with a device of type
                'asyncInternalModem' will have a valid value for this
                object; otherwise it is not instantiated.
                ''',
                'cvpdnsessionattrds1portindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrDS1SlotIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The DS1 database slot index if it is associated with this
                session.  Only a session with a device of type
                'asyncInternalModem' will have a valid value for this
                object; otherwise it is not instantiated.
                ''',
                'cvpdnsessionattrds1slotindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrModemCallStartIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Arbitrary small integer to distinguish modem calls that
                occurred at the same time tick.  Only session over device
                'asyncInternalModem' will have a valid value for this
                object; otherwise, it is not instantiated.
                ''',
                'cvpdnsessionattrmodemcallstartindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrModemCallStartTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The start time of the current modem call.  Only a session
                with a device of type 'asyncInternalModem' will have a
                valid value for this object; otherwise, it is not
                instantiated.
                ''',
                'cvpdnsessionattrmodemcallstarttime',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrModemPortIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Modem Pool database port index if it is associated with
                this session.  Only a session with a device of type
                'asyncInternalModem' will have a valid value for this
                object; otherwise, it is not instantiated.
                ''',
                'cvpdnsessionattrmodemportindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrModemSlotIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Modem Pool database slot index if it is associated with
                this session.  Only a session with device of type
                'asyncInternalModem' will have a valid value for this
                object; otherwise, it is not instantiated.
                ''',
                'cvpdnsessionattrmodemslotindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrMultilink', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the session is part of a
                multilink PPP bundle, even if there is only one link or
                session in the bundle.  If it is multilink PPP, the value
                is true.
                ''',
                'cvpdnsessionattrmultilink',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrMultilinkBundle', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the name of the multilink bundle to
                which this session belongs.  The value of this object is
                only valid when the value of cvpdnSessionAttrMultilink is
                'true'.  If the value of cvpdnSessionAttrMultilink is
                'false', then the value of this object will be the empty
                string.
                ''',
                'cvpdnsessionattrmultilinkbundle',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrMultilinkIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object specifies the ifIndex of the multilink bundle
                to which this session belongs.  The value of this object is
                only valid when the value of cvpdnSessionAttrMultilink is
                'true'.  If the value of cvpdnSessionAttrMultilink is
                'false', then the value of this object will be zero.
                ''',
                'cvpdnsessionattrmultilinkifindex',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrPacketsIn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of input packets through this active
                session.
                ''',
                'cvpdnsessionattrpacketsin',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrPacketsOut', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of output packets through this active
                session.
                ''',
                'cvpdnsessionattrpacketsout',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrRecvPktsDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of dropped packets that were received from
                this active session.
                ''',
                'cvpdnsessionattrrecvpktsdropped',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrSentPktsDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of dropped packets that could not be sent
                into this active session.
                ''',
                'cvpdnsessionattrsentpktsdropped',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrState', REFERENCE_ENUM_CLASS, 'CvpdnsessionattrstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.CvpdnsessionattrstateEnum', 
                [], [], 
                '''                The current state of a tunnel session.
                L2F tunnel sessions will have states with the 'l2f' prefix.
                L2TP tunnel sessions will have states with the 'l2tp'
                prefix.
                
                Each state code is explained below:
                
                    unknown:             The current state of the tunnel's
                                         session is unknown.
                
                    l2fOpening:          The session has just been
                                         initiated through a tunnel and is
                                         pending for the remote end reply
                                         to complete the process.
                
                    l2fOpen:             The session is active.
                
                    l2fCloseWait:        The session has just been closed
                                         and is pending for the remote end
                                         reply to complete the process.
                
                    l2fWaitingForTunnel: The session is in this state when
                                         the tunnel which this session is
                                         going through is still in CLOSED
                                         state.  It waits for the tunnel to
                                         become OPEN before the session is
                                         allowed to be fully established.
                
                    l2tpIdle:            No session is initiated yet.
                
                    l2tpWaitingTunnel:   The session is waiting for the
                                         tunnel to be established.
                
                    l2tpWaitReply:       The session has been initiated and
                                         is pending for the remote end
                                         reply to complete the process.
                
                    l2tpWaitConnect:     This end has acknowledged a
                                         connection request and is waiting
                                         for the remote end to connect.
                
                    l2tpEstablished:     The session is active.
                
                    l2tpShuttingDown:    The session is in progress of
                                         shutting down.
                
                    pptpWaitVAccess:     The session is waiting for the
                                         creation of a virtual access
                                         interface.
                
                    pptpPacEstablished:  The session is active.
                
                    pptpWaitTunnel:      The session is waiting for the
                                         tunnel to be established.
                
                    pptpWaitOCRP:        The session has been initiated and
                                         is pending for the remote end
                                         reply to complete the process.
                
                    pptpPnsEstablished:  The session is active.
                
                    pptpWaitCallDisc:    Session shutdown is in progress.
                ''',
                'cvpdnsessionattrstate',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrUserName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The name of the user of the session.
                ''',
                'cvpdnsessionattrusername',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrVirtualCircuitID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The virtual circuit ID of an active Layer 2 VPN session.
                ''',
                'cvpdnsessionattrvirtualcircuitid',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnSessionAttrEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnsessionattrtable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnsessionattrtable',
            False, 
            [
            _MetaInfoClassMember('cvpdnSessionAttrEntry', REFERENCE_LIST, 'Cvpdnsessionattrentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single session within the tunnel.
                ''',
                'cvpdnsessionattrentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnSessionAttrTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnUnameToFailHistUname', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The user name for this failure entry.
                ''',
                'cvpdnunametofailhistuname',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnUnameToFailHistTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Tunnel ID for this failure entry.  If it is the
                instigator of the tunnel, the ID is the TS tunnel ID,
                otherwise it is the NAS tunnel ID.
                ''',
                'cvpdnunametofailhisttunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnUnameToFailHistCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object is incremented when multiple failures has
                been experienced by this user on this tunnel.  Seeing a
                delta of >1 is an indication that the current failure
                record is the latest of a series of failures that has
                been recorded.
                ''',
                'cvpdnunametofailhistcount',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistDestInetAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The destination IP address of the tunnel in which the
                failure occurred.  This IP address is that of the
                interface at the receiver end of the tunnel.  The type 
                of this address is determined by the value of 
                cvpdnUnameToFailHistDestInetType.
                ''',
                'cvpdnunametofailhistdestinetaddr',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistDestInetType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnUnameToFailHistDestInetAddr.
                ''',
                'cvpdnunametofailhistdestinettype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistDestIp', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the tunnel in which the
                failure occurred.  This IP address is that of the
                interface at the receiver end of the tunnel.
                ''',
                'cvpdnunametofailhistdestip',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistFailReason', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The reason of failure for the current failure record.
                ''',
                'cvpdnunametofailhistfailreason',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistFailTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the time when the failure is
                occurred.
                ''',
                'cvpdnunametofailhistfailtime',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistFailType', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The type of failure for the current failure record.  It
                comes in a form of a an ASCII string which describes
                the type of failure.
                ''',
                'cvpdnunametofailhistfailtype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistLocalInitConn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the tunnel in which the
                failure occurred was generated locally or not.
                ''',
                'cvpdnunametofailhistlocalinitconn',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistLocalName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The local name of the VPDN tunnel in which the failure
                occurred.  It will be the NAS name of the tunnel if the
                system serves as the NAS, or the TS name of the tunnel
                if the system serves as the tunnel server.  The local
                name is the configured host name of the system.  This
                object can be empty if the failure occurred prior to
                successful tunnel projection, thus no source name will
                be available.
                ''',
                'cvpdnunametofailhistlocalname',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistRemoteName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The remote name of the VPDN tunnel in which the failure
                occurred.  It will be the tunnel server name of the
                tunnel if the system is a NAS, or the NAS name of the
                tunnel if the system serves as the tunnel server.  This
                object can be empty if the failure occurred prior to
                successful tunnel projection, thus no source name will
                be available.
                ''',
                'cvpdnunametofailhistremotename',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistSourceInetAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The source IP address of the tunnel in which the
                failure occurred.  This IP address is that of the
                interface at the instigator end of the tunnel.  The
                instigator end is the peer which initiates the tunnel
                estalishment.  The type of this address is determined
                by the value of cvpdnUnameToFailHistSourceInetType.
                ''',
                'cvpdnunametofailhistsourceinetaddr',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistSourceInetType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnUnameToFailHistSourceInetAddr.
                ''',
                'cvpdnunametofailhistsourceinettype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistSourceIp', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the tunnel in which the
                failure occurred.  This IP address is that of the
                interface at the instigator end of the tunnel.
                ''',
                'cvpdnunametofailhistsourceip',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUnameToFailHistUserId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The user ID of this failure entry.
                ''',
                'cvpdnunametofailhistuserid',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnUserToFailHistInfoEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable',
            False, 
            [
            _MetaInfoClassMember('cvpdnUserToFailHistInfoEntry', REFERENCE_LIST, 'Cvpdnusertofailhistinfoentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry', 
                [], [], 
                '''                An entry in the table, containing failure history
                relevant to an user name.
                ''',
                'cvpdnusertofailhistinfoentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnUserToFailHistInfoTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnTemplateName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The name of the VPDN template.
                ''',
                'cvpdntemplatename',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnTemplateActiveSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active session in all groups
                associated with the template.
                ''',
                'cvpdntemplateactivesessions',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTemplateEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdntemplatetable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdntemplatetable',
            False, 
            [
            _MetaInfoClassMember('cvpdnTemplateEntry', REFERENCE_LIST, 'Cvpdntemplateentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry', 
                [], [], 
                '''                An entry in the table, containing information about a
                single VPDN template.
                ''',
                'cvpdntemplateentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnTemplateTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry.CvpdnbundleendpointtypeEnum' : _MetaInfoEnum('CvpdnbundleendpointtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB',
        {
            'none':'none',
            'hostname':'hostname',
            'string':'string',
            'macAddress':'macAddress',
            'ipV4Address':'ipV4Address',
            'ipV6Address':'ipV6Address',
            'phone':'phone',
            'magicNumber':'magicNumber',
        }, 'CISCO-VPDN-MGMT-MIB', _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB']),
    'CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnBundleName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                The name of the multilink PPP bundle associated with a VPDN
                tunnel.
                ''',
                'cvpdnbundlename',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnBundleEndpoint', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Indicates the discriminator used in this bundle that is
                associated with a VPDN tunnel.
                ''',
                'cvpdnbundleendpoint',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundleEndpointClass', REFERENCE_ENUM_CLASS, 'EndpointclassEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'EndpointclassEnum', 
                [], [], 
                '''                The multilink PPP bundle discriminator class associated
                with a VPDN tunnel.  The value of this object represents the
                type of discriminator used in cvpdnBundleEndpoint.
                ''',
                'cvpdnbundleendpointclass',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundleEndpointType', REFERENCE_ENUM_CLASS, 'CvpdnbundleendpointtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry.CvpdnbundleendpointtypeEnum', 
                [], [], 
                '''                The multilink PPP bundle discriminator type associated with
                a VPDN tunnel.  The value of this object represents the type
                of discriminator used in cvpdnBundleEndpoint.
                
                    none:        No endpoint discriminator was supplied, the
                                 default value is being used.
                
                    hostname:    The router's hostname is being used as
                                 discriminator.
                
                    string:      User specified string is being used as
                                 discriminator.
                
                    macAddress:  A MAC address as defined by the MacAddress
                                 textual convention is being used as
                                 discriminator.
                
                    ipV4Address: An IP address as defined by the
                                 InetAddressIPv4 textual convention is being
                                 used as discriminator.
                
                    ipV6Address: An IP address as defined by the
                                 InetAddressIPv6 textual convention is being
                                 used as discriminator.
                
                    phone:       The PSTN phone number is being used as
                                 discriminator.
                
                    magicNumber: A magic number is being used as
                                 discriminator.
                ''',
                'cvpdnbundleendpointtype',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundleLinkCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of active links in a multilink PPP bundle
                associated with a VPDN tunnel.
                ''',
                'cvpdnbundlelinkcount',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundlePeerIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the multilink PPP peer in a VPDN tunnel.
                ''',
                'cvpdnbundlepeeripaddr',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundlePeerIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Indicates the type of address contained in
                cvpdnBundlePeerIpAddr.
                ''',
                'cvpdnbundlepeeripaddrtype',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnBundleEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnbundletable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnbundletable',
            False, 
            [
            _MetaInfoClassMember('cvpdnBundleEntry', REFERENCE_LIST, 'Cvpdnbundleentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry', 
                [], [], 
                '''                An entry in this table represents an active multilink PPP
                bundle that belongs to a VPDN tunnel.
                ''',
                'cvpdnbundleentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnBundleTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry',
            False, 
            [
            _MetaInfoClassMember('cvpdnBundleName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                ''',
                'cvpdnbundlename',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnBundleChildTunnelType', REFERENCE_ENUM_CLASS, 'TunneltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunneltypeEnum', 
                [], [], 
                '''                The tunnel type.  This is the tunnel protocol of an active
                VPDN session that is associated with a multilink PPP
                bundle.
                ''',
                'cvpdnbundlechildtunneltype',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnBundleChildTunnelId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Tunnel ID of an active VPDN session that is associated
                with a multilink PPP bundle.
                ''',
                'cvpdnbundlechildtunnelid',
                'CISCO-VPDN-MGMT-MIB', True),
            _MetaInfoClassMember('cvpdnBundleChildSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The ID of an active VPDN session that is associated with a
                multilink PPP bundle.
                ''',
                'cvpdnbundlechildsessionid',
                'CISCO-VPDN-MGMT-MIB', True),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnBundleChildEntry',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib.Cvpdnbundlechildtable' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib.Cvpdnbundlechildtable',
            False, 
            [
            _MetaInfoClassMember('cvpdnBundleChildEntry', REFERENCE_LIST, 'Cvpdnbundlechildentry' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry', 
                [], [], 
                '''                An entry in this table represents a session that belongs to
                a VPDN tunnel and to a multilink PPP bundle.
                ''',
                'cvpdnbundlechildentry',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'cvpdnBundleChildTable',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
    'CiscoVpdnMgmtMib' : {
        'meta_info' : _MetaInfoClass('CiscoVpdnMgmtMib',
            False, 
            [
            _MetaInfoClassMember('ciscoVpdnMgmtMIBNotifs', REFERENCE_CLASS, 'Ciscovpdnmgmtmibnotifs' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs', 
                [], [], 
                '''                ''',
                'ciscovpdnmgmtmibnotifs',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundleChildTable', REFERENCE_CLASS, 'Cvpdnbundlechildtable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnbundlechildtable', 
                [], [], 
                '''                A table that exposes the containment relationship between a
                multilink PPP bundle and a VPDN tunnel.
                ''',
                'cvpdnbundlechildtable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnBundleTable', REFERENCE_CLASS, 'Cvpdnbundletable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnbundletable', 
                [], [], 
                '''                Table that describes the multilink PPP attributes of the
                active VPDN sessions.
                ''',
                'cvpdnbundletable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnMultilinkInfo', REFERENCE_CLASS, 'Cvpdnmultilinkinfo' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnmultilinkinfo', 
                [], [], 
                '''                ''',
                'cvpdnmultilinkinfo',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSessionAttrTable', REFERENCE_CLASS, 'Cvpdnsessionattrtable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsessionattrtable', 
                [], [], 
                '''                Table of information about individual sessions within the
                active tunnels.  An entry is added to the table when a new
                session is initiated and removed from the table when the
                session is terminated.
                ''',
                'cvpdnsessionattrtable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemInfo', REFERENCE_CLASS, 'Cvpdnsysteminfo' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsysteminfo', 
                [], [], 
                '''                ''',
                'cvpdnsysteminfo',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnSystemTable', REFERENCE_CLASS, 'Cvpdnsystemtable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnsystemtable', 
                [], [], 
                '''                Table of information about the VPDN system for all tunnel
                types.
                ''',
                'cvpdnsystemtable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTemplateTable', REFERENCE_CLASS, 'Cvpdntemplatetable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntemplatetable', 
                [], [], 
                '''                Table of information about the VPDN templates.  The
                VPDN template is a grouping mechanism that allows
                configuration settings to be shared among multiple VPDN
                groups.  One such setting is a limit on the number of
                active sessions across all VPDN groups associated with
                the template.  The template table allows customers to
                monitor template-wide information such as tracking the
                allocation of sessions across templates.
                ''',
                'cvpdntemplatetable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelAttrTable', REFERENCE_CLASS, 'Cvpdntunnelattrtable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelattrtable', 
                [], [], 
                '''                Table of information about the active VPDN tunnels.  An
                entry is added to the table when a new tunnel is initiated
                and removed from the table when the tunnel is terminated.
                ''',
                'cvpdntunnelattrtable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelSessionTable', REFERENCE_CLASS, 'Cvpdntunnelsessiontable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunnelsessiontable', 
                [], [], 
                '''                Table of information about individual user sessions
                within the active tunnels.  Entry is added to the table
                when new user session is initiated and be removed from
                the table when the user session is terminated.
                ''',
                'cvpdntunnelsessiontable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnTunnelTable', REFERENCE_CLASS, 'Cvpdntunneltable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdntunneltable', 
                [], [], 
                '''                Table of information about the active VPDN tunnels.
                ''',
                'cvpdntunneltable',
                'CISCO-VPDN-MGMT-MIB', False),
            _MetaInfoClassMember('cvpdnUserToFailHistInfoTable', REFERENCE_CLASS, 'Cvpdnusertofailhistinfotable' , 'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable', 
                [], [], 
                '''                Table of the record of failure objects which can be
                referenced by an user name.  Only a name that has a
                valid item in the Cisco IOS VPDN failure history table
                will yield a valid entry in this table.  The table has
                a maximum size of 50 entries.  Only the newest 50
                entries will be kept in the table.
                ''',
                'cvpdnusertofailhistinfotable',
                'CISCO-VPDN-MGMT-MIB', False),
            ],
            'CISCO-VPDN-MGMT-MIB',
            'CISCO-VPDN-MGMT-MIB',
            _yang_ns._namespaces['CISCO-VPDN-MGMT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB'
        ),
    },
}
_meta_table['CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdnsystemtable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdntunneltable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelattrtable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelsessiontable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdnsessionattrtable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdntemplatetable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdnbundletable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib.Cvpdnbundlechildtable']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnsysteminfo']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnmultilinkinfo']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnsystemtable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunneltable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelattrtable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntunnelsessiontable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnsessionattrtable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdntemplatetable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnbundletable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']
_meta_table['CiscoVpdnMgmtMib.Cvpdnbundlechildtable']['meta_info'].parent =_meta_table['CiscoVpdnMgmtMib']['meta_info']

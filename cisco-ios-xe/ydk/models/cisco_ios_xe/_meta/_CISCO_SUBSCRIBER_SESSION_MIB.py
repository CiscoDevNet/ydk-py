


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoSubscriberSessionMib.Csubjob' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjob',
            False, 
            [
            _MetaInfoClassMember('csubJobCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of subscriber session jobs
                currently maintained by the csubJobTable.
                ''',
                'csubjobcount',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobFinishedNotifyEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system generates a
                csubJobFinishedNotify notification when the system finishes
                processing a subscriber session job.
                ''',
                'csubjobfinishednotifyenable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobIdNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the next available identifier for the
                creation of a new row in the csubJobTable.  If no available
                identifier exists, then this object has the value '0'.
                ''',
                'csubjobidnext',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobIndexedAttributes', REFERENCE_BITS, 'Subsessionidentities' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'Subsessionidentities', 
                [], [], 
                '''                This object indicates which subscriber session identities the
                system maintains as searchable keys.  This value serves the
                EMS/NMS in configuring a subscriber session query, as at least
                one match criteria must be an 'indexed attribute'.
                ''',
                'csubjobindexedattributes',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMaxLife', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the maximum life a subscriber session
                report corresponding to a subscriber session job having a
                csubJobType of 'query'.  The system tracks the time elapsed
                after it finishes processing a query.  When the time elapsed
                reaches the value specified by this column, the system
                automatically  destroys the report.  A value of '0' disables the
                automatic destruction of reports.
                ''',
                'csubjobmaxlife',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMaxNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the maximum number of outstanding
                subscriber session jobs the system can support.  If the
                csubJobTable contains a number of rows (i.e., the value of
                csubJobCount) equal to this value, then any attempt to create a
                new row will result in a response with an error-status of
                'resourceUnavailable'.
                ''',
                'csubjobmaxnumber',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJob',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggthresh' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggthresh',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsThreshNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object enables or disables the generation of any of the
                csubAggStats* threshold notifications.
                ''',
                'csubaggstatsthreshnotifenable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggThresh',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry.CsubsessionipaddrassignmentEnum' : _MetaInfoEnum('CsubsessionipaddrassignmentEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'none':'none',
            'other':'other',
            'static':'static',
            'localPool':'localPool',
            'dhcpv4':'dhcpv4',
            'dhcpv6':'dhcpv6',
            'userProfileIpAddr':'userProfileIpAddr',
            'userProfileIpSubnet':'userProfileIpSubnet',
            'userProfileNamedPool':'userProfileNamedPool',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubSessionAcctSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the accounting session identifier
                assigned to the subscriber session.
                
                This column is valid only if the 'accountingSid' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionacctsessionid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionAuthenticated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the system has successfully
                authenticated the subscriber session.
                
                    'false'
                        The subscriber session is operationally up, but in the
                        UNAUTHENTICATED state.
                
                    'true'
                        The subscriber session is operationally up, but in the
                        AUTHENTICATED state.
                ''',
                'csubsessionauthenticated',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionAvailableIdentities', REFERENCE_BITS, 'Subsessionidentities' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'Subsessionidentities', 
                [], [], 
                '''                This object indicates the subscriber identities that the system
                has successfully collected for the subscriber session.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is invalid.  If the bit is '1', then the value of the
                corresponding column represents the value of the subscriber
                identity collected by the system.
                
                The following list specifies the mappings between the bits and
                the columns:
                
                    'subscriberLabel' => csubSessionSubscriberLabel
                    'macAddress'      => csubSessionMacAddress
                    'nativeVrf'       => csubSessionNativeVrf
                    'nativeIpAddress' => csubSessionNativeIpAddrType,
                                         csubSessionNativeIpAddr,
                                         csubSessionNativeIpMask
                    'nativeIpAddress2'=> csubSessionNativeIpAddrType2,
                                         csubSessionNativeIpAddr2,
                                         csubSessionNativeIpMask2                                 
                    'domainVrf'       => csubSessionDomainVrf
                    'domainIpAddress' => csubSessionDomainIpAddrType,
                                         csubSessionDomainIpAddr,
                                         csubSessionDomainIpMask
                    'pbhk'            => csubSessionPbhk
                    'remoteId'        => csubSessionRemoteId
                    'circuitId'       => csubSessionCircuitId
                    'nasPort'         => csubSessionNasPort
                    'domain'          => csubSessionDomain
                    'username'        => csubSessionUsername
                    'acctSessionId'   => csubSessionAcctSessionId
                    'dnis'            => csubSessionDnis
                    'media'           => csubSessionMedia
                    'mlpNegotiated'   => csubSessionMlpNegotiated
                    'protocol'        => csubSessionProtocol
                    'dhcpClass'       => csubSessionDhcpClass
                    'tunnelName'      => csubSessionTunnelName
                
                Observe that the bit 'ifIndex' should always be '1'.  This
                identity maps to the ifIndex assigned to the subscriber
                session.
                
                Observe that the bit 'serviceName' maps to one or more instance
                of ccbptPolicyMap (defined by the CISCO-CBP-TARGET-MIB).
                ''',
                'csubsessionavailableidentities',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionCircuitId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the Circuit-Id identifying the circuit
                supported by the 'calling station' or AN providing access to
                the subscriber.
                
                This column is valid only if the 'circuitId' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessioncircuitid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionCreationTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates when the subscriber session was created
                (i.e., when the subscriber session was initiated).
                ''',
                'csubsessioncreationtime',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDerivedCfg', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object indicates the row in the cdtTemplateTable (defined
                by the CISCO-DYNAMIC-TEMPLATE-MIB) describing the derived
                configuration for the subscriber session.
                
                Observe that the value of cdtTemplateType corresponding to the
                referenced row must be 'derived'.
                ''',
                'csubsessionderivedcfg',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDhcpClass', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the name of the class matching the DHCP
                DISCOVER message received from the subscriber.
                
                This column is valid only if the 'dhcpClass' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondhcpclass',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDnis', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the DNIS number dialed by the
                subscriber to access the 'calling station' or AN.
                
                This column is valid only if the 'dnis' bit of the corresponding
                instance of csubSessionAvailableIdentities is '1'.
                ''',
                'csubsessiondnis',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDomain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the domain associated with the
                subscriber.
                
                This column is valid only if the 'domain' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondomain',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDomainIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the IP address assigned to the
                subscriber on the service-facing side of the system.
                
                This column is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondomainipaddr',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDomainIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object indicates the type of IP address assigned to the
                subscriber on the service-facing side of the system.
                
                This column is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondomainipaddrtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDomainIpMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the corresponding mask for the IP
                address assigned to the subscriber on the service-facing side of
                the system.
                
                This column is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondomainipmask',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionDomainVrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the VRF to which the system transfers
                the subscriber session's traffic.
                
                This column is valid only if the 'domainVrf' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiondomainvrf',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionIpAddrAssignment', REFERENCE_ENUM_CLASS, 'CsubsessionipaddrassignmentEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry.CsubsessionipaddrassignmentEnum', 
                [], [], 
                '''                This object indicates how the system assigns IP addresses to
                the subscriber:
                
                    'none'
                        The system does not an involvement in (or is it aware
                        of) the assignment an subscriber IP addresses.  For
                        example, a system does not have an involvement in the
                        assignment of subscriber IP addresses for IP interface
                        subscriber sessions.
                
                    'other'
                        The system assigns subscriber IP addresses using a
                        method not recognized by this MIB module.
                
                    'static'
                        Subscriber IP addresses have been configured correctly
                        for the service domain.  The system does not have an
                        involvement in the assignment of the IP address.
                
                    'localPool'
                        The system assigns subscriber IP addresses from a
                        locally configured pool of IP addresses.
                
                    'dhcpv4'
                        The system assigns subscriber IP addresses are using the
                        DHCPv4.
                
                    'dhcpv6'
                        The system assigns subscriber IP addresses using the
                        DHCPv6.
                
                    'userProfileIpAddr'
                        The system assigns subscriber IP addresses from a user
                        profile.
                
                    'userProfileIpSubnet'
                        The system assigns the subscriber an IP subnet from a
                        user profile.
                
                    'userProfileNamedPool'
                        The system assigns subscriber IP addresses from a
                        locally configured named pool specified by a user
                        profile.
                ''',
                'csubsessionipaddrassignment',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionLastChanged', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates when the subscriber session is updated
                with new policy information.
                ''',
                'csubsessionlastchanged',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionLocationIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the location of the
                subscriber
                ''',
                'csubsessionlocationidentifier',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                This object indicates the MAC address of the subscriber.
                
                This column is valid only if the 'macAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionmacaddress',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionMedia', REFERENCE_ENUM_CLASS, 'SubscribermediatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscribermediatypeEnum', 
                [], [], 
                '''                This object indicates the type of media providing access to
                the subscriber.
                
                This column is valid only if the 'media' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionmedia',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionMlpNegotiated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the subscriber session was
                established using multi-link PPP negotiation.
                
                This column is valid only if the 'mlpNegotiated' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionmlpnegotiated',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNasPort', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the NAS port-identifier identifying the
                port on the NAS providing access to the subscriber.
                
                This column is valid only if the 'nasPort' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnasport',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the IP address assigned to the
                subscriber on the customer-facing side of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativeipaddr',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpAddr2', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the IP address assigned to the
                subscriber on the customer-facing side of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativeipaddr2',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object indicates the type of IP address assigned to the
                subscriber on the customer-facing side of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativeipaddrtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpAddrType2', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object indicates the type of IP address assigned to the
                subscriber on the customer-facing side of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                
                In Dual stack scenarios both 'csubSessionNativeIpAddrType' and 
                'csubSessionNativeIpAddrType2' will be valid
                ''',
                'csubsessionnativeipaddrtype2',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the corresponding mask for the IP
                address assigned to the subscriber on the customer-facing side
                of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativeipmask',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeIpMask2', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object indicates the corresponding mask for the IP
                address assigned to the subscriber on the customer-facing side
                of the system.
                
                This column is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativeipmask2',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionNativeVrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the VRF originating the subscriber
                session.
                
                This column is valid only if the 'nativeVrf' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionnativevrf',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionPbhk', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the PBHK identifying the subscriber.
                
                This column is valid only if the 'pbhk' bit of the corresponding
                instance of csubSessionAvailableIdentities is '1'.
                ''',
                'csubsessionpbhk',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionProtocol', REFERENCE_ENUM_CLASS, 'SubscriberprotocoltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberprotocoltypeEnum', 
                [], [], 
                '''                This object indicates the type of protocol providing access to
                the subscriber.
                
                This column is valid only if the 'protocol' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionprotocol',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionRedundancyMode', REFERENCE_ENUM_CLASS, 'SubsessionredundancymodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessionredundancymodeEnum', 
                [], [], 
                '''                This object indicates the redundancy mode in which the
                subscriber session is operating.
                ''',
                'csubsessionredundancymode',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionRemoteId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the Remote-Id identifying the 'calling
                station' or AN supporting the circuit that provides access to
                the subscriber.
                
                This column is valid only if the 'remoteId' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionremoteid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionServiceIdentifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the name used to identify the services
                subscribed by a particular session.
                ''',
                'csubsessionserviceidentifier',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionState', REFERENCE_ENUM_CLASS, 'SubsessionstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessionstateEnum', 
                [], [], 
                '''                This object indicates the operational state of the subscriber
                session.
                ''',
                'csubsessionstate',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionSubscriberLabel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates a positive integer-value uniquely
                identifying the subscriber session within the scope of
                the system.
                
                This column is valid only if the 'subscriberLabel' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionsubscriberlabel',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionTunnelName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the name of the VPDN used to carry the
                subscriber session to the system.
                
                This column is valid only if the 'tunnelName' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessiontunnelname',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionType', REFERENCE_ENUM_CLASS, 'SubsessiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessiontypeEnum', 
                [], [], 
                '''                This object indicates the type of subscriber session.
                ''',
                'csubsessiontype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionUsername', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the username identifying the subscriber.
                
                This column is valid only if the 'username' bit of the
                corresponding instance of csubSessionAvailableIdentities is
                '1'.
                ''',
                'csubsessionusername',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubSessionEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubsessiontable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubsessiontable',
            False, 
            [
            _MetaInfoClassMember('csubSessionEntry', REFERENCE_LIST, 'Csubsessionentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry', 
                [], [], 
                '''                This entry contains data describing a subscriber sessions,
                including its state, configuration, and collected identities.
                
                An entry exists for a corresponding entry in the ifTable
                describing a subscriber session.  Currently, subscriber
                sessions must have one of the following ifType values:
                
                    'ppp'
                    'ipSubscriberSession'
                    'l2SubscriberSession'
                
                The system creates an entry when it establishes a subscriber
                session.  Likewise, the system destroys an entry when it
                terminates the corresponding subscriber session.
                ''',
                'csubsessionentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubSessionTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry',
            False, 
            [
            _MetaInfoClassMember('csubSessionByType', REFERENCE_ENUM_CLASS, 'SubsessiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessiontypeEnum', 
                [], [], 
                '''                This object indicates the type of the subscriber session.
                ''',
                'csubsessionbytype',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubSessionIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object indicates the ifIndex assigned to the subscriber
                session.
                ''',
                'csubsessionifindex',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubSessionByTypeEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubsessionbytypetable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubsessionbytypetable',
            False, 
            [
            _MetaInfoClassMember('csubSessionByTypeEntry', REFERENCE_LIST, 'Csubsessionbytypeentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry', 
                [], [], 
                '''                This entry identifies a subscriber session.
                
                An entry exists for a corresponding entry in the ifTable
                describing a subscriber session.  Currently, subscriber
                sessions must have one of the following ifType values:
                
                    'ppp'
                    'ipSubscriberSession'
                    'l2SubscriberSession'
                
                The system creates an entry when it establishes a subscriber
                session.  Likewise, the system destroys an entry when it
                terminates the corresponding subscriber session.
                ''',
                'csubsessionbytypeentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubSessionByTypeTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.CsubaggstatspointtypeEnum' : _MetaInfoEnum('CsubaggstatspointtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'physical':'physical',
            'interface':'interface',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsPointType', REFERENCE_ENUM_CLASS, 'CsubaggstatspointtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.CsubaggstatspointtypeEnum', 
                [], [], 
                '''                This object indicates format of the csubAggStatsPoint
                for this entry. 
                
                The format for the csubAggStatsPoint is as follows: 
                
                csubAggStatsPointType      csubAggStatsPoint 
                ----------------------     ------------------ 
                    'physical'                 PhysicalIndex 
                    'interface'                InterfaceIndex
                ''',
                'csubaggstatspointtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsPoint', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object should be read with csubAggStatsPointType always.
                
                This object indicates one of the determining factors affecting 
                the 'scope of aggregation' for the set of statistics contained 
                by the row. 
                
                The value indicated by this object should be interpreted as the 
                identifier for the point type specific base table. 
                
                For point types of 'physical', the type specific base table is 
                the entPhysicalTable and this value is a PhysicalIndex.  For 
                point types of 'interface', the type specific base table is 
                the ifTable and this value is an InterfaceIndex. 
                
                If this column indicates a physical entity which has an 
                entPhysicalClass of 'chassis', then the 'scope of aggregation' 
                may includes those subscriber sessions maintained by all nodes 
                contained by the system. 
                
                If this column indicates a physical entity which has an 
                entPhysicalClass of  'module' (e.g., a line card), then the 
                'scope of aggregation' may include those subscriber sessions 
                maintained by the nodes contained by the module. 
                
                If this column indicates a physical entity which has an 
                entPhysicalClass of 'cpu', then the 'scope of aggregation' may 
                include those subscriber sessions maintained by the node 
                running on the processor. 
                
                Aggregation points with entPhysicalTable / ifTable overlap: 
                For interfaces which map directly to physical 'port' class 
                entities in the entPhysicalTable, the preferred representation 
                as aggregation points is the 'physical' point type and 
                PhysicalIndex identifier.
                ''',
                'csubaggstatspoint',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsSessionType', REFERENCE_ENUM_CLASS, 'SubsessiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessiontypeEnum', 
                [], [], 
                '''                This object indicates one of the determining factors affecting
                the 'scope of aggregation' for the statistics contained by the
                row.
                
                If the value of this column is 'all', then the 'scope of
                aggregation' may include all subscriber sessions, regardless of
                type.
                
                If the value of this column is not 'all', then the 'scope of
                aggregation' may include subscriber sessions of the indicated
                subscriber session type.
                ''',
                'csubaggstatssessiontype',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber session
                within the 'scope of aggregation' that have been authenticated.
                ''',
                'csubaggstatsauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsAvgSessionRPH', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average rate (per hour) at which the
                nodes contained by the 'scope of aggregation' have established new
                subscriber sessions.
                ''',
                'csubaggstatsavgsessionrph',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsAvgSessionRPM', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average rate (per minute) at which
                the nodes contained by the 'scope of aggregation' have
                established new subscriber sessions.
                ''',
                'csubaggstatsavgsessionrpm',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsAvgSessionUptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average time subscriber sessions
                within the 'scope of aggregation' spent in the UP state.
                
                The system calculates this average over all subscriber
                sessions maintained by all nodes contained by the 'scope of
                aggregation' since the last discontinuity time.
                ''',
                'csubaggstatsavgsessionuptime',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned from the
                UNAUTHENTICATED to the AUTHENTICATED state during the current
                15-minute interval.
                ''',
                'csubaggstatscurrauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrCreatedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' created during the current
                15-minute interval.
                ''',
                'csubaggstatscurrcreatedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrDiscSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                terminated due to a disconnect event during the current
                15-minute interval.
                ''',
                'csubaggstatscurrdiscsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrFailedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that were in the PENDING state
                and terminated for reasons other than disconnect during the
                current 15-minute interval.
                ''',
                'csubaggstatscurrfailedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrFlowsUp', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                This object indicates the current number of differential traffic classes
                on subscriber sessions currently UP. IP ACLs are used to create differential flows
                (Traffic Classes).Each Traffic Class can have a different set of features applied.
                ''',
                'csubaggstatscurrflowsup',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrInvalidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                This object indicates the number of intervals in the range
                from 0 to csubCurrValidIntervals for which no data is
                available.  This object will typically be '0' except in certain
                circumstances when some intervals are unavailable.
                ''',
                'csubaggstatscurrinvalidintervals',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '899')], [], 
                '''                This object indicates the time that has elapsed since the
                beginning of the current 15-minute measurement interval.  If,
                for some reason, such as an adjustment in the system's
                time-of-day clock, the current interval exceeds the maximum
                value, then the value of this column will be the maximum value.
                ''',
                'csubaggstatscurrtimeelapsed',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned to the UP
                state during the current 15-minute interval.
                ''',
                'csubaggstatscurrupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsCurrValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                This object indicates the number of intervals for which data
                was collected.  The value of this column will be '96' unless the
                measurement was started (or restarted) within 1,440 minutes, in
                which case the value will be the number of complete 15-minute
                intervals for which the system has at least some data.
                
                In certain cases it is possible that some intervals are
                unavailable, in which case the value of this column will
                be maximum interval number for which data is available.
                ''',
                'csubaggstatscurrvalidintervals',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDayAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned from the
                UNAUTHENTICATED to the AUTHENTICATED state during the last 24
                hours.
                
                The system calculates the value of this column by summing the
                values of all instances of csubAggStatsIntAuthSessions that
                expand this row and have a corresponding csubAggStatsIntValid of
                'true'.
                ''',
                'csubaggstatsdayauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDayCreatedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' created during the last 24
                hours.
                
                The system calculates the value of this column by summing the
                values of all instances of csubAggStatsIntCreatedSessions that
                expand this row and have a corresponding csubAggStatsIntValid of
                'true'.
                ''',
                'csubaggstatsdaycreatedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDayDiscSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                terminated due to a disconnect event during the last 24 hours.
                
                The system calculates the value of this column by summing the
                values of all instances of csubAggStatsIntDiscSessions that
                expand this row and have a corresponding csubAggStatsIntValid of
                'true'.
                ''',
                'csubaggstatsdaydiscsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDayFailedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that were in the PENDING state
                and terminated for reasons other than disconnect during the
                last 24 hours.
                
                The system calculates the value of this column by summing the
                values of all instances of csubAggStatsIntFailedSessions that
                expand this row and have a corresponding csubAggStatsIntValid
                of 'true'.
                ''',
                'csubaggstatsdayfailedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDayUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned to the UP
                state during the last 24 hours.
                
                The system calculates the value of this column by summing the
                values of all instances of csubAggStatsIntUpSessions that
                expand this row and have a corresponding csubAggStatsIntValid
                of 'true'.
                ''',
                'csubaggstatsdayupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsDiscontinuityTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The date and time (as determined by the system's clock) of
                the most recent occurrence of an event affecting the 
                continuity of the aggregation statistics for this aggregation 
                point.
                ''',
                'csubaggstatsdiscontinuitytime',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsHighUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the highest number of subscriber sessions
                within the 'scope of aggregation' observed simultaneously in the UP
                state since the last discontinuity time.
                ''',
                'csubaggstatshighupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsLightWeightSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber
                sessions within the 'scope of aggregation' that are less resource intensive.
                ''',
                'csubaggstatslightweightsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsPendingSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber sessions
                within the 'scope of aggregation' that are in the PENDING
                state.
                ''',
                'csubaggstatspendingsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsRedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber sessions
                within the 'scope of aggregation' that are redundant (i.e., 
                sessions with a csubSessionRedundancyMode of 'standby').
                ''',
                'csubaggstatsredsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsThrottleEngagements', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of times that nodes contained
                within the 'scope of aggregation' have engaged the subscriber
                session throttle since the last discontinuity time.
                
                The mechanics of a subscriber session throttle vary with
                subscriber session type and implementation.  However, the
                general concept of the throttle prevents a node from having
                to deal with more than a configured number of requests to
                establish subscriber sessions from the same CPE within the a
                configured interval of time.  When the number of requests
                exceeds the configured threshold within the configured interval,
                then the node processing the requests engages the throttle.
                Typically, when a node engages a throttle, it drops requests
                from the CPE for some period of time, after which the node
                disengages the throttle.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime.
                ''',
                'csubaggstatsthrottleengagements',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned from the
                UNAUTHENTICATED to the AUTHENTICATED state since the last
                discontinuity time.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime
                ''',
                'csubaggstatstotalauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalCreatedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' created since the
                discontinuity time.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime.
                ''',
                'csubaggstatstotalcreatedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalDiscSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                terminated due to a disconnect event since the last
                discontinuity time.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime
                ''',
                'csubaggstatstotaldiscsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalFailedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that were in the PENDING state
                and terminated for reasons other than disconnect since the last
                discontinuity time.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime.
                ''',
                'csubaggstatstotalfailedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalFlowsUp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of differential traffic classes
                on subscriber sessions. IP ACLs are used to create differential flows(Traffic Classes). 
                Each Traffic Class can have a different set of features applied.
                ''',
                'csubaggstatstotalflowsup',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalLightWeightSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                that are less resource intensive
                ''',
                'csubaggstatstotallightweightsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTotalUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned to the UP
                state since the last discontinuity time.
                
                Discontinuities in the value of this counter can occur at
                re-initialization of the management system, and at other times
                as indicated by the value of csubAggStatsDiscontinuityTime
                ''',
                'csubaggstatstotalupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsUnAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber session
                within the 'scope of aggregation' that have not been authenticated.
                ''',
                'csubaggstatsunauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the current number of subscriber sessions
                within the 'scope of aggregation' that are in the UP state.
                ''',
                'csubaggstatsupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatstable',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsEntry', REFERENCE_LIST, 'Csubaggstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry', 
                [], [], 
                '''                An entry contains a set of aggregated statistics relating to
                those subscriber sessions that fall into a 'scope of 
                aggregation'. 
                
                A 'scope of aggregation' is the set of subscriber sessions 
                that meet specified criteria.  For example, a 'scope of 
                aggregation' may be the set of all PPPoE subscriber sessions 
                maintained by the system.  The following criteria define the 
                'scope of aggregation': 
                
                1)  Aggregation Point type 
                        Aggregation point type identifies the format of the 
                        csubAggStatsPoint for this entry. 
                
                2)  Aggregation Point 
                        'Physical' Aggregation Point type case: 
                        In a distributed system, a 'node' represents a physical 
                        entity capable of maintaining the context representing 
                        a subscriber session. 
                
                        If the 'scope of aggregation' specifies a physical 
                        entity having an entPhysicalClass of 'chassis', then 
                        the set of subscriber sessions in the 'scope of 
                        aggregation' may contain the subscriber sessions maintained by all 
                        the nodes contained in the system. 
                
                        If the 'scope of aggregation' specifies a physical 
                        entity having an entPhysicalClass of 'module' (e.g., a 
                        line card), then the set of subscriber sessions in the 
                        'scope of aggregation' may contain the subscriber 
                        sessions maintained by the nodes contained by the 
                        module. 
                
                        If the 'scope of aggregation' specifies a physical 
                        entity having an entPhysicalClass of 'cpu', then the 
                        set of subscriber sessions in the 'scope of aggregation' 
                        may contain the subscriber sessions maintained by the node 
                        running on that processor. 
                
                        Observe that a centralized system (i.e., a system 
                        that essentially contains a single node) can only 
                        support a 'scope of aggregation' that specifies a 
                        physical entity classified as a 'chassis'. 
                
                        If the scope of aggregation specifies 'interface', 
                        then the scope is the set of subscriber sessions carried 
                        by the interface identified the ifIndex value 
                        represented in the csubAggStatsPoint value. 
                
                2)  Subscriber Session Type 
                        If the 'scope of aggregation' specifies the value 'all' 
                        for the subscriber session type, then the set of 
                        subscriber sessions in the 'scope of aggregation' may 
                        contain all subscriber sessions, regardless of type. 
                
                        If the 'scope of aggregation' specifies a value other 
                        than 'all' for the subscriber session type, then the 
                        set of subscriber sessions in the 'scope of aggregation may 
                        contain only those subscriber sessions of the specified 
                        type. 
                
                Implementation Guidance 
                ======================= 
                A system MUST maintain a set of statistics with a 'scope of 
                aggregation' that contains all subscriber sessions maintained 
                by the system.  The system creates this entry during the 
                initialization of the SNMP entity. 
                
                A system SHOULD maintain a set of statistics for each 'scope of 
                aggregation' containing subscriber sessions of each subscriber 
                session type the system is capable of providing access.  If the 
                system supports these sets of statistics, then it creates these 
                entries during the initialization of the SNMP entity. 
                
                A system MAY maintain sets of node-specific statistics.  if the 
                system supports sets of node-specific statistics, then it 
                creates the appropriate entries upon detection of a physical 
                entity (resulting from system restart or insertion) containing 
                those nodes.  Likewise, the system destroys these entries 
                upon removal of the physical entity.
                ''',
                'csubaggstatsentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsPointType', REFERENCE_ENUM_CLASS, 'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.CsubaggstatspointtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.CsubaggstatspointtypeEnum', 
                [], [], 
                '''                ''',
                'csubaggstatspointtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsPoint', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'csubaggstatspoint',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsSessionType', REFERENCE_ENUM_CLASS, 'SubsessiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessiontypeEnum', 
                [], [], 
                '''                ''',
                'csubaggstatssessiontype',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsIntNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                This object indicates the interval number identifying the
                15-minute measurement interval for which aggregated subscriber
                session performance data was successfully collected by the
                system.
                
                The interval identified by the value '1' represents the most
                recent 15-minute measurement interval, and the interval
                identified by the value (n) represents the interval immediately
                preceding the interval identified by the value (n-1).
                ''',
                'csubaggstatsintnumber',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubAggStatsIntAuthSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned from the
                UNAUTHENTICATED to the AUTHENTICATED state during the
                15-minute measurement interval.
                ''',
                'csubaggstatsintauthsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsIntCreatedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' created during the 15-minute
                measurement interval.
                ''',
                'csubaggstatsintcreatedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsIntDiscSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                terminated due to a disconnect event during the 15-minute
                measurement interval.
                ''',
                'csubaggstatsintdiscsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsIntFailedSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that were in the PENDING state
                and terminated for reasons other than disconnect during the
                15-minute measurement interval.
                ''',
                'csubaggstatsintfailedsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsIntUpSessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the total number of subscriber sessions
                within the 'scope of aggregation' that transitioned to the UP
                state during the 15-minute measurement interval.
                ''',
                'csubaggstatsintupsessions',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsIntValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the data for the 15-minute
                measurement interval is valid.
                ''',
                'csubaggstatsintvalid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsIntEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatsinttable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatsinttable',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsIntEntry', REFERENCE_LIST, 'Csubaggstatsintentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry', 
                [], [], 
                '''                An entry contains the aggregated subscriber session performance
                data collected over a single 15-minute measurement interval
                within a 'scope of aggregation'.  For further details regarding
                'scope of aggregation', see the descriptive text associated with
                the csubAggStatsEntry.
                ''',
                'csubaggstatsintentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsIntTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry',
            False, 
            [
            _MetaInfoClassMember('csubSessionRisingThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This threshold, if non-zero, indicates the rising threshold
                for the value of csubAggStatsUpSessions for the aggregation
                point,
                When the current sample of csubAggStatsUpSessions is greater
                than
                or equal to this threshold, and the value of
                csubAggStatsUpSessions
                for the last sample interval was less than this thershold, the
                csubSessionRisingNotif is triggered.
                
                         If the value of this threshold is 0, the threshold is
                not evaluated.
                ''',
                'csubsessionrisingthresh',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubSessionDeltaPercentFallingThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This threshold, if non-zero, indicates the delta falling
                threshold
                as a percentage of the value of csubAggStatsUpSessions for the
                aggregation point, The delta as a percentage of
                csubAggStatsUpSessions (delta_percent) is calculated as
                follows:
                      current value of csubAggStatsUpSessions = value(n)
                             previous sampled value of csubAggStatsUpSessions =
                value(n-1)
                
                             delta_percent = ((value(n-1) - value(n)) /
                value(n-1)) * 100
                
                         If the delta_percent value of the current evaluation
                interval is
                         greater than the value of this threshold, a
                         csubSessionDeltaPercentLossNotif is triggered.
                
                         If the value of this threshold is 0, the threshold is
                not evaluated.
                ''',
                'csubsessiondeltapercentfallingthresh',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionFallingThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This threshold, if non-zero, indicates the falling threshold
                for the value of csubAggStatsUpSessions for the aggregation
                point,
                When the current sample of csubAggStatsUpSessions is less than
                or equal to this threshold, and the value of
                csubAggStatsUpSessions
                for the last sample interval was greater than this thershold,
                the
                csubSessionFallingNotif is triggered.
                
                         If the value of this threshold is 0, the threshold is
                not evaluated.
                ''',
                'csubsessionfallingthresh',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionThreshEvalInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '900')], [], 
                '''                The value of this object sets the number of seconds between
                samples
                for threshold evaluation. For implementations capable of
                per-session event evaluation of thresholds this object
                represents the maximum number of seconds between samples.
                ''',
                'csubsessionthreshevalinterval',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsThreshEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubaggstatsthreshtable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubaggstatsthreshtable',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsThreshEntry', REFERENCE_LIST, 'Csubaggstatsthreshentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry', 
                [], [], 
                '''                A row in this table exists for each row in the
                csubAggStatsTable.
                Each row defines the set of thresholds and evaluation attributes
                for an aggregation point.
                ''',
                'csubaggstatsthreshentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubAggStatsThreshTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobcontrolEnum' : _MetaInfoEnum('CsubjobcontrolEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'noop':'noop',
            'start':'start',
            'abort':'abort',
            'release':'release',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobfinishedreasonEnum' : _MetaInfoEnum('CsubjobfinishedreasonEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'invalid':'invalid',
            'other':'other',
            'normal':'normal',
            'aborted':'aborted',
            'insufficientResources':'insufficientResources',
            'error':'error',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobstateEnum' : _MetaInfoEnum('CsubjobstateEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'idle':'idle',
            'pending':'pending',
            'inProgress':'inProgress',
            'finished':'finished',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobtypeEnum' : _MetaInfoEnum('CsubjobtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB',
        {
            'noop':'noop',
            'query':'query',
            'clear':'clear',
        }, 'CISCO-SUBSCRIBER-SESSION-MIB', _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB']),
    'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry',
            False, 
            [
            _MetaInfoClassMember('csubJobId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates an arbitrary, positive integer-value
                uniquely identifying the subscriber session job.
                ''',
                'csubjobid',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobControl', REFERENCE_ENUM_CLASS, 'CsubjobcontrolEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobcontrolEnum', 
                [], [], 
                '''                This object specifies an action relating to the subscriber
                session job:
                
                    'noop'
                        This action does nothing.
                
                    'start'
                        If the corresponding instance of csubJobType is 'noop',
                        then this action simply causes the system to set the
                        corresponding instances of csubJobState and
                        csubJobFinishedReason to 'finished' and 'normal',
                        respectively.
                
                        If the corresponding instance of csubJobType is not
                        'noop' and the system is not executing a subscriber
                        session job, then this action causes the system
                        immediately execute the subscriber session job.
                
                        If the corresponding instance of csubJobType is not
                        'noop' and the system is already executing a subscriber
                        session job, then this action causes the system to put
                        the job on the subscriber session job queue.
                
                    'abort'
                        If the subscriber session job is in the subscriber
                        session job queue, then this action causes the system to
                        remove the job from the queue.
                
                        If the system is executing the subscriber session job,
                        then this action causes the system to stop the job.
                
                    'release'
                        This action causes the system to destroy any
                        corresponding rows in the csubJobReportTable.
                
                        The system only accepts this action for a previously
                        executed subscriber session job having a corresponding
                        instance of csubJobType set to 'query'.  Any attempt to
                        issue this action under other circumstances will result
                        in a response indicating an  error-status of
                        'inconsistentValue'.
                
                When read, this column is always 'noop'.
                ''',
                'csubjobcontrol',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobFinishedReason', REFERENCE_ENUM_CLASS, 'CsubjobfinishedreasonEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobfinishedreasonEnum', 
                [], [], 
                '''                This object indicates the reason why the system finished
                executing the subscriber session job:
                
                    'invalid'
                        Indicates that the corresponding instance of
                        csubJobState is either 'idle', 'pending', or
                        'inProgress'.
                
                    'other'
                        Indicates that the system finished executing the
                        subscriber session job abnormally for a reason not
                        recognized by this MIB module.
                
                    'normal'
                        Indicates that the system finished executing the
                        subscriber session job with no problems.
                
                    'aborted'
                        Indicates that the system finished executing the
                        subscriber session job as the result of the EMS/NMS
                        writing 'abort' to the corresponding instance of
                        csubJobControl.
                
                    'insufficientResources'
                        Indicates that the system finished executing the
                        subscriber session job abnormally due to insufficient
                        resources to continue.
                
                    'error'
                        Indicates that the system encountered an error that
                        prevented it from completing the job.
                ''',
                'csubjobfinishedreason',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobFinishedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the value of sysUpTime when the system
                finished executing the subscriber session job, for whatever
                reason.  This value will be '0' when the corresponding instance
                of csubJobState is 'idle', 'pending', or 'inProgress'.
                ''',
                'csubjobfinishedtime',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobStartedTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the value of sysUpTime when the system
                started executing the subscriber session job.  This value will
                be '0' when the corresponding instance of csubJobState is 'idle'
                or 'pending'.
                ''',
                'csubjobstartedtime',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobState', REFERENCE_ENUM_CLASS, 'CsubjobstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobstateEnum', 
                [], [], 
                '''                This object indicates the current state of the subscriber
                session job:
                
                    'idle'
                        This state indicates that the system has not executed
                        the subscriber session job since it was created.
                
                    'pending'
                        This state indicates that the subscriber session job is
                        waiting in the subscriber session job queue.
                
                    'inProgress'
                        This state indicates that the system is executing the
                        subscriber session job.  Observe that the system may
                        execute more than one subscriber session job at a time.
                
                    'finished'
                        This state indicates that the system has executed the
                        subscriber session job and it has finished.  The
                        corresponding instance of csubJobFinishedReason
                        indicates further details regarding the reason why the
                        job finished.
                ''',
                'csubjobstate',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object specifies the status of the subscriber session
                job.  The following columns must be valid before activating a
                subscriber session job:
                
                    - csubJobStorage
                    - csubJobType
                    - csubJobControl
                
                However, these objects specify a default value.  Thus, it is
                possible to use create-and-go semantics without setting any
                additional columns.
                
                An implementation must allow the EMS/NMS to modify any column
                when this column is 'active', including columns defined in
                tables that have a one-to-one or sparse dependent relationship
                on this table.
                ''',
                'csubjobstatus',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object specifies what happens to the subscriber session
                job upon restart.
                ''',
                'csubjobstorage',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobType', REFERENCE_ENUM_CLASS, 'CsubjobtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.CsubjobtypeEnum', 
                [], [], 
                '''                This object specifies the type of subscriber session job:
                
                'noop'
                    This type of job does nothing and simply serves as a
                    convenient default value for newly created jobs, thereby
                    allowing create-and-go row creation without having to
                    specify the type of job.
                
                'query'
                    This type of job starts a subscriber session query.  The
                    system searches for any subscriber sessions matching the
                    configured criteria and sorts them into a resulting
                    report.
                
                    Upon activation of a subscriber session with this value,
                    the system automatically creates corresponding rows in
                    the csubJobMatchParamsTable and csubQueryParamsTable.
                
                'clear'
                    This type of job causes the system to terminated all
                    subscriber sessions matching configured criteria.
                
                    Upon activation of a subscriber session with this value,
                    the system automatically creates a corresponding row in
                    the csubJobMatchParamsTable.
                ''',
                'csubjobtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobtable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobtable',
            False, 
            [
            _MetaInfoClassMember('csubJobEntry', REFERENCE_LIST, 'Csubjobentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry', 
                [], [], 
                '''                An entry describing a subscriber session job.  At this time,
                subscriber session jobs can perform one of two tasks:
                
                - Subscriber Session Query
                    This type of job invokes the report generator, which builds
                    a list of subscriber sessions matching criteria specified by
                    the corresponding row in the csubJobMatchParamsTable.  The
                    list built by the report generator must conform to
                    parameters specified by the corresponding row in
                    csubJobQueryParamsTable, which at this time only affects
                    sorting order.
                
                - Subscriber Session Clear
                    This type of job causes the system to terminate those
                    subscriber sessions matching criteria specified by the
                    corresponding row in the csubJobMatchParamsTable.
                
                The following procedure summarizes how the EMS/NMS can start and
                monitor a subscriber session job:
                
                1)  The EMS/NMS must start by reading csubJobIdNext.  If it is
                    zero, continue polling csubJobIdNext until it is non-zero.
                
                2)  The EMS/NMS creates a row in the csubJobTable using the
                    instance identifier retrieved in the last step.  Since every
                    object contained by the entry with a MAX-ACCESS of 
                    'read-create' specifies a default value, it makes little
                    difference whether the EMS/NMS employs create-and-wait or
                    create-and-go semantics.
                
                3)  The EMS/NMS sets the type of subscriber session job by
                    setting the corresponding instance of csubJobType.
                
                4a) If the job is a 'query', then the EMS/NMS must configure
                    the query before starting it by setting columns contained
                    by the corresponding rows in the csubJobMatchParamsTable and
                    csubJobQueryParamsTable.
                
                4b) If job is a 'clear', then the EMS/NMS must configure
                    the job before starting it by setting columns contained by
                    the corresponding row in the csubJobMatchParamsTable.
                
                5)  The EMS/NMS can now start the job by setting the 
                    corresponding instance of csubJobControl to 'start'.
                
                6)  The EMS/NMS can monitor the progress of the job by polling
                    the corresponding instance of csubJobState.  It can also
                    wait for a csubJobFinishedNotify notification.  When the
                    state of the job transitions to 'finished', then the system
                    has finished executing the job.
                
                7)  The EMS/NMS can determine the final status of the job by
                    reading the corresponding instance of csubJobFinishedReason.
                    If job is a 'query' and the corresponding instance of
                    csubJobFinishedReason is 'normal', then the EMS/NMS can
                    safely read the report by retrieving the corresponding
                    rows from the csubJobReportTable.
                
                8a) After a job has finished, the EMS/NMS has the option of
                    destroying it.  It can do this by simply setting the
                    corresponding instance of  csubJobStatus to 'destroy'.
                    Alternatively, the EMS/NMS may retain the job and execute it
                    again in the future (by returning to step 5).  Additionally,
                    nothing would prevent the EMS/NMS from changing the job's
                    type, which causes the automatic destruction of the
                    corresponding report.
                
                8b) If the job is a 'query' and the EMS/NMS opts to retain the
                    job, then it may consider releasing the corresponding report
                    after reading it.  It can do this by setting the
                    corresponding instance of csubJobControl to 'release'.
                ''',
                'csubjobentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry',
            False, 
            [
            _MetaInfoClassMember('csubJobId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'csubjobid',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobMatchAcctSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the accounting session identifier the
                system matches against subscriber sessions in the process of
                executing a subscriber session job.
                
                This value is valid only if the 'accountingSid' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchacctsessionid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchAuthenticated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether a subscriber session should be
                unauthenticated for the system to consider a match in the
                process of executing a subscriber session job.
                
                If this column is 'false', then the subscriber session job
                matches subscriber sessions that are unauthenticated.
                
                If this column is 'true', then the subscriber session job
                matches subscriber session that are authenticated.
                
                This value is valid only if the 'authenticated' bit of the
                corresponding instance of csubJobMatchParams is '1'.
                ''',
                'csubjobmatchauthenticated',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchCircuitId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the Circuit-Id the system matches against
                subscriber sessions in the process of executing a subscriber
                session job.
                
                This value is valid only if the 'circuitId' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchcircuitid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDanglingDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                This object specifies the minimum interval of time a subscriber
                session can remain dangling in order for the system to consider
                it a match in the process of executing a subscriber session job.
                A 'dangling' subscriber session is one in the PENDING state.
                
                The value '0' cannot be written to an instance of this object.
                However, it serves as a convenient value when the column is not
                valid.
                
                This value is valid only if the 'danglingDuration' bit of the
                corresponding instance of csubJobMatchOtherParams is '1'.
                ''',
                'csubjobmatchdanglingduration',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDhcpClass', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the DHCP class name the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'dhcpClass' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdhcpclass',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDnis', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the DNIS number the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'dnis' bit of the corresponding
                instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdnis',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDomain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the domain the system matches against
                subscriber sessions in the process of executing a subscriber
                session job.
                
                This value is valid only if the 'domain' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdomain',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDomainIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the domain IP address that the system
                matches against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdomainipaddr',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDomainIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of Internet address specified
                by csubJobMatchDomainIpAddr and csubJobMatchDomainIpMask.
                
                This value is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdomainipaddrtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDomainIpMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the mask used when matching the domain IP
                address against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'domainIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdomainipmask',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchDomainVrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the domain VRF the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'domainVrf' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchdomainvrf',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchIdentities', REFERENCE_BITS, 'Subsessionidentities' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'Subsessionidentities', 
                [], [], 
                '''                This object specifies the subscriber identities that the
                system uses to determine the subscriber sessions the job
                executes on.
                
                Each bit in this bit string corresponds to one or more columns
                in this table.  If the bit is '0', then the value of the
                corresponding columns are invalid.  If the bit is '1', then the
                value of corresponding columns are valid.
                
                The following list specifies the mappings between the bits and
                the columns:
                
                    'subscriberLabel' => csubJobMatchSubscriberLabel
                    'macAddress'      => csubJobMatchMacAddress
                    'nativeVrf'       => csubJobMatchNativeVrf
                    'nativeIpAddress' => csubJobMatchNativeIpAddrType,
                                         csubJobMatchNativeIpAddr,
                                         csubJobMatchNativeIpMask,
                    'domainVrf'       => csubJobMatchDomainVrf
                    'domainIpAddress' => csubJobMatchDomainIpAddrType,
                                         csubJobMatchDomainIpAddr,
                                         csubJobMatchDomainIpMask
                    'pbhk'            => csubJobMatchPbhk
                    'remoteId'        => csubJobMatchRemoteId
                    'circuitId'       => csubJobMatchCircuitId
                    'nasPort'         => csubJobMatchNasPort
                    'domain'          => csubJobMatchDomain
                    'username'        => csubJobMatchUsername
                    'acctSessionId'   => csubJobMatchAcctSessionId
                    'dnis'            => csubJobMatchDnis
                    'media'           => csubJobMatchMedia
                    'mlpNegotiated'   => csubJobMatchMlpNegotiated
                    'protocol'        => csubJobMatchProtocol
                    'serviceName'     => csubJobMatchServiceName
                    'dhcpClass'       => csubJobMatchDhcpClass
                    'tunnelName'      => csubJobMatchTunnelName
                
                Observe that the bit 'ifIndex' has no meaning, as subscriber
                session jobs do not match against this subscriber session
                identity.
                ''',
                'csubjobmatchidentities',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                This object specifies the MAC address that the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'macAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchmacaddress',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchMedia', REFERENCE_ENUM_CLASS, 'SubscribermediatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscribermediatypeEnum', 
                [], [], 
                '''                This object specifies the media type the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'media' bit of the corresponding
                instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchmedia',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchMlpNegotiated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the MLP negotiated flag the system
                matches against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'mlpNegotiated' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchmlpnegotiated',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchNasPort', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the NAS port-identifier the system
                matches against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'nasPort' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchnasport',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchNativeIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the native IP address that the system
                matches against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchnativeipaddr',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchNativeIpAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of Internet address specified
                by csubJobMatchNativeIpAddr and csubJobMatchNativeIpMask.
                
                This value is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchnativeipaddrtype',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchNativeIpMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the mask used when matching the native IP
                address against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'nativeIpAddress' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchnativeipmask',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchNativeVrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the native VRF the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'nativeVrf' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchnativevrf',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchOtherParams', REFERENCE_BITS, 'Csubjobmatchotherparams' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry.Csubjobmatchotherparams', 
                [], [], 
                '''                This object specifies other parameters relating to subscriber
                sessions a subscriber session job may match against.
                
                Each bit in this bit string corresponds to a column in this
                table.  If the bit is '0', then the value of the corresponding
                column is invalid.  If the bit is '1', then the value of the
                corresponding column represents the value of the parameter
                identity the system should match against for the corresponding
                subscriber session job.
                
                The following list specifies the mappings between bits and the
                columns:
                
                    'danglingDuration' => csubJobMatchDanglingDuration
                    'state'            => csubJobMatchState
                    'authenticated'    => csubJobMatchAuthenticated
                    'redundancyMode'   => csubJobMatchRedundancyMode
                ''',
                'csubjobmatchotherparams',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchPbhk', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the PBHK that the system matches against
                subscriber sessions in the process of executing a subscriber
                session job.
                
                This value is valid only if the 'pbhk' bit of the corresponding
                instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchpbhk',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchProtocol', REFERENCE_ENUM_CLASS, 'SubscriberprotocoltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberprotocoltypeEnum', 
                [], [], 
                '''                This object specifies the protocol type the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'protocol' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchprotocol',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchRedundancyMode', REFERENCE_ENUM_CLASS, 'SubsessionredundancymodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessionredundancymodeEnum', 
                [], [], 
                '''                This object specifies the redudancy mode of the subscriber
                session in order for the system to consider a match in the
                process of executing a subscriber session job.
                
                The value 'other' is not valid and an implementation should not
                allow it to be written to this column.
                
                This value is valid only if the 'redundancyMode' bit of the
                corresponding instance of csubJobMatchOtherParams is '1'.
                ''',
                'csubjobmatchredundancymode',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchRemoteId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the Remote-Id the system matches against
                subscriber sessions in the process of executing a subscriber
                session job.
                
                This value is valid only if the 'remoteId' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchremoteid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchServiceName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the service name the system matches
                against subscriber sessions in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'serviceName' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchservicename',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchState', REFERENCE_ENUM_CLASS, 'SubsessionstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubsessionstateEnum', 
                [], [], 
                '''                This object specifies the state of a subscriber session in
                order for the system to consider a match in the process of
                executing a subscriber session job.
                
                The value 'other' is not valid and an implementation should
                not allow it to be written to this column.
                
                This value is valid only if the 'state' bit of the
                corresponding instance of csubJobMatchOtherParams is '1'.
                ''',
                'csubjobmatchstate',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchSubscriberLabel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the subscriber label that the system
                matches against subscriber sessions in the process of executing
                a subscriber session job.
                
                This value is valid only if the 'subscriberLabel' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchsubscriberlabel',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchTunnelName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the tunnel name the system matches
                against subscriber session in the process of executing a
                subscriber session job.
                
                This value is valid only if the 'tunnelName' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchtunnelname',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchUsername', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the username the system matches against
                subscriber sessions in the process of executing a subscriber
                session job.
                
                This value is valid only if the 'username' bit of the
                corresponding instance of csubJobMatchIdentities is '1'.
                ''',
                'csubjobmatchusername',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobMatchParamsEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobmatchparamstable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobmatchparamstable',
            False, 
            [
            _MetaInfoClassMember('csubJobMatchParamsEntry', REFERENCE_LIST, 'Csubjobmatchparamsentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry', 
                [], [], 
                '''                An entry describes a set of subscriber session match criteria.
                The set contains those subscriber session identities specified
                by csubJobMatchIdentities.
                
                If the corresponding row in the csubJobTable has a csubJobType
                of 'query', then the system builds a report containing those
                subscriber sessions matching these criteria.
                
                If the corresponding row in the csubJobTable has a csubJobType
                of 'clear', then the system terminates those subscriber
                sessions matching these criteria.
                
                The system automatically creates an entry when the EMS/NMS sets
                the corresponding instance of csubJobType to 'query' or 'clear'.
                Likewise, the system automatically destroys an entry under the
                following circumstances:
                
                1)  The EMS/NMS destroys the corresponding row in the
                    csubJobTable.
                
                2)  The EMS/NMS sets the corresponding instance of csubJobType
                    to 'noop'.
                ''',
                'csubjobmatchparamsentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobMatchParamsTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry',
            False, 
            [
            _MetaInfoClassMember('csubJobId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'csubjobid',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobQueryResultingReportSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the number of subscriber sessions that
                matched the corresponding subscriber session query.
                
                The value of this column should be '0' unless the corresponding
                value of csubJobState is 'finished'.
                
                The value of this column should be '0' after the EMS/NMS sets
                the corresponding csubJobControl to 'release'.
                ''',
                'csubjobqueryresultingreportsize',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobQuerySortKey1', REFERENCE_ENUM_CLASS, 'SubsessionidentityEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubsessionidentityEnum', 
                [], [], 
                '''                This object specifies the first subscriber identity that the
                system uses when sorting subscriber sessions into the final
                report corresponding to a subscriber session query.
                
                It is not valid to set this column to 'other' or 'ifIndex'.
                ''',
                'csubjobquerysortkey1',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobQuerySortKey2', REFERENCE_ENUM_CLASS, 'SubsessionidentityEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubsessionidentityEnum', 
                [], [], 
                '''                This object specifies the second subscriber identity that the
                system uses when sorting subscriber sessions into the final
                report corresponding to a subscriber session query.
                
                If it is the desire to have the final report sorted on a single
                subscriber identity, then this column should be 'other'.
                ''',
                'csubjobquerysortkey2',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobQuerySortKey3', REFERENCE_ENUM_CLASS, 'SubsessionidentityEnum' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubsessionidentityEnum', 
                [], [], 
                '''                This object specifies the third subscriber identity that the
                system uses when sorting subscriber sessions into the final
                report corresponding to a subscriber session query.
                
                If it is the desire to have the final report sorted on one or
                two subscriber identities, then this column should be 'other'.
                ''',
                'csubjobquerysortkey3',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobQueryParamsEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobqueryparamstable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobqueryparamstable',
            False, 
            [
            _MetaInfoClassMember('csubJobQueryParamsEntry', REFERENCE_LIST, 'Csubjobqueryparamsentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry', 
                [], [], 
                '''                An entry describes a set of subscriber session query
                parameters.
                
                The system automatically creates an entry when the EMS/NMS sets
                the corresponding instance of csubJobType to 'query'.  Likewise,
                the system automatically destroys an entry under the following
                circumstances:
                
                1)  The EMS/NMS destroys the corresponding row in the csubJobTable.
                
                2)  The EMS/NMS sets the corresponding instance of csubJobType to
                    'noop' or 'clear'.
                ''',
                'csubjobqueryparamsentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobQueryParamsTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry',
            False, 
            [
            _MetaInfoClassMember('csubJobQueueNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates an positive, integer-value that uniquely
                identifies the entry in the table. The value of this object
                starts at '1' and monotonically increases for each subscriber
                session job inserted into the subscriber session job queue.  If
                the value of this object is '4294967295', the system will reset
                it to '1' when it inserts the next subscriber session job into
                the subscriber session job queue.
                ''',
                'csubjobqueuenumber',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobQueueJobId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates the identifier associated with the
                subscriber session job.
                ''',
                'csubjobqueuejobid',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobQueueEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobqueuetable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobqueuetable',
            False, 
            [
            _MetaInfoClassMember('csubJobQueueEntry', REFERENCE_LIST, 'Csubjobqueueentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry', 
                [], [], 
                '''                An entry describing an subscriber session job in the
                subscriber session job queue.
                
                The system creates an entry in this table when it places a
                subscriber session job on the subscriber session job queue.  It
                does this when the EMS/NMS sets an instance of csubJobControl to
                'start' and the system is already executing a subscriber session
                job.  Likewise, the system destroys an entry when it removes it
                from the queue.  This occurs under the following circumstances:
                
                1)  The system has finished executing a job, for whatever
                    reason, and is ready to start executing the job at the head
                    of the queue.
                
                2)  The EMS/NMS has set an instance of csubJobControl to 'abort'
                    for a job that was on the queue.
                ''',
                'csubjobqueueentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobQueueTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry',
            False, 
            [
            _MetaInfoClassMember('csubJobId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'csubjobid',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobReportId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object indicates an arbitrary, positive, integer-value
                that uniquely identifies this entry in a report.  This auxiliary
                value is necessary, as the corresponding subscriber session job
                can specify up to three subscriber identities on which to sort
                the subscriber sessions that end up in the final report.
                ''',
                'csubjobreportid',
                'CISCO-SUBSCRIBER-SESSION-MIB', True),
            _MetaInfoClassMember('csubJobReportSession', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object indicates the ifIndex-value assigned to the
                subscriber session that satisfied the match criteria specified
                by the corresponding subscriber session job having a csubJobType
                of 'query'.
                ''',
                'csubjobreportsession',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobReportEntry',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib.Csubjobreporttable' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib.Csubjobreporttable',
            False, 
            [
            _MetaInfoClassMember('csubJobReportEntry', REFERENCE_LIST, 'Csubjobreportentry' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry', 
                [], [], 
                '''                An entry describes a subscriber session that satisfied the
                match criteria specified by the corresponding job.
                
                The system creates an entry for each subscriber session that
                satisfied the specified match criteria of a subscriber session
                job having a csubJobType of 'query'.  However, it does not
                create these entries until after the system has successfully
                executed the subscriber session job.
                
                The system destroys an entry under the following circumstances:
                
                1)  The corresponding subscriber session job has been destroyed
                    by the EMS/NMS.
                
                2)  The value of csubJobMaxLife is non-zero and the age of the
                    report has reached the specified maximum life.
                
                3)  The EMS/NMS has set the corresponding instance of
                    csubJobControl to 'release'.
                
                4)  The EMS/NMS has restarted the corresponding subscriber
                    session job (i.e., has set the corresponding instance of
                    csubJobControl to 'start').
                ''',
                'csubjobreportentry',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'csubJobReportTable',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
    'CiscoSubscriberSessionMib' : {
        'meta_info' : _MetaInfoClass('CiscoSubscriberSessionMib',
            False, 
            [
            _MetaInfoClassMember('csubAggStatsIntTable', REFERENCE_CLASS, 'Csubaggstatsinttable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatsinttable', 
                [], [], 
                '''                This table contains aggregated subscriber session performance
                data collected for as much as a day's worth of 15-minute
                measurement intervals.
                
                This table has an expansion dependent relationship on the
                csubAggStatsTable, containing zero or more rows for each row
                contained by the csubAggStatsTable.
                
                Observe that the collection and maintenance of aggregated
                subscriber performance data is OPTIONAL for all scopes of
                aggregation.  However, an implementation should maintain at
                least one interval for the 'scope of aggregation' that contains
                all subscriber sessions maintained by the system.
                ''',
                'csubaggstatsinttable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsTable', REFERENCE_CLASS, 'Csubaggstatstable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatstable', 
                [], [], 
                '''                This table contains sets of aggregated statistics relating to
                subscriber sessions, where each set has a unique scope of
                aggregation.
                ''',
                'csubaggstatstable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggStatsThreshTable', REFERENCE_CLASS, 'Csubaggstatsthreshtable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggstatsthreshtable', 
                [], [], 
                '''                Please enter the Table Description here.
                ''',
                'csubaggstatsthreshtable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubAggThresh', REFERENCE_CLASS, 'Csubaggthresh' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubaggthresh', 
                [], [], 
                '''                ''',
                'csubaggthresh',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJob', REFERENCE_CLASS, 'Csubjob' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjob', 
                [], [], 
                '''                ''',
                'csubjob',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobMatchParamsTable', REFERENCE_CLASS, 'Csubjobmatchparamstable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobmatchparamstable', 
                [], [], 
                '''                This table contains subscriber session job parameters
                describing match criteria.
                
                This table has a sparse-dependent relationship on the
                csubJobTable, containing a row for each job having a
                csubJobType of 'query' or 'clear'.
                ''',
                'csubjobmatchparamstable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobQueryParamsTable', REFERENCE_CLASS, 'Csubjobqueryparamstable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobqueryparamstable', 
                [], [], 
                '''                This table contains subscriber session job parameters
                describing query parameters.
                
                This table has a sparse-dependent relationship on the
                csubJobTable, containing a row for each job having a
                csubJobType of 'query'.
                ''',
                'csubjobqueryparamstable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobQueueTable', REFERENCE_CLASS, 'Csubjobqueuetable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobqueuetable', 
                [], [], 
                '''                This table lists the subscriber session jobs currently pending
                in the subscriber session job queue.
                ''',
                'csubjobqueuetable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobReportTable', REFERENCE_CLASS, 'Csubjobreporttable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobreporttable', 
                [], [], 
                '''                This table contains the reports corresponding to subscriber
                session jobs that have a csubJobType of 'query' and
                csubJobState of 'finished'.
                
                This table has an expansion dependent relationship on the
                csubJobTable, containing zero or more rows for each job.
                ''',
                'csubjobreporttable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubJobTable', REFERENCE_CLASS, 'Csubjobtable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubjobtable', 
                [], [], 
                '''                This table contains the subscriber session jobs submitted by
                the EMS/NMS.
                ''',
                'csubjobtable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionByTypeTable', REFERENCE_CLASS, 'Csubsessionbytypetable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubsessionbytypetable', 
                [], [], 
                '''                This table describes a list of subscriber sessions currently
                maintained by the system.  The tables sorts the subscriber
                sessions first by the subscriber session's type and second by
                the ifIndex assigned to the subscriber session.
                ''',
                'csubsessionbytypetable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            _MetaInfoClassMember('csubSessionTable', REFERENCE_CLASS, 'Csubsessiontable' , 'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CiscoSubscriberSessionMib.Csubsessiontable', 
                [], [], 
                '''                This table describes a list of subscriber sessions currently
                maintained by the system.
                
                This table has a sparse dependent relationship on the ifTable,
                containing a row for each interface having an interface type
                describing a subscriber session.
                ''',
                'csubsessiontable',
                'CISCO-SUBSCRIBER-SESSION-MIB', False),
            ],
            'CISCO-SUBSCRIBER-SESSION-MIB',
            'CISCO-SUBSCRIBER-SESSION-MIB',
            _yang_ns._namespaces['CISCO-SUBSCRIBER-SESSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB'
        ),
    },
}
_meta_table['CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubsessiontable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubsessionbytypetable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubaggstatstable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubaggstatsinttable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubaggstatsthreshtable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubjobtable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubjobmatchparamstable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubjobqueryparamstable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubjobqueuetable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib.Csubjobreporttable']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjob']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggthresh']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubsessiontable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubsessionbytypetable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatstable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatsinttable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubaggstatsthreshtable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobtable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobmatchparamstable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobqueryparamstable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobqueuetable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']
_meta_table['CiscoSubscriberSessionMib.Csubjobreporttable']['meta_info'].parent =_meta_table['CiscoSubscriberSessionMib']['meta_info']




import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIetfPwMib.Cpwvcobjects' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcobjects',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an appropriate value to be used 
                for cpwVcIndex when creating entries in the 
                cpwVcTable. The value 0 indicates that no 
                unassigned entries are available.  To obtain the 
                value of cpwVcIndex for a new entry in the 
                cpwVcTable, the manager issues a management 
                protocol retrieval operation to obtain the current 
                value of cpwVcIndex.  After each retrieval 
                operation, the agent should modify the value to 
                reflect the next unassigned index.  After a manager 
                retrieves a value the agent will determine through 
                its local policy when this index value will be made 
                available for reuse.
                ''',
                'cpwvcindexnext',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcNotifRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object defines the maximum number of PW VC notifications
                that can be emitted from the device per second.
                ''',
                'cpwvcnotifrate',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalErrorPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for number of error at VC level processing, for  
                example packets received with unknown VC label.
                ''',
                'cpwvcperftotalerrorpackets',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcUpDownNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is set to true(1), then it enables
                the emission of cpwVcUp and cpwVcDown
                notifications; otherwise these notifications are not
                emitted.
                ''',
                'cpwvcupdownnotifenable',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcObjects',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcadminstatusEnum' : _MetaInfoEnum('CpwvcadminstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'CISCO-IETF-PW-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MIB']),
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcinboundmodeEnum' : _MetaInfoEnum('CpwvcinboundmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB',
        {
            'loose':'loose',
            'strict':'strict',
        }, 'CISCO-IETF-PW-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MIB']),
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcownerEnum' : _MetaInfoEnum('CpwvcownerEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB',
        {
            'manual':'manual',
            'maintenanceProtocol':'maintenanceProtocol',
            'other':'other',
        }, 'CISCO-IETF-PW-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MIB']),
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcpsntypeEnum' : _MetaInfoEnum('CpwvcpsntypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB',
        {
            'mpls':'mpls',
            'l2tp':'l2tp',
            'ip':'ip',
            'mplsOverIp':'mplsOverIp',
            'gre':'gre',
            'other':'other',
        }, 'CISCO-IETF-PW-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MIB']),
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcremotecontrolwordEnum' : _MetaInfoEnum('CpwvcremotecontrolwordEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB',
        {
            'noControlWord':'noControlWord',
            'withControlWord':'withControlWord',
            'notYetKnown':'notYetKnown',
        }, 'CISCO-IETF-PW-MIB', _yang_ns._namespaces['CISCO-IETF-PW-MIB']),
    'CiscoIetfPwMib.Cpwvctable.Cpwvcentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvctable.Cpwvcentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index for the conceptual row identifying a VC within  
                this PW Emulation VC table.
                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcAdminStatus', REFERENCE_ENUM_CLASS, 'CpwvcadminstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcadminstatusEnum', 
                [], [], 
                '''                The desired operational status of this VC.
                ''',
                'cpwvcadminstatus',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcControlWord', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Define if the control word will be sent with each packet by  
                the local node.
                ''',
                'cpwvccontrolword',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcCreateTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System time when this VC was created.
                ''',
                'cpwvccreatetime',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual string containing information about the VC.  
                If there is no description this object contains a zero 
                length string.
                ''',
                'cpwvcdescr',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcHoldingPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                This object define the relative holding priority of the VC   
                in a lowest-to-highest fashion, where 0 is the highest  
                priority. VCs with the same priority are treated with 
                equal priority. Dropped VC will be set 'dormant' (as 
                indicated in cpwVcOperStatus). 
                This value is significant if there are competing resources 
                between VCs and the implementation support this feature. 
                If not supported or not relevant, the value of zero MUST 
                be used.
                ''',
                'cpwvcholdingpriority',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used in the outgoing VC ID field within the 'Virtual 
                Circuit FEC Element' when LDP signaling is used or PW ID  
                AVP for L2TP.
                ''',
                'cpwvcid',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcInboundMode', REFERENCE_ENUM_CLASS, 'CpwvcinboundmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcinboundmodeEnum', 
                [], [], 
                '''                This object is used to enable greater security for  
                implementation that use per platform VC label space. In  
                strict mode, packets coming from the PSN are accepted only  
                from tunnels that are associated to the same VC via the  
                inbound tunnel table in the case of MPLS, or as identified  
                by the source IP address in case of L2TP or IP PSN. The  
                entries in the inbound tunnel table are either explicitly  
                configured or implicitly known by the maintenance protocol  
                used for VC set-up. 
                
                If such association is not known, not configured or not  
                desired, loose mode should be configured, and the node  
                should accept the packet based on the VC label only  
                regardless of the outer tunnel used to carry the VC.
                ''',
                'cpwvcinboundmode',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcInboundOperStatus', REFERENCE_ENUM_CLASS, 'CpwoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwoperstatusEnum', 
                [], [], 
                '''                Indicates the actual operational status of this VC in the  
                inbound direction. 
                
                - down:           if PW signaling has not yet finished, or 
                                  indications available at the service  
                                  level indicate that the VC is not  
                                  passing packets. 
                - testing:        if AdminStatus at the VC level is set to  
                                  test. 
                - dormant:        The VC is not available because of the 
                                  required resources are occupied VC with  
                                  higher priority VCs . 
                - notPresent:     Some component is missing to accomplish  
                                  the set up of the VC. 
                - lowerLayerDown: The underlying PSN is not in OperStatus  
                                  'up'.  
                ''',
                'cpwvcinboundoperstatus',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcInboundVcLabel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC label used in the inbound direction (i.e. packets  
                received from the PSN. It may be set up manually if owner 
                is 'manual' or automatically otherwise.  
                Examples: For MPLS PSN, it represents the 20 bits of VC 
                tag, for L2TP it represent the 32 bits Session ID. 
                If the label is not yet known (signaling in process), the  
                object should return a value of 0xFFFF.
                ''',
                'cpwvcinboundvclabel',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcLocalGroupID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used in the Group ID field sent to the peer PWES  
                within the maintenance protocol used for VC setup,  
                zero if not used.
                ''',
                'cpwvclocalgroupid',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcLocalIfMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If not equal zero, the optional IfMtu object in the  
                maintenance protocol will be sent with this value,  
                representing the locally supported MTU size over the  
                interface (or the virtual interface) associated with the  
                VC.
                ''',
                'cpwvclocalifmtu',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcLocalIfString', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Each VC is associated to an interface (or a virtual  
                interface) in the ifTable of the node as part of the 
                service configuration. This object defines if the  
                maintenance protocol will send the interface's name as 
                appears on the ifTable in the name object as part of the 
                maintenance protocol. If set to false, the optional element 
                will not be sent.
                ''',
                'cpwvclocalifstring',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The canonical name assigned to the VC.
                ''',
                'cpwvcname',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcOperStatus', REFERENCE_ENUM_CLASS, 'CpwoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwoperstatusEnum', 
                [], [], 
                '''                Indicates the actual combined operational status of this  
                VC. It is 'up' if both cpwVcInboundOperStatus and  
                cpwVcOutboundOperStatus are in 'up' state. For all other  
                values, if the VCs in both directions are of the same 
                value it reflects that value, otherwise it is set to the 
                most severe status out of the two statuses. The order of  
                severance from most severe to less severe is: unknown,  
                notPresent, down, lowerLayerDown, dormant, testing, up. 
                The operator may consult the per direction OperStatus for 
                fault isolation per direction.
                ''',
                'cpwvcoperstatus',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcOutboundOperStatus', REFERENCE_ENUM_CLASS, 'CpwoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwoperstatusEnum', 
                [], [], 
                '''                Indicates the actual operational status of this VC in the  
                outbound direction 
                - down:           if PW signaling has not yet finished, or 
                                  indications available at the service  
                                  level indicate that the VC is not 
                                  passing packets. 
                - testing:        if AdminStatus at the VC level is set to  
                                  test. 
                - dormant:        The VC is not available because of the 
                                  required resources are occupied VC with  
                                  higher priority VCs . 
                - notPresent:     Some component is missing to accomplish  
                                  the set up of the VC. 
                - lowerLayerDown: The underlying PSN is not in OperStatus  
                                  'up'.  
                ''',
                'cpwvcoutboundoperstatus',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcOutboundVcLabel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC label used in the outbound direction (i.e. toward  
                the PSN). It may be set up manually if owner is 'manual' or  
                automatically otherwise. Examples: For MPLS PSN, it  
                represents the 20 bits of VC tag, for L2TP it represent the 
                32 bits Session ID. 
                If the label is not yet known (signaling in process), the  
                object should return a value of 0xFFFF.
                ''',
                'cpwvcoutboundvclabel',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcOwner', REFERENCE_ENUM_CLASS, 'CpwvcownerEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcownerEnum', 
                [], [], 
                '''                Set by the operator to indicate the protocol responsible  
                for establishing this VC. Value 'manual' is used in all 
                cases where no maintenance protocol (PW signaling) is used  
                to set-up the VC, i.e. require configuration of entries in 
                the VC tables including VC labels, etc. The value  
                'maintenanceProtocol' is used in case of standard 
                signaling of the VC for the specific PSN, for example LDP 
                for MPLS PSN as specified in <draft- draft-martini- 
                l2circuit-trans-mpls> or L2TP control protocol.  
                Value 'other' is used for other types of signaling.
                ''',
                'cpwvcowner',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPeerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object contains the value of of the peer node address 
                of the PW/PE maintenance protocol entity. This object  
                should contain a value of 0 if not relevant (manual  
                configuration of the VC).
                ''',
                'cpwvcpeeraddr',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPeerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Denotes the address type of the peer node maintenance 
                protocol (signaling) address if PW maintenance protocol is 
                used for the VC creation. It should be set to  
                'unknown' if PE/PW maintenance protocol is not used,  
                i.e. cpwVcOwner is set to 'manual'. 
                ''',
                'cpwvcpeeraddrtype',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPsnType', REFERENCE_ENUM_CLASS, 'CpwvcpsntypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcpsntypeEnum', 
                [], [], 
                '''                Set by the operator to indicate the PSN type on which this  
                VC will be carried. Based on this object, the relevant PSN  
                table entries are created in the in the PSN specific MIB  
                modules. For example, if mpls(1) is defined, the agent  
                create an entry in cpwVcMplsTable, which further define the  
                MPLS PSN configuration. 
                Note: the exact set of PSN types is yet to be worked  
                out by the WG. 
                ''',
                'cpwvcpsntype',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcRemoteControlWord', REFERENCE_ENUM_CLASS, 'CpwvcremotecontrolwordEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry.CpwvcremotecontrolwordEnum', 
                [], [], 
                '''                If maintenance protocol is used for VC establishment, this  
                parameter indicates the received status of the control word  
                usage, i.e. if packets will be received with control word 
                or not. The value of 'notYetKnown' is used while the 
                maintenance protocol has not yet received the indication  
                from the remote node. 
                In manual configuration of the VC this parameters indicate  
                to the local node what is the expected encapsulation for 
                the received packets. 
                ''',
                'cpwvcremotecontrolword',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcRemoteGroupID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Obtained from the Group ID field as received via the  
                maintenance protocol used for VC setup, zero if not used.  
                Value of 0xFFFF shall be used if the object is yet to be  
                defined by the VC maintenance protocol.
                ''',
                'cpwvcremotegroupid',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcRemoteIfMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remote interface MTU as (optionally) received from the 
                remote node via the maintenance protocol. Should be zero if 
                this parameter is not available or not used.
                ''',
                'cpwvcremoteifmtu',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcRemoteIfString', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Indicate the interface description string as received by 
                the maintenance protocol, MUST be NULL string if not  
                applicable or not known yet.
                ''',
                'cpwvcremoteifstring',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                ''',
                'cpwvcrowstatus',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcSetUpPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                This object define the relative set-up priority of the VC   
                in a lowest-to-highest fashion, where 0 is the highest  
                priority. VCs with the same priority are treated with 
                equal priority. Dropped VC will be set 'dormant' (as 
                indicated in cpwVcOperStatus). 
                This value is significant if there are competing resources 
                between VCs and the implementation support this feature. 
                If not supported or not relevant, the value of zero MUST 
                be used.
                ''',
                'cpwvcsetuppriority',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This variable indicates the storage type for this 
                object.
                ''',
                'cpwvcstoragetype',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('1', '900')], [], 
                '''                The number of seconds, including partial seconds, 
                that have elapsed since the beginning of the current 
                measurement period. If, for some reason, such as an 
                adjustment in the system's time-of-day clock, the 
                current interval exceeds the maximum value, the 
                agent will return the maximum value.
                ''',
                'cpwvctimeelapsed',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcType', REFERENCE_ENUM_CLASS, 'CpwvctypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwvctypeEnum', 
                [], [], 
                '''                This value indicate the service to be carried over 
                this VC.  
                Note: the exact set of VC types is yet to be worked  
                out by the WG. 
                ''',
                'cpwvctype',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of consecutive ticks this VC has been 'up' in 
                both directions together (i.e. 'up' is observed in  
                cpwVcOperStatus.)
                ''',
                'cpwvcuptime',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcValidIntervals', ATTRIBUTE, 'int' , None, None, 
                [('0', '96')], [], 
                '''                The number of previous 15-minute intervals 
                for which data was collected.  
                An agent with PW capability must be capable of supporting at  
                least n intervals. The minimum value of n is 4, The default  
                of n is 32 and the maximum value of n is 96. 
                The value will be <n> unless the measurement was (re-)  
                started within the last (<n>*15) minutes, in which case the  
                value will be the number of complete 15 minute intervals for  
                which the agent has at least some data. In certain cases  
                (e.g., in the case where the agent is a proxy) it is  
                possible that some intervals are unavailable.  In this case,  
                this interval is the maximum interval number for which data  
                is available. 
                ''',
                'cpwvcvalidintervals',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvctable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvctable',
            False, 
            [
            _MetaInfoClassMember('cpwVcEntry', REFERENCE_LIST, 'Cpwvcentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable.Cpwvcentry', 
                [], [], 
                '''                A row in this table represents an emulated virtual 
                connection (VC) across a packet network. It is indexed by 
                cpwVcIndex, which uniquely identifying a singular  
                connection. 
                ''',
                'cpwvcentry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPerfCurrentInHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes received 
                by the VC (from the PSN) in the current 15 minute 
                interval.
                ''',
                'cpwvcperfcurrentinhcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfCurrentInHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets received 
                by the VC (from the PSN) in the current 15 minute 
                interval.
                ''',
                'cpwvcperfcurrentinhcpackets',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfCurrentOutHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes forwarded 
                by the VC (to the PSN) in the current 15 minute interval.
                ''',
                'cpwvcperfcurrentouthcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfCurrentOutHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets forwarded 
                by the VC (to the PSN) in the current 15 minute interval.
                ''',
                'cpwvcperfcurrentouthcpackets',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfCurrentEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperfcurrenttable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperfcurrenttable',
            False, 
            [
            _MetaInfoClassMember('cpwVcPerfCurrentEntry', REFERENCE_LIST, 'Cpwvcperfcurrententry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry', 
                [], [], 
                '''                An entry in this table is created by the agent for 
                every VC.
                ''',
                'cpwvcperfcurrententry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfCurrentTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPerfIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '96')], [], 
                '''                A number N, between 1 and 96, which identifies the 
                interval for which the set of statistics is available. 
                The interval identified by 1 is the most recently 
                completed 15 minute interval, and the interval identified 
                by N is the interval immediately preceding the one 
                identified by N-1. 
                The minimum range of N is 1 through 4. The default range 
                is 1 to 32. The maximum range of N is 1 through 96. 
                ''',
                'cpwvcperfintervalnumber',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPerfIntervalInHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes received by the  
                VC (from the PSN) in a particular 15-minute interval.
                ''',
                'cpwvcperfintervalinhcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalInHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets received by 
                the VC (from the PSN) in a particular 15-minute interval.
                ''',
                'cpwvcperfintervalinhcpackets',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalOutHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes forwarded by the  
                VC (to the PSN) in a particular 15-minute interval.
                ''',
                'cpwvcperfintervalouthcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalOutHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets forwarded by  
                the VC (to the PSN) in a particular 15-minute interval.
                ''',
                'cpwvcperfintervalouthcpackets',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The duration of a particular interval in seconds. 
                Adjustments in the system's time-of-day clock, may 
                cause the interval to be greater or less than the 
                normal value. Therefore this actual interval value 
                is provided.
                ''',
                'cpwvcperfintervaltimeelapsed',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates if the data for this interval 
                is valid.
                ''',
                'cpwvcperfintervalvaliddata',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfIntervalEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperfintervaltable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperfintervaltable',
            False, 
            [
            _MetaInfoClassMember('cpwVcPerfIntervalEntry', REFERENCE_LIST, 'Cpwvcperfintervalentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry', 
                [], [], 
                '''                An entry in this table is created agent for every VC.
                ''',
                'cpwvcperfintervalentry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfIntervalTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cpwvcindex',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPerfTotalDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at 
                which any one or more of this row Counter32 or 
                Counter64 suffered a discontinuity. If no such 
                discontinuities have occurred since the last re- 
                initialization of the local management subsystem, then 
                this object contains a zero value.
                ''',
                'cpwvcperftotaldiscontinuitytime',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalInHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes received by the  
                VC (from the PSN).
                ''',
                'cpwvcperftotalinhcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalInHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets received by the  
                VC (from the PSN).
                ''',
                'cpwvcperftotalinhcpackets',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalOutHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes forwarded by the  
                VC (to the PSN).
                ''',
                'cpwvcperftotalouthcbytes',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalOutHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets forwarded by  
                the VC (to the PSN).
                ''',
                'cpwvcperftotalouthcpackets',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfTotalEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcperftotaltable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcperftotaltable',
            False, 
            [
            _MetaInfoClassMember('cpwVcPerfTotalEntry', REFERENCE_LIST, 'Cpwvcperftotalentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry', 
                [], [], 
                '''                An entry in this table is created agent for every VC.
                ''',
                'cpwvcperftotalentry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPerfTotalTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcIdMappingVcType', REFERENCE_ENUM_CLASS, 'CpwvctypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwvctypeEnum', 
                [], [], 
                '''                The VC type (indicate the service) of this VC.
                ''',
                'cpwvcidmappingvctype',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcIdMappingVcID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC ID of this VC. Zero if the VC is configured  
                manually.
                ''',
                'cpwvcidmappingvcid',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcIdMappingPeerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                IP address type of the peer node.
                ''',
                'cpwvcidmappingpeeraddrtype',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcIdMappingPeerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                IP address type of the peer node.
                ''',
                'cpwvcidmappingpeeraddr',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcIdMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcidmappingvcindex',
                'CISCO-IETF-PW-MIB', True),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcIdMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcidmappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcidmappingtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcIdMappingEntry', REFERENCE_LIST, 'Cpwvcidmappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry', 
                [], [], 
                '''                An entry in this table is created by the agent for every  
                VC configured by the cpwVcTable.
                ''',
                'cpwvcidmappingentry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcIdMappingTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry',
            False, 
            [
            _MetaInfoClassMember('cpwVcPeerMappingPeerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                IP address type of the peer node.
                ''',
                'cpwvcpeermappingpeeraddrtype',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPeerMappingPeerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                IP address type of the peer node.
                ''',
                'cpwvcpeermappingpeeraddr',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPeerMappingVcType', REFERENCE_ENUM_CLASS, 'CpwvctypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB', 'CpwvctypeEnum', 
                [], [], 
                '''                The VC type (indicate the service) of this VC.
                ''',
                'cpwvcpeermappingvctype',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPeerMappingVcID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC ID of this VC. Zero if the VC is configured  
                manually.
                ''',
                'cpwvcpeermappingvcid',
                'CISCO-IETF-PW-MIB', True),
            _MetaInfoClassMember('cpwVcPeerMappingVcIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value that represent the VC in the cpwVcTable.
                ''',
                'cpwvcpeermappingvcindex',
                'CISCO-IETF-PW-MIB', True),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPeerMappingEntry',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib.Cpwvcpeermappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib.Cpwvcpeermappingtable',
            False, 
            [
            _MetaInfoClassMember('cpwVcPeerMappingEntry', REFERENCE_LIST, 'Cpwvcpeermappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry', 
                [], [], 
                '''                An entry in this table is created by the agent for every  
                VC configured in cpwVcTable.
                ''',
                'cpwvcpeermappingentry',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'cpwVcPeerMappingTable',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
    'CiscoIetfPwMib' : {
        'meta_info' : _MetaInfoClass('CiscoIetfPwMib',
            False, 
            [
            _MetaInfoClassMember('cpwVcIdMappingTable', REFERENCE_CLASS, 'Cpwvcidmappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcidmappingtable', 
                [], [], 
                '''                This table provides reverse mapping of the existing VCs  
                based on vc type and VC ID ordering. This table is  
                typically useful for EMS ordered query of existing VCs.
                ''',
                'cpwvcidmappingtable',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcObjects', REFERENCE_CLASS, 'Cpwvcobjects' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcobjects', 
                [], [], 
                '''                ''',
                'cpwvcobjects',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPeerMappingTable', REFERENCE_CLASS, 'Cpwvcpeermappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcpeermappingtable', 
                [], [], 
                '''                This table provides reverse mapping of the existing VCs  
                based on vc type and VC ID ordering. This table is  
                typically useful for EMS ordered query of existing VCs.
                ''',
                'cpwvcpeermappingtable',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfCurrentTable', REFERENCE_CLASS, 'Cpwvcperfcurrenttable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperfcurrenttable', 
                [], [], 
                '''                This table provides per-VC performance information for the  
                current interval.
                ''',
                'cpwvcperfcurrenttable',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfIntervalTable', REFERENCE_CLASS, 'Cpwvcperfintervaltable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperfintervaltable', 
                [], [], 
                '''                This table provides per-VC performance information for  
                each interval.
                ''',
                'cpwvcperfintervaltable',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcPerfTotalTable', REFERENCE_CLASS, 'Cpwvcperftotaltable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvcperftotaltable', 
                [], [], 
                '''                This table provides per-VC Performance information from VC  
                start time.
                ''',
                'cpwvcperftotaltable',
                'CISCO-IETF-PW-MIB', False),
            _MetaInfoClassMember('cpwVcTable', REFERENCE_CLASS, 'Cpwvctable' , 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB', 'CiscoIetfPwMib.Cpwvctable', 
                [], [], 
                '''                This table specifies information for connecting various 
                emulated services to various tunnel type.
                ''',
                'cpwvctable',
                'CISCO-IETF-PW-MIB', False),
            ],
            'CISCO-IETF-PW-MIB',
            'CISCO-IETF-PW-MIB',
            _yang_ns._namespaces['CISCO-IETF-PW-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IETF_PW_MIB'
        ),
    },
}
_meta_table['CiscoIetfPwMib.Cpwvctable.Cpwvcentry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvctable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperfcurrenttable.Cpwvcperfcurrententry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvcperfcurrenttable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperfintervaltable.Cpwvcperfintervalentry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvcperfintervaltable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperftotaltable.Cpwvcperftotalentry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvcperftotaltable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcidmappingtable.Cpwvcidmappingentry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvcidmappingtable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcpeermappingtable.Cpwvcpeermappingentry']['meta_info'].parent =_meta_table['CiscoIetfPwMib.Cpwvcpeermappingtable']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcobjects']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvctable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperfcurrenttable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperfintervaltable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcperftotaltable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcidmappingtable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']
_meta_table['CiscoIetfPwMib.Cpwvcpeermappingtable']['meta_info'].parent =_meta_table['CiscoIetfPwMib']['meta_info']

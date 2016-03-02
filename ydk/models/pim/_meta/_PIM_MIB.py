


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'PIMMIB.Pim' : {
        'meta_info' : _MetaInfoClass('PIMMIB.Pim',
            False, 
            [
            _MetaInfoClassMember('pimJoinPruneInterval', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The default interval at which periodic PIM-SM Join/Prune
                messages are to be sent.
                ''',
                'pimjoinpruneinterval',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pim',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimCandidateRPTable.PimCandidateRPEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimCandidateRPTable.PimCandidateRPEntry',
            False, 
            [
            _MetaInfoClassMember('pimCandidateRPGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group address which, when combined with
                pimCandidateRPGroupMask, identifies a group prefix for which
                the local router will advertise itself as a Candidate-RP.
                ''',
                'pimcandidaterpgroupaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimCandidateRPGroupMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The multicast group address mask which, when combined with
                pimCandidateRPGroupMask, identifies a group prefix for which
                the local router will advertise itself as a Candidate-RP.
                ''',
                'pimcandidaterpgroupmask',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimCandidateRPAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The (unicast) address of the interface which will be
                
                
                
                
                
                advertised as a Candidate-RP.
                ''',
                'pimcandidaterpaddress',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimCandidateRPRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.
                ''',
                'pimcandidaterprowstatus',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimCandidateRPEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimCandidateRPTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimCandidateRPTable',
            False, 
            [
            _MetaInfoClassMember('pimCandidateRPEntry', REFERENCE_LIST, 'PimCandidateRPEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimCandidateRPTable.PimCandidateRPEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimCandidateRPTable.
                ''',
                'pimcandidaterpentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimCandidateRPTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimComponentTable.PimComponentEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimComponentTable.PimComponentEntry',
            False, 
            [
            _MetaInfoClassMember('pimComponentIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                A number uniquely identifying the component.  Each protocol
                instance connected to a separate domain should have a
                different index value.  Routers that only support membership
                in a single PIM-SM domain should use a pimComponentIndex
                value of 1.
                ''',
                'pimcomponentindex',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimComponentBSRAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the bootstrap router (BSR) for the local
                PIM region.
                ''',
                'pimcomponentbsraddress',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimComponentBSRExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum time remaining before the bootstrap router in
                the local domain will be declared down.  For candidate BSRs,
                this is the time until the component sends an RP-Set
                message.  For other routers, this is the time until it may
                accept an RP-Set message from a lower candidate BSR.
                ''',
                'pimcomponentbsrexpirytime',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimComponentCRPHoldTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The holdtime of the component when it is a candidate RP in
                the local domain.  The value of 0 is used to indicate that
                the local system is not a Candidate-RP.
                ''',
                'pimcomponentcrpholdtime',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimComponentStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this entry.  Creating the entry creates
                another protocol instance; destroying the entry disables a
                protocol instance.
                ''',
                'pimcomponentstatus',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimComponentEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimComponentTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimComponentTable',
            False, 
            [
            _MetaInfoClassMember('pimComponentEntry', REFERENCE_LIST, 'PimComponentEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimComponentTable.PimComponentEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimComponentTable.
                ''',
                'pimcomponententry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimComponentTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode_Enum' : _MetaInfoEnum('PimInterfaceMode_Enum', 'ydk.models.pim.PIM_MIB',
        {
            'dense':'DENSE',
            'sparse':'SPARSE',
            'sparseDense':'SPARSEDENSE',
        }, 'PIM-MIB', _yang_ns._namespaces['PIM-MIB']),
    'PIMMIB.PimInterfaceTable.PimInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimInterfaceTable.PimInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('pimInterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex value of this PIM interface.
                ''',
                'piminterfaceifindex',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimInterfaceAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the PIM interface.
                ''',
                'piminterfaceaddress',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceCBSRPreference', ATTRIBUTE, 'int' , None, None, 
                [(-1, 255)], [], 
                '''                The preference value for the local interface as a candidate
                bootstrap router.  The value of -1 is used to indicate that
                the local interface is not a candidate BSR interface.
                ''',
                'piminterfacecbsrpreference',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceDR', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Designated Router on this PIM interface.  For point-to-
                point interfaces, this object has the value 0.0.0.0.
                ''',
                'piminterfacedr',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The frequency at which PIM Hello messages are transmitted
                on this interface.
                ''',
                'piminterfacehellointerval',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceJoinPruneInterval', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The frequency at which PIM Join/Prune messages are
                transmitted on this PIM interface.  The default value of
                this object is the pimJoinPruneInterval.
                ''',
                'piminterfacejoinpruneinterval',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceMode', REFERENCE_ENUM_CLASS, 'PimInterfaceMode_Enum' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode_Enum', 
                [], [], 
                '''                The configured mode of this PIM interface.  A value of
                sparseDense is only valid for PIMv1.
                ''',
                'piminterfacemode',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceNetMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The network mask for the IP address of the PIM interface.
                ''',
                'piminterfacenetmask',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this entry.  Creating the entry enables PIM
                on the interface; destroying the entry disables PIM on the
                interface.
                ''',
                'piminterfacestatus',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimInterfaceEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimInterfaceTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('pimInterfaceEntry', REFERENCE_LIST, 'PimInterfaceEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimInterfaceTable.PimInterfaceEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimInterfaceTable.
                ''',
                'piminterfaceentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimInterfaceTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason_Enum' : _MetaInfoEnum('PimIpMRouteNextHopPruneReason_Enum', 'ydk.models.pim.PIM_MIB',
        {
            'other':'OTHER',
            'prune':'PRUNE',
            'assert':'ASSERT',
        }, 'PIM-MIB', _yang_ns._namespaces['PIM-MIB']),
    'PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteNextHopAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutenexthopaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopGroup', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutenexthopgroup',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ipmroutenexthopifindex',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutenexthopsource',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteNextHopSourceMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutenexthopsourcemask',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimIpMRouteNextHopPruneReason', REFERENCE_ENUM_CLASS, 'PimIpMRouteNextHopPruneReason_Enum' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason_Enum', 
                [], [], 
                '''                This object indicates why the downstream interface was
                pruned, whether in response to a PIM prune message or due to
                PIM Assert processing.
                ''',
                'pimipmroutenexthopprunereason',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimIpMRouteNextHopEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimIpMRouteNextHopTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimIpMRouteNextHopTable',
            False, 
            [
            _MetaInfoClassMember('pimIpMRouteNextHopEntry', REFERENCE_LIST, 'PimIpMRouteNextHopEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimIpMRouteNextHopTable.
                There is one entry per entry in the ipMRouteNextHopTable
                whose interface is running PIM and whose
                ipMRouteNextHopState is pruned(1).
                ''',
                'pimipmroutenexthopentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimIpMRouteNextHopTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimIpMRouteTable.PimIpMRouteEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimIpMRouteTable.PimIpMRouteEntry',
            False, 
            [
            _MetaInfoClassMember('ipMRouteGroup', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutegroup',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutesource',
                'PIM-MIB', True),
            _MetaInfoClassMember('ipMRouteSourceMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ''',
                'ipmroutesourcemask',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimIpMRouteAssertMetric', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The metric advertised by the assert winner on the upstream
                interface, or 0 if no such assert is in received.
                ''',
                'pimipmrouteassertmetric',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteAssertMetricPref', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The preference advertised by the assert winner on the
                upstream interface, or 0 if no such assert is in effect.
                ''',
                'pimipmrouteassertmetricpref',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteAssertRPTBit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of the RPT-bit advertised by the assert winner on
                the upstream interface, or false if no such assert is in
                effect.
                ''',
                'pimipmrouteassertrptbit',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteFlags', ATTRIBUTE, 'str' , None, None, 
                [(1, None)], [], 
                '''                This object describes PIM-specific flags related to a
                multicast state entry.  See the PIM Sparse Mode
                specification for the meaning of the RPT and SPT bits.
                ''',
                'pimipmrouteflags',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteUpstreamAssertTimer', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time remaining before the router changes its upstream
                neighbor back to its RPF neighbor.  This timer is called the
                Assert timer in the PIM Sparse and Dense mode specification.
                
                
                
                
                
                A value of 0 indicates that no Assert has changed the
                upstream neighbor away from the RPF neighbor.
                ''',
                'pimipmrouteupstreamasserttimer',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimIpMRouteEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimIpMRouteTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimIpMRouteTable',
            False, 
            [
            _MetaInfoClassMember('pimIpMRouteEntry', REFERENCE_LIST, 'PimIpMRouteEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimIpMRouteTable.PimIpMRouteEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimIpMRouteTable.  There
                is one entry per entry in the ipMRouteTable whose incoming
                interface is running PIM.
                ''',
                'pimipmrouteentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimIpMRouteTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimNeighborTable.PimNeighborEntry.PimNeighborMode_Enum' : _MetaInfoEnum('PimNeighborMode_Enum', 'ydk.models.pim.PIM_MIB',
        {
            'dense':'DENSE',
            'sparse':'SPARSE',
        }, 'PIM-MIB', _yang_ns._namespaces['PIM-MIB']),
    'PIMMIB.PimNeighborTable.PimNeighborEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimNeighborTable.PimNeighborEntry',
            False, 
            [
            _MetaInfoClassMember('pimNeighborAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the PIM neighbor for which this entry
                contains information.
                ''',
                'pimneighboraddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimNeighborExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum time remaining before this PIM neighbor will be
                aged out.
                ''',
                'pimneighborexpirytime',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimNeighborIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The value of ifIndex for the interface used to reach this
                PIM neighbor.
                ''',
                'pimneighborifindex',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimNeighborMode', REFERENCE_ENUM_CLASS, 'PimNeighborMode_Enum' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimNeighborTable.PimNeighborEntry.PimNeighborMode_Enum', 
                [], [], 
                '''                The active PIM mode of this neighbor.  This object is
                deprecated for PIMv2 routers since all neighbors on the
                interface must be either dense or sparse as determined by
                the protocol running on the interface.
                ''',
                'pimneighbormode',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimNeighborUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time since this PIM neighbor (last) became a neighbor
                of the local router.
                ''',
                'pimneighboruptime',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimNeighborEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimNeighborTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimNeighborTable',
            False, 
            [
            _MetaInfoClassMember('pimNeighborEntry', REFERENCE_LIST, 'PimNeighborEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimNeighborTable.PimNeighborEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimNeighborTable.
                ''',
                'pimneighborentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimNeighborTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimRPSetTable.PimRPSetEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimRPSetTable.PimRPSetEntry',
            False, 
            [
            _MetaInfoClassMember('pimRPSetAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the Candidate-RP.
                ''',
                'pimrpsetaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPSetComponent', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                 A number uniquely identifying the component.  Each
                protocol instance connected to a separate domain should have
                a different index value.
                ''',
                'pimrpsetcomponent',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPSetGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group address which, when combined with
                pimRPSetGroupMask, gives the group prefix for which this
                entry contains information about the Candidate-RP.
                ''',
                'pimrpsetgroupaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPSetGroupMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The multicast group address mask which, when combined with
                pimRPSetGroupAddress, gives the group prefix for which this
                entry contains information about the Candidate-RP.
                ''',
                'pimrpsetgroupmask',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPSetExpiryTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum time remaining before the Candidate-RP will be
                declared down.  If the local router is not the BSR, this
                value is 0.
                ''',
                'pimrpsetexpirytime',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPSetHoldTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The holdtime of a Candidate-RP.  If the local router is not
                the BSR, this value is 0.
                ''',
                'pimrpsetholdtime',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimRPSetEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimRPSetTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimRPSetTable',
            False, 
            [
            _MetaInfoClassMember('pimRPSetEntry', REFERENCE_LIST, 'PimRPSetEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimRPSetTable.PimRPSetEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimRPSetTable.
                ''',
                'pimrpsetentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimRPSetTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimRPTable.PimRPEntry.PimRPState_Enum' : _MetaInfoEnum('PimRPState_Enum', 'ydk.models.pim.PIM_MIB',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'PIM-MIB', _yang_ns._namespaces['PIM-MIB']),
    'PIMMIB.PimRPTable.PimRPEntry' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimRPTable.PimRPEntry',
            False, 
            [
            _MetaInfoClassMember('pimRPAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The unicast address of the RP.
                ''',
                'pimrpaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP multicast group address for which this entry
                contains information about an RP.
                ''',
                'pimrpgroupaddress',
                'PIM-MIB', True),
            _MetaInfoClassMember('pimRPLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time when the corresponding
                instance of pimRPState last changed its value.
                ''',
                'pimrplastchange',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this row, by which new entries may be
                created, or old entries deleted from this table.
                ''',
                'pimrprowstatus',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPState', REFERENCE_ENUM_CLASS, 'PimRPState_Enum' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimRPTable.PimRPEntry.PimRPState_Enum', 
                [], [], 
                '''                The state of the RP.
                ''',
                'pimrpstate',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPStateTimer', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The minimum time remaining before the next state change.
                When pimRPState is up, this is the minimum time which must
                expire until it can be declared down.  When pimRPState is
                down, this is the time until it will be declared up (in
                order to retry).
                ''',
                'pimrpstatetimer',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimRPEntry',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB.PimRPTable' : {
        'meta_info' : _MetaInfoClass('PIMMIB.PimRPTable',
            False, 
            [
            _MetaInfoClassMember('pimRPEntry', REFERENCE_LIST, 'PimRPEntry' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimRPTable.PimRPEntry', 
                [], [], 
                '''                An entry (conceptual row) in the pimRPTable.  There is one
                entry per RP address for each IP multicast group.
                ''',
                'pimrpentry',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'pimRPTable',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
    'PIMMIB' : {
        'meta_info' : _MetaInfoClass('PIMMIB',
            False, 
            [
            _MetaInfoClassMember('pim', REFERENCE_CLASS, 'Pim' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.Pim', 
                [], [], 
                '''                ''',
                'pim',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimCandidateRPTable', REFERENCE_CLASS, 'PimCandidateRPTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimCandidateRPTable', 
                [], [], 
                '''                The (conceptual) table listing the IP multicast groups for
                which the local router is to advertise itself as a
                Candidate-RP when the value of pimComponentCRPHoldTime is
                non-zero.  If this table is empty, then the local router
                
                
                
                
                
                will advertise itself as a Candidate-RP for all groups
                (providing the value of pimComponentCRPHoldTime is non-
                zero).
                ''',
                'pimcandidaterptable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimComponentTable', REFERENCE_CLASS, 'PimComponentTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimComponentTable', 
                [], [], 
                '''                The (conceptual) table containing objects specific to a PIM
                domain.  One row exists for each domain to which the router
                is connected.  A PIM-SM domain is defined as an area of the
                network over which Bootstrap messages are forwarded.
                Typically, a PIM-SM router will be a member of exactly one
                domain.  This table also supports, however, routers which
                may form a border between two PIM-SM domains and do not
                forward Bootstrap messages between them.
                ''',
                'pimcomponenttable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimInterfaceTable', REFERENCE_CLASS, 'PimInterfaceTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimInterfaceTable', 
                [], [], 
                '''                The (conceptual) table listing the router's PIM interfaces.
                IGMP and PIM are enabled on all interfaces listed in this
                table.
                ''',
                'piminterfacetable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteNextHopTable', REFERENCE_CLASS, 'PimIpMRouteNextHopTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimIpMRouteNextHopTable', 
                [], [], 
                '''                The (conceptual) table listing PIM-specific information on
                a subset of the rows of the ipMRouteNextHopTable defined in
                the IP Multicast MIB.
                ''',
                'pimipmroutenexthoptable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimIpMRouteTable', REFERENCE_CLASS, 'PimIpMRouteTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimIpMRouteTable', 
                [], [], 
                '''                The (conceptual) table listing PIM-specific information on
                a subset of the rows of the ipMRouteTable defined in the IP
                Multicast MIB.
                ''',
                'pimipmroutetable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimNeighborTable', REFERENCE_CLASS, 'PimNeighborTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimNeighborTable', 
                [], [], 
                '''                The (conceptual) table listing the router's PIM neighbors.
                ''',
                'pimneighbortable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPSetTable', REFERENCE_CLASS, 'PimRPSetTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimRPSetTable', 
                [], [], 
                '''                The (conceptual) table listing PIM information for
                candidate Rendezvous Points (RPs) for IP multicast groups.
                When the local router is the BSR, this information is
                obtained from received Candidate-RP-Advertisements.  When
                the local router is not the BSR, this information is
                obtained from received RP-Set messages.
                ''',
                'pimrpsettable',
                'PIM-MIB', False),
            _MetaInfoClassMember('pimRPTable', REFERENCE_CLASS, 'PimRPTable' , 'ydk.models.pim.PIM_MIB', 'PIMMIB.PimRPTable', 
                [], [], 
                '''                The (conceptual) table listing PIM version 1 information
                for the Rendezvous Points (RPs) for IP multicast groups.
                This table is deprecated since its function is replaced by
                the pimRPSetTable for PIM version 2.
                ''',
                'pimrptable',
                'PIM-MIB', False),
            ],
            'PIM-MIB',
            'PIM-MIB',
            _yang_ns._namespaces['PIM-MIB'],
        'ydk.models.pim.PIM_MIB'
        ),
    },
}
_meta_table['PIMMIB.PimCandidateRPTable.PimCandidateRPEntry']['meta_info'].parent =_meta_table['PIMMIB.PimCandidateRPTable']['meta_info']
_meta_table['PIMMIB.PimComponentTable.PimComponentEntry']['meta_info'].parent =_meta_table['PIMMIB.PimComponentTable']['meta_info']
_meta_table['PIMMIB.PimInterfaceTable.PimInterfaceEntry']['meta_info'].parent =_meta_table['PIMMIB.PimInterfaceTable']['meta_info']
_meta_table['PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry']['meta_info'].parent =_meta_table['PIMMIB.PimIpMRouteNextHopTable']['meta_info']
_meta_table['PIMMIB.PimIpMRouteTable.PimIpMRouteEntry']['meta_info'].parent =_meta_table['PIMMIB.PimIpMRouteTable']['meta_info']
_meta_table['PIMMIB.PimNeighborTable.PimNeighborEntry']['meta_info'].parent =_meta_table['PIMMIB.PimNeighborTable']['meta_info']
_meta_table['PIMMIB.PimRPSetTable.PimRPSetEntry']['meta_info'].parent =_meta_table['PIMMIB.PimRPSetTable']['meta_info']
_meta_table['PIMMIB.PimRPTable.PimRPEntry']['meta_info'].parent =_meta_table['PIMMIB.PimRPTable']['meta_info']
_meta_table['PIMMIB.Pim']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimCandidateRPTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimComponentTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimInterfaceTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimIpMRouteNextHopTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimIpMRouteTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimNeighborTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimRPSetTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']
_meta_table['PIMMIB.PimRPTable']['meta_info'].parent =_meta_table['PIMMIB']['meta_info']

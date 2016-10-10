
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.afi_safi_in' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.route_type' : {
        'deviation_typ' : 'not_supported',
    },
}

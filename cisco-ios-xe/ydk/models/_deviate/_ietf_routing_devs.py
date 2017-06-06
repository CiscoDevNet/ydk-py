
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.description' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.type' : {
        'deviation_typ' : 'not_supported',
    },
    'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.last_updated' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('last-updated', ATTRIBUTE, 'str' , None, None, 
                    [], [], 
                    '''                    Time stamp of the last modification of the route. If the
                    route was never modified, it is the time when the route was
                    inserted into the RIB.
                    ''',
                    'last_updated',
                    'ietf-routing', False),
            ),
        ]
    },
}

""" CISCO_DYNAMIC_TEMPLATE_TC_MIB 

This MIB module defines textual conventions used by the
CISCO\-DYNAMIC\-TEMPLATE\-MIB and MIB modules that use and expand
on dynamic templates.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Dynamictemplatetargettype(Enum):
    """
    Dynamictemplatetargettype

    An enumerated integer\-value describing the type of target

    associated with one or more dynamic templates\:

        'other'

            The implementation of the MIB module using this textual

            convention does not recognize the type of target.

        'interface'

            The target is a physical, logical, or virtual interface

            represented by an ifEntry (defined by the IF\-MIB).

    An implementation must ensure that DynamicTemplateTargetType

    object and any associated DynamicTemplateTargetId objects are

    consistent.  An attempt to set a DynamicTemplateTargetType

    object to a value inconsistent with the associated

    DynamicTemplateTargetId object must result in a response with

    an

    error\-status of 'inconsistentValue'.

    .. data:: other = 1

    .. data:: interface = 2

    """

    other = Enum.YLeaf(1, "other")

    interface = Enum.YLeaf(2, "interface")


class Dynamictemplatetype(Enum):
    """
    Dynamictemplatetype

    An enumerated integer\-value describing the type of dynamic

    template\:

    'other'

        The implementation of the MIB module using this textual

        convention does not recognize the type of dynamic template.

    'derived'

        A configuration resulting from the union of the attributes

        contained by all the dynamic templates associated with a

        target.  The system generates a derived configuration, and

        an EMS/NMS cannot directly modify it.  An EMS/NMS can only

        affect a derived configuration by modifying one or more of

        the dynamic templates associated with the target.

    'ppp'

        A PPP template is a set of locally\-configured attributes

        relating to the configuration of a PPP interface.

    'ethernet'

        An Ethernet template is a set of locally\-configured

        attributes used by the system to configure dynamic

        interfaces initiated on Ethernet virtual interfaces (e.g.,

        EoMPLS) or automatically created VLANs.

    'ipSubscriber'

        An IP subscriber template is a set of locally\-configured

        attributes used by the system to configure certain types of

        IP and L2 subscriber sessions.

    'service'

        A service template is a set of locally\-configured attributes

        used by the system to configure subscriber sessions.  These

        attributes specifically relate to services, and the system

        applies these attributes in response to subscriber session

        life\-cycle events.

    .. data:: other = 1

    .. data:: derived = 2

    .. data:: ppp = 3

    .. data:: ethernet = 4

    .. data:: ipSubscriber = 5

    .. data:: service = 6

    """

    other = Enum.YLeaf(1, "other")

    derived = Enum.YLeaf(2, "derived")

    ppp = Enum.YLeaf(3, "ppp")

    ethernet = Enum.YLeaf(4, "ethernet")

    ipSubscriber = Enum.YLeaf(5, "ipSubscriber")

    service = Enum.YLeaf(6, "service")




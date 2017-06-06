""" CISCO_DYNAMIC_TEMPLATE_TC_MIB 

This MIB module defines textual conventions used by the
CISCO\-DYNAMIC\-TEMPLATE\-MIB and MIB modules that use and expand
on dynamic templates.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DynamictemplatetargettypeEnum(Enum):
    """
    DynamictemplatetargettypeEnum

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

    other = 1

    interface = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_TC_MIB as meta
        return meta._meta_table['DynamictemplatetargettypeEnum']


class DynamictemplatetypeEnum(Enum):
    """
    DynamictemplatetypeEnum

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

    other = 1

    derived = 2

    ppp = 3

    ethernet = 4

    ipSubscriber = 5

    service = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_DYNAMIC_TEMPLATE_TC_MIB as meta
        return meta._meta_table['DynamictemplatetypeEnum']




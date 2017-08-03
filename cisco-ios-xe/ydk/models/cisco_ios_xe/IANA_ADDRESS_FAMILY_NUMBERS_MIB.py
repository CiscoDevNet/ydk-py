""" IANA_ADDRESS_FAMILY_NUMBERS_MIB 

The MIB module defines the AddressFamilyNumbers
textual convention.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Addressfamilynumbers(Enum):
    """
    Addressfamilynumbers

    The definition of this textual convention with the

    addition of newly assigned values is published

    periodically by the IANA, in either the Assigned

    Numbers RFC, or some derivative of it specific to

    Internet Network Management number assignments.

    (The latest arrangements can be obtained by

    contacting the IANA.)

    The enumerations are described as\:

    other(0),    \-\- none of the following

    ipV4(1),     \-\- IP Version 4

    ipV6(2),     \-\- IP Version 6

    nsap(3),     \-\- NSAP

    hdlc(4),     \-\- (8\-bit multidrop)

    bbn1822(5),

    all802(6),   \-\- (includes all 802 media

                 \-\-   plus Ethernet 'canonical format')

    e163(7),

    e164(8),     \-\- (SMDS, Frame Relay, ATM)

    f69(9),      \-\- (Telex)

    x121(10),    \-\- (X.25, Frame Relay)

    ipx(11),     \-\- IPX (Internet Protocol Exchange)

    appletalk(12),  \-\- Apple Talk

    decnetIV(13),   \-\- DEC Net Phase IV

    banyanVines(14),  \-\- Banyan Vines

    e164withNsap(15),

                 \-\- (E.164 with NSAP format subaddress)

    dns(16),     \-\- (Domain Name System)

    distinguishedname(17), \-\- (Distinguished Name, per X.500)

    asnumber(18), \-\- (16\-bit quantity, per the AS number space)

    reserved(65535)

    Requests for new values should be made to IANA via

    email (iana@iana.org).

    .. data:: other = 0

    .. data:: ipV4 = 1

    .. data:: ipV6 = 2

    .. data:: nsap = 3

    .. data:: hdlc = 4

    .. data:: bbn1822 = 5

    .. data:: all802 = 6

    .. data:: e163 = 7

    .. data:: e164 = 8

    .. data:: f69 = 9

    .. data:: x121 = 10

    .. data:: ipx = 11

    .. data:: appletalk = 12

    .. data:: decnetIV = 13

    .. data:: banyanVines = 14

    .. data:: e164withNsap = 15

    .. data:: dns = 16

    .. data:: distinguishedname = 17

    .. data:: asnumber = 18

    .. data:: xtpoveripv4 = 19

    .. data:: xtpoveripv6 = 20

    .. data:: xtpnativemodextp = 21

    .. data:: reserved = 65535

    """

    other = Enum.YLeaf(0, "other")

    ipV4 = Enum.YLeaf(1, "ipV4")

    ipV6 = Enum.YLeaf(2, "ipV6")

    nsap = Enum.YLeaf(3, "nsap")

    hdlc = Enum.YLeaf(4, "hdlc")

    bbn1822 = Enum.YLeaf(5, "bbn1822")

    all802 = Enum.YLeaf(6, "all802")

    e163 = Enum.YLeaf(7, "e163")

    e164 = Enum.YLeaf(8, "e164")

    f69 = Enum.YLeaf(9, "f69")

    x121 = Enum.YLeaf(10, "x121")

    ipx = Enum.YLeaf(11, "ipx")

    appletalk = Enum.YLeaf(12, "appletalk")

    decnetIV = Enum.YLeaf(13, "decnetIV")

    banyanVines = Enum.YLeaf(14, "banyanVines")

    e164withNsap = Enum.YLeaf(15, "e164withNsap")

    dns = Enum.YLeaf(16, "dns")

    distinguishedname = Enum.YLeaf(17, "distinguishedname")

    asnumber = Enum.YLeaf(18, "asnumber")

    xtpoveripv4 = Enum.YLeaf(19, "xtpoveripv4")

    xtpoveripv6 = Enum.YLeaf(20, "xtpoveripv6")

    xtpnativemodextp = Enum.YLeaf(21, "xtpnativemodextp")

    reserved = Enum.YLeaf(65535, "reserved")




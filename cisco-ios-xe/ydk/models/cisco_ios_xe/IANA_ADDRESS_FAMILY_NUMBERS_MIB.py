""" IANA_ADDRESS_FAMILY_NUMBERS_MIB 

The MIB module defines the AddressFamilyNumbers
textual convention.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AddressfamilynumbersEnum(Enum):
    """
    AddressfamilynumbersEnum

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

    other = 0

    ipV4 = 1

    ipV6 = 2

    nsap = 3

    hdlc = 4

    bbn1822 = 5

    all802 = 6

    e163 = 7

    e164 = 8

    f69 = 9

    x121 = 10

    ipx = 11

    appletalk = 12

    decnetIV = 13

    banyanVines = 14

    e164withNsap = 15

    dns = 16

    distinguishedname = 17

    asnumber = 18

    xtpoveripv4 = 19

    xtpoveripv6 = 20

    xtpnativemodextp = 21

    reserved = 65535


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IANA_ADDRESS_FAMILY_NUMBERS_MIB as meta
        return meta._meta_table['AddressfamilynumbersEnum']




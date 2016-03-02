""" IANA_ADDRESS_FAMILY_NUMBERS_MIB 

The MIB module defines the AddressFamilyNumbers
textual convention.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AddressFamilyNumbers_Enum(Enum):
    """
    AddressFamilyNumbers_Enum

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

    """

    OTHER = 0

    IPV4 = 1

    IPV6 = 2

    NSAP = 3

    HDLC = 4

    BBN1822 = 5

    ALL802 = 6

    E163 = 7

    E164 = 8

    F69 = 9

    X121 = 10

    IPX = 11

    APPLETALK = 12

    DECNETIV = 13

    BANYANVINES = 14

    E164WITHNSAP = 15

    DNS = 16

    DISTINGUISHEDNAME = 17

    ASNUMBER = 18

    XTPOVERIPV4 = 19

    XTPOVERIPV6 = 20

    XTPNATIVEMODEXTP = 21

    RESERVED = 65535


    @staticmethod
    def _meta_info():
        from ydk.models.iana._meta import _IANA_ADDRESS_FAMILY_NUMBERS_MIB as meta
        return meta._meta_table['AddressFamilyNumbers_Enum']




""" CISCO_IETF_PW_TC_MIB 

This MIB Module provides Textual Conventions 
and OBJECT\-IDENTITY Objects to be used PW services.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CpwOperStatus_Enum(Enum):
    """
    CpwOperStatus_Enum

    Indicate the operational status of the PW VC. 
    
    \- up\:             Ready to pass packets.  
    \- down\:           If PW signaling has not yet finished, or 
                      indications available at the service  
                      level indicate that the VC is not  
                      passing packets. 
    \- testing\:        If AdminStatus at the VC level is set to  
                      test. 
    \- dormant\:        The VC is not available because of the 
                      required resources are occupied VC with  
                      higher priority VCs . 
    \- notPresent\:     Some component is missing to accomplish  
                      the set up of the VC. 
    \- lowerLayerDown\: The underlying PSN or outer tunnel is not 
                      in OperStatus 'up'.  

    """

    UP = 1

    DOWN = 2

    TESTING = 3

    UNKNOWN = 4

    DORMANT = 5

    NOTPRESENT = 6

    LOWERLAYERDOWN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_PW_TC_MIB as meta
        return meta._meta_table['CpwOperStatus_Enum']


class CpwVcType_Enum(Enum):
    """
    CpwVcType_Enum

    Indicate the VC type (i.e. the carried service). 
    Note\: the exact set of VC types is yet to be worked  
    out by the WG. 

    """

    OTHER = 0

    FRAMERELAY = 1

    ATMAAL5VCC = 2

    ATMTRANSPARENT = 3

    ETHERNETVLAN = 4

    ETHERNET = 5

    HDLC = 6

    PPP = 7

    CEP = 8

    ATMVCCCELL = 9

    ATMVPCCELL = 10

    ETHERNETVPLS = 11

    E1SATOP = 12

    T1SATOP = 13

    E3SATOP = 14

    T3SATOP = 15

    BASICCESPSN = 16

    BASICTDMIP = 17

    TDMCASCESPSN = 18

    TDMCASTDMIP = 19


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _CISCO_IETF_PW_TC_MIB as meta
        return meta._meta_table['CpwVcType_Enum']




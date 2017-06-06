""" OSPF_TRAP_MIB 

The MIB module to describe traps for the OSPF
Version 2 Protocol.

Copyright (C) The IETF Trust (2006).
This version of this MIB module is part of
RFC 4750;  see the RFC itself for full legal
notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class OspfTrapMib(object):
    """
    
    
    .. attribute:: ospftrapcontrol
    
    	
    	**type**\:   :py:class:`Ospftrapcontrol <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol>`
    
    

    """

    _prefix = 'OSPF-TRAP-MIB'
    _revision = '2006-11-10'

    def __init__(self):
        self.ospftrapcontrol = OspfTrapMib.Ospftrapcontrol()
        self.ospftrapcontrol.parent = self


    class Ospftrapcontrol(object):
        """
        
        
        .. attribute:: ospfconfigerrortype
        
        	Potential types of configuration conflicts. Used by the ospfConfigError and ospfConfigVirtError traps.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:   :py:class:`OspfconfigerrortypeEnum <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol.OspfconfigerrortypeEnum>`
        
        .. attribute:: ospfpacketsrc
        
        	The IP address of an inbound packet that cannot be identified by a neighbor instance.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfpackettype
        
        	OSPF packet types.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:   :py:class:`OspfpackettypeEnum <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol.OspfpackettypeEnum>`
        
        .. attribute:: ospfsettrap
        
        	A 4\-octet string serving as a bit map for the trap events defined by the OSPF traps.  This object is used to enable and disable specific OSPF traps where a 1 in the bit field represents enabled.  The right\-most bit (least significant) represents trap 0.  This object is persistent and when written  the entity SHOULD save the change to non\-volatile storage
        	**type**\:  str
        
        	**length:** 4
        
        

        """

        _prefix = 'OSPF-TRAP-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfconfigerrortype = None
            self.ospfpacketsrc = None
            self.ospfpackettype = None
            self.ospfsettrap = None

        class OspfconfigerrortypeEnum(Enum):
            """
            OspfconfigerrortypeEnum

            Potential types of configuration conflicts.

            Used by the ospfConfigError and

            ospfConfigVirtError traps.  When the last value

            of a trap using this object is needed, but no

            traps of that type have been sent, this value

            pertaining to this object should be returned as

            noError.

            .. data:: badVersion = 1

            .. data:: areaMismatch = 2

            .. data:: unknownNbmaNbr = 3

            .. data:: unknownVirtualNbr = 4

            .. data:: authTypeMismatch = 5

            .. data:: authFailure = 6

            .. data:: netMaskMismatch = 7

            .. data:: helloIntervalMismatch = 8

            .. data:: deadIntervalMismatch = 9

            .. data:: optionMismatch = 10

            .. data:: mtuMismatch = 11

            .. data:: duplicateRouterId = 12

            .. data:: noError = 13

            """

            badVersion = 1

            areaMismatch = 2

            unknownNbmaNbr = 3

            unknownVirtualNbr = 4

            authTypeMismatch = 5

            authFailure = 6

            netMaskMismatch = 7

            helloIntervalMismatch = 8

            deadIntervalMismatch = 9

            optionMismatch = 10

            mtuMismatch = 11

            duplicateRouterId = 12

            noError = 13


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_TRAP_MIB as meta
                return meta._meta_table['OspfTrapMib.Ospftrapcontrol.OspfconfigerrortypeEnum']


        class OspfpackettypeEnum(Enum):
            """
            OspfpackettypeEnum

            OSPF packet types.  When the last value of a trap

            using this object is needed, but no traps of

            that type have been sent, this value pertaining

            to this object should be returned as nullPacket.

            .. data:: hello = 1

            .. data:: dbDescript = 2

            .. data:: lsReq = 3

            .. data:: lsUpdate = 4

            .. data:: lsAck = 5

            .. data:: nullPacket = 6

            """

            hello = 1

            dbDescript = 2

            lsReq = 3

            lsUpdate = 4

            lsAck = 5

            nullPacket = 6


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _OSPF_TRAP_MIB as meta
                return meta._meta_table['OspfTrapMib.Ospftrapcontrol.OspfpackettypeEnum']


        @property
        def _common_path(self):

            return '/OSPF-TRAP-MIB:OSPF-TRAP-MIB/OSPF-TRAP-MIB:ospfTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ospfconfigerrortype is not None:
                return True

            if self.ospfpacketsrc is not None:
                return True

            if self.ospfpackettype is not None:
                return True

            if self.ospfsettrap is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _OSPF_TRAP_MIB as meta
            return meta._meta_table['OspfTrapMib.Ospftrapcontrol']['meta_info']

    @property
    def _common_path(self):

        return '/OSPF-TRAP-MIB:OSPF-TRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ospftrapcontrol is not None and self.ospftrapcontrol._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _OSPF_TRAP_MIB as meta
        return meta._meta_table['OspfTrapMib']['meta_info']



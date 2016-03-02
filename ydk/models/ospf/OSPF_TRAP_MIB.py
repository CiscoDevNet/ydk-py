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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class OSPFTRAPMIB(object):
    """
    
    
    .. attribute:: ospftrapcontrol
    
    	
    	**type**\: :py:class:`OspfTrapControl <ydk.models.ospf.OSPF_TRAP_MIB.OSPFTRAPMIB.OspfTrapControl>`
    
    

    """

    _prefix = 'ospf-trap'
    _revision = '2006-11-10'

    def __init__(self):
        self.ospftrapcontrol = OSPFTRAPMIB.OspfTrapControl()
        self.ospftrapcontrol.parent = self


    class OspfTrapControl(object):
        """
        
        
        .. attribute:: ospfconfigerrortype
        
        	Potential types of configuration conflicts. Used by the ospfConfigError and ospfConfigVirtError traps.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\: :py:class:`OspfConfigErrorType_Enum <ydk.models.ospf.OSPF_TRAP_MIB.OSPFTRAPMIB.OspfTrapControl.OspfConfigErrorType_Enum>`
        
        .. attribute:: ospfpacketsrc
        
        	The IP address of an inbound packet that cannot be identified by a neighbor instance.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfpackettype
        
        	OSPF packet types.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\: :py:class:`OspfPacketType_Enum <ydk.models.ospf.OSPF_TRAP_MIB.OSPFTRAPMIB.OspfTrapControl.OspfPacketType_Enum>`
        
        .. attribute:: ospfsettrap
        
        	A 4\-octet string serving as a bit map for the trap events defined by the OSPF traps.  This object is used to enable and disable specific OSPF traps where a 1 in the bit field represents enabled.  The right\-most bit (least significant) represents trap 0.  This object is persistent and when written  the entity SHOULD save the change to non\-volatile storage
        	**type**\: str
        
        	**range:** 4
        
        

        """

        _prefix = 'ospf-trap'
        _revision = '2006-11-10'

        def __init__(self):
            self.parent = None
            self.ospfconfigerrortype = None
            self.ospfpacketsrc = None
            self.ospfpackettype = None
            self.ospfsettrap = None

        class OspfConfigErrorType_Enum(Enum):
            """
            OspfConfigErrorType_Enum

            Potential types of configuration conflicts.
            Used by the ospfConfigError and
            ospfConfigVirtError traps.  When the last value
            of a trap using this object is needed, but no
            traps of that type have been sent, this value
            pertaining to this object should be returned as
            noError.

            """

            BADVERSION = 1

            AREAMISMATCH = 2

            UNKNOWNNBMANBR = 3

            UNKNOWNVIRTUALNBR = 4

            AUTHTYPEMISMATCH = 5

            AUTHFAILURE = 6

            NETMASKMISMATCH = 7

            HELLOINTERVALMISMATCH = 8

            DEADINTERVALMISMATCH = 9

            OPTIONMISMATCH = 10

            MTUMISMATCH = 11

            DUPLICATEROUTERID = 12

            NOERROR = 13


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_TRAP_MIB as meta
                return meta._meta_table['OSPFTRAPMIB.OspfTrapControl.OspfConfigErrorType_Enum']


        class OspfPacketType_Enum(Enum):
            """
            OspfPacketType_Enum

            OSPF packet types.  When the last value of a trap
            using this object is needed, but no traps of
            that type have been sent, this value pertaining
            to this object should be returned as nullPacket.

            """

            HELLO = 1

            DBDESCRIPT = 2

            LSREQ = 3

            LSUPDATE = 4

            LSACK = 5

            NULLPACKET = 6


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _OSPF_TRAP_MIB as meta
                return meta._meta_table['OSPFTRAPMIB.OspfTrapControl.OspfPacketType_Enum']


        @property
        def _common_path(self):

            return '/OSPF-TRAP-MIB:OSPF-TRAP-MIB/OSPF-TRAP-MIB:ospfTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ospfconfigerrortype is not None:
                return True

            if self.ospfpacketsrc is not None:
                return True

            if self.ospfpackettype is not None:
                return True

            if self.ospfsettrap is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _OSPF_TRAP_MIB as meta
            return meta._meta_table['OSPFTRAPMIB.OspfTrapControl']['meta_info']

    @property
    def _common_path(self):

        return '/OSPF-TRAP-MIB:OSPF-TRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ospftrapcontrol is not None and self.ospftrapcontrol._has_data():
            return True

        if self.ospftrapcontrol is not None and self.ospftrapcontrol.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _OSPF_TRAP_MIB as meta
        return meta._meta_table['OSPFTRAPMIB']['meta_info']



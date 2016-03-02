""" CISCO_OSPF_TRAP_MIB 

This MIB module describes new/modified notification
objects/events, which are defined in the latest
version for OSPF MIB IETF draft
draftietf\-ospf\-mib\-update\-05.txt. Support for OSPF 
Sham link is also added

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOOSPFTRAPMIB(object):
    """
    
    
    .. attribute:: cospftrapcontrol
    
    	
    	**type**\: :py:class:`CospfTrapControl <ydk.models.ospf.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.CospfTrapControl>`
    
    

    """

    _prefix = 'cisco-ospf-trap'
    _revision = '2003-07-18'

    def __init__(self):
        self.cospftrapcontrol = CISCOOSPFTRAPMIB.CospfTrapControl()
        self.cospftrapcontrol.parent = self


    class CospfTrapControl(object):
        """
        
        
        .. attribute:: cospfconfigerrortype
        
        	Potential types of configuration conflicts. Used  by the cospfConfigError and cospfConfigVirtError traps. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\: :py:class:`CospfConfigErrorType_Enum <ydk.models.ospf.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.CospfTrapControl.CospfConfigErrorType_Enum>`
        
        .. attribute:: cospfpacketsrc
        
        	The IP address of an inbound packet that can\- not be identified by a neighbor instance. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: cospfpackettype
        
        	OSPF packet types. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\: :py:class:`CospfPacketType_Enum <ydk.models.ospf.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.CospfTrapControl.CospfPacketType_Enum>`
        
        .. attribute:: cospfsettrap
        
        	An octet string serving as a bit  map  for the trap events defined by the OSPF traps in  this MIB. This object is used to enable and   disable  specific OSPF   traps   where  a  1   in  the  corresponding bit  field represents  enabled
        	**type**\: :py:class:`CospfSetTrap_Bits <ydk.models.ospf.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.CospfTrapControl.CospfSetTrap_Bits>`
        
        

        """

        _prefix = 'cisco-ospf-trap'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfconfigerrortype = None
            self.cospfpacketsrc = None
            self.cospfpackettype = None
            self.cospfsettrap = CISCOOSPFTRAPMIB.CospfTrapControl.CospfSetTrap_Bits()

        class CospfConfigErrorType_Enum(Enum):
            """
            CospfConfigErrorType_Enum

            Potential types of configuration conflicts.
            Used  by the cospfConfigError and cospfConfigVirtError
            traps. When the last value of a trap
            using this object is needed, but no traps of
            that type have been sent, this value pertaining
            to this object should be returned as noError.

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

            NOERROR = 12

            UNKNOWNSHAMLINKNBR = 13


            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_TRAP_MIB as meta
                return meta._meta_table['CISCOOSPFTRAPMIB.CospfTrapControl.CospfConfigErrorType_Enum']


        class CospfPacketType_Enum(Enum):
            """
            CospfPacketType_Enum

            OSPF packet types. When the last value of a trap
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
                from ydk.models.ospf._meta import _CISCO_OSPF_TRAP_MIB as meta
                return meta._meta_table['CISCOOSPFTRAPMIB.CospfTrapControl.CospfPacketType_Enum']


        class CospfSetTrap_Bits(FixedBitsDict):
            """
            CospfSetTrap_Bits

            An octet string serving as a bit  map  for
            the trap events defined by the OSPF traps in 
            this MIB. This object is used to enable and  
            disable  specific OSPF   traps   where  a  1  
            in  the  corresponding bit  field represents 
            enabled.
            Keys are:- shamLinksStateChange , retransmit , ifConfigError , nssaTranslatorStatusChange , shamLinkTxRetransmit , originateLsa , virtIfConfigError , shamLinkConfigError , virtRetransmit , shamLinkNbrStateChange , shamLinkStateChange , originateMaxAgeLsa , shamLinkAuthFailure , shamLinkRxBadPacket

            """

            def __init__(self):
                self._dictionary = { 
                    'shamLinksStateChange':False,
                    'retransmit':False,
                    'ifConfigError':False,
                    'nssaTranslatorStatusChange':False,
                    'shamLinkTxRetransmit':False,
                    'originateLsa':False,
                    'virtIfConfigError':False,
                    'shamLinkConfigError':False,
                    'virtRetransmit':False,
                    'shamLinkNbrStateChange':False,
                    'shamLinkStateChange':False,
                    'originateMaxAgeLsa':False,
                    'shamLinkAuthFailure':False,
                    'shamLinkRxBadPacket':False,
                }
                self._pos_map = { 
                    'shamLinksStateChange':13,
                    'retransmit':2,
                    'ifConfigError':0,
                    'nssaTranslatorStatusChange':6,
                    'shamLinkTxRetransmit':12,
                    'originateLsa':4,
                    'virtIfConfigError':1,
                    'shamLinkConfigError':9,
                    'virtRetransmit':3,
                    'shamLinkNbrStateChange':8,
                    'shamLinkStateChange':7,
                    'originateMaxAgeLsa':5,
                    'shamLinkAuthFailure':10,
                    'shamLinkRxBadPacket':11,
                }

        @property
        def _common_path(self):

            return '/CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB/CISCO-OSPF-TRAP-MIB:cospfTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospfconfigerrortype is not None:
                return True

            if self.cospfpacketsrc is not None:
                return True

            if self.cospfpackettype is not None:
                return True

            if self.cospfsettrap is not None:
                if self.cospfsettrap._has_data():
                    return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_TRAP_MIB as meta
            return meta._meta_table['CISCOOSPFTRAPMIB.CospfTrapControl']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cospftrapcontrol is not None and self.cospftrapcontrol._has_data():
            return True

        if self.cospftrapcontrol is not None and self.cospftrapcontrol.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _CISCO_OSPF_TRAP_MIB as meta
        return meta._meta_table['CISCOOSPFTRAPMIB']['meta_info']



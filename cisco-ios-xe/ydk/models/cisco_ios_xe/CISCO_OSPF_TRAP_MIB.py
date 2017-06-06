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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoOspfTrapMib(object):
    """
    
    
    .. attribute:: cospftrapcontrol
    
    	
    	**type**\:   :py:class:`Cospftrapcontrol <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol>`
    
    

    """

    _prefix = 'CISCO-OSPF-TRAP-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        self.cospftrapcontrol = CiscoOspfTrapMib.Cospftrapcontrol()
        self.cospftrapcontrol.parent = self


    class Cospftrapcontrol(object):
        """
        
        
        .. attribute:: cospfconfigerrortype
        
        	Potential types of configuration conflicts. Used  by the cospfConfigError and cospfConfigVirtError traps. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:   :py:class:`CospfconfigerrortypeEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.CospfconfigerrortypeEnum>`
        
        .. attribute:: cospfpacketsrc
        
        	The IP address of an inbound packet that can\- not be identified by a neighbor instance. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: cospfpackettype
        
        	OSPF packet types. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:   :py:class:`CospfpackettypeEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.CospfpackettypeEnum>`
        
        .. attribute:: cospfsettrap
        
        	An octet string serving as a bit  map  for the trap events defined by the OSPF traps in  this MIB. This object is used to enable and   disable  specific OSPF   traps   where  a  1   in  the  corresponding bit  field represents  enabled
        	**type**\:   :py:class:`Cospfsettrap <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.Cospfsettrap>`
        
        

        """

        _prefix = 'CISCO-OSPF-TRAP-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfconfigerrortype = None
            self.cospfpacketsrc = None
            self.cospfpackettype = None
            self.cospfsettrap = CiscoOspfTrapMib.Cospftrapcontrol.Cospfsettrap()

        class CospfconfigerrortypeEnum(Enum):
            """
            CospfconfigerrortypeEnum

            Potential types of configuration conflicts.

            Used  by the cospfConfigError and cospfConfigVirtError

            traps. When the last value of a trap

            using this object is needed, but no traps of

            that type have been sent, this value pertaining

            to this object should be returned as noError.

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

            .. data:: noError = 12

            .. data:: unknownShamLinkNbr = 13

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

            noError = 12

            unknownShamLinkNbr = 13


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_TRAP_MIB as meta
                return meta._meta_table['CiscoOspfTrapMib.Cospftrapcontrol.CospfconfigerrortypeEnum']


        class CospfpackettypeEnum(Enum):
            """
            CospfpackettypeEnum

            OSPF packet types. When the last value of a trap

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
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_TRAP_MIB as meta
                return meta._meta_table['CiscoOspfTrapMib.Cospftrapcontrol.CospfpackettypeEnum']


        class Cospfsettrap(FixedBitsDict):
            """
            Cospfsettrap

            An octet string serving as a bit  map  for
            the trap events defined by the OSPF traps in 
            this MIB. This object is used to enable and  
            disable  specific OSPF   traps   where  a  1  
            in  the  corresponding bit  field represents 
            enabled.
            Keys are:- nssaTranslatorStatusChange , originateLsa , virtRetransmit , shamLinkTxRetransmit , virtIfConfigError , shamLinkStateChange , shamLinkConfigError , ifConfigError , retransmit , shamLinkAuthFailure , shamLinkNbrStateChange , originateMaxAgeLsa , shamLinkRxBadPacket , shamLinksStateChange

            """

            def __init__(self):
                self._dictionary = { 
                    'nssaTranslatorStatusChange':False,
                    'originateLsa':False,
                    'virtRetransmit':False,
                    'shamLinkTxRetransmit':False,
                    'virtIfConfigError':False,
                    'shamLinkStateChange':False,
                    'shamLinkConfigError':False,
                    'ifConfigError':False,
                    'retransmit':False,
                    'shamLinkAuthFailure':False,
                    'shamLinkNbrStateChange':False,
                    'originateMaxAgeLsa':False,
                    'shamLinkRxBadPacket':False,
                    'shamLinksStateChange':False,
                }
                self._pos_map = { 
                    'nssaTranslatorStatusChange':6,
                    'originateLsa':4,
                    'virtRetransmit':3,
                    'shamLinkTxRetransmit':12,
                    'virtIfConfigError':1,
                    'shamLinkStateChange':7,
                    'shamLinkConfigError':9,
                    'ifConfigError':0,
                    'retransmit':2,
                    'shamLinkAuthFailure':10,
                    'shamLinkNbrStateChange':8,
                    'originateMaxAgeLsa':5,
                    'shamLinkRxBadPacket':11,
                    'shamLinksStateChange':13,
                }

        @property
        def _common_path(self):

            return '/CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB/CISCO-OSPF-TRAP-MIB:cospfTrapControl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_TRAP_MIB as meta
            return meta._meta_table['CiscoOspfTrapMib.Cospftrapcontrol']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cospftrapcontrol is not None and self.cospftrapcontrol._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_TRAP_MIB as meta
        return meta._meta_table['CiscoOspfTrapMib']['meta_info']



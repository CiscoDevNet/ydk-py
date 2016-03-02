""" CISCO_VOICE_COMMON_DIAL_CONTROL_MIB 

This MIB module contains voice related objects that
are common across more than one network
encapsulation i.e VoIP, VoATM and VoFR.

\*\*\* ABBREVIATIONS, ACRONYMS AND SYMBOLS \*\*\*

GSM    \- Global System for Mobile Communication

AMR\-NB \- Adaptive Multi Rate \- Narrow Band

iLBC   \- internet Low Bitrate Codec

iSAC   \- internet Speech Audio Codec

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CvcCoderTypeRate_Enum(Enum):
    """
    CvcCoderTypeRate_Enum

    Represents the coder type\-rate for voice/fax compression
    used during a call.
    
    \*\*\* ABBREVIATIONS, ACRONYMS AND SYMBOLS \*\*\*
    
    GSM    \- Global System for Mobile Communication
    
    AMR\-NB \- Adaptive Multi Rate \- Narrow Band
    
    iLBC   \- internet Low Bitrate Codec
    
    iSAC   \- internet Speech Audio Codec
    
    other          \- none of the following.
    fax2400        \- FAX   2400  bps 
    fax4800        \- FAX   4800  bps 
    fax7200        \- FAX   7200  bps 
    fax9600        \- FAX   9600  bps
    fax14400       \- FAX   14400 bps  
    fax12000       \- FAX   12000 bps  
    g729r8000      \- G.729 8000  bps (pre\-IETF bit ordering)
    g729Ar8000     \- G.729 ANNEX\-A 8000  bps
    g726r16000     \- G.726 16000 bps
    g726r24000     \- G.726 24000 bps
    g726r32000     \- G.726 32000 bps
    g711ulawr64000 \- G.711 u\-Law 64000 bps
    g711Alawr64000 \- G.711 A\-Law 64000 bps
    g728r16000     \- G.728 16000 bps
    g723r6300      \- G.723.1 6300 bps
    g723r5300      \- G.723.1 5300 bps
    gsmr13200      \- GSM full rate 13200 bps
    g729Br8000     \- G.729 ANNEX\-B 8000  bps
    g729ABr8000    \- G.729 ANNEX\-A & B 8000 bps
    g723Ar6300     \- G723.1 Annex A 6300 bps              
    g723Ar5300     \- G723.1 Annex A 5300 bps               
    ietfg729r8000  \- G.729 8000 bps (IETF bit ordering)
    gsmeEr12200    \- GSM Enhanced Full Rate 12200 bps
    clearChannel   \- CLEAR channel codec
    g726r40000     \- G.726 40000 bps 
    llcc           \- Lossless compression codec
    gsmAmrNb       \- GSM AMR\-NB 4750 \- 12200 bps
    g722           \- G.722 2400 \- 6400 bps
    iLBC           \- iILBC 13330 or 15200 bps
    iLBCr15200     \- iLBC 15200 bps
    iLBCr13330     \- iLBC 13330 bps
    g722r4800      \- G.722 (modes 1, 2, 3)
    g722r5600      \- G.722 (modes 1, 2)
    g722r6400      \- G.722 (mode 1)
    iSAC           \- iSAC (10 to 32 kbps)
    aaclc          \- AAC\-LC Advanced Audio Coding Low Complexity
    aacld          \- AAC\-LD MPEG\-4 Low Delay Audio Coder

    """

    OTHER = 1

    FAX2400 = 2

    FAX4800 = 3

    FAX7200 = 4

    FAX9600 = 5

    FAX14400 = 6

    FAX12000 = 7

    G729R8000 = 10

    G729AR8000 = 11

    G726R16000 = 12

    G726R24000 = 13

    G726R32000 = 14

    G711ULAWR64000 = 15

    G711ALAWR64000 = 16

    G728R16000 = 17

    G723R6300 = 18

    G723R5300 = 19

    GSMR13200 = 20

    G729BR8000 = 21

    G729ABR8000 = 22

    G723AR6300 = 23

    G723AR5300 = 24

    IETFG729R8000 = 25

    GSMEER12200 = 26

    CLEARCHANNEL = 27

    G726R40000 = 28

    LLCC = 29

    GSMAMRNB = 30

    G722 = 31

    ILBC = 32

    ILBCR15200 = 33

    ILBCR13330 = 34

    G722R4800 = 35

    G722R5600 = 36

    G722R6400 = 37

    ISAC = 38

    AACLC = 39

    AACLD = 40


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcCoderTypeRate_Enum']


class CvcFaxTransmitRate_Enum(Enum):
    """
    CvcFaxTransmitRate_Enum

    This object specifies the default transmit rate of FAX
    for the VoIP, VoATM or VOFR peer. If the value of this
    object is 'none', then the Fax relay feature is disabled         
    ; otherwise the Fax relay feature is enabled.
    
    none      \- Fax relay is disabled.
    voiceRate \- the fastest possible fax rate not exceed
                the configured voice rate.
    fax2400   \- 2400  bps FAX transmit rate.
    fax4800   \- 4800  bps FAX transmit rate.
    fax7200   \- 7200  bps FAX transmit rate.
    fax9600   \- 9600  bps FAX transmit rate.
    fax14400  \- 14400 bps FAX transmit rate.
    fax12000  \- 12000 bps FAX transmit rate.

    """

    NONE = 1

    VOICERATE = 2

    FAX2400 = 3

    FAX4800 = 4

    FAX7200 = 5

    FAX9600 = 6

    FAX14400 = 7

    FAX12000 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcFaxTransmitRate_Enum']


class CvcH320CallType_Enum(Enum):
    """
    CvcH320CallType_Enum

    This object specifies the H320 call type of a voice call.

    """

    NONE = 0

    PRIMARY = 1

    SECONDARY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcH320CallType_Enum']


class CvcInBandSignaling_Enum(Enum):
    """
    CvcInBandSignaling_Enum

    Represents the type of in\-band signaling used between
    the two end points of the call and is used to inform the
    router how interpret the ABCD signaling data bits passed
    as part of the voice payload data.
    
    cas         \- specifies interpret the signaling bits as
                  North American Channel Associated signaling.        
    none        \- specifies no in\-band signaling or signaling
                  is being done via an external method (e.g
                  CCS).
    cept        \- specifies interpret the signaling bits as
                  MELCAS
    transparent \- specifies do not interpret or translate the
                  signaling bits.
    gr303       \- specifies interpret the signaling bits as
                  GR303

    """

    CAS = 1

    NONE = 2

    CEPT = 3

    TRANSPARENT = 4

    GR303 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcInBandSignaling_Enum']


class CvcSpeechCoderRate_Enum(Enum):
    """
    CvcSpeechCoderRate_Enum

    This object specifies the most desirable codec of
    speech for the VoIP, VoATM or VoFR peer.
    g729r8000      \- pre\-IETF G.729 8000  bps
    g729Ar8000     \- G.729 ANNEX\-A 8000  bps
    g726r16000     \- G.726 16000 bps
    g726r24000     \- G.726 24000 bps
    g726r32000     \- G.726 32000 bps
    g711ulawr64000 \- G.711 u\-Law 64000 bps
    g711Alawr64000 \- G.711 A\-Law 64000 bps
    g728r16000     \- G.728 16000 bps
    g723r6300      \- G.723.1 6300 bps
    g723r5300      \- G.723.1 5300 bps
    gsmr13200      \- GSM Full rate 13200 bps
    g729Br8000     \- G.729 ANNEX\-B 8000  bps
    g729ABr8000    \- G.729 ANNEX\-A & B 8000 bps
    g723Ar6300     \- G723.1 Annex A 6300 bps              
    g723Ar5300     \- G723.1 Annex A 5300 bps               
    g729IETFr8000  \- IETF G.729 8000  bps
    gsmeEr12200    \- GSM Enhanced Full Rate 12200 bps
    clearChannel   \- CLEAR Channel codec
    g726r40000     \- G.726 40000 bps
    llcc           \- Lossless compression codec
    gsmAmrNb       \- GSM AMR\-NB 4750 \- 12200 bps
    iLBC           \- iILBC 13330 or 15200 bps
    iLBCr15200     \- iLBC 15200 bps
    iLBCr13330     \- iLBC 13330 bps
    g722r4800      \- G.722 (modes 1, 2, 3)
    g722r5600      \- G.722 (modes 1, 2)
    g722r6400      \- G.722 (mode 1)
    iSAC           \- iSAC (10 to 32 kbps)
    aaclc          \- AAC\-LC Advanced Audio Coding Low Complexity
    aacld          \- AAC\-LD MPEG\-4 Low Delay Audio Coder

    """

    G729R8000 = 1

    G729AR8000 = 2

    G726R16000 = 3

    G726R24000 = 4

    G726R32000 = 5

    G711ULAWR64000 = 6

    G711ALAWR64000 = 7

    G728R16000 = 8

    G723R6300 = 9

    G723R5300 = 10

    GSMR13200 = 11

    G729BR8000 = 12

    G729ABR8000 = 13

    G723AR6300 = 14

    G723AR5300 = 15

    G729IETFR8000 = 16

    GSMEER12200 = 17

    CLEARCHANNEL = 18

    G726R40000 = 19

    LLCC = 20

    GSMAMRNB = 21

    ILBC = 22

    ILBCR15200 = 23

    ILBCR13330 = 24

    G722R4800 = 25

    G722R5600 = 26

    G722R6400 = 27

    ISAC = 28

    AACLC = 29

    AACLD = 30


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcSpeechCoderRate_Enum']


class CvcVideoCoderRate_Enum(Enum):
    """
    CvcVideoCoderRate_Enum

    This object specifies the encoding type used to compress
    the video data of the voice call.

    """

    NONE = 0

    H261 = 1

    H263 = 2

    H263PLUS = 3

    H264 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcVideoCoderRate_Enum']



class CISCOVOICECOMMONDIALCONTROLMIB(object):
    """
    
    
    .. attribute:: cvcommondccallactivetable
    
    	This table is a common extension to the call active table of IETF Dial Control MIB. It contains common call  leg information about a network call leg
    	**type**\: :py:class:`CvCommonDcCallActiveTable <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable>`
    
    .. attribute:: cvcommondccallhistorytable
    
    	This table is the Common extension to the call history table of IETF Dial Control MIB. It contains Common call  leg information about a network call leg
    	**type**\: :py:class:`CvCommonDcCallHistoryTable <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable>`
    
    

    """

    _prefix = 'cisco-voice'
    _revision = '2010-06-30'

    def __init__(self):
        self.cvcommondccallactivetable = CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable()
        self.cvcommondccallactivetable.parent = self
        self.cvcommondccallhistorytable = CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable()
        self.cvcommondccallhistorytable.parent = self


    class CvCommonDcCallActiveTable(object):
        """
        This table is a common extension to the call active
        table of IETF Dial Control MIB. It contains common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallactiveentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the  call establishment to a network dialpeer.              The entry is deleted when its associated call active entry  in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvCommonDcCallActiveEntry <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry>`
        
        

        """

        _prefix = 'cisco-voice'
        _revision = '2010-06-30'

        def __init__(self):
            self.parent = None
            self.cvcommondccallactiveentry = YList()
            self.cvcommondccallactiveentry.parent = self
            self.cvcommondccallactiveentry.name = 'cvcommondccallactiveentry'


        class CvCommonDcCallActiveEntry(object):
            """
            The common information regarding a single network call
            leg. The call leg entry is identified by using the same 
            index objects that are used by Call Active table of IETF 
            Dial Control MIB to identify the call.
            An entry of this table is created when its associated 
            call active entry in the IETF Dial Control MIB is created
            and the call active entry contains information for the 
            call establishment to a network dialpeer.             
            The entry is deleted when its associated call active entry 
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: callactiveindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivesetuptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcommondccallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\: bool
            
            .. attribute:: cvcommondccallactivecallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cvcommondccallactivecodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\: int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg  for the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvcommondccallactiveconnectionid
            
            	The global call identifier for the network call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvcommondccallactiveinbandsignaling
            
            	Specifies the type of in\-band signaling being used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\: :py:class:`CvcInBandSignaling_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling_Enum>`
            
            .. attribute:: cvcommondccallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) is enabled for the voice call
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-voice'
            _revision = '2010-06-30'

            def __init__(self):
                self.parent = None
                self.callactiveindex = None
                self.callactivesetuptime = None
                self.cvcommondccallactivecalleridblock = None
                self.cvcommondccallactivecallingname = None
                self.cvcommondccallactivecodecbytes = None
                self.cvcommondccallactivecodertyperate = None
                self.cvcommondccallactiveconnectionid = None
                self.cvcommondccallactiveinbandsignaling = None
                self.cvcommondccallactivevadenable = None

            @property
            def _common_path(self):
                if self.callactiveindex is None:
                    raise YPYDataValidationError('Key property callactiveindex is None')
                if self.callactivesetuptime is None:
                    raise YPYDataValidationError('Key property callactivesetuptime is None')

                return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveTable/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveEntry[CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + '][CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.callactiveindex is not None:
                    return True

                if self.callactivesetuptime is not None:
                    return True

                if self.cvcommondccallactivecalleridblock is not None:
                    return True

                if self.cvcommondccallactivecallingname is not None:
                    return True

                if self.cvcommondccallactivecodecbytes is not None:
                    return True

                if self.cvcommondccallactivecodertyperate is not None:
                    return True

                if self.cvcommondccallactiveconnectionid is not None:
                    return True

                if self.cvcommondccallactiveinbandsignaling is not None:
                    return True

                if self.cvcommondccallactivevadenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcommondccallactiveentry is not None:
                for child_ref in self.cvcommondccallactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable']['meta_info']


    class CvCommonDcCallHistoryTable(object):
        """
        This table is the Common extension to the call history
        table of IETF Dial Control MIB. It contains Common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallhistoryentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call history entry in the IETF Dial Control MIB is  created and the call history entry contains information  for the call establishment to a network dialpeer. The entry is deleted when its associated call history  entry in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvCommonDcCallHistoryEntry <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry>`
        
        

        """

        _prefix = 'cisco-voice'
        _revision = '2010-06-30'

        def __init__(self):
            self.parent = None
            self.cvcommondccallhistoryentry = YList()
            self.cvcommondccallhistoryentry.parent = self
            self.cvcommondccallhistoryentry.name = 'cvcommondccallhistoryentry'


        class CvCommonDcCallHistoryEntry(object):
            """
            The common information regarding a single network call
            leg. The call leg entry is identified by using the same 
            index objects that are used by Call Active table of IETF 
            Dial Control MIB to identify the call.
            An entry of this table is created when its associated 
            call history entry in the IETF Dial Control MIB is 
            created and the call history entry contains information 
            for the call establishment to a network dialpeer.
            The entry is deleted when its associated call history 
            entry in the IETF Dial Control MIB is deleted.
            
            .. attribute:: ccallhistoryindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcommondccallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\: bool
            
            .. attribute:: cvcommondccallhistorycallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length  of zero
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cvcommondccallhistorycodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\: int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for  the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvcommondccallhistoryconnectionid
            
            	The global call identifier for the gateway call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvcommondccallhistoryinbandsignaling
            
            	Specifies the type of in\-band signaling used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\: :py:class:`CvcInBandSignaling_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling_Enum>`
            
            .. attribute:: cvcommondccallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-voice'
            _revision = '2010-06-30'

            def __init__(self):
                self.parent = None
                self.ccallhistoryindex = None
                self.cvcommondccallhistorycalleridblock = None
                self.cvcommondccallhistorycallingname = None
                self.cvcommondccallhistorycodecbytes = None
                self.cvcommondccallhistorycodertyperate = None
                self.cvcommondccallhistoryconnectionid = None
                self.cvcommondccallhistoryinbandsignaling = None
                self.cvcommondccallhistoryvadenable = None

            @property
            def _common_path(self):
                if self.ccallhistoryindex is None:
                    raise YPYDataValidationError('Key property ccallhistoryindex is None')

                return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryTable/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryEntry[CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccallhistoryindex is not None:
                    return True

                if self.cvcommondccallhistorycalleridblock is not None:
                    return True

                if self.cvcommondccallhistorycallingname is not None:
                    return True

                if self.cvcommondccallhistorycodecbytes is not None:
                    return True

                if self.cvcommondccallhistorycodertyperate is not None:
                    return True

                if self.cvcommondccallhistoryconnectionid is not None:
                    return True

                if self.cvcommondccallhistoryinbandsignaling is not None:
                    return True

                if self.cvcommondccallhistoryvadenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcommondccallhistoryentry is not None:
                for child_ref in self.cvcommondccallhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cvcommondccallactivetable is not None and self.cvcommondccallactivetable._has_data():
            return True

        if self.cvcommondccallactivetable is not None and self.cvcommondccallactivetable.is_presence():
            return True

        if self.cvcommondccallhistorytable is not None and self.cvcommondccallhistorytable._has_data():
            return True

        if self.cvcommondccallhistorytable is not None and self.cvcommondccallhistorytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CISCOVOICECOMMONDIALCONTROLMIB']['meta_info']



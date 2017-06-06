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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CvccodertyperateEnum(Enum):
    """
    CvccodertyperateEnum

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

    .. data:: other = 1

    .. data:: fax2400 = 2

    .. data:: fax4800 = 3

    .. data:: fax7200 = 4

    .. data:: fax9600 = 5

    .. data:: fax14400 = 6

    .. data:: fax12000 = 7

    .. data:: g729r8000 = 10

    .. data:: g729Ar8000 = 11

    .. data:: g726r16000 = 12

    .. data:: g726r24000 = 13

    .. data:: g726r32000 = 14

    .. data:: g711ulawr64000 = 15

    .. data:: g711Alawr64000 = 16

    .. data:: g728r16000 = 17

    .. data:: g723r6300 = 18

    .. data:: g723r5300 = 19

    .. data:: gsmr13200 = 20

    .. data:: g729Br8000 = 21

    .. data:: g729ABr8000 = 22

    .. data:: g723Ar6300 = 23

    .. data:: g723Ar5300 = 24

    .. data:: ietfg729r8000 = 25

    .. data:: gsmeEr12200 = 26

    .. data:: clearChannel = 27

    .. data:: g726r40000 = 28

    .. data:: llcc = 29

    .. data:: gsmAmrNb = 30

    .. data:: g722 = 31

    .. data:: iLBC = 32

    .. data:: iLBCr15200 = 33

    .. data:: iLBCr13330 = 34

    .. data:: g722r4800 = 35

    .. data:: g722r5600 = 36

    .. data:: g722r6400 = 37

    .. data:: iSAC = 38

    .. data:: aaclc = 39

    .. data:: aacld = 40

    """

    other = 1

    fax2400 = 2

    fax4800 = 3

    fax7200 = 4

    fax9600 = 5

    fax14400 = 6

    fax12000 = 7

    g729r8000 = 10

    g729Ar8000 = 11

    g726r16000 = 12

    g726r24000 = 13

    g726r32000 = 14

    g711ulawr64000 = 15

    g711Alawr64000 = 16

    g728r16000 = 17

    g723r6300 = 18

    g723r5300 = 19

    gsmr13200 = 20

    g729Br8000 = 21

    g729ABr8000 = 22

    g723Ar6300 = 23

    g723Ar5300 = 24

    ietfg729r8000 = 25

    gsmeEr12200 = 26

    clearChannel = 27

    g726r40000 = 28

    llcc = 29

    gsmAmrNb = 30

    g722 = 31

    iLBC = 32

    iLBCr15200 = 33

    iLBCr13330 = 34

    g722r4800 = 35

    g722r5600 = 36

    g722r6400 = 37

    iSAC = 38

    aaclc = 39

    aacld = 40


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvccodertyperateEnum']


class CvcfaxtransmitrateEnum(Enum):
    """
    CvcfaxtransmitrateEnum

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

    .. data:: none = 1

    .. data:: voiceRate = 2

    .. data:: fax2400 = 3

    .. data:: fax4800 = 4

    .. data:: fax7200 = 5

    .. data:: fax9600 = 6

    .. data:: fax14400 = 7

    .. data:: fax12000 = 8

    """

    none = 1

    voiceRate = 2

    fax2400 = 3

    fax4800 = 4

    fax7200 = 5

    fax9600 = 6

    fax14400 = 7

    fax12000 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcfaxtransmitrateEnum']


class Cvch320CalltypeEnum(Enum):
    """
    Cvch320CalltypeEnum

    This object specifies the H320 call type of a voice call.

    .. data:: none = 0

    .. data:: primary = 1

    .. data:: secondary = 2

    """

    none = 0

    primary = 1

    secondary = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['Cvch320CalltypeEnum']


class CvcinbandsignalingEnum(Enum):
    """
    CvcinbandsignalingEnum

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

    .. data:: cas = 1

    .. data:: none = 2

    .. data:: cept = 3

    .. data:: transparent = 4

    .. data:: gr303 = 5

    """

    cas = 1

    none = 2

    cept = 3

    transparent = 4

    gr303 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcinbandsignalingEnum']


class CvcspeechcoderrateEnum(Enum):
    """
    CvcspeechcoderrateEnum

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

    .. data:: g729r8000 = 1

    .. data:: g729Ar8000 = 2

    .. data:: g726r16000 = 3

    .. data:: g726r24000 = 4

    .. data:: g726r32000 = 5

    .. data:: g711ulawr64000 = 6

    .. data:: g711Alawr64000 = 7

    .. data:: g728r16000 = 8

    .. data:: g723r6300 = 9

    .. data:: g723r5300 = 10

    .. data:: gsmr13200 = 11

    .. data:: g729Br8000 = 12

    .. data:: g729ABr8000 = 13

    .. data:: g723Ar6300 = 14

    .. data:: g723Ar5300 = 15

    .. data:: g729IETFr8000 = 16

    .. data:: gsmeEr12200 = 17

    .. data:: clearChannel = 18

    .. data:: g726r40000 = 19

    .. data:: llcc = 20

    .. data:: gsmAmrNb = 21

    .. data:: iLBC = 22

    .. data:: iLBCr15200 = 23

    .. data:: iLBCr13330 = 24

    .. data:: g722r4800 = 25

    .. data:: g722r5600 = 26

    .. data:: g722r6400 = 27

    .. data:: iSAC = 28

    .. data:: aaclc = 29

    .. data:: aacld = 30

    """

    g729r8000 = 1

    g729Ar8000 = 2

    g726r16000 = 3

    g726r24000 = 4

    g726r32000 = 5

    g711ulawr64000 = 6

    g711Alawr64000 = 7

    g728r16000 = 8

    g723r6300 = 9

    g723r5300 = 10

    gsmr13200 = 11

    g729Br8000 = 12

    g729ABr8000 = 13

    g723Ar6300 = 14

    g723Ar5300 = 15

    g729IETFr8000 = 16

    gsmeEr12200 = 17

    clearChannel = 18

    g726r40000 = 19

    llcc = 20

    gsmAmrNb = 21

    iLBC = 22

    iLBCr15200 = 23

    iLBCr13330 = 24

    g722r4800 = 25

    g722r5600 = 26

    g722r6400 = 27

    iSAC = 28

    aaclc = 29

    aacld = 30


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcspeechcoderrateEnum']


class CvcvideocoderrateEnum(Enum):
    """
    CvcvideocoderrateEnum

    This object specifies the encoding type used to compress

    the video data of the voice call.

    .. data:: none = 0

    .. data:: h261 = 1

    .. data:: h263 = 2

    .. data:: h263plus = 3

    .. data:: h264 = 4

    """

    none = 0

    h261 = 1

    h263 = 2

    h263plus = 3

    h264 = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvcvideocoderrateEnum']



class CiscoVoiceCommonDialControlMib(object):
    """
    
    
    .. attribute:: cvcommondccallactivetable
    
    	This table is a common extension to the call active table of IETF Dial Control MIB. It contains common call  leg information about a network call leg
    	**type**\:   :py:class:`Cvcommondccallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable>`
    
    .. attribute:: cvcommondccallhistorytable
    
    	This table is the Common extension to the call history table of IETF Dial Control MIB. It contains Common call  leg information about a network call leg
    	**type**\:   :py:class:`Cvcommondccallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable>`
    
    

    """

    _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
    _revision = '2010-06-30'

    def __init__(self):
        self.cvcommondccallactivetable = CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable()
        self.cvcommondccallactivetable.parent = self
        self.cvcommondccallhistorytable = CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable()
        self.cvcommondccallhistorytable.parent = self


    class Cvcommondccallactivetable(object):
        """
        This table is a common extension to the call active
        table of IETF Dial Control MIB. It contains common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallactiveentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the  call establishment to a network dialpeer.              The entry is deleted when its associated call active entry  in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvcommondccallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
        _revision = '2010-06-30'

        def __init__(self):
            self.parent = None
            self.cvcommondccallactiveentry = YList()
            self.cvcommondccallactiveentry.parent = self
            self.cvcommondccallactiveentry.name = 'cvcommondccallactiveentry'


        class Cvcommondccallactiveentry(object):
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
            
            .. attribute:: callactivesetuptime  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DialControlMib.Callactivetable.Callactiveentry>`
            
            .. attribute:: cvcommondccallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\:  bool
            
            .. attribute:: cvcommondccallactivecallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length of zero
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cvcommondccallactivecodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\:  int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg  for the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\:   :py:class:`CvccodertyperateEnum <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvccodertyperateEnum>`
            
            .. attribute:: cvcommondccallactiveconnectionid
            
            	The global call identifier for the network call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallactiveinbandsignaling
            
            	Specifies the type of in\-band signaling being used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:   :py:class:`CvcinbandsignalingEnum <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcinbandsignalingEnum>`
            
            .. attribute:: cvcommondccallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) is enabled for the voice call
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
            _revision = '2010-06-30'

            def __init__(self):
                self.parent = None
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.cvcommondccallactivecalleridblock = None
                self.cvcommondccallactivecallingname = None
                self.cvcommondccallactivecodecbytes = None
                self.cvcommondccallactivecodertyperate = None
                self.cvcommondccallactiveconnectionid = None
                self.cvcommondccallactiveinbandsignaling = None
                self.cvcommondccallactivevadenable = None

            @property
            def _common_path(self):
                if self.callactivesetuptime is None:
                    raise YPYModelError('Key property callactivesetuptime is None')
                if self.callactiveindex is None:
                    raise YPYModelError('Key property callactiveindex is None')

                return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveTable/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveEntry[CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + '][CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.callactivesetuptime is not None:
                    return True

                if self.callactiveindex is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cvcommondccallactiveentry is not None:
                for child_ref in self.cvcommondccallactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable']['meta_info']


    class Cvcommondccallhistorytable(object):
        """
        This table is the Common extension to the call history
        table of IETF Dial Control MIB. It contains Common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallhistoryentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call history entry in the IETF Dial Control MIB is  created and the call history entry contains information  for the call establishment to a network dialpeer. The entry is deleted when its associated call history  entry in the IETF Dial Control MIB is deleted
        	**type**\: list of    :py:class:`Cvcommondccallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
        _revision = '2010-06-30'

        def __init__(self):
            self.parent = None
            self.cvcommondccallhistoryentry = YList()
            self.cvcommondccallhistoryentry.parent = self
            self.cvcommondccallhistoryentry.name = 'cvcommondccallhistoryentry'


        class Cvcommondccallhistoryentry(object):
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
            
            .. attribute:: ccallhistoryindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvcommondccallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\:  bool
            
            .. attribute:: cvcommondccallhistorycallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length  of zero
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cvcommondccallhistorycodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\:  int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for  the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\:   :py:class:`CvccodertyperateEnum <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvccodertyperateEnum>`
            
            .. attribute:: cvcommondccallhistoryconnectionid
            
            	The global call identifier for the gateway call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallhistoryinbandsignaling
            
            	Specifies the type of in\-band signaling used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:   :py:class:`CvcinbandsignalingEnum <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcinbandsignalingEnum>`
            
            .. attribute:: cvcommondccallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
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
                    raise YPYModelError('Key property ccallhistoryindex is None')

                return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryTable/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryEntry[CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:cvCommonDcCallHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cvcommondccallhistoryentry is not None:
                for child_ref in self.cvcommondccallhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cvcommondccallactivetable is not None and self.cvcommondccallactivetable._has_data():
            return True

        if self.cvcommondccallhistorytable is not None and self.cvcommondccallhistorytable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VOICE_COMMON_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CiscoVoiceCommonDialControlMib']['meta_info']



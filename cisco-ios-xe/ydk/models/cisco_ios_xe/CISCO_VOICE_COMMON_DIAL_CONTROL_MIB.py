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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cvccodertyperate(Enum):
    """
    Cvccodertyperate

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

    other = Enum.YLeaf(1, "other")

    fax2400 = Enum.YLeaf(2, "fax2400")

    fax4800 = Enum.YLeaf(3, "fax4800")

    fax7200 = Enum.YLeaf(4, "fax7200")

    fax9600 = Enum.YLeaf(5, "fax9600")

    fax14400 = Enum.YLeaf(6, "fax14400")

    fax12000 = Enum.YLeaf(7, "fax12000")

    g729r8000 = Enum.YLeaf(10, "g729r8000")

    g729Ar8000 = Enum.YLeaf(11, "g729Ar8000")

    g726r16000 = Enum.YLeaf(12, "g726r16000")

    g726r24000 = Enum.YLeaf(13, "g726r24000")

    g726r32000 = Enum.YLeaf(14, "g726r32000")

    g711ulawr64000 = Enum.YLeaf(15, "g711ulawr64000")

    g711Alawr64000 = Enum.YLeaf(16, "g711Alawr64000")

    g728r16000 = Enum.YLeaf(17, "g728r16000")

    g723r6300 = Enum.YLeaf(18, "g723r6300")

    g723r5300 = Enum.YLeaf(19, "g723r5300")

    gsmr13200 = Enum.YLeaf(20, "gsmr13200")

    g729Br8000 = Enum.YLeaf(21, "g729Br8000")

    g729ABr8000 = Enum.YLeaf(22, "g729ABr8000")

    g723Ar6300 = Enum.YLeaf(23, "g723Ar6300")

    g723Ar5300 = Enum.YLeaf(24, "g723Ar5300")

    ietfg729r8000 = Enum.YLeaf(25, "ietfg729r8000")

    gsmeEr12200 = Enum.YLeaf(26, "gsmeEr12200")

    clearChannel = Enum.YLeaf(27, "clearChannel")

    g726r40000 = Enum.YLeaf(28, "g726r40000")

    llcc = Enum.YLeaf(29, "llcc")

    gsmAmrNb = Enum.YLeaf(30, "gsmAmrNb")

    g722 = Enum.YLeaf(31, "g722")

    iLBC = Enum.YLeaf(32, "iLBC")

    iLBCr15200 = Enum.YLeaf(33, "iLBCr15200")

    iLBCr13330 = Enum.YLeaf(34, "iLBCr13330")

    g722r4800 = Enum.YLeaf(35, "g722r4800")

    g722r5600 = Enum.YLeaf(36, "g722r5600")

    g722r6400 = Enum.YLeaf(37, "g722r6400")

    iSAC = Enum.YLeaf(38, "iSAC")

    aaclc = Enum.YLeaf(39, "aaclc")

    aacld = Enum.YLeaf(40, "aacld")


class Cvcfaxtransmitrate(Enum):
    """
    Cvcfaxtransmitrate

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

    none = Enum.YLeaf(1, "none")

    voiceRate = Enum.YLeaf(2, "voiceRate")

    fax2400 = Enum.YLeaf(3, "fax2400")

    fax4800 = Enum.YLeaf(4, "fax4800")

    fax7200 = Enum.YLeaf(5, "fax7200")

    fax9600 = Enum.YLeaf(6, "fax9600")

    fax14400 = Enum.YLeaf(7, "fax14400")

    fax12000 = Enum.YLeaf(8, "fax12000")


class Cvch320Calltype(Enum):
    """
    Cvch320Calltype

    This object specifies the H320 call type of a voice call.

    .. data:: none = 0

    .. data:: primary = 1

    .. data:: secondary = 2

    """

    none = Enum.YLeaf(0, "none")

    primary = Enum.YLeaf(1, "primary")

    secondary = Enum.YLeaf(2, "secondary")


class Cvcinbandsignaling(Enum):
    """
    Cvcinbandsignaling

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

    cas = Enum.YLeaf(1, "cas")

    none = Enum.YLeaf(2, "none")

    cept = Enum.YLeaf(3, "cept")

    transparent = Enum.YLeaf(4, "transparent")

    gr303 = Enum.YLeaf(5, "gr303")


class Cvcspeechcoderrate(Enum):
    """
    Cvcspeechcoderrate

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

    g729r8000 = Enum.YLeaf(1, "g729r8000")

    g729Ar8000 = Enum.YLeaf(2, "g729Ar8000")

    g726r16000 = Enum.YLeaf(3, "g726r16000")

    g726r24000 = Enum.YLeaf(4, "g726r24000")

    g726r32000 = Enum.YLeaf(5, "g726r32000")

    g711ulawr64000 = Enum.YLeaf(6, "g711ulawr64000")

    g711Alawr64000 = Enum.YLeaf(7, "g711Alawr64000")

    g728r16000 = Enum.YLeaf(8, "g728r16000")

    g723r6300 = Enum.YLeaf(9, "g723r6300")

    g723r5300 = Enum.YLeaf(10, "g723r5300")

    gsmr13200 = Enum.YLeaf(11, "gsmr13200")

    g729Br8000 = Enum.YLeaf(12, "g729Br8000")

    g729ABr8000 = Enum.YLeaf(13, "g729ABr8000")

    g723Ar6300 = Enum.YLeaf(14, "g723Ar6300")

    g723Ar5300 = Enum.YLeaf(15, "g723Ar5300")

    g729IETFr8000 = Enum.YLeaf(16, "g729IETFr8000")

    gsmeEr12200 = Enum.YLeaf(17, "gsmeEr12200")

    clearChannel = Enum.YLeaf(18, "clearChannel")

    g726r40000 = Enum.YLeaf(19, "g726r40000")

    llcc = Enum.YLeaf(20, "llcc")

    gsmAmrNb = Enum.YLeaf(21, "gsmAmrNb")

    iLBC = Enum.YLeaf(22, "iLBC")

    iLBCr15200 = Enum.YLeaf(23, "iLBCr15200")

    iLBCr13330 = Enum.YLeaf(24, "iLBCr13330")

    g722r4800 = Enum.YLeaf(25, "g722r4800")

    g722r5600 = Enum.YLeaf(26, "g722r5600")

    g722r6400 = Enum.YLeaf(27, "g722r6400")

    iSAC = Enum.YLeaf(28, "iSAC")

    aaclc = Enum.YLeaf(29, "aaclc")

    aacld = Enum.YLeaf(30, "aacld")


class Cvcvideocoderrate(Enum):
    """
    Cvcvideocoderrate

    This object specifies the encoding type used to compress

    the video data of the voice call.

    .. data:: none = 0

    .. data:: h261 = 1

    .. data:: h263 = 2

    .. data:: h263plus = 3

    .. data:: h264 = 4

    """

    none = Enum.YLeaf(0, "none")

    h261 = Enum.YLeaf(1, "h261")

    h263 = Enum.YLeaf(2, "h263")

    h263plus = Enum.YLeaf(3, "h263plus")

    h264 = Enum.YLeaf(4, "h264")



class CiscoVoiceCommonDialControlMib(Entity):
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
        super(CiscoVoiceCommonDialControlMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"

        self.cvcommondccallactivetable = CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable()
        self.cvcommondccallactivetable.parent = self
        self._children_name_map["cvcommondccallactivetable"] = "cvCommonDcCallActiveTable"
        self._children_yang_names.add("cvCommonDcCallActiveTable")

        self.cvcommondccallhistorytable = CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable()
        self.cvcommondccallhistorytable.parent = self
        self._children_name_map["cvcommondccallhistorytable"] = "cvCommonDcCallHistoryTable"
        self._children_yang_names.add("cvCommonDcCallHistoryTable")


    class Cvcommondccallactivetable(Entity):
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
            super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable, self).__init__()

            self.yang_name = "cvCommonDcCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"

            self.cvcommondccallactiveentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable, self).__setattr__(name, value)


        class Cvcommondccallactiveentry(Entity):
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
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            .. attribute:: cvcommondccallactiveconnectionid
            
            	The global call identifier for the network call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallactiveinbandsignaling
            
            	Specifies the type of in\-band signaling being used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:   :py:class:`Cvcinbandsignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvcinbandsignaling>`
            
            .. attribute:: cvcommondccallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) is enabled for the voice call
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
            _revision = '2010-06-30'

            def __init__(self):
                super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry, self).__init__()

                self.yang_name = "cvCommonDcCallActiveEntry"
                self.yang_parent_name = "cvCommonDcCallActiveTable"

                self.callactivesetuptime = YLeaf(YType.str, "callActiveSetupTime")

                self.callactiveindex = YLeaf(YType.str, "callActiveIndex")

                self.cvcommondccallactivecalleridblock = YLeaf(YType.boolean, "cvCommonDcCallActiveCallerIDBlock")

                self.cvcommondccallactivecallingname = YLeaf(YType.str, "cvCommonDcCallActiveCallingName")

                self.cvcommondccallactivecodecbytes = YLeaf(YType.int32, "cvCommonDcCallActiveCodecBytes")

                self.cvcommondccallactivecodertyperate = YLeaf(YType.enumeration, "cvCommonDcCallActiveCoderTypeRate")

                self.cvcommondccallactiveconnectionid = YLeaf(YType.str, "cvCommonDcCallActiveConnectionId")

                self.cvcommondccallactiveinbandsignaling = YLeaf(YType.enumeration, "cvCommonDcCallActiveInBandSignaling")

                self.cvcommondccallactivevadenable = YLeaf(YType.boolean, "cvCommonDcCallActiveVADEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("callactivesetuptime",
                                "callactiveindex",
                                "cvcommondccallactivecalleridblock",
                                "cvcommondccallactivecallingname",
                                "cvcommondccallactivecodecbytes",
                                "cvcommondccallactivecodertyperate",
                                "cvcommondccallactiveconnectionid",
                                "cvcommondccallactiveinbandsignaling",
                                "cvcommondccallactivevadenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.callactivesetuptime.is_set or
                    self.callactiveindex.is_set or
                    self.cvcommondccallactivecalleridblock.is_set or
                    self.cvcommondccallactivecallingname.is_set or
                    self.cvcommondccallactivecodecbytes.is_set or
                    self.cvcommondccallactivecodertyperate.is_set or
                    self.cvcommondccallactiveconnectionid.is_set or
                    self.cvcommondccallactiveinbandsignaling.is_set or
                    self.cvcommondccallactivevadenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.callactivesetuptime.yfilter != YFilter.not_set or
                    self.callactiveindex.yfilter != YFilter.not_set or
                    self.cvcommondccallactivecalleridblock.yfilter != YFilter.not_set or
                    self.cvcommondccallactivecallingname.yfilter != YFilter.not_set or
                    self.cvcommondccallactivecodecbytes.yfilter != YFilter.not_set or
                    self.cvcommondccallactivecodertyperate.yfilter != YFilter.not_set or
                    self.cvcommondccallactiveconnectionid.yfilter != YFilter.not_set or
                    self.cvcommondccallactiveinbandsignaling.yfilter != YFilter.not_set or
                    self.cvcommondccallactivevadenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCommonDcCallActiveEntry" + "[callActiveSetupTime='" + self.callactivesetuptime.get() + "']" + "[callActiveIndex='" + self.callactiveindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/cvCommonDcCallActiveTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.callactivesetuptime.is_set or self.callactivesetuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactivesetuptime.get_name_leafdata())
                if (self.callactiveindex.is_set or self.callactiveindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.callactiveindex.get_name_leafdata())
                if (self.cvcommondccallactivecalleridblock.is_set or self.cvcommondccallactivecalleridblock.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactivecalleridblock.get_name_leafdata())
                if (self.cvcommondccallactivecallingname.is_set or self.cvcommondccallactivecallingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactivecallingname.get_name_leafdata())
                if (self.cvcommondccallactivecodecbytes.is_set or self.cvcommondccallactivecodecbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactivecodecbytes.get_name_leafdata())
                if (self.cvcommondccallactivecodertyperate.is_set or self.cvcommondccallactivecodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactivecodertyperate.get_name_leafdata())
                if (self.cvcommondccallactiveconnectionid.is_set or self.cvcommondccallactiveconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactiveconnectionid.get_name_leafdata())
                if (self.cvcommondccallactiveinbandsignaling.is_set or self.cvcommondccallactiveinbandsignaling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactiveinbandsignaling.get_name_leafdata())
                if (self.cvcommondccallactivevadenable.is_set or self.cvcommondccallactivevadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallactivevadenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "callActiveSetupTime" or name == "callActiveIndex" or name == "cvCommonDcCallActiveCallerIDBlock" or name == "cvCommonDcCallActiveCallingName" or name == "cvCommonDcCallActiveCodecBytes" or name == "cvCommonDcCallActiveCoderTypeRate" or name == "cvCommonDcCallActiveConnectionId" or name == "cvCommonDcCallActiveInBandSignaling" or name == "cvCommonDcCallActiveVADEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "callActiveSetupTime"):
                    self.callactivesetuptime = value
                    self.callactivesetuptime.value_namespace = name_space
                    self.callactivesetuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "callActiveIndex"):
                    self.callactiveindex = value
                    self.callactiveindex.value_namespace = name_space
                    self.callactiveindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveCallerIDBlock"):
                    self.cvcommondccallactivecalleridblock = value
                    self.cvcommondccallactivecalleridblock.value_namespace = name_space
                    self.cvcommondccallactivecalleridblock.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveCallingName"):
                    self.cvcommondccallactivecallingname = value
                    self.cvcommondccallactivecallingname.value_namespace = name_space
                    self.cvcommondccallactivecallingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveCodecBytes"):
                    self.cvcommondccallactivecodecbytes = value
                    self.cvcommondccallactivecodecbytes.value_namespace = name_space
                    self.cvcommondccallactivecodecbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveCoderTypeRate"):
                    self.cvcommondccallactivecodertyperate = value
                    self.cvcommondccallactivecodertyperate.value_namespace = name_space
                    self.cvcommondccallactivecodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveConnectionId"):
                    self.cvcommondccallactiveconnectionid = value
                    self.cvcommondccallactiveconnectionid.value_namespace = name_space
                    self.cvcommondccallactiveconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveInBandSignaling"):
                    self.cvcommondccallactiveinbandsignaling = value
                    self.cvcommondccallactiveinbandsignaling.value_namespace = name_space
                    self.cvcommondccallactiveinbandsignaling.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallActiveVADEnable"):
                    self.cvcommondccallactivevadenable = value
                    self.cvcommondccallactivevadenable.value_namespace = name_space
                    self.cvcommondccallactivevadenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcommondccallactiveentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcommondccallactiveentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCommonDcCallActiveTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCommonDcCallActiveEntry"):
                for c in self.cvcommondccallactiveentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcommondccallactiveentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCommonDcCallActiveEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvcommondccallhistorytable(Entity):
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
            super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable, self).__init__()

            self.yang_name = "cvCommonDcCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"

            self.cvcommondccallhistoryentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable, self).__setattr__(name, value)


        class Cvcommondccallhistoryentry(Entity):
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
            	**type**\:   :py:class:`Cvccodertyperate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvccodertyperate>`
            
            .. attribute:: cvcommondccallhistoryconnectionid
            
            	The global call identifier for the gateway call
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallhistoryinbandsignaling
            
            	Specifies the type of in\-band signaling used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:   :py:class:`Cvcinbandsignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.Cvcinbandsignaling>`
            
            .. attribute:: cvcommondccallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
            _revision = '2010-06-30'

            def __init__(self):
                super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry, self).__init__()

                self.yang_name = "cvCommonDcCallHistoryEntry"
                self.yang_parent_name = "cvCommonDcCallHistoryTable"

                self.ccallhistoryindex = YLeaf(YType.str, "cCallHistoryIndex")

                self.cvcommondccallhistorycalleridblock = YLeaf(YType.boolean, "cvCommonDcCallHistoryCallerIDBlock")

                self.cvcommondccallhistorycallingname = YLeaf(YType.str, "cvCommonDcCallHistoryCallingName")

                self.cvcommondccallhistorycodecbytes = YLeaf(YType.int32, "cvCommonDcCallHistoryCodecBytes")

                self.cvcommondccallhistorycodertyperate = YLeaf(YType.enumeration, "cvCommonDcCallHistoryCoderTypeRate")

                self.cvcommondccallhistoryconnectionid = YLeaf(YType.str, "cvCommonDcCallHistoryConnectionId")

                self.cvcommondccallhistoryinbandsignaling = YLeaf(YType.enumeration, "cvCommonDcCallHistoryInBandSignaling")

                self.cvcommondccallhistoryvadenable = YLeaf(YType.boolean, "cvCommonDcCallHistoryVADEnable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccallhistoryindex",
                                "cvcommondccallhistorycalleridblock",
                                "cvcommondccallhistorycallingname",
                                "cvcommondccallhistorycodecbytes",
                                "cvcommondccallhistorycodertyperate",
                                "cvcommondccallhistoryconnectionid",
                                "cvcommondccallhistoryinbandsignaling",
                                "cvcommondccallhistoryvadenable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccallhistoryindex.is_set or
                    self.cvcommondccallhistorycalleridblock.is_set or
                    self.cvcommondccallhistorycallingname.is_set or
                    self.cvcommondccallhistorycodecbytes.is_set or
                    self.cvcommondccallhistorycodertyperate.is_set or
                    self.cvcommondccallhistoryconnectionid.is_set or
                    self.cvcommondccallhistoryinbandsignaling.is_set or
                    self.cvcommondccallhistoryvadenable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccallhistoryindex.yfilter != YFilter.not_set or
                    self.cvcommondccallhistorycalleridblock.yfilter != YFilter.not_set or
                    self.cvcommondccallhistorycallingname.yfilter != YFilter.not_set or
                    self.cvcommondccallhistorycodecbytes.yfilter != YFilter.not_set or
                    self.cvcommondccallhistorycodertyperate.yfilter != YFilter.not_set or
                    self.cvcommondccallhistoryconnectionid.yfilter != YFilter.not_set or
                    self.cvcommondccallhistoryinbandsignaling.yfilter != YFilter.not_set or
                    self.cvcommondccallhistoryvadenable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvCommonDcCallHistoryEntry" + "[cCallHistoryIndex='" + self.ccallhistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/cvCommonDcCallHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccallhistoryindex.is_set or self.ccallhistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccallhistoryindex.get_name_leafdata())
                if (self.cvcommondccallhistorycalleridblock.is_set or self.cvcommondccallhistorycalleridblock.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistorycalleridblock.get_name_leafdata())
                if (self.cvcommondccallhistorycallingname.is_set or self.cvcommondccallhistorycallingname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistorycallingname.get_name_leafdata())
                if (self.cvcommondccallhistorycodecbytes.is_set or self.cvcommondccallhistorycodecbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistorycodecbytes.get_name_leafdata())
                if (self.cvcommondccallhistorycodertyperate.is_set or self.cvcommondccallhistorycodertyperate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistorycodertyperate.get_name_leafdata())
                if (self.cvcommondccallhistoryconnectionid.is_set or self.cvcommondccallhistoryconnectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistoryconnectionid.get_name_leafdata())
                if (self.cvcommondccallhistoryinbandsignaling.is_set or self.cvcommondccallhistoryinbandsignaling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistoryinbandsignaling.get_name_leafdata())
                if (self.cvcommondccallhistoryvadenable.is_set or self.cvcommondccallhistoryvadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvcommondccallhistoryvadenable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cCallHistoryIndex" or name == "cvCommonDcCallHistoryCallerIDBlock" or name == "cvCommonDcCallHistoryCallingName" or name == "cvCommonDcCallHistoryCodecBytes" or name == "cvCommonDcCallHistoryCoderTypeRate" or name == "cvCommonDcCallHistoryConnectionId" or name == "cvCommonDcCallHistoryInBandSignaling" or name == "cvCommonDcCallHistoryVADEnable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cCallHistoryIndex"):
                    self.ccallhistoryindex = value
                    self.ccallhistoryindex.value_namespace = name_space
                    self.ccallhistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryCallerIDBlock"):
                    self.cvcommondccallhistorycalleridblock = value
                    self.cvcommondccallhistorycalleridblock.value_namespace = name_space
                    self.cvcommondccallhistorycalleridblock.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryCallingName"):
                    self.cvcommondccallhistorycallingname = value
                    self.cvcommondccallhistorycallingname.value_namespace = name_space
                    self.cvcommondccallhistorycallingname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryCodecBytes"):
                    self.cvcommondccallhistorycodecbytes = value
                    self.cvcommondccallhistorycodecbytes.value_namespace = name_space
                    self.cvcommondccallhistorycodecbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryCoderTypeRate"):
                    self.cvcommondccallhistorycodertyperate = value
                    self.cvcommondccallhistorycodertyperate.value_namespace = name_space
                    self.cvcommondccallhistorycodertyperate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryConnectionId"):
                    self.cvcommondccallhistoryconnectionid = value
                    self.cvcommondccallhistoryconnectionid.value_namespace = name_space
                    self.cvcommondccallhistoryconnectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryInBandSignaling"):
                    self.cvcommondccallhistoryinbandsignaling = value
                    self.cvcommondccallhistoryinbandsignaling.value_namespace = name_space
                    self.cvcommondccallhistoryinbandsignaling.value_namespace_prefix = name_space_prefix
                if(value_path == "cvCommonDcCallHistoryVADEnable"):
                    self.cvcommondccallhistoryvadenable = value
                    self.cvcommondccallhistoryvadenable.value_namespace = name_space
                    self.cvcommondccallhistoryvadenable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvcommondccallhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvcommondccallhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvCommonDcCallHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvCommonDcCallHistoryEntry"):
                for c in self.cvcommondccallhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvcommondccallhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvCommonDcCallHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cvcommondccallactivetable is not None and self.cvcommondccallactivetable.has_data()) or
            (self.cvcommondccallhistorytable is not None and self.cvcommondccallhistorytable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cvcommondccallactivetable is not None and self.cvcommondccallactivetable.has_operation()) or
            (self.cvcommondccallhistorytable is not None and self.cvcommondccallhistorytable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cvCommonDcCallActiveTable"):
            if (self.cvcommondccallactivetable is None):
                self.cvcommondccallactivetable = CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable()
                self.cvcommondccallactivetable.parent = self
                self._children_name_map["cvcommondccallactivetable"] = "cvCommonDcCallActiveTable"
            return self.cvcommondccallactivetable

        if (child_yang_name == "cvCommonDcCallHistoryTable"):
            if (self.cvcommondccallhistorytable is None):
                self.cvcommondccallhistorytable = CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable()
                self.cvcommondccallhistorytable.parent = self
                self._children_name_map["cvcommondccallhistorytable"] = "cvCommonDcCallHistoryTable"
            return self.cvcommondccallhistorytable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cvCommonDcCallActiveTable" or name == "cvCommonDcCallHistoryTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVoiceCommonDialControlMib()
        return self._top_entity


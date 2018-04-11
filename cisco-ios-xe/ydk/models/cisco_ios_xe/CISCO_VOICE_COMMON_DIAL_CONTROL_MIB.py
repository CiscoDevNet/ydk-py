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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CvcCoderTypeRate(Enum):
    """
    CvcCoderTypeRate (Enum Class)

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


class CvcFaxTransmitRate(Enum):
    """
    CvcFaxTransmitRate (Enum Class)

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


class CvcH320CallType(Enum):
    """
    CvcH320CallType (Enum Class)

    This object specifies the H320 call type of a voice call.

    .. data:: none = 0

    .. data:: primary = 1

    .. data:: secondary = 2

    """

    none = Enum.YLeaf(0, "none")

    primary = Enum.YLeaf(1, "primary")

    secondary = Enum.YLeaf(2, "secondary")


class CvcInBandSignaling(Enum):
    """
    CvcInBandSignaling (Enum Class)

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


class CvcSpeechCoderRate(Enum):
    """
    CvcSpeechCoderRate (Enum Class)

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


class CvcVideoCoderRate(Enum):
    """
    CvcVideoCoderRate (Enum Class)

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



class CISCOVOICECOMMONDIALCONTROLMIB(Entity):
    """
    
    
    .. attribute:: cvcommondccallactivetable
    
    	This table is a common extension to the call active table of IETF Dial Control MIB. It contains common call  leg information about a network call leg
    	**type**\:  :py:class:`Cvcommondccallactivetable <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable>`
    
    .. attribute:: cvcommondccallhistorytable
    
    	This table is the Common extension to the call history table of IETF Dial Control MIB. It contains Common call  leg information about a network call leg
    	**type**\:  :py:class:`Cvcommondccallhistorytable <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable>`
    
    

    """

    _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
    _revision = '2010-06-30'

    def __init__(self):
        super(CISCOVOICECOMMONDIALCONTROLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"
        self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cvCommonDcCallActiveTable", ("cvcommondccallactivetable", CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable)), ("cvCommonDcCallHistoryTable", ("cvcommondccallhistorytable", CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cvcommondccallactivetable = CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable()
        self.cvcommondccallactivetable.parent = self
        self._children_name_map["cvcommondccallactivetable"] = "cvCommonDcCallActiveTable"
        self._children_yang_names.add("cvCommonDcCallActiveTable")

        self.cvcommondccallhistorytable = CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable()
        self.cvcommondccallhistorytable.parent = self
        self._children_name_map["cvcommondccallhistorytable"] = "cvCommonDcCallHistoryTable"
        self._children_yang_names.add("cvCommonDcCallHistoryTable")
        self._segment_path = lambda: "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"


    class Cvcommondccallactivetable(Entity):
        """
        This table is a common extension to the call active
        table of IETF Dial Control MIB. It contains common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallactiveentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the  call establishment to a network dialpeer.              The entry is deleted when its associated call active entry  in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvcommondccallactiveentry <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable.Cvcommondccallactiveentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
        _revision = '2010-06-30'

        def __init__(self):
            super(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable, self).__init__()

            self.yang_name = "cvCommonDcCallActiveTable"
            self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCommonDcCallActiveEntry", ("cvcommondccallactiveentry", CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable.Cvcommondccallactiveentry))])
            self._leafs = OrderedDict()

            self.cvcommondccallactiveentry = YList(self)
            self._segment_path = lambda: "cvCommonDcCallActiveTable"
            self._absolute_path = lambda: "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable, [], name, value)


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
            
            .. attribute:: callactivesetuptime  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`callactivesetuptime <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: callactiveindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`callactiveindex <ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB.DIALCONTROLMIB.Callactivetable.Callactiveentry>`
            
            .. attribute:: cvcommondccallactiveconnectionid
            
            	The global call identifier for the network call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) is enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvcommondccallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg  for the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            .. attribute:: cvcommondccallactivecodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\: int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallactiveinbandsignaling
            
            	Specifies the type of in\-band signaling being used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:  :py:class:`CvcInBandSignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling>`
            
            .. attribute:: cvcommondccallactivecallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cvcommondccallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
            _revision = '2010-06-30'

            def __init__(self):
                super(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable.Cvcommondccallactiveentry, self).__init__()

                self.yang_name = "cvCommonDcCallActiveEntry"
                self.yang_parent_name = "cvCommonDcCallActiveTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['callactivesetuptime','callactiveindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('callactivesetuptime', YLeaf(YType.str, 'callActiveSetupTime')),
                    ('callactiveindex', YLeaf(YType.str, 'callActiveIndex')),
                    ('cvcommondccallactiveconnectionid', YLeaf(YType.str, 'cvCommonDcCallActiveConnectionId')),
                    ('cvcommondccallactivevadenable', YLeaf(YType.boolean, 'cvCommonDcCallActiveVADEnable')),
                    ('cvcommondccallactivecodertyperate', YLeaf(YType.enumeration, 'cvCommonDcCallActiveCoderTypeRate')),
                    ('cvcommondccallactivecodecbytes', YLeaf(YType.int32, 'cvCommonDcCallActiveCodecBytes')),
                    ('cvcommondccallactiveinbandsignaling', YLeaf(YType.enumeration, 'cvCommonDcCallActiveInBandSignaling')),
                    ('cvcommondccallactivecallingname', YLeaf(YType.str, 'cvCommonDcCallActiveCallingName')),
                    ('cvcommondccallactivecalleridblock', YLeaf(YType.boolean, 'cvCommonDcCallActiveCallerIDBlock')),
                ])
                self.callactivesetuptime = None
                self.callactiveindex = None
                self.cvcommondccallactiveconnectionid = None
                self.cvcommondccallactivevadenable = None
                self.cvcommondccallactivecodertyperate = None
                self.cvcommondccallactivecodecbytes = None
                self.cvcommondccallactiveinbandsignaling = None
                self.cvcommondccallactivecallingname = None
                self.cvcommondccallactivecalleridblock = None
                self._segment_path = lambda: "cvCommonDcCallActiveEntry" + "[callActiveSetupTime='" + str(self.callactivesetuptime) + "']" + "[callActiveIndex='" + str(self.callactiveindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/cvCommonDcCallActiveTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallactivetable.Cvcommondccallactiveentry, ['callactivesetuptime', 'callactiveindex', 'cvcommondccallactiveconnectionid', 'cvcommondccallactivevadenable', 'cvcommondccallactivecodertyperate', 'cvcommondccallactivecodecbytes', 'cvcommondccallactiveinbandsignaling', 'cvcommondccallactivecallingname', 'cvcommondccallactivecalleridblock'], name, value)


    class Cvcommondccallhistorytable(Entity):
        """
        This table is the Common extension to the call history
        table of IETF Dial Control MIB. It contains Common call 
        leg information about a network call leg.
        
        .. attribute:: cvcommondccallhistoryentry
        
        	The common information regarding a single network call leg. The call leg entry is identified by using the same  index objects that are used by Call Active table of IETF  Dial Control MIB to identify the call. An entry of this table is created when its associated  call history entry in the IETF Dial Control MIB is  created and the call history entry contains information  for the call establishment to a network dialpeer. The entry is deleted when its associated call history  entry in the IETF Dial Control MIB is deleted
        	**type**\: list of  		 :py:class:`Cvcommondccallhistoryentry <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable.Cvcommondccallhistoryentry>`
        
        

        """

        _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
        _revision = '2010-06-30'

        def __init__(self):
            super(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable, self).__init__()

            self.yang_name = "cvCommonDcCallHistoryTable"
            self.yang_parent_name = "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvCommonDcCallHistoryEntry", ("cvcommondccallhistoryentry", CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable.Cvcommondccallhistoryentry))])
            self._leafs = OrderedDict()

            self.cvcommondccallhistoryentry = YList(self)
            self._segment_path = lambda: "cvCommonDcCallHistoryTable"
            self._absolute_path = lambda: "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable, [], name, value)


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
            
            .. attribute:: ccallhistoryindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ccallhistoryindex <ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB.CISCODIALCONTROLMIB.Ccallhistorytable.Ccallhistoryentry>`
            
            .. attribute:: cvcommondccallhistoryconnectionid
            
            	The global call identifier for the gateway call
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: cvcommondccallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvcommondccallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for  the call. This rate is different from the configuration rate  because of rate negotiation during the call
            	**type**\:  :py:class:`CvcCoderTypeRate <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate>`
            
            .. attribute:: cvcommondccallhistorycodecbytes
            
            	Specifies the payload size of the voice packet
            	**type**\: int
            
            	**range:** 10..255
            
            .. attribute:: cvcommondccallhistoryinbandsignaling
            
            	Specifies the type of in\-band signaling used on the call.  This object is instantiated only for  Connection Trunk calls
            	**type**\:  :py:class:`CvcInBandSignaling <ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling>`
            
            .. attribute:: cvcommondccallhistorycallingname
            
            	The calling party name this call is connected to. If the name is not available, then it will have a length  of zero
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: cvcommondccallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this voice call
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'
            _revision = '2010-06-30'

            def __init__(self):
                super(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable.Cvcommondccallhistoryentry, self).__init__()

                self.yang_name = "cvCommonDcCallHistoryEntry"
                self.yang_parent_name = "cvCommonDcCallHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccallhistoryindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccallhistoryindex', YLeaf(YType.str, 'cCallHistoryIndex')),
                    ('cvcommondccallhistoryconnectionid', YLeaf(YType.str, 'cvCommonDcCallHistoryConnectionId')),
                    ('cvcommondccallhistoryvadenable', YLeaf(YType.boolean, 'cvCommonDcCallHistoryVADEnable')),
                    ('cvcommondccallhistorycodertyperate', YLeaf(YType.enumeration, 'cvCommonDcCallHistoryCoderTypeRate')),
                    ('cvcommondccallhistorycodecbytes', YLeaf(YType.int32, 'cvCommonDcCallHistoryCodecBytes')),
                    ('cvcommondccallhistoryinbandsignaling', YLeaf(YType.enumeration, 'cvCommonDcCallHistoryInBandSignaling')),
                    ('cvcommondccallhistorycallingname', YLeaf(YType.str, 'cvCommonDcCallHistoryCallingName')),
                    ('cvcommondccallhistorycalleridblock', YLeaf(YType.boolean, 'cvCommonDcCallHistoryCallerIDBlock')),
                ])
                self.ccallhistoryindex = None
                self.cvcommondccallhistoryconnectionid = None
                self.cvcommondccallhistoryvadenable = None
                self.cvcommondccallhistorycodertyperate = None
                self.cvcommondccallhistorycodecbytes = None
                self.cvcommondccallhistoryinbandsignaling = None
                self.cvcommondccallhistorycallingname = None
                self.cvcommondccallhistorycalleridblock = None
                self._segment_path = lambda: "cvCommonDcCallHistoryEntry" + "[cCallHistoryIndex='" + str(self.ccallhistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB:CISCO-VOICE-COMMON-DIAL-CONTROL-MIB/cvCommonDcCallHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVOICECOMMONDIALCONTROLMIB.Cvcommondccallhistorytable.Cvcommondccallhistoryentry, ['ccallhistoryindex', 'cvcommondccallhistoryconnectionid', 'cvcommondccallhistoryvadenable', 'cvcommondccallhistorycodertyperate', 'cvcommondccallhistorycodecbytes', 'cvcommondccallhistoryinbandsignaling', 'cvcommondccallhistorycallingname', 'cvcommondccallhistorycalleridblock'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOVOICECOMMONDIALCONTROLMIB()
        return self._top_entity


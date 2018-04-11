""" CISCO_OSPF_TRAP_MIB 

This MIB module describes new/modified notification
objects/events, which are defined in the latest
version for OSPF MIB IETF draft
draftietf\-ospf\-mib\-update\-05.txt. Support for OSPF 
Sham link is also added

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOOSPFTRAPMIB(Entity):
    """
    
    
    .. attribute:: cospftrapcontrol
    
    	
    	**type**\:  :py:class:`Cospftrapcontrol <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.Cospftrapcontrol>`
    
    

    """

    _prefix = 'CISCO-OSPF-TRAP-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        super(CISCOOSPFTRAPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-OSPF-TRAP-MIB"
        self.yang_parent_name = "CISCO-OSPF-TRAP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cospfTrapControl", ("cospftrapcontrol", CISCOOSPFTRAPMIB.Cospftrapcontrol))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cospftrapcontrol = CISCOOSPFTRAPMIB.Cospftrapcontrol()
        self.cospftrapcontrol.parent = self
        self._children_name_map["cospftrapcontrol"] = "cospfTrapControl"
        self._children_yang_names.add("cospfTrapControl")
        self._segment_path = lambda: "CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB"


    class Cospftrapcontrol(Entity):
        """
        
        
        .. attribute:: cospfsettrap
        
        	An octet string serving as a bit  map  for the trap events defined by the OSPF traps in  this MIB. This object is used to enable and   disable  specific OSPF   traps   where  a  1   in  the  corresponding bit  field represents  enabled
        	**type**\:  :py:class:`Cospfsettrap <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.Cospftrapcontrol.Cospfsettrap>`
        
        .. attribute:: cospfconfigerrortype
        
        	Potential types of configuration conflicts. Used  by the cospfConfigError and cospfConfigVirtError traps. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:  :py:class:`Cospfconfigerrortype <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.Cospftrapcontrol.Cospfconfigerrortype>`
        
        .. attribute:: cospfpackettype
        
        	OSPF packet types. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:  :py:class:`Cospfpackettype <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CISCOOSPFTRAPMIB.Cospftrapcontrol.Cospfpackettype>`
        
        .. attribute:: cospfpacketsrc
        
        	The IP address of an inbound packet that can\- not be identified by a neighbor instance. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'CISCO-OSPF-TRAP-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFTRAPMIB.Cospftrapcontrol, self).__init__()

            self.yang_name = "cospfTrapControl"
            self.yang_parent_name = "CISCO-OSPF-TRAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cospfsettrap', YLeaf(YType.bits, 'cospfSetTrap')),
                ('cospfconfigerrortype', YLeaf(YType.enumeration, 'cospfConfigErrorType')),
                ('cospfpackettype', YLeaf(YType.enumeration, 'cospfPacketType')),
                ('cospfpacketsrc', YLeaf(YType.str, 'cospfPacketSrc')),
            ])
            self.cospfsettrap = Bits()
            self.cospfconfigerrortype = None
            self.cospfpackettype = None
            self.cospfpacketsrc = None
            self._segment_path = lambda: "cospfTrapControl"
            self._absolute_path = lambda: "CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFTRAPMIB.Cospftrapcontrol, ['cospfsettrap', 'cospfconfigerrortype', 'cospfpackettype', 'cospfpacketsrc'], name, value)

        class Cospfconfigerrortype(Enum):
            """
            Cospfconfigerrortype (Enum Class)

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

            badVersion = Enum.YLeaf(1, "badVersion")

            areaMismatch = Enum.YLeaf(2, "areaMismatch")

            unknownNbmaNbr = Enum.YLeaf(3, "unknownNbmaNbr")

            unknownVirtualNbr = Enum.YLeaf(4, "unknownVirtualNbr")

            authTypeMismatch = Enum.YLeaf(5, "authTypeMismatch")

            authFailure = Enum.YLeaf(6, "authFailure")

            netMaskMismatch = Enum.YLeaf(7, "netMaskMismatch")

            helloIntervalMismatch = Enum.YLeaf(8, "helloIntervalMismatch")

            deadIntervalMismatch = Enum.YLeaf(9, "deadIntervalMismatch")

            optionMismatch = Enum.YLeaf(10, "optionMismatch")

            mtuMismatch = Enum.YLeaf(11, "mtuMismatch")

            noError = Enum.YLeaf(12, "noError")

            unknownShamLinkNbr = Enum.YLeaf(13, "unknownShamLinkNbr")


        class Cospfpackettype(Enum):
            """
            Cospfpackettype (Enum Class)

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

            hello = Enum.YLeaf(1, "hello")

            dbDescript = Enum.YLeaf(2, "dbDescript")

            lsReq = Enum.YLeaf(3, "lsReq")

            lsUpdate = Enum.YLeaf(4, "lsUpdate")

            lsAck = Enum.YLeaf(5, "lsAck")

            nullPacket = Enum.YLeaf(6, "nullPacket")


    def clone_ptr(self):
        self._top_entity = CISCOOSPFTRAPMIB()
        return self._top_entity


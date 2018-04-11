""" OSPF_TRAP_MIB 

The MIB module to describe traps for the OSPF
Version 2 Protocol.

Copyright (C) The IETF Trust (2006).
This version of this MIB module is part of
RFC 4750;  see the RFC itself for full legal
notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OSPFTRAPMIB(Entity):
    """
    
    
    .. attribute:: ospftrapcontrol
    
    	
    	**type**\:  :py:class:`Ospftrapcontrol <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OSPFTRAPMIB.Ospftrapcontrol>`
    
    

    """

    _prefix = 'OSPF-TRAP-MIB'
    _revision = '2006-11-10'

    def __init__(self):
        super(OSPFTRAPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "OSPF-TRAP-MIB"
        self.yang_parent_name = "OSPF-TRAP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ospfTrapControl", ("ospftrapcontrol", OSPFTRAPMIB.Ospftrapcontrol))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ospftrapcontrol = OSPFTRAPMIB.Ospftrapcontrol()
        self.ospftrapcontrol.parent = self
        self._children_name_map["ospftrapcontrol"] = "ospfTrapControl"
        self._children_yang_names.add("ospfTrapControl")
        self._segment_path = lambda: "OSPF-TRAP-MIB:OSPF-TRAP-MIB"


    class Ospftrapcontrol(Entity):
        """
        
        
        .. attribute:: ospfsettrap
        
        	A 4\-octet string serving as a bit map for the trap events defined by the OSPF traps.  This object is used to enable and disable specific OSPF traps where a 1 in the bit field represents enabled.  The right\-most bit (least significant) represents trap 0.  This object is persistent and when written  the entity SHOULD save the change to non\-volatile storage
        	**type**\: str
        
        	**length:** 4
        
        .. attribute:: ospfconfigerrortype
        
        	Potential types of configuration conflicts. Used by the ospfConfigError and ospfConfigVirtError traps.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:  :py:class:`Ospfconfigerrortype <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OSPFTRAPMIB.Ospftrapcontrol.Ospfconfigerrortype>`
        
        .. attribute:: ospfpackettype
        
        	OSPF packet types.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:  :py:class:`Ospfpackettype <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OSPFTRAPMIB.Ospftrapcontrol.Ospfpackettype>`
        
        .. attribute:: ospfpacketsrc
        
        	The IP address of an inbound packet that cannot be identified by a neighbor instance.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'OSPF-TRAP-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OSPFTRAPMIB.Ospftrapcontrol, self).__init__()

            self.yang_name = "ospfTrapControl"
            self.yang_parent_name = "OSPF-TRAP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ospfsettrap', YLeaf(YType.str, 'ospfSetTrap')),
                ('ospfconfigerrortype', YLeaf(YType.enumeration, 'ospfConfigErrorType')),
                ('ospfpackettype', YLeaf(YType.enumeration, 'ospfPacketType')),
                ('ospfpacketsrc', YLeaf(YType.str, 'ospfPacketSrc')),
            ])
            self.ospfsettrap = None
            self.ospfconfigerrortype = None
            self.ospfpackettype = None
            self.ospfpacketsrc = None
            self._segment_path = lambda: "ospfTrapControl"
            self._absolute_path = lambda: "OSPF-TRAP-MIB:OSPF-TRAP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OSPFTRAPMIB.Ospftrapcontrol, ['ospfsettrap', 'ospfconfigerrortype', 'ospfpackettype', 'ospfpacketsrc'], name, value)

        class Ospfconfigerrortype(Enum):
            """
            Ospfconfigerrortype (Enum Class)

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

            duplicateRouterId = Enum.YLeaf(12, "duplicateRouterId")

            noError = Enum.YLeaf(13, "noError")


        class Ospfpackettype(Enum):
            """
            Ospfpackettype (Enum Class)

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

            hello = Enum.YLeaf(1, "hello")

            dbDescript = Enum.YLeaf(2, "dbDescript")

            lsReq = Enum.YLeaf(3, "lsReq")

            lsUpdate = Enum.YLeaf(4, "lsUpdate")

            lsAck = Enum.YLeaf(5, "lsAck")

            nullPacket = Enum.YLeaf(6, "nullPacket")


    def clone_ptr(self):
        self._top_entity = OSPFTRAPMIB()
        return self._top_entity


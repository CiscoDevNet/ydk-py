""" OSPF_TRAP_MIB 

The MIB module to describe traps for the OSPF
Version 2 Protocol.

Copyright (C) The IETF Trust (2006).
This version of this MIB module is part of
RFC 4750;  see the RFC itself for full legal
notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OspfTrapMib(Entity):
    """
    
    
    .. attribute:: ospftrapcontrol
    
    	
    	**type**\:   :py:class:`Ospftrapcontrol <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol>`
    
    

    """

    _prefix = 'OSPF-TRAP-MIB'
    _revision = '2006-11-10'

    def __init__(self):
        super(OspfTrapMib, self).__init__()
        self._top_entity = None

        self.yang_name = "OSPF-TRAP-MIB"
        self.yang_parent_name = "OSPF-TRAP-MIB"

        self.ospftrapcontrol = OspfTrapMib.Ospftrapcontrol()
        self.ospftrapcontrol.parent = self
        self._children_name_map["ospftrapcontrol"] = "ospfTrapControl"
        self._children_yang_names.add("ospfTrapControl")


    class Ospftrapcontrol(Entity):
        """
        
        
        .. attribute:: ospfconfigerrortype
        
        	Potential types of configuration conflicts. Used by the ospfConfigError and ospfConfigVirtError traps.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:   :py:class:`Ospfconfigerrortype <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol.Ospfconfigerrortype>`
        
        .. attribute:: ospfpacketsrc
        
        	The IP address of an inbound packet that cannot be identified by a neighbor instance.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: ospfpackettype
        
        	OSPF packet types.  When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:   :py:class:`Ospfpackettype <ydk.models.cisco_ios_xe.OSPF_TRAP_MIB.OspfTrapMib.Ospftrapcontrol.Ospfpackettype>`
        
        .. attribute:: ospfsettrap
        
        	A 4\-octet string serving as a bit map for the trap events defined by the OSPF traps.  This object is used to enable and disable specific OSPF traps where a 1 in the bit field represents enabled.  The right\-most bit (least significant) represents trap 0.  This object is persistent and when written  the entity SHOULD save the change to non\-volatile storage
        	**type**\:  str
        
        	**length:** 4
        
        

        """

        _prefix = 'OSPF-TRAP-MIB'
        _revision = '2006-11-10'

        def __init__(self):
            super(OspfTrapMib.Ospftrapcontrol, self).__init__()

            self.yang_name = "ospfTrapControl"
            self.yang_parent_name = "OSPF-TRAP-MIB"

            self.ospfconfigerrortype = YLeaf(YType.enumeration, "ospfConfigErrorType")

            self.ospfpacketsrc = YLeaf(YType.str, "ospfPacketSrc")

            self.ospfpackettype = YLeaf(YType.enumeration, "ospfPacketType")

            self.ospfsettrap = YLeaf(YType.str, "ospfSetTrap")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ospfconfigerrortype",
                            "ospfpacketsrc",
                            "ospfpackettype",
                            "ospfsettrap") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(OspfTrapMib.Ospftrapcontrol, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(OspfTrapMib.Ospftrapcontrol, self).__setattr__(name, value)

        class Ospfconfigerrortype(Enum):
            """
            Ospfconfigerrortype

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
            Ospfpackettype

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


        def has_data(self):
            return (
                self.ospfconfigerrortype.is_set or
                self.ospfpacketsrc.is_set or
                self.ospfpackettype.is_set or
                self.ospfsettrap.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ospfconfigerrortype.yfilter != YFilter.not_set or
                self.ospfpacketsrc.yfilter != YFilter.not_set or
                self.ospfpackettype.yfilter != YFilter.not_set or
                self.ospfsettrap.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ospfTrapControl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "OSPF-TRAP-MIB:OSPF-TRAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ospfconfigerrortype.is_set or self.ospfconfigerrortype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfconfigerrortype.get_name_leafdata())
            if (self.ospfpacketsrc.is_set or self.ospfpacketsrc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfpacketsrc.get_name_leafdata())
            if (self.ospfpackettype.is_set or self.ospfpackettype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfpackettype.get_name_leafdata())
            if (self.ospfsettrap.is_set or self.ospfsettrap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ospfsettrap.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ospfConfigErrorType" or name == "ospfPacketSrc" or name == "ospfPacketType" or name == "ospfSetTrap"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ospfConfigErrorType"):
                self.ospfconfigerrortype = value
                self.ospfconfigerrortype.value_namespace = name_space
                self.ospfconfigerrortype.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfPacketSrc"):
                self.ospfpacketsrc = value
                self.ospfpacketsrc.value_namespace = name_space
                self.ospfpacketsrc.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfPacketType"):
                self.ospfpackettype = value
                self.ospfpackettype.value_namespace = name_space
                self.ospfpackettype.value_namespace_prefix = name_space_prefix
            if(value_path == "ospfSetTrap"):
                self.ospfsettrap = value
                self.ospfsettrap.value_namespace = name_space
                self.ospfsettrap.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.ospftrapcontrol is not None and self.ospftrapcontrol.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ospftrapcontrol is not None and self.ospftrapcontrol.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "OSPF-TRAP-MIB:OSPF-TRAP-MIB" + path_buffer

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

        if (child_yang_name == "ospfTrapControl"):
            if (self.ospftrapcontrol is None):
                self.ospftrapcontrol = OspfTrapMib.Ospftrapcontrol()
                self.ospftrapcontrol.parent = self
                self._children_name_map["ospftrapcontrol"] = "ospfTrapControl"
            return self.ospftrapcontrol

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ospfTrapControl"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = OspfTrapMib()
        return self._top_entity


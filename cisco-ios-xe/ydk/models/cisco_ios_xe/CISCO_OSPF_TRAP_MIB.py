""" CISCO_OSPF_TRAP_MIB 

This MIB module describes new/modified notification
objects/events, which are defined in the latest
version for OSPF MIB IETF draft
draftietf\-ospf\-mib\-update\-05.txt. Support for OSPF 
Sham link is also added

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoOspfTrapMib(Entity):
    """
    
    
    .. attribute:: cospftrapcontrol
    
    	
    	**type**\:   :py:class:`Cospftrapcontrol <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol>`
    
    

    """

    _prefix = 'CISCO-OSPF-TRAP-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        super(CiscoOspfTrapMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-OSPF-TRAP-MIB"
        self.yang_parent_name = "CISCO-OSPF-TRAP-MIB"

        self.cospftrapcontrol = CiscoOspfTrapMib.Cospftrapcontrol()
        self.cospftrapcontrol.parent = self
        self._children_name_map["cospftrapcontrol"] = "cospfTrapControl"
        self._children_yang_names.add("cospfTrapControl")


    class Cospftrapcontrol(Entity):
        """
        
        
        .. attribute:: cospfconfigerrortype
        
        	Potential types of configuration conflicts. Used  by the cospfConfigError and cospfConfigVirtError traps. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as noError
        	**type**\:   :py:class:`Cospfconfigerrortype <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.Cospfconfigerrortype>`
        
        .. attribute:: cospfpacketsrc
        
        	The IP address of an inbound packet that can\- not be identified by a neighbor instance. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as 0.0.0.0
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: cospfpackettype
        
        	OSPF packet types. When the last value of a trap using this object is needed, but no traps of that type have been sent, this value pertaining to this object should be returned as nullPacket
        	**type**\:   :py:class:`Cospfpackettype <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.Cospfpackettype>`
        
        .. attribute:: cospfsettrap
        
        	An octet string serving as a bit  map  for the trap events defined by the OSPF traps in  this MIB. This object is used to enable and   disable  specific OSPF   traps   where  a  1   in  the  corresponding bit  field represents  enabled
        	**type**\:   :py:class:`Cospfsettrap <ydk.models.cisco_ios_xe.CISCO_OSPF_TRAP_MIB.CiscoOspfTrapMib.Cospftrapcontrol.Cospfsettrap>`
        
        

        """

        _prefix = 'CISCO-OSPF-TRAP-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfTrapMib.Cospftrapcontrol, self).__init__()

            self.yang_name = "cospfTrapControl"
            self.yang_parent_name = "CISCO-OSPF-TRAP-MIB"

            self.cospfconfigerrortype = YLeaf(YType.enumeration, "cospfConfigErrorType")

            self.cospfpacketsrc = YLeaf(YType.str, "cospfPacketSrc")

            self.cospfpackettype = YLeaf(YType.enumeration, "cospfPacketType")

            self.cospfsettrap = YLeaf(YType.bits, "cospfSetTrap")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cospfconfigerrortype",
                            "cospfpacketsrc",
                            "cospfpackettype",
                            "cospfsettrap") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoOspfTrapMib.Cospftrapcontrol, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfTrapMib.Cospftrapcontrol, self).__setattr__(name, value)

        class Cospfconfigerrortype(Enum):
            """
            Cospfconfigerrortype

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
            Cospfpackettype

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


        def has_data(self):
            return (
                self.cospfconfigerrortype.is_set or
                self.cospfpacketsrc.is_set or
                self.cospfpackettype.is_set or
                self.cospfsettrap.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cospfconfigerrortype.yfilter != YFilter.not_set or
                self.cospfpacketsrc.yfilter != YFilter.not_set or
                self.cospfpackettype.yfilter != YFilter.not_set or
                self.cospfsettrap.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfTrapControl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cospfconfigerrortype.is_set or self.cospfconfigerrortype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfconfigerrortype.get_name_leafdata())
            if (self.cospfpacketsrc.is_set or self.cospfpacketsrc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfpacketsrc.get_name_leafdata())
            if (self.cospfpackettype.is_set or self.cospfpackettype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfpackettype.get_name_leafdata())
            if (self.cospfsettrap.is_set or self.cospfsettrap.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfsettrap.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfConfigErrorType" or name == "cospfPacketSrc" or name == "cospfPacketType" or name == "cospfSetTrap"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cospfConfigErrorType"):
                self.cospfconfigerrortype = value
                self.cospfconfigerrortype.value_namespace = name_space
                self.cospfconfigerrortype.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfPacketSrc"):
                self.cospfpacketsrc = value
                self.cospfpacketsrc.value_namespace = name_space
                self.cospfpacketsrc.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfPacketType"):
                self.cospfpackettype = value
                self.cospfpackettype.value_namespace = name_space
                self.cospfpackettype.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfSetTrap"):
                self.cospfsettrap[value] = True

    def has_data(self):
        return (self.cospftrapcontrol is not None and self.cospftrapcontrol.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cospftrapcontrol is not None and self.cospftrapcontrol.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-OSPF-TRAP-MIB:CISCO-OSPF-TRAP-MIB" + path_buffer

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

        if (child_yang_name == "cospfTrapControl"):
            if (self.cospftrapcontrol is None):
                self.cospftrapcontrol = CiscoOspfTrapMib.Cospftrapcontrol()
                self.cospftrapcontrol.parent = self
                self._children_name_map["cospftrapcontrol"] = "cospfTrapControl"
            return self.cospftrapcontrol

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cospfTrapControl"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoOspfTrapMib()
        return self._top_entity


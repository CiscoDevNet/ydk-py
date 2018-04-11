""" CISCO_PIM_MIB 

This MIB module defines the cisco specific variables
for Protocol Independent Multicast (PIM) management. 
These definitions are an extension of those defined in
the IETF PIM MIB (RFC 2934).

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOPIMMIB(Entity):
    """
    
    
    .. attribute:: cpim
    
    	
    	**type**\:  :py:class:`Cpim <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CISCOPIMMIB.Cpim>`
    
    .. attribute:: ciscopimmibnotificationobjects
    
    	
    	**type**\:  :py:class:`Ciscopimmibnotificationobjects <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CISCOPIMMIB.Ciscopimmibnotificationobjects>`
    
    

    """

    _prefix = 'CISCO-PIM-MIB'
    _revision = '2000-11-02'

    def __init__(self):
        super(CISCOPIMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PIM-MIB"
        self.yang_parent_name = "CISCO-PIM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cpim", ("cpim", CISCOPIMMIB.Cpim)), ("ciscoPimMIBNotificationObjects", ("ciscopimmibnotificationobjects", CISCOPIMMIB.Ciscopimmibnotificationobjects))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cpim = CISCOPIMMIB.Cpim()
        self.cpim.parent = self
        self._children_name_map["cpim"] = "cpim"
        self._children_yang_names.add("cpim")

        self.ciscopimmibnotificationobjects = CISCOPIMMIB.Ciscopimmibnotificationobjects()
        self.ciscopimmibnotificationobjects.parent = self
        self._children_name_map["ciscopimmibnotificationobjects"] = "ciscoPimMIBNotificationObjects"
        self._children_yang_names.add("ciscoPimMIBNotificationObjects")
        self._segment_path = lambda: "CISCO-PIM-MIB:CISCO-PIM-MIB"


    class Cpim(Entity):
        """
        
        
        .. attribute:: cpiminvalidregistermsgsrcvd
        
        	A count of the number of invalid PIM Register messages received by this device. A PIM Register message is termed invalid if  o the encapsulated IP header is malformed, o the destination of the PIM Register message is not the   RP (Rendezvous Point) for the group in question, o the source/DR (Designated Router) address is not a valid   unicast address
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpiminvalidjoinprunemsgsrcvd
        
        	A count of the number of invalid PIM Join/Prune messages received by this device. A PIM Join/Prune message is termed invalid if  o the RP specified in the packet is not the RP for   the group in question
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpimlasterrortype
        
        	The type of the last invalid message that was received by this device
        	**type**\:  :py:class:`Cpimlasterrortype <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CISCOPIMMIB.Cpim.Cpimlasterrortype>`
        
        .. attribute:: cpimlasterrororigintype
        
        	Represents the type of address stored in cpimLastErrorOrigin. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: cpimlasterrororigin
        
        	This object represents the Network Layer Address of the source that originated the last invalid packet. The type of address stored depends on the value in cpimLastErrorOriginType.   The value of this object represents the Network Layer Address of the Designated Router (DR) whenever the value of cpimLastErrorGroup is a zero\-length address,  for eg. when encapsulated IP header is malformed.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorgrouptype
        
        	Represents the type of address stored in cpimLastErrorGroup. The value of this object is unknown(0) if there is a problem in the packet received from the DR.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: cpimlasterrorgroup
        
        	The IP multicast group address to which the last invalid packet was addressed. The type of address stored depends on the value in cpimLastErrorGroupType.   The value of this object is a zero\-length InetAddress if there is a problem in the packet received from the DR, for eg. a malformed encapsulated IP header.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorrptype
        
        	Represents the type of address stored in cpimLastErrorRP. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: cpimlasterrorrp
        
        	The address of the RP, as per the last invalid packet. The type of address stored depends on the value in cpimLastErrorRPType.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\: str
        
        	**length:** 0..255
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            super(CISCOPIMMIB.Cpim, self).__init__()

            self.yang_name = "cpim"
            self.yang_parent_name = "CISCO-PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpiminvalidregistermsgsrcvd', YLeaf(YType.uint32, 'cpimInvalidRegisterMsgsRcvd')),
                ('cpiminvalidjoinprunemsgsrcvd', YLeaf(YType.uint32, 'cpimInvalidJoinPruneMsgsRcvd')),
                ('cpimlasterrortype', YLeaf(YType.enumeration, 'cpimLastErrorType')),
                ('cpimlasterrororigintype', YLeaf(YType.enumeration, 'cpimLastErrorOriginType')),
                ('cpimlasterrororigin', YLeaf(YType.str, 'cpimLastErrorOrigin')),
                ('cpimlasterrorgrouptype', YLeaf(YType.enumeration, 'cpimLastErrorGroupType')),
                ('cpimlasterrorgroup', YLeaf(YType.str, 'cpimLastErrorGroup')),
                ('cpimlasterrorrptype', YLeaf(YType.enumeration, 'cpimLastErrorRPType')),
                ('cpimlasterrorrp', YLeaf(YType.str, 'cpimLastErrorRP')),
            ])
            self.cpiminvalidregistermsgsrcvd = None
            self.cpiminvalidjoinprunemsgsrcvd = None
            self.cpimlasterrortype = None
            self.cpimlasterrororigintype = None
            self.cpimlasterrororigin = None
            self.cpimlasterrorgrouptype = None
            self.cpimlasterrorgroup = None
            self.cpimlasterrorrptype = None
            self.cpimlasterrorrp = None
            self._segment_path = lambda: "cpim"
            self._absolute_path = lambda: "CISCO-PIM-MIB:CISCO-PIM-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPIMMIB.Cpim, ['cpiminvalidregistermsgsrcvd', 'cpiminvalidjoinprunemsgsrcvd', 'cpimlasterrortype', 'cpimlasterrororigintype', 'cpimlasterrororigin', 'cpimlasterrorgrouptype', 'cpimlasterrorgroup', 'cpimlasterrorrptype', 'cpimlasterrorrp'], name, value)

        class Cpimlasterrortype(Enum):
            """
            Cpimlasterrortype (Enum Class)

            The type of the last invalid message that was received by

            this device.

            .. data:: none = 1

            .. data:: invalidRegister = 2

            .. data:: invalidJoinPrune = 3

            """

            none = Enum.YLeaf(1, "none")

            invalidRegister = Enum.YLeaf(2, "invalidRegister")

            invalidJoinPrune = Enum.YLeaf(3, "invalidJoinPrune")



    class Ciscopimmibnotificationobjects(Entity):
        """
        
        
        .. attribute:: cpimrpmappingchangetype
        
        	Describes the operation that resulted in generation of cpimRPMappingChange notification.  o newMapping, as the name suggests indicates that a new   mapping has been added into the pimRPSetTable,  o deletedMapping indicates that a mapping has been    deleted from the pimRPSetTable, and, o modifiedXXXMapping indicates that an RP mapping (which   already existed in the table) has been modified.   The two modifications types i.e. modifiedOldMapping   and modifiedNewMapping, are defined to differentiate   the notification generated before modification from   that generated after modification
        	**type**\:  :py:class:`Cpimrpmappingchangetype <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CISCOPIMMIB.Ciscopimmibnotificationobjects.Cpimrpmappingchangetype>`
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            super(CISCOPIMMIB.Ciscopimmibnotificationobjects, self).__init__()

            self.yang_name = "ciscoPimMIBNotificationObjects"
            self.yang_parent_name = "CISCO-PIM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpimrpmappingchangetype', YLeaf(YType.enumeration, 'cpimRPMappingChangeType')),
            ])
            self.cpimrpmappingchangetype = None
            self._segment_path = lambda: "ciscoPimMIBNotificationObjects"
            self._absolute_path = lambda: "CISCO-PIM-MIB:CISCO-PIM-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPIMMIB.Ciscopimmibnotificationobjects, ['cpimrpmappingchangetype'], name, value)

        class Cpimrpmappingchangetype(Enum):
            """
            Cpimrpmappingchangetype (Enum Class)

            Describes the operation that resulted in generation

            of cpimRPMappingChange notification.

            o newMapping, as the name suggests indicates that a new

              mapping has been added into the pimRPSetTable, 

            o deletedMapping indicates that a mapping has been 

              deleted from the pimRPSetTable, and,

            o modifiedXXXMapping indicates that an RP mapping (which

              already existed in the table) has been modified.

              The two modifications types i.e. modifiedOldMapping

              and modifiedNewMapping, are defined to differentiate

              the notification generated before modification from

              that generated after modification.

            .. data:: newMapping = 1

            .. data:: deletedMapping = 2

            .. data:: modifiedOldMapping = 3

            .. data:: modifiedNewMapping = 4

            """

            newMapping = Enum.YLeaf(1, "newMapping")

            deletedMapping = Enum.YLeaf(2, "deletedMapping")

            modifiedOldMapping = Enum.YLeaf(3, "modifiedOldMapping")

            modifiedNewMapping = Enum.YLeaf(4, "modifiedNewMapping")


    def clone_ptr(self):
        self._top_entity = CISCOPIMMIB()
        return self._top_entity


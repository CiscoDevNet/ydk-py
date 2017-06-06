""" CISCO_PIM_MIB 

This MIB module defines the cisco specific variables
for Protocol Independent Multicast (PIM) management. 
These definitions are an extension of those defined in
the IETF PIM MIB (RFC 2934).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoPimMib(object):
    """
    
    
    .. attribute:: ciscopimmibnotificationobjects
    
    	
    	**type**\:   :py:class:`Ciscopimmibnotificationobjects <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Ciscopimmibnotificationobjects>`
    
    .. attribute:: cpim
    
    	
    	**type**\:   :py:class:`Cpim <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Cpim>`
    
    

    """

    _prefix = 'CISCO-PIM-MIB'
    _revision = '2000-11-02'

    def __init__(self):
        self.ciscopimmibnotificationobjects = CiscoPimMib.Ciscopimmibnotificationobjects()
        self.ciscopimmibnotificationobjects.parent = self
        self.cpim = CiscoPimMib.Cpim()
        self.cpim.parent = self


    class Cpim(object):
        """
        
        
        .. attribute:: cpiminvalidjoinprunemsgsrcvd
        
        	A count of the number of invalid PIM Join/Prune messages received by this device. A PIM Join/Prune message is termed invalid if  o the RP specified in the packet is not the RP for   the group in question
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpiminvalidregistermsgsrcvd
        
        	A count of the number of invalid PIM Register messages received by this device. A PIM Register message is termed invalid if  o the encapsulated IP header is malformed, o the destination of the PIM Register message is not the   RP (Rendezvous Point) for the group in question, o the source/DR (Designated Router) address is not a valid   unicast address
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpimlasterrorgroup
        
        	The IP multicast group address to which the last invalid packet was addressed. The type of address stored depends on the value in cpimLastErrorGroupType.   The value of this object is a zero\-length InetAddress if there is a problem in the packet received from the DR, for eg. a malformed encapsulated IP header.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorgrouptype
        
        	Represents the type of address stored in cpimLastErrorGroup. The value of this object is unknown(0) if there is a problem in the packet received from the DR.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
        
        .. attribute:: cpimlasterrororigin
        
        	This object represents the Network Layer Address of the source that originated the last invalid packet. The type of address stored depends on the value in cpimLastErrorOriginType.   The value of this object represents the Network Layer Address of the Designated Router (DR) whenever the value of cpimLastErrorGroup is a zero\-length address,  for eg. when encapsulated IP header is malformed.  The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrororigintype
        
        	Represents the type of address stored in cpimLastErrorOrigin. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
        
        .. attribute:: cpimlasterrorrp
        
        	The address of the RP, as per the last invalid packet. The type of address stored depends on the value in cpimLastErrorRPType.   The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cpimlasterrorrptype
        
        	Represents the type of address stored in cpimLastErrorRP. The value of this object is irrelevant if the value of cpimLastErrorType is none(1)
        	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
        
        .. attribute:: cpimlasterrortype
        
        	The type of the last invalid message that was received by this device
        	**type**\:   :py:class:`CpimlasterrortypeEnum <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Cpim.CpimlasterrortypeEnum>`
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            self.parent = None
            self.cpiminvalidjoinprunemsgsrcvd = None
            self.cpiminvalidregistermsgsrcvd = None
            self.cpimlasterrorgroup = None
            self.cpimlasterrorgrouptype = None
            self.cpimlasterrororigin = None
            self.cpimlasterrororigintype = None
            self.cpimlasterrorrp = None
            self.cpimlasterrorrptype = None
            self.cpimlasterrortype = None

        class CpimlasterrortypeEnum(Enum):
            """
            CpimlasterrortypeEnum

            The type of the last invalid message that was received by

            this device.

            .. data:: none = 1

            .. data:: invalidRegister = 2

            .. data:: invalidJoinPrune = 3

            """

            none = 1

            invalidRegister = 2

            invalidJoinPrune = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PIM_MIB as meta
                return meta._meta_table['CiscoPimMib.Cpim.CpimlasterrortypeEnum']


        @property
        def _common_path(self):

            return '/CISCO-PIM-MIB:CISCO-PIM-MIB/CISCO-PIM-MIB:cpim'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpiminvalidjoinprunemsgsrcvd is not None:
                return True

            if self.cpiminvalidregistermsgsrcvd is not None:
                return True

            if self.cpimlasterrorgroup is not None:
                return True

            if self.cpimlasterrorgrouptype is not None:
                return True

            if self.cpimlasterrororigin is not None:
                return True

            if self.cpimlasterrororigintype is not None:
                return True

            if self.cpimlasterrorrp is not None:
                return True

            if self.cpimlasterrorrptype is not None:
                return True

            if self.cpimlasterrortype is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PIM_MIB as meta
            return meta._meta_table['CiscoPimMib.Cpim']['meta_info']


    class Ciscopimmibnotificationobjects(object):
        """
        
        
        .. attribute:: cpimrpmappingchangetype
        
        	Describes the operation that resulted in generation of cpimRPMappingChange notification.  o newMapping, as the name suggests indicates that a new   mapping has been added into the pimRPSetTable,  o deletedMapping indicates that a mapping has been    deleted from the pimRPSetTable, and, o modifiedXXXMapping indicates that an RP mapping (which   already existed in the table) has been modified.   The two modifications types i.e. modifiedOldMapping   and modifiedNewMapping, are defined to differentiate   the notification generated before modification from   that generated after modification
        	**type**\:   :py:class:`CpimrpmappingchangetypeEnum <ydk.models.cisco_ios_xe.CISCO_PIM_MIB.CiscoPimMib.Ciscopimmibnotificationobjects.CpimrpmappingchangetypeEnum>`
        
        

        """

        _prefix = 'CISCO-PIM-MIB'
        _revision = '2000-11-02'

        def __init__(self):
            self.parent = None
            self.cpimrpmappingchangetype = None

        class CpimrpmappingchangetypeEnum(Enum):
            """
            CpimrpmappingchangetypeEnum

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

            newMapping = 1

            deletedMapping = 2

            modifiedOldMapping = 3

            modifiedNewMapping = 4


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_PIM_MIB as meta
                return meta._meta_table['CiscoPimMib.Ciscopimmibnotificationobjects.CpimrpmappingchangetypeEnum']


        @property
        def _common_path(self):

            return '/CISCO-PIM-MIB:CISCO-PIM-MIB/CISCO-PIM-MIB:ciscoPimMIBNotificationObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cpimrpmappingchangetype is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_PIM_MIB as meta
            return meta._meta_table['CiscoPimMib.Ciscopimmibnotificationobjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PIM-MIB:CISCO-PIM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ciscopimmibnotificationobjects is not None and self.ciscopimmibnotificationobjects._has_data():
            return True

        if self.cpim is not None and self.cpim._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_PIM_MIB as meta
        return meta._meta_table['CiscoPimMib']['meta_info']



""" CISCO_IGMP_FILTER_MIB 

IGMP Filter configuration MIB. This MIB provides a
mechanism for users to configure the system to intercept 
IGMP joins for IP Multicast groups identified in this 
MIB and only allow certain ports to join certain 
multicast groups.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoIgmpFilterMib(object):
    """
    
    
    .. attribute:: cigmpfiltereditor
    
    	
    	**type**\:   :py:class:`Cigmpfiltereditor <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor>`
    
    .. attribute:: cigmpfiltergeneral
    
    	
    	**type**\:   :py:class:`Cigmpfiltergeneral <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltergeneral>`
    
    .. attribute:: cigmpfilterinterfacetable
    
    	This table contains the list of interfaces that can support IGMP filter feature
    	**type**\:   :py:class:`Cigmpfilterinterfacetable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfilterinterfacetable>`
    
    .. attribute:: cigmpfiltertable
    
    	This table contains entries that identify lists of IP Multicast groups for each profile configured on the device.   Each entry contains a range of contiguous IP Multicast groups associated to a profile index. Multiple cIgmpFilterEntry may be associated with the same cIgmpFilterProfileIndex.  All the cIgmpFilterEntry with  the same profile index  are subjected to the same IGMP filtering action as  defined in cIgmpFilterProfileAction.  Each profile index may be associated with zero or more  interfaces through cIgmpFilterInterfaceIfIndex object in cIgmpFilterInterfaceTable. The maximum number of entries is determined by cIgmpFilterMaxProfiles
    	**type**\:   :py:class:`Cigmpfiltertable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable>`
    
    

    """

    _prefix = 'CISCO-IGMP-FILTER-MIB'
    _revision = '2005-11-29'

    def __init__(self):
        self.cigmpfiltereditor = CiscoIgmpFilterMib.Cigmpfiltereditor()
        self.cigmpfiltereditor.parent = self
        self.cigmpfiltergeneral = CiscoIgmpFilterMib.Cigmpfiltergeneral()
        self.cigmpfiltergeneral.parent = self
        self.cigmpfilterinterfacetable = CiscoIgmpFilterMib.Cigmpfilterinterfacetable()
        self.cigmpfilterinterfacetable.parent = self
        self.cigmpfiltertable = CiscoIgmpFilterMib.Cigmpfiltertable()
        self.cigmpfiltertable.parent = self


    class Cigmpfiltergeneral(object):
        """
        
        
        .. attribute:: cigmpfilterenable
        
        	This object controls whether the IGMP filtering is enabled on the device. A false(2) value will  prevent the IGMP filtering action on the device
        	**type**\:  bool
        
        .. attribute:: cigmpfiltermaxprofiles
        
        	Indicates the maximum number of profiles supported by this device.  A value of zero indicates no limitation on the number of profiles
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: profiles
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterenable = None
            self.cigmpfiltermaxprofiles = None

        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterGeneral'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cigmpfilterenable is not None:
                return True

            if self.cigmpfiltermaxprofiles is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltergeneral']['meta_info']


    class Cigmpfiltereditor(object):
        """
        
        
        .. attribute:: cigmpfilterapplystatus
        
        	The current status of an 'add', 'delete' or 'modify' operation. If no apply is currently active, the status  represented is that of the most recently completed 'add',  'delete' or 'modify' operation.  The value of this objects indicates succeeded(2) state  initially when no 'add', 'delete', 'modify' operation has been carried out.  The possible values are\:    someOtherError \- the 'add', 'delete' or 'modify' failed     due to undefined error(s) in apply operation.    (e.g., insufficient memory).      succeeded \- the 'add', 'delete' or 'modify' operation    was successful. (This value is also used when no    apply has been invoked since the last time the local     system restarted.)     inconsistentEdit \- the 'add', 'delete' or 'modify' failed    due to inconsistency of the data.     entryPresentError \- the 'add' operation failed  as the     corresponding entry already exists in cIgmpFilterTable.     entryNotPresentError \- the 'modify' operation failed     as no corresponding entry exists in cIgmpFilterTable
        	**type**\:   :py:class:`CigmpfilterapplystatusEnum <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfilterapplystatusEnum>`
        
        .. attribute:: cigmpfiltereditendaddress
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddress in cIgmpFilterTable  to establish end address of filtering  range for a profile
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cigmpfiltereditendaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddressType in cIgmpFilterTable.  This object describes the type of Internet      address used to determine the start address  of IP multicast group for a profile
        	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
        
        .. attribute:: cigmpfiltereditoperation
        
        	The function of this object is to allow user to apply the changes in cIgmpFilterEditor objects to  cIgmpFilterTable.   This object always has the value 'none' when read. When written each value causes the appropriate action\:  'add' \- tries to insert the information contained  in cIgmpFilterEditor objects into  cIgmpFilterTable. If the entry already exists in the table the 'add'  fails.          'delete' \- tries to delete corresponding entry from cIgmpFilterTable. If a user completely deletes a profile that has corresponding entries in the cIgmpFilterInterfaceTable, then all the interfaces mapped to corresponding profile will be cleared and set to zero.  'modify' \- Mode of operation used to edit an entry in  cIgmpFilterTable. If the corresponding entry does not   exist, modify operation fails. This mode allows user to  extend/truncate a contiguous filtered range, type of  Internet addressing and filtering action for a profile.   'none' \- no operation is performed
        	**type**\:   :py:class:`CigmpfiltereditoperationEnum <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfiltereditoperationEnum>`
        
        .. attribute:: cigmpfiltereditprofileaction
        
        	Buffer object to edit corresponding object in cIgmpFilterTable to determine filtering action of each profile
        	**type**\:   :py:class:`CigmpfiltereditprofileactionEnum <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfiltereditprofileactionEnum>`
        
        .. attribute:: cigmpfiltereditprofileindex
        
        	Buffer object to edit corresponding object cIgmpFilterProfileIndex in cIgmpFilterTable.  Maximum value this object can be set to is  determined by cIgmpFilterMaxProfiles object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cigmpfiltereditspinlock
        
        	This object is used to facilitate modification of IGMP Filter Editor Group in the CISCO\-IGMP\-FILTER\-MIB  module by multiple managers.  In particular, it is  useful when modifying the value of the cIgmpFilterEditor  object.   The procedure for modifying the cIgmpFilterEditor  object is as follows\:       1.  Retrieve the value of cIgmpFilterEditSpinLock and          of object within cIgmpFilterEditor group.       2.  Generate new values for 'writeable' objects         in the cIgmpFilterEditor group except for          cIgmpFilterEditSpinLock object.      3.  Set the value of cIgmpFilterEditSpinLock to the          retrieved value, and the value of objects in          cIgmpFilterEditor to the new value. If the set         fails for the cIgmpFilterEditSpinLock object,         go back to step 1.   The cIgmpFilterApplyStatus and cIgmpFilterEditSpinLock  should be read together by NMS to make sure that the  result is associated with its configuration request.  To add/delete or modify a profile ( through cIgmpFilterEditor objects ) following procedure may be followed as an example.\:      1.  GET(cIgmpFilterEditSpinLock.0) and save in sValue.     2.  SET(cIgmpFilterEditSpinLock.0 = sValue,             cIgmpFilterEditProfileIndex.0 = validProfileNumber,             cIgmpFilterEditStartAddress.0 = validStartAddress,             cIgmpFilterEditEndAddress.0 = validEndAddress,             cIgmpFilterEditOperation.0 =  validOperation)     3.  If the SET in step 2 is not successful go back         to step 1.     4.  If the SET in step 2 is successful, user should          GET(cIgmpFilterEditSpinLock.0) and          GET(cIgmpFilterApplyStatus.0) simultaneously.      5.  The cIgmpFilterApplyStatus.0 reflects the outcome of         step 2 only if         cIgmpFilterEditSpinLock.0 = sValue + 1 or         cIgmpFilterEditSpinLock.0 = 0 if sValue reaches         value at which cIgmpFilterEditSpinLock wraps          around
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: cigmpfiltereditstartaddress
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddress in cIgmpFilterTable   to establish start address of filtering range for a profile
        	**type**\:  str
        
        	**length:** 1..64
        
        .. attribute:: cigmpfiltereditstartaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddressType in cIgmpFilterTable.  This object describes the type of Internet   address used to determine the start address  of IP multicast group for a profile
        	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterapplystatus = None
            self.cigmpfiltereditendaddress = None
            self.cigmpfiltereditendaddresstype = None
            self.cigmpfiltereditoperation = None
            self.cigmpfiltereditprofileaction = None
            self.cigmpfiltereditprofileindex = None
            self.cigmpfiltereditspinlock = None
            self.cigmpfiltereditstartaddress = None
            self.cigmpfiltereditstartaddresstype = None

        class CigmpfilterapplystatusEnum(Enum):
            """
            CigmpfilterapplystatusEnum

            The current status of an 'add', 'delete' or 'modify'

            operation. If no apply is currently active, the status 

            represented is that of the most recently completed 'add', 

            'delete' or 'modify' operation.

            The value of this objects indicates succeeded(2) state 

            initially when no 'add', 'delete', 'modify' operation

            has been carried out.

            The possible values are\:

               someOtherError \- the 'add', 'delete' or 'modify' failed 

               due to undefined error(s) in apply operation.

               (e.g., insufficient memory). 

               succeeded \- the 'add', 'delete' or 'modify' operation

               was successful. (This value is also used when no

               apply has been invoked since the last time the local 

               system restarted.)

               inconsistentEdit \- the 'add', 'delete' or 'modify' failed

               due to inconsistency of the data.

               entryPresentError \- the 'add' operation failed  as the 

               corresponding entry already exists in cIgmpFilterTable.

               entryNotPresentError \- the 'modify' operation failed 

               as no corresponding entry exists in cIgmpFilterTable.

            .. data:: someOtherError = 1

            .. data:: succeeded = 2

            .. data:: inconsistentEdit = 3

            .. data:: entryPresentError = 4

            .. data:: entryNotPresentError = 5

            """

            someOtherError = 1

            succeeded = 2

            inconsistentEdit = 3

            entryPresentError = 4

            entryNotPresentError = 5


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfilterapplystatusEnum']


        class CigmpfiltereditoperationEnum(Enum):
            """
            CigmpfiltereditoperationEnum

            The function of this object is to allow user to

            apply the changes in cIgmpFilterEditor objects to 

            cIgmpFilterTable. 

            This object always has the value 'none' when read.

            When written each value causes the appropriate action\:

            'add' \- tries to insert the information contained 

            in cIgmpFilterEditor objects into  cIgmpFilterTable.

            If the entry already exists in the table the 'add' 

            fails.        

            'delete' \- tries to delete corresponding entry from

            cIgmpFilterTable. If a user completely deletes a profile

            that has corresponding entries in the

            cIgmpFilterInterfaceTable, then all the interfaces mapped

            to corresponding profile will be cleared and set to zero.

            'modify' \- Mode of operation used to edit an entry in

             cIgmpFilterTable. If the corresponding entry does not 

             exist, modify operation fails. This mode allows user to

             extend/truncate a contiguous filtered range, type of

             Internet addressing and filtering action for a profile. 

            'none' \- no operation is performed.

            .. data:: none = 1

            .. data:: add = 2

            .. data:: delete = 3

            .. data:: modify = 4

            """

            none = 1

            add = 2

            delete = 3

            modify = 4


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfiltereditoperationEnum']


        class CigmpfiltereditprofileactionEnum(Enum):
            """
            CigmpfiltereditprofileactionEnum

            Buffer object to edit corresponding object in

            cIgmpFilterTable to determine filtering action

            of each profile.

            .. data:: unSpecified = 0

            .. data:: permit = 1

            .. data:: deny = 2

            """

            unSpecified = 0

            permit = 1

            deny = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltereditor.CigmpfiltereditprofileactionEnum']


        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterEditor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cigmpfilterapplystatus is not None:
                return True

            if self.cigmpfiltereditendaddress is not None:
                return True

            if self.cigmpfiltereditendaddresstype is not None:
                return True

            if self.cigmpfiltereditoperation is not None:
                return True

            if self.cigmpfiltereditprofileaction is not None:
                return True

            if self.cigmpfiltereditprofileindex is not None:
                return True

            if self.cigmpfiltereditspinlock is not None:
                return True

            if self.cigmpfiltereditstartaddress is not None:
                return True

            if self.cigmpfiltereditstartaddresstype is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltereditor']['meta_info']


    class Cigmpfiltertable(object):
        """
        This table contains entries that identify lists of
        IP Multicast groups for each profile configured on
        the device. 
        
        Each entry contains a range of contiguous IP
        Multicast groups associated to a profile index.
        Multiple cIgmpFilterEntry may be associated
        with the same cIgmpFilterProfileIndex.
        
        All the cIgmpFilterEntry with  the same profile index 
        are subjected to the same IGMP filtering action as 
        defined in cIgmpFilterProfileAction.
        
        Each profile index may be associated with zero or more 
        interfaces through cIgmpFilterInterfaceIfIndex
        object in cIgmpFilterInterfaceTable.
        The maximum number of entries is determined by
        cIgmpFilterMaxProfiles.
        
        .. attribute:: cigmpfilterentry
        
        	An entry (conceptual row) in the cIgmpFilterTable.  The creation, deletion or modification of an entry is controlled through the MIB objects defined under cIgmpFilterEditor group
        	**type**\: list of    :py:class:`Cigmpfilterentry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterentry = YList()
            self.cigmpfilterentry.parent = self
            self.cigmpfilterentry.name = 'cigmpfilterentry'


        class Cigmpfilterentry(object):
            """
            An entry (conceptual row) in the cIgmpFilterTable.
            
            The creation, deletion or modification of an entry
            is controlled through the MIB objects defined under
            cIgmpFilterEditor group.
            
            .. attribute:: cigmpfilterprofileindex  <key>
            
            	Index identifying this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cigmpfilterstartaddresstype  <key>
            
            	This object describes the type of Internet address used to determine the start address  of IP multicast group for a profile
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cigmpfilterstartaddress  <key>
            
            	This object describes the start of the IP multicast group address of a contiguous range which will be subjected to filtering operation
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cigmpfilterendaddress
            
            	This object indicates the end of the IP multicast group address of a contiguous range which will be  subjected to filtering operation
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cigmpfilterendaddresstype
            
            	This object indicates the type of Internet address used to determine the end address  of IP multicast group for a profile
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cigmpfilterprofileaction
            
            	This object defines the action for filtering IGMP reports for this profile.  If the object is set to deny(2)\: then all IGMP reports associated to IP multicast groups included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped.  If the object is set to permit(1)\: then all IGMP reports associated to IP multicast groups not included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped
            	**type**\:   :py:class:`CigmpfilterprofileactionEnum <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry.CigmpfilterprofileactionEnum>`
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                self.parent = None
                self.cigmpfilterprofileindex = None
                self.cigmpfilterstartaddresstype = None
                self.cigmpfilterstartaddress = None
                self.cigmpfilterendaddress = None
                self.cigmpfilterendaddresstype = None
                self.cigmpfilterprofileaction = None

            class CigmpfilterprofileactionEnum(Enum):
                """
                CigmpfilterprofileactionEnum

                This object defines the action for

                filtering IGMP reports for this profile.

                If the object is set to deny(2)\:

                then all IGMP reports associated to IP multicast

                groups included in the profile identified by

                cIgmpFilterInterfaceProfileIndex will be dropped.

                If the object is set to permit(1)\:

                then all IGMP reports associated to IP multicast

                groups not included in the profile identified by

                cIgmpFilterInterfaceProfileIndex will be dropped.

                .. data:: permit = 1

                .. data:: deny = 2

                """

                permit = 1

                deny = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                    return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry.CigmpfilterprofileactionEnum']


            @property
            def _common_path(self):
                if self.cigmpfilterprofileindex is None:
                    raise YPYModelError('Key property cigmpfilterprofileindex is None')
                if self.cigmpfilterstartaddresstype is None:
                    raise YPYModelError('Key property cigmpfilterstartaddresstype is None')
                if self.cigmpfilterstartaddress is None:
                    raise YPYModelError('Key property cigmpfilterstartaddress is None')

                return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterTable/CISCO-IGMP-FILTER-MIB:cIgmpFilterEntry[CISCO-IGMP-FILTER-MIB:cIgmpFilterProfileIndex = ' + str(self.cigmpfilterprofileindex) + '][CISCO-IGMP-FILTER-MIB:cIgmpFilterStartAddressType = ' + str(self.cigmpfilterstartaddresstype) + '][CISCO-IGMP-FILTER-MIB:cIgmpFilterStartAddress = ' + str(self.cigmpfilterstartaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cigmpfilterprofileindex is not None:
                    return True

                if self.cigmpfilterstartaddresstype is not None:
                    return True

                if self.cigmpfilterstartaddress is not None:
                    return True

                if self.cigmpfilterendaddress is not None:
                    return True

                if self.cigmpfilterendaddresstype is not None:
                    return True

                if self.cigmpfilterprofileaction is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cigmpfilterentry is not None:
                for child_ref in self.cigmpfilterentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CiscoIgmpFilterMib.Cigmpfiltertable']['meta_info']


    class Cigmpfilterinterfacetable(object):
        """
        This table contains the list of interfaces that can
        support IGMP filter feature.
        
        .. attribute:: cigmpfilterinterfaceentry
        
        	Each entry contains the configuration for associating the IGMP filter profile index with the interface.  An entry is created for each of the IGMP filter capable  interface on the system.  The entry is removed on removal of corresponding  interface from system
        	**type**\: list of    :py:class:`Cigmpfilterinterfaceentry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterinterfaceentry = YList()
            self.cigmpfilterinterfaceentry.parent = self
            self.cigmpfilterinterfaceentry.name = 'cigmpfilterinterfaceentry'


        class Cigmpfilterinterfaceentry(object):
            """
            Each entry contains the configuration for associating
            the IGMP filter profile index with the interface.
            
            An entry is created for each of the IGMP filter capable 
            interface on the system.
            
            The entry is removed on removal of corresponding 
            interface from system.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cigmpfilterinterfaceprofileindex
            
            	Specifies which IGMP filter profile applies to this interface. If the value of this MIB object matches the  value of cIgmpFilterProfileIndex in cIgmpFilterTable,  the corresponding profile configuration will apply to this interface.   Agent returns inconsistentValue if this profile  does not exist in cIgmpFilterTable.  A value of zero indicates no profile is associated with corresponding interface.  The filtering action on each interface is also defined by the associated profile
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cigmpfilterinterfaceprofileindex = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceTable/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceEntry[CISCO-IGMP-FILTER-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cigmpfilterinterfaceprofileindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cigmpfilterinterfaceentry is not None:
                for child_ref in self.cigmpfilterinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CiscoIgmpFilterMib.Cigmpfilterinterfacetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cigmpfiltereditor is not None and self.cigmpfiltereditor._has_data():
            return True

        if self.cigmpfiltergeneral is not None and self.cigmpfiltergeneral._has_data():
            return True

        if self.cigmpfilterinterfacetable is not None and self.cigmpfilterinterfacetable._has_data():
            return True

        if self.cigmpfiltertable is not None and self.cigmpfiltertable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_IGMP_FILTER_MIB as meta
        return meta._meta_table['CiscoIgmpFilterMib']['meta_info']



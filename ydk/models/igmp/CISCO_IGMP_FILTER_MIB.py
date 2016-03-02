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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum


class CISCOIGMPFILTERMIB(object):
    """
    
    
    .. attribute:: cigmpfiltereditor
    
    	
    	**type**\: :py:class:`CIgmpFilterEditor <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor>`
    
    .. attribute:: cigmpfiltergeneral
    
    	
    	**type**\: :py:class:`CIgmpFilterGeneral <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterGeneral>`
    
    .. attribute:: cigmpfilterinterfacetable
    
    	This table contains the list of interfaces that can support IGMP filter feature
    	**type**\: :py:class:`CIgmpFilterInterfaceTable <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable>`
    
    .. attribute:: cigmpfiltertable
    
    	This table contains entries that identify lists of IP Multicast groups for each profile configured on the device.   Each entry contains a range of contiguous IP Multicast groups associated to a profile index. Multiple cIgmpFilterEntry may be associated with the same cIgmpFilterProfileIndex.  All the cIgmpFilterEntry with  the same profile index  are subjected to the same IGMP filtering action as  defined in cIgmpFilterProfileAction.  Each profile index may be associated with zero or more  interfaces through cIgmpFilterInterfaceIfIndex object in cIgmpFilterInterfaceTable. The maximum number of entries is determined by cIgmpFilterMaxProfiles
    	**type**\: :py:class:`CIgmpFilterTable <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable>`
    
    

    """

    _prefix = 'cisco-igmp'
    _revision = '2005-11-29'

    def __init__(self):
        self.cigmpfiltereditor = CISCOIGMPFILTERMIB.CIgmpFilterEditor()
        self.cigmpfiltereditor.parent = self
        self.cigmpfiltergeneral = CISCOIGMPFILTERMIB.CIgmpFilterGeneral()
        self.cigmpfiltergeneral.parent = self
        self.cigmpfilterinterfacetable = CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable()
        self.cigmpfilterinterfacetable.parent = self
        self.cigmpfiltertable = CISCOIGMPFILTERMIB.CIgmpFilterTable()
        self.cigmpfiltertable.parent = self


    class CIgmpFilterEditor(object):
        """
        
        
        .. attribute:: cigmpfilterapplystatus
        
        	The current status of an 'add', 'delete' or 'modify' operation. If no apply is currently active, the status  represented is that of the most recently completed 'add',  'delete' or 'modify' operation.  The value of this objects indicates succeeded(2) state  initially when no 'add', 'delete', 'modify' operation has been carried out.  The possible values are\:    someOtherError \- the 'add', 'delete' or 'modify' failed     due to undefined error(s) in apply operation.    (e.g., insufficient memory).      succeeded \- the 'add', 'delete' or 'modify' operation    was successful. (This value is also used when no    apply has been invoked since the last time the local     system restarted.)     inconsistentEdit \- the 'add', 'delete' or 'modify' failed    due to inconsistency of the data.     entryPresentError \- the 'add' operation failed  as the     corresponding entry already exists in cIgmpFilterTable.     entryNotPresentError \- the 'modify' operation failed     as no corresponding entry exists in cIgmpFilterTable
        	**type**\: :py:class:`CIgmpFilterApplyStatus_Enum <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterApplyStatus_Enum>`
        
        .. attribute:: cigmpfiltereditendaddress
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddress in cIgmpFilterTable  to establish end address of filtering  range for a profile
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: cigmpfiltereditendaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddressType in cIgmpFilterTable.  This object describes the type of Internet      address used to determine the start address  of IP multicast group for a profile
        	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
        
        .. attribute:: cigmpfiltereditoperation
        
        	The function of this object is to allow user to apply the changes in cIgmpFilterEditor objects to  cIgmpFilterTable.   This object always has the value 'none' when read. When written each value causes the appropriate action\:  'add' \- tries to insert the information contained  in cIgmpFilterEditor objects into  cIgmpFilterTable. If the entry already exists in the table the 'add'  fails.          'delete' \- tries to delete corresponding entry from cIgmpFilterTable. If a user completely deletes a profile that has corresponding entries in the cIgmpFilterInterfaceTable, then all the interfaces mapped to corresponding profile will be cleared and set to zero.  'modify' \- Mode of operation used to edit an entry in  cIgmpFilterTable. If the corresponding entry does not   exist, modify operation fails. This mode allows user to  extend/truncate a contiguous filtered range, type of  Internet addressing and filtering action for a profile.   'none' \- no operation is performed
        	**type**\: :py:class:`CIgmpFilterEditOperation_Enum <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditOperation_Enum>`
        
        .. attribute:: cigmpfiltereditprofileaction
        
        	Buffer object to edit corresponding object in cIgmpFilterTable to determine filtering action of each profile
        	**type**\: :py:class:`CIgmpFilterEditProfileAction_Enum <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditProfileAction_Enum>`
        
        .. attribute:: cigmpfiltereditprofileindex
        
        	Buffer object to edit corresponding object cIgmpFilterProfileIndex in cIgmpFilterTable.  Maximum value this object can be set to is  determined by cIgmpFilterMaxProfiles object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cigmpfiltereditspinlock
        
        	This object is used to facilitate modification of IGMP Filter Editor Group in the CISCO\-IGMP\-FILTER\-MIB  module by multiple managers.  In particular, it is  useful when modifying the value of the cIgmpFilterEditor  object.   The procedure for modifying the cIgmpFilterEditor  object is as follows\:       1.  Retrieve the value of cIgmpFilterEditSpinLock and          of object within cIgmpFilterEditor group.       2.  Generate new values for 'writeable' objects         in the cIgmpFilterEditor group except for          cIgmpFilterEditSpinLock object.      3.  Set the value of cIgmpFilterEditSpinLock to the          retrieved value, and the value of objects in          cIgmpFilterEditor to the new value. If the set         fails for the cIgmpFilterEditSpinLock object,         go back to step 1.   The cIgmpFilterApplyStatus and cIgmpFilterEditSpinLock  should be read together by NMS to make sure that the  result is associated with its configuration request.  To add/delete or modify a profile ( through cIgmpFilterEditor objects ) following procedure may be followed as an example.\:      1.  GET(cIgmpFilterEditSpinLock.0) and save in sValue.     2.  SET(cIgmpFilterEditSpinLock.0 = sValue,             cIgmpFilterEditProfileIndex.0 = validProfileNumber,             cIgmpFilterEditStartAddress.0 = validStartAddress,             cIgmpFilterEditEndAddress.0 = validEndAddress,             cIgmpFilterEditOperation.0 =  validOperation)     3.  If the SET in step 2 is not successful go back         to step 1.     4.  If the SET in step 2 is successful, user should          GET(cIgmpFilterEditSpinLock.0) and          GET(cIgmpFilterApplyStatus.0) simultaneously.      5.  The cIgmpFilterApplyStatus.0 reflects the outcome of         step 2 only if         cIgmpFilterEditSpinLock.0 = sValue + 1 or         cIgmpFilterEditSpinLock.0 = 0 if sValue reaches         value at which cIgmpFilterEditSpinLock wraps          around
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: cigmpfiltereditstartaddress
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddress in cIgmpFilterTable   to establish start address of filtering range for a profile
        	**type**\: str
        
        	**range:** 1..64
        
        .. attribute:: cigmpfiltereditstartaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddressType in cIgmpFilterTable.  This object describes the type of Internet   address used to determine the start address  of IP multicast group for a profile
        	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
        
        

        """

        _prefix = 'cisco-igmp'
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

        class CIgmpFilterApplyStatus_Enum(Enum):
            """
            CIgmpFilterApplyStatus_Enum

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

            """

            SOMEOTHERERROR = 1

            SUCCEEDED = 2

            INCONSISTENTEDIT = 3

            ENTRYPRESENTERROR = 4

            ENTRYNOTPRESENTERROR = 5


            @staticmethod
            def _meta_info():
                from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterApplyStatus_Enum']


        class CIgmpFilterEditOperation_Enum(Enum):
            """
            CIgmpFilterEditOperation_Enum

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

            """

            NONE = 1

            ADD = 2

            DELETE = 3

            MODIFY = 4


            @staticmethod
            def _meta_info():
                from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditOperation_Enum']


        class CIgmpFilterEditProfileAction_Enum(Enum):
            """
            CIgmpFilterEditProfileAction_Enum

            Buffer object to edit corresponding object in
            cIgmpFilterTable to determine filtering action
            of each profile.

            """

            PERMIT = 1

            DENY = 2


            @staticmethod
            def _meta_info():
                from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditProfileAction_Enum']


        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterEditor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
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

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterEditor']['meta_info']


    class CIgmpFilterGeneral(object):
        """
        
        
        .. attribute:: cigmpfilterenable
        
        	This object controls whether the IGMP filtering is enabled on the device. A false(2) value will  prevent the IGMP filtering action on the device
        	**type**\: bool
        
        .. attribute:: cigmpfiltermaxprofiles
        
        	Indicates the maximum number of profiles supported by this device.  A value of zero indicates no limitation on the number of profiles
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-igmp'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cigmpfilterenable is not None:
                return True

            if self.cigmpfiltermaxprofiles is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterGeneral']['meta_info']


    class CIgmpFilterInterfaceTable(object):
        """
        This table contains the list of interfaces that can
        support IGMP filter feature.
        
        .. attribute:: cigmpfilterinterfaceentry
        
        	Each entry contains the configuration for associating the IGMP filter profile index with the interface.  An entry is created for each of the IGMP filter capable  interface on the system.  The entry is removed on removal of corresponding  interface from system
        	**type**\: list of :py:class:`CIgmpFilterInterfaceEntry <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry>`
        
        

        """

        _prefix = 'cisco-igmp'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterinterfaceentry = YList()
            self.cigmpfilterinterfaceentry.parent = self
            self.cigmpfilterinterfaceentry.name = 'cigmpfilterinterfaceentry'


        class CIgmpFilterInterfaceEntry(object):
            """
            Each entry contains the configuration for associating
            the IGMP filter profile index with the interface.
            
            An entry is created for each of the IGMP filter capable 
            interface on the system.
            
            The entry is removed on removal of corresponding 
            interface from system.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cigmpfilterinterfaceprofileindex
            
            	Specifies which IGMP filter profile applies to this interface. If the value of this MIB object matches the  value of cIgmpFilterProfileIndex in cIgmpFilterTable,  the corresponding profile configuration will apply to this interface.   Agent returns inconsistentValue if this profile  does not exist in cIgmpFilterTable.  A value of zero indicates no profile is associated with corresponding interface.  The filtering action on each interface is also defined by the associated profile
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-igmp'
            _revision = '2005-11-29'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cigmpfilterinterfaceprofileindex = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceTable/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceEntry[CISCO-IGMP-FILTER-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cigmpfilterinterfaceprofileindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cigmpfilterinterfaceentry is not None:
                for child_ref in self.cigmpfilterinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable']['meta_info']


    class CIgmpFilterTable(object):
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
        	**type**\: list of :py:class:`CIgmpFilterEntry <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry>`
        
        

        """

        _prefix = 'cisco-igmp'
        _revision = '2005-11-29'

        def __init__(self):
            self.parent = None
            self.cigmpfilterentry = YList()
            self.cigmpfilterentry.parent = self
            self.cigmpfilterentry.name = 'cigmpfilterentry'


        class CIgmpFilterEntry(object):
            """
            An entry (conceptual row) in the cIgmpFilterTable.
            
            The creation, deletion or modification of an entry
            is controlled through the MIB objects defined under
            cIgmpFilterEditor group.
            
            .. attribute:: cigmpfilterprofileindex
            
            	Index identifying this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cigmpfilterstartaddress
            
            	This object describes the start of the IP multicast group address of a contiguous range which will be subjected to filtering operation
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cigmpfilterstartaddresstype
            
            	This object describes the type of Internet address used to determine the start address  of IP multicast group for a profile
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cigmpfilterendaddress
            
            	This object indicates the end of the IP multicast group address of a contiguous range which will be  subjected to filtering operation
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cigmpfilterendaddresstype
            
            	This object indicates the type of Internet address used to determine the end address  of IP multicast group for a profile
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cigmpfilterprofileaction
            
            	This object defines the action for filtering IGMP reports for this profile.  If the object is set to deny(2)\: then all IGMP reports associated to IP multicast groups included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped.  If the object is set to permit(1)\: then all IGMP reports associated to IP multicast groups not included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped
            	**type**\: :py:class:`CIgmpFilterProfileAction_Enum <ydk.models.igmp.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction_Enum>`
            
            

            """

            _prefix = 'cisco-igmp'
            _revision = '2005-11-29'

            def __init__(self):
                self.parent = None
                self.cigmpfilterprofileindex = None
                self.cigmpfilterstartaddress = None
                self.cigmpfilterstartaddresstype = None
                self.cigmpfilterendaddress = None
                self.cigmpfilterendaddresstype = None
                self.cigmpfilterprofileaction = None

            class CIgmpFilterProfileAction_Enum(Enum):
                """
                CIgmpFilterProfileAction_Enum

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

                """

                PERMIT = 1

                DENY = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                    return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction_Enum']


            @property
            def _common_path(self):
                if self.cigmpfilterprofileindex is None:
                    raise YPYDataValidationError('Key property cigmpfilterprofileindex is None')
                if self.cigmpfilterstartaddress is None:
                    raise YPYDataValidationError('Key property cigmpfilterstartaddress is None')
                if self.cigmpfilterstartaddresstype is None:
                    raise YPYDataValidationError('Key property cigmpfilterstartaddresstype is None')

                return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterTable/CISCO-IGMP-FILTER-MIB:cIgmpFilterEntry[CISCO-IGMP-FILTER-MIB:cIgmpFilterProfileIndex = ' + str(self.cigmpfilterprofileindex) + '][CISCO-IGMP-FILTER-MIB:cIgmpFilterStartAddress = ' + str(self.cigmpfilterstartaddress) + '][CISCO-IGMP-FILTER-MIB:cIgmpFilterStartAddressType = ' + str(self.cigmpfilterstartaddresstype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cigmpfilterprofileindex is not None:
                    return True

                if self.cigmpfilterstartaddress is not None:
                    return True

                if self.cigmpfilterstartaddresstype is not None:
                    return True

                if self.cigmpfilterendaddress is not None:
                    return True

                if self.cigmpfilterendaddresstype is not None:
                    return True

                if self.cigmpfilterprofileaction is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
                return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/CISCO-IGMP-FILTER-MIB:cIgmpFilterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cigmpfilterentry is not None:
                for child_ref in self.cigmpfilterentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
            return meta._meta_table['CISCOIGMPFILTERMIB.CIgmpFilterTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cigmpfiltereditor is not None and self.cigmpfiltereditor._has_data():
            return True

        if self.cigmpfiltereditor is not None and self.cigmpfiltereditor.is_presence():
            return True

        if self.cigmpfiltergeneral is not None and self.cigmpfiltergeneral._has_data():
            return True

        if self.cigmpfiltergeneral is not None and self.cigmpfiltergeneral.is_presence():
            return True

        if self.cigmpfilterinterfacetable is not None and self.cigmpfilterinterfacetable._has_data():
            return True

        if self.cigmpfilterinterfacetable is not None and self.cigmpfilterinterfacetable.is_presence():
            return True

        if self.cigmpfiltertable is not None and self.cigmpfiltertable._has_data():
            return True

        if self.cigmpfiltertable is not None and self.cigmpfiltertable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.igmp._meta import _CISCO_IGMP_FILTER_MIB as meta
        return meta._meta_table['CISCOIGMPFILTERMIB']['meta_info']



""" CISCO_IGMP_FILTER_MIB 

IGMP Filter configuration MIB. This MIB provides a
mechanism for users to configure the system to intercept 
IGMP joins for IP Multicast groups identified in this 
MIB and only allow certain ports to join certain 
multicast groups.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOIGMPFILTERMIB(Entity):
    """
    
    
    .. attribute:: cigmpfiltergeneral
    
    	
    	**type**\:  :py:class:`CIgmpFilterGeneral <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterGeneral>`
    
    	**config**\: False
    
    .. attribute:: cigmpfiltereditor
    
    	
    	**type**\:  :py:class:`CIgmpFilterEditor <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor>`
    
    	**config**\: False
    
    .. attribute:: cigmpfiltertable
    
    	This table contains entries that identify lists of IP Multicast groups for each profile configured on the device.   Each entry contains a range of contiguous IP Multicast groups associated to a profile index. Multiple cIgmpFilterEntry may be associated with the same cIgmpFilterProfileIndex.  All the cIgmpFilterEntry with  the same profile index  are subjected to the same IGMP filtering action as  defined in cIgmpFilterProfileAction.  Each profile index may be associated with zero or more  interfaces through cIgmpFilterInterfaceIfIndex object in cIgmpFilterInterfaceTable. The maximum number of entries is determined by cIgmpFilterMaxProfiles
    	**type**\:  :py:class:`CIgmpFilterTable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable>`
    
    	**config**\: False
    
    .. attribute:: cigmpfilterinterfacetable
    
    	This table contains the list of interfaces that can support IGMP filter feature
    	**type**\:  :py:class:`CIgmpFilterInterfaceTable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-IGMP-FILTER-MIB'
    _revision = '2005-11-29'

    def __init__(self):
        super(CISCOIGMPFILTERMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IGMP-FILTER-MIB"
        self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cIgmpFilterGeneral", ("cigmpfiltergeneral", CISCOIGMPFILTERMIB.CIgmpFilterGeneral)), ("cIgmpFilterEditor", ("cigmpfiltereditor", CISCOIGMPFILTERMIB.CIgmpFilterEditor)), ("cIgmpFilterTable", ("cigmpfiltertable", CISCOIGMPFILTERMIB.CIgmpFilterTable)), ("cIgmpFilterInterfaceTable", ("cigmpfilterinterfacetable", CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable))])
        self._leafs = OrderedDict()

        self.cigmpfiltergeneral = CISCOIGMPFILTERMIB.CIgmpFilterGeneral()
        self.cigmpfiltergeneral.parent = self
        self._children_name_map["cigmpfiltergeneral"] = "cIgmpFilterGeneral"

        self.cigmpfiltereditor = CISCOIGMPFILTERMIB.CIgmpFilterEditor()
        self.cigmpfiltereditor.parent = self
        self._children_name_map["cigmpfiltereditor"] = "cIgmpFilterEditor"

        self.cigmpfiltertable = CISCOIGMPFILTERMIB.CIgmpFilterTable()
        self.cigmpfiltertable.parent = self
        self._children_name_map["cigmpfiltertable"] = "cIgmpFilterTable"

        self.cigmpfilterinterfacetable = CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable()
        self.cigmpfilterinterfacetable.parent = self
        self._children_name_map["cigmpfilterinterfacetable"] = "cIgmpFilterInterfaceTable"
        self._segment_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOIGMPFILTERMIB, [], name, value)


    class CIgmpFilterGeneral(Entity):
        """
        
        
        .. attribute:: cigmpfilterenable
        
        	This object controls whether the IGMP filtering is enabled on the device. A false(2) value will  prevent the IGMP filtering action on the device
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cigmpfiltermaxprofiles
        
        	Indicates the maximum number of profiles supported by this device.  A value of zero indicates no limitation on the number of profiles
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: profiles
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CISCOIGMPFILTERMIB.CIgmpFilterGeneral, self).__init__()

            self.yang_name = "cIgmpFilterGeneral"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cigmpfilterenable', (YLeaf(YType.boolean, 'cIgmpFilterEnable'), ['bool'])),
                ('cigmpfiltermaxprofiles', (YLeaf(YType.uint32, 'cIgmpFilterMaxProfiles'), ['int'])),
            ])
            self.cigmpfilterenable = None
            self.cigmpfiltermaxprofiles = None
            self._segment_path = lambda: "cIgmpFilterGeneral"
            self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterGeneral, ['cigmpfilterenable', 'cigmpfiltermaxprofiles'], name, value)



    class CIgmpFilterEditor(Entity):
        """
        
        
        .. attribute:: cigmpfiltereditspinlock
        
        	This object is used to facilitate modification of IGMP Filter Editor Group in the CISCO\-IGMP\-FILTER\-MIB  module by multiple managers.  In particular, it is  useful when modifying the value of the cIgmpFilterEditor  object.   The procedure for modifying the cIgmpFilterEditor  object is as follows\:       1.  Retrieve the value of cIgmpFilterEditSpinLock and          of object within cIgmpFilterEditor group.       2.  Generate new values for 'writeable' objects         in the cIgmpFilterEditor group except for          cIgmpFilterEditSpinLock object.      3.  Set the value of cIgmpFilterEditSpinLock to the          retrieved value, and the value of objects in          cIgmpFilterEditor to the new value. If the set         fails for the cIgmpFilterEditSpinLock object,         go back to step 1.   The cIgmpFilterApplyStatus and cIgmpFilterEditSpinLock  should be read together by NMS to make sure that the  result is associated with its configuration request.  To add/delete or modify a profile ( through cIgmpFilterEditor objects ) following procedure may be followed as an example.\:      1.  GET(cIgmpFilterEditSpinLock.0) and save in sValue.     2.  SET(cIgmpFilterEditSpinLock.0 = sValue,             cIgmpFilterEditProfileIndex.0 = validProfileNumber,             cIgmpFilterEditStartAddress.0 = validStartAddress,             cIgmpFilterEditEndAddress.0 = validEndAddress,             cIgmpFilterEditOperation.0 =  validOperation)     3.  If the SET in step 2 is not successful go back         to step 1.     4.  If the SET in step 2 is successful, user should          GET(cIgmpFilterEditSpinLock.0) and          GET(cIgmpFilterApplyStatus.0) simultaneously.      5.  The cIgmpFilterApplyStatus.0 reflects the outcome of         step 2 only if         cIgmpFilterEditSpinLock.0 = sValue + 1 or         cIgmpFilterEditSpinLock.0 = 0 if sValue reaches         value at which cIgmpFilterEditSpinLock wraps          around
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditprofileindex
        
        	Buffer object to edit corresponding object cIgmpFilterProfileIndex in cIgmpFilterTable.  Maximum value this object can be set to is  determined by cIgmpFilterMaxProfiles object
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditstartaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddressType in cIgmpFilterTable.  This object describes the type of Internet   address used to determine the start address  of IP multicast group for a profile
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditstartaddress
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddress in cIgmpFilterTable   to establish start address of filtering range for a profile
        	**type**\: str
        
        	**length:** 1..64
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditendaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddressType in cIgmpFilterTable.  This object describes the type of Internet      address used to determine the start address  of IP multicast group for a profile
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditendaddress
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddress in cIgmpFilterTable  to establish end address of filtering  range for a profile
        	**type**\: str
        
        	**length:** 0..255
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditprofileaction
        
        	Buffer object to edit corresponding object in cIgmpFilterTable to determine filtering action of each profile
        	**type**\:  :py:class:`CIgmpFilterEditProfileAction <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditProfileAction>`
        
        	**config**\: False
        
        .. attribute:: cigmpfiltereditoperation
        
        	The function of this object is to allow user to apply the changes in cIgmpFilterEditor objects to  cIgmpFilterTable.   This object always has the value 'none' when read. When written each value causes the appropriate action\:  'add' \- tries to insert the information contained  in cIgmpFilterEditor objects into  cIgmpFilterTable. If the entry already exists in the table the 'add'  fails.          'delete' \- tries to delete corresponding entry from cIgmpFilterTable. If a user completely deletes a profile that has corresponding entries in the cIgmpFilterInterfaceTable, then all the interfaces mapped to corresponding profile will be cleared and set to zero.  'modify' \- Mode of operation used to edit an entry in  cIgmpFilterTable. If the corresponding entry does not   exist, modify operation fails. This mode allows user to  extend/truncate a contiguous filtered range, type of  Internet addressing and filtering action for a profile.   'none' \- no operation is performed
        	**type**\:  :py:class:`CIgmpFilterEditOperation <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterEditOperation>`
        
        	**config**\: False
        
        .. attribute:: cigmpfilterapplystatus
        
        	The current status of an 'add', 'delete' or 'modify' operation. If no apply is currently active, the status  represented is that of the most recently completed 'add',  'delete' or 'modify' operation.  The value of this objects indicates succeeded(2) state  initially when no 'add', 'delete', 'modify' operation has been carried out.  The possible values are\:    someOtherError \- the 'add', 'delete' or 'modify' failed     due to undefined error(s) in apply operation.    (e.g., insufficient memory).      succeeded \- the 'add', 'delete' or 'modify' operation    was successful. (This value is also used when no    apply has been invoked since the last time the local     system restarted.)     inconsistentEdit \- the 'add', 'delete' or 'modify' failed    due to inconsistency of the data.     entryPresentError \- the 'add' operation failed  as the     corresponding entry already exists in cIgmpFilterTable.     entryNotPresentError \- the 'modify' operation failed     as no corresponding entry exists in cIgmpFilterTable
        	**type**\:  :py:class:`CIgmpFilterApplyStatus <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterEditor.CIgmpFilterApplyStatus>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CISCOIGMPFILTERMIB.CIgmpFilterEditor, self).__init__()

            self.yang_name = "cIgmpFilterEditor"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cigmpfiltereditspinlock', (YLeaf(YType.int32, 'cIgmpFilterEditSpinLock'), ['int'])),
                ('cigmpfiltereditprofileindex', (YLeaf(YType.uint32, 'cIgmpFilterEditProfileIndex'), ['int'])),
                ('cigmpfiltereditstartaddresstype', (YLeaf(YType.enumeration, 'cIgmpFilterEditStartAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('cigmpfiltereditstartaddress', (YLeaf(YType.str, 'cIgmpFilterEditStartAddress'), ['str'])),
                ('cigmpfiltereditendaddresstype', (YLeaf(YType.enumeration, 'cIgmpFilterEditEndAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('cigmpfiltereditendaddress', (YLeaf(YType.str, 'cIgmpFilterEditEndAddress'), ['str'])),
                ('cigmpfiltereditprofileaction', (YLeaf(YType.enumeration, 'cIgmpFilterEditProfileAction'), [('ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB', 'CIgmpFilterEditor.CIgmpFilterEditProfileAction')])),
                ('cigmpfiltereditoperation', (YLeaf(YType.enumeration, 'cIgmpFilterEditOperation'), [('ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB', 'CIgmpFilterEditor.CIgmpFilterEditOperation')])),
                ('cigmpfilterapplystatus', (YLeaf(YType.enumeration, 'cIgmpFilterApplyStatus'), [('ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB', 'CIgmpFilterEditor.CIgmpFilterApplyStatus')])),
            ])
            self.cigmpfiltereditspinlock = None
            self.cigmpfiltereditprofileindex = None
            self.cigmpfiltereditstartaddresstype = None
            self.cigmpfiltereditstartaddress = None
            self.cigmpfiltereditendaddresstype = None
            self.cigmpfiltereditendaddress = None
            self.cigmpfiltereditprofileaction = None
            self.cigmpfiltereditoperation = None
            self.cigmpfilterapplystatus = None
            self._segment_path = lambda: "cIgmpFilterEditor"
            self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterEditor, ['cigmpfiltereditspinlock', 'cigmpfiltereditprofileindex', 'cigmpfiltereditstartaddresstype', 'cigmpfiltereditstartaddress', 'cigmpfiltereditendaddresstype', 'cigmpfiltereditendaddress', 'cigmpfiltereditprofileaction', 'cigmpfiltereditoperation', 'cigmpfilterapplystatus'], name, value)

        class CIgmpFilterApplyStatus(Enum):
            """
            CIgmpFilterApplyStatus (Enum Class)

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

            someOtherError = Enum.YLeaf(1, "someOtherError")

            succeeded = Enum.YLeaf(2, "succeeded")

            inconsistentEdit = Enum.YLeaf(3, "inconsistentEdit")

            entryPresentError = Enum.YLeaf(4, "entryPresentError")

            entryNotPresentError = Enum.YLeaf(5, "entryNotPresentError")


        class CIgmpFilterEditOperation(Enum):
            """
            CIgmpFilterEditOperation (Enum Class)

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

            none = Enum.YLeaf(1, "none")

            add = Enum.YLeaf(2, "add")

            delete = Enum.YLeaf(3, "delete")

            modify = Enum.YLeaf(4, "modify")


        class CIgmpFilterEditProfileAction(Enum):
            """
            CIgmpFilterEditProfileAction (Enum Class)

            Buffer object to edit corresponding object in

            cIgmpFilterTable to determine filtering action

            of each profile.

            .. data:: unSpecified = 0

            .. data:: permit = 1

            .. data:: deny = 2

            """

            unSpecified = Enum.YLeaf(0, "unSpecified")

            permit = Enum.YLeaf(1, "permit")

            deny = Enum.YLeaf(2, "deny")




    class CIgmpFilterTable(Entity):
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
        	**type**\: list of  		 :py:class:`CIgmpFilterEntry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CISCOIGMPFILTERMIB.CIgmpFilterTable, self).__init__()

            self.yang_name = "cIgmpFilterTable"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cIgmpFilterEntry", ("cigmpfilterentry", CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry))])
            self._leafs = OrderedDict()

            self.cigmpfilterentry = YList(self)
            self._segment_path = lambda: "cIgmpFilterTable"
            self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterTable, [], name, value)


        class CIgmpFilterEntry(Entity):
            """
            An entry (conceptual row) in the cIgmpFilterTable.
            
            The creation, deletion or modification of an entry
            is controlled through the MIB objects defined under
            cIgmpFilterEditor group.
            
            .. attribute:: cigmpfilterprofileindex  (key)
            
            	Index identifying this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cigmpfilterstartaddresstype  (key)
            
            	This object describes the type of Internet address used to determine the start address  of IP multicast group for a profile
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cigmpfilterstartaddress  (key)
            
            	This object describes the start of the IP multicast group address of a contiguous range which will be subjected to filtering operation
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cigmpfilterendaddresstype
            
            	This object indicates the type of Internet address used to determine the end address  of IP multicast group for a profile
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cigmpfilterendaddress
            
            	This object indicates the end of the IP multicast group address of a contiguous range which will be  subjected to filtering operation
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cigmpfilterprofileaction
            
            	This object defines the action for filtering IGMP reports for this profile.  If the object is set to deny(2)\: then all IGMP reports associated to IP multicast groups included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped.  If the object is set to permit(1)\: then all IGMP reports associated to IP multicast groups not included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped
            	**type**\:  :py:class:`CIgmpFilterProfileAction <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                super(CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry, self).__init__()

                self.yang_name = "cIgmpFilterEntry"
                self.yang_parent_name = "cIgmpFilterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cigmpfilterprofileindex','cigmpfilterstartaddresstype','cigmpfilterstartaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cigmpfilterprofileindex', (YLeaf(YType.uint32, 'cIgmpFilterProfileIndex'), ['int'])),
                    ('cigmpfilterstartaddresstype', (YLeaf(YType.enumeration, 'cIgmpFilterStartAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cigmpfilterstartaddress', (YLeaf(YType.str, 'cIgmpFilterStartAddress'), ['str'])),
                    ('cigmpfilterendaddresstype', (YLeaf(YType.enumeration, 'cIgmpFilterEndAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cigmpfilterendaddress', (YLeaf(YType.str, 'cIgmpFilterEndAddress'), ['str'])),
                    ('cigmpfilterprofileaction', (YLeaf(YType.enumeration, 'cIgmpFilterProfileAction'), [('ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB', 'CISCOIGMPFILTERMIB', 'CIgmpFilterTable.CIgmpFilterEntry.CIgmpFilterProfileAction')])),
                ])
                self.cigmpfilterprofileindex = None
                self.cigmpfilterstartaddresstype = None
                self.cigmpfilterstartaddress = None
                self.cigmpfilterendaddresstype = None
                self.cigmpfilterendaddress = None
                self.cigmpfilterprofileaction = None
                self._segment_path = lambda: "cIgmpFilterEntry" + "[cIgmpFilterProfileIndex='" + str(self.cigmpfilterprofileindex) + "']" + "[cIgmpFilterStartAddressType='" + str(self.cigmpfilterstartaddresstype) + "']" + "[cIgmpFilterStartAddress='" + str(self.cigmpfilterstartaddress) + "']"
                self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/cIgmpFilterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterTable.CIgmpFilterEntry, ['cigmpfilterprofileindex', 'cigmpfilterstartaddresstype', 'cigmpfilterstartaddress', 'cigmpfilterendaddresstype', 'cigmpfilterendaddress', 'cigmpfilterprofileaction'], name, value)

            class CIgmpFilterProfileAction(Enum):
                """
                CIgmpFilterProfileAction (Enum Class)

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

                permit = Enum.YLeaf(1, "permit")

                deny = Enum.YLeaf(2, "deny")





    class CIgmpFilterInterfaceTable(Entity):
        """
        This table contains the list of interfaces that can
        support IGMP filter feature.
        
        .. attribute:: cigmpfilterinterfaceentry
        
        	Each entry contains the configuration for associating the IGMP filter profile index with the interface.  An entry is created for each of the IGMP filter capable  interface on the system.  The entry is removed on removal of corresponding  interface from system
        	**type**\: list of  		 :py:class:`CIgmpFilterInterfaceEntry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable, self).__init__()

            self.yang_name = "cIgmpFilterInterfaceTable"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cIgmpFilterInterfaceEntry", ("cigmpfilterinterfaceentry", CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry))])
            self._leafs = OrderedDict()

            self.cigmpfilterinterfaceentry = YList(self)
            self._segment_path = lambda: "cIgmpFilterInterfaceTable"
            self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable, [], name, value)


        class CIgmpFilterInterfaceEntry(Entity):
            """
            Each entry contains the configuration for associating
            the IGMP filter profile index with the interface.
            
            An entry is created for each of the IGMP filter capable 
            interface on the system.
            
            The entry is removed on removal of corresponding 
            interface from system.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cigmpfilterinterfaceprofileindex
            
            	Specifies which IGMP filter profile applies to this interface. If the value of this MIB object matches the  value of cIgmpFilterProfileIndex in cIgmpFilterTable,  the corresponding profile configuration will apply to this interface.   Agent returns inconsistentValue if this profile  does not exist in cIgmpFilterTable.  A value of zero indicates no profile is associated with corresponding interface.  The filtering action on each interface is also defined by the associated profile
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                super(CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry, self).__init__()

                self.yang_name = "cIgmpFilterInterfaceEntry"
                self.yang_parent_name = "cIgmpFilterInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cigmpfilterinterfaceprofileindex', (YLeaf(YType.uint32, 'cIgmpFilterInterfaceProfileIndex'), ['int'])),
                ])
                self.ifindex = None
                self.cigmpfilterinterfaceprofileindex = None
                self._segment_path = lambda: "cIgmpFilterInterfaceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/cIgmpFilterInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIGMPFILTERMIB.CIgmpFilterInterfaceTable.CIgmpFilterInterfaceEntry, ['ifindex', 'cigmpfilterinterfaceprofileindex'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOIGMPFILTERMIB()
        return self._top_entity




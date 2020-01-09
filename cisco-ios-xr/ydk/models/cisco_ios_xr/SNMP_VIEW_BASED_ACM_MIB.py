""" SNMP_VIEW_BASED_ACM_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VacmAccessContextMatchType(Enum):
    """
    VacmAccessContextMatchType (Enum Class)

    .. data:: exact = 1

    .. data:: prefix = 2

    """

    exact = Enum.YLeaf(1, "exact")

    prefix = Enum.YLeaf(2, "prefix")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['VacmAccessContextMatchType']


class VacmViewTreeFamilyTypeType(Enum):
    """
    VacmViewTreeFamilyTypeType (Enum Class)

    .. data:: included = 1

    .. data:: excluded = 2

    """

    included = Enum.YLeaf(1, "included")

    excluded = Enum.YLeaf(2, "excluded")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['VacmViewTreeFamilyTypeType']



class SNMPVIEWBASEDACMMIB(_Entity_):
    """
    
    
    .. attribute:: vacmsecuritytogrouptable
    
    	
    	**type**\:  :py:class:`VacmSecurityToGroupTable <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable>`
    
    .. attribute:: vacmaccesstable
    
    	
    	**type**\:  :py:class:`VacmAccessTable <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmAccessTable>`
    
    .. attribute:: vacmviewtreefamilytable
    
    	
    	**type**\:  :py:class:`VacmViewTreeFamilyTable <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable>`
    
    

    """

    _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPVIEWBASEDACMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-VIEW-BASED-ACM-MIB"
        self.yang_parent_name = "SNMP-VIEW-BASED-ACM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vacmSecurityToGroupTable", ("vacmsecuritytogrouptable", SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable)), ("vacmAccessTable", ("vacmaccesstable", SNMPVIEWBASEDACMMIB.VacmAccessTable)), ("vacmViewTreeFamilyTable", ("vacmviewtreefamilytable", SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable))])
        self._leafs = OrderedDict()

        self.vacmsecuritytogrouptable = SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable()
        self.vacmsecuritytogrouptable.parent = self
        self._children_name_map["vacmsecuritytogrouptable"] = "vacmSecurityToGroupTable"

        self.vacmaccesstable = SNMPVIEWBASEDACMMIB.VacmAccessTable()
        self.vacmaccesstable.parent = self
        self._children_name_map["vacmaccesstable"] = "vacmAccessTable"

        self.vacmviewtreefamilytable = SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable()
        self.vacmviewtreefamilytable.parent = self
        self._children_name_map["vacmviewtreefamilytable"] = "vacmViewTreeFamilyTable"
        self._segment_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPVIEWBASEDACMMIB, [], name, value)


    class VacmSecurityToGroupTable(_Entity_):
        """
        
        
        .. attribute:: vacmsecuritytogroupentry
        
        	
        	**type**\: list of  		 :py:class:`VacmSecurityToGroupEntry <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable, self).__init__()

            self.yang_name = "vacmSecurityToGroupTable"
            self.yang_parent_name = "SNMP-VIEW-BASED-ACM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vacmSecurityToGroupEntry", ("vacmsecuritytogroupentry", SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry))])
            self._leafs = OrderedDict()

            self.vacmsecuritytogroupentry = YList(self)
            self._segment_path = lambda: "vacmSecurityToGroupTable"
            self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable, [], name, value)


        class VacmSecurityToGroupEntry(_Entity_):
            """
            
            
            .. attribute:: vacmsecuritymodel  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: vacmsecurityname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vacmgroupname
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**mandatory**\: True
            
            .. attribute:: vacmsecuritytogroupstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry, self).__init__()

                self.yang_name = "vacmSecurityToGroupEntry"
                self.yang_parent_name = "vacmSecurityToGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vacmsecuritymodel','vacmsecurityname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vacmsecuritymodel', (YLeaf(YType.int32, 'vacmSecurityModel'), ['int'])),
                    ('vacmsecurityname', (YLeaf(YType.str, 'vacmSecurityName'), ['str'])),
                    ('vacmgroupname', (YLeaf(YType.str, 'vacmGroupName'), ['str'])),
                    ('vacmsecuritytogroupstoragetype', (YLeaf(YType.enumeration, 'vacmSecurityToGroupStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.vacmsecuritymodel = None
                self.vacmsecurityname = None
                self.vacmgroupname = None
                self.vacmsecuritytogroupstoragetype = None
                self._segment_path = lambda: "vacmSecurityToGroupEntry" + "[vacmSecurityModel='" + str(self.vacmsecuritymodel) + "']" + "[vacmSecurityName='" + str(self.vacmsecurityname) + "']"
                self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/vacmSecurityToGroupTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry, ['vacmsecuritymodel', 'vacmsecurityname', 'vacmgroupname', 'vacmsecuritytogroupstoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable']['meta_info']


    class VacmAccessTable(_Entity_):
        """
        
        
        .. attribute:: vacmaccessentry
        
        	
        	**type**\: list of  		 :py:class:`VacmAccessEntry <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPVIEWBASEDACMMIB.VacmAccessTable, self).__init__()

            self.yang_name = "vacmAccessTable"
            self.yang_parent_name = "SNMP-VIEW-BASED-ACM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vacmAccessEntry", ("vacmaccessentry", SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry))])
            self._leafs = OrderedDict()

            self.vacmaccessentry = YList(self)
            self._segment_path = lambda: "vacmAccessTable"
            self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmAccessTable, [], name, value)


        class VacmAccessEntry(_Entity_):
            """
            
            
            .. attribute:: vacmgroupname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vacmaccesscontextprefix  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: vacmaccesssecuritymodel  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: vacmaccesssecuritylevel  (key)
            
            	
            	**type**\:  :py:class:`SnmpSecurityLevel <ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB.SnmpSecurityLevel>`
            
            .. attribute:: vacmaccesscontextmatch
            
            	
            	**type**\:  :py:class:`VacmAccessContextMatchType <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.VacmAccessContextMatchType>`
            
            	**default value**\: exact
            
            .. attribute:: vacmaccessreadviewname
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: vacmaccesswriteviewname
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: vacmaccessnotifyviewname
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: vacmaccessstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry, self).__init__()

                self.yang_name = "vacmAccessEntry"
                self.yang_parent_name = "vacmAccessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vacmgroupname','vacmaccesscontextprefix','vacmaccesssecuritymodel','vacmaccesssecuritylevel']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vacmgroupname', (YLeaf(YType.str, 'vacmGroupName'), ['str'])),
                    ('vacmaccesscontextprefix', (YLeaf(YType.str, 'vacmAccessContextPrefix'), ['str'])),
                    ('vacmaccesssecuritymodel', (YLeaf(YType.int32, 'vacmAccessSecurityModel'), ['int'])),
                    ('vacmaccesssecuritylevel', (YLeaf(YType.enumeration, 'vacmAccessSecurityLevel'), [('ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB', 'SnmpSecurityLevel', '')])),
                    ('vacmaccesscontextmatch', (YLeaf(YType.enumeration, 'vacmAccessContextMatch'), [('ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB', 'VacmAccessContextMatchType', '')])),
                    ('vacmaccessreadviewname', (YLeaf(YType.str, 'vacmAccessReadViewName'), ['str'])),
                    ('vacmaccesswriteviewname', (YLeaf(YType.str, 'vacmAccessWriteViewName'), ['str'])),
                    ('vacmaccessnotifyviewname', (YLeaf(YType.str, 'vacmAccessNotifyViewName'), ['str'])),
                    ('vacmaccessstoragetype', (YLeaf(YType.enumeration, 'vacmAccessStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.vacmgroupname = None
                self.vacmaccesscontextprefix = None
                self.vacmaccesssecuritymodel = None
                self.vacmaccesssecuritylevel = None
                self.vacmaccesscontextmatch = None
                self.vacmaccessreadviewname = None
                self.vacmaccesswriteviewname = None
                self.vacmaccessnotifyviewname = None
                self.vacmaccessstoragetype = None
                self._segment_path = lambda: "vacmAccessEntry" + "[vacmGroupName='" + str(self.vacmgroupname) + "']" + "[vacmAccessContextPrefix='" + str(self.vacmaccesscontextprefix) + "']" + "[vacmAccessSecurityModel='" + str(self.vacmaccesssecuritymodel) + "']" + "[vacmAccessSecurityLevel='" + str(self.vacmaccesssecuritylevel) + "']"
                self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/vacmAccessTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry, ['vacmgroupname', 'vacmaccesscontextprefix', 'vacmaccesssecuritymodel', 'vacmaccesssecuritylevel', 'vacmaccesscontextmatch', 'vacmaccessreadviewname', 'vacmaccesswriteviewname', 'vacmaccessnotifyviewname', 'vacmaccessstoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable']['meta_info']


    class VacmViewTreeFamilyTable(_Entity_):
        """
        
        
        .. attribute:: vacmviewtreefamilyentry
        
        	
        	**type**\: list of  		 :py:class:`VacmViewTreeFamilyEntry <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry>`
        
        

        """

        _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable, self).__init__()

            self.yang_name = "vacmViewTreeFamilyTable"
            self.yang_parent_name = "SNMP-VIEW-BASED-ACM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vacmViewTreeFamilyEntry", ("vacmviewtreefamilyentry", SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry))])
            self._leafs = OrderedDict()

            self.vacmviewtreefamilyentry = YList(self)
            self._segment_path = lambda: "vacmViewTreeFamilyTable"
            self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable, [], name, value)


        class VacmViewTreeFamilyEntry(_Entity_):
            """
            
            
            .. attribute:: vacmviewtreefamilyviewname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vacmviewtreefamilysubtree  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: vacmviewtreefamilymask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: vacmviewtreefamilytype
            
            	
            	**type**\:  :py:class:`VacmViewTreeFamilyTypeType <ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB.VacmViewTreeFamilyTypeType>`
            
            	**default value**\: included
            
            .. attribute:: vacmviewtreefamilystoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_VIEW_BASED_ACM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry, self).__init__()

                self.yang_name = "vacmViewTreeFamilyEntry"
                self.yang_parent_name = "vacmViewTreeFamilyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vacmviewtreefamilyviewname','vacmviewtreefamilysubtree']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vacmviewtreefamilyviewname', (YLeaf(YType.str, 'vacmViewTreeFamilyViewName'), ['str'])),
                    ('vacmviewtreefamilysubtree', (YLeaf(YType.str, 'vacmViewTreeFamilySubtree'), ['str'])),
                    ('vacmviewtreefamilymask', (YLeaf(YType.str, 'vacmViewTreeFamilyMask'), ['str'])),
                    ('vacmviewtreefamilytype', (YLeaf(YType.enumeration, 'vacmViewTreeFamilyType'), [('ydk.models.cisco_ios_xr.SNMP_VIEW_BASED_ACM_MIB', 'VacmViewTreeFamilyTypeType', '')])),
                    ('vacmviewtreefamilystoragetype', (YLeaf(YType.enumeration, 'vacmViewTreeFamilyStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.vacmviewtreefamilyviewname = None
                self.vacmviewtreefamilysubtree = None
                self.vacmviewtreefamilymask = None
                self.vacmviewtreefamilytype = None
                self.vacmviewtreefamilystoragetype = None
                self._segment_path = lambda: "vacmViewTreeFamilyEntry" + "[vacmViewTreeFamilyViewName='" + str(self.vacmviewtreefamilyviewname) + "']" + "[vacmViewTreeFamilySubtree='" + str(self.vacmviewtreefamilysubtree) + "']"
                self._absolute_path = lambda: "SNMP-VIEW-BASED-ACM-MIB:SNMP-VIEW-BASED-ACM-MIB/vacmViewTreeFamilyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry, ['vacmviewtreefamilyviewname', 'vacmviewtreefamilysubtree', 'vacmviewtreefamilymask', 'vacmviewtreefamilytype', 'vacmviewtreefamilystoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
                return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
            return meta._meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPVIEWBASEDACMMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_VIEW_BASED_ACM_MIB as meta
        return meta._meta_table['SNMPVIEWBASEDACMMIB']['meta_info']



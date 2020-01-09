""" SNMP_NOTIFICATION_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SnmpNotifyFilterTypeType(Enum):
    """
    SnmpNotifyFilterTypeType (Enum Class)

    .. data:: included = 1

    .. data:: excluded = 2

    """

    included = Enum.YLeaf(1, "included")

    excluded = Enum.YLeaf(2, "excluded")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SnmpNotifyFilterTypeType']


class SnmpNotifyTypeType(Enum):
    """
    SnmpNotifyTypeType (Enum Class)

    .. data:: trap = 1

    .. data:: inform = 2

    """

    trap = Enum.YLeaf(1, "trap")

    inform = Enum.YLeaf(2, "inform")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SnmpNotifyTypeType']



class SNMPNOTIFICATIONMIB(_Entity_):
    """
    
    
    .. attribute:: snmpnotifytable
    
    	
    	**type**\:  :py:class:`SnmpNotifyTable <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyTable>`
    
    .. attribute:: snmpnotifyfilterprofiletable
    
    	
    	**type**\:  :py:class:`SnmpNotifyFilterProfileTable <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable>`
    
    	**presence node**\: True
    
    .. attribute:: snmpnotifyfiltertable
    
    	
    	**type**\:  :py:class:`SnmpNotifyFilterTable <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'SNMP_NOTIFICATION_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPNOTIFICATIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-NOTIFICATION-MIB"
        self.yang_parent_name = "SNMP-NOTIFICATION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snmpNotifyTable", ("snmpnotifytable", SNMPNOTIFICATIONMIB.SnmpNotifyTable)), ("snmpNotifyFilterProfileTable", ("snmpnotifyfilterprofiletable", SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable)), ("snmpNotifyFilterTable", ("snmpnotifyfiltertable", SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable))])
        self._leafs = OrderedDict()

        self.snmpnotifytable = SNMPNOTIFICATIONMIB.SnmpNotifyTable()
        self.snmpnotifytable.parent = self
        self._children_name_map["snmpnotifytable"] = "snmpNotifyTable"

        self.snmpnotifyfilterprofiletable = None
        self._children_name_map["snmpnotifyfilterprofiletable"] = "snmpNotifyFilterProfileTable"

        self.snmpnotifyfiltertable = None
        self._children_name_map["snmpnotifyfiltertable"] = "snmpNotifyFilterTable"
        self._segment_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPNOTIFICATIONMIB, [], name, value)


    class SnmpNotifyTable(_Entity_):
        """
        
        
        .. attribute:: snmpnotifyentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpNotifyEntry <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry>`
        
        

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPNOTIFICATIONMIB.SnmpNotifyTable, self).__init__()

            self.yang_name = "snmpNotifyTable"
            self.yang_parent_name = "SNMP-NOTIFICATION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpNotifyEntry", ("snmpnotifyentry", SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry))])
            self._leafs = OrderedDict()

            self.snmpnotifyentry = YList(self)
            self._segment_path = lambda: "snmpNotifyTable"
            self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyTable, [], name, value)


        class SnmpNotifyEntry(_Entity_):
            """
            
            
            .. attribute:: snmpnotifyname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpnotifytag
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: snmpnotifytype
            
            	
            	**type**\:  :py:class:`SnmpNotifyTypeType <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SnmpNotifyTypeType>`
            
            	**default value**\: trap
            
            .. attribute:: snmpnotifystoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry, self).__init__()

                self.yang_name = "snmpNotifyEntry"
                self.yang_parent_name = "snmpNotifyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmpnotifyname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmpnotifyname', (YLeaf(YType.str, 'snmpNotifyName'), ['str'])),
                    ('snmpnotifytag', (YLeaf(YType.str, 'snmpNotifyTag'), ['str'])),
                    ('snmpnotifytype', (YLeaf(YType.enumeration, 'snmpNotifyType'), [('ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB', 'SnmpNotifyTypeType', '')])),
                    ('snmpnotifystoragetype', (YLeaf(YType.enumeration, 'snmpNotifyStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.snmpnotifyname = None
                self.snmpnotifytag = None
                self.snmpnotifytype = None
                self.snmpnotifystoragetype = None
                self._segment_path = lambda: "snmpNotifyEntry" + "[snmpNotifyName='" + str(self.snmpnotifyname) + "']"
                self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/snmpNotifyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry, ['snmpnotifyname', 'snmpnotifytag', 'snmpnotifytype', 'snmpnotifystoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable']['meta_info']


    class SnmpNotifyFilterProfileTable(_Entity_):
        """
        
        
        .. attribute:: snmpnotifyfilterprofileentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpNotifyFilterProfileEntry <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable, self).__init__()

            self.yang_name = "snmpNotifyFilterProfileTable"
            self.yang_parent_name = "SNMP-NOTIFICATION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpNotifyFilterProfileEntry", ("snmpnotifyfilterprofileentry", SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.snmpnotifyfilterprofileentry = YList(self)
            self._segment_path = lambda: "snmpNotifyFilterProfileTable"
            self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable, [], name, value)


        class SnmpNotifyFilterProfileEntry(_Entity_):
            """
            
            
            .. attribute:: snmptargetparamsname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpnotifyfilterprofilename
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpnotifyfilterprofilestortype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry, self).__init__()

                self.yang_name = "snmpNotifyFilterProfileEntry"
                self.yang_parent_name = "snmpNotifyFilterProfileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmptargetparamsname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmptargetparamsname', (YLeaf(YType.str, 'snmpTargetParamsName'), ['str'])),
                    ('snmpnotifyfilterprofilename', (YLeaf(YType.str, 'snmpNotifyFilterProfileName'), ['str'])),
                    ('snmpnotifyfilterprofilestortype', (YLeaf(YType.enumeration, 'snmpNotifyFilterProfileStorType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.snmptargetparamsname = None
                self.snmpnotifyfilterprofilename = None
                self.snmpnotifyfilterprofilestortype = None
                self._segment_path = lambda: "snmpNotifyFilterProfileEntry" + "[snmpTargetParamsName='" + str(self.snmptargetparamsname) + "']"
                self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/snmpNotifyFilterProfileTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry, ['snmptargetparamsname', 'snmpnotifyfilterprofilename', 'snmpnotifyfilterprofilestortype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable']['meta_info']


    class SnmpNotifyFilterTable(_Entity_):
        """
        
        
        .. attribute:: snmpnotifyfilterentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpNotifyFilterEntry <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'SNMP_NOTIFICATION_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable, self).__init__()

            self.yang_name = "snmpNotifyFilterTable"
            self.yang_parent_name = "SNMP-NOTIFICATION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpNotifyFilterEntry", ("snmpnotifyfilterentry", SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.snmpnotifyfilterentry = YList(self)
            self._segment_path = lambda: "snmpNotifyFilterTable"
            self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable, [], name, value)


        class SnmpNotifyFilterEntry(_Entity_):
            """
            
            
            .. attribute:: snmpnotifyfilterprofilename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpnotifyfiltersubtree  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmpnotifyfiltermask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmpnotifyfiltertype
            
            	
            	**type**\:  :py:class:`SnmpNotifyFilterTypeType <ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB.SnmpNotifyFilterTypeType>`
            
            	**default value**\: included
            
            .. attribute:: snmpnotifyfilterstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_NOTIFICATION_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry, self).__init__()

                self.yang_name = "snmpNotifyFilterEntry"
                self.yang_parent_name = "snmpNotifyFilterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmpnotifyfilterprofilename','snmpnotifyfiltersubtree']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmpnotifyfilterprofilename', (YLeaf(YType.str, 'snmpNotifyFilterProfileName'), ['str'])),
                    ('snmpnotifyfiltersubtree', (YLeaf(YType.str, 'snmpNotifyFilterSubtree'), ['str'])),
                    ('snmpnotifyfiltermask', (YLeaf(YType.str, 'snmpNotifyFilterMask'), ['str'])),
                    ('snmpnotifyfiltertype', (YLeaf(YType.enumeration, 'snmpNotifyFilterType'), [('ydk.models.cisco_ios_xr.SNMP_NOTIFICATION_MIB', 'SnmpNotifyFilterTypeType', '')])),
                    ('snmpnotifyfilterstoragetype', (YLeaf(YType.enumeration, 'snmpNotifyFilterStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.snmpnotifyfilterprofilename = None
                self.snmpnotifyfiltersubtree = None
                self.snmpnotifyfiltermask = None
                self.snmpnotifyfiltertype = None
                self.snmpnotifyfilterstoragetype = None
                self._segment_path = lambda: "snmpNotifyFilterEntry" + "[snmpNotifyFilterProfileName='" + str(self.snmpnotifyfilterprofilename) + "']" + "[snmpNotifyFilterSubtree='" + str(self.snmpnotifyfiltersubtree) + "']"
                self._absolute_path = lambda: "SNMP-NOTIFICATION-MIB:SNMP-NOTIFICATION-MIB/snmpNotifyFilterTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry, ['snmpnotifyfilterprofilename', 'snmpnotifyfiltersubtree', 'snmpnotifyfiltermask', 'snmpnotifyfiltertype', 'snmpnotifyfilterstoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
                return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
            return meta._meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPNOTIFICATIONMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_NOTIFICATION_MIB as meta
        return meta._meta_table['SNMPNOTIFICATIONMIB']['meta_info']



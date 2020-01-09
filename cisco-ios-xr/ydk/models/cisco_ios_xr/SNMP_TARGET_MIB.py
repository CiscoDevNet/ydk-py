""" SNMP_TARGET_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SNMPTARGETMIB(_Entity_):
    """
    
    
    .. attribute:: snmptargetobjects
    
    	
    	**type**\:  :py:class:`SnmpTargetObjects <ydk.models.cisco_ios_xr.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetObjects>`
    
    	**config**\: False
    
    .. attribute:: snmptargetaddrtable
    
    	
    	**type**\:  :py:class:`SnmpTargetAddrTable <ydk.models.cisco_ios_xr.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetAddrTable>`
    
    .. attribute:: snmptargetparamstable
    
    	
    	**type**\:  :py:class:`SnmpTargetParamsTable <ydk.models.cisco_ios_xr.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetParamsTable>`
    
    

    """

    _prefix = 'SNMP_TARGET_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPTARGETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-TARGET-MIB"
        self.yang_parent_name = "SNMP-TARGET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snmpTargetObjects", ("snmptargetobjects", SNMPTARGETMIB.SnmpTargetObjects)), ("snmpTargetAddrTable", ("snmptargetaddrtable", SNMPTARGETMIB.SnmpTargetAddrTable)), ("snmpTargetParamsTable", ("snmptargetparamstable", SNMPTARGETMIB.SnmpTargetParamsTable))])
        self._leafs = OrderedDict()

        self.snmptargetobjects = SNMPTARGETMIB.SnmpTargetObjects()
        self.snmptargetobjects.parent = self
        self._children_name_map["snmptargetobjects"] = "snmpTargetObjects"

        self.snmptargetaddrtable = SNMPTARGETMIB.SnmpTargetAddrTable()
        self.snmptargetaddrtable.parent = self
        self._children_name_map["snmptargetaddrtable"] = "snmpTargetAddrTable"

        self.snmptargetparamstable = SNMPTARGETMIB.SnmpTargetParamsTable()
        self.snmptargetparamstable.parent = self
        self._children_name_map["snmptargetparamstable"] = "snmpTargetParamsTable"
        self._segment_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPTARGETMIB, [], name, value)


    class SnmpTargetObjects(_Entity_):
        """
        
        
        .. attribute:: snmpunavailablecontexts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpunknowncontexts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPTARGETMIB.SnmpTargetObjects, self).__init__()

            self.yang_name = "snmpTargetObjects"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpunavailablecontexts', (YLeaf(YType.uint32, 'snmpUnavailableContexts'), ['int'])),
                ('snmpunknowncontexts', (YLeaf(YType.uint32, 'snmpUnknownContexts'), ['int'])),
            ])
            self.snmpunavailablecontexts = None
            self.snmpunknowncontexts = None
            self._segment_path = lambda: "snmpTargetObjects"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.SnmpTargetObjects, ['snmpunavailablecontexts', 'snmpunknowncontexts'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetObjects']['meta_info']


    class SnmpTargetAddrTable(_Entity_):
        """
        
        
        .. attribute:: snmptargetaddrentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpTargetAddrEntry <ydk.models.cisco_ios_xr.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry>`
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPTARGETMIB.SnmpTargetAddrTable, self).__init__()

            self.yang_name = "snmpTargetAddrTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpTargetAddrEntry", ("snmptargetaddrentry", SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry))])
            self._leafs = OrderedDict()

            self.snmptargetaddrentry = YList(self)
            self._segment_path = lambda: "snmpTargetAddrTable"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.SnmpTargetAddrTable, [], name, value)


        class SnmpTargetAddrEntry(_Entity_):
            """
            
            
            .. attribute:: snmptargetaddrname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrtdomain
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetaddrtaddress
            
            	
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (\\d\*(.\\d\*)\*)?
            
            		**type**\: str
            
            			**pattern:** (\\d\*(.\\d\*)\*)?
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetaddrtimeout
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**default value**\: 1500
            
            .. attribute:: snmptargetaddrretrycount
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            	**default value**\: 3
            
            .. attribute:: snmptargetaddrtaglist
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: snmptargetaddrparams
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetaddrstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            .. attribute:: snmptargetaddrengineid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: snmptargetaddrtmask
            
            	
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (\\d\*(.\\d\*)\*)?
            
            		**type**\: str
            
            			**pattern:** (\\d\*(.\\d\*)\*)?
            
            		**type**\: str
            
            			**pattern:** (\\d\*(.\\d\*)\*)?
            
            .. attribute:: snmptargetaddrmms
            
            	
            	**type**\: int
            
            	**range:** 0..0 \| 484..2147483647
            
            	**default value**\: 2048
            
            .. attribute:: enabled
            
            	
            	**type**\: bool
            
            	**default value**\: true
            
            

            """

            _prefix = 'SNMP_TARGET_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry, self).__init__()

                self.yang_name = "snmpTargetAddrEntry"
                self.yang_parent_name = "snmpTargetAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmptargetaddrname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmptargetaddrname', (YLeaf(YType.str, 'snmpTargetAddrName'), ['str'])),
                    ('snmptargetaddrtdomain', (YLeaf(YType.str, 'snmpTargetAddrTDomain'), ['str'])),
                    ('snmptargetaddrtaddress', (YLeaf(YType.str, 'snmpTargetAddrTAddress'), ['str','str'])),
                    ('snmptargetaddrtimeout', (YLeaf(YType.int32, 'snmpTargetAddrTimeout'), ['int'])),
                    ('snmptargetaddrretrycount', (YLeaf(YType.int32, 'snmpTargetAddrRetryCount'), ['int'])),
                    ('snmptargetaddrtaglist', (YLeaf(YType.str, 'snmpTargetAddrTagList'), ['str'])),
                    ('snmptargetaddrparams', (YLeaf(YType.str, 'snmpTargetAddrParams'), ['str'])),
                    ('snmptargetaddrstoragetype', (YLeaf(YType.enumeration, 'snmpTargetAddrStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                    ('snmptargetaddrengineid', (YLeaf(YType.str, 'snmpTargetAddrEngineID'), ['str'])),
                    ('snmptargetaddrtmask', (YLeaf(YType.str, 'snmpTargetAddrTMask'), ['str','str','str'])),
                    ('snmptargetaddrmms', (YLeaf(YType.int32, 'snmpTargetAddrMMS'), ['int'])),
                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                ])
                self.snmptargetaddrname = None
                self.snmptargetaddrtdomain = None
                self.snmptargetaddrtaddress = None
                self.snmptargetaddrtimeout = None
                self.snmptargetaddrretrycount = None
                self.snmptargetaddrtaglist = None
                self.snmptargetaddrparams = None
                self.snmptargetaddrstoragetype = None
                self.snmptargetaddrengineid = None
                self.snmptargetaddrtmask = None
                self.snmptargetaddrmms = None
                self.enabled = None
                self._segment_path = lambda: "snmpTargetAddrEntry" + "[snmpTargetAddrName='" + str(self.snmptargetaddrname) + "']"
                self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetAddrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry, ['snmptargetaddrname', 'snmptargetaddrtdomain', 'snmptargetaddrtaddress', 'snmptargetaddrtimeout', 'snmptargetaddrretrycount', 'snmptargetaddrtaglist', 'snmptargetaddrparams', 'snmptargetaddrstoragetype', 'snmptargetaddrengineid', 'snmptargetaddrtmask', 'snmptargetaddrmms', 'enabled'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SNMPTARGETMIB.SnmpTargetAddrTable.SnmpTargetAddrEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetAddrTable']['meta_info']


    class SnmpTargetParamsTable(_Entity_):
        """
        
        
        .. attribute:: snmptargetparamsentry
        
        	
        	**type**\: list of  		 :py:class:`SnmpTargetParamsEntry <ydk.models.cisco_ios_xr.SNMP_TARGET_MIB.SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry>`
        
        

        """

        _prefix = 'SNMP_TARGET_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPTARGETMIB.SnmpTargetParamsTable, self).__init__()

            self.yang_name = "snmpTargetParamsTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmpTargetParamsEntry", ("snmptargetparamsentry", SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry))])
            self._leafs = OrderedDict()

            self.snmptargetparamsentry = YList(self)
            self._segment_path = lambda: "snmpTargetParamsTable"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.SnmpTargetParamsTable, [], name, value)


        class SnmpTargetParamsEntry(_Entity_):
            """
            
            
            .. attribute:: snmptargetparamsname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetparamsmpmodel
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetparamssecuritymodel
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetparamssecurityname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetparamssecuritylevel
            
            	
            	**type**\:  :py:class:`SnmpSecurityLevel <ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB.SnmpSecurityLevel>`
            
            	**mandatory**\: True
            
            .. attribute:: snmptargetparamsstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            

            """

            _prefix = 'SNMP_TARGET_MIB'
            _revision = '2002-10-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry, self).__init__()

                self.yang_name = "snmpTargetParamsEntry"
                self.yang_parent_name = "snmpTargetParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmptargetparamsname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmptargetparamsname', (YLeaf(YType.str, 'snmpTargetParamsName'), ['str'])),
                    ('snmptargetparamsmpmodel', (YLeaf(YType.int32, 'snmpTargetParamsMPModel'), ['int'])),
                    ('snmptargetparamssecuritymodel', (YLeaf(YType.int32, 'snmpTargetParamsSecurityModel'), ['int'])),
                    ('snmptargetparamssecurityname', (YLeaf(YType.str, 'snmpTargetParamsSecurityName'), ['str'])),
                    ('snmptargetparamssecuritylevel', (YLeaf(YType.enumeration, 'snmpTargetParamsSecurityLevel'), [('ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB', 'SnmpSecurityLevel', '')])),
                    ('snmptargetparamsstoragetype', (YLeaf(YType.enumeration, 'snmpTargetParamsStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.snmptargetparamsname = None
                self.snmptargetparamsmpmodel = None
                self.snmptargetparamssecuritymodel = None
                self.snmptargetparamssecurityname = None
                self.snmptargetparamssecuritylevel = None
                self.snmptargetparamsstoragetype = None
                self._segment_path = lambda: "snmpTargetParamsEntry" + "[snmpTargetParamsName='" + str(self.snmptargetparamsname) + "']"
                self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry, ['snmptargetparamsname', 'snmptargetparamsmpmodel', 'snmptargetparamssecuritymodel', 'snmptargetparamssecurityname', 'snmptargetparamssecuritylevel', 'snmptargetparamsstoragetype'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
                return meta._meta_table['SNMPTARGETMIB.SnmpTargetParamsTable.SnmpTargetParamsEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
            return meta._meta_table['SNMPTARGETMIB.SnmpTargetParamsTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPTARGETMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_TARGET_MIB as meta
        return meta._meta_table['SNMPTARGETMIB']['meta_info']



""" SNMP_USER_BASED_SM_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SNMPUSERBASEDSMMIB(_Entity_):
    """
    
    
    .. attribute:: usmstats
    
    	
    	**type**\:  :py:class:`UsmStats <ydk.models.cisco_ios_xr.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmStats>`
    
    	**config**\: False
    
    .. attribute:: usmusertable
    
    	
    	**type**\:  :py:class:`UsmUserTable <ydk.models.cisco_ios_xr.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmUserTable>`
    
    

    """

    _prefix = 'SNMP_USER_BASED_SM_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPUSERBASEDSMMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-USER-BASED-SM-MIB"
        self.yang_parent_name = "SNMP-USER-BASED-SM-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("usmStats", ("usmstats", SNMPUSERBASEDSMMIB.UsmStats)), ("usmUserTable", ("usmusertable", SNMPUSERBASEDSMMIB.UsmUserTable))])
        self._leafs = OrderedDict()

        self.usmstats = SNMPUSERBASEDSMMIB.UsmStats()
        self.usmstats.parent = self
        self._children_name_map["usmstats"] = "usmStats"

        self.usmusertable = SNMPUSERBASEDSMMIB.UsmUserTable()
        self.usmusertable.parent = self
        self._children_name_map["usmusertable"] = "usmUserTable"
        self._segment_path = lambda: "SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPUSERBASEDSMMIB, [], name, value)


    class UsmStats(_Entity_):
        """
        
        
        .. attribute:: usmstatsunsupportedseclevels
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: usmstatsnotintimewindows
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: usmstatsunknownusernames
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: usmstatsunknownengineids
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: usmstatswrongdigests
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: usmstatsdecryptionerrors
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMP_USER_BASED_SM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPUSERBASEDSMMIB.UsmStats, self).__init__()

            self.yang_name = "usmStats"
            self.yang_parent_name = "SNMP-USER-BASED-SM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('usmstatsunsupportedseclevels', (YLeaf(YType.uint32, 'usmStatsUnsupportedSecLevels'), ['int'])),
                ('usmstatsnotintimewindows', (YLeaf(YType.uint32, 'usmStatsNotInTimeWindows'), ['int'])),
                ('usmstatsunknownusernames', (YLeaf(YType.uint32, 'usmStatsUnknownUserNames'), ['int'])),
                ('usmstatsunknownengineids', (YLeaf(YType.uint32, 'usmStatsUnknownEngineIDs'), ['int'])),
                ('usmstatswrongdigests', (YLeaf(YType.uint32, 'usmStatsWrongDigests'), ['int'])),
                ('usmstatsdecryptionerrors', (YLeaf(YType.uint32, 'usmStatsDecryptionErrors'), ['int'])),
            ])
            self.usmstatsunsupportedseclevels = None
            self.usmstatsnotintimewindows = None
            self.usmstatsunknownusernames = None
            self.usmstatsunknownengineids = None
            self.usmstatswrongdigests = None
            self.usmstatsdecryptionerrors = None
            self._segment_path = lambda: "usmStats"
            self._absolute_path = lambda: "SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPUSERBASEDSMMIB.UsmStats, ['usmstatsunsupportedseclevels', 'usmstatsnotintimewindows', 'usmstatsunknownusernames', 'usmstatsunknownengineids', 'usmstatswrongdigests', 'usmstatsdecryptionerrors'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_USER_BASED_SM_MIB as meta
            return meta._meta_table['SNMPUSERBASEDSMMIB.UsmStats']['meta_info']


    class UsmUserTable(_Entity_):
        """
        
        
        .. attribute:: usmuserentry
        
        	
        	**type**\: list of  		 :py:class:`UsmUserEntry <ydk.models.cisco_ios_xr.SNMP_USER_BASED_SM_MIB.SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry>`
        
        

        """

        _prefix = 'SNMP_USER_BASED_SM_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPUSERBASEDSMMIB.UsmUserTable, self).__init__()

            self.yang_name = "usmUserTable"
            self.yang_parent_name = "SNMP-USER-BASED-SM-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("usmUserEntry", ("usmuserentry", SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry))])
            self._leafs = OrderedDict()

            self.usmuserentry = YList(self)
            self._segment_path = lambda: "usmUserTable"
            self._absolute_path = lambda: "SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPUSERBASEDSMMIB.UsmUserTable, [], name, value)


        class UsmUserEntry(_Entity_):
            """
            
            
            .. attribute:: usmuserengineid  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmusername  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: usmusersecurityname
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**mandatory**\: True
            
            .. attribute:: usmuserclonefrom
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: usmuserauthprotocol
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**default value**\: 1.3.6.1.6.3.10.1.1.1
            
            .. attribute:: usmuserauthkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserownauthkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserprivprotocol
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**default value**\: 1.3.6.1.6.3.10.1.2.1
            
            .. attribute:: usmuserprivkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserownprivkeychange
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserpublic
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserstoragetype
            
            	
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xr.SNMPv2_TC.StorageType>`
            
            	**default value**\: nonVolatile
            
            .. attribute:: usmuserauthkey
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: usmuserprivkey
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            

            """

            _prefix = 'SNMP_USER_BASED_SM_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry, self).__init__()

                self.yang_name = "usmUserEntry"
                self.yang_parent_name = "usmUserTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['usmuserengineid','usmusername']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('usmuserengineid', (YLeaf(YType.str, 'usmUserEngineID'), ['str'])),
                    ('usmusername', (YLeaf(YType.str, 'usmUserName'), ['str'])),
                    ('usmusersecurityname', (YLeaf(YType.str, 'usmUserSecurityName'), ['str'])),
                    ('usmuserclonefrom', (YLeaf(YType.str, 'usmUserCloneFrom'), ['str'])),
                    ('usmuserauthprotocol', (YLeaf(YType.str, 'usmUserAuthProtocol'), ['str'])),
                    ('usmuserauthkeychange', (YLeaf(YType.str, 'usmUserAuthKeyChange'), ['str'])),
                    ('usmuserownauthkeychange', (YLeaf(YType.str, 'usmUserOwnAuthKeyChange'), ['str'])),
                    ('usmuserprivprotocol', (YLeaf(YType.str, 'usmUserPrivProtocol'), ['str'])),
                    ('usmuserprivkeychange', (YLeaf(YType.str, 'usmUserPrivKeyChange'), ['str'])),
                    ('usmuserownprivkeychange', (YLeaf(YType.str, 'usmUserOwnPrivKeyChange'), ['str'])),
                    ('usmuserpublic', (YLeaf(YType.str, 'usmUserPublic'), ['str'])),
                    ('usmuserstoragetype', (YLeaf(YType.enumeration, 'usmUserStorageType'), [('ydk.models.cisco_ios_xr.SNMPv2_TC', 'StorageType', '')])),
                    ('usmuserauthkey', (YLeaf(YType.str, 'usmUserAuthKey'), ['str'])),
                    ('usmuserprivkey', (YLeaf(YType.str, 'usmUserPrivKey'), ['str'])),
                ])
                self.usmuserengineid = None
                self.usmusername = None
                self.usmusersecurityname = None
                self.usmuserclonefrom = None
                self.usmuserauthprotocol = None
                self.usmuserauthkeychange = None
                self.usmuserownauthkeychange = None
                self.usmuserprivprotocol = None
                self.usmuserprivkeychange = None
                self.usmuserownprivkeychange = None
                self.usmuserpublic = None
                self.usmuserstoragetype = None
                self.usmuserauthkey = None
                self.usmuserprivkey = None
                self._segment_path = lambda: "usmUserEntry" + "[usmUserEngineID='" + str(self.usmuserengineid) + "']" + "[usmUserName='" + str(self.usmusername) + "']"
                self._absolute_path = lambda: "SNMP-USER-BASED-SM-MIB:SNMP-USER-BASED-SM-MIB/usmUserTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry, ['usmuserengineid', 'usmusername', 'usmusersecurityname', 'usmuserclonefrom', 'usmuserauthprotocol', 'usmuserauthkeychange', 'usmuserownauthkeychange', 'usmuserprivprotocol', 'usmuserprivkeychange', 'usmuserownprivkeychange', 'usmuserpublic', 'usmuserstoragetype', 'usmuserauthkey', 'usmuserprivkey'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMP_USER_BASED_SM_MIB as meta
                return meta._meta_table['SNMPUSERBASEDSMMIB.UsmUserTable.UsmUserEntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_USER_BASED_SM_MIB as meta
            return meta._meta_table['SNMPUSERBASEDSMMIB.UsmUserTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPUSERBASEDSMMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_USER_BASED_SM_MIB as meta
        return meta._meta_table['SNMPUSERBASEDSMMIB']['meta_info']



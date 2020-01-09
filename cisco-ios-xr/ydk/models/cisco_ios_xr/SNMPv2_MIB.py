""" SNMPv2_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SnmpEnableAuthenTrapsType(Enum):
    """
    SnmpEnableAuthenTrapsType (Enum Class)

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = Enum.YLeaf(1, "enabled")

    disabled = Enum.YLeaf(2, "disabled")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
        return meta._meta_table['SnmpEnableAuthenTrapsType']



class SNMPv2MIB(_Entity_):
    """
    
    
    .. attribute:: system
    
    	
    	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.SNMPv2_MIB.SNMPv2MIB.System>`
    
    .. attribute:: snmp
    
    	
    	**type**\:  :py:class:`Snmp <ydk.models.cisco_ios_xr.SNMPv2_MIB.SNMPv2MIB.Snmp>`
    
    .. attribute:: snmpset
    
    	
    	**type**\:  :py:class:`SnmpSet <ydk.models.cisco_ios_xr.SNMPv2_MIB.SNMPv2MIB.SnmpSet>`
    
    .. attribute:: sysortable
    
    	
    	**type**\:  :py:class:`SysORTable <ydk.models.cisco_ios_xr.SNMPv2_MIB.SNMPv2MIB.SysORTable>`
    
    

    """

    _prefix = 'SNMPv2_MIB'
    _revision = '2002-10-16'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPv2MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMPv2-MIB"
        self.yang_parent_name = "SNMPv2-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("system", ("system", SNMPv2MIB.System)), ("snmp", ("snmp", SNMPv2MIB.Snmp)), ("snmpSet", ("snmpset", SNMPv2MIB.SnmpSet)), ("sysORTable", ("sysortable", SNMPv2MIB.SysORTable))])
        self._leafs = OrderedDict()

        self.system = SNMPv2MIB.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"

        self.snmp = SNMPv2MIB.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"

        self.snmpset = SNMPv2MIB.SnmpSet()
        self.snmpset.parent = self
        self._children_name_map["snmpset"] = "snmpSet"

        self.sysortable = SNMPv2MIB.SysORTable()
        self.sysortable.parent = self
        self._children_name_map["sysortable"] = "sysORTable"
        self._segment_path = lambda: "SNMPv2-MIB:SNMPv2-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPv2MIB, [], name, value)


    class System(_Entity_):
        """
        
        
        .. attribute:: sysdescr
        
        	
        	**type**\: str
        
        	**length:** 0..255
        
        	**config**\: False
        
        .. attribute:: sysobjectid
        
        	
        	**type**\: str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        	**config**\: False
        
        .. attribute:: sysuptime
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: syscontact
        
        	
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysname
        
        	
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: syslocation
        
        	
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysservices
        
        	
        	**type**\: int
        
        	**range:** 0..127
        
        	**config**\: False
        
        .. attribute:: sysorlastchange
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPv2MIB.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sysdescr', (YLeaf(YType.str, 'sysDescr'), ['str'])),
                ('sysobjectid', (YLeaf(YType.str, 'sysObjectID'), ['str'])),
                ('sysuptime', (YLeaf(YType.uint32, 'sysUpTime'), ['int'])),
                ('syscontact', (YLeaf(YType.str, 'sysContact'), ['str'])),
                ('sysname', (YLeaf(YType.str, 'sysName'), ['str'])),
                ('syslocation', (YLeaf(YType.str, 'sysLocation'), ['str'])),
                ('sysservices', (YLeaf(YType.int32, 'sysServices'), ['int'])),
                ('sysorlastchange', (YLeaf(YType.uint32, 'sysORLastChange'), ['int'])),
            ])
            self.sysdescr = None
            self.sysobjectid = None
            self.sysuptime = None
            self.syscontact = None
            self.sysname = None
            self.syslocation = None
            self.sysservices = None
            self.sysorlastchange = None
            self._segment_path = lambda: "system"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.System, ['sysdescr', 'sysobjectid', 'sysuptime', 'syscontact', 'sysname', 'syslocation', 'sysservices', 'sysorlastchange'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.System']['meta_info']


    class Snmp(_Entity_):
        """
        
        
        .. attribute:: snmpinpkts
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpinbadversions
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpinbadcommunitynames
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpinbadcommunityuses
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpinasnparseerrs
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpenableauthentraps
        
        	
        	**type**\:  :py:class:`SnmpEnableAuthenTrapsType <ydk.models.cisco_ios_xr.SNMPv2_MIB.SnmpEnableAuthenTrapsType>`
        
        	**default value**\: disabled
        
        .. attribute:: snmpsilentdrops
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpproxydrops
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPv2MIB.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpinpkts', (YLeaf(YType.uint32, 'snmpInPkts'), ['int'])),
                ('snmpinbadversions', (YLeaf(YType.uint32, 'snmpInBadVersions'), ['int'])),
                ('snmpinbadcommunitynames', (YLeaf(YType.uint32, 'snmpInBadCommunityNames'), ['int'])),
                ('snmpinbadcommunityuses', (YLeaf(YType.uint32, 'snmpInBadCommunityUses'), ['int'])),
                ('snmpinasnparseerrs', (YLeaf(YType.uint32, 'snmpInASNParseErrs'), ['int'])),
                ('snmpenableauthentraps', (YLeaf(YType.enumeration, 'snmpEnableAuthenTraps'), [('ydk.models.cisco_ios_xr.SNMPv2_MIB', 'SnmpEnableAuthenTrapsType', '')])),
                ('snmpsilentdrops', (YLeaf(YType.uint32, 'snmpSilentDrops'), ['int'])),
                ('snmpproxydrops', (YLeaf(YType.uint32, 'snmpProxyDrops'), ['int'])),
            ])
            self.snmpinpkts = None
            self.snmpinbadversions = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinasnparseerrs = None
            self.snmpenableauthentraps = None
            self.snmpsilentdrops = None
            self.snmpproxydrops = None
            self._segment_path = lambda: "snmp"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.Snmp, ['snmpinpkts', 'snmpinbadversions', 'snmpinbadcommunitynames', 'snmpinbadcommunityuses', 'snmpinasnparseerrs', 'snmpenableauthentraps', 'snmpsilentdrops', 'snmpproxydrops'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.Snmp']['meta_info']


    class SnmpSet(_Entity_):
        """
        
        
        .. attribute:: snmpsetserialno
        
        	
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPv2MIB.SnmpSet, self).__init__()

            self.yang_name = "snmpSet"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpsetserialno', (YLeaf(YType.int32, 'snmpSetSerialNo'), ['int'])),
            ])
            self.snmpsetserialno = None
            self._segment_path = lambda: "snmpSet"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.SnmpSet, ['snmpsetserialno'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.SnmpSet']['meta_info']


    class SysORTable(_Entity_):
        """
        
        
        .. attribute:: sysorentry
        
        	
        	**type**\: list of  		 :py:class:`SysOREntry <ydk.models.cisco_ios_xr.SNMPv2_MIB.SNMPv2MIB.SysORTable.SysOREntry>`
        
        

        """

        _prefix = 'SNMPv2_MIB'
        _revision = '2002-10-16'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPv2MIB.SysORTable, self).__init__()

            self.yang_name = "sysORTable"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sysOREntry", ("sysorentry", SNMPv2MIB.SysORTable.SysOREntry))])
            self._leafs = OrderedDict()

            self.sysorentry = YList(self)
            self._segment_path = lambda: "sysORTable"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.SysORTable, [], name, value)


        class SysOREntry(_Entity_):
            """
            
            
            .. attribute:: sysorindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sysorid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: sysordescr
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: sysoruptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'SNMPv2_MIB'
            _revision = '2002-10-16'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SNMPv2MIB.SysORTable.SysOREntry, self).__init__()

                self.yang_name = "sysOREntry"
                self.yang_parent_name = "sysORTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sysorindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sysorindex', (YLeaf(YType.int32, 'sysORIndex'), ['int'])),
                    ('sysorid', (YLeaf(YType.str, 'sysORID'), ['str'])),
                    ('sysordescr', (YLeaf(YType.str, 'sysORDescr'), ['str'])),
                    ('sysoruptime', (YLeaf(YType.uint32, 'sysORUpTime'), ['int'])),
                ])
                self.sysorindex = None
                self.sysorid = None
                self.sysordescr = None
                self.sysoruptime = None
                self._segment_path = lambda: "sysOREntry" + "[sysORIndex='" + str(self.sysorindex) + "']"
                self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/sysORTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPv2MIB.SysORTable.SysOREntry, ['sysorindex', 'sysorid', 'sysordescr', 'sysoruptime'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
                return meta._meta_table['SNMPv2MIB.SysORTable.SysOREntry']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
            return meta._meta_table['SNMPv2MIB.SysORTable']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPv2MIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMPv2_MIB as meta
        return meta._meta_table['SNMPv2MIB']['meta_info']



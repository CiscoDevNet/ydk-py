""" SNMP_FRAMEWORK_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SnmpSecurityLevel(Enum):
    """
    SnmpSecurityLevel (Enum Class)

    .. data:: noAuthNoPriv = 1

    .. data:: authNoPriv = 2

    .. data:: authPriv = 3

    """

    noAuthNoPriv = Enum.YLeaf(1, "noAuthNoPriv")

    authNoPriv = Enum.YLeaf(2, "authNoPriv")

    authPriv = Enum.YLeaf(3, "authPriv")



class SNMPFRAMEWORKMIB(Entity):
    """
    
    
    .. attribute:: snmpengine
    
    	
    	**type**\:  :py:class:`Snmpengine <ydk.models.cisco_ios_xr.SNMP_FRAMEWORK_MIB.SNMPFRAMEWORKMIB.Snmpengine>`
    
    

    """

    _prefix = 'SNMP_FRAMEWORK_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(SNMPFRAMEWORKMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-FRAMEWORK-MIB"
        self.yang_parent_name = "SNMP-FRAMEWORK-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("snmpEngine", ("snmpengine", SNMPFRAMEWORKMIB.Snmpengine))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.snmpengine = SNMPFRAMEWORKMIB.Snmpengine()
        self.snmpengine.parent = self
        self._children_name_map["snmpengine"] = "snmpEngine"
        self._children_yang_names.add("snmpEngine")
        self._segment_path = lambda: "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB"


    class Snmpengine(Entity):
        """
        
        
        .. attribute:: snmpengineid
        
        	
        	**type**\: str
        
        	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
        
        .. attribute:: snmpengineboots
        
        	
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: snmpenginetime
        
        	
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: snmpenginemaxmessagesize
        
        	
        	**type**\: int
        
        	**range:** 484..2147483647
        
        

        """

        _prefix = 'SNMP_FRAMEWORK_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            super(SNMPFRAMEWORKMIB.Snmpengine, self).__init__()

            self.yang_name = "snmpEngine"
            self.yang_parent_name = "SNMP-FRAMEWORK-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpengineid', YLeaf(YType.str, 'snmpEngineID')),
                ('snmpengineboots', YLeaf(YType.int32, 'snmpEngineBoots')),
                ('snmpenginetime', YLeaf(YType.int32, 'snmpEngineTime')),
                ('snmpenginemaxmessagesize', YLeaf(YType.int32, 'snmpEngineMaxMessageSize')),
            ])
            self.snmpengineid = None
            self.snmpengineboots = None
            self.snmpenginetime = None
            self.snmpenginemaxmessagesize = None
            self._segment_path = lambda: "snmpEngine"
            self._absolute_path = lambda: "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPFRAMEWORKMIB.Snmpengine, ['snmpengineid', 'snmpengineboots', 'snmpenginetime', 'snmpenginemaxmessagesize'], name, value)

    def clone_ptr(self):
        self._top_entity = SNMPFRAMEWORKMIB()
        return self._top_entity


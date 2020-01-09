""" SNMP_MPD_MIB 


"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SNMPMPDMIB(_Entity_):
    """
    
    
    .. attribute:: snmpmpdstats
    
    	
    	**type**\:  :py:class:`SnmpMPDStats <ydk.models.cisco_ios_xr.SNMP_MPD_MIB.SNMPMPDMIB.SnmpMPDStats>`
    
    	**config**\: False
    
    

    """

    _prefix = 'SNMP_MPD_MIB'
    _revision = '2002-10-14'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SNMPMPDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-MPD-MIB"
        self.yang_parent_name = "SNMP-MPD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snmpMPDStats", ("snmpmpdstats", SNMPMPDMIB.SnmpMPDStats))])
        self._leafs = OrderedDict()

        self.snmpmpdstats = SNMPMPDMIB.SnmpMPDStats()
        self.snmpmpdstats.parent = self
        self._children_name_map["snmpmpdstats"] = "snmpMPDStats"
        self._segment_path = lambda: "SNMP-MPD-MIB:SNMP-MPD-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPMPDMIB, [], name, value)


    class SnmpMPDStats(_Entity_):
        """
        
        
        .. attribute:: snmpunknownsecuritymodels
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpinvalidmsgs
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: snmpunknownpduhandlers
        
        	
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMP_MPD_MIB'
        _revision = '2002-10-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SNMPMPDMIB.SnmpMPDStats, self).__init__()

            self.yang_name = "snmpMPDStats"
            self.yang_parent_name = "SNMP-MPD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpunknownsecuritymodels', (YLeaf(YType.uint32, 'snmpUnknownSecurityModels'), ['int'])),
                ('snmpinvalidmsgs', (YLeaf(YType.uint32, 'snmpInvalidMsgs'), ['int'])),
                ('snmpunknownpduhandlers', (YLeaf(YType.uint32, 'snmpUnknownPDUHandlers'), ['int'])),
            ])
            self.snmpunknownsecuritymodels = None
            self.snmpinvalidmsgs = None
            self.snmpunknownpduhandlers = None
            self._segment_path = lambda: "snmpMPDStats"
            self._absolute_path = lambda: "SNMP-MPD-MIB:SNMP-MPD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPMPDMIB.SnmpMPDStats, ['snmpunknownsecuritymodels', 'snmpinvalidmsgs', 'snmpunknownpduhandlers'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _SNMP_MPD_MIB as meta
            return meta._meta_table['SNMPMPDMIB.SnmpMPDStats']['meta_info']

    def clone_ptr(self):
        self._top_entity = SNMPMPDMIB()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _SNMP_MPD_MIB as meta
        return meta._meta_table['SNMPMPDMIB']['meta_info']



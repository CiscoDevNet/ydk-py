""" SNMP_FRAMEWORK_MIB 

The SNMP Management Architecture MIB

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3411;
see the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

from ydk.models.ietf.ietf_yang_smiv2 import ObjectIdentity


class SnmpSecurityLevel(Enum):
    """
    SnmpSecurityLevel (Enum Class)

    A Level of Security at which SNMP messages can be

    sent or with which operations are being processed;

    in particular, one of\:

      noAuthNoPriv \- without authentication and

                     without privacy,

      authNoPriv   \- with authentication but

                     without privacy,

      authPriv     \- with authentication and

                     with privacy.

    These three values are ordered such that

    noAuthNoPriv is less than authNoPriv and

    authNoPriv is less than authPriv.

    .. data:: noAuthNoPriv = 1

    .. data:: authNoPriv = 2

    .. data:: authPriv = 3

    """

    noAuthNoPriv = Enum.YLeaf(1, "noAuthNoPriv")

    authNoPriv = Enum.YLeaf(2, "authNoPriv")

    authPriv = Enum.YLeaf(3, "authPriv")



class SnmpAuthProtocols(ObjectIdentity):
    """
    Registration point for standards\-track
    authentication protocols used in SNMP Management
    Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:SNMP-FRAMEWORK-MIB", pref="SNMP-FRAMEWORK-MIB", tag="SNMP-FRAMEWORK-MIB:snmpAuthProtocols"):
        super(SnmpAuthProtocols, self).__init__(ns, pref, tag)



class SnmpPrivProtocols(ObjectIdentity):
    """
    Registration point for standards\-track privacy
    protocols used in SNMP Management Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:smiv2:SNMP-FRAMEWORK-MIB", pref="SNMP-FRAMEWORK-MIB", tag="SNMP-FRAMEWORK-MIB:snmpPrivProtocols"):
        super(SnmpPrivProtocols, self).__init__(ns, pref, tag)



class SNMPFRAMEWORKMIB(Entity):
    """
    
    
    .. attribute:: snmpengine
    
    	
    	**type**\:  :py:class:`SnmpEngine <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.SNMPFRAMEWORKMIB.SnmpEngine>`
    
    	**config**\: False
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(SNMPFRAMEWORKMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-FRAMEWORK-MIB"
        self.yang_parent_name = "SNMP-FRAMEWORK-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("snmpEngine", ("snmpengine", SNMPFRAMEWORKMIB.SnmpEngine))])
        self._leafs = OrderedDict()

        self.snmpengine = SNMPFRAMEWORKMIB.SnmpEngine()
        self.snmpengine.parent = self
        self._children_name_map["snmpengine"] = "snmpEngine"
        self._segment_path = lambda: "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SNMPFRAMEWORKMIB, [], name, value)


    class SnmpEngine(Entity):
        """
        
        
        .. attribute:: snmpengineid
        
        	An SNMP engine's administratively\-unique identifier.  This information SHOULD be stored in non\-volatile storage so that it remains constant across re\-initializations of the SNMP engine
        	**type**\: str
        
        	**length:** 5..32
        
        	**config**\: False
        
        .. attribute:: snmpengineboots
        
        	The number of times that the SNMP engine has (re\-)initialized itself since snmpEngineID was last configured
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**config**\: False
        
        .. attribute:: snmpenginetime
        
        	The number of seconds since the value of the snmpEngineBoots object last changed. When incrementing this object's value would cause it to exceed its maximum, snmpEngineBoots is incremented as if a re\-initialization had occurred, and this object's value consequently reverts to zero
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: snmpenginemaxmessagesize
        
        	The maximum length in octets of an SNMP message which this SNMP engine can send or receive and process, determined as the minimum of the maximum message size values supported among all of the transports available to and supported by the engine
        	**type**\: int
        
        	**range:** 484..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'SNMP-FRAMEWORK-MIB'
        _revision = '2002-10-14'

        def __init__(self):
            super(SNMPFRAMEWORKMIB.SnmpEngine, self).__init__()

            self.yang_name = "snmpEngine"
            self.yang_parent_name = "SNMP-FRAMEWORK-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpengineid', (YLeaf(YType.str, 'snmpEngineID'), ['str'])),
                ('snmpengineboots', (YLeaf(YType.int32, 'snmpEngineBoots'), ['int'])),
                ('snmpenginetime', (YLeaf(YType.int32, 'snmpEngineTime'), ['int'])),
                ('snmpenginemaxmessagesize', (YLeaf(YType.int32, 'snmpEngineMaxMessageSize'), ['int'])),
            ])
            self.snmpengineid = None
            self.snmpengineboots = None
            self.snmpenginetime = None
            self.snmpenginemaxmessagesize = None
            self._segment_path = lambda: "snmpEngine"
            self._absolute_path = lambda: "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPFRAMEWORKMIB.SnmpEngine, ['snmpengineid', 'snmpengineboots', 'snmpenginetime', 'snmpenginemaxmessagesize'], name, value)


    def clone_ptr(self):
        self._top_entity = SNMPFRAMEWORKMIB()
        return self._top_entity




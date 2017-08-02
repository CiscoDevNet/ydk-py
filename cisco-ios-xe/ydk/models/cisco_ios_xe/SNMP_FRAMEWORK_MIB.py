""" SNMP_FRAMEWORK_MIB 

The SNMP Management Architecture MIB

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3411;
see the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Snmpsecuritylevel(Enum):
    """
    Snmpsecuritylevel

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



class Snmpprivprotocols(Identity):
    """
    Registration point for standards\-track privacy
    protocols used in SNMP Management Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(Snmpprivprotocols, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:SNMP-FRAMEWORK-MIB", "SNMP-FRAMEWORK-MIB", "SNMP-FRAMEWORK-MIB:snmpPrivProtocols")


class Snmpauthprotocols(Identity):
    """
    Registration point for standards\-track
    authentication protocols used in SNMP Management
    Frameworks.
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(Snmpauthprotocols, self).__init__("urn:ietf:params:xml:ns:yang:smiv2:SNMP-FRAMEWORK-MIB", "SNMP-FRAMEWORK-MIB", "SNMP-FRAMEWORK-MIB:snmpAuthProtocols")


class SnmpFrameworkMib(Entity):
    """
    
    
    .. attribute:: snmpengine
    
    	
    	**type**\:   :py:class:`Snmpengine <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.SnmpFrameworkMib.Snmpengine>`
    
    

    """

    _prefix = 'SNMP-FRAMEWORK-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(SnmpFrameworkMib, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-FRAMEWORK-MIB"
        self.yang_parent_name = "SNMP-FRAMEWORK-MIB"

        self.snmpengine = SnmpFrameworkMib.Snmpengine()
        self.snmpengine.parent = self
        self._children_name_map["snmpengine"] = "snmpEngine"
        self._children_yang_names.add("snmpEngine")


    class Snmpengine(Entity):
        """
        
        
        .. attribute:: snmpengineboots
        
        	The number of times that the SNMP engine has (re\-)initialized itself since snmpEngineID was last configured
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: snmpengineid
        
        	An SNMP engine's administratively\-unique identifier.  This information SHOULD be stored in non\-volatile storage so that it remains constant across re\-initializations of the SNMP engine
        	**type**\:  str
        
        	**length:** 5..32
        
        .. attribute:: snmpenginemaxmessagesize
        
        	The maximum length in octets of an SNMP message which this SNMP engine can send or receive and process, determined as the minimum of the maximum message size values supported among all of the transports available to and supported by the engine
        	**type**\:  int
        
        	**range:** 484..2147483647
        
        .. attribute:: snmpenginetime
        
        	The number of seconds since the value of the snmpEngineBoots object last changed. When incrementing this object's value would cause it to exceed its maximum, snmpEngineBoots is incremented as if a re\-initialization had occurred, and this object's value consequently reverts to zero
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'SNMP-FRAMEWORK-MIB'
        _revision = '2002-10-14'

        def __init__(self):
            super(SnmpFrameworkMib.Snmpengine, self).__init__()

            self.yang_name = "snmpEngine"
            self.yang_parent_name = "SNMP-FRAMEWORK-MIB"

            self.snmpengineboots = YLeaf(YType.int32, "snmpEngineBoots")

            self.snmpengineid = YLeaf(YType.str, "snmpEngineID")

            self.snmpenginemaxmessagesize = YLeaf(YType.int32, "snmpEngineMaxMessageSize")

            self.snmpenginetime = YLeaf(YType.int32, "snmpEngineTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("snmpengineboots",
                            "snmpengineid",
                            "snmpenginemaxmessagesize",
                            "snmpenginetime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SnmpFrameworkMib.Snmpengine, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SnmpFrameworkMib.Snmpengine, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.snmpengineboots.is_set or
                self.snmpengineid.is_set or
                self.snmpenginemaxmessagesize.is_set or
                self.snmpenginetime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.snmpengineboots.yfilter != YFilter.not_set or
                self.snmpengineid.yfilter != YFilter.not_set or
                self.snmpenginemaxmessagesize.yfilter != YFilter.not_set or
                self.snmpenginetime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpEngine" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.snmpengineboots.is_set or self.snmpengineboots.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpengineboots.get_name_leafdata())
            if (self.snmpengineid.is_set or self.snmpengineid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpengineid.get_name_leafdata())
            if (self.snmpenginemaxmessagesize.is_set or self.snmpenginemaxmessagesize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpenginemaxmessagesize.get_name_leafdata())
            if (self.snmpenginetime.is_set or self.snmpenginetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpenginetime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpEngineBoots" or name == "snmpEngineID" or name == "snmpEngineMaxMessageSize" or name == "snmpEngineTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "snmpEngineBoots"):
                self.snmpengineboots = value
                self.snmpengineboots.value_namespace = name_space
                self.snmpengineboots.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpEngineID"):
                self.snmpengineid = value
                self.snmpengineid.value_namespace = name_space
                self.snmpengineid.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpEngineMaxMessageSize"):
                self.snmpenginemaxmessagesize = value
                self.snmpenginemaxmessagesize.value_namespace = name_space
                self.snmpenginemaxmessagesize.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpEngineTime"):
                self.snmpenginetime = value
                self.snmpenginetime.value_namespace = name_space
                self.snmpenginetime.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.snmpengine is not None and self.snmpengine.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.snmpengine is not None and self.snmpengine.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "SNMP-FRAMEWORK-MIB:SNMP-FRAMEWORK-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "snmpEngine"):
            if (self.snmpengine is None):
                self.snmpengine = SnmpFrameworkMib.Snmpengine()
                self.snmpengine.parent = self
                self._children_name_map["snmpengine"] = "snmpEngine"
            return self.snmpengine

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "snmpEngine"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SnmpFrameworkMib()
        return self._top_entity


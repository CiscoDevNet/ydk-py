""" SNMP_PROXY_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters
used by a proxy forwarding application.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3413;
see the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SnmpProxyMib(Entity):
    """
    
    
    .. attribute:: snmpproxytable
    
    	The table of translation parameters used by proxy forwarder applications for forwarding SNMP messages
    	**type**\:   :py:class:`Snmpproxytable <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SnmpProxyMib.Snmpproxytable>`
    
    

    """

    _prefix = 'SNMP-PROXY-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(SnmpProxyMib, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-PROXY-MIB"
        self.yang_parent_name = "SNMP-PROXY-MIB"

        self.snmpproxytable = SnmpProxyMib.Snmpproxytable()
        self.snmpproxytable.parent = self
        self._children_name_map["snmpproxytable"] = "snmpProxyTable"
        self._children_yang_names.add("snmpProxyTable")


    class Snmpproxytable(Entity):
        """
        The table of translation parameters used by proxy forwarder
        applications for forwarding SNMP messages.
        
        .. attribute:: snmpproxyentry
        
        	A set of translation parameters used by a proxy forwarder application for forwarding SNMP messages.  Entries in the snmpProxyTable are created and deleted using the snmpProxyRowStatus object
        	**type**\: list of    :py:class:`Snmpproxyentry <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SnmpProxyMib.Snmpproxytable.Snmpproxyentry>`
        
        

        """

        _prefix = 'SNMP-PROXY-MIB'
        _revision = '2002-10-14'

        def __init__(self):
            super(SnmpProxyMib.Snmpproxytable, self).__init__()

            self.yang_name = "snmpProxyTable"
            self.yang_parent_name = "SNMP-PROXY-MIB"

            self.snmpproxyentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SnmpProxyMib.Snmpproxytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SnmpProxyMib.Snmpproxytable, self).__setattr__(name, value)


        class Snmpproxyentry(Entity):
            """
            A set of translation parameters used by a proxy forwarder
            application for forwarding SNMP messages.
            
            Entries in the snmpProxyTable are created and deleted
            using the snmpProxyRowStatus object.
            
            .. attribute:: snmpproxyname  <key>
            
            	The locally arbitrary, but unique identifier associated with this snmpProxyEntry
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmpproxycontextengineid
            
            	The contextEngineID contained in messages that may be forwarded using the translation parameters defined by this entry
            	**type**\:  str
            
            	**length:** 5..32
            
            .. attribute:: snmpproxycontextname
            
            	The contextName contained in messages that may be forwarded using the translation parameters defined by this entry.  This object is optional, and if not supported, the contextName contained in a message is ignored when selecting an entry in the snmpProxyTable
            	**type**\:  str
            
            .. attribute:: snmpproxymultipletargetout
            
            	This object selects a set of management targets defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  This object is only used when selection of multiple targets is required (i.e. when forwarding an incoming notification)
            	**type**\:  str
            
            .. attribute:: snmpproxyrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  The following objects may not be modified while the value of this object is active(1)\:     \- snmpProxyType     \- snmpProxyContextEngineID     \- snmpProxyContextName     \- snmpProxyTargetParamsIn     \- snmpProxySingleTargetOut     \- snmpProxyMultipleTargetOut
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: snmpproxysingletargetout
            
            	This object selects a management target defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  The selected target is defined by an entry in the snmpTargetAddrTable whose index value (snmpTargetAddrName) is equal to this object.  This object is only used when selection of a single target is required (i.e. when forwarding an incoming read or write request)
            	**type**\:  str
            
            .. attribute:: snmpproxystoragetype
            
            	The storage type of this conceptual row. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: snmpproxytargetparamsin
            
            	This object selects an entry in the snmpTargetParamsTable. The selected entry is used to determine which row of the snmpProxyTable to use for forwarding received messages
            	**type**\:  str
            
            .. attribute:: snmpproxytype
            
            	The type of message that may be forwarded using the translation parameters defined by this entry
            	**type**\:   :py:class:`Snmpproxytype <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SnmpProxyMib.Snmpproxytable.Snmpproxyentry.Snmpproxytype>`
            
            

            """

            _prefix = 'SNMP-PROXY-MIB'
            _revision = '2002-10-14'

            def __init__(self):
                super(SnmpProxyMib.Snmpproxytable.Snmpproxyentry, self).__init__()

                self.yang_name = "snmpProxyEntry"
                self.yang_parent_name = "snmpProxyTable"

                self.snmpproxyname = YLeaf(YType.str, "snmpProxyName")

                self.snmpproxycontextengineid = YLeaf(YType.str, "snmpProxyContextEngineID")

                self.snmpproxycontextname = YLeaf(YType.str, "snmpProxyContextName")

                self.snmpproxymultipletargetout = YLeaf(YType.str, "snmpProxyMultipleTargetOut")

                self.snmpproxyrowstatus = YLeaf(YType.enumeration, "snmpProxyRowStatus")

                self.snmpproxysingletargetout = YLeaf(YType.str, "snmpProxySingleTargetOut")

                self.snmpproxystoragetype = YLeaf(YType.enumeration, "snmpProxyStorageType")

                self.snmpproxytargetparamsin = YLeaf(YType.str, "snmpProxyTargetParamsIn")

                self.snmpproxytype = YLeaf(YType.enumeration, "snmpProxyType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("snmpproxyname",
                                "snmpproxycontextengineid",
                                "snmpproxycontextname",
                                "snmpproxymultipletargetout",
                                "snmpproxyrowstatus",
                                "snmpproxysingletargetout",
                                "snmpproxystoragetype",
                                "snmpproxytargetparamsin",
                                "snmpproxytype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SnmpProxyMib.Snmpproxytable.Snmpproxyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SnmpProxyMib.Snmpproxytable.Snmpproxyentry, self).__setattr__(name, value)

            class Snmpproxytype(Enum):
                """
                Snmpproxytype

                The type of message that may be forwarded using

                the translation parameters defined by this entry.

                .. data:: read = 1

                .. data:: write = 2

                .. data:: trap = 3

                .. data:: inform = 4

                """

                read = Enum.YLeaf(1, "read")

                write = Enum.YLeaf(2, "write")

                trap = Enum.YLeaf(3, "trap")

                inform = Enum.YLeaf(4, "inform")


            def has_data(self):
                return (
                    self.snmpproxyname.is_set or
                    self.snmpproxycontextengineid.is_set or
                    self.snmpproxycontextname.is_set or
                    self.snmpproxymultipletargetout.is_set or
                    self.snmpproxyrowstatus.is_set or
                    self.snmpproxysingletargetout.is_set or
                    self.snmpproxystoragetype.is_set or
                    self.snmpproxytargetparamsin.is_set or
                    self.snmpproxytype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.snmpproxyname.yfilter != YFilter.not_set or
                    self.snmpproxycontextengineid.yfilter != YFilter.not_set or
                    self.snmpproxycontextname.yfilter != YFilter.not_set or
                    self.snmpproxymultipletargetout.yfilter != YFilter.not_set or
                    self.snmpproxyrowstatus.yfilter != YFilter.not_set or
                    self.snmpproxysingletargetout.yfilter != YFilter.not_set or
                    self.snmpproxystoragetype.yfilter != YFilter.not_set or
                    self.snmpproxytargetparamsin.yfilter != YFilter.not_set or
                    self.snmpproxytype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpProxyEntry" + "[snmpProxyName='" + self.snmpproxyname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SNMP-PROXY-MIB:SNMP-PROXY-MIB/snmpProxyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.snmpproxyname.is_set or self.snmpproxyname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxyname.get_name_leafdata())
                if (self.snmpproxycontextengineid.is_set or self.snmpproxycontextengineid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxycontextengineid.get_name_leafdata())
                if (self.snmpproxycontextname.is_set or self.snmpproxycontextname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxycontextname.get_name_leafdata())
                if (self.snmpproxymultipletargetout.is_set or self.snmpproxymultipletargetout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxymultipletargetout.get_name_leafdata())
                if (self.snmpproxyrowstatus.is_set or self.snmpproxyrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxyrowstatus.get_name_leafdata())
                if (self.snmpproxysingletargetout.is_set or self.snmpproxysingletargetout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxysingletargetout.get_name_leafdata())
                if (self.snmpproxystoragetype.is_set or self.snmpproxystoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxystoragetype.get_name_leafdata())
                if (self.snmpproxytargetparamsin.is_set or self.snmpproxytargetparamsin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxytargetparamsin.get_name_leafdata())
                if (self.snmpproxytype.is_set or self.snmpproxytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmpproxytype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "snmpProxyName" or name == "snmpProxyContextEngineID" or name == "snmpProxyContextName" or name == "snmpProxyMultipleTargetOut" or name == "snmpProxyRowStatus" or name == "snmpProxySingleTargetOut" or name == "snmpProxyStorageType" or name == "snmpProxyTargetParamsIn" or name == "snmpProxyType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "snmpProxyName"):
                    self.snmpproxyname = value
                    self.snmpproxyname.value_namespace = name_space
                    self.snmpproxyname.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyContextEngineID"):
                    self.snmpproxycontextengineid = value
                    self.snmpproxycontextengineid.value_namespace = name_space
                    self.snmpproxycontextengineid.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyContextName"):
                    self.snmpproxycontextname = value
                    self.snmpproxycontextname.value_namespace = name_space
                    self.snmpproxycontextname.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyMultipleTargetOut"):
                    self.snmpproxymultipletargetout = value
                    self.snmpproxymultipletargetout.value_namespace = name_space
                    self.snmpproxymultipletargetout.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyRowStatus"):
                    self.snmpproxyrowstatus = value
                    self.snmpproxyrowstatus.value_namespace = name_space
                    self.snmpproxyrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxySingleTargetOut"):
                    self.snmpproxysingletargetout = value
                    self.snmpproxysingletargetout.value_namespace = name_space
                    self.snmpproxysingletargetout.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyStorageType"):
                    self.snmpproxystoragetype = value
                    self.snmpproxystoragetype.value_namespace = name_space
                    self.snmpproxystoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyTargetParamsIn"):
                    self.snmpproxytargetparamsin = value
                    self.snmpproxytargetparamsin.value_namespace = name_space
                    self.snmpproxytargetparamsin.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpProxyType"):
                    self.snmpproxytype = value
                    self.snmpproxytype.value_namespace = name_space
                    self.snmpproxytype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.snmpproxyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.snmpproxyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpProxyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMP-PROXY-MIB:SNMP-PROXY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "snmpProxyEntry"):
                for c in self.snmpproxyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SnmpProxyMib.Snmpproxytable.Snmpproxyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.snmpproxyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpProxyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.snmpproxytable is not None and self.snmpproxytable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.snmpproxytable is not None and self.snmpproxytable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "SNMP-PROXY-MIB:SNMP-PROXY-MIB" + path_buffer

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

        if (child_yang_name == "snmpProxyTable"):
            if (self.snmpproxytable is None):
                self.snmpproxytable = SnmpProxyMib.Snmpproxytable()
                self.snmpproxytable.parent = self
                self._children_name_map["snmpproxytable"] = "snmpProxyTable"
            return self.snmpproxytable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "snmpProxyTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SnmpProxyMib()
        return self._top_entity


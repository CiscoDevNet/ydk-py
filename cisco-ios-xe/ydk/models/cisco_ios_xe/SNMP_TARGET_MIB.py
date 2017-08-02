""" SNMP_TARGET_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters used
by an SNMP entity for the generation of SNMP messages.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SnmpTargetMib(Entity):
    """
    
    
    .. attribute:: snmptargetaddrtable
    
    	A table of transport addresses to be used in the generation of SNMP messages
    	**type**\:   :py:class:`Snmptargetaddrtable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetaddrtable>`
    
    .. attribute:: snmptargetobjects
    
    	
    	**type**\:   :py:class:`Snmptargetobjects <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetobjects>`
    
    .. attribute:: snmptargetparamstable
    
    	A table of SNMP target information to be used in the generation of SNMP messages
    	**type**\:   :py:class:`Snmptargetparamstable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetparamstable>`
    
    

    """

    _prefix = 'SNMP-TARGET-MIB'
    _revision = '1998-08-04'

    def __init__(self):
        super(SnmpTargetMib, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-TARGET-MIB"
        self.yang_parent_name = "SNMP-TARGET-MIB"

        self.snmptargetaddrtable = SnmpTargetMib.Snmptargetaddrtable()
        self.snmptargetaddrtable.parent = self
        self._children_name_map["snmptargetaddrtable"] = "snmpTargetAddrTable"
        self._children_yang_names.add("snmpTargetAddrTable")

        self.snmptargetobjects = SnmpTargetMib.Snmptargetobjects()
        self.snmptargetobjects.parent = self
        self._children_name_map["snmptargetobjects"] = "snmpTargetObjects"
        self._children_yang_names.add("snmpTargetObjects")

        self.snmptargetparamstable = SnmpTargetMib.Snmptargetparamstable()
        self.snmptargetparamstable.parent = self
        self._children_name_map["snmptargetparamstable"] = "snmpTargetParamsTable"
        self._children_yang_names.add("snmpTargetParamsTable")


    class Snmptargetobjects(Entity):
        """
        
        
        .. attribute:: snmptargetspinlock
        
        	This object is used to facilitate modification of table entries in the SNMP\-TARGET\-MIB module by multiple      managers.  In particular, it is useful when modifying the value of the snmpTargetAddrTagList object.  The procedure for modifying the snmpTargetAddrTagList object is as follows\:      1.  Retrieve the value of snmpTargetSpinLock and         of snmpTargetAddrTagList.      2.  Generate a new value for snmpTargetAddrTagList.      3.  Set the value of snmpTargetSpinLock to the         retrieved value, and the value of         snmpTargetAddrTagList to the new value.  If         the set fails for the snmpTargetSpinLock         object, go back to step 1
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: snmpunavailablecontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unavailable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknowncontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unknown
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SnmpTargetMib.Snmptargetobjects, self).__init__()

            self.yang_name = "snmpTargetObjects"
            self.yang_parent_name = "SNMP-TARGET-MIB"

            self.snmptargetspinlock = YLeaf(YType.int32, "snmpTargetSpinLock")

            self.snmpunavailablecontexts = YLeaf(YType.uint32, "snmpUnavailableContexts")

            self.snmpunknowncontexts = YLeaf(YType.uint32, "snmpUnknownContexts")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("snmptargetspinlock",
                            "snmpunavailablecontexts",
                            "snmpunknowncontexts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SnmpTargetMib.Snmptargetobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SnmpTargetMib.Snmptargetobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.snmptargetspinlock.is_set or
                self.snmpunavailablecontexts.is_set or
                self.snmpunknowncontexts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.snmptargetspinlock.yfilter != YFilter.not_set or
                self.snmpunavailablecontexts.yfilter != YFilter.not_set or
                self.snmpunknowncontexts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpTargetObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.snmptargetspinlock.is_set or self.snmptargetspinlock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmptargetspinlock.get_name_leafdata())
            if (self.snmpunavailablecontexts.is_set or self.snmpunavailablecontexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpunavailablecontexts.get_name_leafdata())
            if (self.snmpunknowncontexts.is_set or self.snmpunknowncontexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpunknowncontexts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpTargetSpinLock" or name == "snmpUnavailableContexts" or name == "snmpUnknownContexts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "snmpTargetSpinLock"):
                self.snmptargetspinlock = value
                self.snmptargetspinlock.value_namespace = name_space
                self.snmptargetspinlock.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpUnavailableContexts"):
                self.snmpunavailablecontexts = value
                self.snmpunavailablecontexts.value_namespace = name_space
                self.snmpunavailablecontexts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpUnknownContexts"):
                self.snmpunknowncontexts = value
                self.snmpunknowncontexts.value_namespace = name_space
                self.snmpunknowncontexts.value_namespace_prefix = name_space_prefix


    class Snmptargetaddrtable(Entity):
        """
        A table of transport addresses to be used in the generation
        of SNMP messages.
        
        .. attribute:: snmptargetaddrentry
        
        	A transport address to be used in the generation of SNMP operations.  Entries in the snmpTargetAddrTable are created and deleted using the snmpTargetAddrRowStatus object
        	**type**\: list of    :py:class:`Snmptargetaddrentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SnmpTargetMib.Snmptargetaddrtable, self).__init__()

            self.yang_name = "snmpTargetAddrTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"

            self.snmptargetaddrentry = YList(self)

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
                        super(SnmpTargetMib.Snmptargetaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SnmpTargetMib.Snmptargetaddrtable, self).__setattr__(name, value)


        class Snmptargetaddrentry(Entity):
            """
            A transport address to be used in the generation
            of SNMP operations.
            
            Entries in the snmpTargetAddrTable are created and
            deleted using the snmpTargetAddrRowStatus object.
            
            .. attribute:: snmptargetaddrname  <key>
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetAddrEntry
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrparams
            
            	The value of this object identifies an entry in the snmpTargetParamsTable.  The identified entry contains SNMP parameters to be used when generating messages to be sent to this transport address
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrretrycount
            
            	This object specifies a default number of retries to be attempted when a response is not received for a generated message.  An application may provide its own retry count, in which case the value of this object is ignored
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: snmptargetaddrrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetAddrRowStatus column is 'notReady'.  In particular, a newly created row cannot be made active until the corresponding instances of snmpTargetAddrTDomain, snmpTargetAddrTAddress, and snmpTargetAddrParams have all been set.  The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetAddrTDomain     \- snmpTargetAddrTAddress An attempt to set these objects while the value of snmpTargetAddrRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: snmptargetaddrstoragetype
            
            	The storage type for this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: snmptargetaddrtaddress
            
            	This object contains a transport address.  The format of this address depends on the value of the snmpTargetAddrTDomain object
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: snmptargetaddrtaglist
            
            	This object contains a list of tag values which are used to select target addresses for a particular operation
            	**type**\:  str
            
            .. attribute:: snmptargetaddrtdomain
            
            	This object indicates the transport type of the address contained in the snmpTargetAddrTAddress object
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmptargetaddrtimeout
            
            	This object should reflect the expected maximum round trip time for communicating with the transport address defined by this row.  When a message is sent to this address, and a response (if one is expected) is not received within this time period, an implementation may assume that the response will not be delivered.  Note that the time interval that an application waits for a response may actually be derived from the value of this object.  The method for deriving the actual time interval is implementation dependent.  One such method      is to derive the expected round trip time based on a particular retransmission algorithm and on the number of timeouts which have occurred.  The type of message may also be considered when deriving expected round trip times for retransmissions.  For example, if a message is being sent with a securityLevel that indicates both authentication and privacy, the derived value may be increased to compensate for extra processing time spent during authentication and encryption processing
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                super(SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry, self).__init__()

                self.yang_name = "snmpTargetAddrEntry"
                self.yang_parent_name = "snmpTargetAddrTable"

                self.snmptargetaddrname = YLeaf(YType.str, "snmpTargetAddrName")

                self.snmptargetaddrparams = YLeaf(YType.str, "snmpTargetAddrParams")

                self.snmptargetaddrretrycount = YLeaf(YType.int32, "snmpTargetAddrRetryCount")

                self.snmptargetaddrrowstatus = YLeaf(YType.enumeration, "snmpTargetAddrRowStatus")

                self.snmptargetaddrstoragetype = YLeaf(YType.enumeration, "snmpTargetAddrStorageType")

                self.snmptargetaddrtaddress = YLeaf(YType.str, "snmpTargetAddrTAddress")

                self.snmptargetaddrtaglist = YLeaf(YType.str, "snmpTargetAddrTagList")

                self.snmptargetaddrtdomain = YLeaf(YType.str, "snmpTargetAddrTDomain")

                self.snmptargetaddrtimeout = YLeaf(YType.int32, "snmpTargetAddrTimeout")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("snmptargetaddrname",
                                "snmptargetaddrparams",
                                "snmptargetaddrretrycount",
                                "snmptargetaddrrowstatus",
                                "snmptargetaddrstoragetype",
                                "snmptargetaddrtaddress",
                                "snmptargetaddrtaglist",
                                "snmptargetaddrtdomain",
                                "snmptargetaddrtimeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.snmptargetaddrname.is_set or
                    self.snmptargetaddrparams.is_set or
                    self.snmptargetaddrretrycount.is_set or
                    self.snmptargetaddrrowstatus.is_set or
                    self.snmptargetaddrstoragetype.is_set or
                    self.snmptargetaddrtaddress.is_set or
                    self.snmptargetaddrtaglist.is_set or
                    self.snmptargetaddrtdomain.is_set or
                    self.snmptargetaddrtimeout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.snmptargetaddrname.yfilter != YFilter.not_set or
                    self.snmptargetaddrparams.yfilter != YFilter.not_set or
                    self.snmptargetaddrretrycount.yfilter != YFilter.not_set or
                    self.snmptargetaddrrowstatus.yfilter != YFilter.not_set or
                    self.snmptargetaddrstoragetype.yfilter != YFilter.not_set or
                    self.snmptargetaddrtaddress.yfilter != YFilter.not_set or
                    self.snmptargetaddrtaglist.yfilter != YFilter.not_set or
                    self.snmptargetaddrtdomain.yfilter != YFilter.not_set or
                    self.snmptargetaddrtimeout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpTargetAddrEntry" + "[snmpTargetAddrName='" + self.snmptargetaddrname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.snmptargetaddrname.is_set or self.snmptargetaddrname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrname.get_name_leafdata())
                if (self.snmptargetaddrparams.is_set or self.snmptargetaddrparams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrparams.get_name_leafdata())
                if (self.snmptargetaddrretrycount.is_set or self.snmptargetaddrretrycount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrretrycount.get_name_leafdata())
                if (self.snmptargetaddrrowstatus.is_set or self.snmptargetaddrrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrrowstatus.get_name_leafdata())
                if (self.snmptargetaddrstoragetype.is_set or self.snmptargetaddrstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrstoragetype.get_name_leafdata())
                if (self.snmptargetaddrtaddress.is_set or self.snmptargetaddrtaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrtaddress.get_name_leafdata())
                if (self.snmptargetaddrtaglist.is_set or self.snmptargetaddrtaglist.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrtaglist.get_name_leafdata())
                if (self.snmptargetaddrtdomain.is_set or self.snmptargetaddrtdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrtdomain.get_name_leafdata())
                if (self.snmptargetaddrtimeout.is_set or self.snmptargetaddrtimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetaddrtimeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "snmpTargetAddrName" or name == "snmpTargetAddrParams" or name == "snmpTargetAddrRetryCount" or name == "snmpTargetAddrRowStatus" or name == "snmpTargetAddrStorageType" or name == "snmpTargetAddrTAddress" or name == "snmpTargetAddrTagList" or name == "snmpTargetAddrTDomain" or name == "snmpTargetAddrTimeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "snmpTargetAddrName"):
                    self.snmptargetaddrname = value
                    self.snmptargetaddrname.value_namespace = name_space
                    self.snmptargetaddrname.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrParams"):
                    self.snmptargetaddrparams = value
                    self.snmptargetaddrparams.value_namespace = name_space
                    self.snmptargetaddrparams.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrRetryCount"):
                    self.snmptargetaddrretrycount = value
                    self.snmptargetaddrretrycount.value_namespace = name_space
                    self.snmptargetaddrretrycount.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrRowStatus"):
                    self.snmptargetaddrrowstatus = value
                    self.snmptargetaddrrowstatus.value_namespace = name_space
                    self.snmptargetaddrrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrStorageType"):
                    self.snmptargetaddrstoragetype = value
                    self.snmptargetaddrstoragetype.value_namespace = name_space
                    self.snmptargetaddrstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrTAddress"):
                    self.snmptargetaddrtaddress = value
                    self.snmptargetaddrtaddress.value_namespace = name_space
                    self.snmptargetaddrtaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrTagList"):
                    self.snmptargetaddrtaglist = value
                    self.snmptargetaddrtaglist.value_namespace = name_space
                    self.snmptargetaddrtaglist.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrTDomain"):
                    self.snmptargetaddrtdomain = value
                    self.snmptargetaddrtdomain.value_namespace = name_space
                    self.snmptargetaddrtdomain.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetAddrTimeout"):
                    self.snmptargetaddrtimeout = value
                    self.snmptargetaddrtimeout.value_namespace = name_space
                    self.snmptargetaddrtimeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.snmptargetaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.snmptargetaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpTargetAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "snmpTargetAddrEntry"):
                for c in self.snmptargetaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SnmpTargetMib.Snmptargetaddrtable.Snmptargetaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.snmptargetaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpTargetAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Snmptargetparamstable(Entity):
        """
        A table of SNMP target information to be used
        in the generation of SNMP messages.
        
        .. attribute:: snmptargetparamsentry
        
        	A set of SNMP target information.  Entries in the snmpTargetParamsTable are created and deleted using the snmpTargetParamsRowStatus object
        	**type**\: list of    :py:class:`Snmptargetparamsentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SnmpTargetMib.Snmptargetparamstable, self).__init__()

            self.yang_name = "snmpTargetParamsTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"

            self.snmptargetparamsentry = YList(self)

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
                        super(SnmpTargetMib.Snmptargetparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SnmpTargetMib.Snmptargetparamstable, self).__setattr__(name, value)


        class Snmptargetparamsentry(Entity):
            """
            A set of SNMP target information.
            
            Entries in the snmpTargetParamsTable are created and
            deleted using the snmpTargetParamsRowStatus object.
            
            .. attribute:: snmptargetparamsname  <key>
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetParamsEntry
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetparamsmpmodel
            
            	The Message Processing Model to be used when generating SNMP messages using this entry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetparamsrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetParamsRowStatus column is 'notReady'.  In particular, a newly created row cannot be made      active until the corresponding snmpTargetParamsMPModel, snmpTargetParamsSecurityModel, snmpTargetParamsSecurityName, and snmpTargetParamsSecurityLevel have all been set. The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetParamsMPModel     \- snmpTargetParamsSecurityModel     \- snmpTargetParamsSecurityName     \- snmpTargetParamsSecurityLevel An attempt to set these objects while the value of snmpTargetParamsRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: snmptargetparamssecuritylevel
            
            	The Level of Security to be used when generating SNMP messages using this entry
            	**type**\:   :py:class:`Snmpsecuritylevel <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.Snmpsecuritylevel>`
            
            .. attribute:: snmptargetparamssecuritymodel
            
            	The Security Model to be used when generating SNMP messages using this entry.  An implementation may choose to return an inconsistentValue error if an attempt is made to set this variable to a value for a security model which the implementation does      not support
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: snmptargetparamssecurityname
            
            	The securityName which identifies the Principal on whose behalf SNMP messages will be generated using this entry
            	**type**\:  str
            
            .. attribute:: snmptargetparamsstoragetype
            
            	The storage type for this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                super(SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry, self).__init__()

                self.yang_name = "snmpTargetParamsEntry"
                self.yang_parent_name = "snmpTargetParamsTable"

                self.snmptargetparamsname = YLeaf(YType.str, "snmpTargetParamsName")

                self.snmptargetparamsmpmodel = YLeaf(YType.int32, "snmpTargetParamsMPModel")

                self.snmptargetparamsrowstatus = YLeaf(YType.enumeration, "snmpTargetParamsRowStatus")

                self.snmptargetparamssecuritylevel = YLeaf(YType.enumeration, "snmpTargetParamsSecurityLevel")

                self.snmptargetparamssecuritymodel = YLeaf(YType.int32, "snmpTargetParamsSecurityModel")

                self.snmptargetparamssecurityname = YLeaf(YType.str, "snmpTargetParamsSecurityName")

                self.snmptargetparamsstoragetype = YLeaf(YType.enumeration, "snmpTargetParamsStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("snmptargetparamsname",
                                "snmptargetparamsmpmodel",
                                "snmptargetparamsrowstatus",
                                "snmptargetparamssecuritylevel",
                                "snmptargetparamssecuritymodel",
                                "snmptargetparamssecurityname",
                                "snmptargetparamsstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.snmptargetparamsname.is_set or
                    self.snmptargetparamsmpmodel.is_set or
                    self.snmptargetparamsrowstatus.is_set or
                    self.snmptargetparamssecuritylevel.is_set or
                    self.snmptargetparamssecuritymodel.is_set or
                    self.snmptargetparamssecurityname.is_set or
                    self.snmptargetparamsstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.snmptargetparamsname.yfilter != YFilter.not_set or
                    self.snmptargetparamsmpmodel.yfilter != YFilter.not_set or
                    self.snmptargetparamsrowstatus.yfilter != YFilter.not_set or
                    self.snmptargetparamssecuritylevel.yfilter != YFilter.not_set or
                    self.snmptargetparamssecuritymodel.yfilter != YFilter.not_set or
                    self.snmptargetparamssecurityname.yfilter != YFilter.not_set or
                    self.snmptargetparamsstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmpTargetParamsEntry" + "[snmpTargetParamsName='" + self.snmptargetparamsname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.snmptargetparamsname.is_set or self.snmptargetparamsname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamsname.get_name_leafdata())
                if (self.snmptargetparamsmpmodel.is_set or self.snmptargetparamsmpmodel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamsmpmodel.get_name_leafdata())
                if (self.snmptargetparamsrowstatus.is_set or self.snmptargetparamsrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamsrowstatus.get_name_leafdata())
                if (self.snmptargetparamssecuritylevel.is_set or self.snmptargetparamssecuritylevel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamssecuritylevel.get_name_leafdata())
                if (self.snmptargetparamssecuritymodel.is_set or self.snmptargetparamssecuritymodel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamssecuritymodel.get_name_leafdata())
                if (self.snmptargetparamssecurityname.is_set or self.snmptargetparamssecurityname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamssecurityname.get_name_leafdata())
                if (self.snmptargetparamsstoragetype.is_set or self.snmptargetparamsstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.snmptargetparamsstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "snmpTargetParamsName" or name == "snmpTargetParamsMPModel" or name == "snmpTargetParamsRowStatus" or name == "snmpTargetParamsSecurityLevel" or name == "snmpTargetParamsSecurityModel" or name == "snmpTargetParamsSecurityName" or name == "snmpTargetParamsStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "snmpTargetParamsName"):
                    self.snmptargetparamsname = value
                    self.snmptargetparamsname.value_namespace = name_space
                    self.snmptargetparamsname.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsMPModel"):
                    self.snmptargetparamsmpmodel = value
                    self.snmptargetparamsmpmodel.value_namespace = name_space
                    self.snmptargetparamsmpmodel.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsRowStatus"):
                    self.snmptargetparamsrowstatus = value
                    self.snmptargetparamsrowstatus.value_namespace = name_space
                    self.snmptargetparamsrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsSecurityLevel"):
                    self.snmptargetparamssecuritylevel = value
                    self.snmptargetparamssecuritylevel.value_namespace = name_space
                    self.snmptargetparamssecuritylevel.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsSecurityModel"):
                    self.snmptargetparamssecuritymodel = value
                    self.snmptargetparamssecuritymodel.value_namespace = name_space
                    self.snmptargetparamssecuritymodel.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsSecurityName"):
                    self.snmptargetparamssecurityname = value
                    self.snmptargetparamssecurityname.value_namespace = name_space
                    self.snmptargetparamssecurityname.value_namespace_prefix = name_space_prefix
                if(value_path == "snmpTargetParamsStorageType"):
                    self.snmptargetparamsstoragetype = value
                    self.snmptargetparamsstoragetype.value_namespace = name_space
                    self.snmptargetparamsstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.snmptargetparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.snmptargetparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpTargetParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "snmpTargetParamsEntry"):
                for c in self.snmptargetparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SnmpTargetMib.Snmptargetparamstable.Snmptargetparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.snmptargetparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpTargetParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.snmptargetaddrtable is not None and self.snmptargetaddrtable.has_data()) or
            (self.snmptargetobjects is not None and self.snmptargetobjects.has_data()) or
            (self.snmptargetparamstable is not None and self.snmptargetparamstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.snmptargetaddrtable is not None and self.snmptargetaddrtable.has_operation()) or
            (self.snmptargetobjects is not None and self.snmptargetobjects.has_operation()) or
            (self.snmptargetparamstable is not None and self.snmptargetparamstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "SNMP-TARGET-MIB:SNMP-TARGET-MIB" + path_buffer

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

        if (child_yang_name == "snmpTargetAddrTable"):
            if (self.snmptargetaddrtable is None):
                self.snmptargetaddrtable = SnmpTargetMib.Snmptargetaddrtable()
                self.snmptargetaddrtable.parent = self
                self._children_name_map["snmptargetaddrtable"] = "snmpTargetAddrTable"
            return self.snmptargetaddrtable

        if (child_yang_name == "snmpTargetObjects"):
            if (self.snmptargetobjects is None):
                self.snmptargetobjects = SnmpTargetMib.Snmptargetobjects()
                self.snmptargetobjects.parent = self
                self._children_name_map["snmptargetobjects"] = "snmpTargetObjects"
            return self.snmptargetobjects

        if (child_yang_name == "snmpTargetParamsTable"):
            if (self.snmptargetparamstable is None):
                self.snmptargetparamstable = SnmpTargetMib.Snmptargetparamstable()
                self.snmptargetparamstable.parent = self
                self._children_name_map["snmptargetparamstable"] = "snmpTargetParamsTable"
            return self.snmptargetparamstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "snmpTargetAddrTable" or name == "snmpTargetObjects" or name == "snmpTargetParamsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SnmpTargetMib()
        return self._top_entity


""" EXPRESSION_MIB 

The MIB module for defining expressions of MIB objects
for network management purposes.

This MIB is an early snapshot of work done by the IETF's
Distributed Management working group.  After this snapshot
was taken, the MIB was modified, had new OIDs assigned,
and then published as RFC 2982.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ExpressionMib(Entity):
    """
    
    
    .. attribute:: expexpressiontable
    
    	A table of expression definitions
    	**type**\:   :py:class:`Expexpressiontable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expexpressiontable>`
    
    .. attribute:: expnames
    
    	
    	**type**\:   :py:class:`Expnames <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnames>`
    
    .. attribute:: expnametable
    
    	A table of expression names, for creating and deleting expressions
    	**type**\:   :py:class:`Expnametable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnametable>`
    
    .. attribute:: expobjecttable
    
    	A table of object definitions for each expExpression.  Wildcarding instance IDs\:  It is legal to omit all or part of the instance portion for some or all of the objects in an expression. (See the DESCRIPTION of expObjectID for details.  However, note that if more than one object in the same expression is wildcarded in this way, they all must be objects where that portion of the instance is the same.  In other words, all objects may be in the same SEQUENCE or in different SEQUENCEs but with the same semantic index value (e.g., a value of ifIndex) for the wildcarded portion
    	**type**\:   :py:class:`Expobjecttable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expobjecttable>`
    
    .. attribute:: expresource
    
    	
    	**type**\:   :py:class:`Expresource <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expresource>`
    
    .. attribute:: expvaluetable
    
    	A table of values from evaluated expressions
    	**type**\:   :py:class:`Expvaluetable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expvaluetable>`
    
    

    """

    _prefix = 'EXPRESSION-MIB'
    _revision = '2005-11-24'

    def __init__(self):
        super(ExpressionMib, self).__init__()
        self._top_entity = None

        self.yang_name = "EXPRESSION-MIB"
        self.yang_parent_name = "EXPRESSION-MIB"

        self.expexpressiontable = ExpressionMib.Expexpressiontable()
        self.expexpressiontable.parent = self
        self._children_name_map["expexpressiontable"] = "expExpressionTable"
        self._children_yang_names.add("expExpressionTable")

        self.expnames = ExpressionMib.Expnames()
        self.expnames.parent = self
        self._children_name_map["expnames"] = "expNames"
        self._children_yang_names.add("expNames")

        self.expnametable = ExpressionMib.Expnametable()
        self.expnametable.parent = self
        self._children_name_map["expnametable"] = "expNameTable"
        self._children_yang_names.add("expNameTable")

        self.expobjecttable = ExpressionMib.Expobjecttable()
        self.expobjecttable.parent = self
        self._children_name_map["expobjecttable"] = "expObjectTable"
        self._children_yang_names.add("expObjectTable")

        self.expresource = ExpressionMib.Expresource()
        self.expresource.parent = self
        self._children_name_map["expresource"] = "expResource"
        self._children_yang_names.add("expResource")

        self.expvaluetable = ExpressionMib.Expvaluetable()
        self.expvaluetable.parent = self
        self._children_name_map["expvaluetable"] = "expValueTable"
        self._children_yang_names.add("expValueTable")


    class Expresource(Entity):
        """
        
        
        .. attribute:: expresourcedeltaminimum
        
        	The minimum expExpressionDeltaInterval this system will accept.  A system may use the larger values of this minimum to lessen the impact of constantly computing deltas.  The value \-1 indicates this system will not accept deltaValue as a value for expObjectSampleType.  Unless explicitly resource limited, a system's value for this object should be 1.  Changing this value will not invalidate an existing setting of expObjectSampleType
        	**type**\:  int
        
        	**range:** \-1..None \| 1..600
        
        	**units**\: seconds
        
        .. attribute:: expresourcedeltawildcardinstancemaximum
        
        	The maximum number of dynamic instance entries this system will support for wildcarded delta objects in expressions. These are the entries that maintain state, one for each instance of each deltaValue object for each value of an expression.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object should be 0.  Changing this value will not eliminate or inhibit existing delta wildcard instance objects but will prevent the creation of more such objects
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceresourcelacks
        
        	The number of times this system could not evaluate an expression because that would have created a value instance in excess of expResourceDeltaWildcardInstanceMaximum
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstances
        
        	The number of currently active instance entries as defined for expResourceDeltaWildcardInstanceMaximum
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceshigh
        
        	The highest value of expResourceDeltaWildcardInstances that has occurred since initialization of the management system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expresource, self).__init__()

            self.yang_name = "expResource"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expresourcedeltaminimum = YLeaf(YType.int32, "expResourceDeltaMinimum")

            self.expresourcedeltawildcardinstancemaximum = YLeaf(YType.uint32, "expResourceDeltaWildcardInstanceMaximum")

            self.expresourcedeltawildcardinstanceresourcelacks = YLeaf(YType.uint32, "expResourceDeltaWildcardInstanceResourceLacks")

            self.expresourcedeltawildcardinstances = YLeaf(YType.uint32, "expResourceDeltaWildcardInstances")

            self.expresourcedeltawildcardinstanceshigh = YLeaf(YType.uint32, "expResourceDeltaWildcardInstancesHigh")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("expresourcedeltaminimum",
                            "expresourcedeltawildcardinstancemaximum",
                            "expresourcedeltawildcardinstanceresourcelacks",
                            "expresourcedeltawildcardinstances",
                            "expresourcedeltawildcardinstanceshigh") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ExpressionMib.Expresource, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expresource, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.expresourcedeltaminimum.is_set or
                self.expresourcedeltawildcardinstancemaximum.is_set or
                self.expresourcedeltawildcardinstanceresourcelacks.is_set or
                self.expresourcedeltawildcardinstances.is_set or
                self.expresourcedeltawildcardinstanceshigh.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.expresourcedeltaminimum.yfilter != YFilter.not_set or
                self.expresourcedeltawildcardinstancemaximum.yfilter != YFilter.not_set or
                self.expresourcedeltawildcardinstanceresourcelacks.yfilter != YFilter.not_set or
                self.expresourcedeltawildcardinstances.yfilter != YFilter.not_set or
                self.expresourcedeltawildcardinstanceshigh.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expResource" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.expresourcedeltaminimum.is_set or self.expresourcedeltaminimum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expresourcedeltaminimum.get_name_leafdata())
            if (self.expresourcedeltawildcardinstancemaximum.is_set or self.expresourcedeltawildcardinstancemaximum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expresourcedeltawildcardinstancemaximum.get_name_leafdata())
            if (self.expresourcedeltawildcardinstanceresourcelacks.is_set or self.expresourcedeltawildcardinstanceresourcelacks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expresourcedeltawildcardinstanceresourcelacks.get_name_leafdata())
            if (self.expresourcedeltawildcardinstances.is_set or self.expresourcedeltawildcardinstances.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expresourcedeltawildcardinstances.get_name_leafdata())
            if (self.expresourcedeltawildcardinstanceshigh.is_set or self.expresourcedeltawildcardinstanceshigh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expresourcedeltawildcardinstanceshigh.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expResourceDeltaMinimum" or name == "expResourceDeltaWildcardInstanceMaximum" or name == "expResourceDeltaWildcardInstanceResourceLacks" or name == "expResourceDeltaWildcardInstances" or name == "expResourceDeltaWildcardInstancesHigh"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "expResourceDeltaMinimum"):
                self.expresourcedeltaminimum = value
                self.expresourcedeltaminimum.value_namespace = name_space
                self.expresourcedeltaminimum.value_namespace_prefix = name_space_prefix
            if(value_path == "expResourceDeltaWildcardInstanceMaximum"):
                self.expresourcedeltawildcardinstancemaximum = value
                self.expresourcedeltawildcardinstancemaximum.value_namespace = name_space
                self.expresourcedeltawildcardinstancemaximum.value_namespace_prefix = name_space_prefix
            if(value_path == "expResourceDeltaWildcardInstanceResourceLacks"):
                self.expresourcedeltawildcardinstanceresourcelacks = value
                self.expresourcedeltawildcardinstanceresourcelacks.value_namespace = name_space
                self.expresourcedeltawildcardinstanceresourcelacks.value_namespace_prefix = name_space_prefix
            if(value_path == "expResourceDeltaWildcardInstances"):
                self.expresourcedeltawildcardinstances = value
                self.expresourcedeltawildcardinstances.value_namespace = name_space
                self.expresourcedeltawildcardinstances.value_namespace_prefix = name_space_prefix
            if(value_path == "expResourceDeltaWildcardInstancesHigh"):
                self.expresourcedeltawildcardinstanceshigh = value
                self.expresourcedeltawildcardinstanceshigh.value_namespace = name_space
                self.expresourcedeltawildcardinstanceshigh.value_namespace_prefix = name_space_prefix


    class Expnames(Entity):
        """
        
        
        .. attribute:: expnamehighestindex
        
        	The highest value of ExpressionIndex ever assigned on this system.  Preferrably this value is preserved across system reboots.  A managed system that is unable to store expressions across reboots need not preserve this value across reboots.  If all expression\-creating applications cooperate, they may use this to avoid reusing an ExpressionIndex.  To do so, attempt creation of a new entry with this value + 1 as the value of expExpressionIndex.  Although reusing ExpressionIndexes could lead to an application receiving a misunderstood value, it is a matter of local management policy whether to reuse them
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: expnamelastchange
        
        	The value of sysUpTime the last time an expression was created or deleted or had its name changed using expExpressionName
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expnames, self).__init__()

            self.yang_name = "expNames"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expnamehighestindex = YLeaf(YType.uint32, "expNameHighestIndex")

            self.expnamelastchange = YLeaf(YType.uint32, "expNameLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("expnamehighestindex",
                            "expnamelastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ExpressionMib.Expnames, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expnames, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.expnamehighestindex.is_set or
                self.expnamelastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.expnamehighestindex.yfilter != YFilter.not_set or
                self.expnamelastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expNames" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.expnamehighestindex.is_set or self.expnamehighestindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expnamehighestindex.get_name_leafdata())
            if (self.expnamelastchange.is_set or self.expnamelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.expnamelastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expNameHighestIndex" or name == "expNameLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "expNameHighestIndex"):
                self.expnamehighestindex = value
                self.expnamehighestindex.value_namespace = name_space
                self.expnamehighestindex.value_namespace_prefix = name_space_prefix
            if(value_path == "expNameLastChange"):
                self.expnamelastchange = value
                self.expnamelastchange.value_namespace = name_space
                self.expnamelastchange.value_namespace_prefix = name_space_prefix


    class Expnametable(Entity):
        """
        A table of expression names, for creating and deleting
        expressions.
        
        .. attribute:: expnameentry
        
        	Information about a single expression.  New expressions can be created using expNameStatus.  To create an expression first create the named entry in this table.  Then use expExpressionIndex to populate expExpressionTable and expObjectTable.  For expression evaluation to succeed all related entries in expNameTable, expExpressionTable, and expObjectTable must be 'active'.  If these conditions are not met the corresponding values in expValue simply are not instantiated.  Deleting an entry deletes all related entries in expExpressionTable and expObjectTable.  Because of the relationships among the multiple tables for an expression (expNameTable, expExpressionTable, expObjectTable, and expValueTable) and the SNMP rules for independence in setting object values, it is necessary to do final error checking when an expression is evaluated, that is, when one of its instances in expValueTable is read.  Earlier checking need not be done and an implementation may not impose any ordering on the creation of objects related to an expression other than to require values for expName and expExpressionIndex before any other related objects can be created.  To maintain security of MIB information, when creating a new row in this table, the managed system must record the security credentials of the requester.  If the subsequent expression includes objects with expObjectSampleType 'deltaValue' the evaluation of that expression takes place under the security credentials of the creator of its expNameEntry
        	**type**\: list of    :py:class:`Expnameentry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnametable.Expnameentry>`
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expnametable, self).__init__()

            self.yang_name = "expNameTable"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expnameentry = YList(self)

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
                        super(ExpressionMib.Expnametable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expnametable, self).__setattr__(name, value)


        class Expnameentry(Entity):
            """
            Information about a single expression.  New expressions
            can be created using expNameStatus.
            
            To create an expression first create the named entry in this
            table.  Then use expExpressionIndex to populate
            expExpressionTable and expObjectTable.  For expression
            evaluation to succeed all related entries in expNameTable,
            expExpressionTable, and expObjectTable must be 'active'.  If
            these conditions are not met the corresponding values in
            expValue simply are not instantiated.
            
            Deleting an entry deletes all related entries in
            expExpressionTable and expObjectTable.
            
            Because of the relationships among the multiple tables
            for an expression (expNameTable, expExpressionTable,
            expObjectTable, and expValueTable) and the SNMP rules
            for independence in setting object values, it is
            necessary to do final error checking when an expression
            is evaluated, that is, when one of its instances in
            expValueTable is read.  Earlier checking need not be
            done and an implementation may not impose any ordering
            on the creation of objects related to an expression other
            than to require values for expName and expExpressionIndex
            before any other related objects can be created.
            
            To maintain security of MIB information, when creating a new
            row in this table, the managed system must record the
            security credentials of the requester.  If the subsequent
            expression includes objects with expObjectSampleType
            'deltaValue' the evaluation of that expression takes place
            under the security credentials of the creator of its
            expNameEntry.
            
            .. attribute:: expname  <key>
            
            	The name of the expression.  Choosing names with useful lexical ordering supports using GetNext or GetBulk to retrieve a useful subset of the table
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: expexpressionindex
            
            	The numeric identification of the expression.  Applications may select this number in ascending numerical order by using expNameHighestIndex as a hint or may use any other acceptable, unused number.  Once set this value may not be set to a different value
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: expnamestatus
            
            	The control that allows creation/deletion of entries
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(ExpressionMib.Expnametable.Expnameentry, self).__init__()

                self.yang_name = "expNameEntry"
                self.yang_parent_name = "expNameTable"

                self.expname = YLeaf(YType.str, "expName")

                self.expexpressionindex = YLeaf(YType.uint32, "expExpressionIndex")

                self.expnamestatus = YLeaf(YType.enumeration, "expNameStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("expname",
                                "expexpressionindex",
                                "expnamestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExpressionMib.Expnametable.Expnameentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExpressionMib.Expnametable.Expnameentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.expname.is_set or
                    self.expexpressionindex.is_set or
                    self.expnamestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.expname.yfilter != YFilter.not_set or
                    self.expexpressionindex.yfilter != YFilter.not_set or
                    self.expnamestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "expNameEntry" + "[expName='" + self.expname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/expNameTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.expname.is_set or self.expname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expname.get_name_leafdata())
                if (self.expexpressionindex.is_set or self.expexpressionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionindex.get_name_leafdata())
                if (self.expnamestatus.is_set or self.expnamestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expnamestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "expName" or name == "expExpressionIndex" or name == "expNameStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "expName"):
                    self.expname = value
                    self.expname.value_namespace = name_space
                    self.expname.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionIndex"):
                    self.expexpressionindex = value
                    self.expexpressionindex.value_namespace = name_space
                    self.expexpressionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expNameStatus"):
                    self.expnamestatus = value
                    self.expnamestatus.value_namespace = name_space
                    self.expnamestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.expnameentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.expnameentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expNameTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "expNameEntry"):
                for c in self.expnameentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ExpressionMib.Expnametable.Expnameentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.expnameentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expNameEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Expexpressiontable(Entity):
        """
        A table of expression definitions.
        
        .. attribute:: expexpressionentry
        
        	Information about a single expression.  An entry appears in this table when an entry is created in expNameTable. Deleting that expNameTable entry automatically deletes this entry and its associated expObjectTable entries.  Values of read\-write objects in this table may be changed at any time
        	**type**\: list of    :py:class:`Expexpressionentry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expexpressiontable.Expexpressionentry>`
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expexpressiontable, self).__init__()

            self.yang_name = "expExpressionTable"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expexpressionentry = YList(self)

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
                        super(ExpressionMib.Expexpressiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expexpressiontable, self).__setattr__(name, value)


        class Expexpressionentry(Entity):
            """
            Information about a single expression.  An entry appears
            in this table when an entry is created in expNameTable.
            Deleting that expNameTable entry automatically deletes
            this entry and its associated expObjectTable entries.
            
            Values of read\-write objects in this table may be changed
            at any time.
            
            .. attribute:: expexpressionindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnametable.Expnameentry>`
            
            .. attribute:: expexpression
            
            	The expression to be evaluated.  This object is the same as a DisplayString (RFC 1903) except for its maximum length.  Except for the variable names the expression is in ANSI C syntax.  Only the subset of ANSI C operators and functions listed here is allowed.  Variables are expressed as a dollar sign ('$') and an integer that corresponds to an expObjectIndex.  An example of a valid expression is\:          ($1\-$5)\*100  Expressions may not be recursive, that is although an expression may use the results of another expression, it may not contain any variable that is directly or indirectly a result of its own evaluation.  The only allowed operators are\:          ( )         \- (unary)         + \- \* / %         & \| ^ << >> ~         ! && \|\| == != > >= < <=  Note the parentheses are included for parenthesizing the expression, not for casting data types.  The only constant types defined are\:          int (32\-bit signed)         long (64\-bit signed)         unsigned int         unsigned long         hexadecimal         character         string         oid  The default type for a positive integer is int unless it is too large in which case it is long.  All but oid are as defined for ANSI C.  Note that a hexadecimal constant may end up as a scalar or an array of 8\-bit integers.  A string constant is enclosed in double quotes and may contain back\-slashed individual characters as in ANSI C.  An oid constant comprises 32\-bit, unsigned integers and at least one period, for example\:          0.         .0         1.3.6.1  Integer\-typed objects are treated as 32\- or 64\-bit, signed or unsigned integers, as appropriate.  The results of mixing them are as for ANSI C, including the type of the result.  Note that a 32\-bit value is thus promoted to 64 bits only in an operation with a 64\-bit value.  There is no provision for larger values to handle overflow.  Relative to SNMP data types, a resulting value becomes unsigned when calculating it uses any unsigned value, including a counter.  To force the final value to be of data type counter the expression must explicitly use the counter32() or counter64() function (defined below).  OCTET STRINGS and OBJECT IDENTIFIERs are treated as 1\-based arrays of unsigned 8\-bit integers and unsigned 32\-bit integers, respectively.  IpAddresses are treated as 32\-bit, unsigned integers in network byte order, that is, the hex version of 255.0.0.0 is 0xff000000.  Conditional expressions result in a 32\-bit, unsigned integer of value 0 for false or 1 for true. When an arbitrary value is used as a boolean 0 is false and non\-zero is true.  Rules for the resulting data type from an operation, based on the operator\:  For << and >> the result is the same as the left hand operand.  For &&, \|\|, ==, !=, <, <=, >, and >= the result is always Unsigned32.  For unary \- the result is always Integer32.  For +, \-, \*, /, %, &, \|, and ^ the result is promoted according to the following rules, in order from most to least preferred\:          If left hand and right hand operands are the same         type, use that.          If either side is Counter64, use that.          If either side is IpAddress, use that.          If either side is TimeTicks, use that.          If either side is Counter32, use that.          Otherwise use Unsigned32.  The following rules say what operators apply with what data types.  Any combination not explicitly defined does not work.  For all operators any of the following can be the left hand or right hand operand\: Integer32, Counter32, Unsigned32, Counter64.  The operators +, \-, \*, /, %, <, <=, >, and >= also work with TimeTicks.  The operators &, \|, and ^ also work with IpAddress.  The operators << and >> also work with IpAddress but only as the left hand operand.  The + operator performs a concatenation of two OCTET STRINGs or two OBJECT IDENTIFIERs.  The operators &, \| perform bitwise operations on OCTET STRINGs.  If the OCTET STRING happens to be a DisplayString the results may be meaningless, but the agent system does not check this as some such systems do not have this information.  The operators << and >> perform bitwise operations on OCTET STRINGs appearing as the left hand operand.  The only functions defined are\:          counter32         counter64         arraySection         stringBegins         stringEnds         stringContains         oidBegins         oidEnds         oidContains         sum         exists  The following function definitions indicate their by naming the data type of the parameter in the parameter's position in the parameter list.  The parameter must be of the type indicated and generally may be a constant, a MIB object, a function, or an expression.  counter32(integer) \- wrapped around an integer value counter32 forces Counter32 as a data type.  counter64(integer) \- similar to counter32 except that the resulting data type is 'counter64'.  arraySection(array, integer, integer) \- selects a piece of an array (i.e. part of an OCTET STRING or OBJECT IDENTIFIER).  The integer arguments are in the range 0 to 4,294,967,295.  The first is an initial array index (1\-based) and the second is an ending array index.  A value of 0 indicates first or last element, respectively.  If the first element is larger than the array length the result is 0 length.  If the second integer is less than or equal to the first, the result is 0 length.  If the second is larger than the array length it indicates last element.  stringBegins/Ends/Contains(octetString, octetString) \- looks for the second string (which can be a string constant) in the first and returns the 1\-based index where the match began.  A return value of 0 indicates no match (i.e. boolean false).  oidBegins/Ends/Contains(oid, oid) \- looks for the second OID (which can be an OID constant) in the first and returns the the 1\-based index where the match began.  A return value of 0 indicates no match (i.e. boolean false).  sum(integerObject\*) \- sums all availiable values of the wildcarded integer object, resulting in an integer scalar. Must be used with caution as it wraps on overflow with no notification.  exists(anyTypeObject) \- verifies the object instance exists. A return value of 0 indicates NoSuchInstance (i.e. boolean false)
            	**type**\:  str
            
            	**length:** 1..1024
            
            .. attribute:: expexpressioncomment
            
            	A comment to explain the use or meaning of the expression
            	**type**\:  str
            
            .. attribute:: expexpressiondeltainterval
            
            	Sampling interval for objects in this expression with expObjectSampleType 'deltaValue'.  This object is not instantiated if not applicable.  A value of 0 indicates no automated sampling.  In this case the delta is the difference from the last time the expression was evaluated.  Note that this is subject to unpredictable delta times in the face of retries or multiple managers.  A value greater than zero is the number of seconds between automated samples.  Until the delta interval has expired once the delta for the object is effectively not instantiated and evaluating the expression has results as if the object itself were not instantiated.  Note that delta values potentially consume large amounts of system CPU and memory.  Delta state and processing must continue constantly even if the expression is not being used.  That is, the expression is being evaluated every delta interval, even if no application is reading those values.  For wildcarded objects this can be substantial overhead.  Note that delta intervals, external expression value sampling intervals and delta intervals for expressions within other expressions can have unusual interactions as they are impossible to synchronize accurately.  In general one interval embedded below another must be enough shorter that the higher sample sees relatively smooth, predictable behavior
            	**type**\:  int
            
            	**range:** 0..86400
            
            	**units**\: seconds
            
            .. attribute:: expexpressionerror
            
            	The error that occurred.  In the following explanations the expected timing of the error is in parentheses.  'S' means the error occurs on a Set request.  'E' means the error occurs on the attempt to evaluate the expression either due to Get from expValueTable or in ongoing delta processing.  invalidSyntax           the value sent for expExpression                         is not valid Expression MIB                         expression syntax (S) undefinedObjectIndex    an object reference ($n) in                         expExpression does not have a                         matching instance in                         expObjectTable (E) unrecognizedOperator    the value sent for expExpression                         held an unrecognized operator (S) unrecognizedFunction    the value sent for expExpression                         held an unrecognized function                         name (S) invalidOperandType      an operand in expExpression is not                         the right type for the associated                         operator or result (SE) unmatchedParenthesis    the value sent for expExpression                         is not correctly parenthesized (S) tooManyWildcardValues   evaluating the expression exceeded                         the limit set by expResourceDelta                         WildcardInstanceMaximum (E) recursion               through some chain of embedded                         expressions the expression invokes                         itself (E) deltaTooShort           the delta for the next evaluation                         passed before the system could                         evaluate the present sample (E) resourceUnavailable     some resource, typically dynamic                         memory, was unavailable (SE) divideByZero            an attempt to divide by zero                         occurred (E)  For the errors that occur when the attempt is made to set expExpression Set request fails with the SNMP error code 'wrongValue'. Such failures refer to the most recent failure to Set expExpression, not to the present value of expExpression which must be either unset or syntactically correct.  Errors that occur during evalutaion for a Get\* operation return the SNMP error code 'genErr' except for 'tooManyWildcardValues' and 'resourceUnavailable' which return the SNMP error code 'resourceUnavailable'.  This object is not instantiated if there have been no errors
            	**type**\:   :py:class:`Expexpressionerror <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expexpressiontable.Expexpressionentry.Expexpressionerror>`
            
            .. attribute:: expexpressionerrorindex
            
            	The 1\-based character index into expExpression for where the error occurred.  The value zero indicates irrelevance.  This object is not instantiated if there have been no errors
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: expexpressionerrors
            
            	The number of errors encountered while evaluating this expression.  Note that an object in the expression not being accessible is not considered an error.  It is a legitimate condition that causes the corresponding expression value not to be instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: expexpressionerrortime
            
            	The value of sysUpTime the last time an error caused a failure to evaluate this expression.  This object is not instantiated if there have been no errors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: expexpressioninstance
            
            	The expValueInstance being evaluated when the error occurred.  A zero\-length indicates irrelevance.  This object is not instantiated if there have been no errors
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expexpressionname
            
            	The unique name of the expression, the same as expName.  Use this object to change the expression's name without changing its expExpressionIndex
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: expexpressionowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: expexpressionprefix
            
            	An object prefix to assist an application in determining the instance indexing to use in expValueTable, relieving the application of the need to scan the expObjectTable to determine such a prefix.  See expObjectTable for information on wildcarded objects.  If the expValueInstance portion of the value OID may be treated as a scalar (that is, normally, 0) the value of expExpressionPrefix is zero length, that is, no OID at all.  Otherwise expExpressionPrefix is the value of any wildcarded instance of expObjectID for the expression.  This is sufficient as the remainder, that is, the instance fragment relevant to instancing the values must be the same for all wildcarded objects in the expression
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expexpressionvaluetype
            
            	The type of the expression value.  One and only one of the value objects in expValueTable will be instantiated to match this type.  If the result of the expression can not be made into this type, an invalidOperandType error will occur
            	**type**\:   :py:class:`Expexpressionvaluetype <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expexpressiontable.Expexpressionentry.Expexpressionvaluetype>`
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(ExpressionMib.Expexpressiontable.Expexpressionentry, self).__init__()

                self.yang_name = "expExpressionEntry"
                self.yang_parent_name = "expExpressionTable"

                self.expexpressionindex = YLeaf(YType.str, "expExpressionIndex")

                self.expexpression = YLeaf(YType.str, "expExpression")

                self.expexpressioncomment = YLeaf(YType.str, "expExpressionComment")

                self.expexpressiondeltainterval = YLeaf(YType.int32, "expExpressionDeltaInterval")

                self.expexpressionerror = YLeaf(YType.enumeration, "expExpressionError")

                self.expexpressionerrorindex = YLeaf(YType.int32, "expExpressionErrorIndex")

                self.expexpressionerrors = YLeaf(YType.uint32, "expExpressionErrors")

                self.expexpressionerrortime = YLeaf(YType.uint32, "expExpressionErrorTime")

                self.expexpressioninstance = YLeaf(YType.str, "expExpressionInstance")

                self.expexpressionname = YLeaf(YType.str, "expExpressionName")

                self.expexpressionowner = YLeaf(YType.str, "expExpressionOwner")

                self.expexpressionprefix = YLeaf(YType.str, "expExpressionPrefix")

                self.expexpressionvaluetype = YLeaf(YType.enumeration, "expExpressionValueType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("expexpressionindex",
                                "expexpression",
                                "expexpressioncomment",
                                "expexpressiondeltainterval",
                                "expexpressionerror",
                                "expexpressionerrorindex",
                                "expexpressionerrors",
                                "expexpressionerrortime",
                                "expexpressioninstance",
                                "expexpressionname",
                                "expexpressionowner",
                                "expexpressionprefix",
                                "expexpressionvaluetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExpressionMib.Expexpressiontable.Expexpressionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExpressionMib.Expexpressiontable.Expexpressionentry, self).__setattr__(name, value)

            class Expexpressionerror(Enum):
                """
                Expexpressionerror

                The error that occurred.  In the following explanations the

                expected timing of the error is in parentheses.  'S' means

                the error occurs on a Set request.  'E' means the error

                occurs on the attempt to evaluate the expression either

                due to Get from expValueTable or in ongoing delta

                processing.

                invalidSyntax           the value sent for expExpression

                                        is not valid Expression MIB

                                        expression syntax (S)

                undefinedObjectIndex    an object reference ($n) in

                                        expExpression does not have a

                                        matching instance in

                                        expObjectTable (E)

                unrecognizedOperator    the value sent for expExpression

                                        held an unrecognized operator (S)

                unrecognizedFunction    the value sent for expExpression

                                        held an unrecognized function

                                        name (S)

                invalidOperandType      an operand in expExpression is not

                                        the right type for the associated

                                        operator or result (SE)

                unmatchedParenthesis    the value sent for expExpression

                                        is not correctly parenthesized (S)

                tooManyWildcardValues   evaluating the expression exceeded

                                        the limit set by expResourceDelta

                                        WildcardInstanceMaximum (E)

                recursion               through some chain of embedded

                                        expressions the expression invokes

                                        itself (E)

                deltaTooShort           the delta for the next evaluation

                                        passed before the system could

                                        evaluate the present sample (E)

                resourceUnavailable     some resource, typically dynamic

                                        memory, was unavailable (SE)

                divideByZero            an attempt to divide by zero

                                        occurred (E)

                For the errors that occur when the attempt is made to set

                expExpression Set request fails with the SNMP error code

                'wrongValue'. Such failures refer to the most recent failure

                to Set expExpression, not to the present value of

                expExpression which must be either unset or syntactically

                correct.

                Errors that occur during evalutaion for a Get\* operation

                return the SNMP error code 'genErr' except for

                'tooManyWildcardValues' and 'resourceUnavailable' which

                return the SNMP error code 'resourceUnavailable'.

                This object is not instantiated if there have been no

                errors.

                .. data:: invalidSyntax = 1

                .. data:: undefinedObjectIndex = 2

                .. data:: unrecognizedOperator = 3

                .. data:: unrecognizedFunction = 4

                .. data:: invalidOperandType = 5

                .. data:: unmatchedParenthesis = 6

                .. data:: tooManyWildcardValues = 7

                .. data:: recursion = 8

                .. data:: deltaTooShort = 9

                .. data:: resourceUnavailable = 10

                .. data:: divideByZero = 11

                """

                invalidSyntax = Enum.YLeaf(1, "invalidSyntax")

                undefinedObjectIndex = Enum.YLeaf(2, "undefinedObjectIndex")

                unrecognizedOperator = Enum.YLeaf(3, "unrecognizedOperator")

                unrecognizedFunction = Enum.YLeaf(4, "unrecognizedFunction")

                invalidOperandType = Enum.YLeaf(5, "invalidOperandType")

                unmatchedParenthesis = Enum.YLeaf(6, "unmatchedParenthesis")

                tooManyWildcardValues = Enum.YLeaf(7, "tooManyWildcardValues")

                recursion = Enum.YLeaf(8, "recursion")

                deltaTooShort = Enum.YLeaf(9, "deltaTooShort")

                resourceUnavailable = Enum.YLeaf(10, "resourceUnavailable")

                divideByZero = Enum.YLeaf(11, "divideByZero")


            class Expexpressionvaluetype(Enum):
                """
                Expexpressionvaluetype

                The type of the expression value.  One and only one of

                the value objects in expValueTable will be instantiated to

                match this type.

                If the result of the expression can not be made into this

                type, an invalidOperandType error will occur.

                .. data:: counter32 = 1

                .. data:: unsignedOrGauge32 = 2

                .. data:: timeTicks = 3

                .. data:: integer32 = 4

                .. data:: ipAddress = 5

                .. data:: octetString = 6

                .. data:: objectId = 7

                .. data:: counter64 = 8

                """

                counter32 = Enum.YLeaf(1, "counter32")

                unsignedOrGauge32 = Enum.YLeaf(2, "unsignedOrGauge32")

                timeTicks = Enum.YLeaf(3, "timeTicks")

                integer32 = Enum.YLeaf(4, "integer32")

                ipAddress = Enum.YLeaf(5, "ipAddress")

                octetString = Enum.YLeaf(6, "octetString")

                objectId = Enum.YLeaf(7, "objectId")

                counter64 = Enum.YLeaf(8, "counter64")


            def has_data(self):
                return (
                    self.expexpressionindex.is_set or
                    self.expexpression.is_set or
                    self.expexpressioncomment.is_set or
                    self.expexpressiondeltainterval.is_set or
                    self.expexpressionerror.is_set or
                    self.expexpressionerrorindex.is_set or
                    self.expexpressionerrors.is_set or
                    self.expexpressionerrortime.is_set or
                    self.expexpressioninstance.is_set or
                    self.expexpressionname.is_set or
                    self.expexpressionowner.is_set or
                    self.expexpressionprefix.is_set or
                    self.expexpressionvaluetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.expexpressionindex.yfilter != YFilter.not_set or
                    self.expexpression.yfilter != YFilter.not_set or
                    self.expexpressioncomment.yfilter != YFilter.not_set or
                    self.expexpressiondeltainterval.yfilter != YFilter.not_set or
                    self.expexpressionerror.yfilter != YFilter.not_set or
                    self.expexpressionerrorindex.yfilter != YFilter.not_set or
                    self.expexpressionerrors.yfilter != YFilter.not_set or
                    self.expexpressionerrortime.yfilter != YFilter.not_set or
                    self.expexpressioninstance.yfilter != YFilter.not_set or
                    self.expexpressionname.yfilter != YFilter.not_set or
                    self.expexpressionowner.yfilter != YFilter.not_set or
                    self.expexpressionprefix.yfilter != YFilter.not_set or
                    self.expexpressionvaluetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "expExpressionEntry" + "[expExpressionIndex='" + self.expexpressionindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/expExpressionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.expexpressionindex.is_set or self.expexpressionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionindex.get_name_leafdata())
                if (self.expexpression.is_set or self.expexpression.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpression.get_name_leafdata())
                if (self.expexpressioncomment.is_set or self.expexpressioncomment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressioncomment.get_name_leafdata())
                if (self.expexpressiondeltainterval.is_set or self.expexpressiondeltainterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressiondeltainterval.get_name_leafdata())
                if (self.expexpressionerror.is_set or self.expexpressionerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionerror.get_name_leafdata())
                if (self.expexpressionerrorindex.is_set or self.expexpressionerrorindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionerrorindex.get_name_leafdata())
                if (self.expexpressionerrors.is_set or self.expexpressionerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionerrors.get_name_leafdata())
                if (self.expexpressionerrortime.is_set or self.expexpressionerrortime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionerrortime.get_name_leafdata())
                if (self.expexpressioninstance.is_set or self.expexpressioninstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressioninstance.get_name_leafdata())
                if (self.expexpressionname.is_set or self.expexpressionname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionname.get_name_leafdata())
                if (self.expexpressionowner.is_set or self.expexpressionowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionowner.get_name_leafdata())
                if (self.expexpressionprefix.is_set or self.expexpressionprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionprefix.get_name_leafdata())
                if (self.expexpressionvaluetype.is_set or self.expexpressionvaluetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionvaluetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "expExpressionIndex" or name == "expExpression" or name == "expExpressionComment" or name == "expExpressionDeltaInterval" or name == "expExpressionError" or name == "expExpressionErrorIndex" or name == "expExpressionErrors" or name == "expExpressionErrorTime" or name == "expExpressionInstance" or name == "expExpressionName" or name == "expExpressionOwner" or name == "expExpressionPrefix" or name == "expExpressionValueType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "expExpressionIndex"):
                    self.expexpressionindex = value
                    self.expexpressionindex.value_namespace = name_space
                    self.expexpressionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpression"):
                    self.expexpression = value
                    self.expexpression.value_namespace = name_space
                    self.expexpression.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionComment"):
                    self.expexpressioncomment = value
                    self.expexpressioncomment.value_namespace = name_space
                    self.expexpressioncomment.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionDeltaInterval"):
                    self.expexpressiondeltainterval = value
                    self.expexpressiondeltainterval.value_namespace = name_space
                    self.expexpressiondeltainterval.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionError"):
                    self.expexpressionerror = value
                    self.expexpressionerror.value_namespace = name_space
                    self.expexpressionerror.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionErrorIndex"):
                    self.expexpressionerrorindex = value
                    self.expexpressionerrorindex.value_namespace = name_space
                    self.expexpressionerrorindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionErrors"):
                    self.expexpressionerrors = value
                    self.expexpressionerrors.value_namespace = name_space
                    self.expexpressionerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionErrorTime"):
                    self.expexpressionerrortime = value
                    self.expexpressionerrortime.value_namespace = name_space
                    self.expexpressionerrortime.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionInstance"):
                    self.expexpressioninstance = value
                    self.expexpressioninstance.value_namespace = name_space
                    self.expexpressioninstance.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionName"):
                    self.expexpressionname = value
                    self.expexpressionname.value_namespace = name_space
                    self.expexpressionname.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionOwner"):
                    self.expexpressionowner = value
                    self.expexpressionowner.value_namespace = name_space
                    self.expexpressionowner.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionPrefix"):
                    self.expexpressionprefix = value
                    self.expexpressionprefix.value_namespace = name_space
                    self.expexpressionprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "expExpressionValueType"):
                    self.expexpressionvaluetype = value
                    self.expexpressionvaluetype.value_namespace = name_space
                    self.expexpressionvaluetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.expexpressionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.expexpressionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expExpressionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "expExpressionEntry"):
                for c in self.expexpressionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ExpressionMib.Expexpressiontable.Expexpressionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.expexpressionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expExpressionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Expobjecttable(Entity):
        """
        A table of object definitions for each expExpression.
        
        Wildcarding instance IDs\:
        
        It is legal to omit all or part of the instance portion for
        some or all of the objects in an expression. (See the
        DESCRIPTION of expObjectID for details.  However, note that
        if more than one object in the same expression is wildcarded
        in this way, they all must be objects where that portion of
        the instance is the same.  In other words, all objects may
        be in the same SEQUENCE or in different SEQUENCEs but with
        the same semantic index value (e.g., a value of ifIndex)
        for the wildcarded portion.
        
        .. attribute:: expobjectentry
        
        	Information about an object.  An application uses expObjectStatus to create entries in this table while in the process of defining an expression.  Values of read\-create objects in this table may be changed at any time
        	**type**\: list of    :py:class:`Expobjectentry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expobjecttable.Expobjectentry>`
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expobjecttable, self).__init__()

            self.yang_name = "expObjectTable"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expobjectentry = YList(self)

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
                        super(ExpressionMib.Expobjecttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expobjecttable, self).__setattr__(name, value)


        class Expobjectentry(Entity):
            """
            Information about an object.  An application uses
            expObjectStatus to create entries in this table while
            in the process of defining an expression.
            
            Values of read\-create objects in this table may be
            changed at any time.
            
            .. attribute:: expexpressionindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnametable.Expnameentry>`
            
            .. attribute:: expobjectindex  <key>
            
            	Within an expression, a unique, numeric identification for an object.  Prefixed with a dollar sign ('$') this is used to reference the object in the corresponding expExpression
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: expobjectconditional
            
            	The OBJECT IDENTIFIER (OID) of an object that overrides whether the instance of expObjectID is to be considered usable.  If the value of the object at expObjectConditional is 0 or not instantiated, the object at expObjectID is treated as if it is not instantiated.  In other words, expObjectConditional is a filter that controls whether or not to use the value at expObjectID.  The OID may be for a leaf object (e.g. sysObjectID.0) or may be wildcarded to match expObjectID.  If expObject is wildcarded and expObjectID in the same row is not, the wild portion of expObjectConditional must match the wildcarding of the rest of the expression.  If no object in the expression is wildcarded but expObjectConditional is, use the lexically first instance (if any) of expObjectConditional.  If the value of expObjectConditional is 0.0 operation is as if the value pointed to by expObjectConditional is a non\-zero (true) value.  Note that expObjectConditional can not trivially use an object of syntax TruthValue, since the underlying value is not 0 or 1
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectconditionalwildcard
            
            	A true value indicates the expObjectConditional of this row is a wildcard object. False indicates that expObjectConditional is fully instanced.  NOTE\: The simplest implementations of this MIB may not allow wildcards
            	**type**\:  bool
            
            .. attribute:: expobjectdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks or TimeStamp object that indicates a discontinuity in the value at expObjectID.  This object is not instantiated if expObject is not 'deltaValue'.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match expObjectID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking must still check sysUpTime for an overall discontinuity.  If the object identified is not accessible no discontinuity check will be made
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectdiscontinuityidtype
            
            	The value 'timeTicks' indicates the expObjectDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates that expObjectDeltaDiscontinuityID is of syntax TimeStamp.  This object is not instantiated if expObject is not 'deltaValue'
            	**type**\:   :py:class:`Expobjectdiscontinuityidtype <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expobjecttable.Expobjectentry.Expobjectdiscontinuityidtype>`
            
            .. attribute:: expobjectdiscontinuityidwildcard
            
            	A true value indicates the expObjectDeltaDiscontinuityID of this row is a wildcard object.  False indicates that expObjectDeltaDiscontinuityID is fully instanced.  This object is not instantiated if expObject is not 'deltaValue'.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\:  bool
            
            .. attribute:: expobjectid
            
            	The OBJECT IDENTIFIER (OID) of this object.  The OID may be fully qualified, meaning it includes a complete instance identifier part (e.g., ifInOctets.1 or sysUpTime.0), or it may not be fully qualified, meaning it may lack all or part of the instance identifier.  If the expObjectID is not fully qualified, then expObjectWildcard must be set to true(1).   The value of the expression will be multiple values, as if done for a GetNext sweep of the object.  An object here may itself be the result of an expression but recursion is not allowed.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectidwildcard
            
            	A true value indicates the expObjecID of this row is a wildcard object. False indicates that expObjectID is fully instanced.  If all expObjectWildcard values for a given expression are FALSE, expExpressionPrefix will reflect a scalar object (ie will be 0.0).  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\:  bool
            
            .. attribute:: expobjectsampletype
            
            	The method of sampling the selected variable.  An 'absoluteValue' is simply the present value of the object. A 'deltaValue' is the present value minus the previous value, which was sampled expExpressionDeltaInterval seconds ago.  This is intended primarily for use with SNMP counters, which are meaningless as an 'absoluteValue', but may be used with any integer\-based value.  When an expression contains both delta and absolute values the absolute values are obtained at the end of the delta period
            	**type**\:   :py:class:`Expobjectsampletype <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expobjecttable.Expobjectentry.Expobjectsampletype>`
            
            .. attribute:: expobjectstatus
            
            	The control that allows creation/deletion of entries.  Objects in this table may be changed while expObjectStatus is in any state
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(ExpressionMib.Expobjecttable.Expobjectentry, self).__init__()

                self.yang_name = "expObjectEntry"
                self.yang_parent_name = "expObjectTable"

                self.expexpressionindex = YLeaf(YType.str, "expExpressionIndex")

                self.expobjectindex = YLeaf(YType.uint32, "expObjectIndex")

                self.expobjectconditional = YLeaf(YType.str, "expObjectConditional")

                self.expobjectconditionalwildcard = YLeaf(YType.boolean, "expObjectConditionalWildcard")

                self.expobjectdeltadiscontinuityid = YLeaf(YType.str, "expObjectDeltaDiscontinuityID")

                self.expobjectdiscontinuityidtype = YLeaf(YType.enumeration, "expObjectDiscontinuityIDType")

                self.expobjectdiscontinuityidwildcard = YLeaf(YType.boolean, "expObjectDiscontinuityIDWildcard")

                self.expobjectid = YLeaf(YType.str, "expObjectID")

                self.expobjectidwildcard = YLeaf(YType.boolean, "expObjectIDWildcard")

                self.expobjectsampletype = YLeaf(YType.enumeration, "expObjectSampleType")

                self.expobjectstatus = YLeaf(YType.enumeration, "expObjectStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("expexpressionindex",
                                "expobjectindex",
                                "expobjectconditional",
                                "expobjectconditionalwildcard",
                                "expobjectdeltadiscontinuityid",
                                "expobjectdiscontinuityidtype",
                                "expobjectdiscontinuityidwildcard",
                                "expobjectid",
                                "expobjectidwildcard",
                                "expobjectsampletype",
                                "expobjectstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExpressionMib.Expobjecttable.Expobjectentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExpressionMib.Expobjecttable.Expobjectentry, self).__setattr__(name, value)

            class Expobjectdiscontinuityidtype(Enum):
                """
                Expobjectdiscontinuityidtype

                The value 'timeTicks' indicates the

                expObjectDeltaDiscontinuityID of this row is of syntax

                TimeTicks.  The value 'timeStamp' indicates that

                expObjectDeltaDiscontinuityID is of syntax TimeStamp.

                This object is not instantiated if expObject is not

                'deltaValue'.

                .. data:: timeTicks = 1

                .. data:: timeStamp = 2

                """

                timeTicks = Enum.YLeaf(1, "timeTicks")

                timeStamp = Enum.YLeaf(2, "timeStamp")


            class Expobjectsampletype(Enum):
                """
                Expobjectsampletype

                The method of sampling the selected variable.

                An 'absoluteValue' is simply the present value of the

                object.

                A 'deltaValue' is the present value minus the previous

                value, which was sampled expExpressionDeltaInterval

                seconds ago.  This is intended primarily for use with

                SNMP counters, which are meaningless as an 'absoluteValue',

                but may be used with any integer\-based value.

                When an expression contains both delta and absolute values

                the absolute values are obtained at the end of the delta

                period.

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")


            def has_data(self):
                return (
                    self.expexpressionindex.is_set or
                    self.expobjectindex.is_set or
                    self.expobjectconditional.is_set or
                    self.expobjectconditionalwildcard.is_set or
                    self.expobjectdeltadiscontinuityid.is_set or
                    self.expobjectdiscontinuityidtype.is_set or
                    self.expobjectdiscontinuityidwildcard.is_set or
                    self.expobjectid.is_set or
                    self.expobjectidwildcard.is_set or
                    self.expobjectsampletype.is_set or
                    self.expobjectstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.expexpressionindex.yfilter != YFilter.not_set or
                    self.expobjectindex.yfilter != YFilter.not_set or
                    self.expobjectconditional.yfilter != YFilter.not_set or
                    self.expobjectconditionalwildcard.yfilter != YFilter.not_set or
                    self.expobjectdeltadiscontinuityid.yfilter != YFilter.not_set or
                    self.expobjectdiscontinuityidtype.yfilter != YFilter.not_set or
                    self.expobjectdiscontinuityidwildcard.yfilter != YFilter.not_set or
                    self.expobjectid.yfilter != YFilter.not_set or
                    self.expobjectidwildcard.yfilter != YFilter.not_set or
                    self.expobjectsampletype.yfilter != YFilter.not_set or
                    self.expobjectstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "expObjectEntry" + "[expExpressionIndex='" + self.expexpressionindex.get() + "']" + "[expObjectIndex='" + self.expobjectindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/expObjectTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.expexpressionindex.is_set or self.expexpressionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionindex.get_name_leafdata())
                if (self.expobjectindex.is_set or self.expobjectindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectindex.get_name_leafdata())
                if (self.expobjectconditional.is_set or self.expobjectconditional.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectconditional.get_name_leafdata())
                if (self.expobjectconditionalwildcard.is_set or self.expobjectconditionalwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectconditionalwildcard.get_name_leafdata())
                if (self.expobjectdeltadiscontinuityid.is_set or self.expobjectdeltadiscontinuityid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectdeltadiscontinuityid.get_name_leafdata())
                if (self.expobjectdiscontinuityidtype.is_set or self.expobjectdiscontinuityidtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectdiscontinuityidtype.get_name_leafdata())
                if (self.expobjectdiscontinuityidwildcard.is_set or self.expobjectdiscontinuityidwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectdiscontinuityidwildcard.get_name_leafdata())
                if (self.expobjectid.is_set or self.expobjectid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectid.get_name_leafdata())
                if (self.expobjectidwildcard.is_set or self.expobjectidwildcard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectidwildcard.get_name_leafdata())
                if (self.expobjectsampletype.is_set or self.expobjectsampletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectsampletype.get_name_leafdata())
                if (self.expobjectstatus.is_set or self.expobjectstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expobjectstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "expExpressionIndex" or name == "expObjectIndex" or name == "expObjectConditional" or name == "expObjectConditionalWildcard" or name == "expObjectDeltaDiscontinuityID" or name == "expObjectDiscontinuityIDType" or name == "expObjectDiscontinuityIDWildcard" or name == "expObjectID" or name == "expObjectIDWildcard" or name == "expObjectSampleType" or name == "expObjectStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "expExpressionIndex"):
                    self.expexpressionindex = value
                    self.expexpressionindex.value_namespace = name_space
                    self.expexpressionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectIndex"):
                    self.expobjectindex = value
                    self.expobjectindex.value_namespace = name_space
                    self.expobjectindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectConditional"):
                    self.expobjectconditional = value
                    self.expobjectconditional.value_namespace = name_space
                    self.expobjectconditional.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectConditionalWildcard"):
                    self.expobjectconditionalwildcard = value
                    self.expobjectconditionalwildcard.value_namespace = name_space
                    self.expobjectconditionalwildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectDeltaDiscontinuityID"):
                    self.expobjectdeltadiscontinuityid = value
                    self.expobjectdeltadiscontinuityid.value_namespace = name_space
                    self.expobjectdeltadiscontinuityid.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectDiscontinuityIDType"):
                    self.expobjectdiscontinuityidtype = value
                    self.expobjectdiscontinuityidtype.value_namespace = name_space
                    self.expobjectdiscontinuityidtype.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectDiscontinuityIDWildcard"):
                    self.expobjectdiscontinuityidwildcard = value
                    self.expobjectdiscontinuityidwildcard.value_namespace = name_space
                    self.expobjectdiscontinuityidwildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectID"):
                    self.expobjectid = value
                    self.expobjectid.value_namespace = name_space
                    self.expobjectid.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectIDWildcard"):
                    self.expobjectidwildcard = value
                    self.expobjectidwildcard.value_namespace = name_space
                    self.expobjectidwildcard.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectSampleType"):
                    self.expobjectsampletype = value
                    self.expobjectsampletype.value_namespace = name_space
                    self.expobjectsampletype.value_namespace_prefix = name_space_prefix
                if(value_path == "expObjectStatus"):
                    self.expobjectstatus = value
                    self.expobjectstatus.value_namespace = name_space
                    self.expobjectstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.expobjectentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.expobjectentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expObjectTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "expObjectEntry"):
                for c in self.expobjectentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ExpressionMib.Expobjecttable.Expobjectentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.expobjectentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expObjectEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Expvaluetable(Entity):
        """
        A table of values from evaluated expressions.
        
        .. attribute:: expvalueentry
        
        	A single value from an evaluated expression.  For a given instance, only one 'Val' object in the conceptual row will be instantiated, that is, the one with the appropriate type for the value.  For values that contain no objects of  expObjectSampleType 'deltaValue', reading a value from the table causes the evaluation of the expression for that value.  For those that contain a 'deltaValue' the value read is as of the last delta interval.  If in the attempt to evaluate the expression one or more of the necessary objects is not available, the corresponding entry in this table is effectively not instantiated.  To maintain security of MIB information, expression evaluation must take place using security credentials for the implied Gets of the objects in the expression.  For expressions with no deltaValue those security credentials are the ones that came with the Get\* for the value.  For expressions with a deltaValue the ongoing expression evaluation is under the security credentials of the creator of the corresponding expNameEntry
        	**type**\: list of    :py:class:`Expvalueentry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expvaluetable.Expvalueentry>`
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(ExpressionMib.Expvaluetable, self).__init__()

            self.yang_name = "expValueTable"
            self.yang_parent_name = "EXPRESSION-MIB"

            self.expvalueentry = YList(self)

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
                        super(ExpressionMib.Expvaluetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExpressionMib.Expvaluetable, self).__setattr__(name, value)


        class Expvalueentry(Entity):
            """
            A single value from an evaluated expression.  For a given
            instance, only one 'Val' object in the conceptual row will
            be instantiated, that is, the one with the appropriate type
            for the value.  For values that contain no objects of 
            expObjectSampleType 'deltaValue', reading a value from the
            table causes the evaluation of the expression for that
            value.  For those that contain a 'deltaValue' the value
            read is as of the last delta interval.
            
            If in the attempt to evaluate the expression one or more
            of the necessary objects is not available, the corresponding
            entry in this table is effectively not instantiated.
            
            To maintain security of MIB information, expression
            evaluation must take place using security credentials for
            the implied Gets of the objects in the expression.  For
            expressions with no deltaValue those security credentials
            are the ones that came with the Get\* for the value.  For
            expressions with a deltaValue the ongoing expression
            evaluation is under the security credentials of the
            creator of the corresponding expNameEntry.
            
            .. attribute:: expexpressionindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.ExpressionMib.Expnametable.Expnameentry>`
            
            .. attribute:: expvalueinstance  <key>
            
            	The final instance portion of a value's OID according to the wildcarding in instances of expObjectID for the expression.  The prefix of this OID fragment is 0.0, leading to the following behavior.  If there is no wildcarding, the value is 0.0.0.  In other words, there is one value which standing alone would have been a scalar with a 0 at the end of its OID.  If there is wildcarding, the value is 0.0 followed by a value that the wildcard can take, thus defining one value instance for each real, possible value of the wildcard. So, for example, if the wildcard worked out to be an ifIndex, there is an expValueInstance for each applicable ifIndex
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expvaluecounter32val
            
            	The value when expExpressionValueType is 'counter32'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: expvaluecounter64val
            
            	The value when expExpressionValueType is 'counter64'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: expvalueinteger32val
            
            	The value when expExpressionValueType is 'integer32'
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: expvalueipaddressval
            
            	The value when expExpressionValueType is 'ipAddress'
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: expvalueoctetstringval
            
            	The value when expExpressionValueType is 'octetString'
            	**type**\:  str
            
            	**length:** 0..65535
            
            .. attribute:: expvalueoidval
            
            	The value when expExpressionValueType is 'objectId'
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expvalueunsigned32val
            
            	The value when expExpressionValueType is 'unsignedOrGauge32' or 'timeTicks'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(ExpressionMib.Expvaluetable.Expvalueentry, self).__init__()

                self.yang_name = "expValueEntry"
                self.yang_parent_name = "expValueTable"

                self.expexpressionindex = YLeaf(YType.str, "expExpressionIndex")

                self.expvalueinstance = YLeaf(YType.str, "expValueInstance")

                self.expvaluecounter32val = YLeaf(YType.uint32, "expValueCounter32Val")

                self.expvaluecounter64val = YLeaf(YType.uint64, "expValueCounter64Val")

                self.expvalueinteger32val = YLeaf(YType.int32, "expValueInteger32Val")

                self.expvalueipaddressval = YLeaf(YType.str, "expValueIpAddressVal")

                self.expvalueoctetstringval = YLeaf(YType.str, "expValueOctetStringVal")

                self.expvalueoidval = YLeaf(YType.str, "expValueOidVal")

                self.expvalueunsigned32val = YLeaf(YType.uint32, "expValueUnsigned32Val")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("expexpressionindex",
                                "expvalueinstance",
                                "expvaluecounter32val",
                                "expvaluecounter64val",
                                "expvalueinteger32val",
                                "expvalueipaddressval",
                                "expvalueoctetstringval",
                                "expvalueoidval",
                                "expvalueunsigned32val") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExpressionMib.Expvaluetable.Expvalueentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExpressionMib.Expvaluetable.Expvalueentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.expexpressionindex.is_set or
                    self.expvalueinstance.is_set or
                    self.expvaluecounter32val.is_set or
                    self.expvaluecounter64val.is_set or
                    self.expvalueinteger32val.is_set or
                    self.expvalueipaddressval.is_set or
                    self.expvalueoctetstringval.is_set or
                    self.expvalueoidval.is_set or
                    self.expvalueunsigned32val.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.expexpressionindex.yfilter != YFilter.not_set or
                    self.expvalueinstance.yfilter != YFilter.not_set or
                    self.expvaluecounter32val.yfilter != YFilter.not_set or
                    self.expvaluecounter64val.yfilter != YFilter.not_set or
                    self.expvalueinteger32val.yfilter != YFilter.not_set or
                    self.expvalueipaddressval.yfilter != YFilter.not_set or
                    self.expvalueoctetstringval.yfilter != YFilter.not_set or
                    self.expvalueoidval.yfilter != YFilter.not_set or
                    self.expvalueunsigned32val.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "expValueEntry" + "[expExpressionIndex='" + self.expexpressionindex.get() + "']" + "[expValueInstance='" + self.expvalueinstance.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/expValueTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.expexpressionindex.is_set or self.expexpressionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expexpressionindex.get_name_leafdata())
                if (self.expvalueinstance.is_set or self.expvalueinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueinstance.get_name_leafdata())
                if (self.expvaluecounter32val.is_set or self.expvaluecounter32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvaluecounter32val.get_name_leafdata())
                if (self.expvaluecounter64val.is_set or self.expvaluecounter64val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvaluecounter64val.get_name_leafdata())
                if (self.expvalueinteger32val.is_set or self.expvalueinteger32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueinteger32val.get_name_leafdata())
                if (self.expvalueipaddressval.is_set or self.expvalueipaddressval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueipaddressval.get_name_leafdata())
                if (self.expvalueoctetstringval.is_set or self.expvalueoctetstringval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueoctetstringval.get_name_leafdata())
                if (self.expvalueoidval.is_set or self.expvalueoidval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueoidval.get_name_leafdata())
                if (self.expvalueunsigned32val.is_set or self.expvalueunsigned32val.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.expvalueunsigned32val.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "expExpressionIndex" or name == "expValueInstance" or name == "expValueCounter32Val" or name == "expValueCounter64Val" or name == "expValueInteger32Val" or name == "expValueIpAddressVal" or name == "expValueOctetStringVal" or name == "expValueOidVal" or name == "expValueUnsigned32Val"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "expExpressionIndex"):
                    self.expexpressionindex = value
                    self.expexpressionindex.value_namespace = name_space
                    self.expexpressionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueInstance"):
                    self.expvalueinstance = value
                    self.expvalueinstance.value_namespace = name_space
                    self.expvalueinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueCounter32Val"):
                    self.expvaluecounter32val = value
                    self.expvaluecounter32val.value_namespace = name_space
                    self.expvaluecounter32val.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueCounter64Val"):
                    self.expvaluecounter64val = value
                    self.expvaluecounter64val.value_namespace = name_space
                    self.expvaluecounter64val.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueInteger32Val"):
                    self.expvalueinteger32val = value
                    self.expvalueinteger32val.value_namespace = name_space
                    self.expvalueinteger32val.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueIpAddressVal"):
                    self.expvalueipaddressval = value
                    self.expvalueipaddressval.value_namespace = name_space
                    self.expvalueipaddressval.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueOctetStringVal"):
                    self.expvalueoctetstringval = value
                    self.expvalueoctetstringval.value_namespace = name_space
                    self.expvalueoctetstringval.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueOidVal"):
                    self.expvalueoidval = value
                    self.expvalueoidval.value_namespace = name_space
                    self.expvalueoidval.value_namespace_prefix = name_space_prefix
                if(value_path == "expValueUnsigned32Val"):
                    self.expvalueunsigned32val = value
                    self.expvalueunsigned32val.value_namespace = name_space
                    self.expvalueunsigned32val.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.expvalueentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.expvalueentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "expValueTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "expValueEntry"):
                for c in self.expvalueentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ExpressionMib.Expvaluetable.Expvalueentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.expvalueentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "expValueEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.expexpressiontable is not None and self.expexpressiontable.has_data()) or
            (self.expnames is not None and self.expnames.has_data()) or
            (self.expnametable is not None and self.expnametable.has_data()) or
            (self.expobjecttable is not None and self.expobjecttable.has_data()) or
            (self.expresource is not None and self.expresource.has_data()) or
            (self.expvaluetable is not None and self.expvaluetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.expexpressiontable is not None and self.expexpressiontable.has_operation()) or
            (self.expnames is not None and self.expnames.has_operation()) or
            (self.expnametable is not None and self.expnametable.has_operation()) or
            (self.expobjecttable is not None and self.expobjecttable.has_operation()) or
            (self.expresource is not None and self.expresource.has_operation()) or
            (self.expvaluetable is not None and self.expvaluetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "EXPRESSION-MIB:EXPRESSION-MIB" + path_buffer

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

        if (child_yang_name == "expExpressionTable"):
            if (self.expexpressiontable is None):
                self.expexpressiontable = ExpressionMib.Expexpressiontable()
                self.expexpressiontable.parent = self
                self._children_name_map["expexpressiontable"] = "expExpressionTable"
            return self.expexpressiontable

        if (child_yang_name == "expNames"):
            if (self.expnames is None):
                self.expnames = ExpressionMib.Expnames()
                self.expnames.parent = self
                self._children_name_map["expnames"] = "expNames"
            return self.expnames

        if (child_yang_name == "expNameTable"):
            if (self.expnametable is None):
                self.expnametable = ExpressionMib.Expnametable()
                self.expnametable.parent = self
                self._children_name_map["expnametable"] = "expNameTable"
            return self.expnametable

        if (child_yang_name == "expObjectTable"):
            if (self.expobjecttable is None):
                self.expobjecttable = ExpressionMib.Expobjecttable()
                self.expobjecttable.parent = self
                self._children_name_map["expobjecttable"] = "expObjectTable"
            return self.expobjecttable

        if (child_yang_name == "expResource"):
            if (self.expresource is None):
                self.expresource = ExpressionMib.Expresource()
                self.expresource.parent = self
                self._children_name_map["expresource"] = "expResource"
            return self.expresource

        if (child_yang_name == "expValueTable"):
            if (self.expvaluetable is None):
                self.expvaluetable = ExpressionMib.Expvaluetable()
                self.expvaluetable.parent = self
                self._children_name_map["expvaluetable"] = "expValueTable"
            return self.expvaluetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "expExpressionTable" or name == "expNames" or name == "expNameTable" or name == "expObjectTable" or name == "expResource" or name == "expValueTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ExpressionMib()
        return self._top_entity


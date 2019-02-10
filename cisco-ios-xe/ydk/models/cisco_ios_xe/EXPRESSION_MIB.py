""" EXPRESSION_MIB 

The MIB module for defining expressions of MIB objects
for network management purposes.

This MIB is an early snapshot of work done by the IETF's
Distributed Management working group.  After this snapshot
was taken, the MIB was modified, had new OIDs assigned,
and then published as RFC 2982.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class EXPRESSIONMIB(Entity):
    """
    
    
    .. attribute:: expresource
    
    	
    	**type**\:  :py:class:`ExpResource <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpResource>`
    
    	**config**\: False
    
    .. attribute:: expnames
    
    	
    	**type**\:  :py:class:`ExpNames <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNames>`
    
    	**config**\: False
    
    .. attribute:: expnametable
    
    	A table of expression names, for creating and deleting expressions
    	**type**\:  :py:class:`ExpNameTable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNameTable>`
    
    	**config**\: False
    
    .. attribute:: expexpressiontable
    
    	A table of expression definitions
    	**type**\:  :py:class:`ExpExpressionTable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpExpressionTable>`
    
    	**config**\: False
    
    .. attribute:: expobjecttable
    
    	A table of object definitions for each expExpression.  Wildcarding instance IDs\:  It is legal to omit all or part of the instance portion for some or all of the objects in an expression. (See the DESCRIPTION of expObjectID for details.  However, note that if more than one object in the same expression is wildcarded in this way, they all must be objects where that portion of the instance is the same.  In other words, all objects may be in the same SEQUENCE or in different SEQUENCEs but with the same semantic index value (e.g., a value of ifIndex) for the wildcarded portion
    	**type**\:  :py:class:`ExpObjectTable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpObjectTable>`
    
    	**config**\: False
    
    .. attribute:: expvaluetable
    
    	A table of values from evaluated expressions
    	**type**\:  :py:class:`ExpValueTable <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpValueTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'EXPRESSION-MIB'
    _revision = '2005-11-24'

    def __init__(self):
        super(EXPRESSIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "EXPRESSION-MIB"
        self.yang_parent_name = "EXPRESSION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("expResource", ("expresource", EXPRESSIONMIB.ExpResource)), ("expNames", ("expnames", EXPRESSIONMIB.ExpNames)), ("expNameTable", ("expnametable", EXPRESSIONMIB.ExpNameTable)), ("expExpressionTable", ("expexpressiontable", EXPRESSIONMIB.ExpExpressionTable)), ("expObjectTable", ("expobjecttable", EXPRESSIONMIB.ExpObjectTable)), ("expValueTable", ("expvaluetable", EXPRESSIONMIB.ExpValueTable))])
        self._leafs = OrderedDict()

        self.expresource = EXPRESSIONMIB.ExpResource()
        self.expresource.parent = self
        self._children_name_map["expresource"] = "expResource"

        self.expnames = EXPRESSIONMIB.ExpNames()
        self.expnames.parent = self
        self._children_name_map["expnames"] = "expNames"

        self.expnametable = EXPRESSIONMIB.ExpNameTable()
        self.expnametable.parent = self
        self._children_name_map["expnametable"] = "expNameTable"

        self.expexpressiontable = EXPRESSIONMIB.ExpExpressionTable()
        self.expexpressiontable.parent = self
        self._children_name_map["expexpressiontable"] = "expExpressionTable"

        self.expobjecttable = EXPRESSIONMIB.ExpObjectTable()
        self.expobjecttable.parent = self
        self._children_name_map["expobjecttable"] = "expObjectTable"

        self.expvaluetable = EXPRESSIONMIB.ExpValueTable()
        self.expvaluetable.parent = self
        self._children_name_map["expvaluetable"] = "expValueTable"
        self._segment_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EXPRESSIONMIB, [], name, value)


    class ExpResource(Entity):
        """
        
        
        .. attribute:: expresourcedeltaminimum
        
        	The minimum expExpressionDeltaInterval this system will accept.  A system may use the larger values of this minimum to lessen the impact of constantly computing deltas.  The value \-1 indicates this system will not accept deltaValue as a value for expObjectSampleType.  Unless explicitly resource limited, a system's value for this object should be 1.  Changing this value will not invalidate an existing setting of expObjectSampleType
        	**type**\: int
        
        	**range:** \-1..None \| 1..600
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: expresourcedeltawildcardinstancemaximum
        
        	The maximum number of dynamic instance entries this system will support for wildcarded delta objects in expressions. These are the entries that maintain state, one for each instance of each deltaValue object for each value of an expression.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object should be 0.  Changing this value will not eliminate or inhibit existing delta wildcard instance objects but will prevent the creation of more such objects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstances
        
        	The number of currently active instance entries as defined for expResourceDeltaWildcardInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceshigh
        
        	The highest value of expResourceDeltaWildcardInstances that has occurred since initialization of the management system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceresourcelacks
        
        	The number of times this system could not evaluate an expression because that would have created a value instance in excess of expResourceDeltaWildcardInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: instances
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpResource, self).__init__()

            self.yang_name = "expResource"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('expresourcedeltaminimum', (YLeaf(YType.int32, 'expResourceDeltaMinimum'), ['int'])),
                ('expresourcedeltawildcardinstancemaximum', (YLeaf(YType.uint32, 'expResourceDeltaWildcardInstanceMaximum'), ['int'])),
                ('expresourcedeltawildcardinstances', (YLeaf(YType.uint32, 'expResourceDeltaWildcardInstances'), ['int'])),
                ('expresourcedeltawildcardinstanceshigh', (YLeaf(YType.uint32, 'expResourceDeltaWildcardInstancesHigh'), ['int'])),
                ('expresourcedeltawildcardinstanceresourcelacks', (YLeaf(YType.uint32, 'expResourceDeltaWildcardInstanceResourceLacks'), ['int'])),
            ])
            self.expresourcedeltaminimum = None
            self.expresourcedeltawildcardinstancemaximum = None
            self.expresourcedeltawildcardinstances = None
            self.expresourcedeltawildcardinstanceshigh = None
            self.expresourcedeltawildcardinstanceresourcelacks = None
            self._segment_path = lambda: "expResource"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpResource, ['expresourcedeltaminimum', 'expresourcedeltawildcardinstancemaximum', 'expresourcedeltawildcardinstances', 'expresourcedeltawildcardinstanceshigh', 'expresourcedeltawildcardinstanceresourcelacks'], name, value)



    class ExpNames(Entity):
        """
        
        
        .. attribute:: expnamelastchange
        
        	The value of sysUpTime the last time an expression was created or deleted or had its name changed using expExpressionName
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: expnamehighestindex
        
        	The highest value of ExpressionIndex ever assigned on this system.  Preferrably this value is preserved across system reboots.  A managed system that is unable to store expressions across reboots need not preserve this value across reboots.  If all expression\-creating applications cooperate, they may use this to avoid reusing an ExpressionIndex.  To do so, attempt creation of a new entry with this value + 1 as the value of expExpressionIndex.  Although reusing ExpressionIndexes could lead to an application receiving a misunderstood value, it is a matter of local management policy whether to reuse them
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpNames, self).__init__()

            self.yang_name = "expNames"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('expnamelastchange', (YLeaf(YType.uint32, 'expNameLastChange'), ['int'])),
                ('expnamehighestindex', (YLeaf(YType.uint32, 'expNameHighestIndex'), ['int'])),
            ])
            self.expnamelastchange = None
            self.expnamehighestindex = None
            self._segment_path = lambda: "expNames"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpNames, ['expnamelastchange', 'expnamehighestindex'], name, value)



    class ExpNameTable(Entity):
        """
        A table of expression names, for creating and deleting
        expressions.
        
        .. attribute:: expnameentry
        
        	Information about a single expression.  New expressions can be created using expNameStatus.  To create an expression first create the named entry in this table.  Then use expExpressionIndex to populate expExpressionTable and expObjectTable.  For expression evaluation to succeed all related entries in expNameTable, expExpressionTable, and expObjectTable must be 'active'.  If these conditions are not met the corresponding values in expValue simply are not instantiated.  Deleting an entry deletes all related entries in expExpressionTable and expObjectTable.  Because of the relationships among the multiple tables for an expression (expNameTable, expExpressionTable, expObjectTable, and expValueTable) and the SNMP rules for independence in setting object values, it is necessary to do final error checking when an expression is evaluated, that is, when one of its instances in expValueTable is read.  Earlier checking need not be done and an implementation may not impose any ordering on the creation of objects related to an expression other than to require values for expName and expExpressionIndex before any other related objects can be created.  To maintain security of MIB information, when creating a new row in this table, the managed system must record the security credentials of the requester.  If the subsequent expression includes objects with expObjectSampleType 'deltaValue' the evaluation of that expression takes place under the security credentials of the creator of its expNameEntry
        	**type**\: list of  		 :py:class:`ExpNameEntry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNameTable.ExpNameEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpNameTable, self).__init__()

            self.yang_name = "expNameTable"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("expNameEntry", ("expnameentry", EXPRESSIONMIB.ExpNameTable.ExpNameEntry))])
            self._leafs = OrderedDict()

            self.expnameentry = YList(self)
            self._segment_path = lambda: "expNameTable"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpNameTable, [], name, value)


        class ExpNameEntry(Entity):
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
            
            .. attribute:: expname  (key)
            
            	The name of the expression.  Choosing names with useful lexical ordering supports using GetNext or GetBulk to retrieve a useful subset of the table
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: expexpressionindex
            
            	The numeric identification of the expression.  Applications may select this number in ascending numerical order by using expNameHighestIndex as a hint or may use any other acceptable, unused number.  Once set this value may not be set to a different value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: expnamestatus
            
            	The control that allows creation/deletion of entries
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(EXPRESSIONMIB.ExpNameTable.ExpNameEntry, self).__init__()

                self.yang_name = "expNameEntry"
                self.yang_parent_name = "expNameTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expname', (YLeaf(YType.str, 'expName'), ['str'])),
                    ('expexpressionindex', (YLeaf(YType.uint32, 'expExpressionIndex'), ['int'])),
                    ('expnamestatus', (YLeaf(YType.enumeration, 'expNameStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.expname = None
                self.expexpressionindex = None
                self.expnamestatus = None
                self._segment_path = lambda: "expNameEntry" + "[expName='" + str(self.expname) + "']"
                self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/expNameTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EXPRESSIONMIB.ExpNameTable.ExpNameEntry, ['expname', 'expexpressionindex', 'expnamestatus'], name, value)




    class ExpExpressionTable(Entity):
        """
        A table of expression definitions.
        
        .. attribute:: expexpressionentry
        
        	Information about a single expression.  An entry appears in this table when an entry is created in expNameTable. Deleting that expNameTable entry automatically deletes this entry and its associated expObjectTable entries.  Values of read\-write objects in this table may be changed at any time
        	**type**\: list of  		 :py:class:`ExpExpressionEntry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpExpressionTable, self).__init__()

            self.yang_name = "expExpressionTable"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("expExpressionEntry", ("expexpressionentry", EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry))])
            self._leafs = OrderedDict()

            self.expexpressionentry = YList(self)
            self._segment_path = lambda: "expExpressionTable"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpExpressionTable, [], name, value)


        class ExpExpressionEntry(Entity):
            """
            Information about a single expression.  An entry appears
            in this table when an entry is created in expNameTable.
            Deleting that expNameTable entry automatically deletes
            this entry and its associated expObjectTable entries.
            
            Values of read\-write objects in this table may be changed
            at any time.
            
            .. attribute:: expexpressionindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNameTable.ExpNameEntry>`
            
            	**config**\: False
            
            .. attribute:: expexpressionname
            
            	The unique name of the expression, the same as expName.  Use this object to change the expression's name without changing its expExpressionIndex
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: expexpression
            
            	The expression to be evaluated.  This object is the same as a DisplayString (RFC 1903) except for its maximum length.  Except for the variable names the expression is in ANSI C syntax.  Only the subset of ANSI C operators and functions listed here is allowed.  Variables are expressed as a dollar sign ('$') and an integer that corresponds to an expObjectIndex.  An example of a valid expression is\:          ($1\-$5)\*100  Expressions may not be recursive, that is although an expression may use the results of another expression, it may not contain any variable that is directly or indirectly a result of its own evaluation.  The only allowed operators are\:          ( )         \- (unary)         + \- \* / %         & \| ^ << >> ~         ! && \|\| == != > >= < <=  Note the parentheses are included for parenthesizing the expression, not for casting data types.  The only constant types defined are\:          int (32\-bit signed)         long (64\-bit signed)         unsigned int         unsigned long         hexadecimal         character         string         oid  The default type for a positive integer is int unless it is too large in which case it is long.  All but oid are as defined for ANSI C.  Note that a hexadecimal constant may end up as a scalar or an array of 8\-bit integers.  A string constant is enclosed in double quotes and may contain back\-slashed individual characters as in ANSI C.  An oid constant comprises 32\-bit, unsigned integers and at least one period, for example\:          0.         .0         1.3.6.1  Integer\-typed objects are treated as 32\- or 64\-bit, signed or unsigned integers, as appropriate.  The results of mixing them are as for ANSI C, including the type of the result.  Note that a 32\-bit value is thus promoted to 64 bits only in an operation with a 64\-bit value.  There is no provision for larger values to handle overflow.  Relative to SNMP data types, a resulting value becomes unsigned when calculating it uses any unsigned value, including a counter.  To force the final value to be of data type counter the expression must explicitly use the counter32() or counter64() function (defined below).  OCTET STRINGS and OBJECT IDENTIFIERs are treated as 1\-based arrays of unsigned 8\-bit integers and unsigned 32\-bit integers, respectively.  IpAddresses are treated as 32\-bit, unsigned integers in network byte order, that is, the hex version of 255.0.0.0 is 0xff000000.  Conditional expressions result in a 32\-bit, unsigned integer of value 0 for false or 1 for true. When an arbitrary value is used as a boolean 0 is false and non\-zero is true.  Rules for the resulting data type from an operation, based on the operator\:  For << and >> the result is the same as the left hand operand.  For &&, \|\|, ==, !=, <, <=, >, and >= the result is always Unsigned32.  For unary \- the result is always Integer32.  For +, \-, \*, /, %, &, \|, and ^ the result is promoted according to the following rules, in order from most to least preferred\:          If left hand and right hand operands are the same         type, use that.          If either side is Counter64, use that.          If either side is IpAddress, use that.          If either side is TimeTicks, use that.          If either side is Counter32, use that.          Otherwise use Unsigned32.  The following rules say what operators apply with what data types.  Any combination not explicitly defined does not work.  For all operators any of the following can be the left hand or right hand operand\: Integer32, Counter32, Unsigned32, Counter64.  The operators +, \-, \*, /, %, <, <=, >, and >= also work with TimeTicks.  The operators &, \|, and ^ also work with IpAddress.  The operators << and >> also work with IpAddress but only as the left hand operand.  The + operator performs a concatenation of two OCTET STRINGs or two OBJECT IDENTIFIERs.  The operators &, \| perform bitwise operations on OCTET STRINGs.  If the OCTET STRING happens to be a DisplayString the results may be meaningless, but the agent system does not check this as some such systems do not have this information.  The operators << and >> perform bitwise operations on OCTET STRINGs appearing as the left hand operand.  The only functions defined are\:          counter32         counter64         arraySection         stringBegins         stringEnds         stringContains         oidBegins         oidEnds         oidContains         sum         exists  The following function definitions indicate their by naming the data type of the parameter in the parameter's position in the parameter list.  The parameter must be of the type indicated and generally may be a constant, a MIB object, a function, or an expression.  counter32(integer) \- wrapped around an integer value counter32 forces Counter32 as a data type.  counter64(integer) \- similar to counter32 except that the resulting data type is 'counter64'.  arraySection(array, integer, integer) \- selects a piece of an array (i.e. part of an OCTET STRING or OBJECT IDENTIFIER).  The integer arguments are in the range 0 to 4,294,967,295.  The first is an initial array index (1\-based) and the second is an ending array index.  A value of 0 indicates first or last element, respectively.  If the first element is larger than the array length the result is 0 length.  If the second integer is less than or equal to the first, the result is 0 length.  If the second is larger than the array length it indicates last element.  stringBegins/Ends/Contains(octetString, octetString) \- looks for the second string (which can be a string constant) in the first and returns the 1\-based index where the match began.  A return value of 0 indicates no match (i.e. boolean false).  oidBegins/Ends/Contains(oid, oid) \- looks for the second OID (which can be an OID constant) in the first and returns the the 1\-based index where the match began.  A return value of 0 indicates no match (i.e. boolean false).  sum(integerObject\*) \- sums all availiable values of the wildcarded integer object, resulting in an integer scalar. Must be used with caution as it wraps on overflow with no notification.  exists(anyTypeObject) \- verifies the object instance exists. A return value of 0 indicates NoSuchInstance (i.e. boolean false)
            	**type**\: str
            
            	**length:** 1..1024
            
            	**config**\: False
            
            .. attribute:: expexpressionvaluetype
            
            	The type of the expression value.  One and only one of the value objects in expValueTable will be instantiated to match this type.  If the result of the expression can not be made into this type, an invalidOperandType error will occur
            	**type**\:  :py:class:`ExpExpressionValueType <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry.ExpExpressionValueType>`
            
            	**config**\: False
            
            .. attribute:: expexpressioncomment
            
            	A comment to explain the use or meaning of the expression
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: expexpressiondeltainterval
            
            	Sampling interval for objects in this expression with expObjectSampleType 'deltaValue'.  This object is not instantiated if not applicable.  A value of 0 indicates no automated sampling.  In this case the delta is the difference from the last time the expression was evaluated.  Note that this is subject to unpredictable delta times in the face of retries or multiple managers.  A value greater than zero is the number of seconds between automated samples.  Until the delta interval has expired once the delta for the object is effectively not instantiated and evaluating the expression has results as if the object itself were not instantiated.  Note that delta values potentially consume large amounts of system CPU and memory.  Delta state and processing must continue constantly even if the expression is not being used.  That is, the expression is being evaluated every delta interval, even if no application is reading those values.  For wildcarded objects this can be substantial overhead.  Note that delta intervals, external expression value sampling intervals and delta intervals for expressions within other expressions can have unusual interactions as they are impossible to synchronize accurately.  In general one interval embedded below another must be enough shorter that the higher sample sees relatively smooth, predictable behavior
            	**type**\: int
            
            	**range:** 0..86400
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: expexpressionprefix
            
            	An object prefix to assist an application in determining the instance indexing to use in expValueTable, relieving the application of the need to scan the expObjectTable to determine such a prefix.  See expObjectTable for information on wildcarded objects.  If the expValueInstance portion of the value OID may be treated as a scalar (that is, normally, 0) the value of expExpressionPrefix is zero length, that is, no OID at all.  Otherwise expExpressionPrefix is the value of any wildcarded instance of expObjectID for the expression.  This is sufficient as the remainder, that is, the instance fragment relevant to instancing the values must be the same for all wildcarded objects in the expression
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expexpressionerrors
            
            	The number of errors encountered while evaluating this expression.  Note that an object in the expression not being accessible is not considered an error.  It is a legitimate condition that causes the corresponding expression value not to be instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: expexpressionerrortime
            
            	The value of sysUpTime the last time an error caused a failure to evaluate this expression.  This object is not instantiated if there have been no errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: expexpressionerrorindex
            
            	The 1\-based character index into expExpression for where the error occurred.  The value zero indicates irrelevance.  This object is not instantiated if there have been no errors
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: expexpressionerror
            
            	The error that occurred.  In the following explanations the expected timing of the error is in parentheses.  'S' means the error occurs on a Set request.  'E' means the error occurs on the attempt to evaluate the expression either due to Get from expValueTable or in ongoing delta processing.  invalidSyntax           the value sent for expExpression                         is not valid Expression MIB                         expression syntax (S) undefinedObjectIndex    an object reference ($n) in                         expExpression does not have a                         matching instance in                         expObjectTable (E) unrecognizedOperator    the value sent for expExpression                         held an unrecognized operator (S) unrecognizedFunction    the value sent for expExpression                         held an unrecognized function                         name (S) invalidOperandType      an operand in expExpression is not                         the right type for the associated                         operator or result (SE) unmatchedParenthesis    the value sent for expExpression                         is not correctly parenthesized (S) tooManyWildcardValues   evaluating the expression exceeded                         the limit set by expResourceDelta                         WildcardInstanceMaximum (E) recursion               through some chain of embedded                         expressions the expression invokes                         itself (E) deltaTooShort           the delta for the next evaluation                         passed before the system could                         evaluate the present sample (E) resourceUnavailable     some resource, typically dynamic                         memory, was unavailable (SE) divideByZero            an attempt to divide by zero                         occurred (E)  For the errors that occur when the attempt is made to set expExpression Set request fails with the SNMP error code 'wrongValue'. Such failures refer to the most recent failure to Set expExpression, not to the present value of expExpression which must be either unset or syntactically correct.  Errors that occur during evalutaion for a Get\* operation return the SNMP error code 'genErr' except for 'tooManyWildcardValues' and 'resourceUnavailable' which return the SNMP error code 'resourceUnavailable'.  This object is not instantiated if there have been no errors
            	**type**\:  :py:class:`ExpExpressionError <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry.ExpExpressionError>`
            
            	**config**\: False
            
            .. attribute:: expexpressioninstance
            
            	The expValueInstance being evaluated when the error occurred.  A zero\-length indicates irrelevance.  This object is not instantiated if there have been no errors
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expexpressionowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry, self).__init__()

                self.yang_name = "expExpressionEntry"
                self.yang_parent_name = "expExpressionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionindex', (YLeaf(YType.str, 'expExpressionIndex'), ['int'])),
                    ('expexpressionname', (YLeaf(YType.str, 'expExpressionName'), ['str'])),
                    ('expexpression', (YLeaf(YType.str, 'expExpression'), ['str'])),
                    ('expexpressionvaluetype', (YLeaf(YType.enumeration, 'expExpressionValueType'), [('ydk.models.cisco_ios_xe.EXPRESSION_MIB', 'EXPRESSIONMIB', 'ExpExpressionTable.ExpExpressionEntry.ExpExpressionValueType')])),
                    ('expexpressioncomment', (YLeaf(YType.str, 'expExpressionComment'), ['str'])),
                    ('expexpressiondeltainterval', (YLeaf(YType.int32, 'expExpressionDeltaInterval'), ['int'])),
                    ('expexpressionprefix', (YLeaf(YType.str, 'expExpressionPrefix'), ['str'])),
                    ('expexpressionerrors', (YLeaf(YType.uint32, 'expExpressionErrors'), ['int'])),
                    ('expexpressionerrortime', (YLeaf(YType.uint32, 'expExpressionErrorTime'), ['int'])),
                    ('expexpressionerrorindex', (YLeaf(YType.int32, 'expExpressionErrorIndex'), ['int'])),
                    ('expexpressionerror', (YLeaf(YType.enumeration, 'expExpressionError'), [('ydk.models.cisco_ios_xe.EXPRESSION_MIB', 'EXPRESSIONMIB', 'ExpExpressionTable.ExpExpressionEntry.ExpExpressionError')])),
                    ('expexpressioninstance', (YLeaf(YType.str, 'expExpressionInstance'), ['str'])),
                    ('expexpressionowner', (YLeaf(YType.str, 'expExpressionOwner'), ['str'])),
                ])
                self.expexpressionindex = None
                self.expexpressionname = None
                self.expexpression = None
                self.expexpressionvaluetype = None
                self.expexpressioncomment = None
                self.expexpressiondeltainterval = None
                self.expexpressionprefix = None
                self.expexpressionerrors = None
                self.expexpressionerrortime = None
                self.expexpressionerrorindex = None
                self.expexpressionerror = None
                self.expexpressioninstance = None
                self.expexpressionowner = None
                self._segment_path = lambda: "expExpressionEntry" + "[expExpressionIndex='" + str(self.expexpressionindex) + "']"
                self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/expExpressionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EXPRESSIONMIB.ExpExpressionTable.ExpExpressionEntry, ['expexpressionindex', 'expexpressionname', 'expexpression', 'expexpressionvaluetype', 'expexpressioncomment', 'expexpressiondeltainterval', 'expexpressionprefix', 'expexpressionerrors', 'expexpressionerrortime', 'expexpressionerrorindex', 'expexpressionerror', 'expexpressioninstance', 'expexpressionowner'], name, value)

            class ExpExpressionError(Enum):
                """
                ExpExpressionError (Enum Class)

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


            class ExpExpressionValueType(Enum):
                """
                ExpExpressionValueType (Enum Class)

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





    class ExpObjectTable(Entity):
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
        	**type**\: list of  		 :py:class:`ExpObjectEntry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpObjectTable, self).__init__()

            self.yang_name = "expObjectTable"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("expObjectEntry", ("expobjectentry", EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry))])
            self._leafs = OrderedDict()

            self.expobjectentry = YList(self)
            self._segment_path = lambda: "expObjectTable"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpObjectTable, [], name, value)


        class ExpObjectEntry(Entity):
            """
            Information about an object.  An application uses
            expObjectStatus to create entries in this table while
            in the process of defining an expression.
            
            Values of read\-create objects in this table may be
            changed at any time.
            
            .. attribute:: expexpressionindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNameTable.ExpNameEntry>`
            
            	**config**\: False
            
            .. attribute:: expobjectindex  (key)
            
            	Within an expression, a unique, numeric identification for an object.  Prefixed with a dollar sign ('$') this is used to reference the object in the corresponding expExpression
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: expobjectid
            
            	The OBJECT IDENTIFIER (OID) of this object.  The OID may be fully qualified, meaning it includes a complete instance identifier part (e.g., ifInOctets.1 or sysUpTime.0), or it may not be fully qualified, meaning it may lack all or part of the instance identifier.  If the expObjectID is not fully qualified, then expObjectWildcard must be set to true(1).   The value of the expression will be multiple values, as if done for a GetNext sweep of the object.  An object here may itself be the result of an expression but recursion is not allowed.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expobjectidwildcard
            
            	A true value indicates the expObjecID of this row is a wildcard object. False indicates that expObjectID is fully instanced.  If all expObjectWildcard values for a given expression are FALSE, expExpressionPrefix will reflect a scalar object (ie will be 0.0).  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: expobjectsampletype
            
            	The method of sampling the selected variable.  An 'absoluteValue' is simply the present value of the object. A 'deltaValue' is the present value minus the previous value, which was sampled expExpressionDeltaInterval seconds ago.  This is intended primarily for use with SNMP counters, which are meaningless as an 'absoluteValue', but may be used with any integer\-based value.  When an expression contains both delta and absolute values the absolute values are obtained at the end of the delta period
            	**type**\:  :py:class:`ExpObjectSampleType <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry.ExpObjectSampleType>`
            
            	**config**\: False
            
            .. attribute:: expobjectdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks or TimeStamp object that indicates a discontinuity in the value at expObjectID.  This object is not instantiated if expObject is not 'deltaValue'.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match expObjectID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking must still check sysUpTime for an overall discontinuity.  If the object identified is not accessible no discontinuity check will be made
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expobjectdiscontinuityidwildcard
            
            	A true value indicates the expObjectDeltaDiscontinuityID of this row is a wildcard object.  False indicates that expObjectDeltaDiscontinuityID is fully instanced.  This object is not instantiated if expObject is not 'deltaValue'.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: expobjectdiscontinuityidtype
            
            	The value 'timeTicks' indicates the expObjectDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates that expObjectDeltaDiscontinuityID is of syntax TimeStamp.  This object is not instantiated if expObject is not 'deltaValue'
            	**type**\:  :py:class:`ExpObjectDiscontinuityIDType <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry.ExpObjectDiscontinuityIDType>`
            
            	**config**\: False
            
            .. attribute:: expobjectconditional
            
            	The OBJECT IDENTIFIER (OID) of an object that overrides whether the instance of expObjectID is to be considered usable.  If the value of the object at expObjectConditional is 0 or not instantiated, the object at expObjectID is treated as if it is not instantiated.  In other words, expObjectConditional is a filter that controls whether or not to use the value at expObjectID.  The OID may be for a leaf object (e.g. sysObjectID.0) or may be wildcarded to match expObjectID.  If expObject is wildcarded and expObjectID in the same row is not, the wild portion of expObjectConditional must match the wildcarding of the rest of the expression.  If no object in the expression is wildcarded but expObjectConditional is, use the lexically first instance (if any) of expObjectConditional.  If the value of expObjectConditional is 0.0 operation is as if the value pointed to by expObjectConditional is a non\-zero (true) value.  Note that expObjectConditional can not trivially use an object of syntax TruthValue, since the underlying value is not 0 or 1
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expobjectconditionalwildcard
            
            	A true value indicates the expObjectConditional of this row is a wildcard object. False indicates that expObjectConditional is fully instanced.  NOTE\: The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: expobjectstatus
            
            	The control that allows creation/deletion of entries.  Objects in this table may be changed while expObjectStatus is in any state
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry, self).__init__()

                self.yang_name = "expObjectEntry"
                self.yang_parent_name = "expObjectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionindex','expobjectindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionindex', (YLeaf(YType.str, 'expExpressionIndex'), ['int'])),
                    ('expobjectindex', (YLeaf(YType.uint32, 'expObjectIndex'), ['int'])),
                    ('expobjectid', (YLeaf(YType.str, 'expObjectID'), ['str'])),
                    ('expobjectidwildcard', (YLeaf(YType.boolean, 'expObjectIDWildcard'), ['bool'])),
                    ('expobjectsampletype', (YLeaf(YType.enumeration, 'expObjectSampleType'), [('ydk.models.cisco_ios_xe.EXPRESSION_MIB', 'EXPRESSIONMIB', 'ExpObjectTable.ExpObjectEntry.ExpObjectSampleType')])),
                    ('expobjectdeltadiscontinuityid', (YLeaf(YType.str, 'expObjectDeltaDiscontinuityID'), ['str'])),
                    ('expobjectdiscontinuityidwildcard', (YLeaf(YType.boolean, 'expObjectDiscontinuityIDWildcard'), ['bool'])),
                    ('expobjectdiscontinuityidtype', (YLeaf(YType.enumeration, 'expObjectDiscontinuityIDType'), [('ydk.models.cisco_ios_xe.EXPRESSION_MIB', 'EXPRESSIONMIB', 'ExpObjectTable.ExpObjectEntry.ExpObjectDiscontinuityIDType')])),
                    ('expobjectconditional', (YLeaf(YType.str, 'expObjectConditional'), ['str'])),
                    ('expobjectconditionalwildcard', (YLeaf(YType.boolean, 'expObjectConditionalWildcard'), ['bool'])),
                    ('expobjectstatus', (YLeaf(YType.enumeration, 'expObjectStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.expexpressionindex = None
                self.expobjectindex = None
                self.expobjectid = None
                self.expobjectidwildcard = None
                self.expobjectsampletype = None
                self.expobjectdeltadiscontinuityid = None
                self.expobjectdiscontinuityidwildcard = None
                self.expobjectdiscontinuityidtype = None
                self.expobjectconditional = None
                self.expobjectconditionalwildcard = None
                self.expobjectstatus = None
                self._segment_path = lambda: "expObjectEntry" + "[expExpressionIndex='" + str(self.expexpressionindex) + "']" + "[expObjectIndex='" + str(self.expobjectindex) + "']"
                self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/expObjectTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EXPRESSIONMIB.ExpObjectTable.ExpObjectEntry, ['expexpressionindex', 'expobjectindex', 'expobjectid', 'expobjectidwildcard', 'expobjectsampletype', 'expobjectdeltadiscontinuityid', 'expobjectdiscontinuityidwildcard', 'expobjectdiscontinuityidtype', 'expobjectconditional', 'expobjectconditionalwildcard', 'expobjectstatus'], name, value)

            class ExpObjectDiscontinuityIDType(Enum):
                """
                ExpObjectDiscontinuityIDType (Enum Class)

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


            class ExpObjectSampleType(Enum):
                """
                ExpObjectSampleType (Enum Class)

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





    class ExpValueTable(Entity):
        """
        A table of values from evaluated expressions.
        
        .. attribute:: expvalueentry
        
        	A single value from an evaluated expression.  For a given instance, only one 'Val' object in the conceptual row will be instantiated, that is, the one with the appropriate type for the value.  For values that contain no objects of  expObjectSampleType 'deltaValue', reading a value from the table causes the evaluation of the expression for that value.  For those that contain a 'deltaValue' the value read is as of the last delta interval.  If in the attempt to evaluate the expression one or more of the necessary objects is not available, the corresponding entry in this table is effectively not instantiated.  To maintain security of MIB information, expression evaluation must take place using security credentials for the implied Gets of the objects in the expression.  For expressions with no deltaValue those security credentials are the ones that came with the Get\* for the value.  For expressions with a deltaValue the ongoing expression evaluation is under the security credentials of the creator of the corresponding expNameEntry
        	**type**\: list of  		 :py:class:`ExpValueEntry <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpValueTable.ExpValueEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'EXPRESSION-MIB'
        _revision = '2005-11-24'

        def __init__(self):
            super(EXPRESSIONMIB.ExpValueTable, self).__init__()

            self.yang_name = "expValueTable"
            self.yang_parent_name = "EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("expValueEntry", ("expvalueentry", EXPRESSIONMIB.ExpValueTable.ExpValueEntry))])
            self._leafs = OrderedDict()

            self.expvalueentry = YList(self)
            self._segment_path = lambda: "expValueTable"
            self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EXPRESSIONMIB.ExpValueTable, [], name, value)


        class ExpValueEntry(Entity):
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
            
            .. attribute:: expexpressionindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`expexpressionindex <ydk.models.cisco_ios_xe.EXPRESSION_MIB.EXPRESSIONMIB.ExpNameTable.ExpNameEntry>`
            
            	**config**\: False
            
            .. attribute:: expvalueinstance  (key)
            
            	The final instance portion of a value's OID according to the wildcarding in instances of expObjectID for the expression.  The prefix of this OID fragment is 0.0, leading to the following behavior.  If there is no wildcarding, the value is 0.0.0.  In other words, there is one value which standing alone would have been a scalar with a 0 at the end of its OID.  If there is wildcarding, the value is 0.0 followed by a value that the wildcard can take, thus defining one value instance for each real, possible value of the wildcard. So, for example, if the wildcard worked out to be an ifIndex, there is an expValueInstance for each applicable ifIndex
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expvaluecounter32val
            
            	The value when expExpressionValueType is 'counter32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: expvalueunsigned32val
            
            	The value when expExpressionValueType is 'unsignedOrGauge32' or 'timeTicks'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: expvalueinteger32val
            
            	The value when expExpressionValueType is 'integer32'
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: expvalueipaddressval
            
            	The value when expExpressionValueType is 'ipAddress'
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: expvalueoctetstringval
            
            	The value when expExpressionValueType is 'octetString'
            	**type**\: str
            
            	**length:** 0..65535
            
            	**config**\: False
            
            .. attribute:: expvalueoidval
            
            	The value when expExpressionValueType is 'objectId'
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: expvaluecounter64val
            
            	The value when expExpressionValueType is 'counter64'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'EXPRESSION-MIB'
            _revision = '2005-11-24'

            def __init__(self):
                super(EXPRESSIONMIB.ExpValueTable.ExpValueEntry, self).__init__()

                self.yang_name = "expValueEntry"
                self.yang_parent_name = "expValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionindex','expvalueinstance']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionindex', (YLeaf(YType.str, 'expExpressionIndex'), ['int'])),
                    ('expvalueinstance', (YLeaf(YType.str, 'expValueInstance'), ['str'])),
                    ('expvaluecounter32val', (YLeaf(YType.uint32, 'expValueCounter32Val'), ['int'])),
                    ('expvalueunsigned32val', (YLeaf(YType.uint32, 'expValueUnsigned32Val'), ['int'])),
                    ('expvalueinteger32val', (YLeaf(YType.int32, 'expValueInteger32Val'), ['int'])),
                    ('expvalueipaddressval', (YLeaf(YType.str, 'expValueIpAddressVal'), ['str'])),
                    ('expvalueoctetstringval', (YLeaf(YType.str, 'expValueOctetStringVal'), ['str'])),
                    ('expvalueoidval', (YLeaf(YType.str, 'expValueOidVal'), ['str'])),
                    ('expvaluecounter64val', (YLeaf(YType.uint64, 'expValueCounter64Val'), ['int'])),
                ])
                self.expexpressionindex = None
                self.expvalueinstance = None
                self.expvaluecounter32val = None
                self.expvalueunsigned32val = None
                self.expvalueinteger32val = None
                self.expvalueipaddressval = None
                self.expvalueoctetstringval = None
                self.expvalueoidval = None
                self.expvaluecounter64val = None
                self._segment_path = lambda: "expValueEntry" + "[expExpressionIndex='" + str(self.expexpressionindex) + "']" + "[expValueInstance='" + str(self.expvalueinstance) + "']"
                self._absolute_path = lambda: "EXPRESSION-MIB:EXPRESSION-MIB/expValueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EXPRESSIONMIB.ExpValueTable.ExpValueEntry, ['expexpressionindex', 'expvalueinstance', 'expvaluecounter32val', 'expvalueunsigned32val', 'expvalueinteger32val', 'expvalueipaddressval', 'expvalueoctetstringval', 'expvalueoidval', 'expvaluecounter64val'], name, value)



    def clone_ptr(self):
        self._top_entity = EXPRESSIONMIB()
        return self._top_entity




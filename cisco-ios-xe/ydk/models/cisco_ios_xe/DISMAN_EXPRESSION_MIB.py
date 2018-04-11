""" DISMAN_EXPRESSION_MIB 

The MIB module for defining expressions of MIB objects for
management purposes.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DISMANEXPRESSIONMIB(Entity):
    """
    
    
    .. attribute:: expresource
    
    	
    	**type**\:  :py:class:`Expresource <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expresource>`
    
    .. attribute:: expexpressiontable
    
    	A table of expression definitions
    	**type**\:  :py:class:`Expexpressiontable <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable>`
    
    .. attribute:: experrortable
    
    	A table of expression errors
    	**type**\:  :py:class:`Experrortable <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Experrortable>`
    
    .. attribute:: expobjecttable
    
    	A table of object definitions for each expExpression.  Wildcarding instance IDs\:  It is legal to omit all or part of the instance portion for some or all of the objects in an expression. (See the DESCRIPTION of expObjectID for details.  However, note that if more than one object in the same expression is wildcarded in this way, they all must be objects where that portion of the instance is the same.  In other words, all objects may be in the same SEQUENCE or in different SEQUENCEs but with the same semantic index value (e.g., a value of ifIndex) for the wildcarded portion
    	**type**\:  :py:class:`Expobjecttable <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expobjecttable>`
    
    .. attribute:: expvaluetable
    
    	A table of values from evaluated expressions
    	**type**\:  :py:class:`Expvaluetable <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expvaluetable>`
    
    

    """

    _prefix = 'DISMAN-EXPRESSION-MIB'
    _revision = '2000-10-16'

    def __init__(self):
        super(DISMANEXPRESSIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DISMAN-EXPRESSION-MIB"
        self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("expResource", ("expresource", DISMANEXPRESSIONMIB.Expresource)), ("expExpressionTable", ("expexpressiontable", DISMANEXPRESSIONMIB.Expexpressiontable)), ("expErrorTable", ("experrortable", DISMANEXPRESSIONMIB.Experrortable)), ("expObjectTable", ("expobjecttable", DISMANEXPRESSIONMIB.Expobjecttable)), ("expValueTable", ("expvaluetable", DISMANEXPRESSIONMIB.Expvaluetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.expresource = DISMANEXPRESSIONMIB.Expresource()
        self.expresource.parent = self
        self._children_name_map["expresource"] = "expResource"
        self._children_yang_names.add("expResource")

        self.expexpressiontable = DISMANEXPRESSIONMIB.Expexpressiontable()
        self.expexpressiontable.parent = self
        self._children_name_map["expexpressiontable"] = "expExpressionTable"
        self._children_yang_names.add("expExpressionTable")

        self.experrortable = DISMANEXPRESSIONMIB.Experrortable()
        self.experrortable.parent = self
        self._children_name_map["experrortable"] = "expErrorTable"
        self._children_yang_names.add("expErrorTable")

        self.expobjecttable = DISMANEXPRESSIONMIB.Expobjecttable()
        self.expobjecttable.parent = self
        self._children_name_map["expobjecttable"] = "expObjectTable"
        self._children_yang_names.add("expObjectTable")

        self.expvaluetable = DISMANEXPRESSIONMIB.Expvaluetable()
        self.expvaluetable.parent = self
        self._children_name_map["expvaluetable"] = "expValueTable"
        self._children_yang_names.add("expValueTable")
        self._segment_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB"


    class Expresource(Entity):
        """
        
        
        .. attribute:: expresourcedeltaminimum
        
        	The minimum expExpressionDeltaInterval this system will accept.  A system may use the larger values of this minimum to lessen the impact of constantly computing deltas.  For larger delta sampling intervals the system samples less often and suffers less overhead.  This object provides a way to enforce such lower overhead for all expressions created after it is set.  The value \-1 indicates that expResourceDeltaMinimum is irrelevant as the system will not accept 'deltaValue' as a value for expObjectSampleType.  Unless explicitly resource limited, a system's value for this object should be 1, allowing as small as a 1 second interval for ongoing delta sampling.  Changing this value will not invalidate an existing setting of expObjectSampleType
        	**type**\: int
        
        	**range:** \-1..None \| 1..600
        
        	**units**\: seconds
        
        .. attribute:: expresourcedeltawildcardinstancemaximum
        
        	For every instance of a deltaValue object, one dynamic instance entry is needed for holding the instance value from the previous sample, i.e. to maintain state.  This object limits maximum number of dynamic instance entries this system will support for wildcarded delta objects in expressions. For a given delta expression, the number of dynamic instances is the number of values that meet all criteria to exist times the number of delta values in the expression.  A value of 0 indicates no preset limit, that is, the limit is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for this object should be 0.  Changing this value will not eliminate or inhibit existing delta wildcard instance objects but will prevent the creation of more such objects.  An attempt to allocate beyond the limit results in expErrorCode being tooManyWildcardValues for that evaluation attempt
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstances
        
        	The number of currently active instance entries as defined for expResourceDeltaWildcardInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceshigh
        
        	The highest value of expResourceDeltaWildcardInstances that has occurred since initialization of the managed system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        .. attribute:: expresourcedeltawildcardinstanceresourcelacks
        
        	The number of times this system could not evaluate an expression because that would have created a value instance in excess of expResourceDeltaWildcardInstanceMaximum
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: instances
        
        

        """

        _prefix = 'DISMAN-EXPRESSION-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEXPRESSIONMIB.Expresource, self).__init__()

            self.yang_name = "expResource"
            self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('expresourcedeltaminimum', YLeaf(YType.int32, 'expResourceDeltaMinimum')),
                ('expresourcedeltawildcardinstancemaximum', YLeaf(YType.uint32, 'expResourceDeltaWildcardInstanceMaximum')),
                ('expresourcedeltawildcardinstances', YLeaf(YType.uint32, 'expResourceDeltaWildcardInstances')),
                ('expresourcedeltawildcardinstanceshigh', YLeaf(YType.uint32, 'expResourceDeltaWildcardInstancesHigh')),
                ('expresourcedeltawildcardinstanceresourcelacks', YLeaf(YType.uint32, 'expResourceDeltaWildcardInstanceResourceLacks')),
            ])
            self.expresourcedeltaminimum = None
            self.expresourcedeltawildcardinstancemaximum = None
            self.expresourcedeltawildcardinstances = None
            self.expresourcedeltawildcardinstanceshigh = None
            self.expresourcedeltawildcardinstanceresourcelacks = None
            self._segment_path = lambda: "expResource"
            self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEXPRESSIONMIB.Expresource, ['expresourcedeltaminimum', 'expresourcedeltawildcardinstancemaximum', 'expresourcedeltawildcardinstances', 'expresourcedeltawildcardinstanceshigh', 'expresourcedeltawildcardinstanceresourcelacks'], name, value)


    class Expexpressiontable(Entity):
        """
        A table of expression definitions.
        
        .. attribute:: expexpressionentry
        
        	Information about a single expression.  New expressions can be created using expExpressionRowStatus.  To create an expression first create the named entry in this table.  Then use expExpressionName to populate expObjectTable. For expression evaluation to succeed all related entries in expExpressionTable and expObjectTable must be 'active'.  If these conditions are not met the corresponding values in expValue simply are not instantiated.  Deleting an entry deletes all related entries in expObjectTable and expErrorTable.  Because of the relationships among the multiple tables for an expression (expExpressionTable, expObjectTable, and expValueTable) and the SNMP rules for independence in setting object values, it is necessary to do final error checking when an expression is evaluated, that is, when one of its instances in expValueTable is read or a delta interval expires.  Earlier checking need not be done and an implementation may not impose any ordering on the creation of objects related to an expression.  To maintain security of MIB information, when creating a new row in this table, the managed system must record the security credentials of the requester.  These security credentials are the parameters necessary as inputs to isAccessAllowed from the Architecture for  Describing SNMP Management Frameworks.  When obtaining the objects that make up the expression, the system must (conceptually) use isAccessAllowed to ensure that it does not violate security.  The evaluation of the expression takes place under the security credentials of the creator of its expExpressionEntry.  Values of read\-write objects in this table may be changed at any time
        	**type**\: list of  		 :py:class:`Expexpressionentry <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
        
        

        """

        _prefix = 'DISMAN-EXPRESSION-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEXPRESSIONMIB.Expexpressiontable, self).__init__()

            self.yang_name = "expExpressionTable"
            self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("expExpressionEntry", ("expexpressionentry", DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry))])
            self._leafs = OrderedDict()

            self.expexpressionentry = YList(self)
            self._segment_path = lambda: "expExpressionTable"
            self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEXPRESSIONMIB.Expexpressiontable, [], name, value)


        class Expexpressionentry(Entity):
            """
            Information about a single expression.  New expressions
            can be created using expExpressionRowStatus.
            
            To create an expression first create the named entry in this
            table.  Then use expExpressionName to populate expObjectTable.
            For expression evaluation to succeed all related entries in
            expExpressionTable and expObjectTable must be 'active'.  If
            these conditions are not met the corresponding values in
            expValue simply are not instantiated.
            
            Deleting an entry deletes all related entries in expObjectTable
            and expErrorTable.
            
            Because of the relationships among the multiple tables for an
            expression (expExpressionTable, expObjectTable, and
            expValueTable) and the SNMP rules for independence in setting
            object values, it is necessary to do final error checking when
            an expression is evaluated, that is, when one of its instances
            in expValueTable is read or a delta interval expires.  Earlier
            checking need not be done and an implementation may not impose
            any ordering on the creation of objects related to an
            expression.
            
            To maintain security of MIB information, when creating a new row in
            this table, the managed system must record the security credentials
            of the requester.  These security credentials are the parameters
            necessary as inputs to isAccessAllowed from the Architecture for
            
            Describing SNMP Management Frameworks.  When obtaining the objects
            that make up the expression, the system must (conceptually) use
            isAccessAllowed to ensure that it does not violate security.
            
            The evaluation of the expression takes place under the
            security credentials of the creator of its expExpressionEntry.
            
            Values of read\-write objects in this table may be changed
            at any time.
            
            .. attribute:: expexpressionowner  (key)
            
            	The owner of this entry. The exact semantics of this string are subject to the security policy defined by the security administrator
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: expexpressionname  (key)
            
            	The name of the expression.  This is locally unique, within the scope of an expExpressionOwner
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: expexpression
            
            	The expression to be evaluated.  This object is the same as a DisplayString (RFC 1903) except for its maximum length.  Except for the variable names the expression is in ANSI C syntax.  Only the subset of ANSI C operators and functions listed here is allowed.  Variables are expressed as a dollar sign ('$') and an integer that corresponds to an expObjectIndex.  An example of a valid expression is\:       ($1\-$5)\*100  Expressions must not be recursive, that is although an expression may use the results of another expression, it must not contain any variable that is directly or indirectly a result of its own evaluation. The managed system must check for recursive expressions.  The only allowed operators are\:       ( )      \- (unary)      + \- \* / %      & \| ^ << >> ~      ! && \|\| == != > >= < <=  Note the parentheses are included for parenthesizing the expression, not for casting data types.  The only constant types defined are\:       int (32\-bit signed)      long (64\-bit signed)      unsigned int      unsigned long      hexadecimal      character      string      oid  The default type for a positive integer is int unless it is too large in which case it is long.  All but oid are as defined for ANSI C.  Note that a hexadecimal constant may end up as a scalar or an array of 8\-bit integers.  A string constant is enclosed in double quotes and may contain back\-slashed individual characters as in ANSI C.  An oid constant comprises 32\-bit, unsigned integers and at least one period, for example\:       0.      .0      1.3.6.1  No additional leading or trailing subidentifiers are automatically added to an OID constant.  The constant is taken as expressed.  Integer\-typed objects are treated as 32\- or 64\-bit, signed or unsigned integers, as appropriate.  The results of mixing them are as for ANSI C, including the type of the result.  Note that a 32\-bit value is thus promoted to 64 bits only in an operation with a 64\-bit value.  There is no provision for larger values to handle overflow.  Relative to SNMP data types, a resulting value becomes unsigned when calculating it uses any unsigned value, including a counter.  To force the final value to be of data type counter the expression must explicitly use the counter32() or counter64() function (defined below).  OCTET STRINGS and OBJECT IDENTIFIERs are treated as one\-dimensioned arrays of unsigned 8\-bit integers and unsigned 32\-bit integers, respectively.  IpAddresses are treated as 32\-bit, unsigned integers in network byte order, that is, the hex version of 255.0.0.0 is 0xff000000.  Conditional expressions result in a 32\-bit, unsigned integer of value 0 for false or 1 for true. When an arbitrary value is used as a boolean 0 is false and non\-zero is true.  Rules for the resulting data type from an operation, based on the operator\:  For << and >> the result is the same as the left hand operand.  For &&, \|\|, ==, !=, <, <=, >, and >= the result is always Unsigned32.  For unary \- the result is always Integer32.  For +, \-, \*, /, %, &, \|, and ^ the result is promoted according to the following rules, in order from most to least preferred\:       If left hand and right hand operands are the same type,      use that.       If either side is Counter64, use that.       If either side is IpAddress, use that.       If either side is TimeTicks, use that.       If either side is Counter32, use that.       Otherwise use Unsigned32.  The following rules say what operators apply with what data types.  Any combination not explicitly defined does not work.  For all operators any of the following can be the left hand or right hand operand\: Integer32, Counter32, Unsigned32, Counter64.  The operators +, \-, \*, /, %, <, <=, >, and >= work with TimeTicks.  The operators &, \|, and ^ work with IpAddress.  The operators << and >> work with IpAddress but only as the left hand operand.  The + operator performs a concatenation of two OCTET STRINGs or two OBJECT IDENTIFIERs.  The operators &, \| perform bitwise operations on OCTET STRINGs. If the OCTET STRING happens to be a DisplayString the results may be meaningless, but the agent system does not check this as some such systems do not have this information.  The operators << and >> perform bitwise operations on OCTET STRINGs appearing as the left hand operand.  The only functions defined are\:       counter32      counter64      arraySection      stringBegins      stringEnds      stringContains      oidBegins      oidEnds      oidContains      average      maximum      minimum      sum      exists  The following function definitions indicate their parameters by naming the data type of the parameter in the parameter's position in the parameter list.  The parameter must be of the type indicated and generally may be a constant, a MIB object, a function, or an expression.  counter32(integer) \- wrapped around an integer value counter32 forces Counter32 as a data type.  counter64(integer) \- similar to counter32 except that the resulting data type is 'counter64'.  arraySection(array, integer, integer) \- selects a piece of an array (i.e. part of an OCTET STRING or OBJECT IDENTIFIER).  The integer arguments are in the range 0 to 4,294,967,295.  The first is an initial array index (one\-dimensioned) and the second is an ending array index.  A value of 0 indicates first or last element, respectively.  If the first element is larger than the array length the result is 0 length.  If the second integer is less than or equal to the first, the result is 0 length.  If the second is larger than the array length it indicates last element.  stringBegins/Ends/Contains(octetString, octetString) \- looks for the second string (which can be a string constant) in the first and returns the one\-dimensioned arrayindex where the match began. A return value of 0 indicates no match (i.e. boolean false).  oidBegins/Ends/Contains(oid, oid) \- looks for the second OID (which can be an OID constant) in the first and returns the the one\-dimensioned index where the match began. A return value of 0 indicates no match (i.e. boolean false).  average/maximum/minimum(integer) \- calculates the average, minimum, or maximum value of the integer valued object over multiple sample times.  If the object disappears for any sample period, the accumulation and the resulting value object cease to exist until the object reappears at which point the calculation starts over.  sum(integerObject\*) \- sums all available values of the wildcarded integer object, resulting in an integer scalar.  Must be used with caution as it wraps on overflow with no notification.  exists(anyTypeObject) \- verifies the object instance exists. A return value of 0 indicates NoSuchInstance (i.e. boolean false)
            	**type**\: str
            
            	**length:** 1..1024
            
            .. attribute:: expexpressionvaluetype
            
            	The type of the expression value.  One and only one of the value objects in expValueTable will be instantiated to match this type.  If the result of the expression can not be made into this type, an invalidOperandType error will occur
            	**type**\:  :py:class:`Expexpressionvaluetype <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry.Expexpressionvaluetype>`
            
            .. attribute:: expexpressioncomment
            
            	A comment to explain the use or meaning of the expression
            	**type**\: str
            
            .. attribute:: expexpressiondeltainterval
            
            	Sampling interval for objects in this expression with expObjectSampleType 'deltaValue'.  This object has no effect if the the expression has no deltaValue objects.  A value of 0 indicates no automated sampling.  In this case the delta is the difference from the last time the expression was evaluated.  Note that this is subject to unpredictable delta times in the face of retries or multiple managers.  A value greater than zero is the number of seconds between automated samples.  Until the delta interval has expired once the delta for the object is effectively not instantiated and evaluating the expression has results as if the object itself were not instantiated.  Note that delta values potentially consume large amounts of system CPU and memory.  Delta state and processing must continue constantly even if the expression is not being used. That is, the expression is being evaluated every delta interval, even if no application is reading those values.  For wildcarded objects this can be substantial overhead.  Note that delta intervals, external expression value sampling intervals and delta intervals for expressions within other expressions can have unusual interactions as they are impossible to synchronize accurately.  In general one interval embedded below another must be enough shorter that the higher sample sees relatively smooth, predictable behavior.  So, for example, to avoid the higher level getting the same sample twice, the lower level should sample at least twice as fast as the higher level does
            	**type**\: int
            
            	**range:** 0..86400
            
            	**units**\: seconds
            
            .. attribute:: expexpressionprefix
            
            	An object prefix to assist an application in determining the instance indexing to use in expValueTable, relieving the application of the need to scan the expObjectTable to determine such a prefix.  See expObjectTable for information on wildcarded objects.  If the expValueInstance portion of the value OID may be treated as a scalar (that is, normally, 0) the value of expExpressionPrefix is zero length, that is, no OID at all. Note that zero length implies a null OID, not the OID 0.0.  Otherwise, the value of expExpressionPrefix is the expObjectID value of any one of the wildcarded objects for the expression. This is sufficient, as the remainder, that is, the instance fragment relevant to instancing the values, must be the same for all wildcarded objects in the expression
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expexpressionerrors
            
            	The number of errors encountered while evaluating this expression.  Note that an object in the expression not being accessible, is not considered an error. An example of an inaccessible object is when the object is excluded from the view of the user whose security credentials are used in the expression evaluation. In such cases, it is a legitimate condition that causes the corresponding expression value not to be instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: expexpressionentrystatus
            
            	The control that allows creation and deletion of entries
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DISMAN-EXPRESSION-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry, self).__init__()

                self.yang_name = "expExpressionEntry"
                self.yang_parent_name = "expExpressionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionowner','expexpressionname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionowner', YLeaf(YType.str, 'expExpressionOwner')),
                    ('expexpressionname', YLeaf(YType.str, 'expExpressionName')),
                    ('expexpression', YLeaf(YType.str, 'expExpression')),
                    ('expexpressionvaluetype', YLeaf(YType.enumeration, 'expExpressionValueType')),
                    ('expexpressioncomment', YLeaf(YType.str, 'expExpressionComment')),
                    ('expexpressiondeltainterval', YLeaf(YType.int32, 'expExpressionDeltaInterval')),
                    ('expexpressionprefix', YLeaf(YType.str, 'expExpressionPrefix')),
                    ('expexpressionerrors', YLeaf(YType.uint32, 'expExpressionErrors')),
                    ('expexpressionentrystatus', YLeaf(YType.enumeration, 'expExpressionEntryStatus')),
                ])
                self.expexpressionowner = None
                self.expexpressionname = None
                self.expexpression = None
                self.expexpressionvaluetype = None
                self.expexpressioncomment = None
                self.expexpressiondeltainterval = None
                self.expexpressionprefix = None
                self.expexpressionerrors = None
                self.expexpressionentrystatus = None
                self._segment_path = lambda: "expExpressionEntry" + "[expExpressionOwner='" + str(self.expexpressionowner) + "']" + "[expExpressionName='" + str(self.expexpressionname) + "']"
                self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/expExpressionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry, ['expexpressionowner', 'expexpressionname', 'expexpression', 'expexpressionvaluetype', 'expexpressioncomment', 'expexpressiondeltainterval', 'expexpressionprefix', 'expexpressionerrors', 'expexpressionentrystatus'], name, value)

            class Expexpressionvaluetype(Enum):
                """
                Expexpressionvaluetype (Enum Class)

                The type of the expression value.  One and only one of the

                value objects in expValueTable will be instantiated to match

                this type.

                If the result of the expression can not be made into this type,

                an invalidOperandType error will occur.

                .. data:: counter32 = 1

                .. data:: unsigned32 = 2

                .. data:: timeTicks = 3

                .. data:: integer32 = 4

                .. data:: ipAddress = 5

                .. data:: octetString = 6

                .. data:: objectId = 7

                .. data:: counter64 = 8

                """

                counter32 = Enum.YLeaf(1, "counter32")

                unsigned32 = Enum.YLeaf(2, "unsigned32")

                timeTicks = Enum.YLeaf(3, "timeTicks")

                integer32 = Enum.YLeaf(4, "integer32")

                ipAddress = Enum.YLeaf(5, "ipAddress")

                octetString = Enum.YLeaf(6, "octetString")

                objectId = Enum.YLeaf(7, "objectId")

                counter64 = Enum.YLeaf(8, "counter64")



    class Experrortable(Entity):
        """
        A table of expression errors.
        
        .. attribute:: experrorentry
        
        	Information about errors in processing an expression.  Entries appear in this table only when there is a matching expExpressionEntry and then only when there has been an error for that expression as reflected by the error codes defined for expErrorCode
        	**type**\: list of  		 :py:class:`Experrorentry <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Experrortable.Experrorentry>`
        
        

        """

        _prefix = 'DISMAN-EXPRESSION-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEXPRESSIONMIB.Experrortable, self).__init__()

            self.yang_name = "expErrorTable"
            self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("expErrorEntry", ("experrorentry", DISMANEXPRESSIONMIB.Experrortable.Experrorentry))])
            self._leafs = OrderedDict()

            self.experrorentry = YList(self)
            self._segment_path = lambda: "expErrorTable"
            self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEXPRESSIONMIB.Experrortable, [], name, value)


        class Experrorentry(Entity):
            """
            Information about errors in processing an expression.
            
            Entries appear in this table only when there is a matching
            expExpressionEntry and then only when there has been an
            error for that expression as reflected by the error codes
            defined for expErrorCode.
            
            .. attribute:: expexpressionowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`expexpressionowner <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: expexpressionname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`expexpressionname <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: experrortime
            
            	The value of sysUpTime the last time an error caused a failure to evaluate this expression
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: experrorindex
            
            	The one\-dimensioned character array index into expExpression for where the error occurred.  The value zero indicates irrelevance
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: experrorcode
            
            	The error that occurred.  In the following explanations the expected timing of the error is in parentheses.  'S' means the error occurs on a Set request.  'E' means the error occurs on the attempt to evaluate the expression either due to Get from expValueTable or in ongoing delta processing.  invalidSyntax       the value sent for expExpression is not                valid Expression MIB expression syntax                (S) undefinedObjectIndex     an object reference ($n) in                expExpression does not have a matching                instance in expObjectTable (E) unrecognizedOperator     the value sent for expExpression held an                unrecognized operator (S) unrecognizedFunction     the value sent for expExpression held an                unrecognized function name (S) invalidOperandType  an operand in expExpression is not the                right type for the associated operator                or result (SE) unmatchedParenthesis     the value sent for expExpression is not                correctly parenthesized (S) tooManyWildcardValues    evaluating the expression exceeded the                limit set by                expResourceDeltaWildcardInstanceMaximum                (E) recursion      through some chain of embedded                expressions the expression invokes itself                (E) deltaTooShort       the delta for the next evaluation passed                before the system could evaluate the                present sample (E) resourceUnavailable some resource, typically dynamic memory,                was unavailable (SE) divideByZero        an attempt to divide by zero occurred                (E)  For the errors that occur when the attempt is made to set expExpression Set request fails with the SNMP error code 'wrongValue'.  Such failures refer to the most recent failure to Set expExpression, not to the present value of expExpression which must be either unset or syntactically correct.  Errors that occur during evaluation for a Get\* operation return the SNMP error code 'genErr' except for 'tooManyWildcardValues' and 'resourceUnavailable' which return the SNMP error code 'resourceUnavailable'
            	**type**\:  :py:class:`Experrorcode <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Experrortable.Experrorentry.Experrorcode>`
            
            .. attribute:: experrorinstance
            
            	The expValueInstance being evaluated when the error occurred.  A zero\-length indicates irrelevance
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'DISMAN-EXPRESSION-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEXPRESSIONMIB.Experrortable.Experrorentry, self).__init__()

                self.yang_name = "expErrorEntry"
                self.yang_parent_name = "expErrorTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionowner','expexpressionname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionowner', YLeaf(YType.str, 'expExpressionOwner')),
                    ('expexpressionname', YLeaf(YType.str, 'expExpressionName')),
                    ('experrortime', YLeaf(YType.uint32, 'expErrorTime')),
                    ('experrorindex', YLeaf(YType.int32, 'expErrorIndex')),
                    ('experrorcode', YLeaf(YType.enumeration, 'expErrorCode')),
                    ('experrorinstance', YLeaf(YType.str, 'expErrorInstance')),
                ])
                self.expexpressionowner = None
                self.expexpressionname = None
                self.experrortime = None
                self.experrorindex = None
                self.experrorcode = None
                self.experrorinstance = None
                self._segment_path = lambda: "expErrorEntry" + "[expExpressionOwner='" + str(self.expexpressionowner) + "']" + "[expExpressionName='" + str(self.expexpressionname) + "']"
                self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/expErrorTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEXPRESSIONMIB.Experrortable.Experrorentry, ['expexpressionowner', 'expexpressionname', 'experrortime', 'experrorindex', 'experrorcode', 'experrorinstance'], name, value)

            class Experrorcode(Enum):
                """
                Experrorcode (Enum Class)

                The error that occurred.  In the following explanations the

                expected timing of the error is in parentheses.  'S' means

                the error occurs on a Set request.  'E' means the error

                occurs on the attempt to evaluate the expression either due to

                Get from expValueTable or in ongoing delta processing.

                invalidSyntax       the value sent for expExpression is not

                               valid Expression MIB expression syntax

                               (S)

                undefinedObjectIndex     an object reference ($n) in

                               expExpression does not have a matching

                               instance in expObjectTable (E)

                unrecognizedOperator     the value sent for expExpression held an

                               unrecognized operator (S)

                unrecognizedFunction     the value sent for expExpression held an

                               unrecognized function name (S)

                invalidOperandType  an operand in expExpression is not the

                               right type for the associated operator

                               or result (SE)

                unmatchedParenthesis     the value sent for expExpression is not

                               correctly parenthesized (S)

                tooManyWildcardValues    evaluating the expression exceeded the

                               limit set by

                               expResourceDeltaWildcardInstanceMaximum

                               (E)

                recursion      through some chain of embedded

                               expressions the expression invokes itself

                               (E)

                deltaTooShort       the delta for the next evaluation passed

                               before the system could evaluate the

                               present sample (E)

                resourceUnavailable some resource, typically dynamic memory,

                               was unavailable (SE)

                divideByZero        an attempt to divide by zero occurred

                               (E)

                For the errors that occur when the attempt is made to set

                expExpression Set request fails with the SNMP error code

                'wrongValue'.  Such failures refer to the most recent failure to

                Set expExpression, not to the present value of expExpression

                which must be either unset or syntactically correct.

                Errors that occur during evaluation for a Get\* operation return

                the SNMP error code 'genErr' except for 'tooManyWildcardValues'

                and 'resourceUnavailable' which return the SNMP error code

                'resourceUnavailable'.

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



    class Expobjecttable(Entity):
        """
        A table of object definitions for each expExpression.
        
        Wildcarding instance IDs\:
        
        It is legal to omit all or part of the instance portion for
        some or all of the objects in an expression. (See the
        DESCRIPTION of expObjectID for details.  However, note that
        if more than one object in the same expression is wildcarded
        in this way, they all must be objects where that portion of
        the instance is the same.  In other words, all objects may be
        in the same SEQUENCE or in different SEQUENCEs but with the
        same semantic index value (e.g., a value of ifIndex)
        for the wildcarded portion.
        
        .. attribute:: expobjectentry
        
        	Information about an object.  An application uses expObjectEntryStatus to create entries in this table while in the process of defining an expression.  Values of read\-create objects in this table may be changed at any time
        	**type**\: list of  		 :py:class:`Expobjectentry <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry>`
        
        

        """

        _prefix = 'DISMAN-EXPRESSION-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEXPRESSIONMIB.Expobjecttable, self).__init__()

            self.yang_name = "expObjectTable"
            self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("expObjectEntry", ("expobjectentry", DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry))])
            self._leafs = OrderedDict()

            self.expobjectentry = YList(self)
            self._segment_path = lambda: "expObjectTable"
            self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEXPRESSIONMIB.Expobjecttable, [], name, value)


        class Expobjectentry(Entity):
            """
            Information about an object.  An application uses
            expObjectEntryStatus to create entries in this table while
            in the process of defining an expression.
            
            Values of read\-create objects in this table may be
            changed at any time.
            
            .. attribute:: expexpressionowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`expexpressionowner <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: expexpressionname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`expexpressionname <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: expobjectindex  (key)
            
            	Within an expression, a unique, numeric identification for an object.  Prefixed with a dollar sign ('$') this is used to reference the object in the corresponding expExpression
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: expobjectid
            
            	The OBJECT IDENTIFIER (OID) of this object.  The OID may be fully qualified, meaning it includes a complete instance identifier part (e.g., ifInOctets.1 or sysUpTime.0), or it may not be fully qualified, meaning it may lack all or part of the instance identifier.  If the expObjectID is not fully qualified, then expObjectWildcard must be set to true(1). The value of the expression will be multiple values, as if done for a GetNext sweep of the object.  An object here may itself be the result of an expression but recursion is not allowed.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectidwildcard
            
            	A true value indicates the expObjecID of this row is a wildcard object. False indicates that expObjectID is fully instanced. If all expObjectWildcard values for a given expression are FALSE, expExpressionPrefix will reflect a scalar object (i.e. will be 0.0).  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            .. attribute:: expobjectsampletype
            
            	The method of sampling the selected variable.  An 'absoluteValue' is simply the present value of the object.  A 'deltaValue' is the present value minus the previous value, which was sampled expExpressionDeltaInterval seconds ago. This is intended primarily for use with SNMP counters, which are meaningless as an 'absoluteValue', but may be used with any integer\-based value.  A 'changedValue' is a boolean for whether the present value is different from the previous value.  It is applicable to any data type and results in an Unsigned32 with value 1 if the object's value is changed and 0 if not.  In all other respects it is as a 'deltaValue' and all statements and operation regarding delta values apply to changed values.  When an expression contains both delta and absolute values the absolute values are obtained at the end of the delta period
            	**type**\:  :py:class:`Expobjectsampletype <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry.Expobjectsampletype>`
            
            .. attribute:: expobjectdeltadiscontinuityid
            
            	The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or DateAndTime object that indicates a discontinuity in the value at expObjectID.  This object is instantiated only if expObjectSampleType is 'deltaValue' or 'changedValue'.  The OID may be for a leaf object (e.g. sysUpTime.0) or may be wildcarded to match expObjectID.  This object supports normal checking for a discontinuity in a counter.  Note that if this object does not point to sysUpTime discontinuity checking must still check sysUpTime for an overall discontinuity.  If the object identified is not accessible no discontinuity check will be made
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectdiscontinuityidwildcard
            
            	A true value indicates the expObjectDeltaDiscontinuityID of this row is a wildcard object.  False indicates that expObjectDeltaDiscontinuityID is fully instanced.  This object is instantiated only if expObjectSampleType is 'deltaValue' or 'changedValue'.  NOTE\:  The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            .. attribute:: expobjectdiscontinuityidtype
            
            	The value 'timeTicks' indicates the expObjectDeltaDiscontinuityID of this row is of syntax TimeTicks.  The value 'timeStamp' indicates syntax TimeStamp.  The value 'dateAndTime indicates syntax DateAndTime.  This object is instantiated only if expObjectSampleType is 'deltaValue' or 'changedValue'
            	**type**\:  :py:class:`Expobjectdiscontinuityidtype <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry.Expobjectdiscontinuityidtype>`
            
            .. attribute:: expobjectconditional
            
            	The OBJECT IDENTIFIER (OID) of an object that overrides whether the instance of expObjectID is to be considered usable.  If the value of the object at expObjectConditional is 0 or not instantiated, the object at expObjectID is treated as if it is not instantiated.  In other words, expObjectConditional is a filter that controls whether or not to use the value at expObjectID.  The OID may be for a leaf object (e.g. sysObjectID.0) or may be wildcarded to match expObjectID.  If expObject is wildcarded and expObjectID in the same row is not, the wild portion of expObjectConditional must match the wildcarding of the rest of the expression.  If no object in the expression is wildcarded but expObjectConditional is, use the lexically first instance (if any) of expObjectConditional.  If the value of expObjectConditional is 0.0 operation is as if the value pointed to by expObjectConditional is a non\-zero (true) value.  Note that expObjectConditional can not trivially use an object of syntax TruthValue, since the underlying value is not 0 or 1
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expobjectconditionalwildcard
            
            	A true value indicates the expObjectConditional of this row is a wildcard object. False indicates that expObjectConditional is fully instanced.  NOTE\: The simplest implementations of this MIB may not allow wildcards
            	**type**\: bool
            
            .. attribute:: expobjectentrystatus
            
            	The control that allows creation/deletion of entries.  Objects in this table may be changed while expObjectEntryStatus is in any state
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DISMAN-EXPRESSION-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry, self).__init__()

                self.yang_name = "expObjectEntry"
                self.yang_parent_name = "expObjectTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionowner','expexpressionname','expobjectindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionowner', YLeaf(YType.str, 'expExpressionOwner')),
                    ('expexpressionname', YLeaf(YType.str, 'expExpressionName')),
                    ('expobjectindex', YLeaf(YType.uint32, 'expObjectIndex')),
                    ('expobjectid', YLeaf(YType.str, 'expObjectID')),
                    ('expobjectidwildcard', YLeaf(YType.boolean, 'expObjectIDWildcard')),
                    ('expobjectsampletype', YLeaf(YType.enumeration, 'expObjectSampleType')),
                    ('expobjectdeltadiscontinuityid', YLeaf(YType.str, 'expObjectDeltaDiscontinuityID')),
                    ('expobjectdiscontinuityidwildcard', YLeaf(YType.boolean, 'expObjectDiscontinuityIDWildcard')),
                    ('expobjectdiscontinuityidtype', YLeaf(YType.enumeration, 'expObjectDiscontinuityIDType')),
                    ('expobjectconditional', YLeaf(YType.str, 'expObjectConditional')),
                    ('expobjectconditionalwildcard', YLeaf(YType.boolean, 'expObjectConditionalWildcard')),
                    ('expobjectentrystatus', YLeaf(YType.enumeration, 'expObjectEntryStatus')),
                ])
                self.expexpressionowner = None
                self.expexpressionname = None
                self.expobjectindex = None
                self.expobjectid = None
                self.expobjectidwildcard = None
                self.expobjectsampletype = None
                self.expobjectdeltadiscontinuityid = None
                self.expobjectdiscontinuityidwildcard = None
                self.expobjectdiscontinuityidtype = None
                self.expobjectconditional = None
                self.expobjectconditionalwildcard = None
                self.expobjectentrystatus = None
                self._segment_path = lambda: "expObjectEntry" + "[expExpressionOwner='" + str(self.expexpressionowner) + "']" + "[expExpressionName='" + str(self.expexpressionname) + "']" + "[expObjectIndex='" + str(self.expobjectindex) + "']"
                self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/expObjectTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEXPRESSIONMIB.Expobjecttable.Expobjectentry, ['expexpressionowner', 'expexpressionname', 'expobjectindex', 'expobjectid', 'expobjectidwildcard', 'expobjectsampletype', 'expobjectdeltadiscontinuityid', 'expobjectdiscontinuityidwildcard', 'expobjectdiscontinuityidtype', 'expobjectconditional', 'expobjectconditionalwildcard', 'expobjectentrystatus'], name, value)

            class Expobjectdiscontinuityidtype(Enum):
                """
                Expobjectdiscontinuityidtype (Enum Class)

                The value 'timeTicks' indicates the expObjectDeltaDiscontinuityID

                of this row is of syntax TimeTicks.  The value 'timeStamp' indicates

                syntax TimeStamp.  The value 'dateAndTime indicates syntax

                DateAndTime.

                This object is instantiated only if expObjectSampleType is

                'deltaValue' or 'changedValue'.

                .. data:: timeTicks = 1

                .. data:: timeStamp = 2

                .. data:: dateAndTime = 3

                """

                timeTicks = Enum.YLeaf(1, "timeTicks")

                timeStamp = Enum.YLeaf(2, "timeStamp")

                dateAndTime = Enum.YLeaf(3, "dateAndTime")


            class Expobjectsampletype(Enum):
                """
                Expobjectsampletype (Enum Class)

                The method of sampling the selected variable.

                An 'absoluteValue' is simply the present value of the object.

                A 'deltaValue' is the present value minus the previous value,

                which was sampled expExpressionDeltaInterval seconds ago.

                This is intended primarily for use with SNMP counters, which are

                meaningless as an 'absoluteValue', but may be used with any

                integer\-based value.

                A 'changedValue' is a boolean for whether the present value is

                different from the previous value.  It is applicable to any data

                type and results in an Unsigned32 with value 1 if the object's

                value is changed and 0 if not.  In all other respects it is as a

                'deltaValue' and all statements and operation regarding delta

                values apply to changed values.

                When an expression contains both delta and absolute values

                the absolute values are obtained at the end of the delta

                period.

                .. data:: absoluteValue = 1

                .. data:: deltaValue = 2

                .. data:: changedValue = 3

                """

                absoluteValue = Enum.YLeaf(1, "absoluteValue")

                deltaValue = Enum.YLeaf(2, "deltaValue")

                changedValue = Enum.YLeaf(3, "changedValue")



    class Expvaluetable(Entity):
        """
        A table of values from evaluated expressions.
        
        .. attribute:: expvalueentry
        
        	A single value from an evaluated expression.  For a given instance, only one 'Val' object in the conceptual row will be instantiated, that is, the one with the appropriate type for the value.  For values that contain no objects of expObjectSampleType 'deltaValue' or 'changedValue', reading a value from the table causes the evaluation of the expression for that value.  For those that contain a 'deltaValue' or 'changedValue' the value read is as of the last sampling interval.  If in the attempt to evaluate the expression one or more of the necessary objects is not available, the corresponding entry in this table is effectively not instantiated.  To maintain security of MIB information, when creating a new row in this table, the managed system must record the security credentials of the requester.  These security credentials are the parameters necessary as inputs to isAccessAllowed from [RFC2571]. When obtaining the objects that make up the expression, the system must (conceptually) use isAccessAllowed to ensure that it does not violate security.  The evaluation of that expression takes place under the security credentials of the creator of its expExpressionEntry.  To maintain security of MIB information, expression evaluation must take place using security credentials for the implied Gets of the objects in the expression as inputs (conceptually) to isAccessAllowed from the Architecture for Describing SNMP Management Frameworks.  These are the security credentials of the creator of the corresponding expExpressionEntry
        	**type**\: list of  		 :py:class:`Expvalueentry <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expvaluetable.Expvalueentry>`
        
        

        """

        _prefix = 'DISMAN-EXPRESSION-MIB'
        _revision = '2000-10-16'

        def __init__(self):
            super(DISMANEXPRESSIONMIB.Expvaluetable, self).__init__()

            self.yang_name = "expValueTable"
            self.yang_parent_name = "DISMAN-EXPRESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("expValueEntry", ("expvalueentry", DISMANEXPRESSIONMIB.Expvaluetable.Expvalueentry))])
            self._leafs = OrderedDict()

            self.expvalueentry = YList(self)
            self._segment_path = lambda: "expValueTable"
            self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DISMANEXPRESSIONMIB.Expvaluetable, [], name, value)


        class Expvalueentry(Entity):
            """
            A single value from an evaluated expression.  For a given
            instance, only one 'Val' object in the conceptual row will be
            instantiated, that is, the one with the appropriate type for
            the value.  For values that contain no objects of
            expObjectSampleType 'deltaValue' or 'changedValue', reading a
            value from the table causes the evaluation of the expression
            for that value.  For those that contain a 'deltaValue' or
            'changedValue' the value read is as of the last sampling
            interval.
            
            If in the attempt to evaluate the expression one or more
            of the necessary objects is not available, the corresponding
            entry in this table is effectively not instantiated.
            
            To maintain security of MIB information, when creating a new
            row in this table, the managed system must record the security
            credentials of the requester.  These security credentials are
            the parameters necessary as inputs to isAccessAllowed from
            [RFC2571]. When obtaining the objects that make up the
            expression, the system must (conceptually) use isAccessAllowed to
            ensure that it does not violate security.
            
            The evaluation of that expression takes place under the
            security credentials of the creator of its expExpressionEntry.
            
            To maintain security of MIB information, expression evaluation must
            take place using security credentials for the implied Gets of the
            objects in the expression as inputs (conceptually) to
            isAccessAllowed from the Architecture for Describing SNMP
            Management Frameworks.  These are the security credentials of the
            creator of the corresponding expExpressionEntry.
            
            .. attribute:: expexpressionowner  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..32
            
            	**refers to**\:  :py:class:`expexpressionowner <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: expexpressionname  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`expexpressionname <ydk.models.cisco_ios_xe.DISMAN_EXPRESSION_MIB.DISMANEXPRESSIONMIB.Expexpressiontable.Expexpressionentry>`
            
            .. attribute:: expvalueinstance  (key)
            
            	The final instance portion of a value's OID according to the wildcarding in instances of expObjectID for the expression.  The prefix of this OID fragment is 0.0, leading to the following behavior.  If there is no wildcarding, the value is 0.0.0.  In other words, there is one value which standing alone would have been a scalar with a 0 at the end of its OID.  If there is wildcarding, the value is 0.0 followed by a value that the wildcard can take, thus defining one value instance for each real, possible value of the wildcard. So, for example, if the wildcard worked out to be an ifIndex, there is an expValueInstance for each applicable ifIndex
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expvaluecounter32val
            
            	The value when expExpressionValueType is 'counter32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: expvalueunsigned32val
            
            	The value when expExpressionValueType is 'unsigned32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: expvaluetimeticksval
            
            	The value when expExpressionValueType is 'timeTicks'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: expvalueinteger32val
            
            	The value when expExpressionValueType is 'integer32'
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: expvalueipaddressval
            
            	The value when expExpressionValueType is 'ipAddress'
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: expvalueoctetstringval
            
            	The value when expExpressionValueType is 'octetString'
            	**type**\: str
            
            	**length:** 0..65536
            
            .. attribute:: expvalueoidval
            
            	The value when expExpressionValueType is 'objectId'
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: expvaluecounter64val
            
            	The value when expExpressionValueType is 'counter64'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'DISMAN-EXPRESSION-MIB'
            _revision = '2000-10-16'

            def __init__(self):
                super(DISMANEXPRESSIONMIB.Expvaluetable.Expvalueentry, self).__init__()

                self.yang_name = "expValueEntry"
                self.yang_parent_name = "expValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['expexpressionowner','expexpressionname','expvalueinstance']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('expexpressionowner', YLeaf(YType.str, 'expExpressionOwner')),
                    ('expexpressionname', YLeaf(YType.str, 'expExpressionName')),
                    ('expvalueinstance', YLeaf(YType.str, 'expValueInstance')),
                    ('expvaluecounter32val', YLeaf(YType.uint32, 'expValueCounter32Val')),
                    ('expvalueunsigned32val', YLeaf(YType.uint32, 'expValueUnsigned32Val')),
                    ('expvaluetimeticksval', YLeaf(YType.uint32, 'expValueTimeTicksVal')),
                    ('expvalueinteger32val', YLeaf(YType.int32, 'expValueInteger32Val')),
                    ('expvalueipaddressval', YLeaf(YType.str, 'expValueIpAddressVal')),
                    ('expvalueoctetstringval', YLeaf(YType.str, 'expValueOctetStringVal')),
                    ('expvalueoidval', YLeaf(YType.str, 'expValueOidVal')),
                    ('expvaluecounter64val', YLeaf(YType.uint64, 'expValueCounter64Val')),
                ])
                self.expexpressionowner = None
                self.expexpressionname = None
                self.expvalueinstance = None
                self.expvaluecounter32val = None
                self.expvalueunsigned32val = None
                self.expvaluetimeticksval = None
                self.expvalueinteger32val = None
                self.expvalueipaddressval = None
                self.expvalueoctetstringval = None
                self.expvalueoidval = None
                self.expvaluecounter64val = None
                self._segment_path = lambda: "expValueEntry" + "[expExpressionOwner='" + str(self.expexpressionowner) + "']" + "[expExpressionName='" + str(self.expexpressionname) + "']" + "[expValueInstance='" + str(self.expvalueinstance) + "']"
                self._absolute_path = lambda: "DISMAN-EXPRESSION-MIB:DISMAN-EXPRESSION-MIB/expValueTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DISMANEXPRESSIONMIB.Expvaluetable.Expvalueentry, ['expexpressionowner', 'expexpressionname', 'expvalueinstance', 'expvaluecounter32val', 'expvalueunsigned32val', 'expvaluetimeticksval', 'expvalueinteger32val', 'expvalueipaddressval', 'expvalueoctetstringval', 'expvalueoidval', 'expvaluecounter64val'], name, value)

    def clone_ptr(self):
        self._top_entity = DISMANEXPRESSIONMIB()
        return self._top_entity


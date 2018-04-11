""" SNMP_TARGET_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters used
by an SNMP entity for the generation of SNMP messages.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SNMPTARGETMIB(Entity):
    """
    
    
    .. attribute:: snmptargetobjects
    
    	
    	**type**\:  :py:class:`Snmptargetobjects <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SNMPTARGETMIB.Snmptargetobjects>`
    
    .. attribute:: snmptargetaddrtable
    
    	A table of transport addresses to be used in the generation of SNMP messages
    	**type**\:  :py:class:`Snmptargetaddrtable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SNMPTARGETMIB.Snmptargetaddrtable>`
    
    .. attribute:: snmptargetparamstable
    
    	A table of SNMP target information to be used in the generation of SNMP messages
    	**type**\:  :py:class:`Snmptargetparamstable <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SNMPTARGETMIB.Snmptargetparamstable>`
    
    

    """

    _prefix = 'SNMP-TARGET-MIB'
    _revision = '1998-08-04'

    def __init__(self):
        super(SNMPTARGETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-TARGET-MIB"
        self.yang_parent_name = "SNMP-TARGET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("snmpTargetObjects", ("snmptargetobjects", SNMPTARGETMIB.Snmptargetobjects)), ("snmpTargetAddrTable", ("snmptargetaddrtable", SNMPTARGETMIB.Snmptargetaddrtable)), ("snmpTargetParamsTable", ("snmptargetparamstable", SNMPTARGETMIB.Snmptargetparamstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.snmptargetobjects = SNMPTARGETMIB.Snmptargetobjects()
        self.snmptargetobjects.parent = self
        self._children_name_map["snmptargetobjects"] = "snmpTargetObjects"
        self._children_yang_names.add("snmpTargetObjects")

        self.snmptargetaddrtable = SNMPTARGETMIB.Snmptargetaddrtable()
        self.snmptargetaddrtable.parent = self
        self._children_name_map["snmptargetaddrtable"] = "snmpTargetAddrTable"
        self._children_yang_names.add("snmpTargetAddrTable")

        self.snmptargetparamstable = SNMPTARGETMIB.Snmptargetparamstable()
        self.snmptargetparamstable.parent = self
        self._children_name_map["snmptargetparamstable"] = "snmpTargetParamsTable"
        self._children_yang_names.add("snmpTargetParamsTable")
        self._segment_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB"


    class Snmptargetobjects(Entity):
        """
        
        
        .. attribute:: snmptargetspinlock
        
        	This object is used to facilitate modification of table entries in the SNMP\-TARGET\-MIB module by multiple      managers.  In particular, it is useful when modifying the value of the snmpTargetAddrTagList object.  The procedure for modifying the snmpTargetAddrTagList object is as follows\:      1.  Retrieve the value of snmpTargetSpinLock and         of snmpTargetAddrTagList.      2.  Generate a new value for snmpTargetAddrTagList.      3.  Set the value of snmpTargetSpinLock to the         retrieved value, and the value of         snmpTargetAddrTagList to the new value.  If         the set fails for the snmpTargetSpinLock         object, go back to step 1
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: snmpunavailablecontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unavailable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpunknowncontexts
        
        	The total number of packets received by the SNMP engine which were dropped because the context contained in the message was unknown
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SNMPTARGETMIB.Snmptargetobjects, self).__init__()

            self.yang_name = "snmpTargetObjects"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmptargetspinlock', YLeaf(YType.int32, 'snmpTargetSpinLock')),
                ('snmpunavailablecontexts', YLeaf(YType.uint32, 'snmpUnavailableContexts')),
                ('snmpunknowncontexts', YLeaf(YType.uint32, 'snmpUnknownContexts')),
            ])
            self.snmptargetspinlock = None
            self.snmpunavailablecontexts = None
            self.snmpunknowncontexts = None
            self._segment_path = lambda: "snmpTargetObjects"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.Snmptargetobjects, ['snmptargetspinlock', 'snmpunavailablecontexts', 'snmpunknowncontexts'], name, value)


    class Snmptargetaddrtable(Entity):
        """
        A table of transport addresses to be used in the generation
        of SNMP messages.
        
        .. attribute:: snmptargetaddrentry
        
        	A transport address to be used in the generation of SNMP operations.  Entries in the snmpTargetAddrTable are created and deleted using the snmpTargetAddrRowStatus object
        	**type**\: list of  		 :py:class:`Snmptargetaddrentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SNMPTARGETMIB.Snmptargetaddrtable.Snmptargetaddrentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SNMPTARGETMIB.Snmptargetaddrtable, self).__init__()

            self.yang_name = "snmpTargetAddrTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("snmpTargetAddrEntry", ("snmptargetaddrentry", SNMPTARGETMIB.Snmptargetaddrtable.Snmptargetaddrentry))])
            self._leafs = OrderedDict()

            self.snmptargetaddrentry = YList(self)
            self._segment_path = lambda: "snmpTargetAddrTable"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.Snmptargetaddrtable, [], name, value)


        class Snmptargetaddrentry(Entity):
            """
            A transport address to be used in the generation
            of SNMP operations.
            
            Entries in the snmpTargetAddrTable are created and
            deleted using the snmpTargetAddrRowStatus object.
            
            .. attribute:: snmptargetaddrname  (key)
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetAddrEntry
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrtdomain
            
            	This object indicates the transport type of the address contained in the snmpTargetAddrTAddress object
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: snmptargetaddrtaddress
            
            	This object contains a transport address.  The format of this address depends on the value of the snmpTargetAddrTDomain object
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: snmptargetaddrtimeout
            
            	This object should reflect the expected maximum round trip time for communicating with the transport address defined by this row.  When a message is sent to this address, and a response (if one is expected) is not received within this time period, an implementation may assume that the response will not be delivered.  Note that the time interval that an application waits for a response may actually be derived from the value of this object.  The method for deriving the actual time interval is implementation dependent.  One such method      is to derive the expected round trip time based on a particular retransmission algorithm and on the number of timeouts which have occurred.  The type of message may also be considered when deriving expected round trip times for retransmissions.  For example, if a message is being sent with a securityLevel that indicates both authentication and privacy, the derived value may be increased to compensate for extra processing time spent during authentication and encryption processing
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetaddrretrycount
            
            	This object specifies a default number of retries to be attempted when a response is not received for a generated message.  An application may provide its own retry count, in which case the value of this object is ignored
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: snmptargetaddrtaglist
            
            	This object contains a list of tag values which are used to select target addresses for a particular operation
            	**type**\: str
            
            .. attribute:: snmptargetaddrparams
            
            	The value of this object identifies an entry in the snmpTargetParamsTable.  The identified entry contains SNMP parameters to be used when generating messages to be sent to this transport address
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetaddrstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: snmptargetaddrrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetAddrRowStatus column is 'notReady'.  In particular, a newly created row cannot be made active until the corresponding instances of snmpTargetAddrTDomain, snmpTargetAddrTAddress, and snmpTargetAddrParams have all been set.  The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetAddrTDomain     \- snmpTargetAddrTAddress An attempt to set these objects while the value of snmpTargetAddrRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                super(SNMPTARGETMIB.Snmptargetaddrtable.Snmptargetaddrentry, self).__init__()

                self.yang_name = "snmpTargetAddrEntry"
                self.yang_parent_name = "snmpTargetAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmptargetaddrname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmptargetaddrname', YLeaf(YType.str, 'snmpTargetAddrName')),
                    ('snmptargetaddrtdomain', YLeaf(YType.str, 'snmpTargetAddrTDomain')),
                    ('snmptargetaddrtaddress', YLeaf(YType.str, 'snmpTargetAddrTAddress')),
                    ('snmptargetaddrtimeout', YLeaf(YType.int32, 'snmpTargetAddrTimeout')),
                    ('snmptargetaddrretrycount', YLeaf(YType.int32, 'snmpTargetAddrRetryCount')),
                    ('snmptargetaddrtaglist', YLeaf(YType.str, 'snmpTargetAddrTagList')),
                    ('snmptargetaddrparams', YLeaf(YType.str, 'snmpTargetAddrParams')),
                    ('snmptargetaddrstoragetype', YLeaf(YType.enumeration, 'snmpTargetAddrStorageType')),
                    ('snmptargetaddrrowstatus', YLeaf(YType.enumeration, 'snmpTargetAddrRowStatus')),
                ])
                self.snmptargetaddrname = None
                self.snmptargetaddrtdomain = None
                self.snmptargetaddrtaddress = None
                self.snmptargetaddrtimeout = None
                self.snmptargetaddrretrycount = None
                self.snmptargetaddrtaglist = None
                self.snmptargetaddrparams = None
                self.snmptargetaddrstoragetype = None
                self.snmptargetaddrrowstatus = None
                self._segment_path = lambda: "snmpTargetAddrEntry" + "[snmpTargetAddrName='" + str(self.snmptargetaddrname) + "']"
                self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPTARGETMIB.Snmptargetaddrtable.Snmptargetaddrentry, ['snmptargetaddrname', 'snmptargetaddrtdomain', 'snmptargetaddrtaddress', 'snmptargetaddrtimeout', 'snmptargetaddrretrycount', 'snmptargetaddrtaglist', 'snmptargetaddrparams', 'snmptargetaddrstoragetype', 'snmptargetaddrrowstatus'], name, value)


    class Snmptargetparamstable(Entity):
        """
        A table of SNMP target information to be used
        in the generation of SNMP messages.
        
        .. attribute:: snmptargetparamsentry
        
        	A set of SNMP target information.  Entries in the snmpTargetParamsTable are created and deleted using the snmpTargetParamsRowStatus object
        	**type**\: list of  		 :py:class:`Snmptargetparamsentry <ydk.models.cisco_ios_xe.SNMP_TARGET_MIB.SNMPTARGETMIB.Snmptargetparamstable.Snmptargetparamsentry>`
        
        

        """

        _prefix = 'SNMP-TARGET-MIB'
        _revision = '1998-08-04'

        def __init__(self):
            super(SNMPTARGETMIB.Snmptargetparamstable, self).__init__()

            self.yang_name = "snmpTargetParamsTable"
            self.yang_parent_name = "SNMP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("snmpTargetParamsEntry", ("snmptargetparamsentry", SNMPTARGETMIB.Snmptargetparamstable.Snmptargetparamsentry))])
            self._leafs = OrderedDict()

            self.snmptargetparamsentry = YList(self)
            self._segment_path = lambda: "snmpTargetParamsTable"
            self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPTARGETMIB.Snmptargetparamstable, [], name, value)


        class Snmptargetparamsentry(Entity):
            """
            A set of SNMP target information.
            
            Entries in the snmpTargetParamsTable are created and
            deleted using the snmpTargetParamsRowStatus object.
            
            .. attribute:: snmptargetparamsname  (key)
            
            	The locally arbitrary, but unique identifier associated with this snmpTargetParamsEntry
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmptargetparamsmpmodel
            
            	The Message Processing Model to be used when generating SNMP messages using this entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: snmptargetparamssecuritymodel
            
            	The Security Model to be used when generating SNMP messages using this entry.  An implementation may choose to return an inconsistentValue error if an attempt is made to set this variable to a value for a security model which the implementation does      not support
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: snmptargetparamssecurityname
            
            	The securityName which identifies the Principal on whose behalf SNMP messages will be generated using this entry
            	**type**\: str
            
            .. attribute:: snmptargetparamssecuritylevel
            
            	The Level of Security to be used when generating SNMP messages using this entry
            	**type**\:  :py:class:`SnmpSecurityLevel <ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB.SnmpSecurityLevel>`
            
            .. attribute:: snmptargetparamsstoragetype
            
            	The storage type for this conceptual row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: snmptargetparamsrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the snmpTargetParamsRowStatus column is 'notReady'.  In particular, a newly created row cannot be made      active until the corresponding snmpTargetParamsMPModel, snmpTargetParamsSecurityModel, snmpTargetParamsSecurityName, and snmpTargetParamsSecurityLevel have all been set. The following objects may not be modified while the value of this object is active(1)\:     \- snmpTargetParamsMPModel     \- snmpTargetParamsSecurityModel     \- snmpTargetParamsSecurityName     \- snmpTargetParamsSecurityLevel An attempt to set these objects while the value of snmpTargetParamsRowStatus is active(1) will result in an inconsistentValue error
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'SNMP-TARGET-MIB'
            _revision = '1998-08-04'

            def __init__(self):
                super(SNMPTARGETMIB.Snmptargetparamstable.Snmptargetparamsentry, self).__init__()

                self.yang_name = "snmpTargetParamsEntry"
                self.yang_parent_name = "snmpTargetParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmptargetparamsname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmptargetparamsname', YLeaf(YType.str, 'snmpTargetParamsName')),
                    ('snmptargetparamsmpmodel', YLeaf(YType.int32, 'snmpTargetParamsMPModel')),
                    ('snmptargetparamssecuritymodel', YLeaf(YType.int32, 'snmpTargetParamsSecurityModel')),
                    ('snmptargetparamssecurityname', YLeaf(YType.str, 'snmpTargetParamsSecurityName')),
                    ('snmptargetparamssecuritylevel', YLeaf(YType.enumeration, 'snmpTargetParamsSecurityLevel')),
                    ('snmptargetparamsstoragetype', YLeaf(YType.enumeration, 'snmpTargetParamsStorageType')),
                    ('snmptargetparamsrowstatus', YLeaf(YType.enumeration, 'snmpTargetParamsRowStatus')),
                ])
                self.snmptargetparamsname = None
                self.snmptargetparamsmpmodel = None
                self.snmptargetparamssecuritymodel = None
                self.snmptargetparamssecurityname = None
                self.snmptargetparamssecuritylevel = None
                self.snmptargetparamsstoragetype = None
                self.snmptargetparamsrowstatus = None
                self._segment_path = lambda: "snmpTargetParamsEntry" + "[snmpTargetParamsName='" + str(self.snmptargetparamsname) + "']"
                self._absolute_path = lambda: "SNMP-TARGET-MIB:SNMP-TARGET-MIB/snmpTargetParamsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPTARGETMIB.Snmptargetparamstable.Snmptargetparamsentry, ['snmptargetparamsname', 'snmptargetparamsmpmodel', 'snmptargetparamssecuritymodel', 'snmptargetparamssecurityname', 'snmptargetparamssecuritylevel', 'snmptargetparamsstoragetype', 'snmptargetparamsrowstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = SNMPTARGETMIB()
        return self._top_entity


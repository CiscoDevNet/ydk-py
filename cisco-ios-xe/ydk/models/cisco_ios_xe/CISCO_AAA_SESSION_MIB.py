""" CISCO_AAA_SESSION_MIB 

This MIB module provides data for accounting sessions
based on Authentication, Authorization, Accounting
(AAA) protocols.


References\:
    RFC 2139 RADIUS Accounting
    The TACACS+ Protocol Version 1.78, Internet Draft

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOAAASESSIONMIB(Entity):
    """
    
    
    .. attribute:: casnactive
    
    	
    	**type**\:  :py:class:`CasnActive <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CISCOAAASESSIONMIB.CasnActive>`
    
    	**config**\: False
    
    .. attribute:: casngeneral
    
    	
    	**type**\:  :py:class:`CasnGeneral <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CISCOAAASESSIONMIB.CasnGeneral>`
    
    	**config**\: False
    
    .. attribute:: casnactivetable
    
    	This table contains entries for active AAA accounting sessions in the system
    	**type**\:  :py:class:`CasnActiveTable <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CISCOAAASESSIONMIB.CasnActiveTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-AAA-SESSION-MIB'
    _revision = '2006-03-21'

    def __init__(self):
        super(CISCOAAASESSIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-AAA-SESSION-MIB"
        self.yang_parent_name = "CISCO-AAA-SESSION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("casnActive", ("casnactive", CISCOAAASESSIONMIB.CasnActive)), ("casnGeneral", ("casngeneral", CISCOAAASESSIONMIB.CasnGeneral)), ("casnActiveTable", ("casnactivetable", CISCOAAASESSIONMIB.CasnActiveTable))])
        self._leafs = OrderedDict()

        self.casnactive = CISCOAAASESSIONMIB.CasnActive()
        self.casnactive.parent = self
        self._children_name_map["casnactive"] = "casnActive"

        self.casngeneral = CISCOAAASESSIONMIB.CasnGeneral()
        self.casngeneral.parent = self
        self._children_name_map["casngeneral"] = "casnGeneral"

        self.casnactivetable = CISCOAAASESSIONMIB.CasnActiveTable()
        self.casnactivetable.parent = self
        self._children_name_map["casnactivetable"] = "casnActiveTable"
        self._segment_path = lambda: "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOAAASESSIONMIB, [], name, value)


    class CasnActive(Entity):
        """
        
        
        .. attribute:: casnactivetableentries
        
        	Number of entries currently in casnActiveTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: casnactivetablehighwatermark
        
        	Maximum number of entries present in casnActiveTable since last system re\-initialization.  This corresponds to the maximum value reported by casnActiveTableEntries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CISCOAAASESSIONMIB.CasnActive, self).__init__()

            self.yang_name = "casnActive"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('casnactivetableentries', (YLeaf(YType.uint32, 'casnActiveTableEntries'), ['int'])),
                ('casnactivetablehighwatermark', (YLeaf(YType.uint32, 'casnActiveTableHighWaterMark'), ['int'])),
            ])
            self.casnactivetableentries = None
            self.casnactivetablehighwatermark = None
            self._segment_path = lambda: "casnActive"
            self._absolute_path = lambda: "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASESSIONMIB.CasnActive, ['casnactivetableentries', 'casnactivetablehighwatermark'], name, value)



    class CasnGeneral(Entity):
        """
        
        
        .. attribute:: casntotalsessions
        
        	Total number of sessions since last system re\-initialization.  This value includes all sessions currently in the casnActiveTable and all previous sessions whether terminated via casnDisconnect or via other mechanisms
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: casndisconnectedsessions
        
        	Total number of sessions which have been disconnected using casnDisconnect since last system re\-initialization.  This value includes any sessions still in the casnActiveTable with a casnDisconnect value of true(1) and all previous sessions which terminated as a result of setting casnDisconnect
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CISCOAAASESSIONMIB.CasnGeneral, self).__init__()

            self.yang_name = "casnGeneral"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('casntotalsessions', (YLeaf(YType.uint32, 'casnTotalSessions'), ['int'])),
                ('casndisconnectedsessions', (YLeaf(YType.uint32, 'casnDisconnectedSessions'), ['int'])),
            ])
            self.casntotalsessions = None
            self.casndisconnectedsessions = None
            self._segment_path = lambda: "casnGeneral"
            self._absolute_path = lambda: "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASESSIONMIB.CasnGeneral, ['casntotalsessions', 'casndisconnectedsessions'], name, value)



    class CasnActiveTable(Entity):
        """
        This table contains entries for active AAA accounting
        sessions in the system.
        
        .. attribute:: casnactiveentry
        
        	The information regarding a single accounting session.  Entries are created when a new accounting session is begun.  Entries are removed when the accounting session is ended.  Initiating termination of a session with the object casnDisconnect will cause removal of the entry when the session completes termination
        	**type**\: list of  		 :py:class:`CasnActiveEntry <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CISCOAAASESSIONMIB.CasnActiveTable.CasnActiveEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CISCOAAASESSIONMIB.CasnActiveTable, self).__init__()

            self.yang_name = "casnActiveTable"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("casnActiveEntry", ("casnactiveentry", CISCOAAASESSIONMIB.CasnActiveTable.CasnActiveEntry))])
            self._leafs = OrderedDict()

            self.casnactiveentry = YList(self)
            self._segment_path = lambda: "casnActiveTable"
            self._absolute_path = lambda: "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASESSIONMIB.CasnActiveTable, [], name, value)


        class CasnActiveEntry(Entity):
            """
            The information regarding a single accounting session.
            
            Entries are created when a new accounting session
            is begun.
            
            Entries are removed when the accounting session
            is ended.
            
            Initiating termination of a session with the object
            casnDisconnect will cause removal of the entry when
            the session completes termination.
            
            .. attribute:: casnsessionid  (key)
            
            	This is the session identification used by the accounting protocol.  This value is unique to a session within the system, even if multiple accounting protocols are in use.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 44, Acct\-Session\-Id    TACACS+\: attribute 'task\_id'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: casnuserid
            
            	The User login ID or zero length string if unavailable.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 1, User\-Name    TACACS+\: attribute 'user'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: casnipaddr
            
            	The IP address of the session or 0.0.0.0 if not applicable or unavailable.  RADIUS\:  attribute 8, Framed\-IP\-Address TACACS+\: attribute 'addr'
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: casnidletime
            
            	The elapsed time that this session has been idle.  This is the time since the last user\-level data has been received or transmitted. Protocol level handshaking associated with the call is considered to be idle for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: casndisconnect
            
            	This object is used to terminate this session.  Setting the value to true(1) will initiate termination of this session.  The entry will be removed once the session has completed termination.  Once this object has been set to true(1), the session termination process can not be cancelled by setting the value false(2)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: casncalltrackerid
            
            	The value of this object is the entry index in the CISCO\-CALL\-TRACKER\-MIB cctActiveTable of the call corresponding to this accounting session.  Using the value of this object to query the cctActiveTable will provide more detailed data regarding the session represented by this casnActiveEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casnnasport
            
            	The value of this object identifies a particular conceptual row associated with the session identified by casnSessionId.  The conceptual row that this object points to represents a port that is used to transport a session.  If the port transporting the session cannot be determined, the value of this object will be zeroDotZero.  For example, suppose a session is established using an ATM PVC.  If the ifIndex of the ATM interface is 7, and the  VPI/VCI values of the PVC are 1, 100 respectively, then the value of this object might be as follows\:         casnNasPort.15 = atmVclAdminStatus.7.1.100                    ^                      ^ ^  ^                    \|                      \| \|  \|    casnSessionId \-\-+                      \| \|  \|          ifIndex \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  \|        atmVclVpi \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  \|        atmVclVci \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  where atmVclAdminStatus is the first accessible object of the atmVclTable of the ATM\-MIB
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: casnvaiifindex
            
            	The ifIndex of the Virtual Access Interface (VAI) that is associated with the PPP session.  This interface may not be represented in the IF\-MIB in which case the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-AAA-SESSION-MIB'
            _revision = '2006-03-21'

            def __init__(self):
                super(CISCOAAASESSIONMIB.CasnActiveTable.CasnActiveEntry, self).__init__()

                self.yang_name = "casnActiveEntry"
                self.yang_parent_name = "casnActiveTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['casnsessionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('casnsessionid', (YLeaf(YType.uint32, 'casnSessionId'), ['int'])),
                    ('casnuserid', (YLeaf(YType.str, 'casnUserId'), ['str'])),
                    ('casnipaddr', (YLeaf(YType.str, 'casnIpAddr'), ['str'])),
                    ('casnidletime', (YLeaf(YType.uint32, 'casnIdleTime'), ['int'])),
                    ('casndisconnect', (YLeaf(YType.boolean, 'casnDisconnect'), ['bool'])),
                    ('casncalltrackerid', (YLeaf(YType.uint32, 'casnCallTrackerId'), ['int'])),
                    ('casnnasport', (YLeaf(YType.str, 'casnNasPort'), ['str'])),
                    ('casnvaiifindex', (YLeaf(YType.int32, 'casnVaiIfIndex'), ['int'])),
                ])
                self.casnsessionid = None
                self.casnuserid = None
                self.casnipaddr = None
                self.casnidletime = None
                self.casndisconnect = None
                self.casncalltrackerid = None
                self.casnnasport = None
                self.casnvaiifindex = None
                self._segment_path = lambda: "casnActiveEntry" + "[casnSessionId='" + str(self.casnsessionid) + "']"
                self._absolute_path = lambda: "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/casnActiveTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOAAASESSIONMIB.CasnActiveTable.CasnActiveEntry, ['casnsessionid', 'casnuserid', 'casnipaddr', 'casnidletime', 'casndisconnect', 'casncalltrackerid', 'casnnasport', 'casnvaiifindex'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOAAASESSIONMIB()
        return self._top_entity




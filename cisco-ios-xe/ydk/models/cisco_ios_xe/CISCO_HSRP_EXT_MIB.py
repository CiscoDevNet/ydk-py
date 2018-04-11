""" CISCO_HSRP_EXT_MIB 

The Extension MIB module for the CISCO\-HSRP\-MIB which is
based on RFC2281.

This MIB provides an extension to the CISCO\-HSRP\-MIB which 
defines Cisco's proprietary Hot Standby Routing Protocol 
(HSRP), defined in RFC2281. The extensions cover assigning 
of secondary HSRP ip addresses, modifying an HSRP Group's 
priority by tracking the operational status of interfaces, 
etc. 

Terminology\:
HSRP is a protocol used amoung a group of routers for the 
purpose of selecting an active router and a standby router. 

An active router is the router of choice for routing 
packets.

A standby router is a router that takes over the routing 
duties when an active router fails, or when preset 
conditions have been met.

A HSRP group or a standby group is a set of routers 
which communicate using HSRP. An HSRP group has a group 
MAC address and a group IP address. These are the 
designated addresses. The active router assumes  
(i.e. inherits) these group addresses. An HSRP group is
identified by a ( ifIndex, cHsrpGrpNumber ) pair.

BIA stands for Burned In Address.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOHSRPEXTMIB(Entity):
    """
    
    
    .. attribute:: chsrpextiftrackedtable
    
    	A table containing information about tracked interfaces per HSRP group
    	**type**\:  :py:class:`Chsrpextiftrackedtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextiftrackedtable>`
    
    .. attribute:: chsrpextsecaddrtable
    
    	A table containing information about secondary HSRP IP Addresses per interface and group
    	**type**\:  :py:class:`Chsrpextsecaddrtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextsecaddrtable>`
    
    .. attribute:: chsrpextifstandbytable
    
    	A table containing information about standby interfaces per HSRP group
    	**type**\:  :py:class:`Chsrpextifstandbytable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextifstandbytable>`
    
    .. attribute:: chsrpextiftable
    
    	HSRP\-specific configurations for each physical interface
    	**type**\:  :py:class:`Chsrpextiftable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextiftable>`
    
    

    """

    _prefix = 'CISCO-HSRP-EXT-MIB'
    _revision = '2010-09-02'

    def __init__(self):
        super(CISCOHSRPEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-HSRP-EXT-MIB"
        self.yang_parent_name = "CISCO-HSRP-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cHsrpExtIfTrackedTable", ("chsrpextiftrackedtable", CISCOHSRPEXTMIB.Chsrpextiftrackedtable)), ("cHsrpExtSecAddrTable", ("chsrpextsecaddrtable", CISCOHSRPEXTMIB.Chsrpextsecaddrtable)), ("cHsrpExtIfStandbyTable", ("chsrpextifstandbytable", CISCOHSRPEXTMIB.Chsrpextifstandbytable)), ("cHsrpExtIfTable", ("chsrpextiftable", CISCOHSRPEXTMIB.Chsrpextiftable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.chsrpextiftrackedtable = CISCOHSRPEXTMIB.Chsrpextiftrackedtable()
        self.chsrpextiftrackedtable.parent = self
        self._children_name_map["chsrpextiftrackedtable"] = "cHsrpExtIfTrackedTable"
        self._children_yang_names.add("cHsrpExtIfTrackedTable")

        self.chsrpextsecaddrtable = CISCOHSRPEXTMIB.Chsrpextsecaddrtable()
        self.chsrpextsecaddrtable.parent = self
        self._children_name_map["chsrpextsecaddrtable"] = "cHsrpExtSecAddrTable"
        self._children_yang_names.add("cHsrpExtSecAddrTable")

        self.chsrpextifstandbytable = CISCOHSRPEXTMIB.Chsrpextifstandbytable()
        self.chsrpextifstandbytable.parent = self
        self._children_name_map["chsrpextifstandbytable"] = "cHsrpExtIfStandbyTable"
        self._children_yang_names.add("cHsrpExtIfStandbyTable")

        self.chsrpextiftable = CISCOHSRPEXTMIB.Chsrpextiftable()
        self.chsrpextiftable.parent = self
        self._children_name_map["chsrpextiftable"] = "cHsrpExtIfTable"
        self._children_yang_names.add("cHsrpExtIfTable")
        self._segment_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB"


    class Chsrpextiftrackedtable(Entity):
        """
        A table containing information about tracked interfaces per
        HSRP group.
        
        .. attribute:: chsrpextiftrackedentry
        
        	Each row of this table allows the tracking of one interface of the HSRP group which is identified by the (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause. Weight(priority) is given to each and every interface tracked.  When a tracked interface is unavailable, the HSRP priority of the router is decreased. i.e cHsrpGrpPriority value assigned  to an HSRP group will reduce by the value assigned to cHsrpExtIfTrackedPriority. This reduces the likelihood  of a router with a failed key interface becoming the  active router.  Setting cHsrpExtIfTrackedRowStatus to active starts the tracking of cHsrpExtIfTracked by the HSRP group.  The value of cHsrpExtIfTrackedRowStatus may be set  to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfTrackedRowStatus to either 'createAndGo'  or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row entry in the cHsrpExtIfTrackedTable can not be created unless the corresponding row in the cHsrpGrpTable has been  created. If that corresponding row in cHsrpGrpTable is  deleted, the interfaces it tracks also get deleted.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of  		 :py:class:`Chsrpextiftrackedentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextiftrackedtable.Chsrpextiftrackedentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CISCOHSRPEXTMIB.Chsrpextiftrackedtable, self).__init__()

            self.yang_name = "cHsrpExtIfTrackedTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cHsrpExtIfTrackedEntry", ("chsrpextiftrackedentry", CISCOHSRPEXTMIB.Chsrpextiftrackedtable.Chsrpextiftrackedentry))])
            self._leafs = OrderedDict()

            self.chsrpextiftrackedentry = YList(self)
            self._segment_path = lambda: "cHsrpExtIfTrackedTable"
            self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextiftrackedtable, [], name, value)


        class Chsrpextiftrackedentry(Entity):
            """
            Each row of this table allows the tracking of one
            interface of the HSRP group which is identified by the
            (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause.
            Weight(priority) is given to each and every interface tracked. 
            When a tracked interface is unavailable, the HSRP priority of
            the router is decreased. i.e cHsrpGrpPriority value assigned 
            to an HSRP group will reduce by the value assigned to
            cHsrpExtIfTrackedPriority. This reduces the likelihood 
            of a router with a failed key interface becoming the 
            active router.
            
            Setting cHsrpExtIfTrackedRowStatus to active starts
            the tracking of cHsrpExtIfTracked by the HSRP group. 
            The value of cHsrpExtIfTrackedRowStatus may be set 
            to destroy at any time.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtIfTrackedRowStatus to either 'createAndGo' 
            or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row entry in the cHsrpExtIfTrackedTable can not be created
            unless the corresponding row in the cHsrpGrpTable has been 
            created. If that corresponding row in cHsrpGrpTable is 
            deleted, the interfaces it tracks also get deleted.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextiftracked  (key)
            
            	The ifIndex value of the tracked interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: chsrpextiftrackedpriority
            
            	Priority of the tracked interface for the corresponding { ifIndex, cHsrpGrpNumber } pair. In the range of 0 to 255, 0 is the lowest priority and 255 is the highest. When a tracked  interface is unavailable, the cHsrpGrpPriority of the router  is decreased by the value of this object instance (If the  cHsrpGrpPriority is less than the  cHsrpExtIfTrackedPriority, then the HSRP priority  becomes 0). This allows a standby router to be configured  with a priority such that if the currently active router's  priority is lowered because the tracked interface goes down,  the standby router can takeover
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: chsrpextiftrackedrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfTrackedEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: chsrpextiftrackedipnone
            
            	This object specifies the disable HSRP IPv4 virtual IP address
            	**type**\: bool
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CISCOHSRPEXTMIB.Chsrpextiftrackedtable.Chsrpextiftrackedentry, self).__init__()

                self.yang_name = "cHsrpExtIfTrackedEntry"
                self.yang_parent_name = "cHsrpExtIfTrackedTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','chsrpgrpnumber','chsrpextiftracked']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('chsrpgrpnumber', YLeaf(YType.str, 'cHsrpGrpNumber')),
                    ('chsrpextiftracked', YLeaf(YType.int32, 'cHsrpExtIfTracked')),
                    ('chsrpextiftrackedpriority', YLeaf(YType.uint32, 'cHsrpExtIfTrackedPriority')),
                    ('chsrpextiftrackedrowstatus', YLeaf(YType.enumeration, 'cHsrpExtIfTrackedRowStatus')),
                    ('chsrpextiftrackedipnone', YLeaf(YType.boolean, 'cHsrpExtIfTrackedIpNone')),
                ])
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextiftracked = None
                self.chsrpextiftrackedpriority = None
                self.chsrpextiftrackedrowstatus = None
                self.chsrpextiftrackedipnone = None
                self._segment_path = lambda: "cHsrpExtIfTrackedEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cHsrpGrpNumber='" + str(self.chsrpgrpnumber) + "']" + "[cHsrpExtIfTracked='" + str(self.chsrpextiftracked) + "']"
                self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfTrackedTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextiftrackedtable.Chsrpextiftrackedentry, ['ifindex', 'chsrpgrpnumber', 'chsrpextiftracked', 'chsrpextiftrackedpriority', 'chsrpextiftrackedrowstatus', 'chsrpextiftrackedipnone'], name, value)


    class Chsrpextsecaddrtable(Entity):
        """
        A table containing information about secondary HSRP IP
        Addresses per interface and group.
        
        .. attribute:: chsrpextsecaddrentry
        
        	The CHsrpExtSecAddrEntry allows creation of secondary IP Addresses for each cHsrpGrpEntry row.  Secondary addresses can be added by setting  cHsrpExtSecAddrRowStatus to be active. The value of cHsrpExtSecAddrRowStatus may be set to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtSecAddrRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout.  Before creation of a cHsrpExtSecAddrEntry row, either cHsrpGrpConfiguredVirtualIpAddr or  cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address. This is because a secondary ip address cannot be created unless the primary ip address has already been set.  To create a new cHsrpExtSecAddrEntry row, a management  station should choose the ifIndex of the interface which is to  be added as part of an HSRP group. Also, an HSRP group number  and a cHsrpExtSecAddrAddress should be chosen.  Deleting a {ifIndex, cHsrpGrpNumber} row in the cHsrpGrpTable will delete all corresponding rows in the cHsrpExtSecAddrTable. Deleting a primary address value in the cHsrpGrpEntry row will delete all secondary addresses for the same {ifIndex, cHsrpGrpNumber} pair
        	**type**\: list of  		 :py:class:`Chsrpextsecaddrentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextsecaddrtable.Chsrpextsecaddrentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CISCOHSRPEXTMIB.Chsrpextsecaddrtable, self).__init__()

            self.yang_name = "cHsrpExtSecAddrTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cHsrpExtSecAddrEntry", ("chsrpextsecaddrentry", CISCOHSRPEXTMIB.Chsrpextsecaddrtable.Chsrpextsecaddrentry))])
            self._leafs = OrderedDict()

            self.chsrpextsecaddrentry = YList(self)
            self._segment_path = lambda: "cHsrpExtSecAddrTable"
            self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextsecaddrtable, [], name, value)


        class Chsrpextsecaddrentry(Entity):
            """
            The CHsrpExtSecAddrEntry allows creation of secondary
            IP Addresses for each cHsrpGrpEntry row.
            
            Secondary addresses can be added by setting 
            cHsrpExtSecAddrRowStatus to be active. The value of
            cHsrpExtSecAddrRowStatus may be set to destroy at any
            time.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtSecAddrRowStatus to either 'createAndGo'
            or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            Before creation of a cHsrpExtSecAddrEntry row,
            either cHsrpGrpConfiguredVirtualIpAddr or 
            cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address.
            This is because a secondary ip address cannot be created
            unless the primary ip address has already been set.
            
            To create a new cHsrpExtSecAddrEntry row, a management 
            station should choose the ifIndex of the interface which is to 
            be added as part of an HSRP group. Also, an HSRP group number 
            and a cHsrpExtSecAddrAddress should be chosen.
            
            Deleting a {ifIndex, cHsrpGrpNumber} row in the
            cHsrpGrpTable will delete all corresponding
            rows in the cHsrpExtSecAddrTable.
            Deleting a primary address value in the cHsrpGrpEntry row
            will delete all secondary addresses for the same
            {ifIndex, cHsrpGrpNumber} pair.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextsecaddraddress  (key)
            
            	A secondary IpAddress for the {ifIndex, cHsrpGrpNumber} pair. As explained in the DESCRIPTION for cHsrpExtSecAddrEntry, a primary address must exist before a secondary address for  the same {ifIndex, cHsrpGrpNumber} pair can be created
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpextsecaddrrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtSecAddrEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CISCOHSRPEXTMIB.Chsrpextsecaddrtable.Chsrpextsecaddrentry, self).__init__()

                self.yang_name = "cHsrpExtSecAddrEntry"
                self.yang_parent_name = "cHsrpExtSecAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','chsrpgrpnumber','chsrpextsecaddraddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('chsrpgrpnumber', YLeaf(YType.str, 'cHsrpGrpNumber')),
                    ('chsrpextsecaddraddress', YLeaf(YType.str, 'cHsrpExtSecAddrAddress')),
                    ('chsrpextsecaddrrowstatus', YLeaf(YType.enumeration, 'cHsrpExtSecAddrRowStatus')),
                ])
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextsecaddraddress = None
                self.chsrpextsecaddrrowstatus = None
                self._segment_path = lambda: "cHsrpExtSecAddrEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cHsrpGrpNumber='" + str(self.chsrpgrpnumber) + "']" + "[cHsrpExtSecAddrAddress='" + str(self.chsrpextsecaddraddress) + "']"
                self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtSecAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextsecaddrtable.Chsrpextsecaddrentry, ['ifindex', 'chsrpgrpnumber', 'chsrpextsecaddraddress', 'chsrpextsecaddrrowstatus'], name, value)


    class Chsrpextifstandbytable(Entity):
        """
        A table containing information about standby
        interfaces per HSRP group.
        
        .. attribute:: chsrpextifstandbyentry
        
        	The cHsrpExtIfStandbyEntry allows an HSRP group interface to track one or more standby interfaces.  To create a new cHsrpExtIfStandbyEntry row, a management station should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, an HSRP group number and a cHsrpExtIfStandbyIndex should be chosen
        	**type**\: list of  		 :py:class:`Chsrpextifstandbyentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextifstandbytable.Chsrpextifstandbyentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CISCOHSRPEXTMIB.Chsrpextifstandbytable, self).__init__()

            self.yang_name = "cHsrpExtIfStandbyTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cHsrpExtIfStandbyEntry", ("chsrpextifstandbyentry", CISCOHSRPEXTMIB.Chsrpextifstandbytable.Chsrpextifstandbyentry))])
            self._leafs = OrderedDict()

            self.chsrpextifstandbyentry = YList(self)
            self._segment_path = lambda: "cHsrpExtIfStandbyTable"
            self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextifstandbytable, [], name, value)


        class Chsrpextifstandbyentry(Entity):
            """
            The cHsrpExtIfStandbyEntry allows an HSRP group
            interface to track one or more standby interfaces.
            
            To create a new cHsrpExtIfStandbyEntry row, a
            management station should choose the ifIndex of
            the interface which is to be added as part of an
            HSRP group. Also, an HSRP group number and a
            cHsrpExtIfStandbyIndex should be chosen.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CISCOHSRPMIB.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextifstandbyindex  (key)
            
            	This object defines the index of the standby table
            	**type**\: int
            
            	**range:** 1..4
            
            .. attribute:: chsrpextifstandbydestaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbyDestAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: chsrpextifstandbydestaddr
            
            	This object specifies the destination IP address of the standby router
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbysourceaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbySourceAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: chsrpextifstandbysourceaddr
            
            	This object specifies the source IP address of the standby router
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbyrowstatus
            
            	The control that allows modification, creation, and deletion of entries. Entries may not be created via SNMP without explicitly setting cHsrpExtIfStandbyRowStatus to either 'createAndGo' or 'createAndWait'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CISCOHSRPEXTMIB.Chsrpextifstandbytable.Chsrpextifstandbyentry, self).__init__()

                self.yang_name = "cHsrpExtIfStandbyEntry"
                self.yang_parent_name = "cHsrpExtIfStandbyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','chsrpgrpnumber','chsrpextifstandbyindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('chsrpgrpnumber', YLeaf(YType.str, 'cHsrpGrpNumber')),
                    ('chsrpextifstandbyindex', YLeaf(YType.uint32, 'cHsrpExtIfStandbyIndex')),
                    ('chsrpextifstandbydestaddrtype', YLeaf(YType.enumeration, 'cHsrpExtIfStandbyDestAddrType')),
                    ('chsrpextifstandbydestaddr', YLeaf(YType.str, 'cHsrpExtIfStandbyDestAddr')),
                    ('chsrpextifstandbysourceaddrtype', YLeaf(YType.enumeration, 'cHsrpExtIfStandbySourceAddrType')),
                    ('chsrpextifstandbysourceaddr', YLeaf(YType.str, 'cHsrpExtIfStandbySourceAddr')),
                    ('chsrpextifstandbyrowstatus', YLeaf(YType.enumeration, 'cHsrpExtIfStandbyRowStatus')),
                ])
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextifstandbyindex = None
                self.chsrpextifstandbydestaddrtype = None
                self.chsrpextifstandbydestaddr = None
                self.chsrpextifstandbysourceaddrtype = None
                self.chsrpextifstandbysourceaddr = None
                self.chsrpextifstandbyrowstatus = None
                self._segment_path = lambda: "cHsrpExtIfStandbyEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[cHsrpGrpNumber='" + str(self.chsrpgrpnumber) + "']" + "[cHsrpExtIfStandbyIndex='" + str(self.chsrpextifstandbyindex) + "']"
                self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfStandbyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextifstandbytable.Chsrpextifstandbyentry, ['ifindex', 'chsrpgrpnumber', 'chsrpextifstandbyindex', 'chsrpextifstandbydestaddrtype', 'chsrpextifstandbydestaddr', 'chsrpextifstandbysourceaddrtype', 'chsrpextifstandbysourceaddr', 'chsrpextifstandbyrowstatus'], name, value)


    class Chsrpextiftable(Entity):
        """
        HSRP\-specific configurations for each physical interface.
        
        .. attribute:: chsrpextifentry
        
        	If HSRP entries on this interface must use the BIA (Burned In Address), there must be an entry for the interface in this  table. Entries of this table are only accessible if HSRP has  been enabled i.e entries can not be created if HSRP is not enabled. Also, the interfaces should be of IEEE 802 ones (Ethernet, Token Ring, FDDI,VLAN, LANE, TR\-LANE).  Setting cHsrpExtIfRowStatus to active initiates the entry with default value for cHsrpExtIfUseBIA as FALSE. The value of cHsrpExtIfRowStatus may be set to destroy at any time. If the row is not initiated, it is similar to having cHsrpExtIfUseBIA as FALSE.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of  		 :py:class:`Chsrpextifentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CISCOHSRPEXTMIB.Chsrpextiftable.Chsrpextifentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CISCOHSRPEXTMIB.Chsrpextiftable, self).__init__()

            self.yang_name = "cHsrpExtIfTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cHsrpExtIfEntry", ("chsrpextifentry", CISCOHSRPEXTMIB.Chsrpextiftable.Chsrpextifentry))])
            self._leafs = OrderedDict()

            self.chsrpextifentry = YList(self)
            self._segment_path = lambda: "cHsrpExtIfTable"
            self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextiftable, [], name, value)


        class Chsrpextifentry(Entity):
            """
            If HSRP entries on this interface must use the BIA (Burned
            In Address), there must be an entry for the interface in this 
            table. Entries of this table are only accessible if HSRP has 
            been enabled i.e entries can not be created if HSRP is not
            enabled. Also, the interfaces should be of IEEE 802 ones
            (Ethernet, Token Ring, FDDI,VLAN, LANE, TR\-LANE).
            
            Setting cHsrpExtIfRowStatus to active initiates the
            entry with default value for cHsrpExtIfUseBIA as FALSE.
            The value of cHsrpExtIfRowStatus may be set to destroy
            at any time. If the row is not initiated, it is similar to
            having cHsrpExtIfUseBIA as FALSE.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: chsrpextifusebia
            
            	If set to TRUE, the HSRP Group MAC Address for all groups on this  interface will be the burned\-in\-address. Otherwise, this will be determined by ciscoHsrpGroupNumber. In case of sub\-interfaces, UseBIA applies to all sub\-interfaces on an  interface and to all groups on those sub\-interfaces
            	**type**\: bool
            
            .. attribute:: chsrpextifrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CISCOHSRPEXTMIB.Chsrpextiftable.Chsrpextifentry, self).__init__()

                self.yang_name = "cHsrpExtIfEntry"
                self.yang_parent_name = "cHsrpExtIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('chsrpextifusebia', YLeaf(YType.boolean, 'cHsrpExtIfUseBIA')),
                    ('chsrpextifrowstatus', YLeaf(YType.enumeration, 'cHsrpExtIfRowStatus')),
                ])
                self.ifindex = None
                self.chsrpextifusebia = None
                self.chsrpextifrowstatus = None
                self._segment_path = lambda: "cHsrpExtIfEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOHSRPEXTMIB.Chsrpextiftable.Chsrpextifentry, ['ifindex', 'chsrpextifusebia', 'chsrpextifrowstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOHSRPEXTMIB()
        return self._top_entity


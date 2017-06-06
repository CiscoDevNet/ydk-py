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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoHsrpExtMib(object):
    """
    
    
    .. attribute:: chsrpextifstandbytable
    
    	A table containing information about standby interfaces per HSRP group
    	**type**\:   :py:class:`Chsrpextifstandbytable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextifstandbytable>`
    
    .. attribute:: chsrpextiftable
    
    	HSRP\-specific configurations for each physical interface
    	**type**\:   :py:class:`Chsrpextiftable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftable>`
    
    .. attribute:: chsrpextiftrackedtable
    
    	A table containing information about tracked interfaces per HSRP group
    	**type**\:   :py:class:`Chsrpextiftrackedtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftrackedtable>`
    
    .. attribute:: chsrpextsecaddrtable
    
    	A table containing information about secondary HSRP IP Addresses per interface and group
    	**type**\:   :py:class:`Chsrpextsecaddrtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextsecaddrtable>`
    
    

    """

    _prefix = 'CISCO-HSRP-EXT-MIB'
    _revision = '2010-09-02'

    def __init__(self):
        self.chsrpextifstandbytable = CiscoHsrpExtMib.Chsrpextifstandbytable()
        self.chsrpextifstandbytable.parent = self
        self.chsrpextiftable = CiscoHsrpExtMib.Chsrpextiftable()
        self.chsrpextiftable.parent = self
        self.chsrpextiftrackedtable = CiscoHsrpExtMib.Chsrpextiftrackedtable()
        self.chsrpextiftrackedtable.parent = self
        self.chsrpextsecaddrtable = CiscoHsrpExtMib.Chsrpextsecaddrtable()
        self.chsrpextsecaddrtable.parent = self


    class Chsrpextiftrackedtable(object):
        """
        A table containing information about tracked interfaces per
        HSRP group.
        
        .. attribute:: chsrpextiftrackedentry
        
        	Each row of this table allows the tracking of one interface of the HSRP group which is identified by the (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause. Weight(priority) is given to each and every interface tracked.  When a tracked interface is unavailable, the HSRP priority of the router is decreased. i.e cHsrpGrpPriority value assigned  to an HSRP group will reduce by the value assigned to cHsrpExtIfTrackedPriority. This reduces the likelihood  of a router with a failed key interface becoming the  active router.  Setting cHsrpExtIfTrackedRowStatus to active starts the tracking of cHsrpExtIfTracked by the HSRP group.  The value of cHsrpExtIfTrackedRowStatus may be set  to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfTrackedRowStatus to either 'createAndGo'  or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row entry in the cHsrpExtIfTrackedTable can not be created unless the corresponding row in the cHsrpGrpTable has been  created. If that corresponding row in cHsrpGrpTable is  deleted, the interfaces it tracks also get deleted.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of    :py:class:`Chsrpextiftrackedentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            self.parent = None
            self.chsrpextiftrackedentry = YList()
            self.chsrpextiftrackedentry.parent = self
            self.chsrpextiftrackedentry.name = 'chsrpextiftrackedentry'


        class Chsrpextiftrackedentry(object):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextiftracked  <key>
            
            	The ifIndex value of the tracked interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: chsrpextiftrackedipnone
            
            	This object specifies the disable HSRP IPv4 virtual IP address
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: chsrpextiftrackedpriority
            
            	Priority of the tracked interface for the corresponding { ifIndex, cHsrpGrpNumber } pair. In the range of 0 to 255, 0 is the lowest priority and 255 is the highest. When a tracked  interface is unavailable, the cHsrpGrpPriority of the router  is decreased by the value of this object instance (If the  cHsrpGrpPriority is less than the  cHsrpExtIfTrackedPriority, then the HSRP priority  becomes 0). This allows a standby router to be configured  with a priority such that if the currently active router's  priority is lowered because the tracked interface goes down,  the standby router can takeover
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: chsrpextiftrackedrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfTrackedEntry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextiftracked = None
                self.chsrpextiftrackedipnone = None
                self.chsrpextiftrackedpriority = None
                self.chsrpextiftrackedrowstatus = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.chsrpgrpnumber is None:
                    raise YPYModelError('Key property chsrpgrpnumber is None')
                if self.chsrpextiftracked is None:
                    raise YPYModelError('Key property chsrpextiftracked is None')

                return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfTrackedTable/CISCO-HSRP-EXT-MIB:cHsrpExtIfTrackedEntry[CISCO-HSRP-EXT-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-HSRP-EXT-MIB:cHsrpGrpNumber = ' + str(self.chsrpgrpnumber) + '][CISCO-HSRP-EXT-MIB:cHsrpExtIfTracked = ' + str(self.chsrpextiftracked) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.chsrpgrpnumber is not None:
                    return True

                if self.chsrpextiftracked is not None:
                    return True

                if self.chsrpextiftrackedipnone is not None:
                    return True

                if self.chsrpextiftrackedpriority is not None:
                    return True

                if self.chsrpextiftrackedrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
                return meta._meta_table['CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfTrackedTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpextiftrackedentry is not None:
                for child_ref in self.chsrpextiftrackedentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
            return meta._meta_table['CiscoHsrpExtMib.Chsrpextiftrackedtable']['meta_info']


    class Chsrpextsecaddrtable(object):
        """
        A table containing information about secondary HSRP IP
        Addresses per interface and group.
        
        .. attribute:: chsrpextsecaddrentry
        
        	The CHsrpExtSecAddrEntry allows creation of secondary IP Addresses for each cHsrpGrpEntry row.  Secondary addresses can be added by setting  cHsrpExtSecAddrRowStatus to be active. The value of cHsrpExtSecAddrRowStatus may be set to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtSecAddrRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout.  Before creation of a cHsrpExtSecAddrEntry row, either cHsrpGrpConfiguredVirtualIpAddr or  cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address. This is because a secondary ip address cannot be created unless the primary ip address has already been set.  To create a new cHsrpExtSecAddrEntry row, a management  station should choose the ifIndex of the interface which is to  be added as part of an HSRP group. Also, an HSRP group number  and a cHsrpExtSecAddrAddress should be chosen.  Deleting a {ifIndex, cHsrpGrpNumber} row in the cHsrpGrpTable will delete all corresponding rows in the cHsrpExtSecAddrTable. Deleting a primary address value in the cHsrpGrpEntry row will delete all secondary addresses for the same {ifIndex, cHsrpGrpNumber} pair
        	**type**\: list of    :py:class:`Chsrpextsecaddrentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            self.parent = None
            self.chsrpextsecaddrentry = YList()
            self.chsrpextsecaddrentry.parent = self
            self.chsrpextsecaddrentry.name = 'chsrpextsecaddrentry'


        class Chsrpextsecaddrentry(object):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextsecaddraddress  <key>
            
            	A secondary IpAddress for the {ifIndex, cHsrpGrpNumber} pair. As explained in the DESCRIPTION for cHsrpExtSecAddrEntry, a primary address must exist before a secondary address for  the same {ifIndex, cHsrpGrpNumber} pair can be created
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpextsecaddrrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtSecAddrEntry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextsecaddraddress = None
                self.chsrpextsecaddrrowstatus = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.chsrpgrpnumber is None:
                    raise YPYModelError('Key property chsrpgrpnumber is None')
                if self.chsrpextsecaddraddress is None:
                    raise YPYModelError('Key property chsrpextsecaddraddress is None')

                return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtSecAddrTable/CISCO-HSRP-EXT-MIB:cHsrpExtSecAddrEntry[CISCO-HSRP-EXT-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-HSRP-EXT-MIB:cHsrpGrpNumber = ' + str(self.chsrpgrpnumber) + '][CISCO-HSRP-EXT-MIB:cHsrpExtSecAddrAddress = ' + str(self.chsrpextsecaddraddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.chsrpgrpnumber is not None:
                    return True

                if self.chsrpextsecaddraddress is not None:
                    return True

                if self.chsrpextsecaddrrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
                return meta._meta_table['CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtSecAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpextsecaddrentry is not None:
                for child_ref in self.chsrpextsecaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
            return meta._meta_table['CiscoHsrpExtMib.Chsrpextsecaddrtable']['meta_info']


    class Chsrpextifstandbytable(object):
        """
        A table containing information about standby
        interfaces per HSRP group.
        
        .. attribute:: chsrpextifstandbyentry
        
        	The cHsrpExtIfStandbyEntry allows an HSRP group interface to track one or more standby interfaces.  To create a new cHsrpExtIfStandbyEntry row, a management station should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, an HSRP group number and a cHsrpExtIfStandbyIndex should be chosen
        	**type**\: list of    :py:class:`Chsrpextifstandbyentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            self.parent = None
            self.chsrpextifstandbyentry = YList()
            self.chsrpextifstandbyentry.parent = self
            self.chsrpextifstandbyentry.name = 'chsrpextifstandbyentry'


        class Chsrpextifstandbyentry(object):
            """
            The cHsrpExtIfStandbyEntry allows an HSRP group
            interface to track one or more standby interfaces.
            
            To create a new cHsrpExtIfStandbyEntry row, a
            management station should choose the ifIndex of
            the interface which is to be added as part of an
            HSRP group. Also, an HSRP group number and a
            cHsrpExtIfStandbyIndex should be chosen.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextifstandbyindex  <key>
            
            	This object defines the index of the standby table
            	**type**\:  int
            
            	**range:** 1..4
            
            .. attribute:: chsrpextifstandbydestaddr
            
            	This object specifies the destination IP address of the standby router
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbydestaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbyDestAddr
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: chsrpextifstandbyrowstatus
            
            	The control that allows modification, creation, and deletion of entries. Entries may not be created via SNMP without explicitly setting cHsrpExtIfStandbyRowStatus to either 'createAndGo' or 'createAndWait'
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: chsrpextifstandbysourceaddr
            
            	This object specifies the source IP address of the standby router
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbysourceaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbySourceAddr
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.chsrpgrpnumber = None
                self.chsrpextifstandbyindex = None
                self.chsrpextifstandbydestaddr = None
                self.chsrpextifstandbydestaddrtype = None
                self.chsrpextifstandbyrowstatus = None
                self.chsrpextifstandbysourceaddr = None
                self.chsrpextifstandbysourceaddrtype = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.chsrpgrpnumber is None:
                    raise YPYModelError('Key property chsrpgrpnumber is None')
                if self.chsrpextifstandbyindex is None:
                    raise YPYModelError('Key property chsrpextifstandbyindex is None')

                return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfStandbyTable/CISCO-HSRP-EXT-MIB:cHsrpExtIfStandbyEntry[CISCO-HSRP-EXT-MIB:ifIndex = ' + str(self.ifindex) + '][CISCO-HSRP-EXT-MIB:cHsrpGrpNumber = ' + str(self.chsrpgrpnumber) + '][CISCO-HSRP-EXT-MIB:cHsrpExtIfStandbyIndex = ' + str(self.chsrpextifstandbyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.chsrpgrpnumber is not None:
                    return True

                if self.chsrpextifstandbyindex is not None:
                    return True

                if self.chsrpextifstandbydestaddr is not None:
                    return True

                if self.chsrpextifstandbydestaddrtype is not None:
                    return True

                if self.chsrpextifstandbyrowstatus is not None:
                    return True

                if self.chsrpextifstandbysourceaddr is not None:
                    return True

                if self.chsrpextifstandbysourceaddrtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
                return meta._meta_table['CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfStandbyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpextifstandbyentry is not None:
                for child_ref in self.chsrpextifstandbyentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
            return meta._meta_table['CiscoHsrpExtMib.Chsrpextifstandbytable']['meta_info']


    class Chsrpextiftable(object):
        """
        HSRP\-specific configurations for each physical interface.
        
        .. attribute:: chsrpextifentry
        
        	If HSRP entries on this interface must use the BIA (Burned In Address), there must be an entry for the interface in this  table. Entries of this table are only accessible if HSRP has  been enabled i.e entries can not be created if HSRP is not enabled. Also, the interfaces should be of IEEE 802 ones (Ethernet, Token Ring, FDDI,VLAN, LANE, TR\-LANE).  Setting cHsrpExtIfRowStatus to active initiates the entry with default value for cHsrpExtIfUseBIA as FALSE. The value of cHsrpExtIfRowStatus may be set to destroy at any time. If the row is not initiated, it is similar to having cHsrpExtIfUseBIA as FALSE.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of    :py:class:`Chsrpextifentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            self.parent = None
            self.chsrpextifentry = YList()
            self.chsrpextifentry.parent = self
            self.chsrpextifentry.name = 'chsrpextifentry'


        class Chsrpextifentry(object):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpextifrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfEntry
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: chsrpextifusebia
            
            	If set to TRUE, the HSRP Group MAC Address for all groups on this  interface will be the burned\-in\-address. Otherwise, this will be determined by ciscoHsrpGroupNumber. In case of sub\-interfaces, UseBIA applies to all sub\-interfaces on an  interface and to all groups on those sub\-interfaces
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.chsrpextifrowstatus = None
                self.chsrpextifusebia = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfTable/CISCO-HSRP-EXT-MIB:cHsrpExtIfEntry[CISCO-HSRP-EXT-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.chsrpextifrowstatus is not None:
                    return True

                if self.chsrpextifusebia is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
                return meta._meta_table['CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/CISCO-HSRP-EXT-MIB:cHsrpExtIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.chsrpextifentry is not None:
                for child_ref in self.chsrpextifentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
            return meta._meta_table['CiscoHsrpExtMib.Chsrpextiftable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.chsrpextifstandbytable is not None and self.chsrpextifstandbytable._has_data():
            return True

        if self.chsrpextiftable is not None and self.chsrpextiftable._has_data():
            return True

        if self.chsrpextiftrackedtable is not None and self.chsrpextiftrackedtable._has_data():
            return True

        if self.chsrpextsecaddrtable is not None and self.chsrpextsecaddrtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_HSRP_EXT_MIB as meta
        return meta._meta_table['CiscoHsrpExtMib']['meta_info']


